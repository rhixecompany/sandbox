# Hermes Persistent Memory Operations

## Memory Tool Usage

```python
# Add facts (batch mode - atomic)
memory(target="memory", operations=[
    {"action": "add", "content": "User prefers concise responses"},
    {"action": "add", "content": "Workspace: C:\\Users\\Alexa\\Desktop\\SandBox"}
])

# Replace facts
memory(target="user", operations=[
    {"action": "replace", "old_text": "prefers concise", "content": "prefers detailed responses"}
])

# Remove facts
memory(target="memory", operations=[
    {"action": "remove", "old_text": "outdated convention"}
])
```

## Reflection & Auto-Write

- Auto-write: enabled by default, writes on session end
- Manual: `memory` tool with batch operations
- Reflection cron: runs daily if enabled, summarizes session

## Char Limits

| Store | Limit | Purpose |
|-------|-------|---------|
| MEMORY.md | 2,200 chars | Agent notes |
| USER.md | 1,375 chars | User profile |

When limit exceeded → consolidate in same turn.

## Session Search

```python
session_search(query="auth refactor")
# Returns: session_id, snippet, bookend_start, messages±5, bookend_end
```

## MCP Knowledge Graph (Honcho)

```python
# Entities and observations
create_entities([{"name": "project", "entityType": "project", "observations": ["uses python"]}])
create_relations([{"from": "user", "to": "project", "relationType": "works_on"}])
add_observations([{"entityName": "project", "contents": ["new observation"]}])
```

## Best Practices

- Prefer MCP knowledge graph for structured facts
- Use native `memory` tool for compact key-value entries
- Don't save task progress/TODOs (use session_search)
- Save: user prefs, env facts, corrections, conventions, completed work