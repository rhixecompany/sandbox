---
title: "Rhixecompany Comics Plan"
source: "docs/rhixecompany-comics-plan.md"
---

# rhixecompany-comics Migration Plan

> Generated: 2026-05-30 | Refreshed: 2026-05-30
> See also: [Architecture](./rhixecompany-comics-architecture.md) | [Migration Report](./rhixecompany-comics-migration-report.md)

## Current State

| Component | Status | Details |
|-----------|--------|---------|
| Directory | ✅ Created | `projects/rhixecompany-comics/` |
| Git remote | ✅ Created | `Rhixe-company/rhixecompany-comics` |
| Default branch | ✅ production | Set as GitHub default |
| Branches | ✅ production + development | Both pushed to origin |
| Backend | ✅ Populated | Django scaffold with manage.py, config/, apps/, Dockerfile |
| Frontend | ✅ Populated | Next.js with next.config.ts, prisma/, src/, Dockerfile |
| Scripts | ✅ Dir created | `scripts/scraper/` exists |
| Docker Compose | ✅ Present | `docker-compose.yml` |
| .gitignore | ✅ Present | Django + Next.js |
| .dockerignore | ✅ Present | — |
| .prettierignore | ✅ Present | — |
| .eslintignore | ✅ Present | — |
| AGENTS.md | ✅ Present | Written and refreshed |
| RESEARCH_REPORT.md | ✅ Present | Architecture note written |

**Migration steps 1–7 from the original plan are complete.** The remaining focus is verification and integration depth.

## Verification Checklist

- [ ] Backend `python manage.py check --deploy` passes
- [ ] Frontend `npm run build` passes
- [ ] Docker Compose starts all services
- [ ] Prisma schema generates client types
- [ ] Celery task definitions exist
- [ ] Scraper scripts are wired into the pipeline
- [ ] Ignore files cover all source project patterns
- [ ] CI workflows are configured for the new repo

## Remaining Integration Work

| Area | Task | Source |
|------|------|--------|
| Scraping | Copy selenium scripts → `scripts/scraper/src/` | selenium_webdriver |
| Scraping | Create Celery task definitions for scraping | Django-Scrapy-Selenium |
| Backend | Verify apps/ content depth (vs empty scaffold) | Django-Scrapy-Selenium |
| Frontend | Verify src/ content depth (vs initial scaffold) | comicwise |
| Docker | Verify multi-stage Dockerfiles work | — |
| CI | Configure GitHub Actions for consolidated repo | — |

## Rollback

Source projects remain untouched. To roll back: delete `projects/rhixecompany-comics/` and the GitHub repo. The source repos (comicwise, Django-Scrapy-Selenium, selenium_webdriver) still have their original content.
