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

## Session Start Capture

The `on_session_start` handler performs a full start capture. The runtime
wire payload only carries `{hook_event_name, session_id, cwd, extra:{model,platform}}`,
so the hook resolves the missing identity/env fields itself (fails open):

| Field | Source |
|-------|--------|
| session_id | payload |
| timestamp | payload or now |
| profile | `HERMES_PROFILE` env → config → `default` |
| user | `USERNAME`/`USER` env → getpass |
| model | `extra.model` → config `model.default` |
| provider | `extra.provider` → config `model.provider` |
| platform | `extra.platform` |
| working_dir | payload `cwd` → `working_dir` |
| hostname, os, python | `platform_snapshot()` |
| git_branch, git_sha, git_dirty | best-effort `git -C <cwd>` snapshot |

The `pre_llm_call` handler records `prompt_length`/`prompt_summary` derived
from `extra.user_message` instead of unsent top-level fields.

## Skip

`SKIP_SESSION_LOGGER=true`
