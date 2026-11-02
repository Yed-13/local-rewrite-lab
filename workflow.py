#!/usr/bin/env python3
# SPDX-License-Identifier: CC-BY-SA-4.0
"""Prepare natural text groups, create editable review copies, and reassemble text."""
import argparse
import json
import re
from pathlib import Path


def prepare(source, folder):
    if folder.exists() and any(folder.iterdir()):
        raise ValueError('Use a new job directory')
    text = source.read_text(encoding='utf-8')
    blocks = [s.strip() for s in re.split(r'\n\s*\n', text) if s.strip()]
    entries, groups, pending = [], [], []
    end_matter = fenced = False

    def flush():
        if not pending:
            return
        identifier = f'section-{len(groups)+1:03d}'
        joined = '\n\n'.join(pending)
        groups.append({'id': identifier, 'text': joined})
        entries.append({'id': identifier, 'kind': 'rewrite', 'text': joined})
        pending.clear()

    for block in blocks:
        if block.casefold() in {'references', 'bibliography', 'works cited', 'ai disclosure', 'ai use disclosure'}:
            end_matter = True
        heading = len(block.split()) <= 12 and not re.search(r'[.!?;:]$', block)
        retained = end_matter or heading or block.startswith(('>', '|', '```')) or fenced
        if '```' in block and block.count('```') % 2:
            fenced = not fenced
        if retained:
            flush()
            entries.append({'kind': 'retained', 'text': block})
        else:
            if len(block.split()) > 320:
                raise ValueError('A paragraph exceeds 320 words; divide it at a natural sentence boundary before preparing')
            if sum(len(s.split()) for s in pending) + len(block.split()) > 320:
                flush()
            pending.append(block)
    flush()
    if not groups:
        raise ValueError('No body prose found')
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'document.json').write_text(json.dumps(entries, indent=2, ensure_ascii=False))
    (folder / 'sections.jsonl').write_text(''.join(json.dumps(g, ensure_ascii=False) + '\n' for g in groups))
    print(f'{len(groups)} groups; {sum(e["kind"]=="retained" for e in entries)} retained blocks')


def review(run, folder, original_plan=None):
    if folder.exists() and any(folder.iterdir()):
        raise ValueError('Use a new review directory')
    records = [json.loads(p.read_text()) for p in sorted(run.glob('[0-9][0-9][0-9].json'))]
    if not records:
        raise ValueError('No candidate JSON files found')
    folder.mkdir(parents=True, exist_ok=True)
    index = {}
    comparison = []
    originals = {e['id']: e['text'] for e in json.loads(original_plan.read_text()) if e['kind'] == 'rewrite'} if original_plan else {}
    for i, r in enumerate(records, 1):
        filename = f'{i:03d}.txt'
        (folder / filename).write_text(r['text'], encoding='utf-8')
        index[r['id']] = filename
        original = originals.get(r['id'], r['source'])
        comparison.append(f'## {r["id"]}\n\nOriginal\n\n{original}\n\nStage input\n\n{r["source"]}\n\nCandidate\n\n{r["text"]}\n')
    (folder / 'index.json').write_text(json.dumps(index, indent=2))
    (folder / 'comparison.md').write_text('\n'.join(comparison))
    print('Edit the review TXT copies against the source before assembling')


def assemble(plan, reviewed, output, overlay=None):
    if output.exists():
        raise FileExistsError(output)
    entries = json.loads(plan.read_text())
    index = json.loads((reviewed / 'index.json').read_text())
    overrides = json.loads((overlay / 'index.json').read_text()) if overlay else {}
    if set(overrides) - set(index):
        raise ValueError('Overlay IDs do not match this document')
    parts = []
    for e in entries:
        if e['kind'] == 'retained':
            text = e['text']
        elif e['id'] in overrides:
            text = (overlay / overrides[e['id']]).read_text()
        else:
            text = (reviewed / index[e['id']]).read_text()
        if not text.strip():
            raise ValueError('Reviewed prose must not be empty')
        parts.append(text.strip())
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text('\n\n'.join(parts) + '\n', encoding='utf-8')
    print(output)


def tail(plan, reviewed, output, count):
    if output.exists():
        raise FileExistsError(output)
    if count < 1:
        raise ValueError('groups must be positive')
    entries = [e for e in json.loads(plan.read_text()) if e['kind'] == 'rewrite']
    index = json.loads((reviewed / 'index.json').read_text())
    records = [{'id': e['id'], 'text': (reviewed / index[e['id']]).read_text().strip()} for e in entries[-count:]]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in records))
    print(f'{len(records)} selected groups')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    a = sub.add_parser('prepare'); a.add_argument('source', type=Path); a.add_argument('job', type=Path)
    a = sub.add_parser('review'); a.add_argument('run', type=Path); a.add_argument('folder', type=Path); a.add_argument('--original-plan', type=Path)
    a = sub.add_parser('assemble'); a.add_argument('plan', type=Path); a.add_argument('reviewed', type=Path); a.add_argument('output', type=Path); a.add_argument('--overlay', type=Path)
    a = sub.add_parser('tail'); a.add_argument('plan', type=Path); a.add_argument('reviewed', type=Path); a.add_argument('output', type=Path); a.add_argument('--groups', type=int, default=2)
    a = p.parse_args()
    if a.command == 'prepare': prepare(a.source, a.job)
    elif a.command == 'review': review(a.run, a.folder, a.original_plan)
    elif a.command == 'tail': tail(a.plan, a.reviewed, a.output, a.groups)
    else: assemble(a.plan, a.reviewed, a.output, a.overlay)


if __name__ == '__main__':
    main()
