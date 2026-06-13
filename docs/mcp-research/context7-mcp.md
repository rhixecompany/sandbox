# Context7 MCP Server (c7-mcp-server)

**Source:** https://github.com/quiint/c7-mcp-server

## Overview

A **Model Context Protocol (MCP)** server that bridges MCP-compatible clients (Claude Desktop, IDE plugins, custom apps) to the **Context7 API** (`https://context7.com`).

⚠️ **Important:** This server only provides an MCP interface—it does **not** generate or host content. All data comes directly from the official Context7 API.

**Exposed command:** `c7-mcp-server` (available globally after install)

**License:** MIT | **Author:** Upstash (unofficial)

## Features (MCP Capabilities)

| Capability | Type | Description |
|------------|------|-------------|
| `c7_query` | Tool | Query documentation context for a project |
| `c7_search` | Tool | Search for projects |
| `c7_info` | Tool | Retrieve project metadata |
| `c7_projects_list` | Tool | List available projects |
| `context7://projects/list` | Resource | JSON list of projects |

## Installation

### Prerequisites

- Node.js / Bun environment

### Option 1: npm (Recommended for Users)

```bash
npm install -g c7-mcp-server
```

Makes `c7-mcp-server` available system-wide.

### Option 2: From Source (Development)

```bash
git clone https://github.com/quiint/c7-mcp-server.git
cd c7-mcp-server
npm install        # or: bun install
npm run build
npm link           # or: bun link
```

## Usage

### With MCP Clients (e.g., Claude Desktop)

The server runs via stdio—**clients launch it**, users don't run it directly.

**1. Ensure global install or link:**
```bash
npm install -g c7-mcp-server
# or
npm link
```

**2. Edit client config** (`claude_desktop_config.json`):
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "context7": {
      "command": "c7-mcp-server"
    }
  }
}
```

**3. Restart the client** — it will launch `c7-mcp-server` in background.

### Testing with MCP Inspector

```bash
# Ensure c7-mcp-server is globally available or linked
npx @modelcontextprotocol/inspector c7-mcp-server
```

Opens browser UI with **Tools**, **Resources**, and **Notifications** tabs.

## MCP Capabilities Details

### Tools

#### `c7_query`

Query documentation context for a specific project.

**Parameters:**
```typescript
{
  projectname: string;    // e.g., "nextjs"
  query: string;          // search query
  format?: "txt" | "json"; // default: "txt"
  tokens?: number;        // token limit
}
```

#### `c7_search`

Search for projects by term.

**Parameters:**
```typescript
{
  term: string;           // search term (title/name)
}
```

#### `c7_info`

Get metadata for a specific project.

**Parameters:**
```typescript
{
  projectname: string;
}
```

#### `c7_projects_list`

List all available projects (no parameters).

### Resources

#### `context7://projects/list`

- **MIME Type:** `application/json`
- Returns JSON list of all Context7 projects

## Development Commands

| Command | Description |
|---------|-------------|
| `npm install` / `bun install` | Install dependencies |
| `npm run build` | Compile TypeScript → `build/` |
| `npm run dev` | Run in development mode |
| `npm link` / `bun link` | Link globally for local testing |
| `npx @modelcontextprotocol/inspector c7-mcp-server` | Launch MCP Inspector |

**Source code:** `src/`

## Project Structure

```
c7-mcp-server/
├── build/              # Compiled output
├── src/                # TypeScript source
├── .gitignore
├── README.md
├── bun.lock
├── package.json
└── tsconfig.json
```

## Official Context7 MCP (Upstash)

Upstash also provides an official Context7 MCP server:

**Installation:**
```bash
# Via npm
npx -y @upstash/context7-mcp --api-key YOUR_API_KEY

# Via npm install
npm install -g @upstash/context7-mcp
```

**Configuration:**
```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp", "--api-key", "YOUR_API_KEY"]
    }
  }
}
```

**Or with HTTP transport:**
```bash
claude mcp add --scope user --header "CONTEXT7_API_KEY: YOUR_API_KEY" --transport http context7 https://mcp.context7.com/mcp
```

**Get API Key:** https://context7.com/dashboard (free tier available)

**Tools Provided:**
- `resolve-library-id` — Resolves library name to Context7-compatible ID
- `query-docs` — Retrieves version-specific documentation

**References:**
- Augment Code: https://www.augmentcode.com/mcp/context7
- Open VSX: https://open-vsx.org/extension/Upstash/context7-mcp

## Hermes Integration

For Hermes Agent (using unofficial c7-mcp-server):

```yaml
mcp_servers:
  context7:
    command: "c7-mcp-server"
    tools:
      include: [c7_query, c7_search, c7_info, c7_projects_list]
```

For official Upstash version (with API key):
```yaml
mcp_servers:
  context7:
    command: "npx"
    args: ["-y", "@upstash/context7-mcp", "--api-key", "${CONTEXT7_API_KEY}"]
    env:
      CONTEXT7_API_KEY: "${CONTEXT7_API_KEY}"
    tools:
      include: [resolve-library-id, query-docs]
```

Then run:
```bash
hermes mcp test context7
/reload-mcp
```

## References

- GitHub (Unofficial): https://github.com/quiint/c7-mcp-server
- Official Upstash: https://www.augmentcode.com/mcp/context7
- mcpservers.org (Unofficial): https://mcpservers.org/servers/arben-adm/mcp-sequential-thinking
- Context7 Dashboard: https://context7.com/dashboard