# Desktop Commander MCP

**Source:** https://github.com/wonderwhy-er/DesktopCommanderMCP

## Overview

**Desktop Commander MCP** is an open-source Model Context Protocol (MCP) server that enables AI assistants like Claude Desktop to control terminals, manage files, and automate tasks on your computer. It transforms Claude into a powerful development assistant capable of executing long-running commands, editing files, and managing processes.

**Key Benefits:**
- Works with Claude Pro subscription ($20/month) — no API token costs
- Full filesystem and terminal access
- Cross-platform support (macOS, Windows, Linux)
- Docker support for isolated environments

---

## Installation Methods

### Option 1: npx Setup (Recommended)
```bash
npx @wonderwhy-er/desktop-commander@latest setup
```
- ✅ Auto-updates on Claude restart
- Uninstall: `npx @wonderwhy-er/desktop-commander@latest remove`

### Option 2: Bash Installer
```bash
curl -fsSL https://raw.githubusercontent.com/wonderwhy-er/DesktopCommanderMCP/refs/heads/main/install.sh | bash
```
- ✅ Auto-updates on Claude restart
- Uninstall: `npx @wonderwhy-er/desktop-commander@latest remove`

### Option 3: Smithery
- Install via Smithery platform
- ✅ Auto-updates on Claude restart

### Option 4: Manual Configuration
Add to `claude_desktop_config.json`:
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- Linux: `~/.config/Claude/claude_desktop_config.json`

- ✅ Auto-updates on Claude restart

### Option 5: Git Clone (Manual Updates Required)
```bash
cd DesktopCommanderMCP && git pull && npm run setup
```
- ❌ No auto-updates
- Manual update required

### Option 6: Docker Installation
**Prerequisites:** Docker Desktop installed and running

**macOS/Linux:**
```bash
# Basic setup (no file access)
docker run -it --rm mcp/desktop-commander:latest

# With folder mounting
docker run -it --rm -v /path/to/folder:/workspace mcp/desktop-commander:latest
```

**Windows PowerShell:**
```powershell
docker run -it --rm -v C:\path\to\folder:/workspace mcp/desktop-commander:latest
```

- ✅ Auto-updates via `latest` tag
- Update: `docker pull mcp/desktop-commander:latest`

---

## Supported Clients

Desktop Commander works with any MCP-compatible client:

| Client | Configuration Location |
|--------|----------------------|
| **Cursor** | `~/.cursor/mcp.json` or `.cursor/mcp.json` |
| **Windsurf** | `~/.codeium/windsurf/mcp_config.json` |
| **VS Code** | `.vscode/mcp.json` or User Settings |
| **Cline** | Extension settings → MCP Servers |
| **Roo Code** | MCP configuration file |
| **Claude Code** | `claude mcp add-json` command |
| **Trae** | "Add manually" feature |
| **Kiro** | Settings → MCP Servers → + Add |
| **Codex** | `~/.codex/config.toml` |
| **JetBrains** | Settings → Tools → AI Assistant → MCP |
| **Gemini CLI** | `~/.gemini/settings.json` |
| **Augment Code** | Augment panel → Add MCP server |
| **Qwen Code** | `.qwen/settings.json` or `~/.qwen/settings.json` |

---

## Available Tools

### Configuration Tools
- **`get_config`** - Get complete server configuration
- **`set_config_value`** - Set configuration values:
  - `blockedCommands`: Array of blocked shell commands
  - `defaultShell`: Shell to use (bash, zsh, powershell)
  - `allowedDirectories`: Filesystem paths accessible for file operations
  - `fileReadLineLimit`: Max lines to read (default: 1000)
  - `fileWriteLineLimit`: Max lines to write (default: 50)
  - `telemetryEnabled`: Enable/disable telemetry

### Terminal Tools
- **`start_process`** - Start programs with smart detection
- **`interact_with_process`** - Send commands to running programs
- **`read_process_output`** - Read output from processes
- **`force_terminate`** - Force terminate terminal sessions
- **`list_sessions`** - List active terminal sessions
- **`list_processes`** - List running processes with details
- **`kill_process`** - Terminate process by PID

### Filesystem Tools
- **`read_file`** - Read files, URLs, Excel, PDFs with pagination
- **`read_multiple_files`** - Read multiple files simultaneously
- **`write_file`** - Write files (supports Excel, append mode)
- **`write_pdf`** - Create/modify PDFs from markdown
- **`create_directory`** - Create directories
- **`list_directory`** - Recursive directory listing (depth parameter)
- **`move_file`** - Move/rename files and directories
- **`start_search`** - Search files by name or content
- **`get_more_search_results`** - Paginated search results
- **`stop_search`** - Stop active searches
- **`list_searches`** - List active search sessions
- **`get_file_info`** - Get file metadata

### Text Editing Tools
- **`edit_block`** - Targeted text replacements with fuzzy search

### Analytics Tools
- **`get_usage_stats`** - Usage statistics
- **`get_recent_tool_calls`** - Recent tool call history
- **`give_feedback_to_desktop_commander`** - Open feedback form
