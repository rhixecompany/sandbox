# Merge Plan: rhixecompany-comics Consolidation

**Generated**: 2026-06-01
**Status**: EXECUTED — plan is historical record

## Target Architecture

```
┌─────────────────────────────────────────────────┐
│               rhixecompany-comics               │
├──────────────────┬──────────────────────────────┤
│   Backend (Django 5.x + DRF)                    │
│   ├── apps/api      — REST API endpoints         │
│   ├── apps/comics   — Comic models + business     │
│   ├── apps/core     — Health/utility endpoints    │
│   ├── apps/scraping — Scrapy + Selenium tasks     │
│   └── apps/users    — Auth + user management      │
├──────────────────┼──────────────────────────────┤
│   Frontend (Next.js 16 App Router)               │
│   ├── browse/         — Browse comics             │
│   ├── comics/[slug]   — Comic detail + reader     │
│   ├── search/         — Search comics             │
│   └── components/     — shadcn/ui + layout        │
├──────────────────┴──────────────────────────────┤
│   Infra: Docker Compose (PostgreSQL, Redis,      │
│          Celery worker)                           │
│   CI: GitHub Actions (lint + test per commit)    │
└──────────────────────────────────────────────────┘
```

## Module Ownership Boundaries

| Layer | Django App / Dir | Ownership | Inherited From |
|-------|-----------------|-----------|---------------|
| API | `apps/api` | REST endpoints, URL routing | Django-Scrapy-Selenium patterns |
| Comics | `apps/comics` | Models, serializers, views | comicwise (Prisma → Django ORM) |
| Scraping | `apps/scraping` | Spiders, Selenium, Celery tasks | Django-Scrapy-Selenium + selenium_webdriver |
| Auth | `apps/users` | User model, JWT auth | comicwise (NextAuth → DRF JWT) |
| Frontend | `frontend/` | Pages, components, API client | comicwise (Next.js 15 → 16) |

## Migration Order (Historical)

1. **Phase 1** (May 29-30): Scaffold — Django + Next.js 16 base, docker-compose, CI
2. **Phase 2** (May 30): Consolidation — merge comicwise frontend + Django-Scrapy-Selenium backend + selenium_webdriver scraping

## Branch Strategy

| Branch | Base | Purpose | Active | Default |
|--------|------|---------|--------|---------|
| `development` | scaffold + consolidation | Active development branch | ✅ | - |
| `production` | scaffold only | Stable release branch | - | ✅ |

## Rollback Strategy

- **Code rollback**: `git revert 42a77c5` restores scaffold-only state
- **Full undo**: `git checkout production && git branch -D development` then recreate from production
- **Source preservation**: Source projects remain in `projects/` until Phase 5 archive

## What Was Retired

| Component | Reason |
|-----------|--------|
| comicwise Prisma ORM | Replaced by Django ORM (consistent backend) |
| comicwise NextAuth | Replaced by DRF JWT (single auth system) |
| Django-Scrapy-Selenium Webpack | Replaced by Next.js build system |
| Django-Scrapy-Selenium templates | Replaced by Next.js App Router |
| selenium_webdriver standalone scripts | Merged into Django management commands |

## Remaining Work

- [ ] Configure remote origin for GitHub
- [ ] Install frontend dependencies and verify build
- [ ] Install backend dependencies and verify migration
- [ ] Run CI pipeline against development branch
- [ ] Set `production` as default branch in GitHub Settings
