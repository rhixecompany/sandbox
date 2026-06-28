# Hermes Config Validation Pitfalls

Documented from session debugging Hermes agent config warnings and errors (2026-06-19).

## 1. Empty Section Warning: `max_concurrent_sessions: null`

**Symptom:** `WARNING tui_gateway.server: config.yaml has empty section(s): 'max_concurrent_sessions'. Remove the line(s) or set them to '{}' — empty sections silently drop nested settings.`

**Root Cause:** YAML `null` value for a top-level key is interpreted as an empty section by the config parser.

**Fix:** Set an explicit integer value:
```yaml
max_concurrent_sessions: 10
```

## 2. MCP Discovery Timeout Too Low

**Symptom:** `TimeoutError: MCP call timed out after 120.1s (configured timeout: 120.0s)` during MCP tool discovery, preceded by `WARNING tools.mcp_tool: MCP server 'code-sandbox' shutdown timed out, cancelling task`

**Root Cause:** `mcp_discovery_timeout: 1.5` (seconds) is far too aggressive for MCP servers that need time to start (npx-based servers especially).

**Fix:** Increase to a reasonable value:
```yaml
mcp_discovery_timeout: 30
```

## 3. Linear MCP Server OAuth Lock Bug

**Symptom:** Repeated `RuntimeError: The current task is not holding this lock` from `mcp.client.auth.oauth2`, followed by MCP discovery timeouts (120s) and `CancelledError` for ALL servers.

**Root Cause:** Known bug in MCP Python SDK (`mcp.client.auth.oauth2` async lock management). The lock is acquired by one task but released by another.

**Stack Trace Pattern:**
```
File "oauth2.py", line 484, in async_auth_flow
  async with self.context.lock:
File "anyio/_core/_synchronization.py", line 166, in __aexit__
  self.release()
File "anyio/_backends/_asyncio.py", line 1854, in release
  raise RuntimeError("The current task is not holding this lock")
```

**Impact:** Blocks MCP tool discovery for ALL servers (not just Linear) because discovery runs sequentially.

**Workaround:** Disable the problematic server in `config.yaml`:
```yaml
mcp_servers:
  linear:
    enabled: false
```

**Cleanup:** Remove stale OAuth tokens:
```bash
rm ~/AppData/Local/hermes/mcp-tokens/linear*.json
```

## 4. Unsupported Model in Fallback Providers

**Symptom:** `ERROR [session] agent.conversation_loop: Non-retryable client error: Error code: 401 - {'type': 'error', 'error': {'type': 'ModelError', 'message': 'Model nemotron-3-super-free is not supported'}}`

**Root Cause:** `fallback_providers` chain includes a model (`nemotron-3-super-free`) that the provider (`opencode-zen`) does not support. When the support. Fallback logic tries it after the primary model fails, causing a hard 401.

**Fix:** Remove unsupported models from `fallback_providers`:
```yaml
fallback_providers:
- api_mode: chat_completions
  base_url: https://opencode.ai/zen/v1
  model: nemotron-3-ultra-free  # Only supported model
  provider: opencode-zen
```

## 5. YAML Multi-line Command Format Error (Hook Commands)

**Symptom:** `command not found` for shell hooks at session boundaries.

**Root Cause:** Hook commands in `config.yaml` split across YAML lines without the `-c` flag:
```yaml
# BROKEN - bash treats path as script file
hooks:
  on_session_start:
    - command: C:\Program Files\Git\usr\bin\bash.exe 
        /c/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hook.sh
```

**Fix:** Use proper single-line quoted command with `-c` flag:
```yaml
# CORRECT - bash executes the command string
hooks:
  on_session_start:
    - command: "C:\\Program Files\\Git\\usr\\bin\\bash.exe -c \"/c/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hook.sh\""
```

**Key Points:**
- YAML folding (`>` or `|`) or implicit line continuation breaks the command
- Must use `-c` to pass command string to bash
- Escape backslashes for Windows paths in YAML double quotes
- Forward slashes in MSYS paths (`/c/Users/...`) work inside the quoted string

## Debugging Checklist for Hermes Config Issues

1. **Check `max_concurrent_sessions`** — Must be integer, not `null`
2. **Check `mcp_discovery_timeout`** — Set ≥ 30s for npx-based servers
3. **Check MCP server configs** — Disable problematic servers (Linear OAuth bug)
4. **Check `fallback_providers`** — Only include models the provider actually supports
5. **Check hook command format** — Single line, `-c` flag, proper escaping
6. **Verify hook scripts executable** — `chmod +x hook.sh` and shebang present
7. **Test hooks manually** — Run directly before relying on Hermes
8. **Clear error log** — `rm ~/AppData/Local/hermes/logs/errors.log` then reproduce
9. **Verify fixes** — Test all hook events (start, end, pre_llm_call) and MCP tool list