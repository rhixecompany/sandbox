# Tool Commands Reference

## Toolset Management
```bash
hermes tools                              # Interactive config
hermes tools --platform cli              # List for CLI
hermes chat --toolsets "web,terminal"    # Use specific toolsets
```

## Platform Presets
- `hermes-cli` — CLI default
- `hermes-telegram` — Telegram bot
- `mcp-<server>` — Dynamic MCP toolsets

## Common Toolsets
`web`, `search`, `terminal`, `file`, `browser`, `vision`, `image_gen`, `moa`, `skills`, `tts`, `todo`, `memory`, `session_search`, `cronjob`, `code_execution`, `delegation`, `clarify`, `homeassistant`, `messaging`, `spotify`, `discord`, `discord_admin`, `debugging`, `safe`

## MCP Integration
```bash
hermes tools --platform cli | grep mcp-   # List MCP-backed tools
/reload-mcp                               # Reload MCP config
```

## Terminal Backend Config
```yaml
terminal:
  backend: local        # local, docker, ssh, singularity, modal, daytona
  cwd: "."
  timeout: 180
  # Docker:
  # docker_image: python:3.11-slim
  # SSH (set in ~/.hermes/.env):
  # TERMINAL_SSH_HOST=...
  # TERMINAL_SSH_USER=...
  # TERMINAL_SSH_KEY=~/.ssh/id_ed25519
```