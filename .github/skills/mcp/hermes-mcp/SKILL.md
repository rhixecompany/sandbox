---
name: hermes-mcp
title: "Hermes MCP"
description: "MCP server lifecycle: add, configure, test, secure, troubleshoot. Built-in servers, custom stdio/HTTP, Docker gateway, security audit."
version: 2.0.0
author: "Hermes Agent"
license: MIT
tags: [imported]
metadata:
  hermes:
    tags: [imported]
---
# Hermes MCP

Complete MCP server lifecycle management. Consolidates: `hermes-mcp-server-setup`, `hermes-mcp`, `hermes-plugins-manager` (MCP parts), `mcp-security-audit`.

---

## Quick Commands

```bash
# List configured servers
hermes mcp list

# Add server (interactive)
hermes mcp add <name> --command "cmd args"
hermes mcp add <name> --url "https://endpoint/mcp"

# Test connection
hermes mcp test <name>

# Enable/disable
hermes config set mcp_servers.<name>.enabled true
hermes config set mcp_servers.<name>.enabled false

# Reload in session
/reload-mcp
# or: hermes /reset
```

---

## Server Types

### 1. stdio Command-Based

```yaml
mcp_servers:
  filesystem:
    command: mcp-server-filesystem
    args: ["--root", "/allowed/path"]
    type: stdio
    enabled: true
  sequential-thinking:
    command: mcp-server-sequential-thinking
    type: stdio
    enabled: true
  playwright:
    command: npx
    args: ["@playwright/mcp@latest"]
    type: stdio
    enabled: true
  docker:
    command: docker
    args: ["mcp", "gateway", "run", "--profile", "default"]
    env:
      LOCALAPPDATA: C:/Users/<user>/AppData/Local
      ProgramData: C:/ProgramData
      ProgramFiles: C:/Program Files
    type: stdio
    enabled: true
```

### 2. HTTP Endpoint

```yaml
mcp_servers:
  context7:
    url: https://mcp.context7.com/mcp
    headers:
      CONTEXT7_API_KEY: <key>
    type: http
    enabled: true
```

### 3. Custom with Env

```yaml
my-server:
  command: /full/path/to/command
  args: ["-arg1", "-arg2"]
  env:
    VAR_NAME: value
    PATH_VAR: /custom/path
    # Pass through from shell
    SYSTEMROOT: /c/Windows
    WINDIR: /c/Windows
    COMSPEC: /c/Windows/System32/cmd.exe
  type: stdio
  enabled: true
```

---

## Common Built-in Servers

| Server | Command | Purpose | Prerequisites |
|--------|---------|---------|---------------|
| `filesystem` | `mcp-server-filesystem` | File ops | npm package |
| `sequential-thinking` | `mcp-server-sequential-thinking` | Reasoning | npm package |
| `playwright` | `npx @playwright/mcp@latest` | Browser | npx, browsers installed |
| `docker` | `docker mcp gateway run` | Docker | Docker Desktop |
| `context7` | HTTP | Docs lookup | API key |
| `github` | `npx @modelcontextprotocol/server-github` | GitHub | Pat |
| `postgres` | `npx @anthropic-ai/server-postgres` | Database | Connection string |
| `puppeteer` | `npx @anthropic-ai/server-puppeteer` | Browser | npx |

---

## Add Server Workflow

### Phase 1: Prerequisites

```bash
# Verify service exists
where docker                    # Windows
which mcp-server-filesystem     # Unix

# Verify service runs
docker ps
mcp-server-filesystem --help
```

### Phase 2: Add

```bash
# Interactive (tests connectivity)
hermes mcp add my-server --command "cmd args"
# or
hermes mcp add my-server --url "https://endpoint/mcp"
```

### Phase 3: Test & Enable

```bash
hermes mcp test my-server
# If success:
hermes config set mcp_servers.my-server.enabled true
```

### Phase 4: Verify in Session

```bash
# Fresh session or
/reload-mcp

# Check tools
hermes tools list | grep mcp_
```

---

## Windows-Specific

| Issue | Fix |
|-------|-----|
| WinError 2 (file not found) | Use full absolute path: `C:\\Program Files\\...` or forward slashes `C:/Program Files/...` |
| WinError 5 (access denied) | Start service first (Docker Desktop), verify env vars passed |
| WinError 193 (not valid Win32) | Architecture mismatch, use correct binary |
| YAML escaping | Double backslash `C:\\\\Users\\\\...` or forward slashes `C:/Users/...` |
| Env not inherited | Explicit `env:` section in config |
| Cold start delay | Wait 5-30s for Docker, retry test |

---

