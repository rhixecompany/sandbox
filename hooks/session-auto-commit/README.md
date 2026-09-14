# session-auto-commit

Auto-commits session changes to git at the end of a Hermes session.

## Live Files

- `hooks.json` — event map and entrypoint
- `README.md` — this file
- `hook.sh` — shell wrapper
- `hook.py` — async Python entrypoint
- `auto-commit.sh` — deprecated legacy shell script mapped to deprecated `session_end`

## Events

- `on_session_end`

## Skip

`SKIP_SESSION_AUTO_COMMIT=true`
