# RESEARCH_REPORT.md

## Project: rhixecompany-comics

**Type:** Dual-stack comics platform (Django 5.x + Next.js 16)
**Tech Stack:** Django 5.x, DRF, Next.js 16, React 19, Tailwind 4, Celery + Redis, Scrapy, Selenium, PostgreSQL, Docker
**Status:** Active

---

## Similar Projects

| Project | Relevance |
|---------|-----------|
| comicwise | Consolidation source; shared reader patterns + Drizzle migration |
| rhixe_scans | Shared comic domain; Stripe + NextAuth + Tailwind patterns |
| Banking | Shared Drizzle ORM + PostgreSQL + Next.js 16 conventions |

---

## Key Findings

### Django + Next.js Dual-Stack (2026)
- **Biggest risk:** API field drift — maintain OpenAPI spec; generate TS types from DRF
- **Django at `/api/`** — CORS via `django-cors-headers` 4.9+ with explicit origins
- **Server Actions** — eliminate boilerplate API routes in Next.js
- **Build Adapters API (16.2 stable)** — OpenNext, Cloudflare, Amplify supported
- **`proxy.ts` replaces `middleware.ts`** — explicit boundary for auth and redirects

### Next.js 16 + React 19 (2026)
- **Turbopack default** — 2–5× faster builds, ~400% faster dev startup
- **`"use cache"` directive** — explicit caching replaces implicit magic
- **React Compiler, Server Actions, `use()` hook** — all production-stable

### Celery + Redis Production (2026)
- **Critical config:** `task_acks_late=True`, `task_reject_on_worker_lost=True`
- **Queue separation** — dedicated queues for scraping vs content processing
- **`worker_prefetch_multiplier=1`** — prevent workers from hoarding tasks
- **`django-celery-beat`** for DB-backed periodic task scheduling

---

## Cheatsheets

| Topic | Resource |
|-------|----------|
| Next.js 16 + Docker | <https://nextjs.org/docs/app/guides/advanced#standalone> |
| Celery prod settings | <https://docs.celeryq.dev/en/stable/userguide/configuration.html> |
| DRF + Next.js | <https://github.com/nynvr/django-nextjs-postgresql-template> |
| Tailwind 4 | <https://tailwindcss.com/docs/installation> |

---

## Best Practices

1. **OpenAPI spec as source of truth** — generate TS types from DRF schema to prevent API drift
2. **Server Actions for mutations** — reduce API route boilerplate on Next.js side
3. **Celery queue separation** — dedicated queues for scraping vs content processing
4. **Scrapy for static, Celery for scheduling** — spiders as tasks, not views
5. **Tailwind 4 CSS-first** — `@import "tailwindcss"` + `@theme` directive; no `tailwind.config.js`
6. **Neon connection pooling** — use pooled connection strings for app queries

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| API field drift | Frontend breaks | OpenAPI spec + auto-generated TS types |
| Missing Celery `ack_late` | Lost tasks on crash | `task_acks_late=True` in settings |
| Server Actions in Client Components | Runtime errors | Server Actions in Server Components only |
| Tailwind 3→4 config migration | Build breaks | `@import "tailwindcss"` API; no `tailwind.config.js` |
| `db push` in production | Lost migration audit | Use `generate` + `migrate` for production |

---

## Performance

1. **Turbopack + standalone output** — faster builds, smaller Docker images
2. **Celery worker concurrency** — `CPU*2+1` for I/O-bound scraping workloads
3. **Partial Prerendering** — static shell + dynamic content streams
4. **Django connection pooling** — `CONN_MAX_AGE` for production PostgreSQL
5. **Redis caching** — cache frequent DB queries at the Django ORM layer
6. **Neon branching for preview** — copy-on-write branches per deployment

---

## Security

1. **Strict CORS** — `django-cors-headers` with explicit frontend origins
2. **Stripe webhook verification** — `constructEvent()` with endpoint secret
3. **Signed media URLs** — protect paywalled comic images via token expiration
4. **Celery task validation** — validate inputs before worker processing
5. **Django SECRET_KEY rotation** — separate keys per environment
6. **Upgrade to Next.js 16.2.6+** — patches 13 advisories (May 2026 security release)

---

## Related Projects (in workspace)

- **comicwise** — consolidation source; shared reader patterns; Drizzle migration reference
- **rhixe_scans** — shared comic domain; Stripe + NextAuth + media delivery patterns
- **Banking** — shared Drizzle ORM + PostgreSQL + Next.js 16 conventions; fintech patterns

---

## Resources

| Resource | URL |
|----------|-----|
| Next.js 16 | <https://nextjs.org/docs> |
| Celery + Django | <https://docs.celeryq.dev/en/stable/django> |
| DRF + Next.js Template | <https://github.com/nynvr/django-nextjs-postgresql-template> |
| Scrapy | <https://docs.scrapy.org> |
| Tailwind CSS 4 | <https://tailwindcss.com/docs> |

### Research Methodology
- **Web search:** Tavily search (2026 Django+Next.js dual-stack, Celery, Scrapy patterns)
- **Last verified:** 2026-07-28
