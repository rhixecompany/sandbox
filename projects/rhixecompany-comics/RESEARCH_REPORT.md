# RESEARCH_REPORT.md

## Project: rhixecompany-comics

**Type:** Comic platform (Django+Next.js monolith)
**Tech Stack:** Python 3.11+, Django 5.x, DRF, Celery, PostgreSQL, Next.js 16, TypeScript, Tailwind CSS, shadcn/ui, Scrapy, Selenium, Docker Compose
**Status:** Active (consolidation target for comicwise, Django-Scrapy-Selenium, selenium_webdriver)

---

## Similar Projects

| Project | Stack | Notes |
|---------|-------|-------|
| fullstack-comic-app (onggiabayluon) | Django REST + Next.js | Manga/webtoon reader, pre-rendering for perf, monorepo layout with django-apis/ + nextjs-comic/ — https://github.com/onggiabayluon/fullstack-comic-app |
| django-nextjs (QueraTeam) | Django + Next.js | Library integrating Next.js pages into Django routing; Django receives initial request and proxies to Next.js renderer — https://github.com/QueraTeam/django-nextjs |
| dockerize-django-with-nextjs | Django + Next.js + Docker | Minimal Docker Compose example for Django+Next.js co-deployment — https://github.com/codingforinnovations/dockerize-django-with-nextjs |

---

## Key Findings

### Django + Next.js Full-Stack (2026 Pattern)
- Django + Next.js is the dominant Python full-stack split in 2026: Django ships admin-heavy MVPs ~3 weeks vs ~5 weeks in Next.js alone; Django's built-in admin, ORM, auth, and permissions have the highest dev ROI for content-heavy platforms (source: buildmvpfast.com/blog/django-vs-nextjs-productivity-framework-comparison-2026)
- Next.js 16 App Router with React Server Components and streaming SSR wins for complex, SEO-critical interactive frontends — Django templates cannot compete for rich client-side experiences (source: wasp.sh/resources/2026/02/24/best-frameworks-web-dev-2026)
- Combine strengths: Django handles data, auth, admin, background tasks; Next.js handles the public-facing RSC reader, comic listings, and SEO pages — wire via DRF + `django-cors-headers` and shared JWT (SimpleJWT)

### Scrapy + Celery Async Pipeline (2026 Upgrade Path)
- Scrapy 2.14.0 (Jan 5, 2026) introduces `AsyncCrawlerProcess` and native coroutine support, replacing legacy Twisted Deferred chains — makes Scrapy play cleanly alongside other asyncio libraries in Django/Celery pipelines (source: zyte.com/blog/scrapy-in-2026-modern-async-crawling)
- `async def start()` replaces the deprecated `start_requests()` in Scrapy 2.13+; `DownloaderAwarePriorityQueue` is now the default scheduler — multi-domain crawls run smoother with zero code changes (source: groupbwt.com/blog/scrapy-tutorial)
- Scrapy 2.14.0 requires Python 3.10+ (3.9 dropped); 60,000+ GitHub stars, 594 contributors — it remains the production standard for high-volume scraping pipelines

### Comic Platform Open-Source Reference
- Successful Django+DRF+Next.js comic sites use a monorepo split (`django-apis/` + `nextjs-comic/`) with DRF handling all data and Next.js using SSR/pre-rendering for chapter reader pages — this maps exactly to the rhixecompany-comics structure (source: github.com/onggiabayluon/fullstack-comic-app)
- `django-nextjs` library allows seamless co-deployment where Django routes requests to Next.js pages; useful for gradual migration or when Django must own the URL namespace (source: github.com/QueraTeam/django-nextjs)

### Docker Compose Production Stack (2026)
- Multi-stage Dockerfiles are mandatory in 2026: Next.js uses `output: "standalone"` + `node:20-alpine` builder pattern; Django uses `python:3.12-slim-bullseye` with non-root user and layered requirements for cache efficiency (source: noqta.tn/en/tutorials/docker-compose-nextjs-postgres-redis-fullstack-2026)
- Production Docker Compose separates dev and prod configs (`docker-compose.yml` + `docker-compose.prod.yml`); Django runs via Gunicorn behind Nginx; health checks and service dependency ordering are essential for reliable startup (source: medium.com/@sizanmahmud08/production-ready-django-with-docker-in-2026)
- Standard 2026 production services: Django (Gunicorn), PostgreSQL 16, Redis 7, Nginx (reverse proxy + static files), Celery worker, Celery beat — all orchestrated via a single Compose file

