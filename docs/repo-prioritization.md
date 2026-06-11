# Categorization & Prioritization Report

> Generated: 2026-05-30 | Refreshed: live scan

## Priority Tiers

| Tier | Action | Repos |
|------|--------|-------|
| P1 | Consolidate into rhixecompany-comics | comicwise, Django-Scrapy-Selenium, selenium_webdriver |
| P2 | Branch normalization (verify/complete) | banking, cookiecutter-django-tailwind, ecom, profile, Python-projects, rhixe_scans, university-libary-jsm, xamehi, xamehi.tv, youtube-downloader |
| P3 | Standalone tooling (maintain) | Python-projects, youtube-downloader |

## Current Branch State

**Already clean (production/development, default=production):** 12/14 repos
banking, cookiecutter-django-tailwind, Django-Scrapy-Selenium, ecom, profile, Python-projects, rhixe_scans, rhixecompany-comics, selenium_webdriver, university-libary-jsm, xamehi, xamehi.tv, youtube-downloader

**Issues:**
1. **comicwise** — remote still has `main` only (no production/development). Divergent history (80 ahead, 69 behind). **Skip push.**
2. **profile** — local dir is `profile` but GitHub remote is `rhixecompany/rhixecompany`. Branch state is clean.
3. **banking** — 60 staged deletions in `.github/` — intentional cleanup, not a problem.
4. **cookiecutter-django-tailwind** — AGENTS.md modified (unstaged)
5. **selenium_webdriver** — AGENTS.md untracked
6. **xamehi** — AGENTS.md untracked

## Working-Tree Health

| Repo | Dirtiness | Detail |
|------|-----------|--------|
| banking | ❌ Dirty | 60 staged deletions (`.github/agents/`, `.github/instructions/`, `.github/prompts/`) |
| cookiecutter-django-tailwind | ⚠️ Modified | `AGENTS.md` unstaged |
| selenium_webdriver | ⚠️ Untracked | `AGENTS.md` not yet added |
| xamehi | ⚠️ Untracked | `AGENTS.md` not yet added |
| All others | ✅ Clean | — |

## Consolidation Targets Analysis

### comicwise (Rhixe-company org)
- Next.js 15+ frontend → source for rhixecompany-comics frontend
- Remote still on `main` only — consolidation will happen via copy, not git merge

### Django-Scrapy-Selenium (Rhixe-company org)
- Django 4 backend with Scrapy + Selenium + Celery
- Has Docker setup
- Source for rhixecompany-comics backend

### selenium_webdriver (rhixecompany user)
- Node.js selenium-webdriver scripts
- Source for rhixecompany-comics scraper pipeline

## Inter-Project Dependencies

| Source Project | Depends On | Notes |
|---------------|-----------|-------|
| rhixecompany-comics | comicwise (frontend patterns) | Design patterns, asset pipeline |
| rhixecompany-comics | Django-Scrapy-Selenium (backend scaffold) | Django config, Celery patterns |
| rhixecompany-comics | selenium_webdriver (scraping) | Scraping utilities |

## rhixecompany-comics Current Status

| Component | Status | Details |
|-----------|--------|---------|
| Directory | ✅ Created | `projects/rhixecompany-comics/` |
| Git initialized | ✅ production + development | Both on origin |
| Remote | ✅ Created | `Rhixe-company/rhixecompany-comics` |
| Default branch | ✅ production | — |
| AGENTS.md | ✅ Written | Refreshed |
| RESEARCH_REPORT.md | ✅ Written | Current |
| .gitignore | ✅ Present | Django + Next.js combined |
| .dockerignore | ✅ Present | — |
| .prettierignore | ✅ Present | — |
| .eslintignore | ✅ Present | — |
| Backend | ✅ Populated | Django scaffold: manage.py, config/, apps/, Dockerfile |
| Frontend | ✅ Populated | Next.js: next.config.ts, prisma/, src/, Dockerfile |
| Scripts | ✅ Present | `scripts/scraper/` directory |
| Docker compose | ✅ Present | docker-compose.yml with all services |

## Next Steps
1. Run verification checks on rhixecompany-comics (build, lint, test)
2. Verify source repos are still useful or can be archived
3. Commit/clean up dirty working trees (AGENTS.md changes)
4. Document comicwise as archived source (skip push)
