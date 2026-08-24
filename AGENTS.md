---

# AGENTS.md Template — Canonical Agent Guidance
#

# USAGE: This is the MASTER template for AGENTS.md at workspace root.
# Subprojects should have thin AGENTS.md that defer to this root file.

# All shared rules, conventions, workflows defined HERE.
# Subproject AGENTS.md only contains project-specific overrides.
#

# REQUIRED VARIABLES:
#   SandBox       - Workspace name (e.g., "SandBox")

#   C:/Users/Alexa/Desktop/SandBox       - Absolute workspace path
#   C:/Users/Alexa/AppData/Local/hermes          - Hermes home path

#   2026-08-24        - Last verified date

---

# SandBox — AGENTS.md

Canonical agent guidance. First file agents should read. Other instruction files are thin stubs that defer here.

> Verified 2026-08-24. No aspirational practices.

---

## 1. Directory Map

```text
SandBox/
├── AGENTS.md                # This file — canonical agent guidance (read first)
├── .hermes.md               # Hermes-specific project overrides (highest priority)
├── README.md                # Project overview
├── CLAUDE.md / .cursorrules # Thin stubs deferring here
├── .github/prompts/         # Canonical prompt library (190+ prompts)
├── projects/                # 16+ subprojects (monorepo)
│   ├── Bash/                # Primary automation toolkit (Bun/TypeScript)
│   ├── Banking/             # Next.js fintech (Drizzle, Plaid, Dwolla)
│   ├── comicwise/           # Next.js comic streaming (Prisma, Stripe)
│   ├── ecom/                # Django REST + React/Redux ecommerce
│   ├── mcp-servers/         # Multi-language MCP server implementations
│   ├── Python-projects/     # 18 standalone Python scripts
│   └── ...                  # 10+ additional subprojects
├── scripts/                 # Pointer README — canonical scripts live in C:/Users/Alexa/AppData/Local/hermes/scripts/
├── docs/                    # Documentation, architecture blueprints, audits
├── .hermes/                 # Hermes session state, plans, audits
├── .vscode/                 # VS Code workspace settings
│   ├── settings.json        # Ruff for Python, Prettier for TS/JS formatting
│   ├── extensions.json      # Recommended extensions
│   └── launch.json          # Debug configurations
├── venv/ + requirements.txt # Python 3.11 virtualenv
├── node_modules/            # Root-level Bun/Node deps
└── *.py, *.ts, *.json       # Root-level analysis scripts and config

```

---

## 2. Technology Stack

| Layer | Technology | Notes |
|-------|------------|-------|
| **Runtime (TS)** | Bun 1.3.14+ | Runtime + package manager + test runner. DO NOT use npm/pnpm unless project says otherwise |
| **Runtime (Python)** | Python 3.11 / 3.13 | Dual install: python3=3.13.14, python=3.11.15 (venv). PEP 668 enforced |
| **Python Package Mgr** | pip + uv | Requirements in `requirements.txt`. Prefer uv for speed |
| **TypeScript** | ESNext target, strict mode | `tsconfig.json` — `noUncheckedIndexedAccess`, `verbatimModuleSyntax`, `Preserve` modules |
| **Python Quality** | Ruff + Pyright | Ruff for lint/format (select E,F,I,N,W,UP,B), Pyright for typecheck |
| **JS Linting** | ESLint 10 flat config | `eslint.config.mts` — zero-warning gate (`--max-warnings=0`) |
| **Formatter** | Prettier 3 | `.prettierrc.json` / `.prettierrc.ts` |
| **Markdown** | markdownlint-cli2 | `.markdownlintrc.json` — MD013 line_length=500, fenced backtick style |
| **Spell Check** | cspell 10 | `cspell.json` |
| **Testing (TS)** | Vitest | `bun run test` or `vitest run` |
| **Testing (Python)** | pytest 9 | `pytest` with `pytest-asyncio` |
| **Browser Testing** | Playwright | `.github/prompts/playwright-*.prompt.md` patterns |
| **Pre-commit** | pre-commit 4.6 | `.pre-commit-config.yaml` |
| **Changelog** | git-cliff 2.13 | `cliff.toml` |
| **EditorConfig** | `.editorconfig` | indent_style=tab, indent_size=2, end_of_line=crlf, charset=utf-8 |

---

## 3. Architecture Overview

### Workspace Pattern: Hermes-Centric Monorepo

The SandBox is a multi-language monorepo workspace tightly integrated with **Hermes Agent**. Every subproject under `projects/` is autonomous — each has its own `AGENTS.md`, `package.json`, `README.md`, and build system. The workspace root provides shared config, tooling, and prompt libraries.

### Cross-Component Communication

- **Shared CI**: `.github/workflows/` at workspace root applies to `projects/Bash/` and any subproject with matching workflows

- **Prompt Library**: All `.github/prompts/*.prompt.md` are the single source of truth — consumed by Copilot, OpenCode, and Hermes agents

- **Hermes Profile Routing**: code→architect, research→analyst, design→creative, planning→exec, teaching→tutor, ops→adminbot, general→default

