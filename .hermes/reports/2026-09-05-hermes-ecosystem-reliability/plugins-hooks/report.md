# Plugin + Hook Audit Report

Generated: 2026-09-05T08:50:51.243995+00:00

## Summary
- Plugins found: 15
- With plugin.yaml: 12
- Possible events (Hermes source, shell + plugin): 13
- **Shell hooks registered** (config.yaml): 6
- Shell hooks COVERED: 5 of 13
- Shell hooks MISSING: 8 (events exist in code but no shell hook wired)

**Note:** Hermes supports two hook systems — **shell hooks** (config.yaml, run external scripts on lifecycle events) and **plugin hooks** (Python callbacks defined inside plugin code). The 6 shell hooks above are for `on_session_start/end`, `pre/post_tool_call`, `pre_llm_call`, `subagent_stop`. The 8 missing events (`on_stream_*`, `on_turn_complete`, `pre/post_api_request`, `pre_transform_response`, `post_llm_call`) are plugin-internal callbacks — they are dispatched to Python handlers in the hermes-agent process, not to external shell scripts. Shell-hook support for these events would require upstream code changes to expose a new emitter in `agent/shell_hooks.py`.

## Possible events (per Hermes source)
- `on_session_end`
- `on_session_start`
- `on_stream_delta`
- `on_stream_end`
- `on_stream_start`
- `on_turn_complete`
- `post_api_request`
- `post_llm_call`
- `post_tool_call`
- `pre_api_request`
- `pre_llm_call`
- `pre_tool_call`
- `pre_transform_response`

## Registered events (per config.yaml)
- `on_session_end` (3 hooks)
- `on_session_start` (2 hooks)
- `post_tool_call` (2 hooks)
- `pre_llm_call` (3 hooks)
- `pre_tool_call` (2 hooks)
- `subagent_stop` (2 hooks)

## Missing event coverage
- `on_stream_delta` — defined in source but no hook registered
- `on_stream_end` — defined in source but no hook registered
- `on_stream_start` — defined in source but no hook registered
- `on_turn_complete` — defined in source but no hook registered
- `post_api_request` — defined in source but no hook registered
- `post_llm_call` — defined in source but no hook registered
- `pre_api_request` — defined in source but no hook registered
- `pre_transform_response` — defined in source but no hook registered

## Hook commands per event

### `on_session_end`
- `C:/Program Files/Git/usr/bin/bash.exe" "C:/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hook.sh`
- `C:/Program Files/Git/usr/bin/bash.exe" "C:/Users/Alexa/AppData/Local/hermes/hooks/session-auto-commit/hook.sh`
- `C:/Program Files/Git/usr/bin/bash.exe" "C:/Users/Alexa/AppData/Local/hermes/hooks/governance-audit/hook.sh`

### `on_session_start`
- `C:/Program Files/Git/usr/bin/bash.exe" "C:/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hook.sh`
- `C:/Program Files/Git/usr/bin/bash.exe" "C:/Users/Alexa/AppData/Local/hermes/hooks/governance-audit/hook.sh`

### `post_tool_call`
- `C:/Program Files/Git/usr/bin/bash.exe" "C:/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hook.sh`
- `C:/Program Files/Git/usr/bin/bash.exe" "C:/Users/Alexa/AppData/Local/hermes/hooks/governance-audit/hook.sh`

### `pre_llm_call`
- `C:/Program Files/Git/usr/bin/bash.exe" "C:/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hook.sh`
- `C:/Program Files/Git/usr/bin/bash.exe" "C:/Users/Alexa/AppData/Local/hermes/hooks/governance-audit/hook.sh`
- `C:/Program Files/Git/usr/bin/bash.exe" -c "python C:/Users/Alexa/AppData/Local/hermes/skills/devops/mcp-server-health/scripts/mcp_preflight_check.py`

### `pre_tool_call`
- `C:/Program Files/Git/usr/bin/bash.exe" "C:/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hook.sh`
- `C:/Program Files/Git/usr/bin/bash.exe" "C:/Users/Alexa/AppData/Local/hermes/hooks/governance-audit/hook.sh`

### `subagent_stop`
- `C:/Program Files/Git/usr/bin/bash.exe" "C:/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hook.sh`
- `C:/Program Files/Git/usr/bin/bash.exe" "C:/Users/Alexa/AppData/Local/hermes/hooks/governance-audit/hook.sh`

## Plugins (top-level only)
| name | has plugin.yaml | hooks | tools |
|---|---|---|---|
| cli-enhancements | True | 0 | 0 |
| context-engineering | True | 0 | 0 |
| gh-skills-builder | True | 0 | 0 |
| hermes-achievements | False | 0 | 0 |
| mindstudio-agent | False | 0 | 0 |
| oh-my-hermes | False | 0 | 0 |
| opencode | True | 0 | 0 |
| project-planning | True | 0 | 0 |
| superpowers | True | 0 | 0 |
| superpowers-developing-for-claude-code | True | 0 | 0 |
| superpowers-marketplace | True | 0 | 0 |
| telegram-bot | True | 0 | 0 |
| the-elements-of-style | True | 0 | 0 |
| tui-enhancements | True | 0 | 0 |
| where-was-i | True | 0 | 0 |