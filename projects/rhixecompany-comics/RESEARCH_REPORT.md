# RESEARCH_REPORT — rhixecompany-comics

**Type:** Dual-stack comics platform (Django 5.2 LTS/6.0 + Next.js 16.3)
**Tech Stack:** Django 5.2 LTS/6.0, DRF 3.15, Next.js 16.3, React 19, Tailwind 4, Celery + Redis, Scrapy, Selenium,
PostgreSQL 16, Docker
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| Django + Next.js template | https://github.com/nynvr/django-nextjs-postgresql-template | Django 5.1 + DRF 3.15 + Next.js 15 + Docker |
| Unfold Turbo | https://github.com/unfoldadmin/turbo | Django & Next.js boilerplate |
| django-ckeditor-5 | https://github.com/hvlads/django-ckeditor-5 | Rich-text editor for comics CMS |

---

## Fresh Findings (July 2026, verified)

- **Django 6.0** (Dec 3, 2025) supports Python **3.12–3.14** (drops 3.10/3.11); new built-in **CSP** (`SECURE_CSP` + nonce), **Tasks framework** (`@task`), template partials. Third-party libs dropping pre-5.2.
- **Django 4.2 LTS EOL** April 7, 2026 — no upstream security patches. Migration to 5.2 LTS is urgent.
- **Django 5.2 LTS** is the current production target; supports Python 3.10–3.14; `CompositePrimaryKey`, async auth.
- **Next.js 16** (shipped Oct 21, 2025) makes **Turbopack the default bundler** — 2–5× faster production builds, up to 10× faster Fast Refresh. New explicit caching APIs (`revalidateTag`, `updateTag`, `refresh`) replace brittle ISR. **Next.js 16.2** (Mar 18, 2026) added Server Fast Refresh (400–900% faster compile in real apps), Subresource Integrity (SRI) for JS, tree-shaking of dynamic imports.
- **Tailwind v4** is CSS-first (`@import "tailwindcss"` + `@theme`), Rust engine 3–10× faster, drops `tailwind.config.js`.
- **drf-spectacular 0.30.0** (July 6) — renovated test matrix, bug fixes.

---

## Key Architecture Rules

1. **Django at `/api/`**, Next.js at frontend domain; CORS via `django-cors-headers` v4.9+
2. **OpenAPI spec as source of truth** — generate TS types from DRF schema with drf-spectacular 0.30+
3. **Server Components by default** — Server Actions for mutations; Client Components for interactivity only
4. **Queue separation** — dedicated Celery queues for scraping vs content processing
5. **Tailwind 4 CSS-first** — `@import "tailwindcss"` + `@theme`; no `tailwind.config.js`

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Next.js 16 + Docker | https://nextjs.org/docs/app/guides/advanced#standalone | Guide |
| Next.js 16.2 blog | https://nextjs.org/blog/next-16-2-turbopack | Blog |
| Celery prod settings | https://docs.celeryq.dev/en/stable/userguide/configuration.html | Docs |
| Scrapy Django | https://docs.scrapy.org/en/latest/topics/django | Guide |
| Django 6.0 release notes | https://docs.djangoproject.com/en/6.0/releases/6.0 | Docs |
| Tailwind v4 | https://tailwindcss.com/blog/tailwindcss-v4 | Blog |

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| API field drift | Frontend breaks | OpenAPI spec + auto-generated TS types |
| Django 4.2 EOL | No security patches | Migrate to 5.2 LTS immediately |
| Missing Celery ack_late | Lost tasks on crash | `task_acks_late=True` in settings |
| Server Actions in Client Components | Runtime errors | Server Actions in Server Components only |
| Tailwind 3→4 config migration | Build breaks | `@import "tailwindcss"` API; drop `tailwind.config.js` |

---

## Performance
1. **Next.js 16 Turbopack** — default bundler, 2–5× faster prod builds, Server Fast Refresh in 16.2.
2. **Explicit caching** — `revalidateTag`/`updateTag` replace implicit ISR.
3. **Django connection pooling** — `CONN_MAX_AGE` for production PostgreSQL.
4. **Redis caching** — cache frequent DB queries; separate Redis DBs from Celery broker.
5. **Celery worker sizing** — `(2×CPU)+1` for I/O-bound scraping workloads.

---

## Security
1. **Next.js security process** — formalized patching; first patch July 20, 2026.
2. **Strict CORS** — `django-cors-headers` with explicit origins; never `CORS_ALLOW_ALL`.
3. **Signed media URLs** — protect paywalled comic images.
4. **Celery task validation** — validate inputs before worker processing.
5. **Django SECRET_KEY rotation** — separate keys per environment.
6. **Django 6.0 built-in CSP** — adopt `SECURE_CSP` for XSS defense.

---

## Best Practices
1. Pin Django to **5.2 LTS**; schedule 6.0 once deps support Python 3.12+
2. Generate TS types from drf-spectacular OpenAPI; treat spec as contract
3. Use **Server Components** + Server Actions; keep Client Components minimal
4. Separate **Celery queues** for scrape vs process; `task_acks_late=True`
5. Adopt **Tailwind v4** CSS-first config; drop `tailwind.config.js`

---

## Related Projects (in workspace)
- **rhixe_scans** — Next.js + Prisma + Stripe comic reader (shared domain)
- **profile** — Django + GCS + CKEditor CMS
- **selenium_webdriver** — Selenium scraping utility used by Scrapy pipeline
