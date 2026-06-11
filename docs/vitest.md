# Vitest MCP Server

**Source:** https://github.com/djankies/vitest-mcp

> Note: The original URL `https://github.com/djankies/vitrst-mcp` returned a 404. The correct repository is `https://github.com/djankies/vitest-mcp`.

## Overview

**Vitest MCP Server** is an AI-optimized Vitest runner that provides clean, structured test output, log capturing, and line-by-line coverage analysis. It's designed to solve the problem of LLMs struggling with raw test output by providing structured, machine-readable results.

**Repository**: [djankies/vitest-mcp](https://github.com/djankies/vitest-mcp)
**License**: MIT
**Status**: Active (94 commits, 12 releases)

---

## Key Features

- **LLM-optimized test output** - Structured results instead of raw console output
- **Log capturing** - Includes `[stdout]` and `[stderr]` prefixed console output
- **Line-by-line coverage analysis** - Detailed coverage gap insights
- **Multi-IDE support** - Works with Claude Code, Cursor, VS Code, Windsurf, and Cline
- **Multi-repository support** - Handle multiple projects
- **Claude Code hook** - Automatically redirects Vitest commands to MCP tools

---

## Quick Start

### Basic Configuration

The Vitest MCP server works with any MCP-compatible IDE and supports all JavaScript/TypeScript Vitest projects.

### Client-Specific Setup

#### Claude Code

**Method 1: CLI Wizard (Interactive)**
```bash
claude mcp add vitest npx -y @djankies/vitest-mcp
```

**Method 2: Direct Configuration File**
Create or edit `.mcp.json` in your project root.

**Configuration Scopes**: Project-level (`.mcp.json`) or global

#### Claude Desktop

**Configuration Location**:
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

#### VS Code

**Configuration Methods**:
- `.vscode/mcp.json`
- `MCP: Open User Configuration`

**Setup**: `Cmd/Ctrl + Shift + P` → `MCP: Add Server`

#### Cursor

**Configuration Location**:
- `.cursor/mcp.json`
- `~/.cursor/mcp.json`

#### Windsurf

Similar to Cursor, but uses `serverUrl` instead of `url` for remote servers.

#### Cline

Configuration via Cline UI.

---

## Usage

Once configured, interact with tests using natural language:

```
vitest-mcp: [your test request]
```

Prepending with `vitest-mcp:` ensures the tools are used.

---

## Requirements

- **Vitest**: `npm install --save-dev vitest@latest`
- **Coverage Provider**: `npm install --save-dev @vitest/coverage-v8@latest`

---

## Available Tools

### `set_project_root`
**Required first** - Sets the project root for all operations.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `path` | string | Yes | Project root path |

---

### `list_tests`
Lists test files in your project to prevent LLMs from using command line tools.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `directory` | string | Yes | Directory to search for test files |

---

### `run_tests`
Executes tests with structured output.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `target` | string | Yes | File or directory to test |
| `format` | string | No | Output format: "summary" or "detailed" (auto-detects based on results) |
| `showLogs` | boolean | No | Include console output with `[stdout]` or `[stderr]` prefixes |
| `project` | string | No | Vitest project name for monorepos |

---

### `analyze_coverage`
Analyzes test coverage with gap insights.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `target` | string | Yes | File or directory to analyze coverage for |
| `format` | string | No | Output format: "summary" (overview only) or "detailed" (includes line-by-line coverage) |
| `exclude` | string[] | No | Patterns to exclude from coverage (e.g., `["**/*.stories.*"]`) |

**Note**: Coverage thresholds should be configured in `vitest.config.ts`, not via MCP parameters. Automatically excludes test utilities, mocks, stories, and e2e files.

---

## Claude Code Hook

Automatically redirects Vitest commands to MCP tools. Add to `.claude/settings.local.json`.

**Bypass the hook**:
```bash
BYPASS_VITEST_HOOK=1
# Or for entire session:
export BYPASS_VITEST_HOOK=1
```

---

## Configuration

### Vitest Configuration Priority

The MCP server detects configuration files in this order:
1. `vitest.mcp.config.ts`
2. `vitest.config.ts`
3. `vitest.config.js`
4. `vitest.config.mjs`
5. `vite.config.ts`
6. `vite.config.js`
7. `vite.config.mjs`

This allows a dedicated MCP-specific configuration that won't interfere with regular development.

### Coverage Thresholds

Configure in your Vitest configuration file to enable threshold reporting in `analyze_coverage`.

### Vitest-MCP Configuration File

Optional `.vitest-mcp.json` in home or project directory.

### Priority Order

Configuration is merged with highest priority first (project-level overrides global).
