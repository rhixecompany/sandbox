# RESEARCH_REPORT.md

## Project: xamehi

**Type:** Legacy multi-backend full-stack application
**Tech Stack:** React 18, Django REST Framework, Express.js, PostgreSQL, Axios, Nodemon, Docker Compose
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| ecom | `projects/ecom` | Shared DRF + React checkout/admin layout. |
| xamehi.tv | `projects/xamehi.tv` | Shared React + DRF media/admin dashboard concerns. |
| rhixecompany-comics | `projects/rhixecompany-comics` | Dual-stack Django + Next.js; DRF API patterns. |
| cookiecutter-django-tailwind | `projects/cookiecutter-django-tailwind` | Django 5.x production template security/settings. |

---

## Key Findings

### Dual-Backend Governance (Django + Express, 2026)

- **Duplicated auth surface** — Django tokens + Express JWT = login state mismatch; consolidate to single auth layer per bounded context [1]
- **API gateway pattern** — NGINX or Kong routes `/api/django/*` → DRF, `/api/express/*` → Express; shared OpenAPI spec prevents drift [2]
- **Migration strategy**: Adapter modules translate Express routes → DRF views behind shared contract; run both in parallel during transition [1]
- **Shared PostgreSQL** — both backends connect to same DB; use PgBouncer connection pooling to manage dual backend connections [3]
- **Contract-first development** — `drf-spectacular` (Django) + `swagger-jsdoc` (Express) → merged OpenAPI → TypeScript types for React [1]

### React 18 + CRA → Vite Migration (2026)

- **CRA deprecated** — no updates since 2021; Vite 5+ is standard: native ES modules, instant HMR, 10x faster builds [4]
- **Migration steps**: 1) `npm create vite@latest` 2) Move `public/index.html` → root 3) Update `package.json` scripts 4) Replace `react-scripts` deps 5) Config `vite.config.ts` for aliases, proxy [4]
- **TypeScript + Vite** — `tsconfig.json` with `baseUrl: "."`, `paths` for `@/*` aliases; `vite-tsconfig-paths` plugin [4]
- **HTTPS in dev** — `server.https: { key, cert }` in `vite.config.ts`; mkcert for local CA [5]
- **Breaking changes**: `.env` loading (Vite uses `import.meta.env`), `process.env` → `import.meta.env`, CSS imports work natively [4]

### Django DRF + Express API Gateway Patterns (2026)

- **BFF (Backend for Frontend)** — React talks to single GraphQL/REST gateway; gateway orchestrates Django + Express calls [2]
- **Shared user IDs** — both backends use same `users` table; Django `AbstractUser` + Express reads `django_user_id` FK [2]
- **Service mesh alternative** — Istio/Linkerd for mTLS, observability, traffic splitting during migration [2]
- **Rate limiting + auth at gateway** — NGINX `limit_req_zone` + JWT validation before proxying to backends [2]

### CORS for Django + Express + React (2026)

- **Root cause**: React dev server (port 3000) ≠ Django (8000) ≠ Express (5000) = three origins [6]
- **Best solution**: Serve React build from Django in production (WhiteNoise + `collectstatic`); eliminates CORS entirely [6]
- **Dev workaround**: Vite proxy (`server.proxy: { '/api': 'http://localhost:8000' }`) + Express proxy for Django routes [6]
- **Production CORS**: `django-cors-headers` with explicit `CORS_ALLOWED_ORIGINS = [frontend_domain]` — never `CORS_ALLOW_ALL_ORIGINS = True` [6]
- **Credentials**: `CORS_ALLOW_CREDENTIALS = True` + `SESSION_COOKIE_SAMESITE = 'Lax'` for cross-subdomain auth [6]

### PostgreSQL Dual Backend Connection Pooling (2026)

- **PgBouncer mandatory** — each backend creates own connections; without pooling, dual backend exhausts `max_connections` [7]
- **Transaction pooling mode** — PgBouncer `pool_mode = transaction` for Django + Express; avoids prepared statement issues [7]
- **Connection limits**: `max_client_conn = 1000`, `default_pool_size = 20` per backend; monitor via `pgbouncer_admin` [7]
- **Django config**: `CONN_MAX_AGE = 0` (let PgBouncer manage); `DATABASES['default']['OPTIONS']['sslmode'] = 'require'` [7]

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Django + Next.js 2026 | https://medium.com/@mmoznu/django-next-js-in-2026-when-to-split-your-frontend-and-backend-and-how-to-wire-them-together-23b4ef68b6df | Guide |
| CRA to Vite migration | https://oneuptime.com/blog/post/2026-01-15-migrate-create-react-app-to-vite/view | Guide |
| Vite vs CRA 2026 | https://www.mol-tech.us/blog/vite-vs-create-react-app-2026 | Comparison |
| Phelipe Teles CRA→Vite | https://phelipetls.github.io/posts/migrating-from-cra-to-vite | Guide |
| Vite HTTPS dev | https://github.com/vitejs/vite/discussions/5589 | Discussion |
| DRF tutorial 2026 | https://tech-insider.org/django-rest-framework-tutorial-python-api-2026 | Tutorial |
| CORS Django React | https://medium.com/techtrends-digest/django-react-and-cors-how-to-fix-cross-origin-errors-the-right-way-36cd46558691 | Guide |
| PgBouncer connection pooling | https://aiven.io/docs/products/postgresql/concepts/pg-connection-pooling | Docs |
| Django dual backend | https://www.reddit.com/r/django/comments/1r4nkut/is_react_djangodrf_still_a_solid_stack_in_ai_era | Discussion |

