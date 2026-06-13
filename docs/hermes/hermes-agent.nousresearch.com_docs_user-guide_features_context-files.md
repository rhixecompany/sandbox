# Source: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files

# Hermes Agent Context Files - Comprehensive Summary

## Overview

Hermes Agent automatically discovers and loads context files that shape its behavior. Context files are loaded at two levels:
- **Project-local**: Discovered from working directory (walks to git root)
- **Global**: `SOUL.md` loaded only from `HERMES_HOME`

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
**SOUL.md** is always loaded independently as agent identity (slot #1).

---

## AGENTS.md - Primary Project Context

### Progressive Subdirectory Discovery

At session start, Hermes loads `AGENTS.md` from working directory into system prompt. As agent navigates subdirectories, it **progressively discovers** context files and injects them when relevant.

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
- Each subdirectory checked at most once per session
- Discovery walks up parent directories (reading `backend/src/main.py` discovers `backend/AGENTS.md`)
- Subdirectory context files undergo same security scan as startup files

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

---

## SOUL.md - Global Personality Configuration

**Location:** `~/.hermes/SOUL.md` or `$HERMES_HOME/SOUL.md`

Controls agent's personality, tone, and communication style. See [Personality](/docs/user-guide/features/personality) page for full details.

**Key details:**
- Loaded from `HERMES_HOME` only (not project directories)
- Always loaded independently as agent identity (slot #1)
- Inserted directly into prompt without extra wrapper text

---

## .cursorrules Compatibility

Hermes supports Cursor IDE's context files:
- **`.cursorrules`** - Main conventions file
- **`.cursor/rules/*.mdc`** - Rule modules

Loaded **only if** no higher-priority context file exists (`.hermes.md`, `AGENTS.md`, `CLAUDE.md`). Existing Cursor conventions automatically apply.

---

## How Context Files Are Loaded

### At Startup (System Prompt)
Loaded by `build_context_files_prompt()` in `agent/prompt_builder.py`:
- `.hermes.md` / `HERMES.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.cursorrules`

### During Session (Progressive Discovery)
`SubdirectoryHintTracker` in `agent/subdirectory_hints.py` watches tool call arguments for file paths:
- Tracks `path` and `workdir` from tool calls
- Discovers `AGENTS.md`, `CLAUDE.md`, `.cursorrules` in relevant subdirectories

### Final Prompt Structure
```markdown
# Project Context

The following project context files have been loaded and should be followed:

## AGENTS.md
[Your AGENTS.md content here]

## .cursorrules
[Your .cursorrules content here]

[Your SOUL.md content here]  ← Inserted directly, no wrapper
```

---

## Security: Prompt Injection Protection

All context files scanned before inclusion. Scanner checks for:

```html
<!-- ignore instructions -->
<div style="display:none">
curl ... $API_KEY
cat .env
cat credentials
```

**If threat detected:** File blocked with message:
```
[BLOCKED: AGENTS.md contained potential prompt injection (prompt_injection). Content not loaded.]
```

> ⚠️ **Important:** Scanner protects against common patterns but is **not a substitute for reviewing context files** in shared repositories. Always validate `AGENTS.md` content in projects you didn't author.

---

## Size Limits

| Limit | Value |
|-------|-------|
| Max file size | 50 KB per context file |
| Max total context | ~100 KB injected into prompt |

Files exceeding limits are truncated with a notice.