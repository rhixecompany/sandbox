# RESEARCH_REPORT — rhixecompany-comics

> **Type:** Project research report | **Updated:** 2026-07-10

**Type:** Dual-stack comics platform (Django 5.x + Next.js 16)
**Tech Stack:** Django 5.x, DRF, Next.js 16, React 19, Tailwind 4, Celery + Redis, Scrapy, Selenium, PostgreSQL, Docker
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
| --------- | ----- | -------------- |
| Django + Next.js template | <https://github.com/nynvr/django-nextjs-postgresql-template> | Django 5.1 + DRF 3.15 + Next.js 15 + Docker |
| Unfold Turbo | <https://github.com/unfoldadmin/turbo> | Django & Next.js boilerplate |
| Django-Next.js Auth | <https://github.com/PikoCanFly/JWT-HTTPCookies-Django-DRF-NEXT.JS> | JWT + HttpOnly cookies; DRF + Next.js |

---

## Key Findings

### Django + Next.js Dual-Stack (2026)

- Biggest risk: **API field drift** — maintain OpenAPI spec; generate TS types
- Predicted 2026 default stack for AI-ready enterprise platforms
- Django at `/api/`, Next.js at frontend domain; CORS via `django-cors-headers` v4.9+
- Case studies: healthcare SaaS (40% faster onboarding), fintech, AI startups

### Next.js 16 + React 19

- **Server Components by default**; Client Components only for interactive UI
- **Turbopack ~400% faster** dev vs webpack
- Enable `output: 'standalone'` for Docker deployment
- **Server Actions** simplify form handling without extra endpoints
- Server Actions are the "API Route Killer" — eliminate boilerplate API routes
- Use `'use client'` directive at file top to mark Client Components
- Server Components can pass data to Client Components via serializable props
- Interleave Server/Client Components via `children` prop pattern

### Celery + Redis Production (2026)

**Critical Settings (MUST CHANGE FROM DEFAULTS):**

- `task_acks_late=True` — ack AFTER task completes, not before
- `task_reject_on_worker_lost=True` — requeue tasks if worker dies mid-execution
- `worker_prefetch_multiplier=1` — prevent worker from hoarding tasks
- `broker_transport_options={'visibility_timeout': 3600}` — MUST exceed longest task; keep ETA shorter than timeout
- `task_acks_on_failure_or_timeout=True` — ack even on failure

**Redis + Celery 5 Gotchas:**

- `task_reject_on_worker_lost` does NOT work with Redis without `visibility_timeout` config
- Default `visibility_timeout` is 1 hour — tasks running longer get redelivered unexpectedly
- Workers stop consuming after Redis reconnection unless `--without-heartbeat --without-gossip --without-mingle` flags used
- Use `celery-once` with Redis lock to prevent duplicate scraping from retries
- Use RabbitMQ (preferred) or Redis as broker; monitor with Flower
- Retry with `max_retries` + exponential backoff

**Deployment Patterns:**

- During rolling deploy: tasks picked up but not finished VANISH if `task_acks_late=False`
- 47 tasks lost in production incident — worker restart mid-execution = tasks gone
- Use `task_reject_on_worker_lost=True` + proper `visibility_timeout` for reliable redelivery

### CORS + Auth

- `django-cors-headers` v4.9+ drops Python 3.9 in newer versions
- **JWT with HttpOnly cookies + refresh tokens** (more secure than localStorage)
- SimpleJWT with token blacklist on logout
- Next.js API routes proxy to Django; avoid client-side cross-origin
- `CORS_ALLOWED_ORIGINS = ["http://localhost:3000", "http://frontend:3000"]`
- `CORS_ALLOW_CREDENTIALS=True` required for cookie auth

### PostgreSQL Shared Database Dual-Stack Migration Strategies

- **Shared DB isolation**: separate Django app permissions per service
- Use `django-multitenant` or Citus for multi-tenancy if needed
- Run migrations from Django only; Next.js uses Prisma/Drizzle read-only or API
- `pgbouncer` — prevent connection exhaustion from shared PostgreSQL
- Separate schemas per service if isolation needed (`public` for Django, `nextjs` for frontend)

### Tailwind CSS 4 + Radix UI Component Library Patterns

**2026 Landscape:**

