# Repository Summary — `rhixecompany-comics`

> Generated from real local git history on 2026-07-16. All facts are evidence-based
> (commit hashes, dates, file names) and were not invented.

## Overview

`rhixecompany-comics` is a **dual-stack comics platform** — a Django 4.x + DRF backend
combined with a Next.js 16 frontend — maintained by **rhixecompany**. It is the only one of
the five sibling repos with **6 commits** (the others have 5), because it carries two extra
housekeeping commits ("updates" and "sync workspace artifacts"). It is explicitly described
in `architecture.md` as a *consolidation* of scraping/automation patterns inherited from
sibling repos (`selenium_webdriver`, `Django-Scrapy-Selenium`).

The working tree holds a functional scaffold: a `backend/` Django app (entry point,
settings, a health endpoint), a `frontend/` Next.js 16 shell, `scripts/`, `docs/`,
`docker-compose.yml`, and the usual generated guides plus `RESEARCH_REPORT.md` and
`web-research-rhixecompany-comics.md` (29 KB).

## Architecture

- **Type:** Dual-stack web platform (Django backend + Next.js frontend), two independent
  stacks sharing a PostgreSQL database, Celery for async tasks.
- **Backend:** Django 4.x + Django REST Framework, Python 3.10+; PostgreSQL; Celery + Redis.
- **Frontend:** Next.js 16 App Router, TypeScript (strict), Server Components by default.
- **API:** `/api/` on both stacks; health endpoint present now.
- **Scraping layer:** `backend/apps/scraping/` reserves the Django home for Scrapy spiders
  and Selenium-backed browser tasks (patterns from `selenium_webdriver`).
- **Infra:** Docker Compose; Redis for Celery broker/result.

## Key Components

| Path | Role |
|------|------|
| `backend/` | Django + DRF backend (apps: comics, users, core, scraping) |
| `frontend/` | Next.js 16 App Router shell (`frontend/src/app/layout.tsx`) |
| `scripts/` | Automation/tooling scripts |
| `docs/` | Architecture & workflow docs |
| `docker-compose.yml` | Multi-service orchestration |
| `.env.example` / `.dockerignore` / `.editorconfig` | Config templates |
| `architecture.md`, `technology-stack.md`, `tech-stack.md`, `folder-structure.md` | Generated guides |
| `copilot-instructions.md`, `code-exemplars.md`, `cross-linking-report.md`, `execution-summary.md`, `validation-report.md`, `project-workflow.md` | Generated docs |
| `RESEARCH_REPORT.md` / `web-research-rhixecompany-comics.md` | Research dossiers |

## Technologies

- **Backend:** Django 4.x, Django REST Framework, Python 3.10+
- **Frontend:** Next.js 16, TypeScript (strict)
- **Async:** Celery + Redis
- **Database:** PostgreSQL (shared)
- **Infra:** Docker Compose
- **Inheritance:** Scrapy + Selenium patterns from sibling repos
- **Tooling:** ruff/mypy (backend), ESLint/Prettier (frontend), VS Code (`.vscode/`, `.github/`)

## Data Flow

```
Browser → Next.js frontend → Django API (/api/) → Domain apps (comics/users/core) → PostgreSQL
                                └→ Scraping workers (Scrapy/Selenium) → External comic sources
```

## Team

| Contributor | Commits | Role |
|-------------|---------|------|
| `rhixecompany` <rhixecompany@gmail.com> | 6 / 6 (100%) | Sole author — setup, sync, config, docs, research reports |

**Bus factor:** 1. All 6 commits were authored by a single contributor;
no co-authors, merges, or external PRs.
