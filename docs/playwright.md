# Playwright MCP - Comprehensive Summary

## Overview

**Playwright MCP** is a Model Context Protocol (MCP) server developed by Microsoft that provides browser automation capabilities using [Playwright](https://playwright.dev). It enables LLMs to interact with web pages through **structured accessibility snapshots**, bypassing the need for screenshots or visually-tuned models.

---

## Playwright MCP vs Playwright CLI

| Aspect | MCP | CLI + SKILLS |
|--------|-----|--------------|
| **Best for** | Specialized agentic loops with persistent state, rich introspection, iterative reasoning | Coding agents favoring token-efficient workflows |
| **Token efficiency** | Lower – loads large tool schemas and verbose accessibility trees | Higher – uses concise, purpose-built commands |
| **Use cases** | Exploratory automation, self-healing tests, long-running autonomous workflows | High-throughput coding agents balancing browser automation with large codebases |

> **CLI**: Modern coding agents increasingly favor CLI–based workflows exposed as SKILLS over MCP because CLI invocations are more token-efficient.

> **MCP**: Remains relevant for specialized agentic loops that benefit from persistent state, rich introspection, and iterative reasoning over page structure.

---

## Installation

### Standard Config (Works in Most Tools)

```json
{
  "name": "playwright",
  "command": "npx",
  "args": ["@playwright/mcp@latest"]
}
```

### Supported Clients & Setup Methods

#### **VS Code**
- **Button Install**: [VS Code](https://insiders.vscode.dev/redirect?url=vscode%3Amcp%2Finstall) | [VS Code Insiders](https://insiders.vscode.dev/redirect?url=vscode-insiders%3Amcp%2Finstall)
- **Manual**: Add via settings.json or use VS Code CLI

#### **Cursor**
- **Button Install**: [Install in Cursor](https://cursor.com/en/install-mcp?name=Playwright&config=eyJjb...)
- **Manual**: `Cursor Settings` → `MCP` → `Add new MCP Server` → Use `command` type with `npx @playwright/mcp@latest`

#### **Claude Code**
```bash
# Use Claude Code CLI to add the server
```

#### **Cline**
Add to `cline_mcp_settings.json`:
```json
{
  "name": "playwright",
  "command": "npx",
  "args": ["@playwright/mcp@latest"]
}
```

#### **Codex CLI**
Add to `~/.codex/config.toml`:
```toml
[mcp_servers.playwright]
command = "npx"
args = ["@playwright/mcp@latest"]
```

#### **Copilot CLI**
Add to `~/.copilot/mcp-config.json`:
```json
{
  "name": "playwright",
  "command": "npx",
  "args": ["@playwright/mcp@latest"]
}
```

#### **Factory CLI**
- Use `/mcp` within Factory droid for interactive UI

#### **Gemini CLI**
Follow the [MCP install guide](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md#configure-the-mcp-server-in-settingsjson)

#### **Goose**
- **Button Install**: [Install in Goose](https://block.github.io/goose/extension?cmd=npx&arg=%40playwright%2Fmcp%40latest&id=playwright&name=Playwright)
- **Manual**: `Advanced settings` → `Extensions` → `Add custom extension` → Type: `STDIO`, Command: `npx @playwright/mcp`

#### **Junie CLI**
- Use `/mcp` then `Ctrl+A`
- Or add to `.junie/mcp/mcp.json`

#### **Kiro**
- **Button Install**: [Add to Kiro](https://kiro.dev/launch/mcp/add?name=playwright&config=%7B%22command%22...)
- **Manual**: Add to `.kiro/settings/mcp.json`

#### **LM Studio**
- **Button Install**: [Add MCP Server](https://lmstudio.ai/install-mcp?name=playwright&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyJAcGxheXdyaWdodC9tY3BAbGF0ZXN0Il19)
- **Manual**: `Program` → `Install` → `Edit mcp.json`

#### **OpenCode**
Add to `~/.config/opencode/opencode.json`

#### **Qodo Gen**
- Open chat panel → `Connect more tools` → `+ Add new MCP` → Paste standard config

#### **Warp**
- `Settings` → `AI` → `Manage MCP Servers` → `+ Add`
- Or use `/add-mcp` slash command

#### **Windsurf**
Follow [Windsurf MCP documentation](https://docs.windsurf.com/windsurf/cascade/mcp)
