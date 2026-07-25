# Hermes Deep Dive Patterns

## Memory System

```python
# SOUL.md loads as identity (slot #1)
# MEMORY.md/USER.md appear in context header
# Char limits: MEMORY.md < 2200 chars, USER.md < 1375 chars
```

## Agent Loop

```python
# 1. Receive user input
# 2. Load relevant skills (trigger-based)
# 3. Execute tool calls (batched for parallel)
# 4. Synthesize results
# 5. Respond
# 6. Auto-commit session (if session-auto-commit hook enabled)
```

## Profile Isolation

```yaml
# Each profile has its own:
# - skills/
# - plugins/
# - cron/
# - memories/
# Default profile at root config.yaml, NOT profiles/default/
```

## Skill Invocation

```yaml
# Auto-invoked on trigger conditions
# Can also be loaded manually via skill_view()
# Skill frontmatter defines: name, title, description, version, author, license, tags
```

## Learning Loop

```python
# Skills + Memory = Learning Loop
# 1. Execute skill
# 2. Result stored in MEMORY.md
# 3. Next session: MEMORY.md injected
# 4. Skill improves via patch/feedback
```