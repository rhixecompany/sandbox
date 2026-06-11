# Neon MCP Server – Comprehensive Summary

## Overview

**Neon MCP Server** is an open-source tool that enables natural language interaction with Neon Postgres databases via the Model Context Protocol (MCP). It acts as a bridge between LLMs and the [Neon API](https://api-docs.neon.tech/reference/getting-started-with-neon-api), translating natural language into API calls for managing projects, branches, queries, and migrations.

- **License**: MIT
- **Repository**: [neondatabase/mcp-server-neon](https://github.com/neondatabase/mcp-server-neon)
- **Remote endpoint**: `https://mcp.neon.tech/mcp`
- **Deployed on**: Vercel (Next.js App Router)

> **Warning**: Intended for **local development and IDE integrations only**. Not recommended for production. Always review LLM-requested actions before execution.

---

## Key Features

- Manage Neon projects, branches, and databases using natural language
- Run SQL queries and transactions
- Perform safe database migrations (start/commit workflow)
- Optimize slow queries with tuning tools
- Provision Neon Auth and Data API
- Search Neon documentation
- Read-only mode and fine-grained access control via URL params

### Example Natural Language Commands

> "Create a new Postgres database called 'my-database'. Then create a table called users with columns: id, name, email, password."

> "Run a migration on project 'my-project' to add a 'created_at' column to the users table."

> "Summarize all my Neon projects and their data."

---

## Setup Options

### Prerequisites
- Node.js 22+
- `pnpm` via Corepack:
  ```bash
  corepack enable
  ```

### Option 1: Quick Setup with `neonctl init`

Automatically configures Neon MCP Server with OAuth authentication for Cursor, VS Code (GitHub Copilot), and Claude Code:

```bash
neonctl@latest init
```

### Option 2: Remote Hosted MCP (OAuth Authentication)

**Easiest setup** — no local installation or API key required.

#### One-click install buttons:
- [Install in Cursor](https://cursor.com/en-US/install-mcp?name=Neon&config=eyJ1cmwiOiJodHRwczovL21jcC5uZW9uLnRlY2gvbWNwIn0%3D)
- [Add to Kiro](https://kiro.dev/launch/mcp/add?name=Neon&config=%7B%22url%22%3A%20%22https%3A//mcp.neon.tech/mcp%22%7D)

#### Manual configuration:

**Global setup (all agents):**
```bash
neonctl@latest init -g
```

**MCP config file (`mcp.json` or `mcp_config.json`):**
```json
{
  "Neon": {
    "url": "https://mcp.neon.tech/mcp"
  }
}
```

**Kiro config (`~/.kiro/settings/mcp.json` or `.kiro/settings/mcp.json`):**
```json
{
  "Neon": {
    "url": "https://mcp.neon.tech/mcp"
  }
}
```

> **Note**: By default, OAuth operates on personal account projects. To access organization projects, include `org_id` or `project_id` in your prompt.

### Option 3: Remote Hosted MCP (API Key Authentication)

1. [Create a Neon API key](https://console.neon.tech/app/settings?modal=create_api_key)
2. Add to MCP config:

```json
{
  "Neon": {
    "url": "https://mcp.neon.tech/mcp",
    "headers": {
      "Authorization": "Bearer YOUR_API_KEY"
    }
  }
}
```

> Use an **organization API key** to restrict access to org projects only.

---

## Access Control & Scopes

### OAuth Scopes
- `read`: Read-only access
- `write`: Write access
- `*`: Full access (read + write)

### URL Query Parameters

| Param | Description | Example |
|-------|-------------|---------|
| `readonly` | Enable read-only mode (`true`/`false`) | `?readonly=true` |
| `category` | Filter tools by category (repeatable or CSV) | `?category=querying&category=schema` |
| `projectId` | Scope to a single project | `?projectId=proj-123` |

**Examples:**

- Read-only + project-scoped:
  `https://mcp.neon.tech/mcp?readonly=true&projectId=proj-123`
- Category-filtered (querying + schema only):
  `https://mcp.neon.tech/mcp?category=querying&category=schema`

> **Preview available tools**: Visit `/api/list-tools` (no auth required)

### Read-Only Mode

Disables write operations. Available read-only tools include:
- `list_projects`, `list_shared_projects`, `describe_project`
- `list_organizations`, `describe_branch`, `list_branch_computes`
- `compare_database_schema`, `run_sql` (read-only queries only)
- `get_database_tables`, `describe_table_schema`
- `list_slow_queries`, `explain_sql_statement`
- `get_connection_string`, `search`, `fetch`
- `list_docs_resources`, `get_doc_resource`

> **Note**: `run_sql` is available in read-only mode but restricted to SELECT queries.

### Legacy Support

- **SSE Transport (Deprecated)**: Use `https://mcp.neon.tech/sse` if your client doesn't support Streamable HTTP
- **Legacy header**: `x-read-only` (lower priority than `?readonly=true`)

---

## Supported Tools

### Tool Scope Categories
Each tool has a `scope` category for filtering and consent:
- `projects`, `branches`, `schema`, `querying`, `neon_auth`, `data_api`, `docs`, `null`

### Project Management
- `list_projects` (supports `limit`)
- `list_shared_projects`
- `describe_project`
- `create_project`, `delete_project`
- `list_organizations`
