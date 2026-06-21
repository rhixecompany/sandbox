# Desktop Commander MCP

**Source:** <https://github.com/wonderwhy-er/DesktopCommanderMCP>

## Overview

**MCP Server for Claude** that provides terminal control, file system search, and diff file editing capabilities. Built on [MCP Filesystem Server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem).

## What It Enables

Desktop Commander enables AI assistants (Claude Desktop, Cursor, Windsurf, VS Code, etc.) to:

- Execute terminal commands and manage long-running processes
- Search, read, write, and edit files with surgical precision
- Work across your entire OS, not just within an IDE
- Use your existing Claude Pro subscription ($20/mo) — **no API costs**

**Key differentiator:** Unlike Cursor/Windsurf, Claude reads files in full, works across multiple projects simultaneously, and executes changes in one go.

## Features

| Category          | Capabilities                                                                |
| ----------------- | --------------------------------------------------------------------------- |
| **Terminal**      | Start/interact with processes, list sessions, kill processes, SSH support   |
| **Filesystem**    | Read/write files (text, Excel, PDF, URLs), list directories, search content |
| **Text Editing**  | Surgical search/replace with fuzzy matching and diff preview                |
| **Configuration** | Runtime config management via MCP tools                                     |
| **Analytics**     | Usage stats, tool call history, feedback submission                         |
| **Preview UI**    | Rich file previews, Markdown editor, directory browser in Claude Desktop    |

## Installation Methods

### Option 1: NPX (Recommended) ✅ Auto-updates

```bash
npx @wonderwhy-er/desktop-commander@latest setup
# Debug mode:
npx @wonderwhy-er/desktop-commander@latest setup --debug
# Uninstall:
npx @wonderwhy-er/desktop-commander@latest remove
```

### Option 2: Bash Installer ✅ Auto-updates

```bash
curl -fsSL https://raw.githubusercontent.com/wonderwhy-er/DesktopCommanderMCP/refs/heads/main/install.sh | bash
```

### Option 3: Smithery ✅ Auto-updates

```bash
npx -y @smithery/cli install @wonderwhy-er/desktop-commander --client claude
```

### Option 4: Manual Config ✅ Auto-updates

Add to `claude_desktop_config.json`:

```json
{
	"mcpServers": {
		"desktop-commander": {
			"command": "npx",
			"args": ["-y", "@wonderwhy-er/desktop-commander@latest"]
		}
	}
}
```

**Config locations:**

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- Linux: `~/.config/Claude/claude_desktop_config.json`

### Option 5: Git Clone ❌ Manual updates

```bash
git clone https://github.com/wonderwhy-er/DesktopCommanderMCP
cd DesktopCommanderMCP && npm run setup
# Update: cd DesktopCommanderMCP && git pull && npm run setup
```

### Option 6: Docker ✅ Auto-updates (isolated)

```bash
# macOS/Linux
docker run -d --name desktop-commander \
  -v /path/to/work:/work \
  mcp/desktop-commander:latest

# Windows PowerShell
docker run -d --name desktop-commander `
  -v C:\path\to\work:/work `
  mcp/desktop-commander:latest
```

**Prerequisites:** Docker Desktop installed and running.

## Other MCP Clients

