# Copilot Instructions — SandBox Monorepo

**Canonical reference:** See `AGENTS.md` (general agent guidance), `.hermes.md` (Hermes-specific), `CLAUDE.md` (Claude-specific).

## Quick Start

```bash
# Root workspace setup
cd C:\Users\Alexa\Desktop\SandBox
bun install
python -m venv venv && source venv/Scripts/activate && pip install -r requirements.txt

# Root workspace validation (workspace-level code only)
bun run lint && bun run format:check && bun run typecheck

# For subproject work, see the project's own AGENTS.md and package.json scripts
```

## Architecture: Hermes-Centric Polyglot Monorepo

**SandBox** is a 17+ subproject monorepo with independent build systems, each under `projects/`. Every subproject is autonomous — it has its own `AGENTS.md`, `package.json`/`pyproject.toml`, `tsconfig.json`, and CI workflows.

### Key Pattern: Subproject Autonomy

- **Root workspace** lints only root-level code (config, scripts, top-level TypeScript/Python)
- **Subprojects** are excluded from root `tsconfig.json` and linting (`projects/` is in ignore lists)
- **Each subproject has its own**: AGENTS.md, build commands, test suite, CI workflow
- **Shared:** `.github/workflows/` (shared CI), `.github/prompts/` (canonical prompt library), tool configs (Prettier, ESLint flat config, Ruff, etc.)

When working on a subproject:
1. Read **that project's AGENTS.md** first (e.g., `projects/Bash/AGENTS.md`)
2. Use **that project's build/test commands** from `package.json` or `README.md`
3. Root-level workspace commands apply only to root-level changes

### Workspace Components

| Layer            | Examples                                                          | Purpose                                  |
| ---------------- | ----------------------------------------------------------------- | ---------------------------------------- |
| **Automation**   | `projects/Bash/`                                                  | Multi-phase orchestration (TS/PowerShell) |
| **Full-Stack**   | `projects/Banking/`, `projects/comicwise/`, `projects/ecom/`      | Next.js/Django apps with DB integration  |
| **Backend**      | `projects/Python-projects/`, `projects/profile/`, `projects/Resume_maker/` | Standalone services and utilities        |
| **MCP Servers**  | `projects/mcp-servers/`                                           | 10+ language implementations             |
| **Prompts**      | `.github/prompts/` (190+)                                         | Canonical prompt library                 |
| **Docs**         | `docs/`                                                           | Architecture, research, audits           |

## Technology Stack

### Runtimes & Package Managers

| Tech              | Version      | Used For                                           |
| ----------------- | ------------ | -------------------------------------------------- |
| **Bun**           | 1.3.14+      | TypeScript runtime & package manager (primary)     |
| **Python**        | 3.11 / 3.13  | Backend, automation, data processing               |
| **Node.js**       | 18 / 20      | Legacy JavaScript projects (not primary)           |
| **pnpm / npm**    | latest       | Specific projects (check their AGENTS.md)          |

### TypeScript Configuration

- **Root:** `tsconfig.json` with **strict mode enabled**
- **Key compiler options:** `noUncheckedIndexedAccess`, `verbatimModuleSyntax`, `noImplicitOverride`, `allowImportingTsExtensions`, `Preserve` modules
- **Line length:** 2-space indent (see `.editorconfig`)
- **No `any` type** without explicit justification
- **Module syntax:** Use `import type { X }` for types

### Python Configuration

- **Linter:** Ruff (Python 3.11)
- **Type checker:** Pyright
- **Line length:** 120 characters
- **Format:** Double quotes, LF line endings, space indent
- **Rules:** Select E, F, I, N, W, UP, B, SIM, ARG, RUF
- **PEP 668:** Virtual environment enforced (`venv/`)

### JavaScript/TypeScript Tooling

