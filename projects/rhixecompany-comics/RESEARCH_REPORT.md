# RESEARCH_REPORT — rhixecompany-comics

> **Type:** Project research report | **Updated:** 2026-06-29

**Type:** Dual-stack comics platform (Django 5.x + Next.js 16)
**Tech Stack:** Django 5.x, DRF, Next.js 16, React 19, Tailwind 4, Celery + Redis, Scrapy, Selenium, PostgreSQL, Docker
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| Django + Next.js template | https://github.com/nynvr/django-nextjs-postgresql-template | Django 5.1 + DRF 3.15 + Next.js 15 + Docker |
| Unfold Turbo | https://github.com/unfoldadmin/turbo | Django & Next.js boilerplate |
| Django-Next.js Auth | https://github.com/PikoCanFly/JWT-HTTPCookies-Django-DRF-NEXT.JS | JWT + HttpOnly cookies; DRF + Next.js |

---

## Key Findings

### Django + Next.js Dual-Stack (2026)
- Biggest risk: API field drift — maintain OpenAPI spec; generate TS types
- Predicted 2026 default stack for AI-ready enterprise platforms
- Django at `/api/`, Next.js at frontend domain; CORS via `django-cors-headers` v4.9+
- Case studies: healthcare SaaS (40% faster onboarding), fintech, AI startups

### Next.js 16 + React 19
- Server Components by default; Client Components only for interactive UI
- Turbopack ~400% faster dev vs webpack
- enable `output: 'standalone'` for Docker deployment
- Server Actions simplify form handling without extra endpoints

### Celery + Redis Production (2026)
- **Critical settings**: `task_acks_late=True`, `task_reject_on_worker_lost=True`, `worker_prefetch_multiplier=1`
- Visibility timeout must exceed longest task; keep ETA shorter than timeout
- `celery-once` with Redis lock prevents duplicate scraping from retries
- Use RabbitMQ (preferred) or Redis as broker; monitor with Flower
- Retry with `max_retries` + exponential backoff

### CORS + Auth
- `django-cors-headers` v4.9+ drops Python 3.9 in newer versions
- JWT with HttpOnly cookies + refresh tokens (more secure than localStorage)
- SimpleJWT with token blacklist on logout
- Next.js API routes proxy to Django; avoid client-side cross-origin

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Next.js 16 | https://nextjs.org/docs | Docs |
| Celery + Django | https://docs.celeryq.dev/en/stable/django/ | Integration Guide |
| Celery best practices | https://denibertovic.com/posts/celery-best-practices | Production Guide |
| Django CORS Headers | https://generalistprogrammer.com/tutorials/django-cors-headers-python-package-guide | Config |

---

## Best Practices

1. **Shared API contract** — OpenAPI spec; generate TS types for Next.js
2. **Server Components** — minimize client JS
3. **Celery production settings** — `acks_late`, `reject_on_worker_lost`, `prefetch_multiplier=1`
4. **Docker Compose** — all services with health checks
5. **JWT in HttpOnly cookies** — short TTL access tokens + rotation

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| API field drift | runtime type mismatches | generate TS types from OpenAPI |
| Celery visibility timeout | duplicate executions | keep > longest task; ETA < timeout |
| JWT in localStorage | XSS vector | use HttpOnly cookies |
| CORS misconfiguration | frontend can't fetch API | whitelist origin; `CORS_ALLOW_CREDENTIALS=True` |

---

## Performance

1. **Turbopack** — ~400% faster dev vs webpack
2. **Celery workers** — scale independently; `--concurrency=CPU*2+1`
3. **Django Redis cache** — API response caching
4. **Next.js ISR** — for static content caching
5. **pgbouncer** — prevent connection exhaustion from shared PostgreSQL

---

## Security

1. **Shared DB isolation** — separate Django app permissions per service
2. **CORS restriction** — whitelist only frontend domain
3. **SECRET_KEY rotation** — never commit; use env var
4. **django-ratelimit** — API rate limiting
5. **Robots.txt** — respect in both Scrapy and Selenium

---

## Related Projects (in workspace)

- **Banking** — shared fintech-style auth and payment patterns
- **comicwise** — shared comic reader; consolidation target inheriting reader patterns
- **Django-Scrapy-Selenium** — scraping consolidated from this project
- **profile** — shared Django + Docker + PostgreSQL
- **rhixe_scans** — shared comic reader; consolidation target
- **selenium_webdriver** — target where scraping utilities should migrate
- **university-libary-jsm** — serverless Postgres + Redis infra
- **xamehi.tv** — similar DRF + React pattern
- **xamehi** — dual-service architecture (Django + Express)

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Next.js 16 Docs | https://nextjs.org/docs | App Router docs |
| Django Docs | https://docs.djangoproject.com/en/5.2/ | Django 5.x docs |
| Celery Docs | https://docs.celeryq.dev/ | Task queue docs |
| Django CORS Headers | https://github.com/adamchainz/django-cors-headers | CORS middleware |
| Docker Compose | https://docs.docker.com/compose/ | Multi-service orchestration |
