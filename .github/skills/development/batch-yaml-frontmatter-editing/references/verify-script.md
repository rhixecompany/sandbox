# Remediation Verify Script

Copy this into a temp file and run to verify frontmatter integrity after remediation:

```python
#!/usr/bin/env python3
import os, re, sys
from pathlib import Path

SKILLS = Path(os.environ.get("HOME","C:/Users/User")) / "AppData/Local/hermes/skills"
errors = []
count = 0

for skill in sorted(SKILLS.rglob("SKILL.md")):
    count += 1
    text = skill.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        errors.append(f"NO_FM:{skill}"); continue
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        errors.append(f"BROKEN:{skill}"); continue
    fm = m.group(1)
    if not re.search(r"^name:", fm, re.M):
        errors.append(f"NO_NAME:{skill}")
    if not re.search(r"^description:", fm, re.M):
        errors.append(f"NO_DESC:{skill}")

print(f"Verified: {count} skills")
print(f"Errors: {len(errors)}")
for e in errors:
    print(f"  FAIL: {e}")
sys.exit(1 if errors else 0)
```

## Edge case: code-sandbox paths
When running from `execute_code`, the tool's `read_file` triggers may hit the 50-call limit if scanning 600+ files. In that case:
- Use `terminal` with a bash one-liner instead
- Or scan a subset per run (first 200, next 200, etc.)
- Or use the Python `subprocess` approach directly from `execute_code` with a temp script

## Edge case: root-level duplicates
After remediation, verify no duplicate `skills/<name>/` + `skills/<category>/<name>/` pairs remain:
```bash
find "$HERMES_HOME/skills" -maxdepth 3 -name "SKILL.md" | \
  sed 's|.*/||' | sort | uniq -d
```
Any name appearing twice in the output is a duplicate candidate.
