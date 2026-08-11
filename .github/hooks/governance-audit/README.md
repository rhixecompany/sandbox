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
`user` (env → getpass), `model`/`provider`/`platform` (from `extra` or
config), `working_dir` (payload `cwd`), plus best-effort git state
(`git_branch`, `git_sha`, `git_dirty`). All resolution fails open — a missing
value never fails the hook.

## Session End Capture

The `on_session_end` handler writes a full end record with the same derivation
contract as session-logger: `status` comes from
`extra.turn_exit_reason` → `extra.status` → completion booleans and is
normalized to `completed`/`failed`/`interrupted`/`truncated`;
`duration_ms`/`duration_seconds` come from wire overrides or are derived from
the session_start record timestamp; `turns` is the count of `pre_llm_call`
records in the session JSONL; `exit_code` is a wire override or `1` when the
status is `failed`. Identity/host/git fields match the start record so every
end record is self-contained.

## Skip

`SKIP_GOVERNANCE_AUDIT=true`
