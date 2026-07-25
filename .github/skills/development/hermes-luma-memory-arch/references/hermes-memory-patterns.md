# Hermes Memory Architecture Patterns

## Three-Layer Memory System

| Layer | File | Purpose | Char Limit | Load Priority |
|-------|------|---------|------------|---------------|
| Identity | SOUL.md | Agent personality, rules | 2,200 | Slot #1 (always) |
| Agent Notes | MEMORY.md | Env facts, conventions, lessons | 2,200 | Context header |
| User Profile | USER.md | User prefs, workflow, style | 1,375 | Context header |

## Memory Operations

```python
# Native memory tool (compact KV entries)
memory(target="memory", operations=[
    {"action": "add", "content": "User prefers concise responses"},
    {"action": "replace", "old_text": "old fact", "content": "new fact"}
])

# MCP Knowledge Graph (structured facts)
create_entities([{"name": "Alexa", "type": "User", "observations": [...]}])
add_observations([{"entity": "Alexa", "observations": ["Uses VS Code"]}])
```

## Profile Isolation

- Each profile has own `memories/`, `skills/`, `plugins/`, `cron/`
- SOUL.md at `~/AppData/Local/hermes/SOUL.md` (root, not per-profile)
- Cross-profile reads blocked by default (use `cross_profile=true`)

## Char Limit Enforcement

```python
# When write would exceed limit:
# 1. Consolidate/remove entries in same turn
# 2. Retry with consolidated + new entry
```

## Auto-Write Triggers

- User states preference/correction
- Stable env fact discovered
- Explicit "save this" request
- Session end reflection (if enabled)

## What NOT to Save

- Task progress, TODO state → use `session_search`
- PR/issue numbers, commit SHAs
- "Fixed bug X", "Phase N done"
- Stale facts (>1 week)