# Hermes Hook Configuration Pitfalls

Documented from session debugging Hermes agent hook failures (2026-06-19).

## 1. YAML Multi-line Command Format Error

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

## 2. MCP Linear OAuth Lock Bug

**Symptom:** Repeated `RuntimeError: The current task is not holding this lock` from `mcp.client.auth.oauth2`, followed by MCP discovery timeouts (120s) and `CancelledError` for all servers.

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

## Debugging Checklist for Hermes Hook/MCP Issues

1. **Check hook command format** - Single line, `-c` flag, proper escaping
2. **Verify hook scripts executable** - `chmod +x hook.sh` and shebang present
3. **Test hooks manually** - Run directly before relying on Hermes
4. **Check MCP server config** - Disable problematic servers to unblock discovery
5. **Clear error log** - `rm ~/AppData/Local/hermes/logs/errors.log` then reproduce
6. **Verify fixes** - Test all hook events (start, end, pre_llm_call) and MCP tool list