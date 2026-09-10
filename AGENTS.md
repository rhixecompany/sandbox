# AGENTS.md — Canonical Agent Guidance

## 1. Directory Map

```
SandBox/
├── AGENTS.md                # This file — canonical agent guidance (read first)
├── .hermes.md               # Hermes-specific project overrides (highest priority)
├── README.md                # Project overview
├── CLAUDE.md / .cursorrules # Thin stubs deferring here
├── .github/prompts/         # Canonical prompt library (190+ prompts)
├── projects/                # 16+ subprojects (monorepo)
│   ├── Bash/                # Primary automation toolkit (Bun/TS)
│   ├── Banking/             # Next.js fintech (Drizzle, Plaid, Dwolla)
│   ├── comicwise/           # Next.js comic streaming (Prisma, Stripe)
│   ├── ecom/                # Django REST + React/Redux ecommerce
│   ├── mcp-servers/         # Multi-language MCP server implementations
│   ├── Python-projects/     # 18 standalone Python scripts
│   └── ...                  # 10+ additional subprojects
├── scripts/                 # Pointer README — canonical scripts live in ~/AppData/Local/hermes/scripts/
├── docs/                    # Documentation, architecture blueprints, audits
├── .hermes/                 # Hermes session state, plans, audits
├── .vscode/                 # VS Code settings
├── venv/ + requirements.txt # Python 3.11 virtualenv
├── node_modules/            # Root-level Bun/Node deps
└── *.py, *.ts, *.json       # Root-level analysis scripts and config
```

## 2. Technology Stack

| Layer | Technology | Notes |
|-------|-----------|-------|
| **Runtime (TS)** | Bun 1.3.14+ | Runtime + package manager + test runner; `bun install` + `bun run <script>` |
| **Runtime (Python)** | Python 3.11 / 3.13 | Dual install: python3=3.13.14, python=3.11.15; `uv` preferred for speed |
| **Python Package Mgr** | pip + uv | `uv pip install` faster than pip; `requirements.txt` at root |
| **TypeScript** | ESNext, strict mode | `noUncheckedIndexedAccess`, `verbatimModuleSyntax`; `bun run typecheck` |
| **Python Quality** | Ruff + Pyright | `ruff check .` / `pyright .`; zero-warning gate |
| **JS Linting** | ESLint 10 flat config | `eslint.config.mjs` (root); zero-warning gate |
| **Formatter** | Prettier 3 | `.prettierrc.json` at root; `printWidth: 120, singleQuote: false, tabWidth: 2, trailingComma: "all"` |
| **Markdown** | markdownlint-cli2 | MD013 disabled (`.markdownlint.jsonc` sets `MD013: false`); line_length no longer enforced |
| **Spell Check** | cspell 10 | `.cspell.json` in subprojects; not at root |
| **Testing (TS)** | Vitest | `bun run test`; `vitest run` in Bash |
| **Testing (Python)** | pytest 9 | `python -m pytest -v` or `python test.py`; `pytest-asyncio` |
| **Browser Testing** | Playwright | `.github/prompts/playwright-*.prompt.md`; `bun run test:ui` in Banking |
| **Pre-commit** | pre-commit 4.6 | `.pre-commit-config.yaml` at root |
| **Changelog** | git-cliff 2.13 | `cliff.toml`; `git cliff` for CHANGELOG generation |

## 3. Architecture Overview

### Workspace Pattern: Hermes-Centric Monorepo

The SandBox is a multi-language monorepo workspace tightly integrated with **Hermes Agent**. Every subproject under `projects/` is autonomous — each has its own `AGENTS.md`, `package.json`, `README.md`, and build system.

### Cross-Component Communication

- **Shared CI**: `.github/workflows/` at workspace root applies to `projects/Bash/` and matching subprojects
- **Prompt Library**: All `.github/prompts/*.prompt.md` are the single source of truth — consumed by Copilot, OpenCode, and Hermes agents
- **Hermes Profile Routing**: code→architect, research→analyst, design→creative, planning→exec, teaching→tutor, ops→adminbot, general→default

### MCP-First Tool Precedence

Before using native tools (terminal commands, direct file access), check MCP servers. The workspace has **16 active MCP servers** configured.

## 4. Critical Developer Workflows

### Workspace Root

```bash
# Python setup (workspace root)
cd C:/Users/Alexa/Desktop/SandBox
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

# Bun/TypeScript (workspace root - minimal)
bun install
bun run index.ts
```

### Subproject Workflows

Each subproject has its own AGENTS.md with specific commands. Key workflows:

- **Bash**: `bun run test` (Vitest), `bash test-all.sh` (shell script testing), `bash verify-dryrun.sh` (dry-run checks)
- **Banking**: `bun run build` (Next.js), `bun run test:ui` (Playwright), `bun run lint:strict`, `bun run verify:rules`
- **Python-projects**: `ruff check .` (lint), `pyright .` (typecheck), `python -m pytest -v` (tests), `python basic_calculator.py` (smoke)

## 5. Codebase Patterns & Conventions

### File Naming

| Language | Convention | Example |
|----------|-----------|---------|
| TypeScript | `kebab-case.ts` (scripts), `PascalCase.tsx` (components) | `cache-clean.ts`, `UserProfile.tsx` |
| Python | `snake_case.py` (PEP 8) | `health_check.py`, `audit_prompts.py` |
| PowerShell | `PascalCase.ps1` | `Orchestrator-Unified.ps1` |
| Shell (Bash) | `kebab-case.sh` | `test-all.sh`, `cache-clean.sh` |
| Markdown | `kebab-case.md` | `health-check.md` |

### Code Style

