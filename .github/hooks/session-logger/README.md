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

## Session End Capture

The `on_session_end` handler performs a full end capture. The runtime wire
payload only carries `{hook_event_name, session_id, cwd, extra:{completed,
failed, interrupted, turn_exit_reason, model, platform}}` — it never sends
`duration_ms`, `turns`, `tokens_*`, or `status`. The handler therefore derives
those locally:

| Field | Source |
|-------|--------|
| session_id | payload |
| timestamp | payload or now |
| status | `extra.turn_exit_reason` → `extra.status` → `extra.completed/failed/interrupted` booleans → `unknown`; raw repr values (e.g. `text_response(finish_reason=stop)`) are normalized via `lib.normalize_status` to `completed` / `failed` / `interrupted` / `truncated` |
| duration_seconds | payload `duration_seconds` override → computed from the session_start record timestamp in the same JSONL |
| duration_ms | payload `duration_ms` override → derived duration × 1000 |
| turns | payload `turns` override → count of `pre_llm_call` records in the same JSONL |
| tokens_in / tokens_out | payload override if ever sent, else 0 |
| exit_code | payload override → 1 when status is `failed`, else 0 |
| user / profile / model / provider / platform / working_dir | same resolution chain as start capture |
| hostname, os, python | `platform_snapshot()` |
| git_branch, git_sha, git_dirty | best-effort `git -C <cwd>` snapshot |

Every end record is therefore self-contained and useful even though the
runtime sends no metrics — status is real, duration and turns are derived from
the accumulated session log, and identity/host/git context matches the start
record.

## Skip

`SKIP_SESSION_LOGGER=true`
