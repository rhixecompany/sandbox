# Summary: GitHub - vercel/next-devtools-mcp

## Overview

`next-devtools-mcp` is a **Model Context Protocol (MCP) server** developed by Vercel that provides Next.js development tools and utilities for coding agents like Claude, Cursor, and others. It acts as a bridge between AI coding assistants and Next.js development workflows.

---

## Key Features

### 1. Runtime Diagnostics & Live State Access (Next.js 16+)
- Connects directly to running Next.js dev server's built-in MCP endpoint at `/_next/mcp`
- Query runtime errors, routes, logs, and application state
- Tools: `get_errors`, `get_logs`, `get_page_metadata`, `get_project_metadata`, `get_server_action_by_id`

### 2. Development Automation
- **Upgrade to Next.js 16**: Automated codemod execution
- **Enable Cache Components**: Complete setup and migration for Next.js 16
- **Documentation Search**: Search and retrieve official Next.js docs

### 3. Knowledge Base & Documentation
- Pre-loaded resources on Cache Components (12 sections)
- Next.js 16 migration guides
- Next.js fundamentals

---

## Installation

### Quick Install (Recommended)
```bash
npx -y next-devtools-mcp@latest
```

Add `-y` to skip confirmation, `-g` for global installation.

### Manual Configuration
Add to your MCP client config:
```json
{
  "mcpServers": {
    "next-devtools": {
      "command": "npx",
      "args": ["-y", "next-devtools-mcp@latest"]
    }
  }
}
```

---

## Client-Specific Setup

### Claude Code CLI
```bash
claude mcp add next-devtools -- npx -y next-devtools-mcp@latest
```

### Cursor
- **One-click install**: [Install in Cursor](https://cursor.com/en/install-mcp?name=next-devtools&config=eyJjb21tYW5kIjoibnB4IC15IG5leHQtZGV2dG9vbHMtbWNwQGxhdGVzdCJ9)
- **Manual**: `Cursor Settings` → `MCP` → `New MCP Server`

### Codex CLI
```bash
npx -y next-devtools-mcp@latest
```

**Windows 11 Special Config** (`.codex/config.toml`):
```toml
[env]
# Add environment variables if needed

[mcp_servers.next-devtools]
command = "npx"
args = ["-y", "next-devtools-mcp@latest"]
startup_timeout_sec = 30
```

### Gemini CLI
```bash
gemini mcp add next-devtools -- npx -y next-devtools-mcp@latest
```

Config file: `.gemini/antigravity/mcp_config.json`

### Warp UI
`Settings | AI | Manage MCP Servers` → `+ Add`
- Name: `next-devtools`
- Command: `npx`
- Args: `-y, next-devtools-mcp@latest`

---

## Quick Start

### For Next.js 16+ Projects (Recommended)

1. **Start your dev server** (MCP enabled by default at `http://localhost:3000/_next/mcp`)

2. **Initialize MCP context** (IMPORTANT):
   ```
   Use the init tool to set up Next.js DevTools context
   ```

3. **Example prompts**:
   - `Next Devtools, what errors are in my Next.js application?`
   - `Next Devtools, show me the structure of my routes`
   - `Next Devtools, what's in the development server logs?`

### For All Next.js Projects
- `Next Devtools, help me upgrade my Next.js app to version 16`
- `Next Devtools, enable Cache Components in my Next.js app`
- `Next Devtools, search Next.js docs for generateMetadata`

---

## Pro Tip: Auto-Initialize

Add to your agent's config to automatically call `init` at session start:

**Claude** (`~/.claude/CLAUDE.md` or `./.claude/CLAUDE.md`):
```markdown
When working with Next.js, always call the init tool from next-devtools-mcp
at the start of the session.
```

**Cursor** (`.cursorrules`):
```markdown
When working with Next.js, always call the init tool from next-devtools-mcp
at the start of the session to establish proper context and documentation requirements.
```

**Other agents** (`.codex/instructions.md`, `agent.md`, etc.):
```markdown
When working with Next.js, always call the init tool from next-devtools-mcp
at the start of the session.
```

---

## MCP Tools

### `init`
Initialize Next.js DevTools MCP context and establish documentation requirements.

### `nextjs_docs`
Search and retrieve Next.js official documentation.

**Parameters:**
- `action`: `search` | `get`
- `query`: Search term (for `search`)
- `path`: Doc path (for `get`)
- `anchor`: Section anchor (for `get`)
- `routerType`: `app` | `pages` | `all`

### `nextjs_index`
Discover all running Next.js dev servers and list available MCP tools.

**No parameters required** - automatically scans for servers.

### `nextjs_call`
Execute a specific MCP tool on a running Next.js dev server.

**Parameters:**
- `port`: Server port (from `nextjs_index`)
- `toolName`: Tool to execute
- `args`: Tool-specific arguments

### `browser_eval`
Automate and test web applications using Playwright.

**Available actions:**
- `start`, `navigate`, `click`, `type`, `fill_form`
- `evaluate`, `screenshot`, `console_messages`
- `close`, `drag`, `upload_file`, `list_tools`

**Note**: For Next.js projects, prefer `nextjs_index` and `nextjs_call` over `browser_eval`.

### `upgrade_nextjs_16`
Guides through upgrading Next.js to version 16 with automated codemod execution.

### `enable_cache_components`
Complete Cache Components setup and migration for Next.js 16.
