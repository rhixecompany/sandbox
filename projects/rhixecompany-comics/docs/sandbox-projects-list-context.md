# Project Inventory: rhixecompany-comics Consolidation

**Generated**: 2026-06-01
**Context**: Consolidation of comicwise, Django-Scrapy-Selenium, selenium_webdriver

## Source Projects

### comicwise (projects/comicwise)
- **Stack**: Next.js 15+, TypeScript, Tailwind CSS, shadcn/ui, Prisma ORM, PostgreSQL
- **Features**: Comic streaming UI, NextAuth v5 auth, Stripe/PayPal payments, UploadThing file uploads, Resend email
- **Inherited by**: frontend/ (design patterns, asset pipeline)
- **Not migrated**: Prisma schema → Django models, NextAuth → DRF JWT, Stripe webhooks

### Django-Scrapy-Selenium (projects/Django-Scrapy-Selenium)
- **Stack**: Django 4.x, DRF, Scrapy, Selenium, Celery, Redis, Webpack+Tailwind
- **Features**: Scrapy spider management, Selenium browser automation, Celery task queue, Tailwind dashboard
- **Inherited by**: backend/ (Django config, DRF patterns, Celery, scraping architecture)
- **Not migrated**: Webpack config (replaced by Next.js), legacy templates, specific Scrapy spiders

### selenium_webdriver (projects/selenium_webdriver)
- **Stack**: Node.js 18+, selenium-webdriver 4.x, ChromeDriver, ES Modules
- **Features**: Comic data scraping, stale-element retry logic, JSON output generation
- **Inherited by**: backend/apps/scraping/ (Selenium logic merged into Django management commands)
- **Not migrated**: Standalone Node.js scripts (scrape.js, scrape2.js, test.js)

## Target Structure

```
projects/rhixecompany-comics/
├── backend/                    # Django 5.x + DRF
│   ├── apps/
│   │   ├── api/               # DRF API (urls, admin)
│   │   ├── comics/            # Comic models, serializers, views
│   │   ├── core/              # Core views, health check
│   │   ├── scraping/          # Scrapy/Selenium integration (management commands, tasks)
│   │   └── users/             # User models, auth endpoints
│   ├── config/                # Django settings, ASGI/WSGI, URLs
│   ├── manage.py
│   └── requirements.txt
├── frontend/                   # Next.js 16 App Router
│   ├── src/
│   │   ├── app/               # Routes: (root)/browse, comics/[slug], search
│   │   ├── components/        # Layout (Header, Footer, Sidebar), UI (shadcn), providers
│   │   └── lib/               # API client, types, utils
│   └── package.json
├── .github/workflows/test.yml # CI: backend lint+test, frontend lint+test
├── docker-compose.yml         # 5 services: db, redis, backend, celery, frontend
├── AGENTS.md
└── README.md
```

## Migration Status

| Component | Source | Target | Status |
|-----------|--------|--------|--------|
| Django config | Django-Scrapy-Selenium | backend/config/ | ✅ Migrated |
| Comic models | comicwise (Prisma) | backend/apps/comics/ | ✅ Created |
| API endpoints | comicwise | backend/apps/api/ | ✅ Created |
| User auth | comicwise (NextAuth) | backend/apps/users/ | ✅ Created |
| Scraping infrastructure | Django-Scrapy-Selenium | backend/apps/scraping/ | ✅ Migrated |
| Frontend pages | comicwise | frontend/src/app/ | ✅ Migrated |
| UI components | comicwise | frontend/src/components/ | ✅ Migrated |
| CI pipeline | New | .github/workflows/test.yml | ✅ Created |
| Docker setup | New | docker-compose.yml | ✅ Created |
| Git branches | New | development, production | ✅ Created |
| Remote origin | - | - | ❌ Not configured |
