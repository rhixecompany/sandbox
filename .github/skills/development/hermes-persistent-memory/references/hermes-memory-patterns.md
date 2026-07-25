# Hermes Persistent Memory Patterns

## File Locations

- `~/AppData/Local/hermes/memories/USER.md` — User profile (1,375 chars)
- `~/AppData/Local/hermes/memories/MEMORY.md` — Agent notes (2,200 chars)
- `~/AppData/Local/hermes/SOUL.md` — Identity (2,200 chars, root)

## Writing Memory

```python
# Native tool - batch operations
memory(target="memory", operations=[
    {"action": "add", "content": "User uses VS Code on Windows 11"},
    {"action": "replace", "old_text": "old fact", "content": "updated fact"}
])

# MCP Knowledge Graph - structured
create_entities([{"name": "Project", "type": "Project", "observations": [...]}])
create_relations([{"from": "User", "to": "Project", "type": "OWNS"}])
add_observations([{"entity": "Project", "observations": ["Uses Python 3.11"]}])
```

## Char Limit Management

When write would exceed limit:
1. Consolidate/remove entries in same batch
2. Retry with consolidated + new entry

## Auto-Write Triggers

- User states preference → write to USER.md
- Learn stable env fact → write to MEMORY.md
- Explicit "save this" → write to appropriate file
- Session end (if reflection enabled) → both files

## Reflection System

Daily cron job runs reflection:
```yaml
# In config.yaml
cron:
  - schedule: "0 2 * * *"
    prompt: "Reflect on today's session. Update MEMORY.md with lessons learned."
    skills: ["hermes-persistent-memory"]
```

## Profile Structure

```
~/.hermes/
├── SOUL.md              # Root identity (shared)
├── config.yaml          # Profile config
├── profiles/
│   ├── default/
│   │   ├── memories/
│   │   │   ├── USER.md
│   │   │   └── MEMORY.md
│   │   ├── skills/
│   │   ├── plugins/
│   │   └── cron/
│   └── code-architect/
│       ├── memories/
│       └── skills/
```

## Honcho Hybrid Mode

- Auto-injects context + tools available
- `honcho_profile()` — quick facts
- `honcho_search(query)` — raw excerpts
- `honcho_context()` — full session snapshot
- `honcho_reasoning(query, level)` — synthesized answer
- `honcho_conclude(conclusion)` — persist fact