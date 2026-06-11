# MCP Commands Reference

## Catalog
```bash
hermes mcp                    # Interactive picker
hermes mcp catalog            # Plain-text list
hermes mcp install <name>     # Install by name
```

## Configuration & Management
```bash
hermes mcp configure <name>   # Reopen tool selection checklist
hermes mcp test <name>        # Test server connection
/reload-mcp                   # Reload MCP config in chat
```

## Tool Filtering
```yaml
mcp_servers:
  <name>:
    tools:
      include: [tool1, tool2]     # Whitelist (recommended)
      # exclude: [tool3, tool4]    # Blacklist
      prompts: true
      resources: true
```

## Runtime Env Substitution
```yaml
transport:
  command: "my-server"
  args: ["--token", "${MY_PROVIDER_TOKEN}"]
```
Resolves from `~/.hermes/.env` at server-connect time.

## OAuth (Remote/Headless)
```bash
# SSH port forwarding
ssh -N -L <port>:127.0.0.1:<port> user@host
```