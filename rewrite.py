#!/usr/bin/env python3
# SPDX-License-Identifier: CC-BY-SA-4.0
"""Generate one local rewrite per record; save candidates for source review."""
import argparse
import json
import re
import time
import urllib.request
from collections import Counter
from pathlib import Path

INSTRUCTION = '''Rewrite this university discussion in plain, natural English. Retain every argument, fact, name, tool, technical term, number, qualification and testing condition. Keep actual experiences distinct from proposals. Do not invent opinions, details or experiences. Keep first person where it occurs in the source. Use the simplest accurate words and grammatical sentences. Keep roughly the source length. Do not include commentary, an introduction or a conclusion that the source does not contain. Return only the full rewritten discussion.'''

def post(server, endpoint, body):
    request=urllib.request.Request(server.rstrip('/')+endpoint,data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(request,timeout=300) as response:
        return json.load(response)

def prompt(source, style=None):
    instruction=INSTRUCTION
    if style:
        instruction+='\n\nThe following is an older sample by the writer. Follow its sentence habits and vocabulary only. Do not import its facts, names, opinions or experiences into the new discussion.\n<voice_reference>\n'+style[:2800]+'\n</voice_reference>'
    return [{'role':'user','content':instruction+'\n\n<source>\n'+source+'\n</source>'}]

def checks(source, text):
    issues=[]
    numbers=lambda x:Counter(re.findall(r'\d+(?:,\d{3})*(?:\.\d+)?%?',x))
    if numbers(source)!=numbers(text):issues.append('number_tokens_changed')
    if len(text.split())<len(source.split())*.5:issues.append('possible_major_omission')
    if 'written permission' in source.lower() and 'written permission' not in text.lower():issues.append('check_written_permission')
    if re.search(r'\bfictional\b',source,re.I) and not re.search(r'\bfictional\b',text,re.I):issues.append('synthetic_provenance_omitted')
    return issues

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path,help='TXT or JSONL with id and text fields')
    parser.add_argument('output',type=Path,help='New output directory')
    parser.add_argument('--style',type=Path,help='Your own writing sample; omit for direct mode')
    parser.add_argument('--server',default='http://127.0.0.1:8085')
    args=parser.parse_args()
    if args.output.exists() and any(args.output.iterdir()):
        parser.error('Choose an empty output directory to preserve earlier candidates.')
    args.output.mkdir(parents=True,exist_ok=True)
    style=args.style.read_text(encoding='utf-8') if args.style else None
    records=[json.loads(line) for line in args.input.read_text(encoding='utf-8').splitlines() if line.strip()] if args.input.suffix.lower()=='.jsonl' else [{'id':args.input.stem,'text':args.input.read_text(encoding='utf-8')}]
    for index,record in enumerate(records,1):
        source=record['text'].strip()
        formatted=post(args.server,'/apply-template',{'messages':prompt(source,style),'add_generation_prompt':True})['prompt']
        if '<start_of_turn>user' not in formatted or not formatted.rstrip().endswith('<start_of_turn>model'):
            raise ValueError('Unexpected chat template: use the documented Gemma 2 model.')
        settings={'n_predict':1100,'temperature':.8,'top_p':.95,'top_k':40,'min_p':.05,'repeat_penalty':1.05,'seed':42}
        started=time.perf_counter()
        result=post(args.server,'/completion',{'prompt':formatted,**settings})
        text=result['content'].strip()
        stop_type=result.get('stop_type')
        stopped_limit=result.get('stopped_limit')
        if stopped_limit is None and stop_type is not None:stopped_limit=stop_type=='limit'
        issues=checks(source,text)
        if stopped_limit:issues.append('generation_limit_reached')
        if result.get('truncated'):issues.append('context_was_truncated')
        output={'id':record['id'],'source':source,'text':text,'mode':'voice' if style else 'plain','status':'candidate_needs_source_review','settings':settings,'prompt':formatted,'seconds':round(time.perf_counter()-started,2),'checks':issues,'stopped_limit':stopped_limit,'stop_type':stop_type,'context_truncated':result.get('truncated'),'timings':result.get('timings')}
        (args.output/f'{index:03d}.json').write_text(json.dumps(output,indent=2,ensure_ascii=False),encoding='utf-8')
        (args.output/f'{index:03d}.txt').write_text(text,encoding='utf-8')
        print(json.dumps({'id':record['id'],'words':len(text.split()),'seconds':output['seconds'],'checks':output['checks'],'stopped_limit':output['stopped_limit']}),flush=True)

if __name__=='__main__':main()