| Tool           | Config                | Usage                                    |
| -------------- | --------------------- | ---------------------------------------- |
| **ESLint**     | `eslint.config.mjs`   | Flat config; zero-warning gate           |
| **Prettier**   | `.prettierrc.json`    | Auto-format TS/JS/JSON/YAML              |
| **TypeScript** | `tsconfig.json`       | Strict mode, strict checking             |
| **Vitest**     | Via `bun run test`    | Unit testing (Bun projects)              |

### Python Tooling

| Tool       | Config        | Usage                                     |
| ---------- | ------------- | ----------------------------------------- |
| **Ruff**   | `.ruff.toml`  | Lint, format (faster than Black/Flake8)   |
| **Pyright** | `pyrightconfig.json` | Type checking (strict)                    |
| **pytest** | Via `pytest`  | Unit testing (Python projects)            |

### Markdown & Spell Check

- **Markdown linter:** `markdownlint-cli2` (`.markdownlintrc.json`) — line length 500
- **Spell check:** `cspell 10` (`cspell.json`)

## Build, Test, and Lint Commands

### Root Workspace (Top-Level Code Only)

```bash
# Install
bun install

# Format (Prettier)
bun run format
bun run format:check  # Dry-run

# Lint (ESLint)
bun run lint
bun run lint:fix

# Type check (TypeScript)
bun run typecheck

# All checks at once
bun run check  # lint + format:check + markdownlint + spellcheck

# Markdown linting
bun run markdownlint

# Spell check
bun run spellcheck
```

### Running Tests

Each subproject has its own test setup. Check the project's `package.json` or `AGENTS.md`:

```bash
# Examples (not comprehensive):
cd projects/Bash
bun run test                     # Vitest
bash tests/verify-dryrun.sh      # Shell tests

cd projects/ecom/backend
python manage.py test            # Django tests

cd projects/ecom/frontend
bun run test                      # Frontend tests
```

### Python Projects (Root Level)

```bash
# Activate venv first
source venv/Scripts/activate  # Windows: venv\Scripts\activate.bat

# Lint and format
ruff check .                  # Check all Python files
ruff format .                 # Auto-format
ruff check --fix .            # Fix issues automatically

# Type check
pyright .

# Run tests
pytest                        # All tests
pytest path/to/test_file.py   # Single file
pytest -k test_name           # Single test by name
```

## Key Conventions

### File Naming

| Language     | Convention                                               | Example                                         |
| ------------ | -------------------------------------------------------- | ----------------------------------------------- |
| TypeScript   | `kebab-case.ts` (scripts), `PascalCase.tsx` (components) | `cache-clean.ts`, `UserProfile.tsx`             |
| Python       | `snake_case.py` (PEP 8)                                  | `health_check.py`, `audit_prompts.py`           |
| PowerShell   | `PascalCase.ps1`                                         | `Orchestrator-Unified.ps1`                      |
| Bash/Shell   | `kebab-case.sh`                                          | `test-all.sh`, `cache-clean.sh`                 |
| Markdown     | `kebab-case.md`                                          | `copilot-instructions.md`, `health-check.md`    |

### Git Workflow & Commit Convention

**Branch naming:**
```
<type>/<project>/<kebab-case-description>
feat/resume-maker/add-html-output
fix/bash/install-script-permissions
docs/root/update-readme
```

**Types:** `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`  
**Project:** Subproject name (e.g., `banking`, `ecom`) or `root` for workspace changes  
**Target branch:** All PRs merge to `development` (not `main`)

**Commit message format:**
```
feat: add HTML output option
fix: handle empty resume data gracefully
docs: update README with new flags
```

