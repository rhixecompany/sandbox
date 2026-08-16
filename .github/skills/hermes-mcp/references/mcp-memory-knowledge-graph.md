# MCP Memory Server — Knowledge Graph Usage

## Overview

The `@modelcontextprotocol/server-memory` MCP server provides a **knowledge graph** for persistent memory, not a simple key-value store. Data is modeled as **entities** with **observations** linked by **relations**.

## Tools

| Tool | Purpose | Key Parameters |
|------|---------|---------------|
| `create_entities` | Create entities with observations | `entities: [{name, entityType, observations}]` |
| `create_relations` | Link entities | `relations: [{from, relationType, to}]` |
| `add_observations` | Add to existing entities | `observations: [{entityName, contents}]` |
| `delete_entities` | Remove entities | `entityNames: [...]` |
| `delete_observations` | Remove specific observations | `deletions: [{entityName, observations}]` |
| `delete_relations` | Remove links | `relations: [{from, relationType, to}]` |
| `read_graph` | Dump entire knowledge graph | (none) |
| `search_nodes` | Search by keyword | `query: "text"` |
| `open_nodes` | Get specific entities | `names: ["Entity1", "Entity2"]` |

## Activation

The memory server must be added to the current MCP session via the Docker gateway:

```
mcp_mcp_docker_mcp_add(name="memory")
```

This exposes the 9 knowledge graph tools.

## Entity Modeling Pattern

Create entities first, then relations:

```python
# Step 1: Entities with observations
mcp_mcp_docker_mcp_exec(arguments={
    "entities": [
        {"entityType": "User", "name": "Alexa", "observations": ["OS: Windows 11"]},
        {"entityType": "Preference", "name": "Communication-Style", "observations": ["Concise, action-first"]}
    ]
}, name="create_entities")

# Step 2: Relations linking them
mcp_mcp_docker_mcp_exec(arguments={
    "relations": [
        {"from": "Alexa", "relationType": "prefers", "to": "Communication-Style"}
    ]
}, name="create_relations")
```

## When to Use vs Native `memory` Tool

| Use Case | Tool | Why |
|----------|------|-----|
| Rich structured knowledge (many facts, categories, links) | MCP knowledge graph | Entities, types, relations — queryable, traversable |
| Compact key-value updates to Hermes memory stores | Native `memory` tool | `operations` batch mode, char-limit enforcement |
| User told you to "create new memories" | MCP knowledge graph | Direct writes, no staging/approval flow |
| Quick preference/identity fact for next session | Native `memory` tool | Automatic injection into every turn |
