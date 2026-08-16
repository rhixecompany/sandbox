# Hook Event Payloads

> **Verified wire shape (Hermes v0.20.0, 2026-08-08).** Shell hooks receive a
> normalized envelope — NOT the raw kwargs. All event-specific kwargs land
> under `extra`. `cwd` is always the hook process working directory.
> Identity fields (`user`, `profile`, `provider`, `timestamp`) are NOT sent;
> resolve them locally (see `lib.py` helpers `resolve_user`, `resolve_profile`,
> `load_model_config`, `now_iso`).

## Envelope (every event)
```json
{
  "hook_event_name": "on_session_start",
  "tool_name": null,
  "tool_input": null,
  "session_id": "abc123",
  "cwd": "C:/Users/Alexa/Desktop/SandBox",
  "extra": {"model": "deepseek-v4-flash-free", "platform": "cli"}
}
```

## sessionStart (on_session_start)
```json
{
  "hook_event_name": "on_session_start",
  "session_id": "abc123",
  "cwd": "/home/user/project",
  "extra": {"model": "gpt-5-mini", "platform": "cli"}
}
```

## sessionEnd (on_session_end)
```json
{
  "hook_event_name": "on_session_end",
  "session_id": "abc123",
  "cwd": "/home/user/project",
  "extra": {
    "session_id": "abc123",
    "model": "gpt-5-mini",
    "platform": "cli",
    "completed": true,
    "failed": false,
    "interrupted": false,
    "turn_exit_reason": "completed"
  }
}
```

> **No metrics on the wire.** `on_session_end` never carries `duration_ms`,
> `turns`, `tokens_in/out`, `status`, or `exit_code`. Hooks must derive them
> locally: status from `extra.turn_exit_reason` / `extra.completed|failed|
> interrupted` (see `lib.resolve_end_status`), duration from the
> session_start record timestamp in the same session JSONL, turns by counting
> `pre_llm_call` rows (see `lib.duration_seconds_between`). Treat any future
> wire fields as explicit overrides.

## pre_llm_call
```json
{
  "hook_event_name": "pre_llm_call",
  "session_id": "abc123",
  "cwd": "/home/user/project",
  "extra": {
    "session_id": "abc123",
    "task_id": "t1",
    "turn_id": 3,
    "user_message": "Help me debug this TypeScript error",
    "is_first_turn": true,
    "model": "gpt-5-mini",
    "platform": "cli"
  }
}
```

## Field Descriptions
| Field | Type | Description |
|-------|------|-------------|
| `hook_event_name` | string | Event name (normalize with `event.strip().lower().replace("-", "_")`) |
| `session_id` | string | Unique session identifier |
| `cwd` | string | Hook process working directory (all events) |
| `extra` | object | Event-specific kwargs — read `extra.model`, `extra.platform`, `extra.user_message`, `extra.is_first_turn`, etc. |
| `tool_name` / `tool_input` | - | Only populated for `pre_tool_call`; null otherwise |
| `profile` | string | NOT sent; resolve via `resolve_profile()` / `HERMES_PROFILE` |
| `user` | string | NOT sent; resolve via `resolve_user()` |
| `provider` | string | NOT sent; resolve via `load_model_config()` -> `model.provider` |
| `timestamp` | string | NOT sent by shell-hooks bridge; use `now_iso()` |

## Parsing in Hook Script (Python, via lib.py)

```python
session_id = json_get(payload, "session_id", "unknown")
model = json_get(payload, "extra.model") or json_get(payload, "model") or "unknown"
working_dir = json_get(payload, "cwd") or json_get(payload, "working_dir") or ""
```