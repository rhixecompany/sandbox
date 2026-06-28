# MCP Coding Agent Setup — Quick Reference

## Server Commands

| Server | Status Check | Tool Count |
|--------|-------------|------------|
| MindStudio | `hermes mcp test mindstudio` | 197 |
| Codex CLI | `hermes mcp test codex` | 2 |
| Copilot MCP | `hermes mcp test copilot-mcp` | 1 |

## Config Snippet

```yaml
mcp_servers:
  mindstudio:
    command: mindstudio
    args: [mcp]
    enabled: true
```

## Common Issues

- Copilot hangs → add `--allow-all` flag
- Codex usage limit → upgrade or wait for reset
- MCP not visible after config change → `hermes mcp list` + reload session
