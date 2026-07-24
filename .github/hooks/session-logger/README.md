# session-logger

Logs Hermes session lifecycle and prompt events into per-session JSONL files.

## Live Files

- `hooks.json` — event map and entrypoint
- `README.md` — this file
- `hook.sh` — shell wrapper
- `hook.py` — async Python entrypoint
- `log-session-start.sh` — deprecated legacy static event script
- `log-session-end.sh` — deprecated legacy static event script
- `log-prompt.sh` — deprecated legacy static event script

## Events

- `on_session_start`
- `on_session_end`
- `pre_llm_call`

## Logs

- `C:/Users/Alexa/AppData/Local/hermes/logs/sessions/<session_id>.jsonl`

## Skip

`SKIP_SESSION_LOGGER=true`
