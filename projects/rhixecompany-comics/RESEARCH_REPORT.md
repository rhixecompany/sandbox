# RESEARCH_REPORT — rhixecompany-comics

> **Type:** Project research report | **Updated:** 2026-07-16

**Type:** Dual-stack comics platform (Django 5.x + Next.js 16)
**Tech Stack:** Django 5.x, DRF, Next.js 16, React 19, Tailwind 4, Celery + Redis, Scrapy, Selenium, PostgreSQL, Docker
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| Django + Next.js template | <https://github.com/nynvr/django-nextjs-postgresql-template> | Django 5.1 + DRF 3.15 + Next.js 15 + Docker |
| Unfold Turbo | <https://github.com/unfoldadmin/turbo> | Django & Next.js boilerplate |

---

## Key Findings

### Django + Next.js Dual-Stack Architecture (2026)
- **Biggest risk**: API field drift — maintain OpenAPI spec; generate TypeScript types
- Django at `/api/`, Next.js at frontend domain; CORS via `django-cors-headers` v4.9+
- Server Actions eliminate boilerplate API routes — they're the "API Route Killer"
- Predicted 2026 default stack for AI-ready enterprise platforms

### Next.js 16 + React 19
- **Server Components by default**; Client Components only for interactive UI
- **Turbopack ~400% faster** dev vs webpack; enable `output: 'standalone'` for Docker
- Server Actions simplify form handling without extra API endpoints
- Interleave Server/Client Components via `children` prop pattern

### Celery + Redis Production Settings
- **Critical**: `task_acks_late=True`, `task_reject_on_worker_lost=True`, `worker_prefetch_multiplier=1`
- `broker_transport_options = {'visibility_timeout': 3600}` — must exceed longest task
- Queue separation: dedicated queues for high-priority vs bulk scraping
- `django-celery-beat` for DB-backed periodic task scheduling

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Next.js 16 + Docker | <https://nextjs.org/docs/app/guides/advanced#standalone> | Guide |
| Celery prod settings | <https://docs.celeryq.dev/en/stable/userguide/configuration.html> | Docs |
| Scrapy Django Integration | <https://docs.scrapy.org/en/latest/topics/django> | Guide |

---

## Best Practices

1. **OpenAPI spec as source of truth** — generate TS types from DRF schema to prevent API drift
2. **Server Actions for mutations** — reduce API route boilerplate
3. **Celery queue separation** — dedicated queues for scraping vs content processing
4. **Scrapy for static, Celery for scheduling** — spiders as tasks, not views
5. **Tailwind 4 CSS-first** — `@import "tailwindcss"` + `@theme` directive; no config file

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| API field drift | Frontend breaks | OpenAPI spec + auto-generated TS types |
| Missing Celery ack_late | Lost tasks on crash | `task_acks_late=True` in settings |
| Server Actions in Client Components | Runtime errors | Server Actions in Server Components only |
| Tailwind 3 → 4 config migration | Build breaks | `@import "tailwindcss"` API; no `tailwind.config.js` |

---

## Performance

1. **Turbopack + standalone output** — faster builds, smaller Docker images
2. **Celery worker concurrency** — `CPU*2+1` for I/O-bound scraping workloads
3. **Next.js Partial Prerendering** — static shell + dynamic content streams
4. **Django connection pooling** — `CONN_MAX_AGE` for production PostgreSQL
5. **Redis caching** — cache frequent DB queries at the Django ORM layer

---

## Security

1. **Strict CORS** — `django-cors-headers` with explicit frontend origins
2. **Stripe webhook verification** — `constructEvent()` with endpoint secret
3. **Signed media URLs** — protect paywalled comic images
4. **Celery task validation** — validate inputs before worker processing
5. **Django SECRET_KEY rotation** — separate keys per environment

---

## Related Projects (in workspace)

- **comicwise** — consolidation source; shared comic reader patterns
- **rhixe_scans** — shared comic reader; Stripe + NextAuth + Tailwind patterns
- **Django-Scrapy-Selenium** — shared Scrapy + Celery scraping patterns
- **selenium_webdriver** — shared browser automation techniques
- **cookiecutter-django-tailwind** — shared Django + PostgreSQL patterns
- **profile** — shared Django conventions
- **xamehi.tv** — shared DRF + Django patterns

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Next.js 16 | <https://nextjs.org/docs> | Framework docs |
| Celery Django | <https://docs.celeryq.dev/en/stable/django> | Async task queue |
| DRF + Next.js | <https://github.com/nynvr/django-nextjs-postgresql-template> | Reference template |
| Scrapy | <https://docs.scrapy.org> | Web scraping framework |

### Research Methodology
- **Web search:** web_search (2026 dual-stack architecture patterns)
- **Documentation:** web_extract (Next.js, Celery, Scrapy docs)
- **Architecture research:** Django + Next.js integration patterns
- **Last verified:** 2026-07-16
