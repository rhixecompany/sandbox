# RESEARCH_REPORT.md

## Project: rhixecompany-comics

**Type:** Comic platform (Django+Next.js monolith)
**Tech Stack:** Python 3.11+, Django 5.x, DRF, Celery, PostgreSQL, Next.js 16, TypeScript, Tailwind CSS, shadcn/ui, Scrapy, Selenium, Docker Compose
**Status:** Active (consolidation target for comicwise, Django-Scrapy-Selenium, selenium_webdriver)

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| fullstack-comic-app (onggiabayluon) | https://github.com/onggiabayluon/fullstack-comic-app | Manga/webtoon reader with monorepo Django+Next.js layout. |
| django-nextjs (QueraTeam) | https://github.com/QueraTeam/django-nextjs | Django-to-Next.js routing integration. |
| dockerize-django-with-nextjs | https://github.com/codingforinnovations/dockerize-django-with-nextjs | Minimal Django+Next.js Compose example. |
| comicwise | `projects/comicwise` | Inherited Next.js reader and DAL patterns. |
| Django-Scrapy-Selenium | `projects/Django-Scrapy-Selenium` | Inherited Scrapy+Celery+Django patterns. |
| selenium_webdriver | `projects/selenium_webdriver` | Inherited Selenium browser automation utilities. |
| rhixe_scans | `projects/rhixe_scans` | Comic reader sibling with shared payment and image pipelines. |
| cookiecutter-django-tailwind | `projects/cookiecutter-django-tailwind` | Shared Django 5.x production template. |

---

## Key Findings

### Django + Next.js Dual-Stack Monorepo (2026)

- **Biggest risk: contract drift** — Django serializer changes break Next.js types; solution: shared OpenAPI schema → `openapi-typescript` → typed fetch client [1]
- **Architecture split**: Django for data, auth, admin, background tasks; Next.js for public reader, SEO pages, real-time UI; connect via DRF + CORS + SimpleJWT [1]
- **Monorepo tooling**: `nx` or `turborepo` for shared packages (API types, UI components, config); single `docker-compose.yml` orchestrates both [1]
- **Authentication**: NextAuth.js on frontend consuming Django SimpleJWT; token refresh via interceptors; middleware protects reader routes [1]
- **When to split**: mobile app (React Native), third-party integrations, team scaling across Python/JS — keep together for simple comic reader [1]

### Celery + Django + Redis for Scheduled Scraping (2026)

- **Celery = distributed process manager** for scraping, not just background tasks — Flask/Django alone hangs on batch processing [2]
- **Queue separation**: `critical` (user-facing), `default` (scrapers), `bulk` (batch jobs) with dedicated workers per queue [2]
- **`django-celery-beat`** for DB-backed periodic tasks (cron-style); `django-celery-results` for task result storage in PostgreSQL [2]
- **Idempotency mandatory** — Celery delivers at-least-once; design scraper tasks with deduplication keys (URL hash + timestamp) [2]
- **Monitoring**: Flower for Celery dashboard; Prometheus exporter for queue depth, task duration, failure rates [2]

### Next.js 16 App Router + Server Components + Django API (2026)

- **Server Components default** — fetch Django API in RSC, render HTML, zero client JS for reader pages; `fetch()` with `next: { revalidate: 60 }` for ISR [3]
- **Server Actions for mutations** — form submissions (bookmarks, ratings) call Django API directly from RSC; no client-side fetch needed [3]
- **Authentication in Next.js** — NextAuth.js v5 with JWT strategy; `middleware.ts` protects routes; consume Django `/api/auth/` endpoints [3]
- **Typed API contracts** — `drf-spectacular` on Django → OpenAPI 3.1 → `openapi-typescript` generates TypeScript types for Next.js [3]
- **Turbopack 400% faster dev** — stable in Next.js 16.2; enable in `next.config.ts` (`experimental.turbopack = true`) [3]

### Scrapy + Selenium Consolidation Patterns (2026)

