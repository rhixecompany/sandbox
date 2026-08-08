# SandBox — AGENTS.md

Canonical agent guidance. First file agents should read. Other instruction files are thin stubs that defer here.

> Verified 2026-07-28. No aspirational practices.

---

## 1. Directory Map

```
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
├── scripts/                 # Pointer README — canonical scripts live in ~/AppData/Local/hermes/scripts/
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

| Layer                    | Technology                             | Notes                                                                                      |
| ------------------------ | -------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Runtime (TS)**         | Bun 1.3.14+                            | Runtime + package manager + test runner. DO NOT use npm/pnpm unless project says otherwise |
| **Runtime (Python)**     | Python 3.11 / 3.13                     | Dual install: python3=3.13.14, python=3.11.15 (venv). PEP 668 enforced                     |
| **Python Package Mgr**   | pip + uv                               | Requirements in `requirements.txt`. Prefer uv for speed                                    |
| **TypeScript**           | ESNext target, strict mode             | `tsconfig.json` — `noUncheckedIndexedAccess`, `verbatimModuleSyntax`, `Preserve` modules   |
| **Python Quality**       | Ruff + Pyright                         | Ruff for lint/format (select E,F,I,N,W,UP,B), Pyright for typecheck                        |
| **JS Linting**           | ESLint 10 flat config                  | `eslint.config.mts` — zero-warning gate (`--max-warnings=0`)                               |
| **Formatter**            | Prettier 3                             | `.prettierrc.json` / `.prettierrc.ts`                                                      |
| **Markdown**             | markdownlint-cli2                      | `.markdownlintrc.json` — MD013 line_length=500, fenced backtick style                      |
| **Spell Check**          | cspell 10                              | `cspell.json`                                                                              |
| **Testing (TS)**         | Vitest                                 | `bun run test` or `vitest run`                                                             |
| **Testing (Python)**     | pytest 9                               | `pytest` with `pytest-asyncio`                                                             |
| **Browser Testing**      | Playwright                             | `.github/prompts/playwright-*.prompt.md` patterns                                          |
| **Pre-commit**           | pre-commit 4.6                         | `.pre-commit-config.yaml`                                                                  |
| **Changelog**            | git-cliff 2.13                         | `cliff.toml`                                                                               |
| **EditorConfig**         | `.editorconfig`                        | indent_style=tab, indent_size=2, end_of_line=crlf, charset=utf-8                           |
| **DB ORM (TS projects)** | Drizzle (Banking) / Prisma (comicwise) | Schema in `src/db/schema.ts` or `prisma/schema.prisma`                                     |
| **DB ORM (Python)**      | Django ORM (ecom)                      | Migrations via `manage.py makemigrations`                                                  |
| **CI/CD**                | GitHub Actions                         | `.github/workflows/` shared across workspace                                               |
| **Infra**                | Docker Compose                         | For multi-container apps (Banking, ecom, comicwise)                                        |

### Python Toolchain Detail

```bash
python3 --version      # 3.13.14 (system)
python --version       # 3.11.15 (venv)
pip --version          # 3.11.15 venv
uv --version           # Fast pip alternative
ruff check .           # Lint all Python
ruff format .          # Format all Python
pyright .              # Type check
pytest                 # Run tests
```

---

## 3. Architecture Overview

### Workspace Pattern: Hermes-Centric Monorepo

The SandBox is a multi-language monorepo workspace tightly integrated with **Hermes Agent** (built on GitHub Copilot / OpenCode). Every subproject under `projects/` is autonomous — each has its own `AGENTS.md`, `package.json`, `README.md`, and build system. The workspace root provides shared config, tooling, and prompt libraries.

### Key Components

| Component             | Path                              | Stack                                                                   | Purpose                                                                                                   |
| --------------------- | --------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Bash Toolkit**      | `projects/Bash/`                  | Bun/TS + PowerShell + Bash                                              | Multi-phase automation pipeline (discover → clone → triage → debug → remediation → cross-ref)             |
| **Banking App**       | `projects/Banking/`               | Next.js 16, Drizzle ORM, Plaid, Dwolla                                  | Full-stack fintech dashboard with transaction management                                                  |
| **Comicwise**         | `projects/comicwise/`             | Next.js 15, Prisma, Stripe                                              | Digital comic storefront with subscription management                                                     |
| **Ecom**              | `projects/ecom/`                  | Django REST + React/Redux, PayPal                                       | Dual-stack ecommerce platform                                                                             |
| **MCP Servers**       | `projects/mcp-servers/`           | 10 languages (TS, Python, Go, Rust, Java, Kotlin, PHP, Ruby, Swift, C#) | Reference MCP server implementations                                                                      |
| **Python Scripts**    | `projects/Python-projects/`       | Python 3.x                                                              | 18 standalone beginner-to-intermediate scripts                                                            |
| **Prompt Library**    | `.github/prompts/`                | Markdown + YAML frontmatter                                             | 190+ canonical prompt templates                                                                           |
| **Workspace Scripts** | `~/AppData/Local/hermes/scripts/` | Python                                                                  | 100+ automation scripts for Hermes maintenance, audits, tooling (canonical; repo `scripts/` is a pointer) |
| **Documentation**     | `docs/`                           | Markdown                                                                | Architecture blueprints, audits, references, research                                                     |

### Cross-Component Communication

- **Shared CI**: `.github/workflows/` at workspace root applies to `projects/Bash/` and any subproject with matching workflows
- **Prompt Library**: All `.github/prompts/*.prompt.md` are the single source of truth — consumed by Copilot, OpenCode, and Hermes agents
- **Hermes Profile Routing**:
  - Code/debug/refactor → `code-architect` profile
  - Research/synthesis → `research-analyst` profile
  - Design/content → `creative-director` profile
  - Planning/admin → `exec-assistant` profile
  - Tutorials → `patient-tutor` profile
  - DevOps/infra → `alexa` profile
  - General → `default` profile (deepseek-v4-flash-free / opencode-zen)
- **MCP Tooling**: 16 MCP servers bridge file ops, GitHub, browser, search, linting, and containers

### Data Flow Patterns

| Pattern               | Example                     | Description                                                                            |
| --------------------- | --------------------------- | -------------------------------------------------------------------------------------- |
| **Phase Pipeline**    | `projects/Bash/`            | Sequential 6-phase: Discovery → Clone → Triage → Debug → Remediation → Cross-Reference |
| **Full-Stack API**    | `projects/Banking/`         | Next.js App Router → Drizzle ORM → PostgreSQL; Plaid/Dwolla webhooks                   |
| **Dual-Stack**        | `projects/ecom/`            | Django REST API (`:8000`) + React frontend (`:3000`) proxied in dev                    |
| **Subscription**      | `projects/comicwise/`       | Next.js → Prisma → PostgreSQL; Stripe recurring payments via webhooks                  |
| **Standalone Script** | `projects/Python-projects/` | Single-file, no framework, shared `requirements.txt`                                   |

---

## 4. Subproject Directory

Each subproject is self-contained with its own `AGENTS.md`. Brief reference:

| Project                         | Type                | Entry Point                                | Test Command                            |
| ------------------------------- | ------------------- | ------------------------------------------ | --------------------------------------- |
| `Bash/`                         | TS automation       | `src/` scripts, `orchestrator-unified.ps1` | `bun run test`, `bash test-all.sh`      |
| `Banking/`                      | Next.js fintech     | `src/app/` App Router                      | `bun run test`                          |
| `comicwise/`                    | Next.js comics      | `src/app/` App Router                      | `bun run test`                          |
| `ecom/`                         | Django + React      | `backend/manage.py`, `frontend/`           | `python manage.py test`, `bun run test` |
| `mcp-servers/`                  | Multi-language MCP  | Per-language subdirectory                  | Per-language build system               |
| `Python-projects/`              | Python scripts      | Standalone `.py` files                     | Manual (`ruff check`, `mypy`)           |
| `cookiecutter-django-tailwind/` | Django template     | Cookiecutter scaffold                      | Follow project README                   |
| `Django-Scrapy-Selenium/`       | Scrapy/Selenium     | Per-usage                                  | Per-usage                               |
| `Resume_maker/`                 | TS resume gen       | `src/`                                     | `bun run test`                          |
| `rhixe_scans/`                  | TBD                 | Check project README                       | Check project README                    |
| `rhixecompany-comics/`          | TBD                 | Check project README                       | Check project README                    |
| `selenium_webdriver/`           | Selenium automation | Standalone                                 | Manual                                  |
| `university-libary-jsm/`        | Library system      | Check project README                       | Check project README                    |
| `xamehi/`, `xamehi.tv/`         | Media projects      | Check project README                       | Check project README                    |
| `youtube-downloader/`           | YouTube tool        | Check project README                       | Check project README                    |
| `profile/`                      | Profile config      | Check project README                       | Check project README                    |
| `docs/`                         | Documentation       | Markdown files                             | N/A                                     |

---

## 5. Critical Developer Workflows

### Workspace Root

```bash
# Python setup (workspace root)
cd C:\Users\Alexa\Desktop\SandBox
python -m venv venv
source venv/Scripts/activate  # or .venv/Scripts/activate
pip install -r requirements.txt

# Run root-level Python scripts (canonical location)
python ~/AppData/Local/hermes/scripts/health_check.py
python ~/AppData/Local/hermes/scripts/build_registry.py

# Bun/TypeScript (workspace root - minimal)
bun install
bun run index.ts
```

### Bash Project (Primary Automation Toolkit)

```bash
cd projects/Bash

# Install
bun install --frozen-lockfile || bun install

# Full validation gate
bun run format        # Prettier format
bun run typecheck     # tsc --noEmit
bun run lint:strict   # ESLint --max-warnings=0
bun run test          # Vitest

# Shell validation
bash tests/verify-dryrun.sh
bash test-all.sh

# Orchestrator modes
powershell -File orchestrator-unified.ps1 -Mode discover
powershell -File orchestrator-unified.ps1 -Mode clone
powershell -File orchestrator-unified.ps1 -Mode triage
powershell -File orchestrator-unified.ps1 -Mode debug
powershell -File orchestrator-unified.ps1 -Mode remediation
powershell -File orchestrator-unified.ps1 -Mode cross-ref

# Cache cleaning (dry-run first)
bun run clean:cache:dry   # Preview
bun run clean:cache       # Execute

# Dependency cleaning (dry-run first)
bun run clean:deps:dry    # Preview
bun run clean:deps        # Execute

# Lint formatting
bun run format:markdown:check  # Markdown lint
bun run format:markdown:fix    # Auto-fix markdown
bun run lint                   # ESLint
bun run lint:fix               # ESLint auto-fix
```

### Banking Project

```bash
cd projects/Banking

bun run dev        # Next.js dev server
bun run build      # Production build
bun run lint       # ESLint
bun run db:generate  # Drizzle schema → migrations
bun run db:push      # Push migrations to DB
bun run db:studio    # Drizzle Studio (GUI)
```

### Comicwise Project

```bash
cd projects/comicwise

bun run dev              # Next.js dev server
bun run build            # Production build
bun run lint             # ESLint
bunx prisma generate      # Prisma client
bunx prisma db push       # Push schema
bunx prisma studio        # Prisma Studio (GUI)
```

### Ecom Project (Dual-Stack)

```bash
# Backend
cd projects/ecom/backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver    # :8000
python manage.py test         # Backend tests

# Frontend
cd projects/ecom/frontend
bun install
bun run start                     # :3000
bun run test                      # Frontend tests
```

### Python Projects

```bash
cd projects/Python-projects
pip install -r requirements.txt
ruff check .                    # Lint all Python scripts
ruff format .                   # Format all Python scripts
python basic_calculator.py      # Run any script directly
```

### MCP Servers

```bash
cd projects/mcp-servers

# Each language subdirectory is self-contained
cd python
pip install -r requirements.txt
python server.py

cd typescript
bun install
bun run src/server.ts
```

---

## 6. Codebase Patterns & Conventions

### File Naming

| Language     | Convention                                               | Example                                         |
| ------------ | -------------------------------------------------------- | ----------------------------------------------- |
| TypeScript   | `kebab-case.ts` (scripts), `PascalCase.tsx` (components) | `cache-clean.ts`, `UserProfile.tsx`             |
| Python       | `snake_case.py` (PEP 8)                                  | `health_check.py`, `audit_prompts.py`           |
| PowerShell   | `PascalCase.ps1`                                         | `Orchestrator-Unified.ps1`, `Disk-Analysis.ps1` |
| Shell (Bash) | `kebab-case.sh`                                          | `test-all.sh`, `cache-clean.sh`                 |
| Batch        | `kebab-case.bat`                                         | `cache-clean.bat`, `upgrade.bat`                |
| Markdown     | `kebab-case.md`                                          | `health-check.md`, `research-report.md`         |

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

### TypeScript Strict Mode

```jsonc
// tsconfig.json — root
{
	"compilerOptions": {
		"strict": true,
		"noUncheckedIndexedAccess": true, // Must check array/object access
		"noImplicitOverride": true, // Must use `override` keyword
		"verbatimModuleSyntax": true, // import type { X } syntax
		"moduleDetection": "force",
		"noFallthroughCasesInSwitch": true,
		"allowImportingTsExtensions": true, // Use .ts extension in imports
	},
}
```

### Python Quality Gate

```bash
# Full Python quality check
ruff check .          # Lint (E,F,I,N,W,UP,B rulesets)
ruff format --check . # Format check
pyright .             # Type check
pytest                # Unit tests
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

### Logging Convention

- Logs stored in `logs/action_YYYYMMDD_HHMMSS.log`
- No secrets or sensitive data in logs
- Timestamped filenames for traceability

---

## 7. MCP-First Tool Precedence

Before using native tools (terminal commands, direct file access), check MCP servers. The workspace has **16 active MCP servers** configured:

| Priority | MCP Server            | Equivalent Native                                  | Purpose                                                 |
| -------- | --------------------- | -------------------------------------------------- | ------------------------------------------------------- |
| 1        | `filesystem`          | `read_file`, `write_file`, `search_files`, `patch` | File read/write/stat/search ops                         |
| 2        | `github`              | `gh` CLI                                           | PR, issues, file contents, repos                        |
| 3        | `ast-grep`            | `grep`/`rg`                                        | AST-based code search and replace                       |
| 4        | `playwright`          | `browser_*` tools                                  | Browser automation for interactive pages                |
| 5        | `fetch`               | `curl`                                             | HTTP web page content extraction                        |
| 6        | `sequential-thinking` | N/A                                                | Structured multi-step reasoning                         |
| 7        | `code-sandbox`        | `terminal`                                         | Isolated Node.js sandbox for running code               |
| 8        | `mcp-docker`          | `docker` CLI                                       | Container management + GitHub ops                       |
| 9        | `memory`              | N/A                                                | Persistent cross-session memory                         |
| 10       | `python-quality`      | Manual                                             | Ruff lint + Pyright typecheck on Python files           |
| 11       | `tooling-lint`        | Manual                                             | ESLint, Prettier, markdownlint, cspell                  |
| 12       | `tooling-config`      | Manual                                             | pre-commit, git-cliff, .gitignore validation            |
| 13       | `copilot-mcp`         | Copilot CLI                                        | Copilot provider operations                             |
| 14       | `mindstudio`          | N/A                                                | Third-party integrations (Gmail, Google, Slack, Notion) |
| 15       | `smithery`            | N/A                                                | MCP registry and discovery                              |
| 16       | `linear`              | `linear` CLI                                       | Project management                                      |

### When to Use Native Tools Instead

- **Terminal**: `bun`, `pip`, `npm`, `git`, `docker`, `ruff`, `pyright` — anything that launches a process
- **Build/Test commands**: always use terminal
- **Network fetch on plain-text URLs** (`.md`, `.json`, `.yaml`): prefer `curl` via terminal or `web_extract` over browser
- **Large-scale batch file ops**: `search_files` + `patch` (native) vs `filesystem` MCP

---

## 8. .github/prompts Library

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

| Category         | Example Files                                                                                                                                    | Purpose                    |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| **Architecture** | `architecture-blueprint-generator.prompt.md`, `folder-structure-blueprint-generator.prompt.md`, `technology-stack-blueprint-generator.prompt.md` | Generate architecture docs |
| **Generator**    | `agents-generator.prompt.md`, `create-agentsmd.prompt.md`, `readme-blueprint-generator.prompt.md`                                                | Generate agent guidance    |
| **Dev**          | `debug-issue.prompt.md`, `refactor-code.prompt.md`, `code-review.prompt.md`                                                                      | Development workflows      |
| **Testing**      | `write-tests.prompt.md`, `playwright-generate-test.prompt.md`, `pytest-coverage.prompt.md`                                                       | Test generation            |
| **DevOps**       | `containerize-aspnetcore.prompt.md`, `multi-stage-dockerfile.prompt.md`, `terraform-azurerm-set-diff-analyzer.prompt.md`                         | Infrastructure             |
| **Planning**     | `create-implementation-plan.prompt.md`, `breakdown-plan.prompt.md`, `executing-plans.prompt.md`                                                  | Project planning           |
| **Content**      | `comprehensive-prompt-enhancer.prompt.md`, `convert-plaintext-to-md.prompt.md`                                                                   | Content creation           |
| **OpenCode**     | `opencode.json`, `~\.opencode\`                                                                                                                  | OpenCode configuration     |

### Rules for Prompt Files

1. All prompts have YAML frontmatter with `name`, `title`, `description`, `version`, `tags`, `trigger`
2. Templates in `templates/` are imported by reference — never duplicate shared content
3. When updating a prompt, update its cross-references in `index.md`
4. Dedupe exact duplicate bodies — keep one canonical copy, cross-link
5. New prompts go to `.github/prompts/` — never to legacy locations (`.github/agents/`, `.github/instructions/`, root `prompts/`)

---

## 9. Hermes Agent Integration

### Profile Configuration

| Profile           | Model                      | Provider     | Use Case                     |
| ----------------- | -------------------------- | ------------ | ---------------------------- |
| default           | deepseek-v4-flash-free     | opencode-zen | General purpose              |
| alexa             | google/gemma-4-31b-it:free | openrouter   | Operations/DevOps            |
| code-architect    | google/gemma-4-31b-it:free | openrouter   | Code, debugging, refactoring |
| creative-director | google/gemma-4-31b-it:free | openrouter   | Design, content creation     |
| exec-assistant    | google/gemma-4-31b-it:free | openrouter   | Planning, administration     |
| patient-tutor     | google/gemma-4-31b-it:free | openrouter   | Tutorials, explanations      |
| research-analyst  | google/gemma-4-31b-it:free | openrouter   | Research, synthesis          |

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

| #   | File               | Purpose                   | Authority                     |
| --- | ------------------ | ------------------------- | ----------------------------- |
| 1   | `.hermes.md`       | Hermes-specific overrides | Highest — overrides all below |
| 2   | `AGENTS.md`        | General agent guidance    | This file                     |
| 3   | `PROJECT_RULES.md` | Workspace-level rules     | Rules                         |
| 4   | `MASTER_RULES.md`  | Universal agent rules     | Cross-project rules           |
| 5   | `CLAUDE.md`        | Claude-specific behavior  | Copilot/Claude only           |
| 6   | `.cursorrules`     | Cursor IDE rules          | Cursor IDE only               |

### Available Hermes Toolsets (16)

`web`, `browser`, `terminal`, `file`, `code_execution`, `vision`, `image_gen`, `tts`, `skills`, `todo`, `memory`, `context_engine`, `session_search`, `clarify`, `delegation`, `cronjob`

### Active Hooks (3)

`session-logger` | `session-auto-commit` | `governance-audit`

### Active Plugins (15)

`basic`, `custom-provider`, `disk-cleanup`, `huggingface-provider`, `langfuse`, `nous`, `nous-provider`, `ollama-cloud-provider`, `openai-codex`, `openai-codex-provider`, `opencode-zen-provider`, `openrouter-provider`, `security-guidance`, `web-tavily`

---

## 10. Safety Rules

1. **No secrets in output** — never read, print, or commit `.env` files, tokens, API keys, passwords
2. **Destructive ops need approval** — always explain risks and get confirmation before:
   - Deleting files or directories
   - Running `git push --force`
   - Dropping databases
   - Modifying production config
3. **Honest blockers** — report failures directly; never fabricate output or substitute plausible-looking fake data
4. **Memory hygiene** — durable facts only in MEMORY.md; task progress lives in session_search (not memory)
5. **No backup files** — git for rollback; never create `.bak`, `.old`, `.backup` files
6. **Dry-run first** — every destructive command has a `--dry-run` equivalent; use it before the real thing

---

## 11. Debugging & Troubleshooting

### Python Debugging

```bash
# Lint only the changed file (fast)
ruff check path/to/file.py

# Type check
pyright path/to/file.py

# Test single file
pytest path/to/test_file.py -v
```

### TypeScript Debugging

```bash
# Type check only (fast)
tsc --noEmit --pretty

# Lint single file (fast — use this instead of full project)
eslint --config eslint.config.mts path/to/file.ts --format=compact

# Run single test file
vitest run path/to/test_file.ts

# Debug in browser (Next.js projects)
# Add `debugger` statement, then:
bun run dev -- --inspect
```

### General Debugging Workflow

1. Read the error message fully — check stack trace
2. Search codebase for similar patterns (`ast-grep` MCP or `search_files`)
3. Check docs/ and relevant AGENTS.md files
4. Run the smallest reproduction possible
5. Fix root cause, not symptom

---

## 12. Known Issues & Pitfalls

| Issue                                            | Affects                     | Workaround                                                                                                                                                   |
| ------------------------------------------------ | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CRLF line endings in shell scripts               | Windows Git Bash            | Scripts need `#!/bin/bash` and LF endings — check `.gitattributes`                                                                                           |
| `pip install -e file:///...` in requirements.txt | Workspace root              | The editable install path is absolute to `C:\Users\Alexa\...`; use `venv/`                                                                                   |
| Bun + Windows path translation                   | Workspace root              | MSYS/git-bash paths (`/c/Users/...`) vs Windows paths (`C:\\Users\\...`) — prefer absolute Windows paths; prefix native tool calls with `MSYS_NO_PATHCONV=1` |
| OpenCode context overflow                        | All agents with ~652 skills | Use `--disable-builtin-mcps` and `--no-custom-instructions` flags                                                                                            |
| `projects/**` excluded from markdownlint         | Workspace markdown          | Subproject markdown is linted independently in each project                                                                                                  |
| Dual Python installs (3.13 vs 3.11)              | Python scripts              | Always activate venv; `python` is 3.11, `python3` is 3.13                                                                                                    |
| `ruff check .` vs `ruff format .`                | Python                      | These are separate commands — lint ≠ format                                                                                                                  |

---

## 13. Quick Reference Cards

### Python Script Naming & Patterns

```python
# All root-level scripts follow this pattern:
# - snake_case.py filename
# - Executable (chmod +x)
# - Import from stdlib + project modules
# - `if __name__ == "__main__":` guard
# - Uses `argparse` or `fire` for CLI
# - Type hints on all function signatures

# Example from ~/AppData/Local/hermes/scripts/health_check.py:
def check_provider(provider_name: str) -> dict[str, bool]:
    ...
```

### TypeScript Patterns (projects/Bash)

```typescript
// All Bash project scripts:
// - kebab-case filenames
// - Import via ESM (`import { X } from "./y.ts"`) with .ts extension
// - Uses zod 4 for validation
// - Uses ts-morph for AST manipulation
// - Strict mode + noUncheckedIndexedAccess

// Example:
import { z } from "zod";
const Config = z.object({ mode: z.enum(["discover", "clone", ...]) });
```

### Docker Compose Layouts

```yaml
# All compose files at subproject roots, workspace root has none
# Services map to component boundaries
# Environment through .env files (gitignored)
```

### Pre-commit Hook Workflow

```bash
# Hooks run on `git commit`:
# 1. lint-staged (ts → eslint, py → ruff)
# 2. markdownlint on *.md
# 3. cspell on all files
# 4. prettier on staged files
# SKIP checks: SKIP=hook-name git commit -m "msg"
```

---

## Architecture Documentation

Generated architecture blueprints are available in `docs/Project_Architecture/`:

- **Workspace Blueprint:** `docs/Project_Architecture_Blueprint.md` — Comprehensive C4 + component + flow diagrams for entire monorepo
- **Per-Subproject Docs:** `docs/Project_Architecture/*.md` — Architecture, folder structure, and tech stack for each of 22 subprojects
- **Index:** `docs/Project_Architecture/INDEX.md` — Cross-reference table linking all generated docs

Regenerate with: `architecture-blueprint-generator` prompt when project structure changes.
