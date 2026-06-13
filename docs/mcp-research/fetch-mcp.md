# Fetch MCP Server

**Source:** https://github.com/modelcontextprotocol/servers/blob/main/src/fetch/README.md

## Overview

**Fetch MCP Server** is a Model Context Protocol server that provides web content fetching capabilities, enabling LLMs to retrieve and process content from web pages with HTML-to-markdown conversion.

> ⚠️ **Security Caution**: This server can access local/internal IP addresses and may represent a security risk. Exercise caution to ensure sensitive data is not exposed.

## Available Tools

### `fetch` - Primary Tool

Fetches a URL and extracts contents as markdown.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `url` | string | ✅ | - | URL to fetch |
| `max_length` | integer | ❌ | 5000 | Maximum characters to return |
| `start_index` | integer | ❌ | 0 | Start content from this character index |
| `raw` | boolean | ❌ | false | Get raw content without markdown conversion |

**Key Feature:** The `start_index` parameter enables chunked reading of large webpages.

## Available Prompts

### `fetch` Prompt

- **Purpose:** Fetch a URL and extract contents as markdown
- **Arguments:** `url` (string, required)

## Installation

### Prerequisites

- **Optional:** Node.js (enables more robust HTML simplifier)

### Method 1: Using uv (Recommended)

```bash
# No installation needed - run directly with uvx
uvx mcp-server-fetch
```

### Method 2: Using pip

```bash
pip install mcp-server-fetch
python -m mcp_server_fetch
```

## Configuration

### For Claude.app

| Method | Configuration |
|--------|---------------|
| **uvx** | ```json<br>{"mcpServers": {"fetch": {"command": "uvx", "args": ["mcp-server-fetch"]}}}<br>``` |
| **Docker** | ```json<br>{"mcpServers": {"fetch": {"command": "docker", "args": ["run", "-i", "--rm", "mcp/fetch"]}}}<br>``` |
| **pip** | ```json<br>{"mcpServers": {"fetch": {"command": "python", "args": ["-m", "mcp_server_fetch"]}}}<br>``` |

### For VS Code

#### One-Click Install Buttons

- [Install with UV in VS Code](https://insiders.vscode.dev/redirect/mcp/install?name=fetch&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22mcp-server-fetch%22%5D%7D)
- [Install with UV in VS Code Insiders](https://insiders.vscode.dev/redirect/mcp/install?name=fetch&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22mcp-server-fetch%22%5D%7D&quality=insiders)
- [Install with Docker in VS Code](https://insiders.vscode.dev/redirect/mcp/install?name=fetch&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22--rm%22%2C%22mcp%2Ffetch%22%5D%7D)
- [Install with Docker in VS Code Insiders](https://insiders.vscode.dev/redirect/mcp/install?name=fetch&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22--rm%22%2C%22mcp%2Ffetch%22%5D%7D&quality=insiders)

#### Manual Configuration (User Settings JSON)

```json
// Using uvx
{
  "mcp": {
    "servers": {
      "fetch": {
        "command": "uvx",
        "args": ["mcp-server-fetch"]
      }
    }
  }
}

// Using Docker
{
  "mcp": {
    "servers": {
      "fetch": {
        "command": "docker",
        "args": ["run", "-i", "--rm", "mcp/fetch"]
      }
    }
  }
}
```

> **Note:** The `mcp` key is required when using `.vscode/mcp.json` workspace file.

## Customization Options

### robots.txt Compliance

- **Default behavior:** Obeys robots.txt for model-initiated requests (tools), ignores for user-initiated requests (prompts)
- **Disable:** Add `--ignore-robots-txt` to args

### User-Agent Strings

| Request Type | Default User-Agent |
|--------------|-------------------|
| Model-initiated (tool) | `ModelContextProtocol/1.0 (Autonomous; +https://github.com/modelcontextprotocol/servers)` |
| User-initiated (prompt) | `ModelContextProtocol/1.0 (User-Specified; +https://github.com/modelcontextprotocol/servers)` |

**Customize:** Add `--user-agent=YourUserAgent` to args

### Proxy Configuration

```bash
--proxy-url=http://your-proxy:port
```

## Windows-Specific Configuration

For timeout issues on Windows, set `PYTHONIOENCODING=utf-8`:

```json
// uvx on Windows
{
  "mcpServers": {
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"],
      "env": {"PYTHONIOENCODING": "utf-8"}
    }
  }
}

// pip on Windows
{
  "mcpServers": {
    "fetch": {
      "command": "python",
      "args": ["-m", "mcp_server_fetch"],
      "env": {"PYTHONIOENCODING": "utf-8"}
    }
  }
}
```

## Debugging

### MCP Inspector

```bash
# For uvx installations
npx @modelcontextprotocol/inspector uvx mcp-server-fetch

# For local development
cd path/to/servers/src/fetch
npx @modelcontextprotocol/inspector uv run mcp-server-fetch
```

## Contributing

- Contributions welcome: new tools, enhancements, bug fixes, documentation
- Reference other MCP servers: https://github.com/modelcontextprotocol/servers
- Pull requests encouraged

## License

**MIT License** - Free to use, modify, and distribute per MIT terms. See LICENSE file in repository.

## Hermes Integration

For Hermes Agent (uvx mode):

```yaml
mcp_servers:
  fetch:
    command: "uvx"
    args: ["mcp-server-fetch"]
    env:
      PYTHONIOENCODING: "utf-8"
    tools:
      include: [fetch]
```

For Docker mode:
```yaml
mcp_servers:
  fetch:
    command: "docker"
    args: ["run", "-i", "--rm", "mcp/fetch"]
    tools:
      include: [fetch]
```

Then run:
```bash
hermes mcp test fetch
/reload-mcp
```

## References

- GitHub: https://github.com/modelcontextprotocol/servers/tree/main/src/fetch
- mcpservers.org: https://mcpservers.org/servers/zcaceres/fetch-mcp
- PulseMCP: https://www.pulsemcp.com/servers/modelcontextprotocol-fetch