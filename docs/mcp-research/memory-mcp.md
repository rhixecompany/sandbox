# Knowledge Graph Memory MCP Server

**Source:** https://github.com/modelcontextprotocol/servers/tree/main/src/memory

## Overview

A **basic implementation of persistent memory using a local knowledge graph** that enables AI assistants to remember information about users across chat sessions.

## Core Concepts

### Entities

Primary nodes in the knowledge graph. Each entity has:
- **name** (string) — unique identifier
- **entityType** (string) — classification/category
- **observations** (string[]) — discrete facts about the entity

### Relations

Directed connections between entities, always stored in **active voice** describing how entities interact or relate.

### Observations

Discrete pieces of information about an entity that are:
- Atomic/fact-based
- Stored as strings
- Attached to specific entities

## API Tools

| Tool | Parameters | Description |
|------|------------|-------------|
| **create_entities** | `entities: { name, entityType, observations[] }[]` | Create new entities |
| **create_relations** | `relations: { from, to, relationType }[]` | Create directed relations |
| **add_observations** | `observations: { entityName, contents[] }[]` | Add observations to existing entities |
| **delete_entities** | `entityNames: string[]` | Remove entities |
| **delete_observations** | `deletions: { entityName, observations[] }[]` | Remove specific observations |
| **delete_relations** | `relations: { from, to, relationType }[]` | Remove relations |
| **read_graph** | *(none)* | Read entire knowledge graph |
| **search_nodes** | `query: string` | Search entities by query |
| **open_nodes** | `names: string[]` | Open specific nodes by name |

## Installation & Configuration

### Claude Desktop

Add to `claude_desktop_config.json`:

#### Docker

```json
{
  "mcpServers": {
    "memory": {
      "command": "docker",
      "args": ["run", "-i", "-v", "claude-memory:/app/dist", "--rm", "mcp/memory"]
    }
  }
}
```

#### NPX

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

> **Windows:** Use `cmd /c npx` instead of `npx`

#### NPX with Custom Memory File Path

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "env": {
        "MEMORY_FILE_PATH": "memory.jsonl"
      }
    }
  }
}
```

> **Windows:** Use `cmd /c` prefix

### VS Code Installation

#### One-Click Install Buttons

| Method | VS Code | VS Code Insiders |
|--------|---------|------------------|
| **NPX** | [Install](https://insiders.vscode.dev/redirect/mcp/install?name=memory&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40modelcontextprotocol%2Fserver-memory%22%5D%7D) | [Install](https://insiders.vscode.dev/redirect/mcp/install?name=memory&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40modelcontextprotocol%2Fserver-memory%22%5D%7D&quality=insiders) |
| **Docker** | [Install](https://insiders.vscode.dev/redirect/mcp/install?name=memory&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22-v%22%22claude-memory%3A%2Fapp%2Fdist%22%2C%22--rm%22%2C%22mcp%2Fmemory%22%5D%7D) | [Install](https://insiders.vscode.dev/redirect/mcp/install?name=memory&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22-v%22%22claude-memory%3A%2Fapp%2Fdist%22%2C%22--rm%22%2C%22mcp%2Fmemory%22%5D%7D&quality=insiders) |

#### Manual Configuration

**Method 1: User Configuration (Recommended)**
1. Open Command Palette: `Ctrl + Shift + P`
2. Run: `MCP: Open User Configuration`
3. Add server config to `mcp.json`

**Method 2: Workspace Configuration**
Create `.vscode/mcp.json` in workspace root for sharing.

## System Prompt Example

For chat personalization (use in [Claude.ai Projects](https://www.anthropic.com/news/projects) Custom Instructions):

```
Follow these steps for each interaction:
1. User Identification:
   - You should assume that you are interacting with default_user
   - If you have not identified default_user, proactively try to do so.
2. Memory Retrieval:
   - Always begin your chat by saying only "Remembering..." and retrieve all relevant information from your knowledge graph
   - Always refer to your knowledge graph as your "memory"
3. Memory
   - While conversing with the user, be attentive to any new information that falls into these categories:
     a) Basic Identity (age, gender, location, job title, education level, etc.)
     b) Behaviors (interests, habits, etc.)
     c) Preferences (communication style, preferred language, etc.)
     d) Goals (goals, targets, aspirations, etc.)
     e) Relationships (personal and professional relationships up to 3 degrees of separation)
4. Memory Update:
   - If any new information was gathered during the interaction, update your memory as follows:
     a) Create entities for new people, places, concepts
     b) Add observations to existing entities
     c) Create relations between entities
```

## Hermes Integration

For Hermes Agent (NPX mode):

```yaml
mcp_servers:
  memory:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-memory"]
    env:
      MEMORY_FILE_PATH: "~/.hermes/memory.jsonl"
    tools:
      include: [create_entities, create_relations, add_observations, read_graph, search_nodes, open_nodes]
```

For Docker mode (persistent volume):

```yaml
mcp_servers:
  memory:
    command: "docker"
    args: ["run", "-i", "-v", "hermes-memory:/app/dist", "--rm", "mcp/memory"]
    tools:
      include: [create_entities, create_relations, add_observations, read_graph, search_nodes, open_nodes]
```

For Windows NPX:

```yaml
mcp_servers:
  memory:
    command: "cmd"
    args: ["/c", "npx", "-y", "@modelcontextprotocol/server-memory"]
    env:
      MEMORY_FILE_PATH: "%USERPROFILE%\\.hermes\\memory.jsonl"
    tools:
      include: [create_entities, create_relations, add_observations, read_graph, search_nodes, open_nodes]
```

Then run:
```bash
hermes mcp test memory
/reload-mcp
```

## Alternative: Local Memory MCP (npm package)

There's also a standalone npm package: `local-memory-mcp` (https://lobehub.com/mcp/danieleugenewilliams-local-memory-mcp)

```bash
npx local-memory-mcp --db-path ~/.opencode-memory.db
```

Or for a specific session:
```bash
npx local-memory-mcp --db-path ./.memory/opencode.db --session-id opencode-session
```

## Remote Memory MCP Generator

For shared memory across clients: https://memory.mcpgenerator.com

Works with Cursor, Claude, Copilot, and other MCP clients over HTTP/SSE.

## References

- GitHub: https://github.com/modelcontextprotocol/servers/tree/main/src/memory
- mcpservers.org: https://mcpservers.org/servers/modelcontextprotocol/memory
- Remote Memory Generator: https://memory.mcpgenerator.com
- LobeHub (local-memory-mcp): https://lobehub.com/mcp/danieleugenewilliams-local-memory-mcp