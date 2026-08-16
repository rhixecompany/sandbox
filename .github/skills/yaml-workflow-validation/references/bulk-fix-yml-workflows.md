# Bulk Fix YML/YAML Workflows — Reference Recipe

## Unified Python Fix Script

Run this via `execute_code` tool — handls CRLF, trailing spaces, and missing EOF newlines in one pass, correctly excluding node_modules, .venv, and cookiecutter Jinja dirs on Windows/MSYS.

```python
import os, subprocess

basedir = r"C:\path\to\workspace"
config = os.path.join(basedir, ".yamllint.yaml")

# Fix all YAML files
for root, dirs, files in os.walk(basedir):
    dirs[:] = [d for d in dirs if d not in ("node_modules", ".git", ".venv", "__pycache__", ".do")]
    if "{{cookiecutter" in root:
        continue
    for f in files:
        if not (f.endswith('.yml') or f.endswith('.yaml')):
            continue
        if f.endswith('.lock.yml') or f.endswith('.lock.yaml'):
            continue
        fp = os.path.join(root, f)
        # 1. CRLF → LF
        subprocess.run(["sed", "-i", "s/\\r$//", fp], capture_output=True)
        # 2. Trailing spaces
        subprocess.run(["sed", "-i", "s/[[:space:]]*$//", fp], capture_output=True)
        # 3. Missing trailing newline
        with open(fp, 'r') as fh:
            content = fh.read()
        if not content.endswith('\n'):
            with open(fp, 'a') as fh:
                fh.write('\n')
```

## CRLF Verification (Windows/MSYS)

Do NOT trust `od -c | grep \\r` — MSYS translates LF→CRLF at terminal output level. Use Python binary read:

```python
with open(fp, 'rb') as f:
    data = f.read()
print('CRLF present:', b'\\r\\n' in data)
print('Bare CR:', b'\\r' in data and b'\\r\\n' not in data)
```

## yamllint Config Template

```yaml
extends: relaxed

rules:
  line-length:
    max: 400
    level: error
  new-lines:
    type: unix
    level: error
  new-line-at-end-of-file:
    level: error
  trailing-spaces:
    level: error
  indentation:
    spaces: 2
    indent-sequences: consistent
    level: warning
  comments:
    min-spaces-from-content: 1
    level: warning

ignore: |
  *.lock.yml
  *.lock.yaml
  .venv/
```

## Full Sweep Verification

```python
import os, subprocess

failures = []
total = 0
config = r"C:\path\to\.yamllint.yaml"

for root, dirs, files in os.walk(basedir):
    dirs[:] = [d for d in dirs if d not in ("node_modules", ".git", ".venv", "__pycache__")]
    if "{{cookiecutter" in root:
        continue
    for f in files:
        if not (f.endswith('.yml') or f.endswith('.yaml')):
            continue
        if f.endswith('.lock.yml') or f.endswith('.lock.yaml'):
            continue
        fp = os.path.join(root, f)
        total += 1
        r = subprocess.run(["yamllint", "-c", config, fp], capture_output=True, text=True, timeout=10)
        if r.returncode != 0 or r.stdout.strip():
            failures.append(os.path.relpath(fp, basedir))

print(f"Total: {total}, Failures: {len(failures)}")
for f in failures:
    print(f"  FAIL: {f}")
if not failures:
    print("✅ ALL PASS")
```