## Security Audit (`mcp-security-audit`)

### Checklist

```bash
# 1. Review config for hardcoded secrets
grep -r "api_key\|password\|token" ~/.hermes/config.yaml

# 2. Verify no shell injection in args
grep -A 5 "mcp_servers:" ~/.hermes/config.yaml | grep "args:"

# 3. Check pinned versions (not @latest)
grep -B 2 -A 2 "command:" ~/.hermes/config.yaml

# 4. Verify env vars vs hardcoded
# Good: env: { KEY: value }   Bad: args: ["--key=literal"]

# 5. Approved list check
# Only these servers should be enabled by default:
# filesystem, sequential-thinking, context7, playwright, docker, github, postgres
```

### Security Rules

- **Pinned versions only** — no `@latest` in args
- **No hardcoded secrets** — use `env:` section referencing `.env`
- **No shell injection** — args as array, not string
- **Restrict filesystem roots** — `--root /specific/path`
- **HTTPS only** for HTTP servers
- **Minimal permissions** — disable unused servers

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Server not in `hermes mcp list` | Check config.yaml syntax, restart `hermes /reset` |
| `hermes mcp test` fails | Verify service running, check full path, verify env vars |
| Tools not appearing | Enable server, `/reload-mcp`, fresh session |
| Connection timeout | Service cold start — wait and retry |
| WinError 2 | Full absolute path required on Windows |
| Tool list missing MCP tools | Check `tools.include` in config.yaml |
| Permission denied | Start underlying service (Docker, etc.) |

---

## Verification

```bash
# 1. All servers listed
hermes mcp list

# 2. 6+ enabled
grep "enabled: true" ~/.hermes/config.yaml | grep -c "true"

# 3. 200+ tools
hermes tools list | grep -c "mcp_"

# 4. Test each
for s in filesystem sequential-thinking context7 playwright docker; do
  hermes mcp test $s
done

# 5. Security
# No hardcoded secrets, pinned versions, HTTPS only
```

---

## When to Use

- Adding/removing MCP servers
- Configuring MCP environment variables
- Testing MCP connectivity
- Security audit of MCP configs
- Troubleshooting MCP registration
- **Triggers**: "mcp server", "add mcp", "test mcp", "mcp security", "hermes mcp", "configure mcp"

---

## Skills Required

| Skill | Purpose | When Needed |
|-------|---------|-------------|
| `hermes-setup` | Initial Hermes configuration | Before adding MCP servers |
| `hermes-hooks` | Session logging for audit | Tracking MCP changes |
| `hermes-profiles` | Profile-specific MCP config | Per-profile server configs |
| `hermes-plugins` | Plugin-managed servers | When plugins add MCP servers |
| `mcp-security-audit` | Security validation | After any config change |

---

## Pitfalls

| Pitfall | Severity | Mitigation |
|---------|----------|------------|
| Using `@latest` in args | Critical | Pin exact versions (e.g., `@1.2.3`) |
| Hardcoding secrets in config.yaml | Critical | Use `env:` section with `.env` references |
| Relative paths in hooks.json | High | Use absolute paths only |
| Missing `env:` for Windows env vars | High | Explicitly pass SYSTEMROOT, WINDIR, COMSPEC |
| Not testing after config change | High | Run `hermes mcp test <server>` every time |
| Enabling unused servers | Medium | Disable servers not actively needed |
| Forgetting `/reload-mcp` after changes | Medium | Always reload or start fresh session |
| HTTP servers without HTTPS | Medium | Only HTTPS endpoints allowed |
| Filesystem root too broad | Medium | Restrict to specific project paths |

---

## Verification Checklist

- [ ] Frontmatter complete: name, title, description, version, author, license, tags
- [ ] Skills Required table present
- [ ] Phased workflow with 4 clear phases (Prerequisites → Add → Test/Enable → Verify)
- [ ] Pitfalls table with ≥5 entries covering critical/high/medium
- [ ] Verification checklist present
- [ ] Reference files exist in `references/`
- [ ] No placeholder text (`[Add ... here]`)
- [ ] Concrete YAML examples for each server type
- [ ] Windows-specific troubleshooting table
- [ ] Security audit checklist included

---

## References

- `references/commands.md` — Complete CLI command reference
- `references/config-examples.md` — Full config.yaml examples for all server types
- `references/windows-interactive-add.md` — Windows interactive add workflow
- `references/wsl2-bridge.md` — WSL2 to Windows Docker bridge setup
- `references/mcp-memory-knowledge-graph.md` — Knowledge graph API for @modelcontextprotocol/server-memory (entity/relation modeling, tools reference, native vs MCP comparison)