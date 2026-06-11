---
name: hermes-mcp-server-setup
title: Hermes MCP Server Setup & Configuration
description: Configure, test, and integrate Model Context Protocol (MCP) servers into Hermes Agent. Covers stdio transports, environment variables, verification, and troubleshooting.
version: 1.0.0
author: Hermes Assistant
license: MIT
tags: [hermes, mcp, configuration, integration, devops, docker]
metadata:
  hermes:
    tags: [hermes, mcp, servers, integration, devops]
    related_skills: [hermes-agent, hermes-configuration-verification]
---

# Hermes MCP Server Setup & Configuration

MCP (Model Context Protocol) servers extend Hermes Agent with additional tools and integrations. This skill covers the end-to-end workflow for adding, configuring, testing, and troubleshooting MCP servers.

## When to Use

- Adding a new MCP server to Hermes (Docker, Slack, custom endpoints, etc.)
- Configuring MCP server environment variables and arguments
- Testing MCP server connectivity and availability
- Troubleshooting MCP server registration or connection failures
- Documenting MCP server setup for reproducibility

## When NOT to Use

- Configuring non-MCP tools (use `hermes tools` instead)
- Managing bundled/core Hermes features (use `hermes-agent` skill)
- General Hermes config (use `hermes-configuration-verification`)

## Workflow

### Phase 1: Identify Server & Gather Requirements

1. **Determine server type**:
   - Command-based (stdio): `docker`, `mcp-server-*`, custom CLI
   - HTTP/URL-based: REST endpoints, MCP HTTP servers
   - SSH-based: Remote MCP servers

2. **Collect configuration**:
   - Command path (verify it exists and is in PATH or use full path)
   - Arguments needed for the service
   - Environment variables to pass through
   - Whether server requires authentication

3. **Test prerequisites**:
   - Is the underlying service installed? (`docker --version`, `npm list -g mcp-server-*`)
   - Is it accessible? Can you run the command manually?
   - Are required env vars set? Check `.env` and system PATH

### Phase 2: Add MCP Server to Hermes Config

**Option A: Interactive CLI (recommended)**

```bash
hermes mcp add <name> --command "<command> <args>"
# or
hermes mcp add <name> --url <http_endpoint>
```

When prompted to test, say `y` if service is running, `n` if you'll verify later.

**Option B: Manual config.yaml edit**

```bash
hermes config edit
```

Add to `mcp_servers:` section:

```yaml
mcp_servers:
  my-server:
    command: /path/to/command     # or 'url:' for HTTP
    args:                          # optional
      - arg1
      - arg2
    env:                           # optional; pass through to subprocess
      VAR_NAME: value
      PATH_VAR: /custom/path
    type: stdio                    # 'stdio' for command-based, 'http' for URL
    enabled: false                 # enable after testing
```

### Phase 3: Verify Configuration & Test Connection

1. **List all MCP servers**:
   ```bash
   hermes mcp list
   ```
   Verify your server appears with correct transport and status.

2. **Test connection**:
   ```bash
   hermes mcp test <name>
   ```
   
   **Success**: "Connection successful" → server is responding
   
   **Failure**: "Connection failed" or timeout
   - Check if underlying service is running
   - Verify command path exists
   - Check environment variables
   - Ensure required credentials are set

3. **Enable the server** (if test passed):
   ```bash
   hermes config set mcp_servers.<name>.enabled true
   ```

### Phase 4: Integration & Verification in Session

1. **Restart/reload Hermes**:
   ```bash
   # In interactive session:
   /reload-mcp
   
   # Or start fresh session:
   hermes /reset
   ```

2. **Verify tools are available**:
   ```bash
   hermes tools list
   # or in session:
   /tools
   ```

3. **Document the setup**:
   - Write setup guide to `docs/<server>-setup-report.md`
   - Include testing instructions
   - Include troubleshooting section
   - Commit to git

## Common Patterns

### Docker MCP Gateway

```yaml
mcp-docker:
  command: "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker"
  args:
    - mcp
    - gateway
    - run
    - --profile
    - <profile-name>
  env:
    LOCALAPPDATA: C:\Users\<user>\AppData\Local
    ProgramData: C:\ProgramData
    ProgramFiles: C:\Program Files
  type: stdio
  enabled: true
```

**Prerequisites**:
- Docker Desktop installed
- Docker daemon running (`docker ps` succeeds)
- Docker MCP plugin available

**Test**:
```bash
hermes mcp test mcp-docker
# Should connect within 5-10 seconds after Docker daemon is ready
```

### stdio Command-Based Server

```yaml
sequential-thinking:
  command: mcp-server-sequential-thinking
  type: stdio
  enabled: true
```

**Prerequisites**:
- Package installed globally or in PATH: `npm install -g mcp-server-sequential-thinking`
- Command is executable: `which mcp-server-sequential-thinking` (or `where` on Windows)

