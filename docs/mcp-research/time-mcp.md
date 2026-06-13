# Time MCP Server

**Source:** https://github.com/modelcontextprotocol/servers/tree/main/src/time

## Overview

**Time MCP Server** is a Model Context Protocol server providing time and timezone conversion capabilities. It enables LLMs to get current time information and perform timezone conversions using IANA timezone names, with automatic system timezone detection.

**Repository:** `modelcontextprotocol/servers/src/time`
**License:** MIT License

## Available Tools

| Tool | Parameters | Description |
|------|------------|-------------|
| `get_current_time` | `timezone` (optional) | Get current time in a specific timezone or system timezone |
| `convert_time` | `source_timezone`, `time`, `target_timezone` | Convert time between timezones |

## Installation

### Using uv (Recommended)

```bash
# No installation needed - run directly with uvx
uvx mcp-server-time
```

### Using pip

```bash
pip install mcp-server-time
# Then run as script
mcp-server-time
```

## Configuration

### Configuration Format (JSON)

```json
{
  "command": "uvx",
  "args": ["mcp-server-time"]
}
```

### Editor-Specific Setup

#### Claude.app

Add to Claude settings.

#### Zed

Add to `settings.json`.

#### VS Code

**Quick Install Buttons:**
- [Install with UV](https://insiders.vscode.dev/redirect/mcp/install?name=time&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22mcp-server-time%22%5D%7D)
- [Install with UV (Insiders)](https://insiders.vscode.dev/redirect/mcp/install?name=time&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22mcp-server-time%22%5D%7D&quality=insiders)
- [Install with Docker](https://insiders.vscode.dev/redirect/mcp/install?name=time&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22--rm%22%2C%22mcp%2Ftime%22%5D%7D)
- [Install with Docker (Insiders)](https://insiders.vscode.dev/redirect/mcp/install?name=time&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22--rm%22%2C%22mcp%2Ftime%22%5D%7D&quality=insiders)

**Manual Installation:**
1. Press `Ctrl + Shift + P` → `Preferences: Open User Settings (JSON)`
2. Add configuration to User Settings or `.vscode/mcp.json` (workspace-level)

> **Note:** The `mcp` key is required when using `.vscode/mcp.json`

#### Zencoder

1. Go to `Agent Tools`
2. Click `Add Custom MCP`
3. Click `Install`

## Customization

### Override System Timezone

By default, the server auto-detects system timezone. Override with `--local-timezone`:

```json
{
  "command": "uvx",
  "args": ["mcp-server-time", "--local-timezone", "America/New_York"]
}
```

## Example Interactions

### Get Current Time

**Request:** `get_current_time` with `timezone: "America/Los_Angeles"`
**Response:** Current time in Pacific Time

### Convert Time

**Request:** `convert_time` with:
- `source_timezone: "UTC"`
- `time: "14:30"`
- `target_timezone: "America/New_York"`
**Response:** Converted time in Eastern Time

## Debugging

### Using MCP Inspector

```bash
# For uvx installations
npx @modelcontextprotocol/inspector uvx mcp-server-time

# For local development
npx @modelcontextprotocol/inspector python -m mcp_server_time
```

## Build

### Docker Build

```bash
docker build -t mcp/time .
docker run -i --rm mcp/time
```

## Project Structure

```
src/time/
├── src/mcp_server_time/    # Main source code
├── test/                   # Test files
├── .python-version         # Python version specification
├── Dockerfile              # Container configuration
├── pyproject.toml          # Project metadata & dependencies
├── uv.lock                 # uv lock file
└── README.md               # This documentation
```

## Contributing

Contributions welcome! Areas for contribution:
- New time-related tools
- Enhanced existing functionality
- Documentation improvements

**Reference:** See other MCP servers at <https://github.com/modelcontextprotocol/servers>

**Process:** Submit pull requests with new ideas, bug fixes, or enhancements.

## License

**MIT License** - Free to use, modify, and distribute per MIT terms. See LICENSE file in repository for details.

## Hermes Integration

For Hermes Agent (uvx mode):

```yaml
mcp_servers:
  time:
    command: "uvx"
    args: ["mcp-server-time", "--local-timezone", "America/New_York"]
    tools:
      include: [get_current_time, convert_time]
```

For Docker mode:
```yaml
mcp_servers:
  time:
    command: "docker"
    args: ["run", "-i", "--rm", "mcp/time"]
    tools:
      include: [get_current_time, convert_time]
```

Then run:
```bash
hermes mcp test time
/reload-mcp
```

## References

- GitHub: https://github.com/modelcontextprotocol/servers/tree/main/src/time
- mcp-get.com: https://mcp-get.com/packages/mcp-server-time
- mcpservers.org: https://mcpservers.org/servers/Taki-Ta/mcp-server-time
- LobeHub: https://lobehub.com/mcp/foxlauren-mcp-time-server