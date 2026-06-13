import os, re, sys, json
from collections import Counter
home = os.environ.get('USERPROFILE') or '/c/Users/Alexa'
skill_dir = os.path.join(home, 'AppData', 'Local', 'hermes', 'skills')
print('SCAN_ROOT', skill_dir)
counts = Counter()
missing = {'missing_when': [], 'missing_wf': [], 'missing_vc': [], 'missing_bp': [], 'h1_code': []}
for root, dirs, files in os.walk(skill_dir):
    if 'SKILL.md' not in files:
        continue
    path = os.path.join(root, 'SKILL.md')
    rel = path.replace(skill_dir, '').lstrip('/\\').replace('\\', '/')
    try:
        content = open(path, 'r', encoding='utf-8', errors='replace').read()
    except Exception as e:
        print('READ_ERR', rel, e, file=sys.stderr)
        continue
    counts['total'] += 1
    if re.search(r'^## When to (Use|use)\b', content, re.MULTILINE):
        counts['when'] += 1
    else:
        missing['missing_when'].append(rel)
    wf_pattern = r'^## (Workflow|Process|Pipeline|Phases|The Process|Decision Flow)\b'
    if re.search(wf_pattern, content, re.MULTILINE):
        counts['wf'] += 1
    else:
        missing['missing_wf'].append(rel)
    if '## Verification Checklist' in content or '## Checklist' in content:
        counts['vc'] += 1
    else:
        missing['missing_vc'].append(rel)
    if re.search(r'^## Best Practices', content, re.MULTILINE):
        counts['bp'] += 1
    else:
        missing['missing_bp'].append(rel)
    code_blocks = re.findall(r'```[\s\S]*?```', content)
    for cb in code_blocks:
        if re.search(r'^# ', cb, re.MULTILINE):
            counts['h1_code'] += 1
            missing['h1_code'].append(rel)
            break
print('\nSKILL_AUDIT_SUMMARY')
for k in ('total','when','wf','vc','bp','h1_code'):
    print(f'{k}: {counts[k]}')
print('MISSING_WHEN', len(missing['missing_when']))
print('MISSING_WORKFLOW', len(missing['missing_wf']))
print('MISSING_CHECKLIST', len(missing['missing_vc']))
print('MISSING_BP', len(missing['missing_bp']))
print('H1_CODE_BLOCKS', len(missing['h1_code']))
for k in ('missing_when','missing_wf','missing_vc','missing_bp','h1_code'):
    print('\n###', k, len(missing[k]))
    for s in missing[k][:20]:
        print('-', s)
