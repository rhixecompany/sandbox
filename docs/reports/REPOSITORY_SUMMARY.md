# REPOSITORY_SUMMARY.md

# SandBox Workspace — Technical Overview

**Generated:** 2026-07-25  
**Repository:** `C:\Users\Alexa\Desktop\SandBox`  
**Structure:** Monorepo with 17 projects under `projects/`

---

## Architecture

| Property | Value |
|----------|-------|
| **Type** | Polyglot monorepo |
| **Projects** | 17 (9 active, 3 maintenance, 5 archived/consolidation targets) |
| **Languages** | TypeScript (9), Python (8), Bash/PowerShell (2) |
| **Runtimes** | Bun 1.3.14+, Node 18/20, Python 3.11/3.13 |
| **Package Managers** | bun (primary), pnpm, npm, uv/pip |
| **Default Branch** | `production` (auto-published from `staged`) |
| **Working Branch** | `development` |

---

## Project Inventory

| # | Project | Type | Status | Stack | CI |
|---|---------|------|--------|-------|----|
| 1 | **Banking** | Fintech | Active | Next.js 16, Drizzle, Plaid/Dwolla, Bun | ✅ Project-specific |
| 2 | **Bash** | Automation Toolkit | Active | TypeScript, Bun, PowerShell wrappers | ✅ Project-specific |
| 3 | **comicwise** | Comic Streaming | Active | Next.js 15, Prisma, Stripe, pnpm | ✅ Shared PR CI |
| 4 | **cookiecutter-django-tailwind** | Template | Maintenance | Django 5, Tailwind, cookiecutter | ❌ Template only |
| 5 | **Django-Scrapy-Selenium** | Scraper | Consolidation target | Django, Scrapy, Selenium, Celery | ✅ Shared PR CI |
| 6 | **ecom** | E-commerce | Maintenance | Django 3.1, DRF, React/Redux, PayPal | ❌ Legacy Django |
| 7 | **mcp-servers** | MCP Implementations | Active | TypeScript, Python, Go, Rust, Java, Kotlin, PHP, Ruby, Swift, C# | ❌ No CI |
| 8 | **profile** | Blog/CMS | Maintenance | Django, GCS, CKEditor 5 | ❌ No CI |
| 9 | **Python-projects** | Scripts | Archive candidate | 18 Python scripts | ❌ No CI |
| 10 | **Resume_maker** | CLI Generator | Active | TypeScript, Bun, markdown-pdf | ✅ Project-specific |
| 11 | **rhixe_scans** | Comic Reader | Active | Next.js 15, Prisma 6, Stripe/PayPal, WebSocket | ✅ Shared PR CI |
| 12 | **rhixecompany-comics** | Comics Platform | Active | Django + Next.js 16, Prisma, Celery | ✅ Shared PR CI |
| 13 | **selenium_webdriver** | Browser Automation | Active | Node.js, Selenium 4 | ❌ No CI |
| 14 | **university-libary-jsm** | Library Mgmt | Active | Next.js 15, Drizzle, Neon, Redis | ✅ Shared PR CI |
| 15 | **xamehi** | Full-stack | Consolidation target | Django + Express + React | ❌ No CI |
| 16 | **xamehi.tv** | Streaming | Active | DRF + React 17 (CRA), PayPal, JWT | ❌ No CI |
| 17 | **youtube-downloader** | CLI Tool | Active | Python, yt-dlp | ❌ No CI |

---

## Technology Matrix

### Frontend (TypeScript)
| Project | Framework | UI Lib | State | Styling | DB/ORM |
|---------|-----------|--------|-------|---------|--------|
| Banking | Next.js 16 (App) | shadcn/ui | React Query | Tailwind | Drizzle |
| comicwise | Next.js 15 (App) | Radix/shadcn | Zustand | Tailwind | Prisma |
| rhixe_scans | Next.js 15 (App) | Radix/shadcn | Zustand + TanStack | Tailwind | Prisma |
| university-libary-jsm | Next.js 15 (App) | dnd-kit | React Hook Form | Tailwind | Drizzle |
| rhixecompany-comics (FE) | Next.js 16 (App) | MUI | Redux | Tailwind | Prisma |
| xamehi (FE) | React 18 (CRA) | - | Redux | - | - |
| xamehi.tv (FE) | React 17 (CRA) | MUI 4 | Redux | MUI | - |

