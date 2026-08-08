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

## Session Start Capture

The `on_session_start` handler mirrors the session-logger capture for the
governance audit trail: `session_id`, `timestamp`, `profile` (env → config),
`user` (env → getpass), `model`/`platform` (from `extra`), `working_dir`
(payload `cwd`), plus best-effort git state (`git_branch`, `git_sha`,
`git_dirty`). All resolution fails open — a missing value never fails the hook.

## Skip

`SKIP_GOVERNANCE_AUDIT=true`
