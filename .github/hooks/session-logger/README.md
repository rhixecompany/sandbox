---
name: "Session Logger"
description: "Logs all Hermes coding agent session activity for audit and analysis"
tags: ["logging", "audit", "analytics", "hermes"]
---

# Session Logger Hook

Comprehensive logging for Hermes coding agent sessions, tracking session starts, ends, and user prompts for audit trails and usage analytics.

## Overview

This hook provides detailed logging of Hermes agent activity:

- Session start/end lifecycle events with working directory context
- Pre-LLM turn previews via the `user_message` payload
- Configurable log levels via `LOG_LEVEL` env var

## Hook Events

| Event | Script | Log File |
|-------|--------|----------|
| `on_session_start` | `log-session-start.sh` | `session.log` |
| `on_session_end` | `log-session-end.sh` | `session.log` |
| `pre_llm_call` | `log-prompt.sh` | `prompts.log` |

## Installation

1. Ensure scripts are executable:

   ```bash
   chmod +x C:/Users/Alexa/AppData/Local/hermes/hooks/session-logger/*.sh
   ```

2. Create the logs directory:

   ```bash
   mkdir -p C:/Users/Alexa/AppData/Local/hermes/logs/hermes
   ```

3. Register the hook in `config.yaml` under `hooks:` (currently uses standalone `hooks.json`).

## Log Format

JSON Lines format — one compact JSON object per line:

```json
{"timestamp":"2024-01-15T10:30:00Z","event":"on_session_start","cwd":"/workspace/project"}
{"timestamp":"2024-01-15T10:35:00Z","event":"on_session_end","completed":true}
{"timestamp":"2024-01-15T10:31:00Z","event":"pre_llm_call","level":"INFO"}
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `SKIP_LOGGING` | unset | Set to `true` to disable all logging |
| `LOG_LEVEL` | `INFO` | Log level for prompt events (INFO, DEBUG, ERROR) |

## Privacy & Security

- Add `logs/` to `.gitignore` to avoid committing session data
- Use `SKIP_LOGGING=true` to disable entirely
- Logs are stored locally only — no external calls

## Script Requirements (per hermes-hooks-manager)

- `set -euo pipefail` ✓
- `INPUT=$(cat)` ✓
- `jq -c` for compact JSON ✓
- `SKIP_LOGGING` env var support ✓
- Absolute log paths using `$HOME/AppData/Local/hermes/logs/hermes/` ✓

## Source

Built-in Hermes hook.
