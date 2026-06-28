# Skills Install Templates

This file contains templates for verification scripts and batch install wrappers used during large-scale skill operations.

## Batch installer template (Bash)
- See `references/batch-install.md` for a full example.

## Verification script (Python) — creates a JSON summary of installed skills
```python
import subprocess, json
skills = ["subagent-driven-development","watchers","scrapling"]
out = []
for s in skills:
    r = subprocess.run(["hermes","skills","inspect", s], capture_output=True, text=True)
    status = r.returncode
    out.append({"skill": s, "inspect_exit": status, "stdout": r.stdout[:1000]})
print(json.dumps(out, indent=2))
```

## Install wrapper (Bash) — safe pattern that uses full identifier and logs
```bash
#!/usr/bin/env bash
IDENTIFIER="$1"
LOG="$HOME/.hermes/ops/installs.log"
mkdir -p "$(dirname "$LOG")"
{
  echo "$(date -Iseconds) Installing $IDENTIFIER"
  if hermes skills install "$IDENTIFIER" --yes; then
    echo "OK"
  else
    echo "FAIL"
  fi
} >> "$LOG" 2>&1
```
