# Source: https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks

# Event Hooks

Hermes has three hook systems that run custom code at key lifecycle points:

| System | Registered via | Runs in | Use case |
| --- | --- | --- | --- |
| **Gateway hooks** | `HOOK.yaml` + `handler.py` in `~/AppData/Local/hermes/hooks/` | Gateway only | Logging, alerts, webhooks |
| **Plugin hooks** | `ctx.register_hook()` in a [plugin](/docs/user-guide/features/plugins) | CLI + Gateway | Tool interception, metrics, guardrails |
| **Shell hooks** | `hooks:` block in `~/AppData/Local/hermes/config.yaml` pointing at shell scripts | CLI + Gateway | Drop-in scripts for blocking, auto-formatting, context injection |

`HOOK.yaml`, `handler.py`, `~/AppData/Local/hermes/hooks/`, `ctx.register_hook()`, `hooks:`, `~/AppData/Local/hermes/config.yaml`

All three systems are non-blocking — errors in any hook are caught and logged, never crashing the agent.

## Gateway Event Hooks

Gateway hooks fire automatically during gateway operation (Telegram, Discord, Slack, WhatsApp, Teams) without blocking the main agent pipeline.

### Creating a Hook

Each hook is a directory under `~/AppData/Local/hermes/hooks/` containing two files:

```
~/AppData/Local/hermes/hooks/
 └── my-hook/
  ├── HOOK.yaml # Declares which events to listen for
  └── handler.py # Python handler function
```

#### HOOK.yaml

```yaml
name: my-hook
description: Log all agent activity to a file
events:
 - agent:start
 - agent:end
 - agent:step
```

The `events` list determines which events trigger your handler. You can subscribe to any combination of events, including wildcards like `command:*`.

#### handler.py

```python
import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path.home() / ".hermes" / "hooks" / "my-hook" / "activity.log"

async def handle(event_type: str, context: dict):
    """Called for each subscribed event. Must be named 'handle'."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "event": event_type,
        **context,
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
```

**Handler rules:** `handle`, `event_type`, `context`, `async def`, `def`

### Available Events

| Event | When it fires | Context keys |
| --- | --- | --- |
| `gateway:startup` | Gateway process starts | `platforms` (list of active platform names) |
| `session:start` | New messaging session created | `platform`, `user_id`, `session_id`, `session_key` |
| `session:end` | Session ended (before reset) | `platform`, `user_id`, `session_key` |
| `session:reset` | User ran `/new` or `/reset` | `platform`, `user_id`, `session_key` |
| `agent:start` | Agent begins processing a message | `platform`, `user_id`, `session_id`, `message` |
| `agent:step` | Each iteration of the tool-calling loop | `platform`, `user_id`, `session_id`, `iteration`, `tool_names` |
| `agent:end` | Agent finishes processing | `platform`, `user_id`, `session_id`, `message`, `response` |
| `command:*` | Any slash command executed | `platform`, `user_id`, `command`, `args` |

#### Wildcard Matching

Handlers registered for `command:*` fire for any `command:` event (`command:model`, `command:reset`, etc.). Monitor all slash commands with a single subscription.

### Examples

#### Telegram Alert on Long Tasks

Send yourself a message when the agent takes more than 10 steps:

```yaml
# ~/AppData/Local/hermes/hooks/long-task-alert/HOOK.yaml
name: long-task-alert
description: Alert when agent is taking many steps
events:
 - agent:step
```

```python
# ~/AppData/Local/hermes/hooks/long-task-alert/handler.py
import os
import httpx

THRESHOLD = 10
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_HOME_CHANNEL")

async def handle(event_type: str, context: dict):
    iteration = context.get("iteration", 0)
    if iteration == THRESHOLD and BOT_TOKEN and CHAT_ID:
        tools = ", ".join(context.get("tool_names", []))
        text = f"⚠️ Agent has been running for {iteration} steps. Last tools: {tools}"
        async with httpx.AsyncClient() as client:
            await client.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                json={"chat_id": CHAT_ID, "text": text},
            )
```

---

## Plugin Hooks

Plugin hooks run in both CLI and Gateway. Use `ctx.register_hook()` inside a plugin's `register(ctx)` function.

| Hook Point | When | Signature |
| --- | --- | --- |
| `pre_tool_call` | Before tool executes | `def hook(tool_name: str, params: dict, ctx: PluginContext)` |
| `post_tool_call` | After tool executes | `def hook(tool_name: str, params: dict, result: Any, ctx: PluginContext)` |
| `pre_llm_call` | Before LLM request | `def hook(model: str, messages: list, kwargs: dict, ctx: PluginContext)` |
| `post_llm_call` | After LLM response | `def hook(model: str, messages: list, response: Any, ctx: PluginContext)` |
| `on_session_start` | New session | `def hook(session_id: str, platform: str, ctx: PluginContext)` |
| `on_session_end` | Session ends | `def hook(session_id: str, platform: str, ctx: PluginContext)` |

---

## Shell Hooks

Shell hooks are configured in `~/AppData/Local/hermes/config.yaml` and run as subprocesses with JSON stdin/stdout.

```yaml
hooks:
  - name: my-shell-hook
    events:
      - "pre_tool_call"
    command: "python"
    args:
      - "~/AppData/Local/hermes/hooks/my-shell-hook/handler.py"
    timeout: 5
```

The hook receives a JSON payload on stdin:
```json
{
  "event_type": "pre_tool_call",
  "context": {
    "tool_name": "terminal",
    "params": {"command": "ls"}
  }
}
```

Hook must return valid JSON on stdout (or nothing). Non-zero exit codes are logged but don't block the agent.