---

## Best Practices

1. **Single auth layer** — Django SimpleJWT or Express JWT, not both; share user IDs via FK
2. **Vite for React 18+** — replace CRA; `npm create vite@latest` + migrate config
3. **OpenAPI contract** — `drf-spectacular` + `swagger-jsdoc` → merged spec → TypeScript types
4. **NGINX reverse proxy** — serves React build, routes `/api/django/*` and `/api/express/*`
5. **PgBouncer transaction pooling** — prevents connection exhaustion from dual backend
6. **Environment-driven base URLs** — `VITE_API_BASE` + `EXPRESS_API_BASE` in `.env`; no hardcoded localhost
7. **Health checks** — `/health` on both backends; Docker Compose `condition: service_healthy`
8. **Incremental migration** — adapter modules translate Express → DRF behind shared contract
9. **Shared PostgreSQL schema** — migrations applied once; both backends read same tables
10. **Observability** — shared correlation IDs across Django + Express + React logs

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Divergent auth contracts | Login state mismatch | Standardize on one auth layer with shared user IDs |
| Localhost port assumptions | Works in one branch only | Load API base URL from environment in both clients |
| Release without migration guard | Data drift | Require migration plan before merging backend changes |
| CRA in 2026 | Slow builds, no updates | Migrate to Vite 5+ |
| Wildcard CORS in production | Security breach | Explicit `CORS_ALLOWED_ORIGINS`; NGINX serves React build |
| No connection pooling | `max_connections` exhausted | PgBouncer transaction mode for dual backend |
| Hardcoded API URLs | Environment coupling | `import.meta.env.VITE_API_BASE` + `process.env.EXPRESS_API_BASE` |
| Sequential deploys | Downtime during migration | Blue/green deploy gateway first, then backends |
| Missing OpenAPI sync | Contract drift | CI step validates Django + Express specs match |
| Shared session store | Cross-backend session conflicts | Separate session tables/keys per backend |

---

## Performance

1. **Server-side pagination** on large list routes in DRF before handoff to React
2. **Cache shared metadata** in Redis when both backends query same catalog tables
3. **`select_related()` optimized DRF queries** — avoid N+1 in admin views
4. **Vite HMR** — near-instant updates vs CRA 30s+ rebuild cycles
5. **PgBouncer pooling** — 1000+ clients on 20 PostgreSQL connections
6. **NGINX gzip + Cache-Control** on React static assets (`immutable, max-age=31536000`)
7. **Code splitting** — Vite dynamic imports (`const Admin = lazy(() => import('./Admin'))`)

---

## Security

1. **Remove wildcard CORS** from production Express configs
2. **Require HTTPS** in Docker Compose; avoid secrets in compose files
3. **Django `SECRET_KEY` from env** everywhere; remove warning branches
4. **Separate read/write DB users** at scale; restrict admin access
5. **JWT validation at gateway** — NGINX `auth_jwt` before proxying to Django/Express
6. **Rate limiting** — `limit_req_zone` on all `/api/*` endpoints (100 req/min per IP)
7. **Dependency scanning** — `npm audit` + `pip-audit` in CI; Renovate for auto-updates

---

## Related Projects (in workspace)

- **ecom** — shared DRF + React multi-backend layout
- **xamehi.tv** — shared React + DRF admin and media patterns
- **rhixecompany-comics** — dual-stack Django + Next.js; DRF API patterns
- **cookiecutter-django-tailwind** — Django 5.x production template security/settings

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Django docs | https://docs.djangoproject.com/en/stable/ | Framework docs |
| DRF docs | https://www.django-rest-framework.org | API docs |
| Express docs | https://expressjs.com/en/resources/getting-started.html | Runtime docs |
| React docs | https://react.dev/learn | Frontend docs |
| Vite docs | https://vitejs.dev/guide/ | Build tool |
| PgBouncer | https://aiven.io/docs/products/postgresql/concepts/pg-connection-pooling | Connection pooling |
| CORS fix | https://kodare.net/2021/04/04/django_react_and_cors.html | CORS guide |

---

*Last updated: 2026-06-17 | All findings backed by web_search + web_extract citations*