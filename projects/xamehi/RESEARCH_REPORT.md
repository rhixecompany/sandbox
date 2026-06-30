# RESEARCH_REPORT — xamehi

> **Type:** Project research report | **Updated:** 2026-06-29

**Type:** Legacy dual-backend app (Django + Express) + React frontend
**Tech Stack:** Django + DRF, Express, React 18/CRA, PostgreSQL, Axios
**Status:** Active (legacy — consolidation opportunity)

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| Django + React guide | https://fdcservers.net/blog/how-to-build-a-simple-app-with-django-and-react | Django + React CORS setup |
| CRA → Vite migration | https://dev.to/solitrix02/goodbye-cra-hello-vite-a-developers-2026-survival-guide-for-migration-2a9f | CRA deprecation; migration path |
| Stop using CRA | https://medium.com/@thedevnotebook/stop-using-create-react-app-in-2026-next-js-and-vite-have-taken-over-a7c5ac59c4ce | why modern React moves to Vite |

---

## Key Findings

### React CRA Deprecation (2026)
- Create React App no longer recommended by React team — slow builds, no ES module support
- react-scripts 4.x/5.x abandoned; security patches stopped in 2023
- **Migration path**: Vite recommended for SPAs not needing RSC
  - Install Vite + React plugin: `npm create vite@latest`
  - Remove CRA dependencies (react-scripts)
  - Update scripts: `vite` dev, `vite build`, `vite preview`
  - Add SVGR plugin for SVG-as-component imports
  - Update entry from `index.js` → `src/main.jsx`
- Vite: native ESM dev server, 10-20x faster HMR, simpler config

### Dual-Backend Architecture
- Running Django (DRF) and Express requires careful CORS: `django-cors-headers` for Django, `cors` middleware for Express
- Three separate build/deploy steps in production: React build, Django collectstatic, Express deploy
- PostgreSQL connection pooling must be coordinated: Django `CONN_MAX_AGE`, Express `pg-pool`
- Port map must be documented: Express `:5000`, Django `:8000`, React `:3000`

### PostgreSQL Connection Pooling
- pgbouncer for shared DB connection pooling; prevents exhaustion from dual backends
- Django: `CONN_MAX_AGE` for persistent connections
- Express: `pg-pool` with appropriate `max` and `idleTimeoutMillis`

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| CRA → Vite migration | https://dev.to/solitrix02/goodbye-cra-hello-vite-a-developers-2026-survival-guide-for-migration-2a9f | Step-by-step Guide |
| Django CORS | https://pypi.org/project/django-cors-headers/ | Package |
| pgbouncer | https://www.pgbouncer.org/ | Connection pooler docs |
| React 19 features | https://react.dev/blog | React official blog |

---

## Best Practices

1. **Migrate CRA to Vite** — faster builds, active maintenance, modern ESM support
2. **Consolidate APIs** — consider merging Express routes into Django DRF
3. **pgbouncer for shared DB** — prevent connection pool exhaustion from dual backends
4. **Unified CORS config** — single policy across Django and Express
5. **Document port mapping** — Express :5000, Django :8000, React :3000

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| CRA deprecation | no security patches, slow builds | migrate to Vite |
| Dual backend drift | API inconsistency | consolidate API into DRF |
| DB connection exhaustion | application outages | pgbouncer with connection limits |
| Port confusion (3 services) | dev environment errors | document port mapping |

---

## Performance

1. **Vite migration** — 10x faster HMR vs CRA's webpack dev server
2. **Consolidate API** — eliminate Express if low-traffic; reduce infrastructure overhead
3. **pgbouncer** — transaction pooling for high concurrency
4. **Django caching** — add Redis for frequently accessed API endpoints

---

## Security

1. **CORS hardening** — three services = three attack surfaces; restrict each to minimal origins
2. **Express dependency audit** — ensure Express + middleware up to date (legacy risk)
3. **JWT shared secret** — if both backends validate JWTs, rotate regularly
4. **HTTPS required** — all three endpoints (React, Django, Express) need TLS in production

---

## Related Projects (in workspace)

- **xamehi.tv** — same Django + React pattern; xamehi adds Express backend
- **ecom** — simpler (single Django backend + React); xamehi is more complex
- **rhixecompany-comics** — another dual-service architecture (Django + Next.js)

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Vite migration | https://dev.to/solitrix02/goodbye-cra-hello-vite-a-developers-2026-survival-guide-for-migration-2a9f | CRA → Vite guide |
| DRF Docs | https://www.django-rest-framework.org/ | DRF official docs |
| Express.js | https://expressjs.com/ | Express web framework |
| pgbouncer | https://www.pgbouncer.org/ | PostgreSQL connection pooler |
