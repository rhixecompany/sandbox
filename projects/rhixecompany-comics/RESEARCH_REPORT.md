## Project: rhixecompany-comics
**Type:** Comic platform (Django+Next.js monolith)
**Tech Stack:** Python 3.11+, Django 5.x, DRF, Celery, PostgreSQL, Next.js 16, TypeScript, Tailwind CSS, shadcn/ui, Scrapy, Selenium, Docker Compose
**Status:** Active (consolidation target for comicwise, Django-Scrapy-Selenium, selenium_webdriver)

## Similar Projects
| Project | URL | Why Relevant |
|---------|-----|--------------|
| fullstack-comic-app (onggiabayluon) | https://github.com/onggiabayluon/fullstack-comic-app | Manga/webtoon reader with monorepo Django+Next.js layout. |
| django-nextjs (QueraTeam) | https://github.com/QueraTeam/django-nextjs | Django-to-Next.js routing integration. |
| dockerize-django-with-nextjs | https://github.com/codingforinnovations/dockerize-django-with-nextjs | Minimal Django+Next.js Compose example. |
| comicwise | `projects/comicwise` | Inherited Next.js reader and DAL patterns. |
| Django-Scrapy-Selenium | `projects/Django-Scrapy-Selenium` | Inherited Scrapy+Celery+Django patterns. |
| selenium_webdriver | `projects/selenium_webdriver` | Inherited Selenium browser automation utilities. |

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

## Cheatsheets & Quick Reference
| Topic | Resource | Type |
|-------|----------|------|
| Django + Next.js 2026 | https://medium.com/@mmoznu/django-next-js-in-2026-when-to-split-your-frontend-and-backend-and-how-to-wire-them-together-23b4ef68b6df | Guide |
| Django Celery background tasks | https://oneuptime.com/blog/post/2026-01-26-django-celery-background-tasks/view | Guide |

## Best Practices
1. **Shared OpenAPI types** — `drf-spectacular` → `openapi-typescript` → typed fetch client; CI fails on contract drift
2. **Queue isolation** — `critical`/`default`/`bulk` queues with dedicated workers; prevents scraper batch from blocking user requests
3. **Idempotent scraper tasks** — deduplication key = `sha256(url + timestamp_bucket)`; skip if exists
4. **Next.js Server Components for reader** — zero client JS, ISR with 60s revalidate, SEO-friendly

## Common Pitfalls
| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Serving media through Django | Slow media, worker starvation | CDN + object storage (GCS/S3); signed URLs |
| Deprecated Scrapy hooks | Runtime warnings, breakage | Use `async def start()` instead of `start_requests()` |

## Performance
1. **RSC reader pages** cut client JS bundle >60%; improves SEO, FCP, LCP
2. **Redis caching** for chapter data, comic metadata — TTL 10min via `django-redis`
3. **Image CDN** with thumbnail generation in Celery background tasks (Pillow → WebP)

## Security
1. **Sanitize all scraped content** — `bleach` + `lxml.html.clean` before render/storage; strip scripts, iframes
2. **Short-lived JWT** — 15min access, 7d refresh; validate in Next.js middleware + Django DRF
3. **Secrets in environment** — `.gitignore` + secret manager; never in Docker Compose

## Related Projects (in workspace)
- **comicwise** — inherited Next.js reader and DAL patterns
- **Django-Scrapy-Selenium** — inherited Scrapy+Celery+Django patterns
- **selenium_webdriver** — inherited Selenium browser automation utilities
- **rhixe_scans** — comic reader sibling with shared payment and image pipelines
- **cookiecutter-django-tailwind** — shared Django 5.x production template
- **Banking** — Next.js + Drizzle auth/security patterns
- **university-libary-jsm** — Next.js + Drizzle + Neon serverless patterns

## Resources
| Resource | URL | Description |
|----------|-----|-------------|
| Django 5 docs | https://docs.djangoproject.com/en/5.x | Official docs |
| Next.js 16 docs | https://nextjs.org/docs | Official docs |