### Backend (Python)
| Project | Framework | Auth | DB | Async | Deploy |
|---------|-----------|------|----|-------|--------|
| ecom | DRF 3.13 | JWT | PostgreSQL | - | - |
| profile | Django | - | PostgreSQL | - | - |
| Django-Scrapy-Selenium | Django | - | - | Celery | - |
| rhixecompany-comics (BE) | DRF | SimpleJWT | PostgreSQL | Celery | - |
| xamehi (BE) | Django + Express | JWT | - | - | - |
| xamehi.tv | DRF | SimpleJWT + allauth | PostgreSQL | - | Gunicorn |

### Tooling & Automation
| Project | Language | Runtime | Purpose |
|---------|----------|---------|---------|
| Bash | TypeScript | Bun | 6-phase automation orchestrator |
| Resume_maker | TypeScript | Bun | JSON → Markdown/PDF generator |
| selenium_webdriver | JavaScript | Node.js | Chrome scraping |
| youtube-downloader | Python | 3.11 | yt-dlp wrapper |
| Python-projects | Python | 3.11 | 18 beginner scripts |
| mcp-servers | 10 langs | Various | MCP server implementations |

---

## CI/CD Workflows (18 total)

| Workflow | Trigger | Scope |
|----------|---------|-------|
| `pr-ci.yml` | PR to `development` | **Monorepo-aware** — detects changed projects, runs project-specific checks |
| `bash-scripts-ci.yml` | PR touching `projects/Bash/**` | Bun install, shfmt, ShellCheck, TypeScript tests |
| `resume-maker-ci.yml` | PR touching `projects/Resume_maker/**` | TypeCheck, Lint |
| `ci.yml` | Push/PR | Root: bun install, build, test |
| `check-line-endings.yml` | Push/PR to `staged` | CRLF check in markdown |
| `check-plugin-structure.yml` | PR to `staged` | Plugin directory validation |
| `check-pr-target.yml` | PR to `main` | Reject PRs targeting main |
| `codespell.yml` | Push/PR to `staged` | Spelling check |
| `contributors.yml` | Weekly (Sun 3am) | Auto-update contributors |
| `copilot-setup-steps.yml` | Push/PR to workflow file | Copilot CLI setup verification |
| `deploy-website.yml` | Push to `main` (paths) | Astro site build + GitHub Pages |
| `pr-target.yml` | PR opened | Base branch validation |
| `traffic-reporting.yml` | Daily 1am | GitHub traffic stats → webhook |
| `validate-agentic-workflows-pr.yml` | PR to `staged` (workflows/`) | Block compiled workflows, validate .md sources |
| `validate-readme.yml` | PR to `staged` (docs/prompts/) | Auto-generate README, fail if outdated |
| `webhook-caller.yml` | Push to `main` | Fire configured webhooks |

---

## Branch Strategy

```
production (default, protected, auto-published from staged)
    ↑
staged (protected, release candidate)
    ↑
development (working branch, PR target)
    ↑
feature/* (short-lived, deleted after merge)
```

**All 17 projects + root now normalized to `development` + `production` only.** Legacy `chore/workspace-maintenance-20260716` and `master` branches purged July 2025.

---

## Quality Gates

| Gate | Tool | Config |
|------|------|--------|
| TypeScript | `tsc --noEmit` | `tsconfig.json` (strict) |
| Python Lint | `ruff check` | `.ruff.toml` (parent walks) |
| Python Format | `ruff format` | `.ruff.toml` |
| Python Types | `pyright` | `pyrightconfig.json` |
| JS/TS Lint | `eslint` | `eslint.config.mjs` |
| JS/TS Format | `prettier` | `.prettierrc` |
| Markdown Lint | `markdownlint-cli2` | `.markdownlintrc.json` |
| Spelling | `codespell` | `.codespellrc` |
| Shell | `shellcheck` + `shfmt` | `.shellcheckrc` |

---

## Dependency Health (July 2025 Audit)

### Critical Vulnerabilities
| Project | Package | Severity | CVE |
|---------|---------|----------|-----|
| Resume_maker | markdown-pdf | HIGH | GHSA-qghr-877h-f9jh (XSS → local file read) |
| Resume_maker | qs | MODERATE | GHSA-6rw7-vpxm-498p (DoS) |
| Resume_maker | tough-cookie | MODERATE | GHSA-72xf-g2v4-qvf3 (Proto Pollution) |
| Banking | @hono/node-server | MODERATE | GHSA-frvp-7c67-39w9 (Path traversal) |
| Banking | valibot | MODERATE | GHSA-5qjj-4xww-7phc |
| Banking | brace-expansion | MODERATE | GHSA-jxxr-4gwj-5jf2 |

### Outdated Major Versions (Sample)
| Project | Current | Latest | Gap |
|---------|---------|--------|-----|
| ecom | Django 3.1 | 5.1 | 2 major |
| xamehi.tv (FE) | React 17 | 18+ | 1 major |
| xamehi (BE) | Django | 5.x | Unknown |
| profile | Django | 5.x | Unknown |

---

## Disk Usage

| Path | Size |
|------|------|
| `myvenv/` | 393 MB |
| `projects/` | 293 MB |
| `node_modules/` | 30 MB |
| `docs/` | 2.7 MB |
| `uk-earnings-kit/` | 129 KB |
| `earnings-kit/` | 92 KB |

---

## Key Files

| File | Purpose |
|------|---------|
| `AGENTS.md` | Root agent instructions |
| `CLAUDE.md` | Claude Code guidance |
| `.cursorrules` | Cursor IDE rules |
| `.hermes.md` | Hermes Agent project overrides |
| `SESSION_REPORT.md` | Session history |
| `projects/RESEARCH_INDEX.md` | 17-project research index |
| `uk-earnings-kit/UK_EARNING_SITES_MASTER.md` | 346-line UK earning platforms guide |

---

## Active Workstreams (July 2025)

| Priority | Workstream | Status |
|----------|------------|--------|
| P1 | Consolidate `comicwise` + `Django-Scrapy-Selenium` + `selenium_webdriver` → `rhixecompany-comics` | Planning |
| P2 | Branch normalization complete (all 17 projects) | ✅ Done |
| P3 | Ignore file audit — fix all `.*ignore` files | 🔄 In Progress |
| P4 | Dependency audit — upgrade vulnerable/outdated deps | 🔄 In Progress |
| P5 | Bun migration — npm/pnpm → bun for JS/TS repos | Pending |
| P6 | CI workflow setup — GitHub Actions for all repos | 🔄 In Progress |

---

## Agent Configuration (Hermes)

| Profile | Model | Provider | Purpose |
|---------|-------|----------|---------|
| default | deepseek-v4-flash-free | opencode-zen | General |
| code-architect | google/gemma-4-31b-it:free | openrouter | Code/debug/refactor |
| research-analyst | google/gemma-4-31b-it:free | openrouter | Research/synthesis |
| creative-director | google/gemma-4-31b-it:free | openrouter | Design/content |
| exec-assistant | google/gemma-4-31b-it:free | openrouter | Planning/admin |
| patient-tutor | google/gemma-4-31b-it:free | openrouter | Tutorials |
| alexa | google/gemma-4-31b-it:free | openrouter | Operations |

**MCP Servers (16):** ast-grep, code-sandbox, codex, copilot-mcp, fetch, filesystem, github, linear, mcp-docker, memory, mindstudio, playwright, sequential-thinking, smithery, python-quality, tooling-lint, tooling-config