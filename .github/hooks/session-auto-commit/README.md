# session-auto-commit

Auto-commits SESSION_REPORT.md on `on_session_end` event. Reads rolling session log,
generates a 41-session summary, and commits if the file changed.

## Behavior

1. Reads `~/AppData/Local/hermes/logs/sessions/sessions.log`
2. Generates `~/Desktop/SandBox/SESSION_REPORT.md` with last 41 sessions (most recent first)
3. Writes `session_meta_latest.json` for audit trail
4. If in a git repo and file changed, commits with message: `chore(session-report): update rolling 41-session summary`

## Usage

Called automatically by `session-logger/hook.sh` on session end. Can be invoked manually:

```bash
./hook.sh /custom/path/SESSION_REPORT.md
```

## Testing

```bash
# Generate report from existing logs
./hook.sh /tmp/test_report.md
cat /tmp/test_report.md
```