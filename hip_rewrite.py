#!/usr/bin/env python3
# SPDX-License-Identifier: CC-BY-SA-4.0
"""Generate independent HIP candidates for source review; TXT or JSONL input."""
import argparse
import json
import re
import time
import urllib.request
from collections import Counter
from pathlib import Path


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('input',type=Path)
    p.add_argument('output',type=Path)
    p.add_argument('--server',default='http://127.0.0.1:8083')
    p.add_argument('--seed',type=int,default=42)
    args=p.parse_args()
    records=[json.loads(s) for s in args.input.read_text().splitlines() if s.strip()] if args.input.suffix.lower()=='.jsonl' else [{'id':args.input.stem,'text':args.input.read_text()}]
    for r in records:
        if not r['text'].strip() or len(r['text'].split())>320:p.error('Provide complete paragraph groups of 1–320 words; use JSONL for multiple groups.')
    if args.output.exists() and any(args.output.iterdir()):p.error('Use an empty output directory.')
    args.output.mkdir(parents=True,exist_ok=True)
    for i,r in enumerate(records,1):
        source=r['text'].strip();lead=r.get('lead','')
        prompt=f'<source_text>\n{source}\n</source_text>\n\n<target_text>\n{lead}'
        settings=dict(temperature=1.,top_p=.95,top_k=50,min_p=0.,repeat_penalty=1.,seed=r.get('seed',args.seed),n_predict=800,stop=['</target_text>'])
        started=time.perf_counter()
        req=urllib.request.Request(args.server.rstrip('/')+'/completion',data=json.dumps(dict(prompt=prompt,**settings)).encode(),headers={'Content-Type':'application/json'})
        with urllib.request.urlopen(req,timeout=300) as response:raw=json.load(response)
        text=(lead+raw['content']).strip();warnings=[]
        number_tokens=lambda s:Counter(re.findall(r'\d+(?:,\d{3})*(?:\.\d+)?%?',s))
        if number_tokens(source)!=number_tokens(text):warnings.append('number_tokens_changed')
        if raw.get('stop_type')=='limit' or raw.get('stopped_limit'):warnings.append('generation_limit_reached')
        if raw.get('truncated'):warnings.append('context_truncated')
        result=dict(id=r['id'],source=source,text=text,prompt=prompt,settings=settings,seconds=round(time.perf_counter()-started,2),status='candidate_needs_source_review',warnings=warnings,stop_type=raw.get('stop_type'),truncated=raw.get('truncated'))
        (args.output/f'{i:03d}.json').write_text(json.dumps(result,indent=2,ensure_ascii=False))
        (args.output/f'{i:03d}.txt').write_text(text)
        print(json.dumps(dict(id=r['id'],seconds=result['seconds'],warnings=warnings)),flush=True)

if __name__=='__main__':main()
