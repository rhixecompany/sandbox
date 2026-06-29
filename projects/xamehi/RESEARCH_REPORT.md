# RESEARCH_REPORT — xamehi

> **Type:** Project research report | **Updated:** 2026-06-25

---

**Type:** Legacy dual-backend app (Django + Express) + React frontend
**Tech Stack:** Django+DRF, Express, React 18/CRA, PostgreSQL
**Status:** Active (legacy — consolidation opportunity)

---

## Similar Projects

| Project | URL | Why Relevant |
| ------- | --- | ------------ |
| Django + React guide | https://fdcservers.net/blog/how-to-build-a-simple-app-with-django-and-react | Django + React CORS setup patterns |
| CRA migration to Vite | https://dev.to/solitrix02/goodbye-cra-hello-vite-a-developers-2026-survival-guide-for-migration-2a9f | CRA deprecation and migration path |

---

## Key Findings

### Dual-Backend Architecture

- Running Django (DRF) and Express as separate backends requires careful CORS configuration — django-cors-headers for Django, `cors` middleware for Express (forum.djangoproject.com, 2026)
- Dual backends increase production complexity: three separate build/deploy steps (React build, Django collectstatic, Express deploy)
- PostgreSQL connection pooling must be coordinated between both backends to avoid connection exhaustion

### React 18 CRA Migration

- Create React App is no longer recommended by the React team — slow builds, no ES module support (dev.to, 2026)
- Migration to Vite is the recommended path: faster HMR, ES-native dev server, simpler config (oneuptime.com, 2026)
- CRA's react-scripts 4.x/5.x has been abandoned; security patches stopped in 2023

### PostgreSQL Dual-Backend Connection Pooling

- Both Django and Express share the same PostgreSQL database — implement pgbouncer for connection pooling
- Django uses `CONN_MAX_AGE` for persistent connections; Express uses `pg-pool` for connection pooling

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
| ----- | -------- | ---- |
| CRA → Vite migration | https://dev.to/solitrix02/goodbye-cra-hello-vite-a-developers-2026-survival-guide-for-migration-2a9f | Guide |
| Django CORS | https://pypi.org/project/django-cors-headers/ | Package |
| PostgreSQL pooling | https://www.pgbouncer.org/ | Guide |

---

## Best Practices

1. **Consolidate backends** — Consider merging Express API routes into Django DRF for simpler deployment
2. **Migrate CRA to Vite** — Faster builds, modern ESM support, active maintenance
3. **pgbouncer for shared DB** — Prevent connection pool exhaustion from dual backends
4. **Unified CORS config** — Single CORS policy shared across Django and Express for consistent security

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
| ------- | ------ | --------- |
| CRA deprecation | No security patches, slow builds | Migrate to Vite as soon as possible |
| Dual backend drift | API inconsistency | Consolidate API surface into DRF |
| DB connection exhaustion | Application outages | Implement pgbouncer with connection limits |
| Port confusion (3 services) | Dev environment errors | Document port mapping: Express :5000, Django :8000, React :3000 |

---

## Performance

1. **Vite migration** — 10x faster HMR vs CRA's webpack-based dev server
2. **Consolidate API** — Eliminate Express backend to reduce infrastructure overhead if it's low-traffic
3. **PostgreSQL connection pooling** — pgbouncer with transaction pooling for high concurrency
4. **Django caching** — Add Redis caching layer for frequently accessed API endpoints

---

## Security

1. **CORS hardening** — Three services mean three CORS attack surfaces; restrict each to minimal allowed origins
2. **Express dependency audit** — Ensure Express + middleware dependencies are up to date (legacy risk)
3. **JWT shared secret** — If both backends validate JWTs, rotate shared secret regularly
4. **HTTPS required** — Three endpoints (React, Django, Express) all need TLS in production

---

## Related Projects (in workspace)

- **xamehi.tv** — Same Django + React pattern; xamehi adds Express backend
- **ecom** — Simpler architecture (single Django backend + React); xamehi is more complex with dual backends
- **rhixecompany-comics** — Another dual-service architecture (Django + Next.js)

---

## Resources

| Resource | URL | Description |
| -------- | --- | ----------- |
| Vite migration | https://dev.to/solitrix02/goodbye-cra-hello-vite-a-developers-2026-survival-guide-for-migration-2a9f | CRA → Vite guide |
| Django REST Framework | https://www.django-rest-framework.org/ | DRF official docs |
| Express.js | https://expressjs.com/ | Express web framework |
| pgbouncer | https://www.pgbouncer.org/ | PostgreSQL connection pooler |

---