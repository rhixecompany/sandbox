# Hook end-status normalization (verified 2026-08-11)

## Symptom

Live `session_end` records in `logs/sessions/<id>.jsonl` carried
`status: "text_response(finish_reason=stop)"` — a Python-ish repr, useless
for reporting. This was the one real quality gap after the 2026-08-08
wire-shape fix.

## Root cause

The runtime serializes the final TurnResponse object into
`extra.turn_exit_reason`. It is NOT a bare status token. Observed values:

| Raw wire value (`extra.turn_exit_reason`) | Normalized |
|---|---|
| `text_response(finish_reason=stop)` | `completed` |
| `text_response(finish_reason=tool_calls)` | `completed` |
| `text_response(finish_reason=length)` | `truncated` |
| `agent_error(exception=TimeoutError)` | `failed` |
| `interrupted(user_interrupt)` | `interrupted` |

Early docs and fixtures showed the idealized `"turn_exit_reason":"completed"`
shape — that is NOT what production sends.

## Fix

`lib.normalize_status(raw)` in `%LOCALAPPDATA%/hermes/hooks/lib.py`:

1. empty -> `unknown`
2. lowercases, expands `_` / `(` / `)` to spaces
3. `finish reason=stop` -> `completed`; `finish reason=length` -> `truncated`
4. starts with `text response` or `tool call` -> `completed`
5. contains `interrupt` / `cancel` / `abort` -> `interrupted`
6. contains `error` / `fail` / `exception` -> `failed`
7. small direct vocabulary (`success`, `succeeded`, `stop`, `error`, ...)
   via `_STATUS_VOCAB`
8. anything else -> returned VERBATIM (no signal loss)

`lib.resolve_end_status(payload)` applies it automatically; hooks must never
store `extra.turn_exit_reason` raw. Resolution order: `turn_exit_reason` ->
`extra.status` -> `extra.completed|failed|interrupted` booleans -> `unknown`.

## Doctor allowlist quirk (companion insight)

`hermes hooks doctor` hashes the `hook.sh` entrypoint command strings in
config.yaml — NOT the content of `lib.py` or `hook.py` bodies. Python-internal
changes (adding helpers, rewriting handlers) do NOT trigger
"script changed since approval"; doctor stays green. Only editing `hook.sh`
or the config `hooks:` command strings forces re-approval. Use this to
predict whether a hook edit needs an approval step.

## Verification pattern

Fire realistic end payloads through the live `hook.sh` wrapper using a
real-looking `session_id` (never `test*`/`e2e-*` — hooks skip synthetic ids),
then delete the JSONL from `logs/sessions/`, `logs/hermes/governance/`, and
`logs/audit/`. Payload harness lives in `testing-hooks.md`.