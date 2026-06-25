# RESEARCH_REPORT — rhixecompany-comics

> **Type:** Project research report | **Updated:** 2026-06-25

---

**Type:** Dual-stack web platform (Django backend + Next.js frontend)
**Tech Stack:** Django 5.x, Next.js 16, Celery + Redis, Scrapy, Selenium, PostgreSQL, Docker
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
| ------- | --- | ------------ |
| Django + Next.js cookiecutter | https://www.reddit.com/r/django/comments/1cbbmru/django_and_nextjs_cookiecutter_monorepo | Community patterns for Django + Next.js monorepos |
| Next.js + PostgreSQL + Redis Docker | https://oneuptime.com/blog/post/2026-02-08-how-to-set-up-a-nextjs-postgresql-redis-stack-with-docker-compose/ | Reference Docker Compose setup |

---

## Key Findings

### Django + Next.js Dual-Stack Architecture

- The biggest maintenance risk in a split architecture is drift between Django API responses and Next.js type expectations — maintain a shared OpenAPI/Swagger spec (medium.com/@mmoznu, 2026)
- Two independent stacks sharing a PostgreSQL database is a common pattern; ensure migrations are coordinated (reddit.com/r/django, 2026)
- Django at `/api/` and Next.js at frontend domain; CORS configured on Django side

### Next.js 16 App Router

- Server Components by default, Client Components only when interactivity needed — reduces JS bundle size significantly (tech-insider.org, 2026)
- Turbopack in Next.js 16 delivers ~400% faster dev server startup vs webpack (tech-insider.org, 2026)
- Server Actions simplify form handling and data mutations without boilerplate API endpoints (YouTube, 2026)

### Celery + Redis for Scraping

- `django-celery-beat` provides database-backed periodic task scheduling for scraping jobs (oneuptime.com, 2026)
- Scrapy spiders called from Celery tasks for distributed scraping; results persisted via Django ORM
- Redis serves as both Celery broker and result backend; monitoring via Flower dashboard

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
| ----- | -------- | ---- |
| Next.js 16 App Router | https://nextjs.org/docs/app | Official Docs |
| Celery + Django | https://docs.celeryq.dev/en/stable/django/ | Integration Guide |
| Docker Compose multi-service | https://oneuptime.com/blog/post/2026-02-08-how-to-set-up-a-nextjs-postgresql-redis-stack-with-docker-compose/ | Tutorial |

---

## Best Practices

1. **Shared API contract** — Maintain OpenAPI spec for Django API; generate TypeScript types for Next.js frontend
2. **Server Components by default** — Minimize client-side JS; use Client Components only for interactive UI
3. **Celery beat scheduling** — Use `django-celery-beat` DB-backed scheduler for manageable periodic scraping tasks
4. **Docker Compose orchestration** — Run Django, Next.js, PostgreSQL, and Redis as coordinated services

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
| ------- | ------ | --------- |
| API field drift | Runtime type mismatches | Generate TypeScript types from OpenAPI spec |
| Client Component misuse | Bloated JS bundles | Default to Server Component; migrate only interactive parts |
| Celery beat not synced | Missed or duplicate scraping jobs | Use django-celery-beat scheduler with DB backend |
| CORS on `/api/` Django routes | Next.js can't fetch | Configure django-cors-headers for Next.js frontend domain |

---

## Performance

1. **Turbopack** — Next.js 16's Turbopack provides 400% faster dev server vs webpack-based CRA
2. **Celery worker scaling** — Scale Celery workers independently from web workers for heavy scraping loads
3. **Redis caching** — Cache Django API responses in Redis; Next.js ISR for static content
4. **PostgreSQL connection pooling** — Both stacks share the same DB; pgbouncer prevents connection exhaustion

---

## Security

1. **Shared database concerns** — Both stacks access same PostgreSQL; isolate with separate Django app permissions
2. **CORS for dual domains** — Restrict `CORS_ALLOWED_ORIGINS` to Next.js frontend domain only
3. **Next.js Server Actions** — Validate all server action inputs; don't trust client-side form data
4. **Scraping robots.txt** — Respect robots.txt from both Scrapy spiders and Selenium scrapers

---

## Related Projects (in workspace)

- **Django-Scrapy-Selenium** — Scraping functionality was consolidated from this project
- **xamehi.tv** — Shares DRF + React pattern (though xamehi.tv uses React 17, not Next.js)
- **cookiecutter-django-tailwind** — Django 5.x best practices apply to the backend
- **xamehi** — Another dual-service architecture (Django + Express instead of Django + Next.js)

---

## Resources

| Resource | URL | Description |
| -------- | --- | ----------- |
| Next.js 16 Docs | https://nextjs.org/docs | Next.js App Router documentation |
| Django Docs | https://docs.djangoproject.com/en/5.2/ | Django 5.x documentation |
| Celery Docs | https://docs.celeryq.dev/ | Celery task queue documentation |
| Docker Compose | https://docs.docker.com/compose/ | Multi-service orchestration |

---