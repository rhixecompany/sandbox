# MCP Knowledge Graph Memory (vs Native Memory Tool)

## Overview

This Hermes system has **two parallel memory stores** with different semantics:

| Aspect | Native `memory` tool | MCP Knowledge Graph (`memory` server) |
|--------|---------------------|---------------------------------------|
| **Data model** | Flat key-value entries separated by `§` | Entities + typed observations + relations |
| **Write approval** | `memory.write_approval` is ON — stages via TUI | Direct write, no approval |
| **Approve writes** | User types `/memory approve <id>` or `/memory pending` in TUI | N/A — writes are immediate |
| **API** | `memory(action=...)` native tool | `create_entities`, `create_relations`, `add_observations`, `read_graph`, `search_nodes` (via mcp_docker gateway) |
| **Persistence** | Files at `~/AppData/Local/hermes/memories/{MEMORY.md,USER.md}` | In-memory / plugin-managed (knowledge graph JSON) |
| **Best for** | Compact cross-session facts about user/environment | Structured knowledge with relationships |

## Activating the MCP Memory Server

If not already active:
```
# Via the docker gateway catalog
mcp_mcp_docker_mcp_add(name='memory')
```
This adds 9 tools: `create_entities`, `create_relations`, `add_observations`, `delete_entities`, `delete_observations`, `delete_relations`, `read_graph`, `search_nodes`, `open_nodes`.

## Usage Pattern

```python
# Create entities with observations
mcp_mcp_docker_mcp_exec(
  name='create_entities',
  arguments={
    "entities": [
      {
        "entityType": "Preference",
        "name": "My-Preference",
        "observations": ["Detail 1", "Detail 2"]
      }
    ]
  }
)

# Link entities
mcp_mcp_docker_mcp_exec(
  name='create_relations',
  arguments={
    "relations": [
      {"from": "User", "relationType": "prefers", "to": "My-Preference"}
    ]
  }
)

# Read everything
mcp_mcp_docker_mcp_exec(name='read_graph', arguments={})

# Search
mcp_mcp_docker_mcp_exec(
  name='search_nodes',
  arguments={"query": "preference"}
)
```

## When to Use Which

- **Native `memory` tool** — For compact, durable user profile facts (OS, shell, name, model) and agent notes that must survive across sessions. Use batch `operations` for atomic multi-entry updates.
- **MCP knowledge graph** — For structured, relational knowledge that benefits from graph traversal (e.g., "what preferences does the user have, and which workflows depend on those preferences?"). Also useful when native memory writes are blocked by `write_approval` — the MCP store is an immediate alternative.

## Pitfalls

- The MCP memory server is NOT the same store as Hermes' native memory. Updates to one do not affect the other.
- If the gateway restarts, the in-memory knowledge graph may reset. Check via `read_graph` before relying on persisted entities.
- `create_entities` with a name that already exists creates a duplicate unless handled at the application level.
