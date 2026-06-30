from pathlib import Path
import re, json
from datetime import datetime

ROOT = Path('/c/Users/Alexa/Desktop/SandBox/prompts')
OUT = Path('/c/Users/Alexa/Desktop/SandBox/docs/prompt-inventory.md')


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = re.sub(r'-{2,}', '-', text).strip('-')
    return text[:40] or 'prompt'


files = sorted(ROOT.glob('**/*.prompt.md'))
results = []
for p in files:
    rel = str(p.relative_to(ROOT))
    text = p.read_text(encoding='utf-8')
    issues: list[str] = []
    meta = {
        'file': rel,
        'stem': p.stem,
        'size_bytes': p.stat().st_size,
        'modified': datetime.fromtimestamp(p.stat().st_mtime).isoformat(),
    }
    # detect frontmatter block boundaries
    opens = [m.start() for m in re.finditer(r'(?m)^(---|\.\.\.)\s*$', text)]
    closes = [m.start() for m in re.finditer(r'(?m)^(---|\.\.\.)\s*$', text[3:])]
    # simpler rule: first boundary and second boundary
    boundaries = [m.start() for m in re.finditer(r'(?m)^(---|\.\.\.)\s*$', text)]
    if not boundaries:
        issues.append('missing_frontmatter_delimiter')
        yaml = ''
    else:
        frontmatter_end = boundaries[1] if len(boundaries) > 1 else text.find('\n', 3)
        yaml = text[boundaries[0]:frontmatter_end]
        if len(boundaries) < 2:
            issues.append('missing_frontmatter_close')
        # malformed extra fence near top
        if '---##' in text[:max(frontmatter_end, 1)]:
            issues.append('merged_or_bad_fence')

    def has(pattern: str) -> bool:
        return re.search(pattern, yaml, flags=re.MULTILINE) is not None

    def val(pat: str):
        m = re.search(pat, yaml, flags=re.MULTILINE)
        return m.group(1).strip().strip('"').strip("'") if m else ''

    for key in ['name', 'title', 'description', 'version', 'license', 'author']:
        if not has(rf'(?m)^{re.escape(key)}\s*:'):
            issues.append(f'missing_{key}')

    tag_match = re.search(r'(?m)^tags:\s*(?:\[\s*\]|-\s+\S+)', yaml)
    if tag_match is None:
        issues.append('tags_invalid')

    version = val(r'(?m)^version:\s*(.+)')
    if version and not re.fullmatch(r'(0|[1-9]\d*)\.(0|[1-9]\d*)(?:\.(0|[1-9]\d*))?(?:[-+.][0-9A-Za-z.-]+)?', version):
        issues.append('version_not_semver')

    trigger = val(r'(?m)^trigger:\s*(.+)')
    if trigger != p.stem:
        issues.append(f'trigger_mismatch:{trigger or "(blank)"} != {p.stem}')

    tags = re.findall(r'(?m)^\s*-\s+(.+)$', yaml)
    tags = [t.strip().strip('"').strip("'") for t in tags]
    if len(tags) != len(set(tags)):
        issues.append('duplicate_tags')
    body = text if 'yaml' not in dir() else text[frontmatter_end:] if 'frontmatter_end' in dir() else text
    if 'frontmatter_end' in dir() and not re.match(r'^(?:\s*#+.*\n|\s*$)', body):
        issues.append('leading_body_not_heading')
    meta.update({
        'name': val(r'(?m)^name:\s*(.+)') or p.stem,
        'title': val(r'(?m)^title:\s*(.+)'),
        'trigger': trigger,
        'tags': tags,
        'issues': issues,
        'valid': not issues,
    })
    results.append(meta)

summary = {
    'timestamp': datetime.now().isoformat(),
    'total': len(results),
    'valid': sum(1 for r in results if r['valid']),
    'invalid': sum(1 for r in results if not r['valid']),
    'issues_by_type': {},
    'invalid_files': [r['file'] for r in results if not r['valid']],
    'results': results,
}
for r in results:
    for i in r['issues']:
        summary['issues_by_type'][i] = summary['issues_by_type'].get(i, 0) + 1

lines = [
    '# Prompt Inventory',
    '',
    f'Last updated: {summary["timestamp"]}',
    '',
    f'Total: {summary["total"]} | Valid: {summary["valid"]} | Invalid: {summary["invalid"]}',
    '',
    '## Issues by type',
    '',
    '| Issue | Count |',
    '|-------|-------|',
]
for k, v in sorted(summary['issues_by_type'].items()):
    lines.append(f'| {k} | {v} |')
lines += [
    '',
    '## Invalid files',
    '',
    '| File | Issues |',
    '|------|--------|',
]
for r in results:
    if not r['valid']:
        lines.append(f'| {r["file"]} | {", ".join(r["issues"])} |')
lines += ['', '## All files', '', '| File | Name | Title | Trigger | Tags | Valid | Issues |', '|------|------|-------|---------|------|--------|---------|']
for r in results:
    lines.append(f'| {r["file"]} | {r["name"]} | {r["title"]} | {r["trigger"]} | {", ".join(r["tags"])} | {"yes" if r["valid"] else "no"} | {", ".join(r["issues"])} |')
OUT.write_text('\n'.join(lines), encoding='utf-8')
print(json.dumps(summary, ensure_ascii=False, indent=2))
