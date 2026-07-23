# PROJECT_RULES.md — SandBox Workspace Rules

> **Hierarchy:** `.hermes.md` → `AGENTS.md` → `PROJECT_RULES.md` → `MASTER_RULES.md` → `.cursorrules`

## 1. Context File Hierarchy

Files are loaded in this order (each overrides the previous):

| File | Purpose |
|------|---------|
| `.hermes.md` | Hermes-specific project overrides (profiles, MCP, hooks, plugins, toolsets) |
| `AGENTS.md` | General agent guidance (toolchain, conventions, subprojects) |
| `PROJECT_RULES.md` | This file — workspace-level rules |
| `MASTER_RULES.md` | Universal agent rules (core principles) |
| `.cursorrules` | Cursor IDE-specific rules |

## 2. Working Tree State

- **Current branch:** `development`
- **Status:** 3 modified files (per git status)
- **Last commit:** `8aa1f47f` chore: snapshot local workspace updates

## 3. Session Startup Protocol

Per SOUL.md and mandatory 5-skill startup:

1. Read `SESSION_REPORT.md`
2. Load `user-communication-preferences`
3. Verify `USER.md` at `~/AppData/Local/hermes/memories/USER.md`
4. Verify `SOUL.md` at `~/AppData/Local/hermes/SOUL.md`
5. Validate memories across profiles

## 4. Profile Routing

| Task Type | Profile |
|-----------|---------|
| Code implementation, debugging, refactoring | `code-architect` |
| Deep research, literature review, synthesis | `research-analyst` |
| Design, content creation, brainstorming | `creative-director` |
| Planning, coordination, admin | `exec-assistant` |
| Tutorials, explanations, teaching | `patient-tutor` |
| System operations, DevOps, infra | `alexa` |
| General purpose | `default` |

## 5. MCP-First Tool Precedence

Before native tools, check MCP servers:

| MCP Server | Purpose |
|------------|---------|
| `filesystem` | File operations |
| `github` | GitHub API |
| `ast-grep` | Code search/replace |
| `memory` | Persistent memory (knowledge graph) |
| `playwright` | Browser automation |
| `sequential-thinking` | Structured reasoning |
| `cli` | Command execution |
| `code-sandbox` | Isolated Node.js execution |
| `fetch` | HTTP requests |
| `mcp-docker` | Docker management |
| `smithery` | Registry discovery |
| `copilot-mcp` | GitHub Copilot provider |

## 6. Known Issues & Corrections

From AGENTS.md §13 (verified 2026-07-09):

1. `.github/copilot-instructions.md` references root `Bash/` — toolkit is at `projects/Bash/`
2. CI path filter `Bash/**` — should be `projects/Bash/**`
3. `README.md` references `PROJECT_RULES.md` — file now created
4. Prompt boilerplate "use pnpm" is wrong — toolchain is bun
5. Inventory counts in `copilot-instructions.md` stale (2026-05-30 snapshot vs current 174 agents/186 instructions)

## 7. Validation Commands

```bash
# From projects/Bash/
bun run format       # prettier
bun run typecheck    # tsc --noEmit
bun run lint:strict  # eslint --max-warnings=0
bun run test         # vitest
```

## 8. Git Workflow

- **PR target:** `development` (not `master`)
- **Branch naming:** `<type>/<project>/<kebab-case-description>`
- **Commit format:** `type: description` (feat/fix/docs/refactor/test/chore/perf)
- **Default branch:** `production` (per PRESTATE_SandBox.md)