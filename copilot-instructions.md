# Copilot Instructions — SandBox Monorepo

**Canonical reference:** See `AGENTS.md` (general agent guidance), `.hermes.md` (Hermes-specific), `CLAUDE.md` (Claude-specific).

## Overview

**SandBox** is a polyglot monorepo containing 17+ autonomous subprojects spanning TypeScript, Python, Go, Rust, Java, C#, and more. It serves as the workspace for Hermes agent development, automation scripts, multi-language project templates, full-stack applications, and experimental research.

### Key Architecture Pattern

- **Root workspace** handles only workspace-level code (config, shared scripts, TypeScript/Python linting)
- **Each subproject** (`projects/`) is autonomous with its own `AGENTS.md`, `package.json`, CI workflows, and build system
- **Shared config** at root: `.github/`, `.editorconfig`, linting rules, prompt library

**Important:** When working on a subproject, check that project's `AGENTS.md` and `package.json` for specific commands and conventions.

---

## Quick Start

### Root Workspace Setup

```bash
cd C:/Users/Alexa/Desktop/SandBox
bun install
python -m venv venv
source venv/Scripts/activate  # .venv/Scripts/activate on Windows
pip install -r requirements.txt
```

### Root Workspace Validation (workspace-level code only)

```bash
# All checks
bun run check

# Individual checks
bun run lint                  # ESLint (flat config)
bun run format:check          # Prettier
bun run typecheck             # TypeScript
bun run markdownlint          # Markdown linting
bun run spellcheck            # cspell
```

### Subproject Work

Each subproject is autonomous. See its `package.json` and `README.md` for project-specific commands.

**Examples:**

- **Banking** (Next.js 16 + Drizzle): `cd projects/Banking && bun run dev`
- **comicwise** (Next.js + Prisma): `cd projects/comicwise && bun run dev`
- **Bash** (TS automation): `cd projects/Bash && bun run lint`

---

## Major Subprojects at a Glance

| Project             | Stack                              | Key Command                  | Purpose                       |
| ------------------- | ---------------------------------- | ---------------------------- | ----------------------------- |
| **Banking**         | Next.js 16, Drizzle, Plaid, Dwolla | `bun run dev`                | Fintech app (bank simulation) |
| **comicwise**       | Next.js 15, Prisma, Stripe         | `bun run dev`                | Comic streaming platform      |
| **Bash**            | Bun/TypeScript                     | `bun run lint`               | Automation toolkit & scripts  |
| **ecom**            | Django REST, React/Redux           | `python manage.py runserver` | E-commerce application        |
| **mcp-servers**     | Multi-language                     | `bun run <lang>-server`      | MCP server implementations    |
| **Python-projects** | Python 3.11/3.13                   | `python scripts/...`         | 18+ standalone scripts        |

---

## Build, Test, and Lint Commands

### Root Workspace Commands

All commands run from the workspace root (`C:/Users/Alexa/Desktop/SandBox`).

#### Linting & Formatting

```bash
# Lint
bun run lint              # Show ESLint violations
bun run lint:fix          # Fix ESLint violations
bun run lint:fix:all      # Fix all types (directives, problems, suggestions, layout)

# Format
bun run format            # Run Prettier
bun run format:check      # Check Prettier compliance (no changes)

# Markdown & Spell
bun run markdownlint      # Check markdown files
bun run spellcheck        # Check spelling in code/docs
```

#### Type Checking

```bash
bun run typecheck         # TypeScript strict mode check
```

#### Complete Validation

```bash
bun run check             # Run: lint + format:check + typecheck + markdownlint + spellcheck
```

### Subproject Commands

Each subproject has its own commands. Common patterns:

```bash
cd projects/<PROJECT>

# Banking / comicwise (Next.js)
bun run dev               # Development server
bun run build             # Production build
bun run test              # Run tests (Playwright + Vitest)
bun run test:ui           # Playwright UI tests
bun run test:browser      # Vitest browser tests
bun run lint              # ESLint
bun run lint:fix          # ESLint fix
bun run type-check        # TypeScript check
bun run db:push           # Drizzle/Prisma database sync
bun run db:seed           # Seed database

# Bash (TypeScript automation)
bun run lint              # ESLint
bun run test              # Vitest
```

---

## Coding Standards & Conventions

### File Naming

| Language       | Convention                                               | Examples                              |
| -------------- | -------------------------------------------------------- | ------------------------------------- |
| **TypeScript** | `kebab-case.ts` (scripts), `PascalCase.tsx` (components) | `cache-clean.ts`, `UserProfile.tsx`   |
| **Python**     | `snake_case.py` (PEP 8)                                  | `health_check.py`, `audit_prompts.py` |
| **PowerShell** | `PascalCase.ps1`                                         | `Orchestrator-Unified.ps1`            |
| **Bash**       | `kebab-case.sh`                                          | `test-all.sh`, `cache-clean.sh`       |

### Code Style

- **TypeScript**: 2-space indent, single-quotes, `strict` mode, `noUncheckedIndexedAccess`
- **Python**: 4-space indent (PEP 8), double-quotes, type hints encouraged
- **Line endings**: CRLF (Windows host — configured in `.editorconfig`)
- **No `any` type** unless explicitly justified
- **No backup files** (`.bak`, `.old`) — use git for rollback

### Git Conventions

#### Branch Naming

```
<type>/<project>/<kebab-case-description>
```

**Types:** `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`
**Project:** One of the 17+ subprojects under `projects/`, or `root` for workspace-level changes
**Examples:**

- `feat/banking/add-plaid-webhook`
- `fix/comicwise/stripe-charge-retry`
- `docs/root/update-readme`
- `refactor/bash/cleanup-cache-module`

#### PR Target Branch

All PRs target `development` branch (protected), not `main`. Releases flow from `main` → `production`.

#### Commit Messages

```
<type>: <description>

Examples:
  feat: add cache-clean dry-run mode
  fix: correct Plaid webhook signature validation
  refactor: extract database connection pool
```

---

## High-Level Architecture

### Monorepo Pattern

```
SandBox/
├── .github/
│   ├── workflows/         # Shared CI (all subprojects)
│   ├── instructions/      # Domain-specific rules (database, testing, frameworks)
│   ├── copilot-instructions.md
│   └── prompts/           # 190+ canonical prompts (single source of truth)
├── AGENTS.md              # Master agent guidance (read this first)
├── .hermes.md             # Hermes-specific overrides
├── CLAUDE.md              # Claude-specific stubs
├── package.json           # Root workspace (minimal)
├── tsconfig.json          # Root TypeScript (excludes projects/)
├── .ruff.toml             # Python linting
├── projects/              # 17+ autonomous subprojects
│   ├── Banking/           # Next.js 16 fintech
│   ├── comicwise/         # Next.js 15 streaming
│   ├── projects/Bash/              # TypeScript automation
│   ├── ecom/              # Django + React
│   ├── mcp-servers/       # MCP implementations
│   ├── Python-projects/   # Standalone scripts
│   └── ...
├── scripts/               # Canonical location: C:/Users/Alexa/AppData/Local/hermes/scripts/
├── docs/                  # Architecture docs, audits, blueprints
└── .vscode/               # Shared VS Code workspace settings
```

### Subproject Autonomy

Each subproject is self-contained:

- **Own `package.json`** with project-specific scripts and dependencies
- **Own `AGENTS.md`** (thin stub that defers to root `AGENTS.md` for shared rules)
- **Own `.cursorrules`** (thin stub deferring to root)
- **Own `tsconfig.json`** (extends root when applicable)
- **Own CI workflow** in `.github/workflows/`
- **Own build/test/lint commands**

Root `tsconfig.json` **excludes** `projects/` to prevent type-checking subproject code. Each subproject type-checks independently.

### Root Workspace Scope

The root workspace handles **only**:

- Workspace-level TypeScript/JavaScript (configuration, utilities)
- Python scripts at workspace root
- Shared tooling configuration
- Prompt library and documentation
- CI orchestration

**Do NOT** lint/test subprojects from root. Each project is independent.

---

## Key Patterns & Workflows

### TypeScript Strict Mode

All TypeScript files:

```typescript
// Enabled in tsconfig.json:
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "verbatimModuleSyntax": true
  }
}
```

Avoid `any` unless justified. Use `unknown` + type guards instead.

### Python Package Management

```bash
# Root workspace Python setup
cd C:/Users/Alexa/Desktop/SandBox
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

# Subprojects may have their own venv/pyproject.toml
cd projects/ecom
python -m venv venv
pip install -r requirements.txt
```

Ruff is configured at root (`.ruff.toml`). Use `bun run spellcheck` for all Python files.

### Multi-Wrapper Scripts

Any cross-platform automation script **must** have three wrappers:

```bash
# Canonical location: C:/Users/Alexa/AppData/Local/hermes/scripts/
operation.sh       # Bash (Linux/WSL/Git Bash)
operation.ps1      # PowerShell (Windows)
operation.bat      # Batch (Windows fallback)
```

---

## MCP Server Configuration

The workspace includes 16 configured MCP servers. Before using native tools (terminal commands, direct file access), check the MCP precedence:

1. **filesystem** — File read/write/stat/search
2. **github** — PR, issues, file contents
3. **ast-grep** — AST-based code search and replace
4. **playwright** — Browser automation
5. **sequential-thinking** — Structured multi-step reasoning

See `AGENTS.md` § 6 for the complete MCP precedence table.

---

## Common Tasks & Quick Reference

### Run Full Validation

```bash
bun run check    # lint + format:check + typecheck + markdownlint + spellcheck
```

### Develop a Subproject

```bash
cd projects/Banking
bun install      # Install dependencies
bun run dev      # Start dev server
bun run test:ui  # Run Playwright tests
bun run lint:fix # Fix linting violations
```

### Create a Feature Branch

```bash
git checkout development
git pull origin development
git checkout -b feat/banking/add-webhook-retry
# Make changes
git add .
git commit -m "feat: add webhook retry logic"
git push origin feat/banking/add-webhook-retry
# Open PR targeting development
```

### Update Dependencies

```bash
cd projects/comicwise
bun update
# Test changes
bun run test && bun run build
```

### Check TypeScript Errors

```bash
cd projects/Banking
bun run type-check        # Show errors
bun run type-check:watch  # Watch mode (continuous)
```

---

## Troubleshooting

### "Module not found" errors

- Root workspace: run `bun install`
- Subproject: `cd projects/<PROJECT> && bun install`

### TypeScript strict mode violations

Use `bun run typecheck` to see all errors. Avoid `any`; use `unknown` + type narrowing.

### Linting failures

Run `bun run lint:fix` in root or subproject to auto-fix issues.

### Test failures

Check the project's `test:ui` (Playwright) or `test:browser` (Vitest) output for details.

---

## See Also

- **AGENTS.md** — Master agent guidance (conventions, MCP servers, workflows)
- **CLAUDE.md** — Claude-specific behavior notes
- **.hermes.md** — Hermes-specific project overrides
- **CONTRIBUTING.md** — Branching model and workflow details
- **projects/\*/AGENTS.md** — Subproject-specific guidance