| Client           | Config Location                                                                             | Quick Install                                                                                                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cursor**       | `~/.cursor/mcp.json` or `.cursor/mcp.json`                                                  | [One-click](https://cursor.com/en-US/install-mcp?name=desktop-commander&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsIkB3b25kZXJ3aHktZXIvZGVza3RvcC1jb21tYW5kZXJAbGF0ZXN0Il19) |
| **Windsurf**     | `~/.codeium/windsurf/mcp_config.json`                                                       | Manual JSON                                                                                                                                                                      |
| **VS Code**      | `.vscode/mcp.json` or User Settings                                                         | Manual JSON                                                                                                                                                                      |
| **Cline**        | Extension settings → MCP Servers                                                            | Manual JSON                                                                                                                                                                      |
| **Roo Code**     | MCP config file                                                                             | Manual JSON                                                                                                                                                                      |
| **Claude Code**  | `claude mcp add desktop-commander -s user -- npx -y @wonderwhy-er/desktop-commander@latest` | CLI                                                                                                                                                                              |
| **Trae**         | "Add manually" in settings                                                                  | Manual JSON                                                                                                                                                                      |
| **Kiro**         | Kiro → MCP Servers → + Add                                                                  | Manual JSON                                                                                                                                                                      |
| **Codex**        | `~/.codex/config.toml` (TOML)                                                               | CLI or manual                                                                                                                                                                    |
| **JetBrains**    | Settings → Tools → AI Assistant → MCP                                                       | Manual JSON                                                                                                                                                                      |
| **Gemini CLI**   | `~/.gemini/settings.json`                                                                   | Manual JSON                                                                                                                                                                      |
| **Augment Code** | Cmd/Ctrl+Shift+P → Add MCP server                                                           | Manual JSON                                                                                                                                                                      |
| **Qwen Code**    | `.qwen/settings.json` or `~/.qwen/settings.json`                                            | Manual JSON                                                                                                                                                                      |

### Remote MCP (No Desktop App)

**Use from ChatGPT, Claude Web, etc.:** [mcp.desktopcommander.app](https://mcp.desktopcommander.app)

## Available Tools

### Configuration

| Tool               | Description                                                                                                                             |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| `get_config`       | Get complete server config (blockedCommands, defaultShell, allowedDirectories, fileReadLineLimit, fileWriteLineLimit, telemetryEnabled) |
| `set_config_value` | Set specific config value by key                                                                                                        |

### Terminal

| Tool                    | Description                                   |
| ----------------------- | --------------------------------------------- |
| `start_process`         | Start programs with smart readiness detection |
| `interact_with_process` | Send commands to running programs             |
| `read_process_output`   | Read output from processes                    |
| `force_terminate`       | Force terminate session                       |
| `list_sessions`         | List active terminal sessions                 |
| `list_processes`        | List running processes with details           |

### Filesystem

| Tool             | Description                     |
| ---------------- | ------------------------------- |
| `read_file`      | Read text files                 |
| `write_file`     | Write files                     |
| `edit_file`      | Surgical edit with diff preview |
| `list_directory` | List directory contents         |
| `search_files`   | Search files by pattern         |
| `get_file_info`  | File metadata                   |

### Text Editing

| Tool               | Description                          |
| ------------------ | ------------------------------------ |
| `replace_in_file`  | Search and replace with diff preview |
| `insert_into_file` | Insert content at specific location  |

### Analytics

| Tool              | Description                   |
| ----------------- | ----------------------------- |
| `get_usage_stats` | Get usage statistics          |
| `submit_feedback` | Submit feedback to developers |

## Hermes Integration

For Hermes Agent (NPX mode):

```yaml
mcp_servers:
  desktop-commander:
    command: "npx"
    args: ["-y", "@wonderwhy-er/desktop-commander@latest"]
    tools:
      include:
        [
          start_process,
          interact_with_process,
          read_process_output,
          list_sessions,
          read_file,
          write_file,
          edit_file,
          list_directory,
          search_files,
          get_config,
        ]
```

For Docker mode:

```yaml
mcp_servers:
  desktop-commander:
    command: "docker"
    args:
      [
        "run",
        "-i",
        "--rm",
        "-v",
        "C:\\Users\\Alexa\\Desktop\\SandBox:/work",
        "mcp/desktop-commander:latest",
      ]
    tools:
      include:
        [start_process, read_file, write_file, list_directory, search_files]
```

Then run:

```bash
hermes mcp test desktop-commander
/reload-mcp
```

## References

- GitHub: <https://github.com/wonderwhy-er/DesktopCommanderMCP>
- PulseMCP: <https://www.pulsemcp.com/servers/wonderwhy-er-desktop-commander>
- mcpmarket.com: <https://mcpmarket.com/tools/skills/desktop-commander-mcp-installer>
- Remote MCP: <https://mcp.desktopcommander.app>
- Docker: mcp/desktop-commander:latest
  servers/wonderwhy-er-desktop-commander>
- mcpmarket.com: <https://mcpmarket.com/tools/skills/desktop-commander-mcp-installer>
- Remote MCP: <https://mcp.desktopcommander.app>
- Docker: mcp/desktop-commander:latest