- **MCP Tooling**: 16 MCP servers bridge file ops, GitHub, browser, search, linting, and containers

---

## 4. Critical Developer Workflows

### Workspace Root

```bash

# Python setup (workspace root)

cd C:/Users/Alexa/Desktop/SandBox
python -m venv venv
source venv/Scripts/activate  # or .venv/Scripts/activate
pip install -r requirements.txt

# Run root-level Python scripts (canonical location)

python C:/Users/Alexa/AppData/Local/hermes/scripts/health_check.py
python C:/Users/Alexa/AppData/Local/hermes/scripts/build_registry.py

# Bun/TypeScript (workspace root - minimal)

bun install
bun run index.ts

```

### Subproject Workflows

Each subproject has its own AGENTS.md with specific commands. See subproject AGENTS.md for details.

---

## 5. Codebase Patterns & Conventions

### File Naming

| Language | Convention | Example |
|----------|------------|---------|
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

# Canonical: C:/Users/Alexa/AppData/Local/hermes/scripts/

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

```

- **PR target branch**: `development` (not `main`)

---

## 6. MCP-First Tool Precedence

Before using native tools (terminal commands, direct file access), check MCP servers. The workspace has **16 active MCP servers** configured.

| Priority | MCP Server | Equivalent Native | Purpose |
|----------|------------|-------------------|---------|
| 1 | `filesystem` | `read_file`, `write_file`, `search_files`, `patch` | File read/write/stat/search ops |
| 2 | `github` | `gh` CLI | PR, issues, file contents, repos |
| 3 | `ast-grep` | `grep`/`rg` | AST-based code search and replace |
| 4 | `playwright` | `browser_*` tools | Browser automation for interactive pages |
| 5 | `fetch` | `curl` | HTTP web page content extraction |
| 6 | `sequential-thinking` | N/A | Structured multi-step reasoning |
| 7 | `code-sandbox` | `terminal` | Isolated Node.js sandbox for running code |
| 8 | `mcp-docker` | `docker` CLI | Container management + GitHub ops |
| 9 | `memory` | N/A | Persistent cross-session memory |
| 10 | `python-quality` | Manual | Ruff lint + Pyright typecheck on Python files |
| 11 | `tooling-lint` | Manual | ESLint, Prettier, markdownlint, cspell |
| 12 | `tooling-config` | Manual | pre-commit, git-cliff, .gitignore validation |

---

## 7. .github/prompts Library

The prompt library at `.github/prompts/` is the single source of truth for all prompt-family content.

### Structure

```

.github/prompts/
├── index.md                           # Library overview
├── *.prompt.md                        # Canonical prompts (190+)
├── templates/                         # Shared templates
├── .enhance/                          # Enhanced versions
└── archived/                          # Deprecated prompts

```

### Key Prompt Categories

| Category | Example Files | Purpose |
|----------|---------------|---------|
| Architecture | `architecture-blueprint-generator.prompt.md`, `folder-structure-blueprint-generator.prompt.md`, `technology-stack-blueprint-generator.prompt.md` | Generate architecture docs |
| Generator | `agents-generator.prompt.md`, `create-agentsmd.prompt.md`, `readme-blueprint-generator.prompt.md` | Generate agent guidance |
| Dev | `debug-issue.prompt.md`, `refactor-code.prompt.md`, `code-review.prompt.md` | Development workflows |
| Testing | `write-tests.prompt.md`, `playwright-generate-test.prompt.md`, `pytest-coverage.prompt.md` | Test generation |
| DevOps | `containerize-aspnetcore.prompt.md`, `multi-stage-dockerfile.prompt.md`, `terraform-azurerm-set-diff-analyzer.prompt.md` | Infrastructure |
| Planning | `create-implementation-plan.prompt.md`, `breakdown-plan.prompt.md`, `executing-plans.prompt.md` | Project planning |
| Content | `comprehensive-prompt-enhancer.prompt.md`, `convert-plaintext-to-md.prompt.md` | Content creation |

---

## 8. Hermes Agent Integration

### Profile Configuration

| Profile | Model / Guidance |
|---------|------------------|
| **default** ⬤ | Verify with `hermes profile list` / `hermes config show` |
| alexa | Verify with `hermes profile list` / `hermes config show` |
| code-architect | Verify with `hermes profile list` / `hermes config show` |
| creative-director | Verify with `hermes profile list` / `hermes config show` |
| exec-assistant | Verify with `hermes profile list` / `hermes config show` |
| patient-tutor | Verify with `hermes profile list` / `hermes config show` |
| research-analyst | Verify with `hermes profile list` / `hermes config show` |

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

---

## 9. Safety Rules

1. **Never commit secrets** — `.env`, tokens, credentials

2. **No destructive ops without approval** — explain risks first

3. **Verify before claim** — test, check, confirm before reporting

4. **MCP-first** — use MCP servers over native tools where available

5. **Profile per task** — switch profile before execution

6. **Strict sequential** — "only then" is a hard constraint
