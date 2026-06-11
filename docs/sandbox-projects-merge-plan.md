# Sandbox Projects Migration Plan — rhixecompany-comics

**Target:** `projects/rhixecompany-comics` | Django 5.x + Next.js 16 | 2026-06-01

## Architecture

```
rhixecompany-comics/
├── backend/                    # Django 5.x + DRF + Celery
│   ├── config/                 # Settings, URLs, WSGI, ASGI
│   ├── apps/
│   │   ├── comics/             # Comic models, serializers, views ✅
│   │   ├── api/                # REST router + admin config ✅
│   │   ├── users/              # Custom User model + JWT auth ✅
│   │   ├── core/               # Health check, base views ✅
│   │   └── scraping/           # Scrapy/Selenium scraping (stub)
│   ├── requirements.txt ✅
│   └── manage.py ✅
├── frontend/                   # Next.js 16 App Router
│   ├── src/app/                # Basic layout + page ✅
│   └── package.json ✅
├── docker-compose.yml          # ❌ Not yet
├── .github/workflows/          # ❌ Not yet
└── docs/                       # ✅ Inventory done
```

## Status Summary

| Area | Status | Action Needed |
|------|--------|--------------|
| Backend models | ✅ Migrated from Django-Scrapy-Selenium | None |
| Backend views/serializers | ✅ DRF viewsets + nested serializers | None |
| Backend settings | ✅ Comprehensive config | None |
| Backend scraping | ❌ Stub only | Migrate from selenium_webdriver |
| Frontend components | ❌ Basic scaffold only | Migrate from comicwise |
| Docker | ❌ Missing | Create from Django-Scrapy-Selenium patterns |
| GitHub Actions | ❌ Missing | Create from comicwise patterns |
| Legacy workflows | ❌ Active | Disable/remove comicwise workflows |
| Git branches | ✅ development + production | Sync to remote |

## Migration Order

1. **Frontend migration** — Migrate pages/components/actions from comicwise via OpenCode ACPX
2. **Scraping integration** — Migrate selenium_webdriver scraping into Django management commands
3. **Docker setup** — docker-compose.yml with Django + PostgreSQL + Redis + Celery
4. **GitHub Actions** — Test, lint, deploy workflows
5. **Legacy cleanup** — Disable comicwise-specific workflows
6. **Git sync** — Push branches to remote, clean up stale branches

## Rollback Strategy

- Git branches `development` + `production` provide rollback points
- Source projects preserved until migration verified
- Each migration step is an independent commit

## Risk Notes

- comicwise has 293 npm packages — only migrate needed dependencies
- Frontend auth patterns (NextAuth) differ from backend (JWT) — bridge via DRF API calls
- Docker networking requires careful port mapping for multi-service setup
