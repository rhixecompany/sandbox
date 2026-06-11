# rhixecompany-comics Architecture

Generated: 2026-05-30 | Refreshed: 2026-05-30
Phase: 3 — Target architecture design

> **NOTE:** This document describes the **target architecture** for the fully consolidated project.
> Some parts (Docker setup, ignore files, directory structure) are already in place; others (specific app models, auth bridge, scraping pipeline) are aspirational and will be built incrementally.
> See **[rhixecompany-comics-plan.md](./rhixecompany-comics-plan.md)** for current-state vs remaining-work tracking.
> See **[rhixecompany-comics-migration-report.md](./rhixecompany-comics-migration-report.md)** for execution status and verification gates.

## Overview

Consolidation of three repositories into a single monorepo:
- **comicwise** → frontend (Next.js 15+ App Router)
- **Django-Scrapy-Selenium** → backend (Django 5 REST API)
- **selenium_webdriver** → scraping pipeline (Node.js Selenium scripts)

## Target Directory Layout

```
projects/rhixecompany-comics/
├── .git/                       # Git repo (production / development branches)
├── .gitignore                  # Combined Django + Next.js ignore
├── .dockerignore               # Docker build ignore
├── .prettierignore             # Prettier ignore
├── .eslintignore               # ESLint ignore
├── docker-compose.yml          # Full stack compose
├── Dockerfile.backend          # Multi-stage Django build
├── Dockerfile.frontend         # Multi-stage Next.js build
├── Dockerfile.scraper          # Node + Selenium image
├── README.md
├── AGENTS.md                   # Already exists
├── docs/
│   ├── architecture.md         # This file
│   ├── migration-plan.md       # Step-by-step migration
│   └── api-reference.md
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── rhixecompany/           # Django project root
│   │   ├── __init__.py
│   │   ├── settings/
│   │   │   ├── base.py
│   │   │   ├── dev.py
│   │   │   └── prod.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── apps/
│   │   ├── api/                # DRF viewsets, routers, serializers
│   │   ├── comics/             # Core domain models
│   │   ├── authentication/     # JWT auth (NextAuth-compatible)
│   │   └── scraping/           # Scrapy + Celery orchestration
│   └── celery/
│       ├── __init__.py
│       ├── celery.py
│       └── tasks/
│           ├── scrape.py       # Scraping task definitions
│           └── image_process.py
├── frontend/
│   ├── next.config.mjs
│   ├── tsconfig.json
│   ├── tailwind.config.ts
│   ├── package.json
│   ├── src/
│   │   ├── app/                # Next.js App Router
│   │   │   ├── layout.tsx
│   │   │   ├── page.tsx
│   │   │   ├── auth/           # Auth pages + server actions
│   │   │   └── comics/         # Comic browsing routes
│   │   ├── components/         # shadcn/ui components
│   │   ├── lib/
│   │   │   └── api/            # API client wrappers
│   │   └── server-actions/     # Server actions
│   └── prisma/
│       └── schema.prisma       # Shared type definitions
└── scripts/
    └── scraper/
        ├── package.json
        ├── tsconfig.json
        └── src/
            ├── spiders/        # Selenium scrapers
            └── utils/          # Utilities
```

## Backend Architecture

### Django REST API (adapted from Django-Scrapy-Selenium)

- **Framework**: Django 5 + DRF
- **Auth**: JWT tokens (compatible with NextAuth v5)
- **Workers**: Celery + Redis for async tasks
- **Scraping**: Scrapy spiders managed via Celery Beat
- **Database**: PostgreSQL via Django ORM

### Key Models
| Model | Source | Purpose |
|-------|--------|---------|
| Comic, Issue, Author | comicwise Prisma schema | Core content models |
| User, Subscription | comicwise NextAuth | User management |
| ScrapeSource, ScrapeResult | New | Scraping pipeline tracking |
| Celery Task Results | New | Async task monitoring |

## Frontend Architecture

### Next.js 15+ App Router (adapted from comicwise)

- **Framework**: Next.js 15+ with Turbopack
- **UI**: Tailwind CSS + shadcn/ui components
- **Auth**: NextAuth v5 (credentials provider → Django JWT)
- **Payments**: Stripe/PayPal (frontend-hosted checkout)
- **Data Fetching**: Server Components + Server Actions

### Auth Flow
1. User signs in via NextAuth credentials provider
2. NextAuth calls Django `/api/auth/token/` for JWT
3. Access tokens stored in httpOnly cookies
4. Refresh flow via Django `/api/auth/refresh/`

## Scraping Pipeline

### Architecture
1. **Celery Beat** schedules periodic scrape tasks
2. **Celery Worker** receives task, spawns Node.js Selenium script
3. **Node Script** (from selenium_webdriver) scrapes target site
4. **Output** written as JSON, consumed by Django for DB upsert
5. **Post-processing**: Image compression, storage via S3/GCS

### Flow
```
Celery Beat → Celery Worker → subprocess Node.js Selenium → JSON → Django ORM → PostgreSQL
```

## Database Strategy

### Prisma ↔ Django ORM Bridge
- **Prisma schema** = source of truth for frontend types
- **Django ORM** = source of truth for backend operations
- **UUID primary keys** used throughout for compatibility
- **Sync**: After Prisma migrations, run Django `inspectdb` or manual model alignment
- **Writes**: Always through Django API
- **Reads**: Frontend uses Prisma types for type safety

## Docker Setup

### Services
1. **PostgreSQL 16** — Primary database
2. **Redis 7** — Celery broker + cache
3. **Django Backend** — Gunicorn + ASGI
4. **Next.js Frontend** — Node.js dev/prod server
5. **Celery Worker** — Async task processing
6. **Celery Beat** — Scheduled scraping

### compose.yml
```yaml
services:
  db:      (postgres:16-alpine)
  redis:   (redis:7-alpine)
  backend: (Dockerfile.backend, depends_on: [db, redis])
  frontend:(Dockerfile.frontend, depends_on: [backend])
  worker:  (same image as backend, command: celery worker)
  beat:    (same image as backend, command: celery beat)
```

## Ignore Files

### .dockerignore
```
node_modules/
.git/
.env*
*.md
.venv/
__pycache__/
*.pyc
.next/
out/
dist/
coverage/
.gitignore
```

### .prettierignore
```
node_modules/
.next/
out/
dist/
build/
coverage/
*.min.*
*.pyc
.venv/
```

### .eslintignore
```
node_modules/
.next/
out/
dist/
build/
coverage/
*.config.*
.next/
```

## Git Workflow

### Branch Strategy
- **production**: Default branch, stable releases
- **development**: Active development, PRs merge here
- Feature branches from development → PR → development → production

### Setup
1. `production` = GitHub default branch
2. `development` = active checkout, branched from production
3. Delete all other branches