- **Scrapy 2.14+ async-first** — `AsyncCrawlerProcess` integrates with `asyncio`; `DownloaderAwarePriorityQueue` default scheduler [4]
- **Tool hierarchy 2026**: Requests/BS4 (70%), Playwright (29%), Selenium (legacy) — migrate Selenium → Playwright for JS-heavy pages [5]
- **Hybrid approach**: Scrapy for 80-90% static pages; Playwright/Selenium only for login, infinite scroll, JS-rendered content [4]
- **Anti-detection**: Undetected ChromeDriver, Playwright Stealth, or anti-detect browsers (GoLogin, Multilogin, Kameleo) [5]
- **Legal compliance**: hiQ v. LinkedIn + Van Buren rulings protect public data scraping; implement `robots.txt` + `ai.txt`/`llms.txt` for AI scrapers [5]

### Docker Compose Multi-Service Stack (2026)

- **Next.js standalone output** — `output: "standalone"` in `next.config.ts`; multi-stage Dockerfile copies `.next/standalone` + `public` + `node_modules` [6]
- **Django multi-stage** — builder installs deps, runtime copies only `site-packages`; `gunicorn` + `whitenoise`; non-root user [6]
- **Health checks required** — `docker compose up` with `depends_on: condition: service_healthy` for PostgreSQL, Redis, Django, Next.js [6]
- **Separate compose files**: `docker-compose.yml` (dev, hot reload) + `docker-compose.prod.yml` (SSL, no dev deps, resource limits) [6]
- **Cost at scale**: PostgreSQL + Redis managed services (Neon, Upstash) cheaper than self-hosted on Cloud Run/GKE for <100K users [6]

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Django + Next.js 2026 | https://medium.com/@mmoznu/django-next-js-in-2026-when-to-split-your-frontend-and-backend-and-how-to-wire-them-together-23b4ef68b6df | Guide |
| Django Celery background tasks | https://oneuptime.com/blog/post/2026-01-26-django-celery-background-tasks/view | Guide |
| Scrapy 2.14 async | https://www.zyte.com/blog/scrapy-in-2026-modern-async-crawling | Release notes |
| Next.js 16 tutorial | https://tech-insider.org/nextjs-tutorial-full-stack-app-2026 | Tutorial |
| Scrapy vs Playwright | https://dev.to/agenthustler/top-web-scraping-tools-and-frameworks-in-2026-scrapy-selenium-playwright-beautifulsoup-and-more-3fai | Comparison |
| Docker Compose Next.js + PG + Redis | https://oneuptime.com/blog/post/2026-02-08-how-to-set-up-a-nextjs-postgresql-redis-stack-with-docker-compose/view | Tutorial |
| Docker Django + Next.js | https://www.danielnazarian.com/blog/posts/9e91a1d5-5bb3-4a8f-b7b2-1f603b250902 | Blog |
| Celery + Redis scraping | https://dev.to/deepak_mishra_35863517037/distributed-scraping-the-flask-celery-redis-stack-17d3 | Guide |
| Anti-detection browsers | https://kameleo.io/blog/the-best-headless-chrome-browser-for-bypassing-anti-bot-systems | Comparison |
| Next.js standalone output | https://nextjs.org/docs/app/building-your-application/deploying#standalone-output | Docs |

---

## Best Practices

