---
name: hermes-luma-memory-arch
title: "Hermes Memory Architecture (Luma Dock)"
description: "Use when studying Hermes three-layer memory system — SOUL.md/MEMORY.md/USER.md (Layer 1), skills directory (Layer 2), SQLite session DB with FTS5 (Layer 3) — from Luma Dock tutorial."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [hermes, memory, soul-md, memory-md, user-md, state-db, sqlite, fts5, architecture]
---
# Hermes Memory Architecture (Luma Dock)

## Purpose

Understand Hermes' three-layer memory system from the Luma Dock tutorial — persona/frozen facts, skills/procedures, and session search.

## When to Use

- Designing memory for Hermes-based agents
- Debugging memory layer issues
- Understanding token costs per layer
- Editing memory files by hand safely

## When NOT to Use

- Quick memory setup (use persistent-memory guide)
- SOUL.md editing (use personality-soul guide)
- Session search only (use session_search tool)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug memory not loading, token overflow, corruption |
| `writing-plans` | Plan memory structure for new agent |

## Workflow

### Phase 1: Three Layers Overview

| Layer | Files | Purpose | Lifetime | Token Cost |
|-------|-------|---------|----------|------------|
| **1. Persona & Frozen Facts** | `~/.hermes/SOUL.md`, `~/.hermes/memories/MEMORY.md`, `~/.hermes/memories/USER.md` | Identity, environment facts, user profile | Stable, slow-changing, hand-curated | 1,500-5,000 tokens/session |
| **2. Skills** | `~/.hermes/skills/*/SKILL.md` + refs | Procedures, not facts | Auto-generated from successful tasks | 0 unless invoked |
| **3. Session Search** | `~/.hermes/state.db` (SQLite + FTS5) | Every message ever sent | Permanent, queryable | 0 unless queried |

### Phase 2: Layer 1 Detail

**SOUL.md** — Agent persona (slot #1 in prompt)
- Tone, style, directness level
- How to handle uncertainty, disagreement
- What to avoid (sycophancy, hype, over-explaining)
- Edit as plain markdown; loaded verbatim

**MEMORY.md** (2,200 char limit) — Agent's working knowledge
- Project context, ongoing themes, preferences
- Things like: "Working on Next.js SaaS at ~/code/brightcart"
- "Prefer Postgres over MySQL"
- "Replies default short unless detail requested"

**USER.md** (1,375 char limit) — User profile
- Name, role, timezone, preferences
- Communication style
- Pet peeves, things to avoid
- Technical skill level

**Format in prompt:**
```
═══ MEMORY (your personal notes) [67% — 1,474/2,200 chars] ═══
User's project is a Rust web service at ~/code/myapi using Axum + SQLx§This machine runs Ubuntu 22.04, has Docker and Podman installed§User prefers concise responses, dislikes verbose explanations
```
Entries separated by `§` (section sign).

### Phase 3: Frozen Snapshot Pattern

- Memory loaded ONCE at session start → injected into system prompt
- **Frozen** — changes during session don't affect current prompt
- Changes persist to disk immediately
- Visible in NEXT session only
- Tool responses show live state

### Phase 4: Auto-Write & Control

```yaml
memory:
  auto_write: true          # Agent writes when it learns
  reflection_enabled: true  # Daily synthesis pass
  write_approval: prompt    # "prompt" | "auto" — ask before writing
  char_limit_memory: 2200
  char_limit_user: 1375
```

**Disable auto-write:** `hermes config set memory.auto_write false`

### Phase 5: Reflection Pass

Daily background job:
- Reads recent sessions
- Distills patterns
- Writes to MEMORY.md or generates skills
- Runs on auxiliary model (configurable)

```bash
hermes config set auxiliary.background_review "openrouter:google/gemini-flash-1.5"
```

### Phase 6: Layer 2 — Skills

- Directory: `~/.hermes/skills/`
- One folder per skill with SKILL.md + optional refs
- Frontmatter declares triggers
- Auto-created after 3-4 similar successful tasks
- User-locked skills (`user_locked: true`) protected from regeneration
- Tokens only when invoked (progressive disclosure)

### Phase 7: Layer 3 — Session Search (state.db)

SQLite + FTS5 full-text search
- Every message: who, when, channel, content
- Agent queries via `session_search` tool
- Triggers: "did I discuss X", "what did user say about Y"
- Cost: few hundred to few thousand tokens per query
- DB growth: ~20-100 MB over 6 months
- Direct SQL: `sqlite3 ~/.hermes/state.db "SELECT ... WHERE content MATCH 'term'"`

### Phase 8: Manual Editing Rules

1. Don't edit mid-conversation — agent has stale context
2. Keep heading structure (`# Top`, `## Section`, `### Sub`)
3. Preserve timestamps (`<!-- written 2026-05-05 -->`)
4. Corrupted file → restore from backup

### Phase 9: Memory Across Installs

- Sync MEMORY.md between installs (Syncthing, rclone, NFS)
- Each install keeps own state.db → session histories separate
- Shared facts stay in sync; session privacy preserved

### Phase 10: Platform Detection & Error Handling

```python
import platform

def get_platform():
    system = platform.system().lower()
    if system == "windows":
        print(f"Windows: MEMORY.md/USER.md at %APPDATA%/Local/hermes/memories/")
    elif system == "linux":
        print("Linux: config at ~/.hermes/memories/")
    elif system == "darwin":
        print("macOS: config at ~/Library/Application Support/hermes/memories/")
    return system
```

**Memory error handling:**
```python
# Common memory issues
MEMORY_ERRORS = {
    "memory_not_loading": "Check file exists and is valid markdown",
    "token_limit_exceeded": "Reduce MEMORY.md below 2200 chars or USER.md below 1375",
    "corrupted_soul": "Fix YAML frontmatter in SOUL.md",
    "auto_write_disabled": "Run: hermes config set memory.auto_write true",
    "reflection_not_running": "Check: hermes config get memory.reflection_enabled",
}

def resolve_memory_error(error: str) -> str:
    for key, message in MEMORY_ERRORS.items():
        if key in error:
            return message
    return "Unknown memory error — check hermes logs"
```

### Phase 11: FAQ Operations

**See current context:** `/context` slash command
**Forget specific thing:** Delete from MEMORY.md/USER.md + optional state.db rows
**Share memory between installs:** Sync MEMORY.md only

## Pitfalls

- **Token cost ignored** — 12-16K fixed overhead before agent acts
- **Editing during session** — Changes don't affect current context
- **Memory full** — Agent must consolidate; can't auto-compact
- **Reflection noise** — Daily pass may add low-value entries
- **SOUL.md in wrong place** — Only `HERMES_HOME/SOUL.md` loads

## Verification Checklist

- [ ] SOUL.md loads as identity (slot #1)
- [ ] MEMORY.md/USER.md appear in context header
- [ ] Char limits respected
- [ ] Skills invoke on trigger
- [ ] session_search finds past conversations
- [ ] Reflection pass runs (if enabled)

## References

- `references/memory-layer-token-costs.md` — Detailed token accounting
- `references/memory-config-options.md` — All config.yaml memory settings
- `references/sqlite-queries.md` — Direct state.db queries
- `references/hermes-memory-patterns.md` — Memory file templates
- `references/hermes-memory-architecture.md` — Three-layer architecture

## Templates

- `templates/user-md-template.md` — USER.md template
- `templates/memory-md-template.md` — MEMORY.md template

## Scripts

- `scripts/memory-audit.py` — Audit memory file sizes