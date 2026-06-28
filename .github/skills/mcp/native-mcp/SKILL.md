---
author: Hermes Agent
description: 'MCP client: connect servers, register tools (stdio/HTTP).'
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: native-mcp
tags:
- imported
title: Native MCP
version: 1.0.0

---
# Native MCP Client

Hermes Agent has a built-in MCP client that connects to MCP servers at startup, discovers their tools, and makes them available as first-class tools the agent can call directly. No bridge CLI needed -- tools from MCP servers appear alongside built-in tools like `terminal`, `read_file`, etc.

## When to Use

Use this whenever you want to:
- Connect to MCP servers and use their tools from within Hermes Agent
- Add external capabilities (filesystem access, GitHub, databases, APIs) via MCP
- Run local stdio-based MCP servers (npx, uvx, or any command)
- Connect to remote HTTP/StreamableHTTP MCP servers
- Have MCP tools auto-discovered and available in every conversation

For ad-hoc, one-off MCP tool calls from the terminal without configuring anything, see the `mcporter` skill instead.

## Prerequisites

- **mcp Python package** -- optional dependency; install with `pip install mcp`. If not installed, MCP support is silently disabled.
- **Node.js** -- required for `npx`-based MCP servers (most community servers)
- **uv** -- required for `uvx`-based MCP servers (Python-based servers)

Install the MCP SDK:

```bash
pip install mcp
# or, if using uv:
uv pip install mcp
```

## Quick Start: Add & Deploy an MCP Server

### Step 1: Configure the Server

Add MCP servers to `~/.hermes/config.yaml` under the `mcp_servers` key:

```yaml
mcp_servers:
  time:
    command: "uvx"
    args: ["mcp-server-time"]
```

### Step 2: Test the Connection (Do This Before Deploying)

```bash
# Test with Hermes CLI tool
hermes mcp test time

# Expected output shows tool count and names
```

This ensures the MCP server is reachable and tools are discoverable BEFORE you restart the agent.

### Step 3: Restart & Use

Restart Hermes Agent (or just reload the config). On startup it will:
1. Connect to the server
2. Discover available tools
3. Register them with the prefix `mcp_time_*`
4. Inject them into all platform toolsets

You can then use the tools naturally -- just ask the agent to get the current time.

### Step 4: Verify in Conversation

After restart, test that tools are available:

```bash
hermes chat "What time is it?"
```

The agent should use the MCP tool automatically.

## Configuration Reference

Each entry under `mcp_servers` is a server name mapped to its config. There are two transport types: **stdio** (command-based) and **HTTP** (url-based).

### Stdio Transport (command + args)

```yaml
mcp_servers:
  server_name:
    command: "npx"             # (required) executable to run
    args: ["-y", "pkg-name"]   # (optional) command arguments, default: []
    env:                       # (optional) environment variables for the subprocess
      SOME_API_KEY: "value"
    timeout: 120               # (optional) per-tool-call timeout in seconds, default: 120
    connect_timeout: 60        # (optional) initial connection timeout in seconds, default: 60
```

### HTTP Transport (url)

```yaml
mcp_servers:
  server_name:
    url: "https://my-server.example.com/mcp"   # (required) server URL
    headers:                                     # (optional) HTTP headers
      Authorization: "Bearer sk-..."
    timeout: 180               # (optional) per-tool-call timeout in seconds, default: 120
    connect_timeout: 60        # (optional) initial connection timeout in seconds, default: 60
```

### All Config Options

| Option            | Type   | Default | Description                                       |
|-------------------|--------|---------|---------------------------------------------------|
| `command`         | string | --      | Executable to run (stdio transport, required)     |
| `args`            | list   | `[]`    | Arguments passed to the command                   |
| `env`             | dict   | `{}`    | Extra environment variables for the subprocess    |
| `url`             | string | --      | Server URL (HTTP transport, required)             |
| `headers`         | dict   | `{}`    | HTTP headers sent with every request              |
| `timeout`         | int    | `120`   | Per-tool-call timeout in seconds                  |
| `connect_timeout` | int    | `60`    | Timeout for initial connection and discovery      |

Note: A server config must have either `command` (stdio) or `url` (HTTP), not both.

## How It Works

### Startup Discovery

When Hermes Agent starts, `discover_mcp_tools()` is called during tool initialization:

