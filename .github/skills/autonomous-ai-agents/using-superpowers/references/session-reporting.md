# Session Reporting — Reference

This reference accompanies the `using-superpowers` skill and documents the small, repeatable pattern used in this workspace to keep session history available and to regenerate SESSION_REPORT.md on session boundaries.

What it does
- Write compact JSON session event files to %LOCALAPPDATA%/hermes/logs/hermes/ (fields: event, session_id, profile, model, when)
- On session end (or optionally session start), run a verified report generation script that reads session dumps under %LOCALAPPDATA%/hermes/sessions and writes a compact rolling-summary markdown report at the workspace root (~/Desktop/SandBox/SESSION_REPORT.md)

Hook snippet (POSIX shell)

1) session-logger/hook.sh (writes event + triggers auto-commit)
- Writes last_session_event.json into the log dir
- Calls session-auto-commit/hook.sh with the same payload

2) session-auto-commit/hook.sh
- Parses incoming JSON meta
- Reads the last N session dumps (default N=41) from %LOCALAPPDATA%/hermes/sessions
- Writes a compact SESSION_REPORT.md at the specified REPORT_PATH

Verification
- Simulate: echo '{"event":"session_start","session_id":"TEST"}' | bash session-logger/hook.sh
- Verify: cat %LOCALAPPDATA%/hermes/logs/hermes/last_session_event.json and ~/Desktop/SandBox/SESSION_REPORT.md

Pitfalls & workarounds
- If Python isn't available in the hook execution environment, use a shell-only generator: use head/tail/jq and sed/awk to extract first lines from session dumps and write the markdown file.
- If hooks run under a different user or inside a container, ensure paths are adjusted and writable. Prefer writing to a configurable path, not a hardcoded Desktop path.

Files added
- references/session-reporting.md — this file