- **TypeScript**: 2-space indent, single-quotes, strict mode, `noUncheckedIndexedAccess`
- **Python**: 4-space indent (PEP 8), double-quotes, type hints encouraged
- **Line endings**: CRLF (`.editorconfig` — Windows host)
- **No `any`** unless explicitly justified and exempted
- **No backup files** (`.bak`, `.old`) — use git for rollback
- **Dry-run first** on all destructive operations

### Multi-Wrapper Parity

Every script that could run cross-platform MUST have three wrappers:

```bash
# Canonical: ~/AppData/Local/hermes/scripts/
scripts/operation.sh     # Bash (Linux/WSL/Git Bash)
scripts/operation.ps1    # PowerShell (Windows)
scripts/operation.bat    # Batch (Windows fallback)
```

### Git Commit Convention

```
<type>: <description>

Types: feat, fix, docs, refactor, test, chore, perf
Examples:
  feat: add cache-clean dry-run mode
  fix: correct Plaid webhook signature validation
  refactor: extract database connection pool
  chore: update bun lockfile
```

### Git Branch Convention

```
<type>/<project>/<kebab-case-description>

Examples:
  feat/bash/add-dry-run-mode
  fix/banking/plaid-webhook-signature
  refactor/ecom/extract-payment-service

- **PR target branch**: `development` (not `main`)
```

## 6. .github/prompts Library

The prompt library at `.github/prompts/` is the single source of truth for all prompt-family content.

### Structure

```
.github/prompts/
├── index.md                           # Library overview
├── *.prompt.md                        # Canonical prompts (190+)
├── templates/                         # Shared templates
└── archived/                          # Deprecated prompts
```

### Key Prompt Categories

| Category | Example Files | Purpose |
|----------|--------------|---------|
| Architecture | `architecture-blueprint-generator.prompt.md`, `folder-structure-blueprint-generator.prompt.md`, `technology-stack-blueprint-generator.prompt.md` | Generate architecture docs |
| Generator | `agents-generator.prompt.md`, `create-agentsmd.prompt.md`, `readme-blueprint-generator.prompt.md` | Generate agent guidance |
| Dev | `debug-issue.prompt.md`, `refactor-code.prompt.md`, `code-review.prompt.md` | Development workflows |
| Testing | `write-tests.prompt.md`, `playwright-generate-test.prompt.md`, `pytest-coverage.prompt.md` | Test generation |
| DevOps | `containerize-aspnetcore.prompt.md`, `multi-stage-dockerfile.prompt.md`, `terraform-azurerm-set-diff-analyzer.prompt.md` | Infrastructure |
| Planning | `create-implementation-plan.prompt.md`, `breakdown-plan.prompt.md`, `executing-plans.prompt.md` | Project planning |
| Content | `comprehensive-prompt-enhancer.prompt.md`, `convert-plaintext-to-md.prompt.md` | Content creation |

## 7. Hermes Agent Integration

### Profile Configuration

| Profile | Model / Guidance |
|---------|-----------------|
| **default** | Verify with `hermes profile list` / `hermes config show` |
| alexa | Verify with `hermes profile list` / `hermes config show` |
| code-architect | Verify with `hermes profile list` / `hermes config show` |
| creative-director | Verify with `hermes profile list` / `hermes config show` |
| exec-assistant | Verify with `hermes profile list` / `hermes config show` |
| patient-tutor | Verify with `hermes profile list` / `hermes config show` |
| research-analyst | Verify with `hermes profile list` / `hermes config show` |

### Provider Configuration

| Provider | Auth Method | Default Model | Vision | Reasoning | Context |
|----------|-------------|---------------|--------|-----------|---------|
| **nous** | OAuth (device_code) | meituan/longcat-2.0:free | yes | yes | 2000 |
| **opencode-zen** | API Key + OAuth | nemotron-3-ultra-free | yes | yes | 2000 |
| **openrouter** | API Key | nvidia/nemotron-3-ultra-550b-a55b:free | yes | yes | 2000 |

### Session Startup Sequence

```
1. Read SESSION_REPORT.md (workspace root) — last session summary

2. Load mandatory skills:
  - using-superpowers (foundational workflow)
  - user-communication-preferences (safety constraints)
  - session-audit-report (session analysis)
  - hermes-profiles (profile management)
  - validate-memories (memory verification)

3. Review .hermes/SESSION_REPORT.md for session context

4. If any mandatory skill fails → ABORT and report
```

### File Hierarchy (Precedence Order)

| # | File | Purpose | Authority |
|---|------|---------|-----------|
| 1 | `.hermes.md` | Hermes-specific overrides | Highest — overrides all below |
| 2 | `AGENTS.md` | General agent guidance | This file |
| 3 | `PROJECT_RULES.md` | Workspace-level rules | Rules |
| 4 | `MASTER_RULES.md` | Universal agent rules | Cross-project rules |
| 5 | `CLAUDE.md` | Claude-specific behavior | Copilot/Claude only |
| 6 | `.cursorrules` | Cursor IDE rules | Cursor IDE only |

### Available Hermes Toolsets (16)

`web`, `browser`, `terminal`, `file`, `code_execution`, `vision`, `image_gen`, `tts`, `skills`, `todo`, `memory`, `context_engine`, `session_search`, `clarify`, `delegation`, `cronjob`

### Active Hooks (3)

`session-logger` | `session-auto-commit` | `governance-audit`

## 8. Safety Rules

1. **Never commit secrets** — `.env`, tokens, credentials
2. **No destructive ops without approval** — explain risks first
3. **Verify before claim** — test, check, confirm before reporting
4. **MCP-first** — use MCP servers over native tools where available
5. **Profile per task** — switch profile before execution
6. **Strict sequential** — "only then" is a hard constraint

---
*Last updated: 2026-09-08 by comprehensive implementation prompt v3.0*