1. Reads `mcp_servers` from `~/.hermes/config.yaml`
2. For each server, spawns a connection in a dedicated background event loop
3. Initializes the MCP session and calls `list_tools()` to discover available tools
4. Registers each tool in the Hermes tool registry

### Tool Naming Convention

MCP tools are registered with the naming pattern:

```
mcp_{server_name}_{tool_name}
```

Hyphens and dots in names are replaced with underscores for LLM API compatibility.

Examples:
- Server `filesystem`, tool `read_file` → `mcp_filesystem_read_file`
- Server `github`, tool `list-issues` → `mcp_github_list_issues`
- Server `my-api`, tool `fetch.data` → `mcp_my_api_fetch_data`

### Auto-Injection

After discovery, MCP tools are automatically injected into all `hermes-*` platform toolsets (CLI, Discord, Telegram, etc.). This means MCP tools are available in every conversation without any additional configuration.

### Connection Lifecycle

- Each server runs as a long-lived asyncio Task in a background daemon thread
- Connections persist for the lifetime of the agent process
- If a connection drops, automatic reconnection with exponential backoff kicks in (up to 5 retries, max 60s backoff)
- On agent shutdown, all connections are gracefully closed

### Idempotency

`discover_mcp_tools()` is idempotent -- calling it multiple times only connects to servers that aren't already connected. Failed servers are retried on subsequent calls.

## Transport Types

### Stdio Transport

The most common transport. Hermes launches the MCP server as a subprocess and communicates over stdin/stdout.

```yaml
mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
```

The subprocess inherits a **filtered** environment (see Security section below) plus any variables you specify in `env`.

### HTTP / StreamableHTTP Transport

For remote or shared MCP servers. Requires the `mcp` package to include HTTP client support (`mcp.client.streamable_http`).

```yaml
mcp_servers:
  remote_api:
    url: "https://mcp.example.com/mcp"
    headers:
      Authorization: "Bearer sk-..."
```

If HTTP support is not available in your installed `mcp` version, the server will fail with an ImportError and other servers will continue normally.

## Security

### Environment Variable Filtering

For stdio servers, Hermes does NOT pass your full shell environment to MCP subprocesses. Only safe baseline variables are inherited:

- `PATH`, `HOME`, `USER`, `LANG`, `LC_ALL`, `TERM`, `SHELL`, `TMPDIR`
- Any `XDG_*` variables

All other environment variables (API keys, tokens, secrets) are excluded unless you explicitly add them via the `env` config key. This prevents accidental credential leakage to untrusted MCP servers.

```yaml
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      # Only this token is passed to the subprocess
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_..."
```

### Credential Stripping in Error Messages

If an MCP tool call fails, any credential-like patterns in the error message are automatically redacted before being shown to the LLM. This covers:

- GitHub PATs (`ghp_...`)
- OpenAI-style keys (`sk-...`)
- Bearer tokens
- Generic `token=`, `key=`, `API_KEY=`, `password=`, `secret=` patterns

## Deployment to Gateway Profiles

MCP tools configured in the root Hermes config are **automatically available in all gateway profiles**, including custom profiles like `adminbot`. To deploy MCP tools to a messaging gateway:

### Step 1: Create a Gateway Profile

```bash
hermes profile create adminbot
```

This profile inherits MCP servers from the root Hermes config.

### Step 2: Start the Gateway with the Profile

```bash
hermes gateway run --profile adminbot
```

The gateway will:
- Load the root `mcp_servers` config
- Connect to all configured MCP servers
- Register tools in the gateway context
- Make MCP tools available to external clients (Telegram, Slack, etc.)

### Step 3: Verify Tools Are Available

Check that tools are discovered:

```bash
# In another terminal, while gateway is running
hermes mcp list
```

Expected output shows all configured servers with status `✓ enabled`.

### Important: Test Before Deploying

Always test the MCP server connection BEFORE starting the gateway:

```bash
hermes mcp test server_name
```

If `hermes mcp test` hangs or times out, the server will also hang when the gateway tries to load it. Common causes:
- MCP package not installed (`docker-mcp-server`, etc.)
- Docker daemon or required service not running
- Port conflicts or network issues

Fix the underlying issue, verify with `hermes mcp test`, then start the gateway.

### Gateway + MCP Workflow