### shadcn/ui + DRF REST API Patterns (2026)
- shadcn/ui is now "the default design system of the AI era" — it generates components directly into your codebase (no vendor lock-in), is React Server Component-friendly, tree-shakable, and uses Radix primitives for built-in accessibility (source: shadcnspace.com/blog/shadcn-ui-handbook)
- The industry has shifted from "which UI library?" to "UI ownership" — shadcn/ui components become your code, not a dependency; pair with drf-spectacular OpenAPI output and `openapi-typescript` to keep DRF serializers and Next.js types in sync

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Django vs Next.js Productivity 2026 | https://www.buildmvpfast.com/blog/django-vs-nextjs-productivity-framework-comparison-2026 | Comparison |
| Best Full-Stack Frameworks 2026 | https://wasp.sh/resources/2026/02/24/best-frameworks-web-dev-2026 | Survey |
| Scrapy 2.14.0 Async Release | https://www.zyte.com/blog/scrapy-in-2026-modern-async-crawling | Release Notes |
| Scrapy Architecture & Best Practices | https://groupbwt.com/blog/scrapy-tutorial | Guide |
| Docker Compose Next.js+PG+Redis 2026 | https://noqta.tn/en/tutorials/docker-compose-nextjs-postgres-redis-fullstack-2026 | Tutorial |
| Production Django Docker 2026 | https://medium.com/@sizanmahmud08/production-ready-django-with-docker-in-2026-complete-guide-with-nginx-postgresql-and-best-1fb248e65983 | Guide |
| shadcn/ui Handbook 2026 | https://shadcnspace.com/blog/shadcn-ui-handbook | Handbook |
| Django + Next.js 2026 Split Pattern | https://medium.com/@mmoznu/django-next-js-in-2026-when-to-split-your-frontend-and-backend-and-how-to-wire-them-together-23b4ef68b6df | Guide |
| fullstack-comic-app (reference) | https://github.com/onggiabayluon/fullstack-comic-app | OSS Reference |
| django-nextjs library | https://github.com/QueraTeam/django-nextjs | Library |

---

## Best Practices

1. **Scrapy 2.14+ async-first** — Use `async def start()` and `AsyncCrawlerProcess`; integrate with Celery beat for scheduled crawls; use `scrapy-playwright` for JS-heavy comic sources instead of Selenium where possible
2. **Django as the data + auth backbone** — Let Django own ORM, admin, auth, permissions, and Celery tasks; expose only clean DRF endpoints to Next.js; use `drf-spectacular` to auto-generate OpenAPI spec consumed by `openapi-typescript` on the frontend
3. **Next.js 16 RSC for the reader** — Comic listing and chapter reader pages should be React Server Components (zero client JS); use `output: "standalone"` in `next.config.ts` for optimized Docker images
4. **Multi-stage Docker with non-root users** — Both Django (python:3.12-slim) and Next.js (node:20-alpine) containers must use multi-stage builds, non-root runtime users, and separate dev/prod Compose configs with health checks
5. **shadcn/ui as owned code** — Install shadcn/ui components into `frontend/src/components/ui/` and treat them as first-party code; keep form logic outside UI components; use server-safe components in RSC pages and mark interactive ones with `"use client"`

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Serving comic images through Django | Server overload, slow delivery, Django process blocked | S3-compatible storage (R2/MinIO) + CloudFront/Cloudflare CDN for all media |
| Using Scrapy `start_requests()` in 2.13+ | Deprecation warnings, incompatibility with asyncio integrations | Migrate to `async def start()` per Scrapy 2.13+ docs |
| No `output: "standalone"` in Next.js | Bloated Docker image (full node_modules copied), slow builds | Set `output: "standalone"` in `next.config.ts` before containerizing |
| Running containers as root | Security vulnerability, file permission issues in prod | Use non-root user in both Django and Next.js Dockerfiles |
| No caching on comic listings | DB overload on every page load | Redis cache for hot comic/chapter data; Next.js RSC for static pre-render |
| Inconsistent API contracts | Frontend/backend drift | Use `drf-spectacular` OpenAPI + `openapi-typescript` for shared types |
| Missing health checks in Compose | Services start before dependencies are ready | Add `healthcheck` + `depends_on: condition: service_healthy` in docker-compose.yml |
| Selenium for all JS scraping | Slow, resource-heavy, fragile | Migrate JS-heavy targets to `scrapy-playwright`; keep Selenium only for login flows |