**Best practices:**
- One concern per PR (don't mix feat + refactor)
- Scope to the project (keep changes focused)
- Keep <300 lines changed
- Rebase before pushing (no merge commits)

### Code Style & Standards

**TypeScript:**
- 2-space indent (tabs configured, but 2-space size)
- Strict mode always enabled
- No `any` without explicit comment
- Use `import type { X }` for type imports
- Final newlines, CRLF line endings on Windows

**Python:**
- 4-space indent (PEP 8)
- Double quotes
- Type hints on all functions
- Docstrings for public APIs

**Destructive Operations:**
- All destructive scripts must support `--help` and `--dry-run`
- Always run dry-run first to preview changes
- No `.bak` or `.backup` files — use git for rollback
- Logs go to `logs/` with timestamps

### Multi-Wrapper Parity

Automation scripts that run cross-platform must have three implementations:

```
scripts/operation.sh     # Bash (Linux/WSL/Git Bash)
scripts/Operation.ps1    # PowerShell (Windows)
scripts/operation.bat    # Batch (Windows fallback)
```

All must produce identical output and support the same flags.

## Project Structure Quick Reference

```
SandBox/
├── AGENTS.md              # Canonical agent guidance (START HERE)
├── .hermes.md             # Hermes-specific overrides
├── .github/
│   ├── copilot-instructions.md  # This file
│   ├── prompts/           # 190+ canonical prompts
│   └── workflows/         # Shared CI workflows
├── projects/
│   ├── Bash/              # Automation toolkit (TS/PS1/Bash)
│   ├── Banking/           # Next.js fintech
│   ├── comicwise/         # Next.js comics
│   ├── ecom/              # Django + React
│   ├── mcp-servers/       # Multi-language MCP implementations
│   ├── Python-projects/   # Standalone scripts
│   └── ...                # 10+ additional subprojects
├── docs/                  # Architecture, research, audits
├── scripts/               # Pointer — canonical scripts at ~/AppData/Local/hermes/scripts/
├── .vscode/               # Workspace settings (Prettier, Ruff, etc.)
├── venv/                  # Python 3.11 virtualenv
├── node_modules/          # Bun/Node dependencies
└── *.config.{ts,mjs,json,toml,yaml}  # Root config files
```

## Subproject-Specific Guidance

### Bash — Automation Toolkit (`projects/Bash/`)

**Purpose:** Multi-phase orchestration pipeline (Discovery → Clone → Triage → Debug → Remediation → Cross-Reference)

**Commands:**
```bash
cd projects/Bash
bun install --frozen-lockfile
bun run format && bun run typecheck && bun run lint:strict
bash tests/verify-dryrun.sh && bash test-all.sh
powershell -File orchestrator-unified.ps1 -Mode discover
```

**Key patterns:**
- Orchestrator modes: `discover`, `clone`, `triage`, `debug`, `remediation`, `cross-ref`
- All destructive operations support `--dry-run` and `--help`
- Multi-wrapper parity: `.sh`, `.ps1`, `.bat` implementations
- Logs to `logs/` with timestamps (no `.bak` backups)
- TypeScript strict mode; Vitest for tests; Bash for shell tests

**Single test:**
```bash
cd projects/Bash
bun run test -- src/path/to/test.ts  # Vitest single file
bash tests/verify-dryrun.sh           # Shell test verification
```

### Banking — Fintech App (`projects/Banking/`)

**Purpose:** Next.js fintech dashboard with Plaid/Dwolla integrations and Drizzle ORM

**Commands:**
```bash
cd projects/Banking
bun install --frozen-lockfile
bun run dev              # Dev server (:3000)
bun run build            # Production build
bun run db:generate      # Drizzle schema → migrations
bun run db:push          # Push migrations to PostgreSQL
bun run db:studio        # Visual database editor
bun run lint:strict      # ESLint with zero warnings
bun run type-check       # TypeScript check
bun run test             # Vitest unit tests
```

**Key patterns:**
- Next.js 16 App Router + Server Actions
- Drizzle ORM schema in `src/db/schema.ts` (no raw SQL)
- Auth via `auth()` first in protected actions
- Zod validation before database writes
- Plaid sandbox mode for development
- Webhooks for Plaid/Dwolla async events
- `.env.local` for secrets (never commit)

**Single test:**
```bash
cd projects/Banking
bun run test -- src/path/to/test.ts  # Run one test file
bun run test -- --reporter=verbose   # Verbose output
```

### Comicwise — Comic Streaming (`projects/comicwise/`)

**Purpose:** Next.js comic storefront with Prisma ORM and Stripe subscriptions

**Commands:**
```bash
cd projects/comicwise
pnpm install                 # Uses pnpm, not bun
pnpm dev                     # Dev server (:3000)
pnpm build                   # Production build
bunx prisma generate         # Generate Prisma client
bunx prisma db push          # Push schema to PostgreSQL
bunx prisma studio           # Visual database editor
pnpm lint:strict             # ESLint with zero warnings
pnpm type-check              # TypeScript check
pnpm test                    # Vitest unit tests (260+ passing)
pnpm test:ui                 # Playwright E2E tests
```

**Key patterns:**
- Next.js 15 App Router + Server Components
- Prisma ORM for schema + migrations
- Stripe webhooks for subscription lifecycle
- NextAuth.js for authentication
- React Compiler enabled (no manual memoization)
- Turbopack bundler (~24s builds)
- TypeScript strict + zero warnings enforced
- `.env.local` for database URL + Stripe keys

**Single test:**
```bash
cd projects/comicwise
pnpm test -- src/path/to/test.ts     # Vitest single file
pnpm test -- --reporter=verbose      # Verbose output
pnpm test:ui -- --headed             # Playwright with browser visible
```

**Pre-commit quality gate:**
```bash
cd projects/comicwise
pnpm lint:strict && pnpm triage && pnpm type-check && pnpm test && pnpm build
```

### Ecom — Django + React (`projects/ecom/`)

**Purpose:** Dual-stack ecommerce platform (Django REST backend + React/Redux frontend)

**Commands (Backend):**
```bash
cd projects/ecom/backend
pip install -r requirements.txt
python manage.py migrate
python manage.py makemigrations
python manage.py runserver      # Dev server (:8000)
python manage.py test           # Django test runner
python manage.py createsuperuser # Admin access
```

**Commands (Frontend):**
```bash
cd projects/ecom/frontend
bun install
bun run start                    # Dev server (:3000)
bun run test                     # Jest unit tests
bun run build                    # Production build
```

**Key patterns:**
- **Dual dev servers:** Backend `:8000` + Frontend `:3000` (proxied in dev)
- Django REST Framework with API routes at `/api/v1/`
- React + Redux Toolkit for state management
- PayPal integration for checkout
- PEP 8 for Python; Prettier for JavaScript
- `.env` for secrets (never commit)
- Backend tests in `backend/tests/`; frontend in `frontend/__tests__/`

**Single test:**
```bash
# Backend
cd projects/ecom/backend
python manage.py test path.to.TestClass  # Django single test
python -m pytest tests/test_file.py -v   # pytest single file

# Frontend
cd projects/ecom/frontend
bun run test -- src/path/to/test.ts      # Jest single file
```

---

## Common Tasks

### Add a New Feature to a Subproject

1. Read the **subproject's AGENTS.md** (e.g., `projects/Bash/AGENTS.md`)
2. Create a branch: `git checkout -b feat/<project>/<description>`
3. Follow the subproject's build/test commands (see [Subproject-Specific Guidance](#subproject-specific-guidance))
4. Commit with conventional format: `feat: <description>`
5. PR to `development` branch

### Update Root Workspace Config

1. Make changes (e.g., `package.json`, `tsconfig.json`, `.ruff.toml`)
2. Branch: `git checkout -b chore/root/<description>`
3. Run: `bun run check` (root validation)
4. Commit: `chore: <description>`
5. PR to `development`

### Debug a Test Failure

For TypeScript (Bash, Banking, comicwise):
```bash
cd projects/<name>
bun run test -- path/to/test.ts  # Run one test file
bun run test -- --reporter=verbose  # Verbose output
```

For Python (ecom backend):
```bash
cd projects/ecom/backend
python -m pytest tests/test_file.py -v  # Verbose output
python -m pytest tests/test_file.py::TestClass::test_name -v  # Single test
```

For React (ecom frontend):
```bash
cd projects/ecom/frontend
bun run test -- src/path/to/test.ts  # Jest single file
```

### Add a New Dependency

**TypeScript project (Bash, Banking):**
```bash
cd projects/<name>
bun add package-name
bun add --dev package-name
```

**TypeScript project (comicwise with pnpm):**
```bash
cd projects/comicwise
pnpm add package-name
pnpm add --save-dev package-name
```

**Python (ecom backend):**
```bash
cd projects/ecom/backend
pip install package-name
pip freeze > requirements.txt  # Update requirements
```

**React (ecom frontend):**
```bash
cd projects/ecom/frontend
bun add package-name
bun add --dev package-name
```

## MCP Server Configuration

This workspace includes 14 pre-configured MCP servers (in `.mcp.json`). They enhance Copilot with specialized capabilities. Key servers for this repository:

### Currently Configured (14 servers)

| Server             | Type   | Purpose                                    | Use Case                               |
| ------------------ | ------ | ------------------------------------------ | -------------------------------------- |
| **filesystem**     | Local  | File operations (read/write/search)        | Project exploration, editing           |
| **github**         | Local  | GitHub API, PR/issue operations            | Automation, releases, collaboration    |
| **ast-grep**       | Local  | AST-based code search & replace            | Refactoring, pattern matching          |
| **code-sandbox**   | Local  | Node.js jest sandbox                       | Testing, code execution                |
| **playwright**     | Local  | Browser automation                         | E2E testing (comicwise, ecom frontend) |
| **sequential-thinking** | Local | Multi-step reasoning                       | Complex problem solving                |
| **context7**       | HTTP   | Documentation for libraries & frameworks   | API lookup (Next.js, Prisma, Django)   |
| **fetch**          | Local  | Web content extraction                     | Research, external data                |
| **memory**         | Local  | Persistent cross-session memory            | Session tracking, preferences          |
| **neon**           | HTTP   | PostgreSQL database management (Neon)      | Database queries, schema inspection    |
| **sentry**         | HTTP   | Error tracking (Sentry)                    | Debugging, error investigation         |
| **smithery**       | HTTP   | MCP registry & discovery                   | Finding new tools/integrations         |
| **tavily**         | HTTP   | Web search                                 | Research, information gathering        |
| **mcp-docker**     | Docker | Container management + GitHub ops          | Docker Compose, deployment             |

### Recommended Additional Servers (Not Yet Configured)

**For comicwise/Banking (Database-heavy):**
- **postgres-mcp** — Direct PostgreSQL queries (Neon + Drizzle/Prisma)
  ```json
  {
    "postgres": {
      "command": "npx",
      "args": ["-y", "postgres-mcp", "--connection", "${env:DATABASE_URL}"]
    }
  }
  ```

**For Django projects (ecom):**
- **django-mcp** — Django management commands, ORM helpers
  ```json
  {
    "django": {
      "command": "python",
      "args": ["manage.py", "shell_plus", "--kernel", "mcp"]
    }
  }
  ```

**For Testing (All projects):**
- **pytest-mcp** — Python test automation
  ```json
  {
    "pytest": {
      "command": "npx",
      "args": ["-y", "pytest-mcp"]
    }
  }
  ```

**For Documentation:**
- **docs-mcp** — Local documentation search
  ```json
  {
    "docs": {
      "command": "npx",
      "args": ["-y", "docs-mcp", "docs/"]
    }
  }
  ```

### How to Add an MCP Server

1. **Edit `.mcp.json`** at workspace root
2. **Add server definition** (example for context7):
   ```json
   "context7": {
     "type": "http",
     "url": "https://mcp.context7.com/mcp"
   }
   ```
3. **Restart Copilot** or refresh MCP connections
4. **Verify:** `gh copilot mcp list` (if using GitHub CLI)

### MCP Server Best Practices

- **Use filesystem for local operations** — faster than git operations
- **Use github for PR/issue workflows** — official GitHub API
- **Use context7 for library docs** — always get current versions
- **Use playwright for E2E testing** — especially comicwise/ecom frontend
- **Use sequential-thinking for complex tasks** — multi-step debugging, planning
- **Never expose secrets** — use `${env:VARIABLE}` for tokens

---



1. **Subproject Exclusions:** Root linting ignores `projects/` — subprojects lint themselves
2. **Dual Python Installs:** `python` = 3.11 (venv), `python3` = 3.13 (system). Always activate venv.
3. **Bun + Windows Paths:** Prefer absolute Windows paths (`C:\...`) over MSYS paths (`/c/...`)
4. **Pre-commit:** Hooks run on `git commit` — skip with `SKIP=hook-name git commit`
5. **CI Workflows:** `.github/workflows/` are shared; per-project workflows in subprojects if needed

## Helpful Resources

- **Full Architecture:** `AGENTS.md` (sections 1–13)
- **Hermes Config:** `.hermes.md` (profiles, MCP servers, plugins)
- **Subproject Guidance:** Each project's `AGENTS.md` (e.g., `projects/Bash/AGENTS.md`)
- **Branching/Contributing:** `CONTRIBUTING.md`
- **Prompt Library:** `.github/prompts/` (190+ templates)
- **Architecture Docs:** `docs/Project_Architecture/`
- **MCP Configuration:** `.mcp.json` (14 servers, add more as needed)

---

## When to Reference What

| Question                                    | File to Check                      | Section                          |
| ------------------------------------------- | ---------------------------------- | -------------------------------- |
| "What's the Bash project structure?"        | `projects/Bash/AGENTS.md`          | Architecture, Stack, Commands    |
| "How do I test in Banking?"                 | `projects/Banking/AGENTS.md`       | Commands (test examples)         |
| "What's comicwise's package manager?"       | `projects/comicwise/AGENTS.md`     | Stack (pnpm, not bun)            |
| "How do I run ecom locally?"                | `projects/ecom/AGENTS.md`          | Commands (dual servers)          |
| "What CI workflows exist?"                  | `.github/workflows/`               | Per-project `.yml` files         |
| "How do I commit changes?"                  | `CONTRIBUTING.md`                  | Branch naming, commit format     |
| "What's the workspace architecture?"        | `AGENTS.md`                        | Section 3: Architecture Overview |
| "Which MCP servers are available?"          | `.mcp.json`                        | Server definitions               |
| "How do I configure VS Code?"               | `.vscode/`                         | `settings.json`, `extensions.json` |
| "What Python tooling is available?"         | `AGENTS.md`                        | Section 2: Python Toolchain      |

---

## Adjustments Made to This Guide

✅ **Added subproject-specific examples** for Bash, Banking, comicwise, and ecom with:
  - Project-specific commands for dev, build, test, database operations
  - Key architectural patterns and conventions for each project
  - Single test examples (not just full test suite)
  - Package manager differences (Bash/Banking: bun, comicwise: pnpm, ecom: dual)

✅ **Added MCP Server configuration** with:
  - Currently configured 14 servers and their purposes
  - Recommended additional servers for database, Django, testing, docs
  - JSON examples for adding new servers
  - Best practices for using MCP servers

✅ **Enhanced "Common Tasks"** section with:
  - Subproject-specific commands for debugging, adding dependencies
  - Backend/frontend separation for ecom
  - Quality gates for comicwise pre-commit

✅ **Added reference table** for when to check specific files/sections

---

## Quick Command Reference by Project

```bash
# Bash (TypeScript + Shell)
cd projects/Bash && bun install && bun run lint:strict && bash test-all.sh

# Banking (Next.js + Drizzle)
cd projects/Banking && bun install && bun run dev && bun run db:studio

# Comicwise (Next.js + Prisma, uses pnpm)
cd projects/comicwise && pnpm install && pnpm dev && pnpm db:studio

# Ecom (Django + React, dual servers)
cd projects/ecom/backend && pip install -r requirements.txt && python manage.py runserver &
cd projects/ecom/frontend && bun install && bun run start
```