1. **shadcn/ui** — default choice for React + Tailwind; CLI copies component source into your project; built on Radix primitives; full code ownership
2. **Radix UI** — largest headless primitive library (28+ components); Radix Themes adds optional styled layer
3. **daisyUI** — semantic class names (`btn btn-primary`), 35+ built-in themes, framework-agnostic
4. **Headless UI** — from Tailwind Labs; React/Vue; minimal components
5. **Flowbite** — 400+ components, React/Vue/Svelte/HTML
6. **Spell UI** — motion-first components (Motion/Framer Motion), shadcn-compatible CLI

**Radix + Tailwind CSS v4 Integration:**

- Radix Themes uses `radix` CSS layer; Tailwind utilities in `utilities` layer
- Order CSS layers: `@layer base < radix < utilities` so Tailwind overrides Radix
- Use `@import "@radix-ui/themes/styles.css";` then Tailwind imports
- Target `data-[state=open]:opacity-100` for Radix state-based styling
- `tailwindcss-radix` plugin available for automatic layer ordering

### Docker Compose Multi-Service Orchestration Django + Next.js

**2026 Best Practices:**

- Use `docker compose` (v2, space not hyphen) — legacy binary deprecated
- Compose spec v5.0.0 (late 2025) adds `include` directive for modular compose files
- Separate `docker-compose.yml` (dev) and `docker-compose.prod.yml` (prod)
- Health checks on ALL services (db, redis, backend, frontend)
- Next.js: `output: 'standalone'` in `next.config.js` for minimal Docker image
- Multi-stage Dockerfiles: `deps` → `builder` → `runner` stages
- Gunicorn for Django production (`gunicorn core.wsgi:application --bind 0.0.0.0:8000`)
- Shared `.env` across services; never commit secrets
- Nginx reverse proxy in front for static files + SSL termination
- `depends_on` with `condition: service_healthy` for proper startup order

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
| ------- | ---------- | ------ |
| Next.js 16 | <https://nextjs.org/docs> | Docs |
| Next.js Server/Client Components | <https://nextjs.org/docs/app/getting-started/server-and-client-components> | Guide |
| Celery + Django | <https://docs.celeryq.dev/en/stable/django/> | Integration Guide |
| Celery Best Practices | <https://denibertovic.com/posts/celery-best-practices> | Production Guide |
| Celery Config Reference | <https://docs.celeryq.dev/en/main/userguide/configuration.html> | Docs |
| Django CORS Headers | <https://generalistprogrammer.com/tutorials/django-cors-headers-python-package-guide> | Config |
| Docker Compose | <https://docs.docker.com/compose/> | Multi-service orchestration |
| Tailwind CSS 4 | <https://tailwindcss.com/docs> | Docs |
| Radix UI | <https://www.radix-ui.com> | Component Library |
| shadcn/ui | <https://ui.shadcn.com> | Component Generator |

---

## Best Practices

1. **Shared API contract** — OpenAPI spec; generate TS types for Next.js via `openapi-typescript` or `orval`
2. **Server Components** — minimize client JS; default to Server Components in App Router
3. **Celery production settings** — `acks_late`, `reject_on_worker_lost`, `prefetch_multiplier=1`, `visibility_timeout > max_task_duration`
4. **Docker Compose** — all services with health checks; dev/prod split configs
5. **JWT in HttpOnly cookies** — short TTL access tokens + rotation; `CORS_ALLOW_CREDENTIALS=True`
6. **Redis visibility_timeout** — set explicitly in `broker_transport_options` for Celery 5 + Redis
7. **OpenAPI generation** — `drf-spectacular` on Django; generate TS types for Next.js client
8. **Next.js Server Actions** — prefer over API routes for mutations; reduces boilerplate
9. **Tailwind + Radix layering** — configure CSS layer order: base < radix < utilities
10. **pgbouncer** — connection pooling for shared PostgreSQL across Django + Next.js services

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
| --------- | -------- | ----------- |
| API field drift | runtime type mismatches | generate TS types from OpenAPI |
| Celery `task_acks_late=False` | tasks vanish on worker restart | set `task_acks_late=True` |
| Celery visibility timeout | duplicate executions | keep > longest task; ETA < timeout |
| JWT in localStorage | XSS vector | use HttpOnly cookies |
| CORS misconfiguration | frontend can't fetch API | whitelist origin; `CORS_ALLOW_CREDENTIALS=True` |
| Radix + Tailwind CSS layers | Radix styles override Tailwind | order layers: base < radix < utilities |
| Docker Compose legacy binary | deprecated, missing features | use `docker compose` (v2 plugin) |
| Next.js without `output: standalone` | bloated Docker images | enable in `next.config.js` |
| Celery worker prefetch > 1 | one worker hoards tasks | `worker_prefetch_multiplier=1` |
| Shared DB no connection pooling | connection exhaustion | use `pgbouncer` |

