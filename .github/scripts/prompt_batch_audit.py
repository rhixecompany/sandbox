#!/usr/bin/env python3
"""Batch audit/fix prompts under prompts/ according to enhance-markdown rules."""
import asyncio
from pathlib import Path
import yaml, re, sys


def audit(p):
    issues = []
    txt = p.read_text(encoding='utf-8', errors='ignore')
    if not txt.startswith('---'):
        issues.append('missing_frontmatter')
        return issues
    m = re.match(r'---\r?\n(.*?)\r?\n---\r?\n', txt, re.S)
    if not m:
        issues.append('malformed_frontmatter')
        return issues
    try:
        data = yaml.safe_load(m.group(1)) or {}
    except Exception as e:
        issues.append(f'yaml_error:{e}')
        return issues
    if not isinstance(data, dict):
        issues.append('frontmatter_not_dict')
        return issues
    for key in ['name', 'title', 'tags', 'version', 'author', 'license']:
        if key not in data or data[key] is None:
            issues.append(f'missing_{key}')
    tags = data.get('tags')
    if not tags and 'empty_tags' not in issues:
        issues.append('empty_tags')
    tail = txt[m.end():m.end()+600]
    if '---##' in tail or '|---##' in tail:
        issues.append('merged_yaml_close')
    return issues


def summarize(p, issues):
    return {
        'file': str(p),
        'issues': issues,
    }


async def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('prompts')
    mode = sys.argv[2] if len(sys.argv) > 2 else 'audit'
    files = sorted(root.rglob('*.md')) if root.is_dir() else [root]

    results = []
    for p in files:
        issues = audit(p)
        if issues:
            results.append(summarize(p, issues))

    print(f'audited={len(files)} issues={len(results)}')
    for r in results[:50]:
        print(r['file'] + ' :: ' + ','.join(r['issues']))


if __name__ == '__main__':
    asyncio.run(main())
