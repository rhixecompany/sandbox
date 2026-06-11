# MCP Docker Server Setup — Windows Example

**Session**: MCP Docker integration for Hermes Agent on Windows 11
**Date**: 2026-05-29
**Outcome**: ✅ Configuration complete (commit `ec2e412`)

## Scenario

User: Windows 11 with Docker Desktop installed
Goal: Add Docker MCP gateway to Hermes Agent for container management
Challenge: Docker command not in system PATH; needs full absolute path

## Solution Applied

### Step 1: Locate Docker Command

```bash
where docker
# Output:
# C:\Program Files\Docker\Docker\resources\bin\docker
# C:\Program Files\Docker\Docker\resources\bin\docker.exe
```

### Step 2: Add MCP Server via CLI

```bash
hermes mcp add mcp-docker --command '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker" mcp gateway run --profile adminbot'
```

When prompted, approve the config save even if test fails (service may be starting up).

### Step 3: Verify Configuration

Check that MCP server was registered:

```bash
hermes mcp list
```

Should show mcp-docker with enabled status.

### Step 4: Enable and Test

```bash
hermes config set mcp_servers.mcp-docker.enabled true
hermes mcp test mcp-docker
```

**Expected on first test** (if Docker just started): "Connection failed"
**Expected after Docker is ready** (5-30 seconds): "Connection successful"

## Key Configuration Patterns

### Pattern 1: Full Path (No PATH Lookup)

```yaml
mcp-docker:
  command: "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker"
  args:
    - mcp
    - gateway
    - run
    - --profile
    - adminbot
  type: stdio
  enabled: true
```

**When to use**: Command not in system PATH, or explicit path required for clarity

### Pattern 2: With Environment Variables

```yaml
mcp-docker:
  command: "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker"
  args:
    - mcp
    - gateway
    - run
    - --profile
    - adminbot
  env:
    LOCALAPPDATA: C:\Users\Alexa\AppData\Local
    ProgramData: C:\ProgramData
    ProgramFiles: C:\Program Files
  type: stdio
  enabled: true
```

**When to use**: Subprocess needs explicit env vars (not inherited from parent)

## Troubleshooting Applied

### Issue: "Access is denied" on first test

**Diagnosis**: Docker daemon was starting up (Docker Desktop launching)

**Solution**: 
1. Wait for Docker Desktop to fully start (5-30 seconds)
2. Verify with `docker ps` command (returns container list)
3. Retry test: `hermes mcp test mcp-docker`

### Issue: Command not found in PATH

**Diagnosis**: `where docker` or `which docker` not returning a command

**Solution**:
1. Use `where docker` to locate full path
2. Use absolute path in config instead of command name
3. Verify path exists: `test -f "C:\Program Files\..."` (or `dir` on Windows)

### Issue: YAML parse errors

**Diagnosis**: Syntax errors in backslash escaping or quotes

**Solution**:
- YAML requires doubled backslash: `\\` not `\`
- Or use forward slashes: `C:/Program Files/...`
- Quote paths with spaces: `command: "path/to/command"`

## Key Learnings

1. **Full paths needed on Windows when command not in PATH**
   - Use `where` command to find absolute path
   - Don't rely on PATH environment variable alone

2. **Docker startup delay is normal**
   - First test may fail; this doesn't indicate config error
   - Wait 10-30 seconds for Docker Desktop to initialize
   - Safe to save config and test later

3. **YAML path escaping on Windows**
   - Doubled backslashes: `C:\\Users\\...`
   - Or forward slashes: `C:/Users/...`
   - Always quote paths with spaces

4. **Environment variables passed explicitly**
   - Subprocess doesn't inherit all parent env by default
   - Explicitly pass required vars in `env:` section
   - Useful for Windows system path overrides

5. **Config structure: args vs command**
   - Can combine into one: `command: "path/to/command arg1 arg2"`
   - Or separate: `command: "path"` + `args: [arg1, arg2]`
   - Separate structure is clearer and avoids escaping

## Testing & Verification

**Verification checks performed**:
- Docker command located and path verified
- Docker daemon running (docker ps returns containers)
- MCP server listed in `hermes mcp list`
- Server enabled and configuration saved
- Setup guide and troubleshooting documented
- Committed to version control

**Typical verification flow**:
```bash
where docker                                    # Locate command
docker ps                                       # Verify daemon running
hermes mcp list                                 # Check registration
hermes mcp test mcp-docker                      # Test connection
hermes config set mcp_servers.mcp-docker.enabled true  # Enable
```

## When to Use This Approach

✅ **Use for**:
- Command-based MCP servers on Windows
- Commands not in system PATH
- Any stdio transport MCP server
- Docker Desktop or other heavyweight services

❌ **Don't use for**:
- HTTP/URL-based MCP servers (different config)
- Commands already in PATH (can use name alone)
- Debugging active MCP failures (reference main skill)

## Session Artifacts

- Git commit: `ec2e412` — MCP Docker setup documentation
- Related setup: Git submodules (commit `9bef828`)
- Full guide: `docs/mcp-docker-setup-report.md`
