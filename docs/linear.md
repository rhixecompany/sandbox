# MCP Server – Linear Docs: Comprehensive Summary

## Overview

Linear provides a **Model Context Protocol (MCP) server** that offers a standardized, secure interface for AI models and agents to access Linear data. The server is **centrally hosted and managed**, following the authenticated remote MCP specification.

**Key Endpoint**:
`https://mcp.linear.app/mcp`

**Core Capabilities**:
- Find, create, and update Linear objects (issues, projects, comments)
- More functionality in development
- Supports **Streamable HTTP transports** with **OAuth 2.1** and dynamic client registration

---

## Supported Clients & Setup Instructions

### General Configuration
- **Transport**: Streamable HTTP
- **Authentication**: OAuth 2.1 with dynamic client registration
- **Endpoint**: `https://mcp.linear.app/mcp`

---

### Claude

#### Team, Enterprise (Claude.ai)
- Navigate to [connectors page](https://claude.ai/customize/connectors) and connect Linear

#### Free, Pro (Claude Desktop)
- Go to **Settings > Connectors** and add the Linear connector

---

### Claude Code

**Setup Command**:
```bash
claude mcp add --transport http linear-server https://mcp.linear.app/mcp
```

**Authentication**:
Run `/mcp` in a Claude Code session to complete the authentication flow.

---

### Codex

#### CLI Configuration
```bash
codex mcp add linear --url https://mcp.linear.app/mcp
```

**First-time Setup Requirement**:
Enable `rmcp` feature in `~/.codex/config.toml`:
```toml
[features]
experimental_use_rmcp_client = true
```

#### Environment Variable Configuration
Add to `~/.codex/config.toml`:
```toml
[features]
experimental_use_rmcp_client = true

[mcp_servers.linear]
url = "https://mcp.linear.app/mcp"
```

**Authentication**:
```bash
codex mcp login linear
```

---

### Cursor
- **One-click install**: [Install Linear MCP](cursor://anysphere.cursor-deeplink/mcp/install?name=Linear&config=eyJ...)
- Or search for Linear in Cursor's [MCP tools directory](https://cursor.com/docs/context/mcp/directory)

---

### Visual Studio Code

**Configuration** (add to settings):
```json
{
  "mcpServers": {
    "linear": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.linear.app/mcp"]
    }
  }
}
```

**Alternative Command**:
```bash
npx mcp-remote https://mcp.linear.app/mcp
```

---

### v0 by Vercel
- Install from the [connections page](https://v0.app/chat/settings/mcp-connections)

---

### Windsurf

**Configuration**:
```json
{
  "mcpServers": {
    "linear": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.linear.app/mcp"]
    }
  }
}
```

---

### Zed

**Configuration**:
```json
{
  "context_servers": {
    "linear": {
      "source": "custom",
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.linear.app/mcp"],
      "env": {}
    }
  }
}
```

---

### Other Clients
For any MCP-compatible tool, use:
```bash
npx -y mcp-remote https://mcp.linear.app/mcp
```

---

## Frequently Asked Questions (FAQ)

### Clearing Authentication Issues
**Problem**: Saved auth info causing connection failures
**Solution**:
```bash
rm -rf ~/.mcp-auth
```
Then retry the connection. Ensure you're using an up-to-date Node.js version if issues persist.

---

### WSL (Windows Subsystem for Linux) Configuration
Use this alternative configuration:
```json
{
  "mcpServers": {
    "linear": {
      "command": "wsl",
      "args": ["npx", "-y", "mcp-remote", "https://mcp.linear.app/sse", "--transport sse-only"]
    }
  }
}
```

---

### Remote MCP Support
✅ **Yes**, Linear's MCP server is available at:
`https://mcp.linear.app/mcp`

---

### Direct Token Authentication
The MCP server supports passing credentials directly via the `Authorization` header:
```
Authorization: Bearer <yourtoken>
```

**Use Cases**:
- Interact as an `app` user
- Provide read-only access via restricted API key
- Integrate with existing Linear OAuth applications without interactive login

---

## Key Features & Integrations

### Core Functionalities
- **Assign and delegate issues**
- **Triage Intelligence**
- **Code Intelligence**

### Supported Integrations
Linear integrates with numerous platforms including:
- **Communication**: Slack, Discord, Microsoft Teams, Intercom, Front, Gong
- **Development**: GitHub, GitLab, Sentry, Jira, Airbyte
- **Productivity**: Notion, Google Sheets, Zapier
- **Design**: Figma
- **CRM**: Salesforce, Zendesk

---

## Important Notes
- Linear welcomes [feedback](https://linear.app/contact/support) on MCP server functionality
- The server follows the [MCP specification](https://modelcontextprotocol.io/specification/2025-03-26)
- Backwards compatibility available via [`mcp-remote`](https://github.com/geelen/mcp-remote) module for clients without native remote MCP support
