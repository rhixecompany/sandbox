# MCP (Model Context Protocol) — Hermes Agent

> **Source:** https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp

---

## Overview

MCP lets Hermes Agent connect to **external tool servers** (GitHub, databases, filesystems, browser stacks, internal APIs, etc.) so the agent can use tools that live outside Hermes itself.

---

## Quick Start

```bash
# Install MCP dependencies
cd ~/.hermes/hermes-agent
uv pip install -e ".[mcp]"

# Configure a filesystem server in ~/.hermes/config.yaml
mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]

# Start Hermes
hermes chat
```

**Example usage:** *"List the files in /home/user/projects and summarize the repo structure."*

---

## Catalog: One-Click Install for Nous-Approved MCPs

Hermes ships a curated catalog of MCP servers reviewed by Nous staff. Disabled by default — install only what you need.

### Commands

| Command | Description |
|---------|-------------|
| `hermes mcp` | Interactive picker (default) |
| `hermes mcp catalog` | Plain-text list, scriptable |
| `hermes mcp install <name>` | Install a catalog entry by name |

### Picker Status Indicators

```
n8n       available  Manage and inspect n8n workflows from Hermes
linear    enabled    Linear issue/project management (remote OAuth)
github    installed (disabled)  GitHub repo + PR tools
```

- **Enter** on a row → install, enable, disable, or uninstall
- Catalog entries stored under `optional-mcps/` in the hermes-agent repo
- No community submission tier; entries added by merging a PR

### Tool Selection at Install Time

After credentials configured, Hermes probes the MCP server and presents a checklist:

```
Select tools for 'linear' (SPACE toggle, ENTER confirm)
 [x] find_issues      Find issues matching a query
 [x] get_issue        Get a single issue
 [x] create_issue     Create a new issue
 [ ] delete_workspace Delete a Linear workspace
```

- Pre-checked rows come from `tools.default_enabled` in manifest
- Only checked tools end up in `mcp_servers.<name>.tools.include`
- If probe fails (server unreachable, OAuth incomplete), install still succeeds using manifest's `tools.default_enabled` or no filter
- Re-run `hermes mcp configure <name>` once server reachable to refine

### Trust Model

> **Installing a catalog entry runs whatever the manifest specifies** — `git clone`, bootstrap commands (`pip install`, `npm install`), and the MCP server's own code. Manifests are gated by PR review, **but you should still read the manifest before installing**, especially:
> - `source:` field's repository
> - `install.bootstrap:` commands
> - `transport.command:` invocation

Manifests at: [`optional-mcps/<name>/manifest.yaml`](https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps)

### Manifest Version Compatibility

- Manifests pin a `manifest_version`
- Forward-compatible: if entry requires newer version than installed Hermes, picker shows `⚠ '<name>' requires a newer Hermes`
- Run `hermes update` to install latest Hermes

### Runtime `${ENV_VAR}` Substitution

Inside `transport.command`, `transport.args`, `transport.url`, and `headers`, `${VAR}` placeholders resolve at server-connect time from environment variables (including `~/.hermes/.env`).

```yaml
# Example
transport:
  command: "my-server"
  args: ["--token", "${MY_PROVIDER_TOKEN}"]
```

> Distinct from `${INSTALL_DIR}` in catalog manifests (substituted at install-time with cloned repo path).

### Updating Tool Selection Later

```bash
hermes mcp configure linear
```
Reopens checklist with current selection pre-checked.

### Updating Catalog Manifest

```bash
hermes mcp install <name>  # Refresh after Hermes update if manifest version changed
```
To add an MCP to catalog: open PR against [`optional-mcps/`](https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps)

---

## Two Kinds of MCP Servers

### Stdio Servers (Local Subprocesses)

```yaml
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "***"
```

**Keys:** `command`, `args`, `env`

### HTTP Servers (Remote Endpoints)

```yaml
mcp_servers:
  remote_api:
    url: "https://mcp.example.com/mcp"
    headers:
      Authorization: "Bearer ***"
```

### OAuth-Authenticated HTTP Servers

Most hosted MCP servers (Linear, Sentry, Atlassian, Asana, Figma, Stripe, etc.) require OAuth 2.1.

```yaml
mcp_servers:
  linear:
    url: "https://mcp.linear.app/mcp"
    auth: oauth
```

**Flow:** On first connect, Hermes prints authorize URL, opens browser, waits for callback on local loopback port. Tokens cached at `~/.hermes/mcp-tokens/<server>.json` (0o600 perms).

#### Remote / Headless Hosts

When Hermes runs on different machine than browser:

```bash
# SSH port forwarding
ssh -N -L <port>:127.0.0.1:<port> user@host
```

See [OAuth over SSH / Remote Hosts](/docs/guides/oauth-over-ssh#mcp-servers) for full details.

---

## Configuration Reference

### Complete `mcp_servers` Schema

```yaml
mcp_servers:
  <server_name>:
    # Stdio (local subprocess)
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/path"]
    env:
      ENV_VAR: "value"
    
    # HTTP (remote)
    # url: "https://mcp.example.com/mcp"
    # headers:
    #   Authorization: "Bearer ***"
    
    # OAuth
    # auth: "oauth"
    
    # Tool filtering
    tools:
      include: [tool1, tool2]      # Whitelist (recommended)
      # exclude: [tool3, tool4]     # Blacklist
      prompts: true                # Enable prompt wrappers
      resources: true              # Enable resource wrappers
```

### Tool Filtering

| Filter | Use Case |
|--------|----------|
| `tools.include` | Whitelist — only these tools exposed (safest) |
| `tools.exclude` | Blacklist — all except these (use for dangerous actions) |
| `tools.prompts` | Enable/disable `list_prompts`, `get_prompt` wrappers |
| `tools.resources` | Enable/disable `list_resources`, `read_resource` wrappers |

---

## Verification

```bash
# Reload MCP config
/reload-mcp

# List available tools
Tell me which MCP-backed tools are available right now.
```

---

## Common Patterns

### Pattern 1: Local Project Assistant
```yaml
mcp_servers:
  fs:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/project"]
  git:
    command: "uvx"
    args: ["mcp-server-git", "--repository", "/home/user/project"]
```

### Pattern 2: GitHub Triage Assistant
```yaml
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "***"
    tools:
      include: [list_issues, create_issue, update_issue, search_code]
    prompts: false
    resources: false
```

### Pattern 3: Internal API Assistant
```yaml
mcp_servers:
  internal_api:
    url: "https://mcp.internal.example.com"
    headers:
      Authorization: "Bearer ${INTERNAL_API_TOKEN}"
    tools:
      include: [query_db, call_service]
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Server not connecting | Check `command`/`url`; verify server runs standalone first |
| OAuth fails | Ensure loopback port available; check `~/.hermes/mcp-tokens/` perms |
| Tools missing | Run `hermes mcp configure <name>`; check `tools.include` |
| Version mismatch | `hermes update` then `hermes mcp install <name>` |

---

**Source:** [Hermes Agent Docs - MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)  
**Extracted:** 2026-06-08