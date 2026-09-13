# AGENTS.md — Canonical Agent Guidance

Pointer + workspace-specific supplements. Persona + rules → `SOUL.md`. Style →
`user-communication-preferences` skill. Multi-file → `multi-file-change-protocol` skill.

## Multi-File Trigger

>6 file changes → load skill `multi-file-change-protocol` (14-skill stack + 5-step process).

## 1. Directory Map

```
SandBox/
├── AGENTS.md                # This file
├── .hermes.md               # Hermes-specific overrides (highest priority)
├── README.md                # Project overview
├── CLAUDE.md / .cursorrules # Thin stubs
├── .github/prompts/         # Prompt library (190+ prompts)
├── projects/                # 16+ subprojects (monorepo)
│   ├── Bash/                # Bun/TS automation toolkit
│   ├── Banking/             # Next.js fintech
│   ├── comicwise/           # Next.js comic streaming
│   ├── ecom/                # Django REST + React/Redux
│   ├── mcp-servers/         # Multi-language MCP servers
│   └── Python-projects/     # 18 standalone Python scripts
├── scripts/                 # Pointer → canonical at ~/AppData/Local/hermes/scripts/
├── docs/                    # Architecture blueprints, audits
├── .hermes/                 # Plans, specs, session state
├── .vscode/                 # VS Code settings
└── venv/ + requirements.txt # Python 3.11 virtualenv
```

## 2. Workspace Workflows

### Workspace Root
```bash
cd C:/Users/Alexa/Desktop/SandBox
python -m venv venv && source venv/Scripts/activate
pip install -r requirements.txt
bun install && bun run index.ts
```

### Subprojects
| Project | Commands |
|---|---|
| Bash | `bun run test`, `bash test-all.sh`, `bash verify-dryrun.sh` |
| Banking | `bun run build`, `bun run test:ui`, `bun run lint:strict` |
| Python-projects | `ruff check .`, `pyright .`, `python -m pytest -v` |

## 3. Conventions

| Topic | Convention |
|---|---|
| TS files | `kebab-case.ts` (scripts), `PascalCase.tsx` (components) |
| Python files | `snake_case.py` (PEP 8) |
| Markdown | `kebab-case.md` |
| TS style | 2-space, single-quotes, strict, no `any` |
| Python style | 4-space, double-quotes, type hints |
| Line endings | CRLF (`.editorconfig`) |
| Commit type | `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf` |
| Branch | `<type>/<project>/<kebab>` → PR target `development` |
| No backup files | `.bak`/`.old` — use git for rollback |
| Destructive ops | Dry-run first, explain risks |

## 4. Multi-Wrapper Parity

Cross-platform scripts need 3 wrappers under `~/AppData/Local/hermes/scripts/`:
```bash
scripts/operation.sh     # Bash
scripts/operation.ps1    # PowerShell
scripts/operation.bat    # Batch fallback
```

## 5. .github/prompts Library

Single source of truth for all prompt-family content.

```
.github/prompts/
├── index.md
├── *.prompt.md            # 190+ canonical prompts
├── templates/             # Shared templates
└── archived/              # Deprecated
```

| Category | Examples |
|---|---|
| Architecture | `architecture-blueprint-generator.prompt.md`, `folder-structure-blueprint-generator.prompt.md` |
| Generator | `agents-generator.prompt.md`, `create-agentsmd.prompt.md`, `readme-blueprint-generator.prompt.md` |
| Dev | `debug-issue.prompt.md`, `refactor-code.prompt.md`, `code-review.prompt.md` |
| Testing | `write-tests.prompt.md`, `playwright-generate-test.prompt.md`, `pytest-coverage.prompt.md` |
| DevOps | `containerize-aspnetcore.prompt.md`, `multi-stage-dockerfile.prompt.md` |
| Planning | `create-implementation-plan.prompt.md`, `breakdown-plan.prompt.md`, `executing-plans.prompt.md` |

## 6. MCP-First Tool Precedence

23 active MCP servers. Before any native tool, check MCP equivalents. Priority:
filesystem → github → ast-grep → playwright → fetch → sequential-thinking →
code-sandbox → mcp-docker → memory → python-quality → tooling-lint →
tooling-config.

## 7. Session Startup Sequence

1. Read `SESSION_REPORT.md` (workspace root)
2. Load mandatory skills: `using-superpowers`, `user-communication-preferences`,
   `session-audit-report`, `hermes-profiles`, `validate-memories`
3. Review `.hermes/SESSION_REPORT.md` for session context
4. If any mandatory skill fails → ABORT and report

## 8. File Hierarchy (Precedence)

| # | File | Authority |
|---|---|---|
| 1 | `.hermes.md` | Highest |
| 2 | `AGENTS.md` | This file |
| 3 | `CLAUDE.md` | Copilot/Claude only |
| 4 | `.cursorrules` | Cursor IDE only |

## 9. Safety Rules

1. Never commit secrets — `.env`, tokens, credentials
2. No destructive ops without approval — explain risks first
3. Verify before claim — test, check, confirm
4. MCP-first — use MCP servers over native
5. Profile per task — switch profile before execution
6. Strict sequential — "only then" is a hard constraint