```bash
# 1. Add MCP server to config
# 2. Test connection
hermes mcp test docker

# 3. Verify it appears in the list
hermes mcp list | grep docker

# 4. Create or use a gateway profile
hermes profile create mybot

# 5. Deploy the gateway
hermes gateway run --profile mybot

# 6. Configure messaging platforms (in .env or hermes config)
# 7. Connect externally to the gateway
## Troubleshooting

### CRITICAL: Always Test MCP Servers Before Deploying to Gateway

When deploying MCP servers to a gateway profile, verify the connection works first:

```bash
# After adding server to config
hermes mcp test docker

# If this times out or fails, fix the issue before starting the gateway
hermes gateway run --profile mybot
```

If `hermes mcp test` hangs, the gateway will also hang when trying to load that server. Common causes:
- Required daemon not running (e.g., Docker not started)
- Binary not on PATH
- Port conflicts
- Permission issues

Always test in this order:
1. Add to `mcp_servers` in config.yaml
2. Run `hermes mcp test server_name` — must succeed
3. Create/use gateway profile
4. Start gateway

### PITFALL: Windows Subprocess Argument Parsing Failures

**Problem:** On Windows, Python's `subprocess.Popen()` defaults to using `cmd.exe` (Windows command shell), not bash. When wrapping MCP servers that require complex POSIX-style subcommand chains, `cmd.exe` cannot parse them correctly.

**Example failure:**
```
Command: docker mcp gateway run --profile adminbot

cmd.exe parses as: docker [mcp] (--profile unknown flag)
bash parses as:    docker [mcp] [gateway] [run] [--profile] [adminbot]
```

**Symptom:** `hermes mcp test` times out (40-50s), error message shows "unknown flag" for flag args.

**Mitigations (in order of preference):**
1. **Use pre-compiled binaries instead of shell wrappers** — e.g., `docker-mcp-server` (binary) instead of wrapper-based gateways. Binaries don't require shell parsing.
2. **Increase connection timeout** in config — some servers just need more init time:
   ```yaml
   mcp_servers:
     my_server:
       command: my-tool
       connect_timeout: 120  # was 60
   ```
3. **If you must use a wrapper on Windows:**
   - Do not use Python's `subprocess.Popen()` with shell=False (default)
   - Do not use `shell=True` — cmd.exe still can't parse complex chains
   - Instead, use `shell=True` with bash explicitly via `bash -c "..."`
   - This requires bash to be on PATH in the Windows process context (MSYS/git-bash may not be available in native Windows processes)

**Best Practice:** Prefer pre-compiled MCP server binaries over Python/shell wrappers. See `references/docker-mcp-integration.md` for worked example (Approach A vs. Approach B).

**Session Reference:** `C:\Users\Alexa\Desktop\Sandbox\HERMES_MCP_DOCKER_FIX_REPORT.txt` documents the root cause analysis, three attempted fixes, and technical rationale (May 25, 2026).

### "MCP SDK not available -- skipping MCP tool discovery"

The `mcp` Python package is not installed. Install it:

```bash
pip install mcp
```

### "No MCP servers configured"

No `mcp_servers` key in `~/.hermes/config.yaml`, or it's empty. Add at least one server.

### "Failed to connect to MCP server 'X'"

Common causes:
- **Command not found**: The `command` binary isn't on PATH. Ensure `npx`, `uvx`, or the relevant command is installed.
- **Package not found**: For npx servers, the npm package may not exist or may need `-y` in args to auto-install.
- **Timeout**: The server took too long to start. Increase `connect_timeout`.
- **Port conflict**: For HTTP servers, the URL may be unreachable.

### Initialization-Latent MCP Servers

Some MCP servers (e.g. `docker mcp gateway run --profile adminbot`) take **4–6 seconds** to initialize before they're ready to accept protocol messages. During init they pull Docker images and discover sub-server tools. Hermes sends the `initialize` message immediately after launching the subprocess, so the handshake arrives before the server is ready and the connection fails.

**Symptom:** `hermes mcp test` consistently times out (30s+), even when the server starts successfully when run directly.

**Mitigations (in order of preference):**
1. **Increase `connect_timeout`** in the server config (default is 60s, so this rarely helps alone unless the timeout was manually lowered)
2. **Create a wrapper script** that waits for a ready signal before relaying stdin/stdout. See `references/docker-mcp-integration.md` for a worked example.
3. **For gateway-style servers:** if the gateway writes init logs to stderr and signals readiness on stderr (e.g. "Start stdio server"), write a Python wrapper that:
   - Spawns the gateway subprocess
   - Reads stderr until the ready signal appears
   - Then relays stdin↔stdout bidirectionally
   - This ensures the `initialize` handshake doesn't arrive before the server is ready

### "MCP server 'X' requires HTTP transport but mcp.client.streamable_http is not available"

Your `mcp` package version doesn't include HTTP client support. Upgrade:

```bash
pip install --upgrade mcp
```

### Tools not appearing

- Check that the server is listed under `mcp_servers` (not `mcp` or `servers`)
- Ensure the YAML indentation is correct
- Look at Hermes Agent startup logs for connection messages
- Tool names are prefixed with `mcp_{server}_{tool}` -- look for that pattern

### Connection keeps dropping

The client retries up to 5 times with exponential backoff (1s, 2s, 4s, 8s, 16s, capped at 60s). If the server is fundamentally unreachable, it gives up after 5 attempts. Check the server process and network connectivity.

## Examples

### Time Server (uvx)

```yaml
mcp_servers:
  time:
    command: "uvx"
    args: ["mcp-server-time"]
