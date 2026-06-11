# Docker MCP Integration

**Status (May 25, 2026):** Approach A (direct `docker-mcp-server`) is the recommended and actively maintained approach. Approach B (Docker MCP Gateway wrapper) has been superseded due to platform-specific subprocess limitations on Windows.

---

## Approach A: Docker Management Server (`docker`) ✓ RECOMMENDED

Provides direct Docker daemon management (containers, images, volumes, networks, compose, exec, DB backup/restore).

### Quick Config

```yaml
# ~/.hermes/config.yaml
mcp_servers:
  docker:
    command: docker-mcp-server
    enabled: true
```

### Test

```bash
hermes mcp test docker
# Expected: ✓ Connected (625ms), 20 tools discovered
```

### 20 Available Tools

- Container lifecycle: `docker_container_list`, `.start`, `.stop`, `.restart`, `.logs`, `.stats`
- Docker Compose: `docker_compose_up`, `.down`
- Resources: `docker_resource_list` (images/volumes/networks)
- Execute: `docker_exec` (run commands in containers)
- Database: `docker_db_query`, `.backup`, `.restore`, `.status`
- Environment: `docker_env_list`, `.compose_config`, `.healthcheck`
- Server: `docker_mcp_health`, `.profile_info`, `.projects`

### Package

```bash
npm install -g @hypnosis/docker-mcp-server
# Binary: docker-mcp-server (on PATH after global install)
```

### Why Use This?

✓ Fast connection (< 1s)  
✓ No init latency  
✓ Pre-compiled binary (no subprocess parsing issues)  
✓ Direct Docker daemon communication  
✓ Production-ready and stable  

---

## Approach B: Docker MCP Gateway (`docker-adminbot`) ⚠ DEPRECATED

**Status:** No longer recommended. The Python wrapper approach has fundamental platform limitations on Windows.

### What It Provided

| Server | Tools | Purpose |
|--------|-------|---------| 
| GitHub Official | 41 | PRs, issues, commits, code review, copilot, branches, releases |
| GitHub (Archived) | 26 | Legacy GitHub API (PRs, issues, commits, forks, repos) |
| Git | 5 (unstable) | Local Git: add, commit, diff, log, status |
| GitMCP | 5 | Remote git docs & code search via gitmcp.io |
| Internal | 9 | `mcp-find`, `mcp-add`, `mcp-remove`, `mcp-exec`, `code-mode`, `mcp-config-set`, `mcp-create-profile`, `mcp-activate-profile`, `mcp-discover` |

**Total:** 63+ tools discovered (but now unavailable)

### Why It Was Deprecated

**Root Cause:** Python `subprocess.Popen()` on Windows uses `cmd.exe` by default, which cannot parse complex POSIX-style Docker MCP subcommand chains.

**Example failure:**
```
Command: docker mcp gateway run --profile adminbot
Parsed by cmd.exe as: docker [mcp] (--profile unknown flag)
Parsed by bash as: docker [mcp] [gateway] [run] [--profile] [adminbot]
```

**Symptoms:**
- `hermes mcp test docker-adminbot` consistently times out (40-50s)
- Error: "unknown flag: --profile"
- Gateway subprocess parsing fails before wrapper can relay protocol messages
- Attempted fixes (explicit bash, shell=True, etc.) all failed due to Windows process context limitations

**Session Details:** See `HERMES_MCP_DOCKER_FIX_REPORT.txt` (May 25, 2026) for full debugging transcript, three attempted fixes, root cause analysis, and technical rationale.

### If You Need GitHub Tools

For GitHub PRs, issues, and code search, use the standalone GitHub MCP server instead:

```yaml
mcp_servers:
  github:
    command: npx
    args: [-y, "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_xxxxxxxxxxxxxxxxxxxx"
```

This is faster, more reliable, and avoids the gateway wrapper complexity.

---

## Which One Should I Use?

| If you want to... | Use |
|---|---|
| List/start/stop Docker containers | `docker` (Approach A) ✓ |
| View Docker logs, stats, compose | `docker` (Approach A) ✓ |
| Run commands inside containers | `docker` (Approach A) ✓ |
| Back up/restore a Docker DB | `docker` (Approach A) ✓ |
| Create GitHub PRs and issues | Use separate `github` server |
| Search GitHub repos and code | Use separate `github` server |
| Manage branches and commits | Use separate `github` server |

Both servers can be enabled simultaneously — they don't conflict.

---

## Troubleshooting

### Connection Timeout — `docker` Server

**Causes:** Docker daemon not running, binary not on PATH, port conflict

```bash
docker ps                          # is Docker running?
which docker-mcp-server            # is binary on PATH?
npm list -g @hypnosis/docker-mcp-server
```

### Diagnosing MCP Server Timeouts (General Pattern)

When `hermes mcp test server_name` times out consistently:

1. **Check config syntax:** YAML indentation matters
   ```bash
   cat ~/.hermes/config.yaml | grep -A 5 mcp_servers
   ```

2. **Test the underlying command directly:**
   ```bash
   # If stdio transport:
   timeout 5 docker-mcp-server  # or npx pkg-name, etc.
   
   # Should output JSON-RPC init message within 1-2s
   ```

3. **Check for initialization delays:** Some servers take 4-6s to initialize
   ```bash
   time docker mcp gateway run --profile adminbot 2>&1 | head -20
   # Look for ready signals like "Start stdio server"
   ```

4. **If wrapper is used:** Check debug logs for subprocess parsing errors
   ```bash
   cat C:\Users\Alexa\AppData\Local\hermes\wrapper_debug.log
   # Look for: unknown flag, execvpe errors, arg parsing failures
   ```

5. **Increase timeouts incrementally:**
   ```yaml
   mcp_servers:
     slow_server:
       command: my-slow-server
       connect_timeout: 120  # was 60
       timeout: 180          # was 120
   ```

6. **If subprocess args are failing on Windows:** 
   - Avoid complex command chains in Python subprocess calls
   - Use pre-compiled binaries instead of shell-based commands
   - If you must use a wrapper, run it through bash explicitly (requires bash on PATH in the Windows context)

### Port Conflicts (SSE Transport)

Kill stale gateway processes:
```bash
# Find process on port 8555
netstat -ano | grep ":8555"
# Kill it
taskkill //F //PID <pid>
```

### Init Logs Pollute Stdio

Some gateways write MCP protocol messages to **stdout** and init logs to **stderr**, which is the correct separation. Wrappers must handle this by draining stderr until a ready signal appears. Never use `2>&1` when testing — that merges stderr into stdout and corrupts the JSON-RPC stream.

---

## References

- Session analysis: `C:\Users\Alexa\Desktop\Sandbox\HERMES_MCP_DOCKER_FIX_REPORT.txt` (May 25, 2026)
- Gateway wrapper (archived): `C:\Users\Alexa\AppData\Local\hermes\docker-mcp-gateway-wrapper.py`
- Wrapper debug log: `C:\Users\Alexa\AppData\Local\hermes\wrapper_debug.log`
