#!/usr/bin/env python3
"""Fix prompt metadata: remove duplicate external metadata blocks, then inject a single metadata block inside the first frontmatter."""
from pathlib import Path
import re

ROOT = Path('prompts')
FRONTMATTER_RE = re.compile(r'---\r?\n(.*?)\r?\n---\r?\n', re.S)
METADATA_BLOCK_RE = re.compile(r'^metadata:\r?\n(?:[ \t]+.*\r?\n)+', re.M)
CLEANUP_COUNT = 0
UPDATED_COUNT = 0
REMAINING = 0

for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or p.suffix != '.md' or 'templates' in p.parts or '_shared' in p.parts or p.parent.name == 'templates':
        continue
    text = p.read_text(encoding='utf-8', errors='ignore')
    match = FRONTMATTER_RE.match(text)
    if not match:
        continue

    fm_text = match.group(1)
    after = text[match.end():]
    metas = METADATA_BLOCK_RE.findall('\n' + after)

    if len(metas) > 1:
        cleaned = after
        for i, m in enumerate(metas):
            if i == 0:
                continue
            cleaned = cleaned.replace('\n' + m, '', 1)
        p.write_text(text[:match.end()] + cleaned, encoding='utf-8')
        text = text[:match.end()] + cleaned
        CLEANUP_COUNT += 1

    match = FRONTMATTER_RE.match(text)
    if not match:
        continue
    fm_text = match.group(1)
    after = text[match.end():]
    if 'metadata:' in fm_text:
        continue
    slug = p.stem.replace(' ', '-').replace('_', '-').lower()
    new_fm = fm_text + f'\nmetadata:\n  hermes:\n    related_skills: []\n    tags:\n    - {slug}\n'
    new_front = match.group(0).replace(match.group(1), new_fm, 1)
    p.write_text(new_front + after, encoding='utf-8')
    UPDATED_COUNT += 1

print(f'cleaned_duplicates={CLEANUP_COUNT}')
print(f'injected_metadata={UPDATED_COUNT}')

for p in sorted(ROOT.rglob('*.md')):
    if 'templates' in p.parts or '_shared' in p.parts or p.parent.name == 'templates':
        continue
    txt = p.read_text(encoding='utf-8', errors='ignore')
    m = FRONTMATTER_RE.match(txt)
    if not m:
        continue
    if 'metadata:' not in m.group(1):
        REMAINING += 1
print(f'remaining_missing={REMAINING}')
