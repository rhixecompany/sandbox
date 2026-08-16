# Verified Hook Cleanup Commands

Use these exact commands after creating an approval note in `.hermes/approvals/`.

```bash
# Inspect live hook state
hermes hooks list
hermes hooks doctor

# Inspect canonical hook tree
find "C:/Users/Alexa/AppData/Local/hermes/hooks" -maxdepth 2 -type f | sort

# Check wrapper scripts
HERMES_SCRIPTS="$LOCALAPPDATA/../Local/hermes/scripts"
for name in session-logger session-auto-commit governance-audit; do
  ls -la "$HERMES_SCRIPTS/$name" 2>/dev/null || echo "missing wrapper $name"
done

# Compare wrapper to canonical
for name in session-logger session-auto-commit governance-audit; do
  diff -u "$LOCALAPPDATA/../Local/hermes/scripts/$name" \
    "C:/Users/Alexa/AppData/Local/hermes/hooks/$name/hook.sh" || true
done

# Repo-local stale copies
ls -la .github/scripts/session-logger .github/scripts/session-auto-commit .github/scripts/governance-audit 2>/dev/null || true
```

## Cleanup Commands

```bash
# Remove repo wrapper copies
rm -f .github/scripts/session-logger \
      .github/scripts/session-auto-commit \
      .github/scripts/governance-audit

# Remove stale live wrappers
HERMES_SCRIPTS="$LOCALAPPDATA/../Local/hermes/scripts"
for name in session-logger session-auto-commit governance-audit; do
  rm -f "$HERMES_SCRIPTS/$name"
done

# Remove compiled Python caches from hook trees
HERMES_HOOKS="$LOCALAPPDATA/../Local/hermes/hooks"
for name in session-logger session-auto-commit governance-audit; do
  rm -rf "$HERMES_HOOKS/$name/__pycache__"
done
```

## Verification Sequence

```bash
hermes hooks list
hermes hooks doctor
grep -A 20 "^hooks:" "$LOCALAPPDATA/hermes/config.yaml"
```

## Temporary Ad-Hoc Verification Script

Save to `C:/Users/Alexa/AppData/Local/Temp/hermes-verify-hook-cleanup.py`, run with `python3`, then remove it after use.

```python
from pathlib import Path

LOCALAPPDATA = "C:/Users/Alexa/AppData/Local"
ROOT = Path("C:/Users/Alexa/Desktop/SandBox")
HOOKS = Path(LOCALAPPDATA) / "hermes" / "hooks"
SCRIPTS = ROOT / ".github" / "scripts"
LIVE_SCRIPTS = Path(LOCALAPPDATA) / "hermes" / "scripts"
CHECKS = []

def ok_or_fail(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    print(f"{status}\t{name}{(' | ' + detail) if detail else ''}")
    CHECKS.append((name, condition))

for name in ("session-logger", "session-auto-commit", "governance-audit"):
    repo_paths = [SCRIPTS / name]
    repo_missing = not any(p.exists() for p in repo_paths)
    ok_or_fail(f"repo/{name}/removed", repo_missing, str(repo_paths) if not repo_missing else "")
    canonical = HOOKS / name / "hook.sh"
    ok_or_fail(f"canonical/{name}/hook.sh/exists", canonical.exists(), str(canonical))
    live = LIVE_SCRIPTS / name
    ok_or_fail(f"live/scripts/{name}/removed", not live.exists(), str(live) if live.exists() else "")
    meta = HOOKS / name / "hooks.json"
    ok_or_fail(f"hook/{name}/hooks.json/exists", meta.exists(), str(meta))
    pc = HOOKS / name / "__pycache__"
    ok_or_fail(f"hook/{name}/__pycache__/removed", not pc.exists(), str(pc) if pc.exists() else "")

if any(condition is False for _, condition in CHECKS):
    raise SystemExit("VERIFY_FAILED")
print("VERIFY_OK")
```
