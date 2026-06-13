# SQLite MCP Server (Go Implementation)

**Source:** https://github.com/liliang-cn/mcp-sqlite-server

## Overview

A **Model Context Protocol (MCP) server for SQLite database operations**, built with Go. This server allows AI assistants to interact with SQLite databases through a secure, directory-restricted interface.

## Features

- Full SQLite database interaction capabilities
- Directory-restricted access for security
- Go-based implementation for performance
- 19 total tools covering queries, table management, indexes, databases, and optimization

## Available Tools (19 Total)

### Query & Data Manipulation

| Tool | Description |
|------|-------------|
| `query` | Execute a SELECT query |
| `execute` | Execute non-SELECT statements (INSERT, UPDATE, DELETE, DDL) |
| `transaction` | Execute multiple statements in a transaction |

### Table Management

| Tool | Description |
|------|-------------|
| `create_table` | Create a new table |
| `list_tables` | List all tables in the database |
| `describe_table` | Get detailed schema information for a table |
| `drop_table` | Drop a table |

### Index Management

| Tool | Description |
|------|-------------|
| `create_index` | Create an index |
| `list_indexes` | List all indexes |
| `drop_index` | Drop an index |

### Database Management

| Tool | Description |
|------|-------------|
| `create_database` | Create a new database file |
| `database_exists` | Check if a database exists |
| `switch_database` | Switch current database context |
| `current_database` | Get current database name |
| `list_database_files` | List all database files in allowed directory |
| `delete_database` | Delete a database file |

### Database Analysis & Optimization

| Tool | Description |
|------|-------------|
| `vacuum` | Run VACUUM to reclaim space |
| `analyze_query` | Analyze query execution plan |
| `database_stats` | Get database statistics |

## Installation

### Prerequisites

- Go 1.21+

### Install via go install (Recommended)

```bash
go install github.com/liliang-cn/mcp-sqlite-server@latest
```

> **Note:** Ensure `$HOME/go/bin` (or `$GOPATH/bin`) is in your PATH:
> ```bash
> export PATH="$HOME/go/bin:$PATH"
> # Add to ~/.zshrc or ~/.bashrc for persistence
> ```

### Build from Source

```bash
git clone https://github.com/liliang-cn/mcp-sqlite-server.git
cd mcp-sqlite-server
./build.sh
# Or: go build -o mcp-sqlite-server
```

## Usage

### Basic Usage

**Required:** You must specify at least one database path or directory as an argument.

```bash
# Using a specific database file
mcp-sqlite-server /path/to/database.db

# Using a directory (allows access to all .db files in directory)
mcp-sqlite-server /path/to/db/directory
```

**Note:** The server will exit with an error if:
- No database path/directory is provided
- The specified path doesn't exist or isn't accessible

### With Claude Desktop

Add to your Claude Desktop MCP configuration:

**Config locations:**
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "mcp-sqlite-server",
      "args": ["/absolute/path/to/your/database.db"]
    }
  }
}
```

**Important:** Make sure to use the full absolute path to the binary (e.g., `$HOME/go/bin/mcp-sqlite-server`) or ensure the binary is in your system PATH.

## Security

- **Directory restriction:** Server only allows access to databases within the specified directory
- **Read-only mode available:** Can be configured to only allow SELECT queries
- **Path validation:** All database paths are validated against allowed directories

## Repository Structure

```
mcp-sqlite-server/
├── database/             # Database operations
├── logger/               # Logging utilities
├── server/               # MCP server implementation
├── .gitignore
├── README.md
├── build.sh              # Build script
├── go.mod                # Go module definition
├── go.sum                # Go dependencies
└── main.go               # Entry point
```

## Alternative Implementations

### 1. @berthojoris/mcp-sqlite-server (TypeScript/Node.js)

**npm:** https://www.npmjs.com/package/@berthojoris/mcp-sqlite-server

```bash
npx @berthojoris/mcp-sqlite-server sqlite:///path/to/database.sqlite list,read,create,update,delete
```

**Configuration:**
```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": ["-y", "@berthojoris/mcp-sqlite-server", "sqlite:///path/to/db.sqlite", "list,read,create,update,delete"]
    }
  }
}
```

**Permission levels:**
- `list` - List tables and schemas
- `read` - Read data
- `create` - INSERT
- `update` - UPDATE
- `delete` - DELETE
- `ddl` - DDL operations (CREATE TABLE, etc.)
- `transaction` - Transactions
- `utility` - Utility commands

### 2. mcp-sqlite (Augment Code)

https://www.augmentcode.com/mcp/mcp-sqlite - Another Node.js implementation with 8 tools

### 3. VS Code Extension

**Marketplace:** https://marketplace.visualstudio.com/items?itemName=Mrbeandev.mcp-sqlite-tool

Python-based with VS Code integration for managing SQLite via MCP.

## Hermes Integration

For Hermes Agent (Go binary):

```yaml
mcp_servers:
  sqlite:
    command: "mcp-sqlite-server"
    args: ["C:/Users/Alexa/Desktop/SandBox/data/app.db"]
    tools:
      include: [query, execute, transaction, create_table, list_tables, describe_table, create_index, create_database, vacuum, analyze_query]
```

For NPX mode (berthojoris version):

```yaml
mcp_servers:
  sqlite:
    command: "npx"
    args: ["-y", "@berthojoris/mcp-sqlite-server", "sqlite:///C:/Users/Alexa/Desktop/SandBox/data/app.db", "list,read,create,update,delete,ddl,transaction,utility"]
    tools:
      include: [list, read, create, update, delete, ddl, transaction, utility]
```

Then run:
```bash
hermes mcp test sqlite
/reload-mcp
```

## References

- GitHub (Go): https://github.com/liliang-cn/mcp-sqlite-server
- npm (TypeScript): https://www.npmjs.com/package/@berthojoris/mcp-sqlite-server
- Augment Code: https://www.augmentcode.com/mcp/mcp-sqlite
- VS Code Extension: https://marketplace.visualstudio.com/items?itemName=Mrbeandev.mcp-sqlite-tool