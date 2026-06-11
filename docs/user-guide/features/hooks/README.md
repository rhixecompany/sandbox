# Hermes Agent Hooks — Comprehensive Summary

> **Source:** https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks

---

## Overview

Hooks allow you to run custom logic at specific points in the Hermes Agent lifecycle. They're implemented as executable scripts that receive JSON input via stdin and return JSON output via stdout.

---

## Built-in Hooks

| Hook | Events | Purpose | Skip Flag |
|------|--------|---------|-----------|
| **session-logger** | on_session_start, on_session_end, pre_llm_call | Log session activity | `SKIP_LOGGING=true` |
| **session-auto-commit** | on_session_end | Auto-commit changes | `SKIP_AUTO_COMMIT=true` |
| **governance-audit** | on_session_start, on_session_end, pre_llm_call | Threat detection | `SKIP_GOVERNANCE_AUDIT=true` |

---

## Hook Locations

| Artifact | Path |
|----------|------|
| Hook scripts | `~/.hermes/hooks/<name>/` |
| Hook logs | `~/.hermes/logs/hermes/` |
| Hook config | `config.yaml` → `hooks: {}` |

---

## Hook Script Rules

1. **Always use `jq -c` for compact JSON output**
2. **Use `awk "BEGIN {exit !($a > $b)}"` for float comparison** (never `bc` + `(( ))`)
3. **Always support a SKIP flag** (e.g., `SKIP_LOGGING=true`)
4. **Use absolute paths in `hooks.json`**
5. **Log to `logs/hermes/`, never `logs/copilot/`**

---

## Hook Configuration (`config.yaml`)

```yaml
hooks:
  session-logger:
    enabled: true
    events: [on_session_start, on_session_end, pre_llm_call]
    script: "~/.hermes/hooks/session-logger/hook.sh"
  
  session-auto-commit:
    enabled: true
    events: [on_session_end]
    script: "~/.hermes/hooks/session-auto-commit/hook.sh"
  
  governance-audit:
    enabled: true
    events: [on_session_start, on_session_end, pre_llm_call]
    script: "~/.hermes/hooks/governance-audit/hook.sh"
```

---

## Event Payloads

### on_session_start
```json
{
  "event": "on_session_start",
  "session_id": "abc123",
  "timestamp": "2026-01-15T10:30:00Z",
  "reason": "new_session"
}
```

### on_session_end
```json
{
  "event": "on_session_end",
  "session_id": "abc123",
  "timestamp": "2026-01-15T11:45:00Z",
  "completed": true,
  "interrupted": false,
  "reason": "conversation_complete"
}
```

### pre_llm_call
```json
{
  "event": "pre_llm_call",
  "session_id": "abc123",
  "turn_id": "turn-7",
  "timestamp": "2026-01-15T10:35:00Z",
  "user_message": "Help me debug this TypeScript error",
  "is_first_turn": false,
  "model": "nvidia/nemotron-3-ultra:free"
}
```

---

## Creating Custom Hooks

### 1. Create Hook Directory
```bash
mkdir -p ~/.hermes/hooks/my-hook
```

### 2. Write Hook Script (`hook.sh`)
```bash
#!/usr/bin/env bash
set -euo pipefail

# Read JSON from stdin
input=$(cat)

# Check skip flag
skip_var="SKIP_MY_HOOK"
if [[ "${!skip_var:-}" == "true" ]]; then
  echo '{"status": "skipped"}'
  exit 0
fi

# Parse event
event=$(echo "$input" | jq -r '.event')

  case "$event" in
  on_session_start)
    # Your logic here
    echo '{"status": "ok"}'
    ;;
  pre_llm_call)
    prompt=$(echo "$input" | jq -r '.user_message // .prompt')
    # Your logic here
    echo '{"status": "ok"}'
    ;;
  *)
    echo '{"status": "ignored"}'
    ;;
esac
```

### 3. Make Executable
```bash
chmod +x ~/.hermes/hooks/my-hook/hook.sh
```

### 4. Register in `config.yaml`
```yaml
hooks:
  my-hook:
    enabled: true
    events: [on_session_start, pre_llm_call]
    script: "~/.hermes/hooks/my-hook/hook.sh"
```

---

## Hook Development Tips

### Testing Locally
```bash
# Simulate event
echo '{"event":"on_session_start","session_id":"test","timestamp":"2026-01-15T10:30:00Z","reason":"new_session"}' | ~/.hermes/hooks/my-hook/hook.sh
```

### Logging
```bash
# Append to hook-specific log
log_file=~/.hermes/logs/hermes/my-hook.log
echo "$(date -Iseconds) $event" >> "$log_file"
```

### Error Handling
```bash
# Return error status (agent will log but continue)
echo '{"status": "error", "message": "hook failed: ..."}' >&2
exit 1
```

---

## Common Hook Patterns

### 1. Audit Trail
Log all prompts and responses for compliance.

### 2. Auto-Formatting
Run formatters on file changes at session end.

### 3. Cost Tracking
Accumulate token usage per session/project.

### 4. Security Scanning
Inspect prompts for secrets, PII, injection attempts.

### 5. Notification Bridge
Send session summaries to Slack, Discord, email.

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Hook not firing | Check `config.yaml` events list; verify script path |
| Script fails silently | Check `~/.hermes/logs/hermes/` for stderr |
| JSON parse error | Ensure script outputs valid JSON; use `jq -c` |
| Skip flag not working | Verify env var name matches `SKIP_<HOOK_NAME>` pattern |
| Permission denied | `chmod +x ~/.hermes/hooks/<name>/hook.sh` |

---

## Advanced: Hook Chaining

Multiple hooks can listen to the same event — they execute in config order. Each receives the original event payload (not previous hook's output).

---

**Source:** [Hermes Agent Docs - Hooks](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks)  
**Extracted:** 2026-06-08
