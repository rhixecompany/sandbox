# Batch Frontmatter Field Retrofit

## Problem
Add one or more new frontmatter fields (`scripts`, `skills`, `formatter`, `plan`) to every `.prompt.md` file in a library (200+ files) without breaking existing structure.

## Approach
Use Python regex on the raw text to avoid YAML roundtrip issues (PyYAML normalizes list formatting and drops comments).

```python
import os, re

prompts_dir = "C:/path/to/prompts"
for fname in sorted(os.listdir(prompts_dir)):
    if not fname.endswith('.prompt.md'):
        continue
    path = os.path.join(prompts_dir, fname)
    with open(path, encoding='utf-8') as f:
        content = f.read()

    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        continue

    fm_block = m.group(1)
    body = content[m.end():]
    fm_lines = fm_block.split('\n')

    # Check which fields already exist
    has_field = {f: any(re.match(r'^' + f + ':', l) for l in fm_lines)
                 for f in ['scripts', 'skills', 'formatter', 'plan']}

    changes = []
    new_lines = list(fm_lines)

    # Trim trailing blanks
    while new_lines and new_lines[-1].strip() == '':
        new_lines.pop()

    if not has_field['scripts']:
        new_lines.append('scripts: []')
        changes.append('scripts')

    if not has_field['skills']:
        # Option A: infer from dependencies
        skills_from_deps = []
        for l in fm_lines:
            if l.strip().startswith('- skill:'):
                skills_from_deps.append(l.strip().replace('- skill:', '').strip())
        if skills_from_deps:
            new_lines.append('skills:')
            for s in skills_from_deps:
                new_lines.append(f'- {s}')
        else:
            new_lines.append('skills: []')
        changes.append('skills')

    if not has_field['formatter']:
        new_lines.append('formatter: default')
        changes.append('formatter')

    if not has_field['plan']:
        # Try to match plan by prompt name
        prompt_name = next((l.replace('name:', '').strip()
                           for l in fm_lines if l.strip().startswith('name:')), None)
        # ... fuzzy match against plan index ...
        new_lines.append('plan: ""')
        changes.append('plan')

    new_fm = '\n'.join(new_lines)
    new_content = f'---\n{new_fm}\n---\n{body}'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
```

## Verification
After the fix, run a scan against the required fields:

```python
pass_count = 0
fail_count = 0
for fname in files:
    with open(path) as f:
        content = f.read()
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    fm = m.group(1) if m else ''
    missing = [f for f in ['scripts', 'skills', 'formatter', 'plan']
               if not re.search(r'^' + f + ':', fm, re.MULTILINE)]
    if missing:
        fail_count += 1
    else:
        pass_count += 1
print(f"{pass_count} passed, {fail_count} failed")
```

## Pitfalls
- **Regex on multi-line YAML** — Simple `^field:` checks don't catch continuation lines. Only use for boolean presence (field exists vs doesn't). For value correctness, use `yaml.safe_load`.
- **Line number prefix from `read_file`** — Don't use `read_file` output for parsing. Use `open(path, encoding='utf-8')` directly.
- **read_file dedup cache** — After writing, a subsequent `read_file` may return stale content if the dedup cache thinks nothing changed. Force fresh with `wc -l` or re-open from terminal.
- **Empty skills vs inferred skills** — When a prompt has `dependencies:` with `skill:` entries, infer the `skills:` list from those. When it has neither, use `skills: []`.
- **Plan matching** — Simple substring matching between prompt `name:` and plan filenames works for most cases. Document mismatches for manual follow-up.
