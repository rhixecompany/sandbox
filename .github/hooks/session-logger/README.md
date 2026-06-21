# session-logger

Unified session logging hook for `on_session_start`, `on_session_end`, and `pre_llm_call` events.

## Outputs

| File | Format | Purpose |
|------|--------|---------|
| `~/AppData/Local/hermes/logs/sessions/{session_id}.jsonl` | JSONL | Full session event log with input payload |
| `~/AppData/Local/hermes/logs/sessions/sessions.log` | Text | Compact one-line-per-event for SESSION_REPORT |
| `~/AppData/Local/hermes/logs/sessions/session_meta.json` | JSON | Latest event metadata for audit/verification |

## Event Schema

```json
{
  "event": "session_start|session_end|prompt|unknown",
  "session_id": "uuid",
  "profile": "default|code-architect|...",
  "model": "gpt-5.4-mini|...",
  "timestamp": "2026-06-21T...",
  "summary": "user prompt or event description",
  "input": "original stdin JSON (escaped)"
}
```

## Integration

- Calls `session-auto-commit/hook.sh` on `on_session_end` to regenerate `SESSION_REPORT.md`
- Compatible with Hermes hook protocol (stdin input, stdout `{}`)
- Set `HERMES_SESSION_ID`, `HERMES_PROFILE`, `HERMES_MODEL` env vars for explicit context

## Testing

```bash
# Simulate session start
echo '{"session_id":"test-123","profile":"default","model":"gpt-5.4-mini"}' | ./hook.sh on_session_start

# Simulate prompt
echo '{"prompt":"test message"}' | ./hook.sh pre_llm_call

# Simulate session end
echo '{"summary":"session complete"}' | ./hook.sh on_session_end
```