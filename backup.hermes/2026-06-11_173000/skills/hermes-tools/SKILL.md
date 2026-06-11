---
name: hermes-tools
description: Toolset configuration, terminal backends, and built-in tool reference
version: 1.0.0
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [hermes, tools, toolsets, terminal]
    category: tools
    requires_toolsets: [terminal, file, skills]
    config:
      - key: hermes.skill.tools.enabled
        description: "Enable tools configuration skill"
        default: "true"
---

# Hermes Tools & Toolsets Skill

## When to Use
- Configuring toolsets for specific workflows
- Switching terminal backends (local, docker, ssh, modal, daytona)
- Understanding available tool categories
- Troubleshooting tool availability

## Procedure
1. **View Available Tools**:
   ```bash
   hermes tools                    # Interactive config
   hermes tools --platform cli     # List for CLI
   hermes chat --toolsets "web,terminal,file,skills,mcp,memory"
   ```

2. **Common Toolset Patterns**:
   ```bash
   # Minimal CLI
   hermes chat --toolsets "web,terminal"
   
   # Full Coding Agent
   hermes chat --toolsets "web,terminal,file,browser,skills,code_execution,delegation,memory"
   
   # Research Only
   hermes chat --toolsets "web,search,skills,memory,session_search"
   
   # Bot with Messaging
   hermes chat --toolsets "web,terminal,file,skills,messaging" --platform telegram
   ```

3. **Terminal Backends** (config.yaml):
   ```yaml
   terminal:
     backend: local        # or: docker, ssh, singularity, modal, daytona
     cwd: "."
     timeout: 180
   
   # Docker (persistent sandbox)
   # backend: docker
   # docker_image: python:3.11-slim
   
   # SSH (recommended for security)
   # backend: ssh
   # TERMINAL_SSH_HOST=... in ~/.hermes/.env
   ```

4. **MCP Tool Integration**:
   ```bash
   hermes tools --platform cli | grep mcp-
   ```

## Pitfalls
- **Tool not available** → Check `hermes tools` — is toolset enabled for platform?
- **Terminal fails** → Check backend config; try `local` first
- **Browser not working** → Ensure `npx` available; try `browser_vision` for debug
- **MCP tools missing** → `/reload-mcp`; check `tools.include` in config
- **Image gen fails** → Verify tool gateway or provider credentials

## Verification
- `hermes tools` shows expected toolsets
- Terminal executes commands in configured backend
- MCP tools appear after `/reload-mcp`

## References
- `references/commands.md` — CLI commands
- `references/tool-categories.md` — 9 tool categories table
- `references/backends.md` — Terminal backend comparison