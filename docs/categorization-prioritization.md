# Categorization & Prioritization

> Generated: 2026-05-30 | Refreshed: live scan

## Priority Tiers

| Tier | Action | Count | Repos |
|------|--------|-------|-------|
| **P1** | Consolidate into rhixecompany-comics | 3 | comicwise (frontend), Django-Scrapy-Selenium (backend), selenium_webdriver (scraper) |
| **P2** | Branch normalization | 1 | comicwise (unrelated history — skip push) |
| **P3** | Standalone maintain | 10 | banking, cookiecutter-django-tailwind, ecom, profile, Python-projects, rhixe_scans, university-libary-jsm, xamehi, xamehi.tv, youtube-downloader |

**Total: 14 repos** (13 source + 1 consolidation target rhixecompany-comics)

## Branch Normalization Status

| Status | Count | Details |
|--------|-------|---------|
| ✅ Clean (production + development on origin, default=production) | 12 | All except comicwise |
| ⚠️ Exception (main only on origin, divergent history) | 1 | comicwise — skip push per repo.prompts.md |
| ✅ Consolidation target (production + development on origin) | 1 | rhixecompany-comics — already wired |

## Working-Tree Dirtiness

| Repo | State | Detail |
|------|-------|--------|
| banking | ❌ 60 staged deletions | `.github/agents/`, `.github/instructions/`, `.github/prompts/` — intentional cleanup |
| cookiecutter-django-tailwind | ⚠️ 1 modified | `AGENTS.md` unstaged |
| selenium_webdriver | ⚠️ 1 untracked | `AGENTS.md` not yet added |
| xamehi | ⚠️ 1 untracked | `AGENTS.md` not yet added |
| All others | ✅ clean | — |

## Consolidation Architecture

### rhixecompany-comics

**Source components:**
- **comicwise** → frontend (Next.js App Router, Prisma, Tailwind, shadcn/ui)
- **Django-Scrapy-Selenium** → backend scaffold (Django REST, Celery, Scrapy)
- **selenium_webdriver** → scraper pipeline (Node.js, Selenium WebDriver)

**Current state (live filesystem):**
| Component | Status | Details |
|-----------|--------|---------|
| Directory | ✅ Created | `projects/rhixecompany-comics/` |
| Git remote | ✅ Created | `Rhixe-company/rhixecompany-comics` |
| Branches | ✅ production + development | Both on origin, default=production |
| Backend | ✅ Populated | Django scaffold: manage.py, config/, apps/, Dockerfile, requirements.txt |
| Frontend | ✅ Populated | Next.js: next.config.ts, prisma/, src/, package.json, Dockerfile |
| Scripts | ✅ Directory | `scripts/scraper/` exists |
| Docker compose | ✅ Created | `docker-compose.yml` |
| Ignore files | ✅ Complete | .gitignore, .dockerignore, .prettierignore, .eslintignore |
| AGENTS.md | ✅ Present | Refreshed |
| Architecture doc | ✅ Exists | `docs/rhixecompany-comics-architecture.md` |

**Remaining work:**
- Verify backend apps have actual content (not just empty dirs)
- Verify frontend src/ is populated (not just scaffold)
- Wire up scraper scripts from selenium_webdriver
- Run verification checks (build, test, lint)
