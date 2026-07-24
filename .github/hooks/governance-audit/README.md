# governance-audit

Audits Hermes session events and LLM prompts for governance signals.

## Live Files

- `hooks.json` — event map and entrypoint
- `README.md` — this file
- `hook.sh` — shell wrapper
- `hook.py` — async Python entrypoint
- `audit-session-start.sh` — deprecated legacy static event script
- `audit-session-end.sh` — deprecated legacy static event script
- `audit-prompt.sh` — deprecated legacy static event script

## Events

- `on_session_start`
- `on_session_end`
- `pre_llm_call`

## Logs

- `C:/Users/Alexa/AppData/Local/hermes/logs/hermes/governance/<session_id>.jsonl`
- Deprecated fallback: `C:/Users/Alexa/AppData/Local/hermes/logs/audit/<session_id>.jsonl`

## Skip

`SKIP_GOVERNANCE_AUDIT=true`