---

## Performance

1. **Next.js React Server Components** for comic listings and chapter index pages — zero client JS shipped, full SSR with caching via `cache()` and `revalidate` tags
2. **Scrapy async scheduler** — Scrapy 2.14 `DownloaderAwarePriorityQueue` default improves multi-domain concurrency; set `CONCURRENT_REQUESTS=16` and `DOWNLOAD_DELAY=1.0` for polite production scraping
3. **Image CDN pipeline** — Celery task generates WebP/AVIF thumbnails on upload; serve all comic pages via CDN with `next/image` `loader` prop; never through Django or Gunicorn
4. **Django ORM query discipline** — Use `select_related()` + `prefetch_related()` on comic detail/chapter list views; index `Comic.slug`, `Chapter.number`, `Comic.status` columns in PostgreSQL
5. **Redis layered caching** — Separate Celery queues for scraping, image processing, and notifications; use Redis as Django cache backend for hot comic/chapter data; set appropriate TTLs per content freshness

---

## Security

1. **robots.txt + rate limit compliance** — `ROBOTSTXT_OBEY=True` (Scrapy default); implement `DOWNLOAD_DELAY` and user-agent rotation; verify terms of service before adding new scrape sources
2. **Scraped data sanitization** — Bleach/sanitize all scraped HTML titles, descriptions, and chapter content before storage and before rendering in Next.js to prevent stored XSS
3. **Non-root Docker containers** — Both Django and Next.js production containers run as dedicated non-root users; drop all unnecessary Linux capabilities; read-only root filesystem where possible
4. **JWT + CSRF hygiene** — Django SimpleJWT issues short-lived access tokens (15 min) + refresh tokens; Next.js validates tokens server-side in middleware; Django admin restricted by IP in production via Nginx
5. **Secrets management** — Django `SECRET_KEY`, DB credentials, Redis URL, S3 keys all in environment variables (never committed); use Docker Compose secrets or a vault in production; `.env` files in `.gitignore`

---

## Related Projects (in workspace)

- **comicwise** — consolidation source, inherited Next.js frontend patterns
- **Django-Scrapy-Selenium** — consolidation source, inherited Scrapy+Celery+Django patterns
- **selenium_webdriver** — consolidation source, inherited Selenium utilities
- **rhixe_scans** — comic reader sibling, shared Next.js + Tailwind patterns
- **cookiecutter-django-tailwind** — shared Django 5.x production template

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Django 5 Docs | https://docs.djangoproject.com/en/5.x | Official documentation |
| Next.js 16 Docs | https://nextjs.org/docs | Official documentation |
| DRF Docs | https://www.django-rest-framework.org | REST framework |
| Scrapy 2.14 Docs | https://docs.scrapy.org | Web scraping framework (async release) |
| Scrapy 2.14 Release Notes | https://www.zyte.com/blog/scrapy-in-2026-modern-async-crawling | Async/await crawling standards |
| Playwright Docs | https://playwright.dev | Modern browser automation (Selenium replacement) |
| shadcn/ui Docs | https://ui.shadcn.com | Component library (code-owned) |
| shadcn/ui Handbook 2026 | https://shadcnspace.com/blog/shadcn-ui-handbook | Production patterns & architecture |
| Celery Docs | https://docs.celeryq.dev | Distributed task queue |
| drf-spectacular | https://drf-spectacular.readthedocs.io | OpenAPI schema generation for DRF |
| docker-compose fullstack 2026 | https://noqta.tn/en/tutorials/docker-compose-nextjs-postgres-redis-fullstack-2026 | Next.js + PG + Redis Docker tutorial |
| Production Django Docker 2026 | https://medium.com/@sizanmahmud08/production-ready-django-with-docker-in-2026-complete-guide-with-nginx-postgresql-and-best-1fb248e65983 | Django multi-stage Docker guide |
| fullstack-comic-app (OSS ref) | https://github.com/onggiabayluon/fullstack-comic-app | Django+DRF+Next.js comic platform reference |
| django-nextjs library | https://github.com/QueraTeam/django-nextjs | Django-to-Next.js routing integration |
| Django vs Next.js 2026 | https://www.buildmvpfast.com/blog/django-vs-nextjs-productivity-framework-comparison-2026 | Productivity comparison with real timings |
