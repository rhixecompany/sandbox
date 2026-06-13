# Vitest MCP Server

**Source:** https://github.com/djankies/vitest-mcp

## Repository Overview

- **Repository:** `djankies/vitest-mcp`
- **Description:** AI-optimized Vitest runner with clean, structured output, log capturing, and coverage analysis
- **License:** MIT
- **Commits:** 94
- **Releases:** 12

## Problem Statement

> **The Problem with LLMs and Testing**
>
> LLMs struggle with traditional test output formats. They produce verbose, unstructured output that's difficult for LLMs to parse and reason about. This MCP server solves that by providing structured, LLM-optimized test results.

## Key Features

| Feature | Description |
|---------|-------------|
| **LLM-Optimized Output** | Clean, structured test results designed for AI consumption |
| **Log Capturing** | Captures `console.log`, `console.error` with `[stdout]`/`[stderr]` prefixes |
| **Line-by-Line Coverage** | Detailed coverage analysis with gap insights |
| **Multi-Repository Support** | Works across monorepos and multiple projects |
| **Claude Code Hook** | Automatically redirects Vitest commands to MCP tools |
| **Multi-IDE Support** | Claude Code, VS Code, Cursor, Windsurf, Cline |

## Quick Start

### Basic Configuration (Any MCP Client)

```json
{
  "mcpServers": {
    "vitest": {
      "command": "npx",
      "args": ["-y", "@djankies/vitest-mcp"]
    }
  }
}
```

> ⚠️ **Note**: The above example may not be valid for all MCP clients. Verify your client's specific setup instructions.

## Client-Specific Setup

### 1. Claude Code

#### Method 1: CLI Wizard (Interactive)
```bash
claude mcp add vitest npx -y @djankies/vitest-mcp
```

#### Method 2: Direct Configuration File (`.mcp.json`)
```json
{
  "mcpServers": {
    "vitest": {
      "command": "npx",
      "args": ["-y", "@djankies/vitest-mcp"]
    }
  }
}
```

**Configuration Scopes:**
- **Project** (`.mcp.json` in project root) - Shared with team
- **User** (`~/.claude/mcp.json`) - Personal across projects
- **Local** (`.mcp.json` with `"scope": "local"`) - Machine-specific

### 2. Claude Desktop

**Config Location:**
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "vitest": {
      "command": "npx",
      "args": ["-y", "@djankies/vitest-mcp"]
    }
  }
}
```

### 3. VS Code

**Config Location:** `.vscode/mcp.json` or via `MCP: Open User Configuration`

```json
{
  "servers": {
    "vitest": {
      "command": "npx",
      "args": ["-y", "@djankies/vitest-mcp"]
    }
  }
}
```

### 4. Cursor

**Config Location:** `.cursor/mcp.json` or `~/.cursor/mcp.json`

```json
{
  "mcpServers": {
    "vitest": {
      "command": "npx",
      "args": ["-y", "@djankies/vitest-mcp"]
    }
  }
}
```

### 5. Windsurf

Similar to Cursor but use `serverUrl` instead of `url` for remote servers.

### 6. Cline

**Config via Cline UI:** `Cmd/Ctrl + ,` → MCP Servers

## Requirements

```bash
npm install --save-dev vitest@latest @vitest/coverage-v8@latest
```

## Available Tools

### 1. `set_project_root` 🚨 **Required First**

Sets the project root for all operations.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `path` | string | Yes | Project root path |

```json
{
  "path": "/path/to/project"
}
```

### 2. `list_tests`

Lists test files in your project. Prevents LLMs from falling back to command line tools.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `directory` | string | Yes | Directory to search for test files |

```json
{
  "directory": "src"
}
```

### 3. `run_tests`

Executes tests with structured output.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `target` | string | Yes | File or directory to test |
| `format` | string | No | `"summary"` or `"detailed"` (auto-detects) |
| `showLogs` | boolean | No | Include console output with `[stdout]`/`[stderr]` prefixes |
| `project` | string | No | Vitest project name for monorepos |

```json
{
  "target": "src/utils.test.ts",
  "format": "detailed",
  "showLogs": true,
  "project": "frontend"
}
```

### 4. `analyze_coverage`

Analyzes test coverage with gap insights.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `target` | string | Yes | File or directory to analyze |
| `format` | string | No | `"summary"` (overview) or `"detailed"` (line-by-line) |
| `exclude` | string[] | No | Patterns to exclude (e.g., `["**/*.stories.*"]`) |

```json
{
  "target": "src",
  "format": "detailed",
  "exclude": ["**/*.stories.*", "**/*.test.ts"]
}
```

> **Note**: Coverage thresholds should be configured in `vitest.config.ts`, not via MCP parameters. Automatically excludes test utilities, mocks, stories, and e2e files.

## Multi-Repository Support

The server supports monorepos and multiple projects through the `project` parameter in tool calls, allowing different Vitest configurations per project within the same workspace.

## Hermes Integration

For Hermes Agent, add to `config.yaml`:

```yaml
mcp_servers:
  vitest:
    command: "npx"
    args: ["-y", "@djankies/vitest-mcp"]
    tools:
      include: [set_project_root, list_tests, run_tests, analyze_coverage]
```

Then run:
```bash
hermes mcp test vitest
/reload-mcp
```

## References

- GitHub: https://github.com/djankies/vitest-mcp
- npm: https://www.npmjs.com/package/@djankies/vitest-mcp
- Vitest Issue: https://github.com/vitest-dev/vitest/issues/8411