---

## Performance

1. **Turbopack** — ~400% faster dev vs webpack
2. **Celery workers** — scale independently; `--concurrency=CPU*2+1`
3. **Django Redis cache** — API response caching
4. **Next.js ISR** — for static content caching
5. **pgbouncer** — prevent connection exhaustion from shared PostgreSQL
6. **Next.js Server Components** — zero JS sent to client for static content
7. **Server Actions** — eliminate API round-trips for mutations
8. **Radix UI primitives** — minimal bundle, tree-shakeable

---

## Security

1. **Shared DB isolation** — separate Django app permissions per service
2. **CORS restriction** — whitelist only frontend domain
3. **SECRET_KEY rotation** — never commit; use env var
4. **django-ratelimit** — API rate limiting
5. **Robots.txt** — respect in both Scrapy and Selenium
6. **HttpOnly cookies** — JWT storage; `Secure` flag in prod
7. **CSRF protection** — DRF `SessionAuthentication` + Next.js proxy
8. **Content Security Policy** — via Django middleware + Next.js headers

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
| ---------- | ----- | ------------- |
| Next.js 16 Docs | <https://nextjs.org/docs> | App Router docs |
| Next.js Server Components | <https://nextjs.org/docs/app/getting-started/server-and-client-components> | Server/Client Components guide |
| Next.js Server Actions | <https://nextjs.org/docs/app/guides/forms> | Forms & mutations |
| Django Docs | <https://docs.djangoproject.com/en/5.2/> | Django 5.x docs |
| DRF Docs | <https://www.django-rest-framework.org/> | REST framework |
| Celery Docs | <https://docs.celeryq.dev/> | Task queue docs |
| Celery Config | <https://docs.celeryq.dev/en/main/userguide/configuration.html> | Settings reference |
| Django CORS Headers | <https://github.com/adamchainz/django-cors-headers> | CORS middleware |
| Docker Compose | <https://docs.docker.com/compose/> | Multi-service orchestration |
| Tailwind CSS 4 | <https://tailwindcss.com/docs> | Utility-first CSS |
| Radix UI | <https://www.radix-ui.com> | Headless primitives |
| shadcn/ui | <https://ui.shadcn.com> | Copy-paste components |
| MasteringBackend Celery | <https://publication.masteringbackend.com/5-celery-settings-most-python-backend-engineers-never-change-d585465a6a8b> | 5 critical Celery settings |
| Celery Production Patterns | <https://levelup.gitconnected.com/celery-in-production-the-patterns-nobody-teaches-and-the-failures-nobody-talks-about-9b6216d102b3> | Real-world failures |
| Django + Next.js Docker | <https://medium.com/@sizanmahmud08/how-to-integrate-django-with-next-js-9238fa4dd4f3> | Step-by-step Docker guide |

---

## Section 9 Query Research (2026-07-10)

The following queries from `docs/per-project-research-queries.md` section 9 have been researched and findings incorporated above:

1. **Django + Next.js dual-stack architecture 2026 patterns** — Covered in Key Findings
2. **DRF + Next.js App Router API contract maintenance (OpenAPI/TS types)** — Best Practices #1, #7; Cheatsheets
3. **Celery + Redis async task processing for comic scraping** — Critical Celery settings section
4. **Django CORS headers + Next.js cross-origin API patterns** — CORS + Auth section
5. **PostgreSQL shared database dual-stack migration strategies** — PostgreSQL section
6. **Tailwind CSS 4 + Radix UI component library patterns** — Tailwind + Radix section
7. **Docker Compose multi-service orchestration Django + Next.js** — Docker Compose section
8. **Next.js 16 Server Components + React 19 patterns** — Next.js 16 section
9. **Celery 5 production reliability settings** — Celery + Redis Production (detailed)
10. **shadcn/ui + Radix + Tailwind 4 integration patterns** — Tailwind + Radix section

---

*Report updated with 2026 web research findings. All external sources cited inline.*
