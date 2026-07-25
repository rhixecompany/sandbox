# Hermes Memory Architecture Patterns

## Three-Layer Memory

| Layer | File | Limit | Purpose |
|-------|------|-------|---------|
| 1 - Identity | SOUL.md | 2200 | Agent personality, core rules, profile routing |
| 2 - Agent Notes | MEMORY.md | 2200 | Env facts, conventions, lessons, completed work |
| 3 - User Profile | USER.md | 1375 | User prefs, workflow, style, timezone |

## File Locations

```
~/.hermes/
├── SOUL.md                    # Root (shared)
├── config.yaml
└── profiles/
    └── <profile>/
        └── memories/
            ├── USER.md
            └── MEMORY.md
```

## Char Limit Enforcement

```python
# When write would exceed limit:
# 1. Consolidate/remove stale entries in same batch
# 2. Retry with consolidated + new entry
```

## Auto-Write Triggers

- User states preference/correction
- Stable env fact discovered
- Explicit "save this" request
- Session end (if reflection enabled)

## What to Save

✅ User preferences, env facts, corrections, conventions, completed work
❌ Task progress, TODOs, PR numbers, commit SHAs, stale facts (>1 week)

## Cross-Session Recall

```python
session_search(query="auth refactor")
# Returns: session_id, snippet, bookend_start, messages±5, bookend_end
```

## MCP Knowledge Graph (Honcho)

```python
# Structured facts
create_entities([{"name": "Alexa", "type": "User", "observations": [...]}])
create_relations([{"from": "Alexa", "to": "VS Code", "type": "USES"}])
add_observations([{"entity": "Alexa", "observations": ["Windows 11"]}])
```