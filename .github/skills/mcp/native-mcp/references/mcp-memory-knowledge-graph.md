# MCP Memory Server — Knowledge Graph Pattern

> `@modelcontextprotocol/server-memory` — Persistent memory via knowledge graph.

## Overview

The MCP memory server uses a **knowledge graph** model, fundamentally different from the flat key-value approach of Hermes' native `memory` tool. Data is stored as **entities** with typed **observations**, connected by **relations**.

## Key Differences from Native `memory` Tool

| Aspect | Native `memory` Tool | MCP Memory Server |
|--------|---------------------|-------------------|
| Model | Flat key-value entries per target | Knowledge graph: entities + observations + relations |
| Writes | Staged for approval (if write_approval on) | Immediate — no staging |
| Update granularity | Replace/remove whole entries | Add/delete individual observations |
| Query | Full-text FTS5 search | Graph traversal + search_nodes |
| Char limit | 2200 (memory) / 1375 (user) | No per-entity limit (graph-based) |
| Tool access | `memory` native tool | create_entities, add_observations, open_nodes, etc. |

## Entity Model

- **Entities**: Named nodes with a type and observations array
- **Observations**: Typed facts as plain strings per entity
- **Relations**: Directed edges with a type linking entities

```
Entity: "Alexa" (type: "User")
  Observations: ["Name: Alexa", "OS: Windows 11", "Active Profile: default"]

Relations: Alexa --[prefers]→ Communication-Preferences
```

## Tool Reference

| Tool | Purpose |
|------|---------|
| `create_entities` | Create entities with name, type, and observations array |
| `add_observations` | Add observations to existing entities |
| `delete_observations` | Remove specific observations |
| `delete_entities` | Remove entities and their relations |
| `create_relations` | Link entities with typed relations |
| `delete_relations` | Remove relations |
| `read_graph` | Dump entire knowledge graph |
| `search_nodes` | Search across entity names, types, observations |
| `open_nodes` | Retrieve specific entities by name |

## Usage

### Add Server
```yaml
mcp_servers:
  memory:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-memory"]
```

### Create Entities
```
create_entities(entities=[{
    "name": "Alexa",
    "entityType": "User",
    "observations": ["Name: Alexa", "OS: Windows 11"]
}])
```

### Link with Relations
```
create_relations(relations=[{
    "from": "Alexa",
    "relationType": "uses",
    "to": "Tech-Stack"
}])
```

### Query
```
read_graph()          # Full graph dump
search_nodes(query="Windows")  # Search
open_nodes(names=["Alexa"])    # Get specific
```

## When to Use

| Scenario | Tool |
|----------|------|
| Simple key-value facts | Native `memory` tool |
| Structured data with relationships | MCP Memory Server |
| Multi-entity domain modeling | MCP Memory Server |
| Immediate writes (no staging) | MCP Memory Server |
| Char-limited stores | Native (limits); MCP (graph, no limits) |

## Pitfalls

- **Tool prefix**: When accessed via docker-gateway, tools are `mcp_mcp_docker_create_entities` etc.
- **No auto-pruning**: MCP memory server grows unbounded — unlike native tool with char limits.
- **Full graph reads**: `read_graph()` returns everything. Use `search_nodes()` for large graphs.
- **Observation format**: Plain strings. Encode as `key: value` pairs — no schema enforcement.
- **Server must be added to session**: Not auto-connected like native memory tool. Use `mcp_add(name="memory")` via the gateway.
