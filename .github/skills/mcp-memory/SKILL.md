---
name: mcp-memory
title: MCP Memory — Knowledge Graph Persistence
description: Exposes all memory MCP tools for creating/reading/updating/deleting entities, relations, and observations in a persistent knowledge graph. Includes test cases per tool.
version: 1.0.0
author: OWL
license: MIT
tags:
  - mcp
  - memory
  - knowledge-graph
  - persistence
metadata:
  hermes:
    tags: []
---
# MCP Memory

Provides a persistent knowledge graph via the standard `@modelcontextprotocol/server-memory`. Enables storing, querying, and managing entities (nodes), their observations (attributes), and relations (edges) — cross-session durable storage that survives agent restarts.

## Overview

Automated reasoning and workflow tool for `mcp-memory`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## Prerequisites

- MCP server: `memory` must be enabled (`hermes mcp list` → `✓ enabled`)
- Config: `npx -y @modelcontextprotocol/server-memory`
- Note: Uses stdio transport (not docker)

## Tools

| Tool | Description |
|------|-------------|
| `create_entities` | Create one or more entities (nodes) in the knowledge graph |
| `create_relations` | Create relations (edges) between existing entities |
| `add_observations` | Add properties/observations to existing entities |
| `search_nodes` | Search entities by query string |
| `open_nodes` | Retrieve full details of entities by name |
| `delete_entities` | Remove entities by name |
| `delete_observations` | Remove observations by matching content |
| `delete_relations` | Remove relations by matching attributes |
| `read_graph` | Dump the entire knowledge graph |

## Workflow

### Phase 1: Verify

```
hermes mcp test memory
```

### Phase 2: Write Operations

```
# Create entities
create_entities(entities: [
  {name: "ProjectX", entityType: "project", observations: ["Started 2026", "Tech stack: Python"]},
  {name: "Alice", entityType: "person", observations: ["Role: developer"]}
])

# Link them
create_relations(relations: [
  {from: "Alice", to: "ProjectX", relationType: "works_on"}
])

# Add more data
add_observations(observations: [
  {entityName: "ProjectX", contents: ["Uses FastAPI", "Deployed on Render"]}
])
```

### Phase 3: Read Operations

```
# Search
search_nodes(query: "Project")  # returns matching entities

# Open specific
open_nodes(names: ["ProjectX"])  # full details

# Dump all
read_graph()
```

### Phase 4: Delete (⚠️)

```
delete_observations(deletions: [{entityName: "ProjectX", observations: ["Deployed on Render"]}])
delete_entities(entityNames: ["ProjectX"])
delete_relations(relations: [{from: "Alice", to: "ProjectX", relationType: "works_on"}])
```

### Phase 5: Test Cases

```bash
# 1. Connectivity
hermes mcp test memory

# 2. Create test entity
# Call: mcp_memory_create_entities(entities: [{name: "TestSkill", entityType: "skill", observations: ["Test entity for verification"]}])

# 3. Search
# Call: mcp_memory_search_nodes(query: "TestSkill")

# 4. Open
# Call: mcp_memory_open_nodes(names: ["TestSkill"])

# 5. Add observation
# Call: mcp_memory_add_observations(observations: [{entityName: "TestSkill", contents: ["Verified on 2026-06-29"]}])

# 6. Delete test entity
# Call: mcp_memory_delete_entities(entityNames: ["TestSkill"])
```

## Best Practices

1. **Entity names should be unique** — opening by name returns all matching entities; duplicates cause ambiguity
2. **Use `entityType` for categorization** — makes `search_nodes` queries more precise
3. **Batch creates** — `create_entities` accepts multiple entities in one call
4. **Verify with `open_nodes` after writing** — confirms data was stored correctly
5. **This is durable storage** — survives agent restarts. Use for project context, user preferences, learning artifacts
6. **Relations can be queried but not searched directly** — use `open_nodes` to see a node's relations
7. **This is separate from Honcho** — MCP memory is a knowledge graph; Honcho is dialectic user modeling

## Pitfalls

- Entity names are **case-sensitive** — `search_nodes("project")` won't find `"ProjectX"`
- `read_graph` on a large graph may produce substantial output — use `search_nodes` first for targeted queries
- `delete_entities` removes all observations and relations attached to the entity
- `delete_observations` matches observation content exactly — partial strings won't match
- No auto-persistence of relations when entities are deleted — orphan relations may remain
- This is NOT the same as the native `memory` tool — MCP memory is a separate knowledge graph store

## Verification Checklist

- [ ] `hermes mcp test memory` passes
- [ ] `create_entities` creates an entity successfully
- [ ] `search_nodes` finds the created entity
- [ ] `add_observations` appends data to an entity
- [ ] `delete_entities` removes a test entity

## When to Use


- When you need to perform MCP Memory — Knowledge Graph Persistence operations or tasks
- When managing MCP Memory — Knowledge Graph Persistence infrastructure or configurations
- When automating or debugging MCP Memory — Knowledge Graph Persistence workflows
- **Triggers**: "mcp memory — knowledge graph persistence" required for a project
