# Technology Stack Blueprint

## Project: SandBox Root

> **Generated:** 2026-06-25  
> **Generator:** technology-stack-blueprint-generator  
> **Analysis Depth:** Comprehensive

---

## Overview

The SandBox root serves as the workspace orchestrator for 15+ subprojects. It provides the top-level context, tooling configuration, and shared automation scripts that coordinate the entire ecosystem.

**Project Type:** Monorepo Workspace (Multi-Technology Orchestrator)

---

## Technology Stack

### Languages & Runtimes

| Technology | Version | Usage |
|---|---|---|
| Python 3 | 3.11.15 / 3.13.14 | Automation scripts, toolchain |
| Bash | — | Shell scripting, CI/CD |
| PowerShell | 5.1+ | Windows orchestration |
| Bun | 1.3.14 | TypeScript runtime (shared tooling) |
| Node.js | >=18 | JavaScript runtime (shared tooling) |
| Git | — | Version control |

### Package Managers

| Tool | Version | Usage |
|---|---|---|
| bun | 1.3.14 | Primary JS/TS package manager |
| pip | (Python 3.11) | Python dependency management |
| uv | installed | Fast Python package installer |

### Core Dependencies (Root Level)

| Dependency | Version | Category |
|---|---|---|
| prettier | ^3.8.3 | Code formatting |
| eslint | ^10.4.0 | Linting |
| typescript | latest | Type checking |
| husky | ^9.1.7 | Git hooks |
| lint-staged | ^16.4.0 | Staged file linting |
| cspell | ^10.0.0 | Spell checking |
| markdownlint-cli2 | ^0.22.1 | Markdown linting |

### CI/CD & Development Tools

| Tool | Usage |
|---|---|
| Hermes AI Agent | Primary development assistant |
| GitHub Actions | CI workflows |
| Git Hooks (husky) | Pre-commit validation |
| MCP Servers (13) | Extended tool capabilities |
| Docker | Containerized environments |

---

## Project Structure

```
SandBox/
├── AGENTS.md          # Workspace context & conventions
├── Bash/              # Primary automation toolkit
├── Resume_maker/      # Job docs generator
├── projects/          # All subprojects (15+)
│   ├── Banking/       # Next.js fintech app
│   ├── comicwise/     # Next.js comic streaming
│   ├── cookiecutter-django-tailwind/
│   ├── Django-Scrapy-Selenium/
│   ├── docs/          # Documentation only
│   ├── ecom/          # Ecommerce platform
│   ├── profile/       # Django blog/CMS
│   ├── Python-projects/
│   ├── rhixe_scans/   # Comic reader
│   ├── rhixecompany-comics/
│   ├── selenium_webdriver/
│   ├── university-libary-jsm/
│   ├── xamehi.tv/     # Streaming platform
│   ├── xamehi/        # Dual-backend app
│   └── youtube-downloader/
├── prompts/           # AI prompt assets
├── docs/              # Hermes docs & reports
└── .hermes/           # Hermes plans & config
```

---

## Licensing

| Component | License |
|---|---|
| Root workspace | ISC (package.json) |
| Subprojects | Various (MIT, ISC, proprietary) |

---

## Coding Conventions

- **DRY principle**: No redundant facts across files
- **Git-first**: No `.bak`/`.backup`/`.old` copies
- **Bun-first**: TypeScript projects use `bun run`, `bun install`
- **Minimal edits**: Keep changes scoped and targeted
- **Environment security**: Never commit secrets, tokens, or `.env`
- **Session logging**: Update `SESSION_REPORT.md` on start/end

---

## Architecture Diagram

```
┌────────────────────────────────────────────────────────────┐
│                    SandBox Root (Orchestrator)              │
├──────────┬──────────┬──────────┬──────────┬────────────────┤
│  Bash/   │Resume_   │ projects/│  docs/   │  .hermes/      │
│ (Bun/TS) │ maker/   │ (15 dirs)│ (reports)│  (plans)       │
│          │ (Bun/TS) │          │          │                │
├──────────┴──────────┴──────────┴──────────┴────────────────┤
│  Tooling: eslint, prettier, husky, markdownlint, cspell    │
│  Runtime: Bun 1.3.14, Python 3.11/3.13, Node.js >=18      │
│  CI: GitHub Actions, Git hooks                             │
└────────────────────────────────────────────────────────────┘
```

---

## Usage Patterns

- Primary development via Hermes AI Agent with 14 MCP servers
- TypeScript projects use Bun runtime exclusively
- Python projects use pip with optional uv acceleration
- Cross-project references via `projects/*/AGENTS.md`
- Validation toolkit: `cd Bash && bun run format && bun run typecheck && bun run lint:strict`

---

## Environment

| Variable | Value |
|---|---|
| OS | Windows 11 |
| Shell | Git Bash (MSYS) |
| Editor | VS Code |
| Python 3 | 3.13.14 |
| Python (alt) | 3.11.15 |
| Bun | 1.3.14 |
| uv | installed |
