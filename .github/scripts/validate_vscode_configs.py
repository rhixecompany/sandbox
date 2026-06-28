import os
import json
from pathlib import Path

WORKSPACE = Path(r"C:/Users/Alexa/Desktop/SandBox/projects")
report = []
errors = []

for repo in sorted(WORKSPACE.iterdir()):
    if not repo.is_dir():
        continue
    vscode = repo / '.vscode'
    if not vscode.exists():
        continue
    entry = {'repo': repo.name, 'files': [], 'formatter_conflicts': []}
    # validate JSON files
    for f in vscode.glob('*.json'):
        rel = f.name
        try:
            # settings.json may be JSONC but our templates are strict JSON; attempt load
            with open(f, 'r', encoding='utf-8') as fh:
                data = json.load(fh)
            entry['files'].append({'file': rel, 'valid': True})
            # check formatter conflicts in settings.json
            if rel == 'settings.json' and isinstance(data, dict):
                formatters = {}
                for k,v in data.items():
                    if k.startswith('[') and isinstance(v, dict) and 'editor.defaultFormatter' in v:
                        lang = k.strip('[]')
                        fmt = v['editor.defaultFormatter']
                        if lang in formatters and formatters[lang] != fmt:
                            entry['formatter_conflicts'].append({'language': lang, 'first': formatters[lang], 'second': fmt})
                        formatters[lang] = fmt
        except Exception as e:
            entry['files'].append({'file': rel, 'valid': False, 'error': str(e)})
            errors.append(f"{repo.name}/{rel}: {e}")
    report.append(entry)

# print concise summary
for r in report:
    print(f"{r['repo']}: {len(r['files'])} json files checked")
    for f in r['files']:
        status = 'OK' if f['valid'] else 'INVALID'
        print(f"  - {f['file']}: {status}")
    if r['formatter_conflicts']:
        print('  Formatter conflicts:')
        for c in r['formatter_conflicts']:
            print(f"    - {c['language']}: {c['first']} vs {c['second']}")

if errors:
    print('\nErrors found:')
    for e in errors:
        print(' -', e)
else:
    print('\nAll JSON files parsed successfully; no formatter conflicts detected in checked settings.json files.')
