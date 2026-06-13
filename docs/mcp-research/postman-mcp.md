# Postman MCP Server (Local)

**Source:** https://learning.postman.com/docs/reference/postman-api/postman-mcp-server/postman-mcp-local-server

## Overview

The **local Postman MCP server** runs on **STDIO transport** and is hosted locally on your environment. It's a lightweight solution ideal for integration with editors and tools like **Visual Studio Code**.

### Key Characteristics

- **Authentication:** Only supports API key authentication (Postman API key or Bearer token)
- **Transport:** STDIO-based
- **Prerequisites:** Node.js required to run as Node application
- **Region:** Defaults to `us`; use `--region` flag or `POSTMAN_API_BASE_URL` env var for `eu`

## Use Cases

Consider the local server when you:
- Want to power **local API testing**
- Have **specific security and network requirements**
- Prefer to **build from source code** (repo available)
- Work with **internal APIs**

## Supported Configurations

| Configuration | Description |
|---------------|-------------|
| **Minimal** (Default) | Essential tools for basic Postman operations only |
| **Code** | Tools for searching public/internal API definitions + generating client code |
| **Full** | All 100+ available Postman API tools |
| **Quiet** | Suppresses `debug`/`info` logs (stderr); returns only `warn`/`error`. **Required for Windsurf on Windows** to avoid stderr pipe buffer deadlock. Can combine with Minimal, Code, or Full |

> **Region flag:** Use `--region us|eu` or set `POSTMAN_API_BASE_URL` environment variable directly.

## Installation by Tool

### Claude Code

```bash
# Minimal
claude mcp add postman --env POSTMAN_API_KEY=*** npx @postman/postman-mcp-server@latest

# Code
claude mcp add postman --env POSTMAN_API_KEY=*** npx @postman/postman-mcp-server@latest --code

# Full
claude mcp add postman --env POSTMAN_API_KEY=*** npx @postman/postman-mcp-server@latest --full
```

### Cursor

**One-click install:** [Install in Cursor](https://cursor.com/en/install-mcp?name=postman-api-mcp&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyJAcG9zdG1hbi9wb3N0bWFuLW1jcC1zZXJ2ZXIiLCItLWZ1bGwiXSwiZW52Ijp7IlBPU1RNQU5fQVBJX0tFWSI6IllPVVJfQVBJX0tFWSJ9fQ%3D%3D)

**Manual** (`.vscode/mcp.json`):
```json
{
  "servers": {
    "postman-api-mcp": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "@postman/postman-mcp-server",
        "--full",        // optional: full mode
        "--code",        // optional: code mode
        "--region us"    // optional: us or eu (default: us)
      ],
      "env": {
        "POSTMAN_API_KEY": "${input:postman-api-key}"
      }
    }
  },
  "inputs": [
    {
      "id": "postman-api-key",
      "type": "promptString",
      "description": "Enter your Postman API key"
    }
  ]
}
```
> Default: **Full** mode. Remove `--full` for Minimal; replace with `--code` for Code mode.

### Visual Studio Code

**One-click install:** [Install in VS Code](https://insiders.vscode.dev/redirect/mcp/install?name=postman-api-mcp&inputs=%5B%7B%22id%22%3A%22postman-api-key%22%2C%22type%22%3A%22promptString%22%2C%22description%22%3A%22Enter%20your%20Postman%20API%20key%22%7D%5D&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22%40postman%2Fpostman-mcp-server%22%2C%22--full%22%5D%2C%22env%22%3A%7B%22POSTMAN_API_KEY%22%3A%22%24%7Binput%3Apostman-api-key%7D%22%7D%7D)

**Manual** (`mcp.json`):
```json
{
  "servers": {
    "postman": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "@postman/postman-mcp-server",
        "--full",        // optional: full mode
        "--code",        // optional: code mode
        "--region us"    // optional: us or eu (default: us)
      ],
      "env": {
        "POSTMAN_API_KEY": "${input:postman-api-key}"
      }
    }
  },
  "inputs": [
    {
      "id": "postman-api-key",
      "type": "promptString",
      "description": "Enter your Postman API key"
    }
  ]
}
```

### Claude Desktop

Download `.mcpb` file from [latest release](https://github.com/postmanlabs/postman-mcp-server/releases):

| Mode | File |
|------|------|
| Minimal | `postman-api-mcp-minimal.mcpb` |
| Code | `postman-mcp-server-code.mcpb` |
| Full | `postman-api-mcp-full.mcpb` |

See [Claude Desktop Extensions](https://www.anthropic.com/engineering/desktop-extensions) docs.

### Codex

```bash
# Minimal
codex mcp add postman --env POSTMAN_API_KEY=*** npx @postman/postman-mcp-server --minimal

# Code
codex mcp add postman --env POSTMAN_API_KEY=*** npx @postman/postman-mcp-server --code

# Full
codex mcp add postman --env POSTMAN_API_KEY=*** npx @postman/postman-mcp-server --full
```

### Windsurf

**GUI Install:**
1. Click **Open MCP Marketplace**
2. Search "Postman"
3. Click **Install**
4. Enter Postman API key
5. Select tools (or **All Tools**)
6. Turn on **Enabled**

> **Windows users:** Use `--quiet` flag to avoid startup timeout from stderr buffer deadlock.

**Manual** (`.codeium/windsurf/mcp_config.json`):
```json
{
  "mcpServers": {
    "postman": {
      "args": [
        "@postman/postman-mcp-server",
        "minimal"        // default; or "--full", "--code", "--quiet"
      ],
      "env": {
        "POSTMAN_API_KEY": "your-api-key"
      }
    }
  }
}
```

## Hermes Integration

For Hermes Agent (NPX mode):

```yaml
mcp_servers:
  postman:
    command: "npx"
    args: ["@postman/postman-mcp-server", "--full", "--region", "us"]
    env:
      POSTMAN_API_KEY: "${POSTMAN_API_KEY}"
    tools:
      include: [get_workspaces, get_collections, get_environments, create_collection, update_collection, run_collection, search_apis]
```

Then run:
```bash
hermes mcp test postman
/reload-mcp
```

## References

- Postman Docs: https://learning.postman.com/docs/reference/postman-api/postman-mcp-server/postman-mcp-local-server
- GitHub: https://github.com/postmanlabs/postman-mcp-server
- mcpservers.org: https://mcpservers.org/servers/postmanlabs/postman-api-mcp
- Releases: https://github.com/postmanlabs/postman-mcp-server/releases