### HTTP Endpoint Server

```yaml
context7:
  url: https://mcp.context7.com/mcp
  headers:
    CONTEXT7_API_KEY: <your-api-key>
  enabled: true
```

**Prerequisites**:
- API key in `.env` or inline (as shown)
- Endpoint is publicly accessible
- API key has required permissions

## Troubleshooting

### "The system cannot find the file specified" (WinError 2)

**Cause**: Command path not found or not in PATH

**Fix**:
1. Verify the command exists: `where docker` or `which mcp-server-*`
2. Use full absolute path if not in PATH:
   ```yaml
   command: "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker"
   ```
3. On Windows, use forward slashes or escaped backslashes in YAML

### "Access is denied" (WinError 5)

**Causes**:
- Underlying service not running (e.g., Docker Desktop not started)
- Process permissions issue (e.g., Docker socket requires elevation)
- Environment variables not set correctly

**Fixes**:
1. Start the underlying service:
   - Docker: Open Docker Desktop, wait for "Docker is running"
   - npm package: Verify with `npm list -g <package>`
2. Verify service is responsive:
   - Docker: `docker ps`
   - HTTP endpoint: `curl https://endpoint.url`
3. Check environment variables are passed correctly:
   ```bash
   hermes config show  # View current config
   # Look for mcp_servers.<name>.env section
   ```

### "Connection timeout" or "Connection refused"

**Causes**:
- Service is slow to start (Docker Desktop cold start)
- Server is not listening on expected port/socket
- Firewall blocking connection

**Fixes**:
1. Wait longer if service is starting: `sleep 10 && hermes mcp test <name>`
2. Verify service is listening: `docker ps`, `netstat`, `lsof`
3. Check firewall rules for HTTP/TCP endpoints

### MCP Tools not showing in Hermes

**Causes**:
- Server is disabled in config (`enabled: false`)
- Server failed to connect during load
- Tools not reloaded after config change

**Fixes**:
1. Enable the server: `hermes config set mcp_servers.<name>.enabled true`
2. Check status: `hermes mcp list`
3. Reload in session: `/reload-mcp`
4. Restart Hermes: `hermes /reset`

### Server works but tools are limited

**Cause**: MCP server only exposes a subset of tools (by design or permission)

**Check available tools**:
```bash
# In Hermes session, after /reload-mcp:
hermes tools list
```

The server may require additional configuration or API scopes to expose more tools.

## Pitfalls

1. **Forgetting full path on Windows**
   - Command names alone don't resolve if not in PATH
   - Use absolute path: `C:\Program Files\...`
   - Or add the directory to system PATH

2. **YAML escaping in config**
   - Backslashes in paths must be escaped: `C:\\Users\\...` (double backslash)
   - Or use forward slashes: `C:/Users/...`
   - String quotes required for paths with spaces: `command: "C:\\Program Files\\..."`

3. **Environment variables not inherited**
   - Subprocess doesn't inherit parent shell env by default
   - Explicitly pass required vars in `env:` section
   - Common vars: PATH, HOME, TEMP, system directories

4. **Testing without underlying service**
   - MCP test always tries to connect
   - If service is not running, test will fail even if config is correct
   - Safe to save config with `enabled: false` and test later

5. **Cold start delays**
   - First connection to Docker/heavy services takes 5-30 seconds
   - Retry test after giving service time to start
   - Don't judge config validity on first test failure

6. **Permissions in Docker**
   - Docker socket access on Unix requires group membership or elevation
   - On Windows, Docker Desktop user must have Docker Desktop installed for their profile
   - Not a config issue — it's a system setup issue

## Overview

Hermes Mcp Server Setup is a skill for handling hermes mcp server setup tasks and automation workflows. Use this skill when you need to perform hermes mcp server setup operations efficiently.

## Verification Checklist

- [ ] Server command/URL exists and is accessible
- [ ] Underlying service is installed and running
- [ ] Config YAML is syntactically correct (no duplicate colons, proper indentation)
- [ ] Environment variables are set (if required)
- [ ] Full path used on Windows (not just command name)
- [ ] `hermes mcp list` shows the server
- [ ] `hermes mcp test <name>` succeeds (or fails gracefully with clear error)
- [ ] Server enabled after successful test: `enabled: true`
- [ ] `/reload-mcp` executed in session or `hermes /reset` run
- [ ] Tools are available: `hermes tools list` or `/tools` in session

## Next Steps

After successful setup:
1. Document the configuration (create setup report in `docs/`)
2. Add troubleshooting section (reference `references/mcp-<server>-troubleshooting.md`)
3. Commit to git: `git add . && git commit -m "chore: configure MCP <server>"`
4. In session, use the newly available MCP tools for tasks

## References

- `references/mcp-server-patterns.md` — Common MCP server configurations
- `references/mcp-docker-setup-example.md` — Docker MCP gateway (Windows) full example
- Hermes docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp

