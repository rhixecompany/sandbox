# SandBox Monorepo

[![CI](https://github.com/rhixecompany/sandbox/actions/workflows/pr-ci.yml/badge.svg)](https://github.com/rhixecompany/sandbox/actions/workflows/pr-ci.yml)
[![PR CI](https://github.com/rhixecompany/sandbox/actions/workflows/pr-ci.yml/badge.svg?event=pull_request)](https://github.com/rhixecompany/sandbox/actions/workflows/pr-ci.yml)
[![TypeScript Strict](https://img.shields.io/badge/TypeScript-strict-3178C6)](https://www.typescriptlang.org/tsconfig/#strict)
[![Bun](https://img.shields.io/badge/runtime-Bun-14151A?logo=bun)](https://bun.sh)
[![Python](https://img.shields.io/badge/python-3.11%2F3.13-3776AB?logo=python)](https://python.org)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**SandBox** is a polyglot monorepo containing 17+ subprojects spanning TypeScript, Python, Go, Rust, Java, C#, and more. It serves as the workspace for Hermes agent development, automation scripts, multi-language project templates, full-stack applications, and experimental research.

## Table of Contents

- [AI Assistant & Copilot Instructions](#-ai-assistant--copilot-instructions)
- [Technology Stack](#technology-stack)
- [Project Architecture](#-project-architecture)
- [Project Index](#-project-index)
- [Getting Started](#-getting-started)
- [Development Workflow](#-development-workflow)
- [Coding Standards](#-coding-standards)
- [Testing](#-testing)
- [Contributing](#-contributing)
- [License](#-license)

## 🤖 AI Assistant & Copilot Instructions

**For GitHub Copilot, Claude, or other AI assistants:** See [`.github/copilot-instructions.md`](.github/copilot-instructions.md)

This guide provides:

- **Quick Start** — Setup for workspace and subprojects
- **Subproject-Specific Guidance** — Detailed commands & patterns for Bash, Banking, comicwise, and ecom
- **MCP Server Configuration** — 18 servers (14 configured, 4 recommended)
- **Common Tasks** — Practical workflows with copy-paste examples
- **Reference Tables** — Lookup guide for quick answers

**Quick links:**

- [Bash Toolkit](/.github/copilot-instructions.md#bash--automation-toolkit-projectsbash) — TS automation pipeline
- [Banking App](/.github/copilot-instructions.md#banking--fintech-app-projectsbanking) — Next.js 16 + Drizzle
- [Comicwise](/.github/copilot-instructions.md#comicwise--comic-streaming-projectscomicwise) — Next.js 15 + Prisma (quality gates)
- [Ecom](/.github/copilot-instructions.md#ecom--django--react-projectsecom) — Django + React (dual servers)

---

## Technology Stack

### Runtimes & Package Managers

| Technology   | Version     | Usage                                                   |
| ------------ | ----------- | ------------------------------------------------------- |
| **Bun**      | 1.3.14+     | Primary runtime & package manager (TypeScript projects) |
| **Node.js**  | 18 / 20     | Legacy JavaScript projects                              |
| **Python**   | 3.11 / 3.13 | Backend services, automation scripts, data processing   |
| **pnpm**     | latest      | comicwise project                                       |
| **npm**      | latest      | Legacy JS projects                                      |
| **uv / pip** | latest      | Python dependency management                            |

### Frontend Frameworks

| Framework                   | Used In                                       |
| --------------------------- | --------------------------------------------- |
| **Next.js 16** (App Router) | Banking, rhixecompany-comics                  |
| **Next.js 15** (App Router) | comicwise, rhixe_scans, university-libary-jsm |
| **React 18** (CRA)          | xamehi                                        |
| **React 17** (CRA)          | xamehi.tv                                     |
| **Django Templates**        | profile, ecom                                 |

### Backend & API

| Technology       | Used In                                               |
| ---------------- | ----------------------------------------------------- |
| **Django / DRF** | ecom, profile, rhixecompany-comics, xamehi, xamehi.tv |
| **Express.js**   | xamehi                                                |
| **FastAPI**      | Python automation services                            |
| **Prisma**       | comicwise, rhixe_scans, rhixecompany-comics           |
| **Drizzle ORM**  | Banking, university-libary-jsm                        |

### Databases & Infrastructure

| Technology                     | Used In                                           |
| ------------------------------ | ------------------------------------------------- |
| **PostgreSQL**                 | Primary database (multiple projects)              |
| **Neon Serverless PostgreSQL** | university-libary-jsm                             |
| **Redis**                      | Caching / session store (university-libary-jsm)   |
| **Stripe**                     | Payment processing (comicwise, rhixe_scans)       |
| **PayPal**                     | Payment processing (rhixe_scans, xamehi.tv, ecom) |
| **Plaid / Dwolla**             | Banking / fintech (Banking)                       |

### Tooling & Quality Gates

| Tool                            | Purpose                            | Config                        |
| ------------------------------- | ---------------------------------- | ----------------------------- |
| **TypeScript** (`tsc --noEmit`) | Type checking                      | `tsconfig.json` (strict mode) |
| **ESLint** 10 (flat config)     | JS/TS linting (zero-warnings gate) | `eslint.config.mts`           |
| **Prettier** 3                  | Code formatting                    | `.prettierrc.ts`              |
| **Ruff**                        | Python linting & formatting        | `.ruff.toml`                  |
| **Pyright**                     | Python type checking               | `pyrightconfig.json`          |
| **markdownlint-cli2**           | Markdown linting                   | `.markdownlintrc.json`        |
| **cspell** 10                   | Spell checking                     | `cspell.json`                 |
| **pre-commit** 4.6              | Git hooks                          | `.pre-commit-config.yaml`     |
| **git-cliff** 2.13              | Changelog generation               | `cliff.toml`                  |
| **EditorConfig**                | Cross-editor consistency           | `.editorconfig`               |
| **ShellCheck + shfmt**          | Shell script quality               | `.shellcheckrc`               |
| **codespell**                   | Spelling verification              | `.codespellrc`                |

### MCP Server Ecosystem

16 MCP servers integrated for enhanced agent capabilities:

| Server                | Purpose                                |
| --------------------- | -------------------------------------- |
| `ast-grep`            | AST-based code search & replace        |
| `code-sandbox`        | Isolated Node.js execution             |
| `fetch`               | HTTP content extraction                |
| `filesystem`          | Sandboxed file operations              |
| `github`              | GitHub API operations                  |
| `linear`              | Project management                     |
| `mcp-docker`          | Container management                   |
| `memory`              | Persistent agent memory                |
| `mindstudio`          | Multi-modal AI tools                   |
| `playwright`          | Browser automation                     |
| `sequential-thinking` | Structured reasoning                   |
| `smithery`            | MCP registry                           |
| `python-quality`      | Ruff + Pyright integration             |
| `tooling-lint`        | ESLint, Prettier, markdownlint, cspell |
| `tooling-config`      | Pre-commit, git-cliff, editorconfig    |

## 🧬 Project Architecture

```
SandBox/                              # Monorepo root
├── .github/                          # GitHub configuration
│   ├── prompts/                      # Canonical prompt library (200+ prompts)
│   ├── workflows/                    # CI/CD pipelines (18 workflows)
│   ├── scripts/                      # Shared GitHub automation scripts (per-repo)
│   ├── hooks/                        # Git hooks
│   └── copilot-instructions.md       # Workspace-wide Copilot guidance
├── projects/                         # All subprojects (17+)
│   ├── Banking/                      # Fintech — Next.js 16 + Drizzle + Plaid
│   ├── Bash/                         # TypeScript automation toolkit (6-phase orchestrator)
│   ├── comicwise/                    # Comic streaming — Next.js 15 + Prisma + Stripe
│   ├── cookiecutter-django-tailwind/ # Django 5 + Tailwind template
│   ├── Django-Scrapy-Selenium/       # Web scraper — Django + Scrapy + Selenium
│   ├── ecom/                         # E-commerce — Django 3.1 + DRF + React
│   ├── mcp-servers/                  # MCP server implementations (10 languages)
│   ├── profile/                      # Blog/CMS — Django + GCS + CKEditor
│   ├── Python-projects/              # 18 Python automation scripts
│   ├── Resume_maker/                 # CLI PDF generator — TypeScript + Bun
│   ├── rhixe_scans/                  # Comic reader — Next.js 15 + Prisma + WebSocket
│   ├── rhixecompany-comics/          # Comics platform — Django + Next.js 16
│   ├── selenium_webdriver/           # Browser automation — Node.js + Selenium 4
│   ├── university-libary-jsm/        # Library mgmt — Next.js 15 + Drizzle + Neon
│   ├── xamehi/                       # Full-stack — Django + Express + React
│   ├── xamehi.tv/                    # Streaming — DRF + React 17
│   └── youtube-downloader/           # CLI — Python + yt-dlp
├── docs/                             # Hermes documentation & reference materials
│   ├── architecture/                 # Architecture blueprints
│   ├── Project_Architecture/         # Per-project architecture docs
│   └── tech-stack/                   # Technology stack analysis
├── scripts/                          # Pointer README — canonical scripts live in ~/AppData/Local/hermes/scripts/
│   ├── audit_prompts.py/             # Prompt library auditing
│   ├── fix_*  /                      # Batch remediation scripts
│   ├── generate_skills.py/           # Skill generation
│   └── ... (100+ automation scripts)
├── AGENTS.md                         # Canonical agent instructions
├── .hermes.md                        # Hermes profile + MCP config
├── .mcp.json                         # MCP server definitions
├── tsconfig.json                     # Root TypeScript config (strict)
├── package.json                      # Root Bun workspace
└── requirements.txt                  # Python dependencies
```

### Architecture Overview

The workspace follows a **polyglot monorepo** pattern:

- **Shared tooling at root**: TypeScript config, Python venv, ESLint, Prettier, markdownlint, cspell
- **Autonomous subprojects**: Each `projects/*/` directory is independently configurable with its own `AGENTS.md`, tooling config, and CI pipeline
- **CI/CD is monorepo-aware**: PR workflows detect changed projects and run only relevant checks (see `pr-ci.yml`)
- **Branch strategy**: `production` ← `staged` ← `development` ← `feature/*` branches
- **Agent-first**: All instructions are written for AI agents (Hermes, Copilot, Claude, Cursor) with explicit routing, tool precedence, and MCP-first policy

### Key Design Patterns

1. **6-Phase Orchestration** (Bash project): Discovery → Clone → Triage → Debug → Remediation → Cross-Reference
2. **Multi-Wrapper Parity**: Every destructive script has `.sh`, `.ps1`, `.bat` equivalents with `--dry-run` support
3. **TypeScript Strict**: No `any`, no implicit returns; `zod` v4 for validation
4. **MCP-First Tooling**: Prefer MCP servers over native CLI tools for every capability

### Data Flow

```
Developer PR ──→ pr-ci.yml (detect changed projects)
                      │
            ┌─────────┼─────────┐
            ▼         ▼         ▼
      Root checks  Bun checks  Python checks
      (tsc, lint)  (install,   (install,
                    typecheck,  ruff lint)
                    lint, test)
            │         │         │
            └─────────┼─────────┘
                      ▼
              PR Summary Comment
```

## 📋 Project Index

### Active Projects

| #   | Project                   | Language/Framework                                               | Status    | Description                                               |
| --- | ------------------------- | ---------------------------------------------------------------- | --------- | --------------------------------------------------------- |
| 1   | **Banking**               | TypeScript, Next.js 16, Drizzle, Plaid/Dwolla                    | ✅ Active | Fintech application                                       |
| 2   | **Bash**                  | TypeScript, Bun                                                  | ✅ Active | 6-phase automation orchestrator with multi-wrapper parity |
| 3   | **comicwise**             | TypeScript, Next.js 15, Prisma, Stripe                           | ✅ Active | Comic book streaming platform                             |
| 4   | **mcp-servers**           | TypeScript, Python, Go, Rust, Java, Kotlin, PHP, Ruby, Swift, C# | ✅ Active | MCP server implementations across 10 languages            |
| 5   | **Resume_maker**          | TypeScript, Bun                                                  | ✅ Active | JSON → Markdown → PDF resume generator                    |
| 6   | **rhixe_scans**           | TypeScript, Next.js 15, Prisma, WebSocket, Stripe/PayPal         | ✅ Active | Comic reader platform                                     |
| 7   | **rhixecompany-comics**   | TypeScript/Python, Next.js 16 + Django, Prisma, Celery           | ✅ Active | Full comics platform                                      |
| 8   | **selenium_webdriver**    | JavaScript, Node.js, Selenium 4                                  | ✅ Active | Chrome browser automation                                 |
| 9   | **university-libary-jsm** | TypeScript, Next.js 15, Drizzle, Neon, Redis                     | ✅ Active | University library management system                      |
| 10  | **xamehi.tv**             | Python, DRF + React 17, PayPal, JWT                              | ✅ Active | Video streaming platform                                  |
| 11  | **youtube-downloader**    | Python 3.11, yt-dlp                                              | ✅ Active | YouTube download CLI tool                                 |

### Maintenance / Template Projects

| #   | Project                          | Language/Framework                       | Status                  | Description                   |
| --- | -------------------------------- | ---------------------------------------- | ----------------------- | ----------------------------- |
| 12  | **cookiecutter-django-tailwind** | Python, Django 5, Tailwind               | 🔧 Maintenance          | Cookiecutter project template |
| 13  | **Django-Scrapy-Selenium**       | Python, Django, Scrapy, Selenium, Celery | 🔧 Consolidation target | Web scraping framework        |
| 14  | **ecom**                         | Python, Django 3.1, DRF, React/Redux     | 🔧 Maintenance          | E-commerce platform (legacy)  |
| 15  | **profile**                      | Python, Django, GCS, CKEditor 5          | 🔧 Maintenance          | Blog / CMS                    |
| 16  | **xamehi**                       | Python/JS, Django + Express + React      | 🔧 Consolidation target | Full-stack application        |
| 17  | **Python-projects**              | Python 3.11                              | 📦 Archive candidate    | 18 beginner Python scripts    |

### CI/CD Pipeline

18 GitHub Actions workflows handle automated quality control:

| Workflow                | Trigger            | Scope                                   |
| ----------------------- | ------------------ | --------------------------------------- |
| `pr-ci.yml`             | PR → `development` | Monorepo-aware multi-project validation |
| `bash-scripts-ci.yml`   | PR touching Bash   | TypeScript tests + shell validation     |
| `python-ci.yml`         | Python changes     | Ruff + Pyright                          |
| `validate-readme.yml`   | PR → `staged`      | README freshness check                  |
| `codespell.yml`         | Push/PR → `staged` | Spelling                                |
| `deploy-website.yml`    | Push → `main`      | Astro → GitHub Pages                    |
| `traffic-reporting.yml` | Daily 1am          | GitHub traffic stats                    |

## 🚀 Getting Started

### Prerequisites

| Tool        | Version | Installation                                                            |
| ----------- | ------- | ----------------------------------------------------------------------- |
| **Bun**     | 1.3.14+ | `bun install -g bun` or [bun.sh](https://bun.sh)                        |
| **Python**  | 3.11+   | [python.org](https://python.org) or `winget install Python.Python.3.11` |
| **Node.js** | 18+     | [nodejs.org](https://nodejs.org) or `winget install OpenJS.NodeJS`      |
| **Git**     | latest  | `winget install Git.Git`                                                |

### Quick Start

```bash
# Clone the repository
git clone https://github.com/rhixecompany/sandbox.git
cd SandBox

# Install root TypeScript dependencies
bun install

# Set up Python environment
python -m venv venv
source venv/Scripts/activate   # Windows
# or: source venv/bin/activate  # Linux/macOS
pip install -r requirements.txt

# Navigate to a project and follow its AGENTS.md
cd projects/Bash
bun install
bun run format:check   # Prettier
bun run typecheck      # tsc --noEmit
bun run lint:strict    # ESLint, zero warnings
bun run test           # Vitest
```

### Per-Project Setup

Each subproject is self-contained. Enter its directory and follow the local `AGENTS.md`:

```bash
cd projects/<project-name>
# Read AGENTS.md for project-specific setup
```

## 🔧 Development Workflow

### Branch Strategy

```
production  ← auto-published from staged (protected)
    ↑
staged      ← release candidate (protected)
    ↑
development ← active integration, all PRs target here
    ↑
feature/*   ← short-lived branches, deleted after merge
```

### Branch Naming

```text
<type>/<project>/<kebab-case-description>
```

**Examples:**

- `feat/resume-maker/add-html-output`
- `fix/bash/install-script-permissions`
- `docs/root/update-readme`
- `chore/root/upgrade-bun-version`

**Types:** `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`

### Standard Workflow

```bash
# 1. Start from clean development
git checkout development
git pull origin development

# 2. Create feature branch
git checkout -b feat/<project>/<description>

# 3. Make changes, scoped to one project

# 4. Commit with conventional message
git add <files>
git commit -m "feat: add HTML output option to resume generator"

# 5. Keep branch up to date
git fetch origin
git rebase origin/development

# 6. Push and open PR (target: development → production)
git push origin feat/<project>/<description>
```

### Pre-PR Checklist

```bash
# Full quality gate
bun run format && bun run typecheck && bun run lint:strict && bun run test

# Or per-project
cd projects/<name>
bun run typecheck && bun run lint

# Review your diff
git diff origin/development
```

### Commit Convention

Follow conventional commits:

```
<type>: <description>

feat: add HTML output option
fix: handle empty resume data gracefully
docs: update README with new flags
chore: upgrade markdown-pdf to 11.0.0
refactor: extract PDF generation to separate module
```

## 📐 Coding Standards

### Language-Specific Rules

| Language       | Style Guide  | Key Rules                                                                          |
| -------------- | ------------ | ---------------------------------------------------------------------------------- |
| **TypeScript** | Strict mode  | No `any`, no implicit returns, `noUncheckedIndexedAccess`, `zod` v4 for validation |
| **Python**     | PEP 8        | 4-space indent, double quotes, Ruff linting                                        |
| **Bash**       | Kebab-case   | `.sh` extension, ShellCheck validated                                              |
| **PowerShell** | PascalCase   | `.ps1` extension, 4-space indent                                                   |
| **Markdown**   | markdownlint | `.markdownlintrc.json` rules                                                       |

### General Conventions

- **CRLF line endings** per `.editorconfig` (Windows host)
- **2-space indent** for TypeScript/JavaScript
- **Single quotes** for TypeScript/JavaScript strings
- **No backup files** — use git for rollback (never `.bak`, `.old`)
- **Dry-run first** — destructive actions need `--dry-run` flag
- **Logs** — timestamped to `logs/action_YYYYMMDD_HHMMSS.log`
- **Secrets** — never hardcoded; `.env` is `.gitignore`'d
- **Commits** — conventional format (`<type>: <description>`)

### Validated Via

Run these from the workspace root or individual project directories:

```bash
bun run format:check              # Prettier formatting
bun run typecheck                 # TypeScript strict type check
bun run lint:strict               # ESLint, zero warnings
ruff check .                      # Python lint
pyright                           # Python type check
markdownlint-cli2 .               # Markdown lint
cspell "**/*.md"                  # Spell check
```

## 🧪 Testing

### TypeScript / Bun Projects

```bash
# Run all tests
bun run test

# Single test file
bun run test -- src/specific.test.ts

# Tests matching pattern
bun run test -- --grep "pattern"

# Shell script verification
bash tests/verify-dryrun.sh
bash test-all.sh
```

Vitest tests live in `**/*.test.ts` alongside source files.

### Python Projects

```bash
# Run pytest
pytest

# With coverage
pytest --cov=.
```

### CI Validation

Every PR triggers the `pr-ci.yml` workflow which:

1. Detects which project(s) changed
2. Runs appropriate toolchain checks (install, typecheck, lint)
3. Validates no forbidden files (`.env`, credentials, binaries)
4. Checks PR size (<100 files recommended)
5. Posts a summary comment on the PR

## 🤝 Contributing

1. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) for full workflow details
2. Review [`AGENTS.md`](AGENTS.md) for agent-specific guidance
3. Follow the **branch naming convention**: `<type>/<project>/<description>`
4. Keep PRs **small and scoped** to one project
5. Run the **full quality gate** before opening a PR
6. **Rebase, don't merge** — keep linear history
7. Target PRs to `development` (never `production` directly)

### Key Resources

| File                                   | Purpose                                          |
| -------------------------------------- | ------------------------------------------------ |
| [`AGENTS.md`](AGENTS.md)               | Canonical agent instructions, toolchain, routing |
| [`CLAUDE.md`](CLAUDE.md)               | Claude model guidance                            |
| [`CONTRIBUTING.md`](CONTRIBUTING.md)   | Git workflow, PR guidelines, branch naming       |
| [`.cursorrules`](.cursorrules)         | Cursor IDE configuration                         |
| [`.hermes.md`](.hermes.md)             | Hermes Agent profile & MCP config                |
| [`docs/`](docs/)                       | Architecture docs, tech stack analysis           |
| [`.github/prompts/`](.github/prompts/) | 200+ canonical MCP prompts                       |

## 📄 License

This project is private workspace software. See individual subprojects for their respective licenses. The `youtube-downloader` project includes a `LICENSE` file; all others are governed by workspace rules defined in `AGENTS.md`.

---

> **Maintained by Hermes Agent** · Workspace for multi-language automation, research, and toolkit development.