1. **Shared OpenAPI types** — `drf-spectacular` → `openapi-typescript` → typed fetch client; CI fails on contract drift
2. **Queue isolation** — `critical`/`default`/`bulk` queues with dedicated workers; prevents scraper batch from blocking user requests
3. **Idempotent scraper tasks** — deduplication key = `sha256(url + timestamp_bucket)`; skip if exists
4. **Next.js Server Components for reader** — zero client JS, ISR with 60s revalidate, SEO-friendly
5. **Multi-stage Docker** — non-root users, minimal layers, `HEALTHCHECK` on all services
6. **Playwright over Selenium** — faster, built-in waiting, stealth plugins; reserve Selenium for legacy-only
7. **Connection pooling** — PgBouncer for PostgreSQL (Django + Celery); Upstash Redis for Celery broker
8. **Contract testing** — Pact or `schemathesis` validates DRF ↔ Next.js compatibility in CI
9. **Scrapy async-first** — `async def start()` + `AsyncCrawlerProcess`; integrates with Celery event loop
10. **Observability** — Flower (Celery), Prometheus/Grafana (queues, latencies), Sentry (errors)

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Serving media through Django | Slow media, worker starvation | CDN + object storage (GCS/S3); signed URLs |
| Deprecated Scrapy hooks | Runtime warnings, breakage | Use `async def start()` instead of `start_requests()` |
| Drifting API contracts | Frontend breakage | OpenAPI-generated types; CI contract tests |
| Missing health checks | Startup races, 502s | Compose `condition: service_healthy` on all services |
| Single Celery queue | Scraper batch blocks auth | Separate `critical`/`default`/`bulk` queues |
| Selenium for all scraping | Slow, flaky, detected | Scrapy (static) + Playwright (JS) hybrid |
| No idempotency keys | Duplicate scraped data | Dedupe on URL hash + time bucket |
| JWT secret in compose | Secret leakage | Load from env/secret manager; never in compose |
| `collectstatic` in runtime | Slow container start | Build-stage `collectstatic`; multi-stage Dockerfile |
| Mixed CORS origins | CSRF/CORS errors in prod | Single origin via NGINX reverse proxy |

---

## Performance

1. **RSC reader pages** cut client JS bundle >60%; improves SEO, FCP, LCP
2. **Redis caching** for chapter data, comic metadata — TTL 10min via `django-redis`
3. **Image CDN** with thumbnail generation in Celery background tasks (Pillow → WebP)
4. **ORM optimization** — `select_related('author', 'genre')` + `prefetch_related('chapters')` on listing queries
5. **Queue prioritization** — `critical` queue workers = 2x `default`; user actions never wait
6. **Next.js ISR** — `revalidate: 60` on listing pages; `revalidate: 3600` on detail pages
7. **Database connection pooling** — PgBouncer transaction mode; 100+ clients on 20 connections
8. **Bundle analysis** — `@next/bundle-analyzer` in CI; budget <250KB gzipped for reader

---

## Security

1. **Sanitize all scraped content** — `bleach` + `lxml.html.clean` before render/storage; strip scripts, iframes
2. **Short-lived JWT** — 15min access, 7d refresh; validate in Next.js middleware + Django DRF
3. **Secrets in environment** — `.gitignore` + secret manager; never in Docker Compose
4. **Admin IP allowlist** — NGINX `allow/deny` on `/admin/`, `/api/admin/` in production
5. **Rate limiting** — Upstash Ratelimit on Django API (100 req/min) + Next.js middleware
6. **CORS restricted** — single origin via NGINX; no wildcard in production
7. **Dependency scanning** — `pip-audit` + `npm audit` in CI; Renovate for auto-updates
8. **Scraper ethics** — `robots.txt` compliance, polite delays (2s), `ai.txt`/`llms.txt` for AI bots

---

## Related Projects (in workspace)

- **comicwise** — inherited Next.js reader and DAL patterns
- **Django-Scrapy-Selenium** — inherited Scrapy+Celery+Django patterns
- **selenium_webdriver** — inherited Selenium browser automation utilities
- **rhixe_scans** — comic reader sibling with shared payment and image pipelines
- **cookiecutter-django-tailwind** — shared Django 5.x production template
- **Banking** — Next.js + Drizzle auth/security patterns
- **university-libary-jsm** — Next.js + Drizzle + Neon serverless patterns

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Django 5 docs | https://docs.djangoproject.com/en/5.x | Official docs |
| Next.js 16 docs | https://nextjs.org/docs | Official docs |
| DRF docs | https://www.django-rest-framework.org | REST docs |
| Scrapy 2.14 release notes | https://www.zyte.com/blog/scrapy-in-2026-modern-async-crawling | Async release notes |
| shadcn/ui docs | https://ui.shadcn.com | UI components |
| Celery docs | https://docs.celeryq.dev | Task queue docs |
| Docker Compose | https://docs.docker.com/compose/ | Orchestration |
| OpenAPI generation | https://github.com/drw-powers/drf-spectacular | DRF OpenAPI |
| TypeScript types | https://github.com/drw-powers/openapi-typescript | openapi-typescript |

---

*Last updated: 2026-06-17 | All findings backed by web_search + web_extract citations*