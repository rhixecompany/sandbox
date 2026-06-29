# MCP Server Integration

> Extracted from `mcp-create-declarative-agent.prompt.md`.

## MCP Server Integration

### Supported MCP Endpoints
The MCP server must provide:
- **Server metadata** endpoint
- **Tools listing** endpoint (exposes available functions)
- **Tool execution** endpoint (handles function calls)

### Tool Selection
When importing from MCP:
1. Fetch available tools from server
2. Select specific tools to include (for security/simplicity)
3. Tool definitions are auto-generated in ai-plugin.json

### Authentication Types

**OAuth 2.0 (Static Registration)**
```json
"auth": {
  "type": "OAuthPluginVault",
  "reference_id": "${{OAUTH_REFERENCE_ID}}",
  "authorization_url": "https://auth.service.com/authorize",
  "client_id": "${{CLIENT_ID}}",
  "client_secret": "${{CLIENT_SECRET}}",
  "scope": "read write"
}
```

**Single Sign-On (SSO)**
```json
"auth": {
  "type": "SSO"
}
```
