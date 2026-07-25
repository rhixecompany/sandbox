---
name: hermes-persistent-memory
title: "Hermes Persistent Memory (Official Docs)"
description: "Use when configuring and using Hermes bounded persistent memory — MEMORY.md (2,200 chars) and USER.md (1,375 chars), auto-write, reflection, write approval, external providers."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [hermes, memory, persistent, memory-md, user-md, auto-write, reflection, config]
---
# Hermes Persistent Memory (Official Documentation)

## Purpose

Official guide for Hermes Agent's bounded, curated memory system — MEMORY.md (agent notes) and USER.md (user profile) with strict character limits.

## When to Use

- Configuring memory behavior
- Understanding auto-write and reflection
- Setting write approval modes
- Setting up external memory providers

## When NOT to Use

- SOUL.md personality (different file)
- Session search (SQLite, different tool)
- Skills (procedural, different system)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug memory not writing, char limit errors |
| `executing-plans` | Configure memory, set up external providers |

## Workflow

### Phase 1: How It Works

Two files in `~/.hermes/memories/`:
- **MEMORY.md** (2,200 chars) — Agent's personal notes: environment facts, conventions, lessons, completed work
- **USER.md** (1,375 chars) — User profile: identity, preferences, communication style, skill level

Injected as frozen snapshot at session start. Changes persist to disk immediately but appear in prompt next session.

### Phase 2: Memory Tool Actions

Agent uses `memory` tool:
- **add** — New entry
- **replace** — Update existing (substring match via `old_text`)
- **remove** — Delete entry (substring match via `old_text`)

No `read` action — content always in system prompt.

### Phase 3: Substring Matching

`replace`/`remove` use short unique substring:
```python
# If memory contains "User prefers dark mode in all editors"
memory(action="replace", target="memory",
       old_text="dark mode",
       content="User prefers light mode in VS Code, dark mode in terminal")
```

Multiple matches → error asking for more specific substring.

### Phase 4: Two Targets Explained

| Target | Purpose | Examples |
|--------|---------|----------|
| `memory` | Agent's notes | Environment facts, project context, conventions, completed work, tool quirks, explicit requests |
| `user` | User profile | Name, role, timezone, communication prefs, pet peeves, workflow habits, skill level |

### Phase 5: What to Save vs Skip

**Save (Proactively):**
- User preferences: "I prefer TypeScript over JavaScript" → USER
- Environment facts: "Server runs Debian 12, PostgreSQL 16" → MEMORY
- Corrections: "Don't use sudo for Docker, user in docker group" → MEMORY
- Conventions: "Project uses tabs, 120-char width, Google docstrings" → MEMORY
- Completed work: "Migrated auth from JWT to session cookies 2026-03-14" → MEMORY
- Explicit requests: "Remember API key rotation monthly" → MEMORY

**Skip:**
- Trivial/obvious: "User asked about Python"
- Easily rediscovered: "Python 3.12 supports f-string nesting"
- Raw data dumps: Large code blocks, logs, tables
- Session ephemera: Temp paths, one-off debug context
- Already in SOUL.md/AGENTS.md

### Phase 6: Capacity Management

| Store | Limit | Typical Entries |
|-------|-------|-----------------|
| MEMORY.md | 2,200 chars | 8-15 |
| USER.md | 1,375 chars | 5-10 |

**When full:** `memory` tool returns error. Agent must:
1. Review current entries
2. Consolidate similar entries
3. Remove stale/irrelevant entries
4. Retry write

No silent dropping — agent always aware of what's forgotten.

### Phase 7: Good Entry Examples

**MEMORY.md (agent notes):**
- `This machine runs Windows 11, WSL2 Ubuntu 22.04, Docker Desktop + Podman` (83 chars)
- `Project uses pnpm workspaces, monorepo at ~/code/monorepo, TypeScript strict` (85 chars)
- `Docker commands work without sudo — user in docker group` (53 chars)
- `Completed: migrated auth from JWT to session cookies on 2026-03-14` (59 chars)
- `Avoid npm install -g — use pnpm dlx or project-local bins` (64 chars)

**USER.md (user profile):**
- `Name: Alex. Timezone: America/Los_Angeles (PDT). Work hours: Mon-Fri 9-5` (59 chars)
- `Prefers concise responses — lead with action, explain second` (53 chars)
- `Dislikes emoji and corporate-speak ("I'd be happy to help")` (52 chars)
- `Technical level: senior engineer. Don't explain basics unless asked` (56 chars)
- `Pet peeve: variable names like data, info, obj — use descriptive names` (60 chars)

### Phase 8: Duplicate Prevention

Substring overlap >80% on existing entry blocks `add`. Prevents repeated facts.

### Phase 9: Security Scanning

All writes scanned for:
- Prompt injection patterns
- PII (emails, API keys, tokens, addresses)
- Suspicious instructions

Flagged writes blocked and logged.

### Phase 10: Session Search (Separate)

SQLite `state.db` with FTS5 — independent of memory tool.

| Aspect | session_search | memory |
|--------|----------------|--------|
| Scope | All past conversations | Curated facts only |
| Freshness | Real-time (includes last msg) | Frozen at session start |
| Granularity | Full messages | Condensed entries |
| Cost | On-demand query | Always in prompt |
| Use for | "What did we discuss about X?" | "What OS does user run?" |

### Phase 11: Configuration

```yaml
memory:
  auto_write: true          # Agent writes when it learns
  reflection_enabled: true  # Daily reflection pass
  write_approval: prompt    # "prompt" | "auto"
  char_limit_memory: 2200   # Custom limit
  char_limit_user: 1375     # Custom limit
```

- `auto_write: false` → agent tells you what it would write
- `write_approval: "auto"` → agent writes without prompting (caution)

### Phase 12: Controlling Memory Writes

```bash
# Auto-approve
hermes config set memory.write_approval auto

# Require prompt (default)
hermes config set memory.write_approval prompt
```

### Phase 13: Background Review Notifications

```bash
hermes config set display.memory_notifications true
```

Shows toast when background review writes to memory.

### Phase 14: Cheaper Reflection Model

```bash
hermes config set auxiliary.background_review "openrouter:google/gemini-flash-1.5"
```

### Phase 15: Skill Write Approval

```bash
hermes config set skills.write_approval auto
# or prompt
```

### Phase 16: External Memory Providers

Pluggable backends: databases, vector stores, remote services. See Memory Providers docs.

## Pitfalls

- **Char limit errors** — Agent must consolidate; can't ignore
- **Reflection noise** — Daily pass may add low-value entries
- **Frozen snapshot** — Mid-session edits don't affect current context
- **SOUL.md confusion** — Separate file, different purpose (persona)
- **Provider complexity** — External providers need custom implementation

## Verification Checklist

- [ ] MEMORY.md/USER.md exist at `~/.hermes/memories/`
- [ ] Char limits respected
- [ ] Auto-write works (or prompts correctly)
- [ ] Reflection runs daily (if enabled)
- [ ] Write approval behavior matches config
- [ ] Security scan doesn't block legitimate entries
- [ ] Session search works independently

## References

- `references/memory-providers.md` — External provider interface
- `references/reflection-prompts.md` — Background review prompts
- `references/security-scan-patterns.md` — Blocked patterns