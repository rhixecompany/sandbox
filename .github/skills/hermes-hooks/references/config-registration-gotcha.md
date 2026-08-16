# Hooks Config Registration Gotcha

## Problem

Hooks written to `~/AppData/Local/hermes/hooks/` are silently ignored if not registered in `~/AppData/Local/hermes/config.yaml` under the `hooks:` key.

## Symptom

- Hook scripts exist and are executable
- `hermes hooks list` shows "No shell hooks configured"
- Session start/end does not trigger hooks

## Root Cause

Hermes loads hooks from config.yaml, not by filesystem discovery. The directory structure alone is insufficient.

## Fix

After creating hooks, register them in config.yaml:

```yaml
hooks:
  session-logger:
    enabled: true
    path: C:\Users\Alexa\AppData\Local\hermes\hooks\session-logger
  session-auto-commit:
    enabled: true
    path: C:\Users\Alexa\AppData\Local\hermes\hooks\session-auto-commit
  governance-audit:
    enabled: true
    path: C:\Users\Alexa\AppData\Local\hermes\hooks\governance-audit
```

Verify with:
```bash
grep -A 20 "hooks:" $LOCALAPPDATA/hermes/config.yaml
hermes hooks list
```

## Config.yaml Empty Gotcha

`~/AppData/Local/hermes/config.yaml` may appear empty (0 bytes) but `hermes config show` still displays runtime config. This is because Hermes merges:
1. Hardcoded defaults
2. Environment variables
3. Config file values

An empty config.yaml means "use defaults" — it does NOT mean "no config." Always use `hermes config show` to verify actual runtime state.

## Quick Restore (Full Hook Tree)

```bash
# 1. Create directories
mkdir -p $LOCALAPPDATA/hermes/hooks/{session-logger,session-auto-commit,governance-audit}
mkdir -p $LOCALAPPDATA/hermes/logs/hermes/governance

# 2. Write hooks.json for each
for hook in session-logger session-auto-commit governance-audit; do
  echo "{\"name\":\"$hook\",\"events\":[\"on_session_start\",\"on_session_end\"],\"script\":\"main.sh\"}" \
    > $LOCALAPPDATA/hermes/hooks/$hook/hooks.json
done

# 3. Make scripts executable
for dir in session-logger session-auto-commit governance-audit; do
  chmod +x $LOCALAPPDATA/hermes/hooks/$dir/*.sh 2>/dev/null
done

# 4. Register in config.yaml (use hermes config edit)

# 5. Verify
hermes hooks list
echo '{}' | bash $LOCALAPPDATA/hermes/hooks/session-logger/log-session-start.sh
```