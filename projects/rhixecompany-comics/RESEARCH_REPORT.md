# RESEARCH_REPORT — rhixecompany-comics

> **Type:** Project research report | **Updated:** 2026-06-29

---

**Tech Stack:** Django 5.x, Next.js 16, Celery + Redis, Scrapy, Selenium, PostgreSQL, Docker
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
| ------- | --- | ------------ |
| Django + Next.js template | https://github.com/nynvr/django-nextjs-postgresql-template | Django 5.1, DRF 3.15, Next.js 15, Docker Compose template |
| Next.js + PostgreSQL + Redis | https://oneuptime.com/blog/post/2026-02-08-how-to-set-up-a-nextjs-postgresql-redis-stack-with-docker-compose/ | Multi-stage builds, Prisma, Redis caching setup |

---

## Key Findings

### Django + Next.js Dual-Stack Architecture
- Biggest risk is API field drift — maintain OpenAPI spec; generate TypeScript types from it (LinkedIn/KanhaSoft, 2026)
- Predicted as 2026 "default stack" for AI-ready, enterprise-grade platforms
- Django at `/api/`, Next.js at frontend domain; CORS via `django-cors-headers` v4.9+
- Real-world case studies: healthcare SaaS (40% faster onboarding), fintech (FCA-compliant), AI startups

### Next.js 16 App Router
- Server Components by default; Client Components only for interactive UI — reduces bundle size
- Turbopack delivers ~400% faster dev server vs webpack
- Server Actions simplify form handling without extra API endpoints

### Celery + Redis for Scraping
- **Production-critical:** `task_acks_late=True`, `task_reject_on_worker_lost=True`, `worker_prefetch_multiplier=1`
- **Visibility timeout:** Must exceed longest task; keep countdown/ETA shorter than timeout to avoid duplicate delivery
- **Deduplication:** `celery-once` with Redis lock prevents duplicate scraping from retries (dev.to/artemooon, 2026)
- TCP keepalive + broker retry policies for Redis failover resilience

### CORS for Dual-Stack
- `django-cors-headers` v4.9+ supports Django 6.1; drops Python 3.9 support in newer versions
- Restrict `CORS_ALLOWED_ORIGINS` to frontend domain only — never `CORS_ALLOW_ALL_ORIGINS=True`

---

## Cheatsheets

| Topic | Resource | Type |
| ----- | -------- | ---- |
| Next.js 16 App Router | https://nextjs.org/docs | Official Docs |
| Celery + Django | https://docs.celeryq.dev/en/stable/django/ | Integration Guide |
| Django CORS Headers | https://generalistprogrammer.com/tutorials/django-cors-headers-python-package-guide | Config Guide |
| Celery Redis at Scale | https://dev.to/artemooon/celery-redis-at-scale-designing-a-reliable-and-efficient-task-queue-in-production-27nh | Production Patterns |

---

## Best Practices

1. **Shared API contract** — OpenAPI spec for Django; generated TypeScript types for Next.js
2. **Server Components by default** — Minimize client JS; migrate only interactive parts
3. **Celery production settings** — `acks_late`, `reject_on_worker_lost`, `prefetch_multiplier=1`
4. **Docker Compose** — Run all 4 services with health checks and named volumes

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
| ------- | ------ | --------- |
| API field drift | Runtime type mismatches | Generate TS types from OpenAPI |
| Client Component misuse | Bloated JS bundles | Server Component by default |
| Celery visibility timeout | Duplicate executions | Keep > longest task; ETA < timeout |
| CORS on `/api/` | Frontend can't fetch | Restrict origins via django-cors-headers |

---

## Performance

1. **Turbopack** — ~400% faster dev server vs webpack
2. **Celery workers** — Scale independently; `prefetch_multiplier=1` for fair distribution
3. **Redis caching** — Cache Django API responses; Next.js ISR for static content
4. **pgbouncer** — Prevent connection exhaustion from both stacks sharing PostgreSQL

---

## Security

1. **Shared DB** — Isolate with separate Django app permissions
2. **CORS** — Restrict `CORS_ALLOWED_ORIGINS` to frontend domain only
3. **Server Actions** — Validate all inputs server-side
4. **Scraping** — Respect `robots.txt` in both Scrapy and Selenium

---

## Related Projects (in workspace)

- **Django-Scrapy-Selenium** — Scraping consolidated from this project
- **xamehi.tv** — Similar DRF + React pattern (React 17)
- **cookiecutter-django-tailwind** — Django 5.x best practices
- **xamehi** — Another dual-service architecture (Django + Express)

---

## Resources

| Resource | URL | Description |
| -------- | --- | ----------- |
| Next.js 16 Docs | https://nextjs.org/docs | App Router documentation |
| Django Docs | https://docs.djangoproject.com/en/5.2/ | Django 5.x docs |
| Celery Docs | https://docs.celeryq.dev/ | Task queue docs |
| Django CORS Headers | https://github.com/adamchainz/django-cors-headers | CORS middleware |
| Docker Compose | https://docs.docker.com/compose/ | Multi-service orchestration |