```

Registers tools like `mcp_time_get_current_time`.

### Docker Server (npm package)

```yaml
mcp_servers:
  docker:
    command: "docker-mcp-server"
```

Registers 20 Docker tools (`docker_container_list`, `docker_container_start`, etc.). See `references/docker-mcp-integration.md` for full Docker setup workflow, troubleshooting, and gateway deployment pattern.

### Filesystem Server (npx)

```yaml
mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/documents"]
    timeout: 30
```

Registers tools like `mcp_filesystem_read_file`, `mcp_filesystem_write_file`, `mcp_filesystem_list_directory`.

### GitHub Server with Authentication

```yaml
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_xx...xxxx"
    timeout: 60
```

Registers tools like `mcp_github_list_issues`, `mcp_github_create_pull_request`, etc.

### Remote HTTP Server

```yaml
mcp_servers:
  company_api:
    url: "https://mcp.mycompany.com/v1/mcp"
    headers:
      Authorization: "Bearer sk-xxx...xxxx"
      X-Team-Id: "engineering"
    timeout: 180
    connect_timeout: 30
```

### Multiple Servers

```yaml
mcp_servers:
  time:
    command: "uvx"
    args: ["mcp-server-time"]

  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]

  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_xx...xxxx"

  company_api:
    url: "https://mcp.internal.company.com/mcp"
    headers:
      Authorization: "Bearer sk-xxx...xxxx"
    timeout: 300
```

All tools from all servers are registered and available simultaneously. Each server's tools are prefixed with its name to avoid collisions.

## Sampling (Server-Initiated LLM Requests)

Hermes supports MCP's `sampling/createMessage` capability — MCP servers can request LLM completions through the agent during tool execution. This enables agent-in-the-loop workflows (data analysis, content generation, decision-making).

Sampling is **enabled by default**. Configure per server:

```yaml
mcp_servers:
  my_server:
    command: "npx"
    args: ["-y", "my-mcp-server"]
    sampling:
      enabled: true           # default: true
      model: "gemini-3-flash" # model override (optional)
      max_tokens_cap: 4096    # max tokens per request
      timeout: 30             # LLM call timeout (seconds)
      max_rpm: 10             # max requests per minute
      allowed_models: []      # model whitelist (empty = all)
      max_tool_rounds: 5      # tool loop limit (0 = disable)
      log_level: "info"       # audit verbosity
```

Servers can also include `tools` in sampling requests for multi-turn tool-augmented workflows. The `max_tool_rounds` config prevents infinite tool loops. Per-server audit metrics (requests, errors, tokens, tool use count) are tracked via `get_mcp_status()`.

Disable sampling for untrusted servers with `sampling: { enabled: false }`.

## Notes

- MCP tools are called synchronously from the agent's perspective but run asynchronously on a dedicated background event loop
- Tool results are returned as JSON with either `{"result": "..."}` or `{"error": "..."}`
- The native MCP client is independent of `mcporter` -- you can use both simultaneously
- Server connections are persistent and shared across all conversations in the same agent process
- Adding or removing servers requires restarting the agent (no hot-reload currently)

## References

| File | Topic |
|------|-------|
| `references/docker-mcp-integration.md` | Docker MCP setup and troubleshooting |
| `references/mcp-memory-knowledge-graph.md` | MCP memory server knowledge graph pattern |
```


## Pitfalls

- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context
- **Context limits:** Process in batches; write results after each batch
## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

