---
name: hermes-context
description: Context files (AGENTS.md, SOUL.md, CLAUDE.md, .cursorrules) discovery, priority, and progressive loading
version: 1.0.0
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [hermes, context-files, agents, soul, cursorrules]
    category: context-files
    requires_toolsets: [terminal, file, skills]
    config:
      - key: hermes.skill.context.enabled
        description: "Enable context files skill"
        default: "true"
---

# Hermes Context Files Skill

## When to Use
- Setting up project context (AGENTS.md, .cursorrules)
- Understanding context file discovery and priority
- Configuring progressive subdirectory discovery for monorepos
- Debugging context loading issues

## Procedure
1. **Supported Context Files**:
   | File | Purpose | Discovery Method |
   |------|---------|------------------|
   | `.hermes.md` / `HERMES.md` | Project instructions (highest priority) | Walks to git root |
   | `AGENTS.md` | Project instructions, conventions, architecture | CWD at startup + subdirs progressively |
   | `CLAUDE.md` | Claude Code context files (also detected) | CWD at startup + subdirs progressively |
   | `SOUL.md` | Global personality and tone | `HERMES_HOME/SOUL.md` only |
   | `.cursorrules` | Cursor IDE coding conventions | CWD only |
   | `.cursor/rules/*.mdc` | Cursor IDE rule modules | CWD only |

2. **Loading Priority** (First Match Wins):
   ```
   .hermes.md → AGENTS.md → CLAUDE.md → .cursorrules
   ```
   **SOUL.md is always loaded independently** as agent identity (slot #1)

3. **Progressive Subdirectory Discovery**:
   At session start, Hermes loads `AGENTS.md` from working directory. As agent navigates subdirectories via tools (`read_file`, `terminal`, `search_files`), it **progressively discovers** context files in those directories.
   
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
   
   Key behaviors:
   - Each subdirectory checked **at most once per session**
   - Discovery walks up parent directories
   - Subdirectory context files undergo same **security scan**

4. **Example AGENTS.md Structure**:
   ```markdown
   # Project Context
   
   This is a Next.js 14 web app with Python FastAPI backend.
   
   ## Architecture
   - Frontend: Next.js 14 with App Router in `/frontend`
   - Backend: FastAPI in `/backend`, uses SQLAlchemy ORM
   - Database: PostgreSQL 16
   - Deployment: Docker Compose on Hetzner VPS
   
   ## Conventions
   - Use TypeScript strict mode for all frontend code
   - Python code follows PEP 8, use type hints everywhere
   - All API endpoints return JSON with {data, error, meta} shape
   - Tests go in __tests__/ (frontend) or tests/ (backend)
   
   ## Important Notes
   - Never modify migration files directly — use Alembic commands
   - The .env.local file has real API keys, don't commit it
   - Frontend port 3000, backend 8000, DB 5432
   ```

5. **Per-Subdirectory Context (Monorepos)**:
   ```markdown
   <!-- frontend/AGENTS.md -->
   # Frontend Context
   - Use pnpm not npm for package management
   - Components in src/components/, pages in src/app/
   - Use Tailwind CSS, never inline styles
   - Run tests with pnpm test
   
   <!-- backend/AGENTS.md -->
   # Backend Context
   - Use poetry for dependency management
   - Run dev server: poetry run uvicorn main:app --reload
   - All endpoints need OpenAPI docstrings
   - Database models in models/, schemas in schemas/
   ```

6. **.cursorrules Compatibility**:
   - Reads `.cursorrules` and `.cursor/rules/*.mdc` automatically
   - Only if no higher-priority context file found
   - Existing Cursor conventions apply when using Hermes

7. **How Context Files Are Loaded**:
   - **At Startup**: `build_context_files_prompt()` in `agent/prompt_builder.py`
   - **During Session**: `SubdirectoryHintTracker` in `agent/subdirectory_hints.py` watches tool call arguments
   - **Final Prompt Structure**:
     ```
     # Project Context
     
     The following project context files have been loaded:
     
     ## AGENTS.md
     [Your AGENTS.md content]
     
     ## .cursorrules
     [Your .cursorrules content]
     
     [Your SOUL.md content]  # Inserted directly, no wrapper
     ```

8. **Security**: All context files scanned for prompt injection before adding to system prompt

## Pitfalls
- **Context not loading** → Check file exists at correct path; verify priority order
- **Subdirectory not discovered** → Each dir checked once/session; restart to re-discover
- **SOUL.md ignored** → Must be at `HERMES_HOME/SOUL.md`, not project dir
- **Duplication** → Keep subdirectory AGENTS.md focused; avoid repeating root content
- **Token bloat** → AGENTS.md injected every message — keep focused and concise

## Verification
- Start session → root AGENTS.md loaded in system prompt
- Navigate to subdirectory → its AGENTS.md progressively loaded
- `hermes chat -q "What project am I in?"` returns correct context
- No security scan warnings in logs

## References
- `references/commands.md` — CLI commands
- `references/priority-table.md` — File priority reference
- `references/best-practices.md` — Context file best practices