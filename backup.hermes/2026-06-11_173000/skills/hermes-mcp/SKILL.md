---
name: hermes-mcp
description: MCP catalog, server configuration, tool filtering, and WSL2 bridge patterns
version: 1.0.0
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [hermes, mcp, model-context-protocol]
    category: mcp
    requires_toolsets: [terminal, file, skills]
    config:
      - key: hermes.skill.mcp.enabled
        description: "Enable MCP skill"
        default: "true"
---

# Hermes MCP (Model Context Protocol) Skill

## When to Use
- Connecting to external tool servers (GitHub, filesystem, browsers, APIs)
- Installing Nous-approved MCP servers from catalog
- Configuring tool filtering (whitelist/blacklist)
- Setting up WSL2 → Windows Chrome bridge

## Procedure
- **Installing MCP Dependencies**:
  ```bash
  cd ~/.hermes/hermes-agent
  uv pip install -e ".[mcp]"
  ```

- **Browsing / Adding Servers**:
  ```bash
  hermes mcp catalog      # Plain-text list
  hermes mcp add          # Add a server entry (may prompt for auth)
  ```
  - `hermes mpc install <name>` is *not* validated in this skill; use `add` + `command` + `args`.
  - `hermes mcp add ...` is interactive on Windows (prompts for “Does this server require authentication?”).
  - Do **not** run `hermes mcp add ...` unattended in an automated step — it will block waiting for stdin.

- **Directly adding a local/bundled MCP server** (preferred on Windows):
  ```bash
  hermes mcp add <name> --command <cmd> --args <args...>
  # examples
  hermes mcp add playwright --command npx --args "-y" "@playwright/mcp@latest"
  hermes mcp add github --command npx --args "-y" "@modelcontextprotocol/server-github"
  ```
  - If it prompts, stop and handle manually or switch to writing into `config.yaml` directly.
  - For non-interactive/fleet setup, configure `mcp_servers:` in config.yaml and reload; don’t loop `hermes mcp add` in automation.

- **Configuring Custom Servers** (config.yaml):
  ```yaml
  mcp_servers:
    fs:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-filesystem", "/path"]
      tools:
        include: [list_files, read_file, write_file]
    
    github:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-github"]
      env:
        GITHUB_PERSONAL_ACCESS_TOKEN: "${GITHUB_TOKEN}"
      tools:
        include: [list_issues, create_issue, search_code]
    
    # WSL2 → Windows Chrome bridge
    chrome-devtools-win:
      command: "cmd.exe"
      args: ["/c", "npx", "-y", "chrome-devtools-mcp@latest", "--autoConnect", "--no-usage-statistics"]
  ```

- **Tool Filtering Strategy**:
  - **Whitelist** (`tools.include`): only these tools exposed (safest, recommended)
  - **Blacklist** (`tools.exclude`): all except these (for dangerous actions)
  - **Prompts/Resources**: `tools.prompts`, `tools.resources` (enable wrappers)

- **Runtime Env Substitution**: `${VAR}` in command/args/url/headers resolves from `~/.hermes/.env`

- **Verify & Reload**:
  ```bash
  /reload-mcp
  hermes mcp test <name>
  ```

- **Common Patterns**:
  - **Pattern 1: Local Project Assistant** — filesystem + git servers for local repo
  - **Pattern 2: GitHub Triage Assistant** — github server with whitelisted tools
  - **Pattern 3: Internal API Assistant** — HTTP server with Bearer token
  - **Pattern 4: Fleet/scripted Windows setup** — write `config.yaml` directly; avoid automated `hermes mcp add` loops.

## Pitfalls
- **Server not connecting** → Check `command`/`url`; verify server runs standalone first
- **OAuth fails** → Ensure loopback port available; check `~/.hermes/mcp-tokens/` perms
- **Tools missing** → Run `hermes mcp configure <name>`; check `tools.include`
- **Version mismatch** → `hermes update` then `hermes mcp install <name>`
- **WSL2 path mapping** → Use `chrome-devtools-mcp --autoConnect`

## Verification
- `hermes mcp catalog` lists available servers
- `/reload-mcp` succeeds
- `hermes mcp test <server>` passes
- MCP tools appear in `hermes tools --platform cli | grep mcp-`

## References
- `references/commands.md` — CLI commands
- `references/config-examples.md` — Complete config.yaml examples
- `references/wsl2-bridge.md` — WSL2 → Windows Chrome setup