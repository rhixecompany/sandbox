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

---

## Key Findings

### Django + Next.js Split
- Use Django for data, auth, admin, and background tasks; Next.js for the public reader and SEO pages; connect through DRF + CORS and SimpleJWT.

### Scrapy + Celery Pipeline
- Scrapy 2.14+ prefers async-first crawlers inside Celery workers; reserve Selenium for login or JS-heavy pages and use Playwright elsewhere.

### Container Production Shape
- Use `output: "standalone"` for Next.js and multi-stage Python builds for Django; run both as non-root and add Compose health checks.

### UI Design System
- shadcn/ui components should be treated as owned code; pair with `drf-spectacular` + `openapi-typescript` for typed API contracts.

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Django 5 docs | https://docs.djangoproject.com/en/5.x | Docs |
| Next.js 16 docs | https://nextjs.org/docs | Docs |
| DRF docs | https://www.django-rest-framework.org | Docs |
| Scrapy async guide | https://www.zyte.com/blog/scrapy-in-2026-modern-async-crawling | Guide |
| shadcn/ui docs | https://ui.shadcn.com | UI docs |
| Celery docs | https://docs.celeryq.dev | Task queue |

---

## Best Practices
1. Keep API types shared between Django and Next.js.
2. Cache hot comic metadata server-side; pre-render listing pages.
3. Run Celery tasks idempotently with retries.
4. Use multi-stage Docker and non-root runtime users.

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Serving media through Django | Slow media delivery | Use CDN + object storage. |
| Deprecated Scrapy hooks | Runtime warnings | Use `async def start()` instead of `start_requests()`. |
| Drifting API contracts | Frontend breakage | Use OpenAPI-generated frontend types. |
| Missing health checks | Startup races | Add Compose health checks. |

---

## Performance
1. RSC reader pages cut client JS and improve SEO.
2. Redis caching for chapter data and Celery queue separation.
3. Image CDN with thumbnail generation in background tasks.
4. ORM query optimization with select/prefetch related.

---

## Security
1. Sanitize all scraped content before render or storage.
2. Use short-lived JWT tokens and validate them in middleware.
3. Keep secrets in environment variables and `.gitignore`.
4. Restrict admin exposure with IP allowlists in production.

---

## Related Projects (in workspace)

- **comicwise** — inherited Next.js reader and DAL patterns
- **Django-Scrapy-Selenium** — inherited Scrapy+Celery+Django patterns
- **selenium_webdriver** — inherited Selenium browser automation utilities
- **rhixe_scans** — comic reader sibling with shared payment and image pipelines
- **cookiecutter-django-tailwind** — shared Django 5.x production template

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
