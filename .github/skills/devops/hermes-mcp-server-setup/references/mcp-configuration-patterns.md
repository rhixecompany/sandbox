# MCP Server Configuration Patterns

Quick reference for common MCP server setup patterns in Hermes.

## Pattern 1: Node.js Package (npm global)

```yaml
sequential-thinking:
  command: mcp-server-sequential-thinking
  type: stdio
  enabled: true
```

**Prerequisites**:
```bash
npm install -g mcp-server-sequential-thinking
which mcp-server-sequential-thinking  # Verify in PATH
```

**Use case**: npm-published MCP servers, already in PATH

---

## Pattern 2: Executable with Full Path

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

**Prerequisites**:
```bash
where docker              # Locate full path
docker ps                 # Verify daemon running
```

**Use case**: Command not in PATH, explicit path needed

---

## Pattern 3: HTTP/REST Endpoint

```yaml
context7:
  url: https://mcp.context7.com/mcp
  headers:
    CONTEXT7_API_KEY: <api-key-value>
  enabled: true
```

**Prerequisites**:
```bash
# API key in .env or set inline
echo $CONTEXT7_API_KEY  # Verify key is set
curl https://mcp.context7.com/mcp  # Verify endpoint accessible
```

**Use case**: Remote MCP servers via HTTP/HTTPS

---

## Pattern 4: Command with Arguments

```yaml
playwright:
  command: playwright-mcp
  args:
    - --caps=network,storage,testing,vision,pdf,devtools
  type: stdio
  enabled: true
```

**Prerequisites**:
```bash
npm install -g @modelcontextprotocol/server-playwright
playwright-mcp --help  # Verify command works
```

**Use case**: Command with multiple arguments/flags

---

## Pattern 5: Command with Environment Passthrough

```yaml
custom-server:
  command: /path/to/server
  env:
    CUSTOM_VAR: value
    HOME: /home/user
    PATH: /custom/bin:/usr/bin
  type: stdio
  enabled: true
```

**Prerequisites**:
```bash
export CUSTOM_VAR=value  # Set env locally first
/path/to/server --test   # Verify runs with env
```

**Use case**: Server needs specific environment variables or PATH overrides

---

## Verification Checklist by Pattern

### stdio (command-based)
- [ ] Command path exists: `test -f <path>` or `where <cmd>` (Windows)
- [ ] Command is executable: `<cmd> --version` or `<cmd> --help`
- [ ] Arguments are correct: `<cmd> <args> --help` (if applicable)
- [ ] Env vars are set (if needed): `echo $VAR_NAME`
- [ ] `hermes mcp list` shows server
- [ ] `hermes mcp test <name>` passes or fails with clear error

### HTTP/REST
- [ ] Endpoint is reachable: `curl <url>` or browser
- [ ] Authentication is set: `echo $API_KEY` or check config headers
- [ ] Endpoint responds: `curl -H "Auth: ..." <url>`
- [ ] `hermes mcp list` shows server
- [ ] `hermes mcp test <name>` connects

---

## Common Env Variables

On Windows, commonly needed passthrough vars:

```yaml
env:
  LOCALAPPDATA: C:\Users\<user>\AppData\Local
  ProgramData: C:\ProgramData
  ProgramFiles: C:\Program Files
  TEMP: C:\Windows\Temp
  USERPROFILE: C:\Users\<user>
```

On Unix:

```yaml
env:
  HOME: /home/user
  PATH: /usr/local/bin:/usr/bin
  TEMP: /tmp
  USER: username
```

---

## Testing Sequence

For any MCP server:

1. **Test underlying service**:
   ```bash
   command --version          # For binaries
   curl <url>                 # For HTTP
   npm list -g <pkg>          # For npm packages
   ```

2. **Add to Hermes**:
   ```bash
   hermes mcp add <name> [--command "..." or --url ...]
   ```

3. **List and verify**:
   ```bash
   hermes mcp list
   ```

4. **Test connection**:
   ```bash
   hermes mcp test <name>
   ```

5. **Enable and reload**:
   ```bash
   hermes config set mcp_servers.<name>.enabled true
   hermes /reset  # or /reload-mcp in session
   ```

6. **Verify tools available**:
   ```bash
   hermes tools list | grep <server>
   ```

---

## Troubleshooting by Symptom

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| "system cannot find file" | Path incorrect or not in PATH | Use `where`/`which` to find, use full path |
| "Access is denied" | Service not running or permissions | Start service, verify with direct command |
| "Connection timeout" | Service slow to start | Wait 5-30s and retry |
| "Connection refused" | Service not listening | Check service is running, verify port/socket |
| Tools not showing | Server disabled or failed to connect | Enable server, reload MCP, check logs |
| Wrong server connected | Multiple versions installed | Use full path, verify `which` output |

---

## References

- Main skill: `hermes-mcp-server-setup`
- Windows example: `references/mcp-docker-windows-example.md`
- Hermes docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
