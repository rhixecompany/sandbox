# Hermes Agent Context Files - Comprehensive Summary

## Overview

Hermes Agent automatically discovers and loads context files that shape its behavior. Context files are categorized as **project-local** (discovered from working directory) or **global** (`SOUL.md` loaded from `HERMES_HOME` only).

---

## Supported Context Files

| File | Purpose | Discovery Method |
|------|---------|------------------|
| **`.hermes.md`** / **`HERMES.md`** | Project instructions (highest priority) | Walks to git root |
| **`AGENTS.md`** | Project instructions, conventions, architecture | CWD at startup + subdirectories progressively |
| **`CLAUDE.md`** | Claude Code context files (also detected) | CWD at startup + subdirectories progressively |
| **`SOUL.md`** | Global personality and tone customization | `HERMES_HOME/SOUL.md` only |
| **`.cursorrules`** | Cursor IDE coding conventions | CWD only |
| **`.cursor/rules/*.mdc`** | Cursor IDE rule modules | CWD only |

### Loading Priority (First Match Wins)

```
.hermes.md → AGENTS.md → CLAUDE.md → .cursorrules
```

**`SOUL.md` is always loaded independently** as agent identity (slot #1), regardless of project context.

---

## AGENTS.md - Primary Project Context

### Progressive Subdirectory Discovery

At session start, Hermes loads `AGENTS.md` from working directory into system prompt. As agent navigates subdirectories via tools (`read_file`, `terminal`, `search_files`), it **progressively discovers** context files in those directories and injects them when relevant.

```
my-project/
├── AGENTS.md           ← Loaded at startup (system prompt)
├── frontend/
│   └── AGENTS.md       ← Discovered when agent reads frontend/ files
├── backend/
│   └── AGENTS.md       ← Discovered when agent reads backend/ files
└── shared/
    └── AGENTS.md       ← Discovered when agent reads shared/ files
```

**Key behaviors:**
- Each subdirectory checked **at most once per session**
- Discovery walks up parent directories (reading `backend/src/main.py` discovers `backend/AGENTS.md`)
- Subdirectory context files undergo same **security scan** as startup files

### Example AGENTS.md Structure

```markdown
# Project Context

This is a Next.js 14 web application with a Python FastAPI backend.

## Architecture
- Frontend: Next.js 14 with App Router in `/frontend`
- Backend: FastAPI in `/backend`, uses SQLAlchemy ORM
- Database: PostgreSQL 16
- Deployment: Docker Compose on a Hetzner VPS

## Conventions
- Use TypeScript strict mode for all frontend code
- Python code follows PEP 8, use type hints everywhere
- All API endpoints return JSON with `{data, error, meta}` shape
- Tests go in `__tests__/` directories (frontend) or `tests/` (backend)

## Important Notes
- Never modify migration files directly — use Alembic commands
- The `.env.local` file has real API keys, don't commit it
- Frontend port is 3000, backend is 8000, DB is 5432
```

### Per-Subdirectory Context (Monorepos)

```markdown
<!-- frontend/AGENTS.md -->
# Frontend Context
- Use `pnpm` not `npm` for package management
- Components go in `src/components/`, pages in `src/app/`
- Use Tailwind CSS, never inline styles
- Run tests with `pnpm test`

<!-- backend/AGENTS.md -->
# Backend Context
- Use `poetry` for dependency management
- Run dev server with `poetry run uvicorn main:app --reload`
- All endpoints need OpenAPI docstrings
- Database models in `models/`, schemas in `schemas/`
```

---

## SOUL.md - Global Personality Configuration

**Location:** `~/AppData/Local/hermes/SOUL.md` or `$HERMES_HOME/SOUL.md`

Controls agent's personality, tone, and communication style. See [Personality](/docs/user-guide/features/personality) page for full details.

**Key details:**
- Loaded from `HERMES_HOME` only (not project directories)
- Always loaded independently as agent identity (slot #1)
- Inserted directly into prompt without extra wrapper text

---

## .cursorrules Compatibility

Hermes loads Cursor IDE's `.cursorrules` and `.cursor/rules/*.mdc` if:
1. They exist in project root
2. No higher-priority context file found (`.hermes.md`, `AGENTS.md`, `CLAUDE.md`)

This means existing Cursor conventions automatically apply when using Hermes.

---

## How Context Files Are Loaded

### At Startup (System Prompt)

Loaded by `build_context_files_prompt()` in `agent/prompt_builder.py`:

```python
# Priority order
.hermes.md → AGENTS.md → CLAUDE.md → .cursorrules
# Project Context section header added
```

### During Session (Progressive Discovery)

`SubdirectoryHintTracker` in `agent/subdirectory_hints.py` watches tool call arguments for file paths:

```python
# Watches for paths in tool calls
path → workdir → discovers AGENTS.md, CLAUDE.md, .cursorrules
```

### Final Prompt Structure

```markdown
# Project Context

The following project context files have been loaded and should be followed:

## AGENTS.md
[Your AGENTS.md content here]

## .cursorrules
[Your .cursorrules content here]

[Your SOUL.md content here]  # Inserted directly, no wrapper
```

---

## Security

All context files undergo a **security scan** before being added to the system prompt. The scan checks for:
- Prompt injection patterns
- Malicious instructions
- Attempts to override system behavior

Files that fail the scan are rejected with a warning.

---

## Best Practices

1. **Keep AGENTS.md focused** — token cost is injected into every message
2. **Use subdirectory AGENTS.md** for monorepos — avoids bloating root context
3. **One AGENTS.md per logical component** — frontend, backend, shared, infra
4. **SOUL.md for personality only** — not project instructions
5. **Leverage .cursorrules** — if you already use Cursor, no duplication needed

---

## Quick Reference

| File | Location | Scope | Priority |
|------|----------|-------|----------|
| `.hermes.md` / `HERMES.md` | Git root | Project | 1 (highest) |
| `AGENTS.md` | CWD + subdirs | Project | 2 |
| `CLAUDE.md` | CWD + subdirs | Project | 3 |
| `.cursorrules` | CWD | Project | 4 |
| `.cursor/rules/*.mdc` | CWD | Project | 4 |
| `SOUL.md` | `HERMES_HOME` | Global | Independent (slot #1) |

---

**Source:** [Hermes Agent Docs - Context Files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)  
**Extracted:** 2026-06-08