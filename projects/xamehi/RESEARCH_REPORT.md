# RESEARCH_REPORT — xamehi

> **Type:** Project research report | **Updated:** 2026-07-10

**Type:** Legacy dual-backend app (Django + Express) + React frontend
**Tech Stack:** Django + DRF, Express, React 18/CRA, PostgreSQL, Axios
**Status:** Active (legacy — consolidation opportunity)

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| Django + React guide | <https://fdcservers.net/blog/how-to-build-a-simple-app-with-django-and-react> | Django + React CORS setup |
| CRA → Vite migration | <https://dev.to/solitrix02/goodbye-cra-hello-vite-a-developers-2026-survival-guide-for-migration-2a9f> | CRA deprecation; migration path |
| Stop using CRA | <https://medium.com/@thedevnotebook/stop-using-create-react-app-in-2026-next-js-and-vite-have-taken-over-a7c5ac59c4ce> | why modern React moves to Vite |

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
- **Migration guides**:
  - <https://oneuptime.com/blog/post/2026-01-15-migrate-create-react-app-to-vite/view>
  - <https://dev.to/solitrix02/goodbye-cra-hello-vite-a-developers-2026-survival-guide-for-migration-2a9f>
  - <https://adhithiravi.medium.com/migrating-from-create-react-app-to-vite-a-modern-approach-76148adb8983>
  - React official deprecation notice: <https://react.dev/blog/2025/02/14/sunsetting-create-react-app>

### Dual-Backend Architecture (Django + Express)

- Running Django (DRF) and Express requires careful CORS: `django-cors-headers` for Django, `cors` middleware for Express
- Three separate build/deploy steps in production: React build, Django collectstatic, Express deploy
- PostgreSQL connection pooling must be coordinated: Django `CONN_MAX_AGE`, Express `pg-pool`
- Port map must be documented: Express `:5000`, Django `:8000`, React `:3000`
- **Architecture patterns for dual-backend (2026)**:
  - Use API Gateway pattern: Express as API gateway routing to Django DRF for core business logic
  - Shared JWT secret for authentication between both backends
  - Shared PostgreSQL database with pgbouncer for connection pooling
  - Separate API contracts: `/api/django/*` → Django, `/api/express/*` → Express
  - Reference: <https://github.com/eofs/django-rest-framework-proxy> for DRF proxy patterns
  - API Gateway patterns: <https://oneuptime.com/blog/post/2026-01-30-microservices-api-gateway-patterns/view>
  - Best API gateways 2026: <https://zuplo.com/learning-center/best-api-gateways-2026>

### PostgreSQL Connection Pooling

- pgbouncer for shared DB connection pooling; prevents exhaustion from dual backends
- Django: `CONN_MAX_AGE` for persistent connections
- Express: `pg-pool` with appropriate `max` and `idleTimeoutMillis`
- **Critical pgbouncer + Django gotcha**: Transaction pooling mode requires disabling Django's server-side cursors
  - Django setting: `DISABLE_SERVER_SIDE_CURSORS = True`
  - Reference: <https://forum.djangoproject.com/t/configure-pgbouncer-with-django/43161>
- PgBouncer configuration guides:
  - <https://oneuptime.com/blog/post/2026-02-02-postgresql-pgbouncer-pooling/view>
  - <https://medium.com/@codermungan/the-connection-pooling-adventure-django-rate-limiting-and-pgbouncer-02fe1666dcaa>
- Multi-tenant PostgreSQL patterns: <https://clickhouse.com/resources/engineering/multi-tenant-saas-postgres-architecture>

### CORS and Proxy Configuration for Triple-Service Architecture

- **Three origins to manage**: React (`:3000`/`:5173`), Django (`:8000`), Express (`:5000`)
- **Development proxy strategy**:
  - CRA: `proxy` field in `package.json` (single backend only)
  - **Vite**: `server.proxy` in `vite.config.js` — supports multiple proxies
    ```js
    // vite.config.js
    export default defineConfig({
      server: {
        proxy: {
          '/api/django': { target: 'http://localhost:8000', changeOrigin: true, rewrite: p => p.replace(/^\/api\/django/, '') },
          '/api/express': { target: 'http://localhost:5000', changeOrigin: true, rewrite: p => p.replace(/^\/api\/express/, '') }
        }
      }
    })
    ```
  - Reference: <https://tere.ro/development/vite-s-proxy-overlooked-feature>, <https://medium.com/@eric_abell/simplifying-api-proxies-in-vite-a-guide-to-vite-config-js-a5cc3a091a2f>
- **Production CORS**:
  - Django: `django-cors-headers` with `CORS_ALLOWED_ORIGINS = ['https://yourdomain.com']`
  - Express: `cors({ origin: 'https://yourdomain.com', credentials: true })`
  - Reference: <https://www.freecodecamp.org/news/how-to-enable-cors-in-django>, <https://www.blueshoe.io/blog/django-cors-in-production>

### Django REST Framework + Express API Gateway Patterns

- Express can serve as API gateway: route `/api/auth` → Django, `/api/realtime` → Express
- DRF proxy package: <https://github.com/eofs/django-rest-framework-proxy> for proxying to external APIs
- Shared authentication: JWT tokens with shared secret, validated by both backends
- API contract maintenance: OpenAPI/Swagger specs shared between teams
- Consider NestJS instead of raw Express for better structure if keeping Node backend

### Gunicorn + Nodemon Development Workflow

- **Django dev**: `python manage.py runserver` (or gunicorn with `--reload` for production parity)
- **Express dev**: `nodemon index.js` for auto-reload
- **React dev**: `npm start` (CRA) → migrate to `npm run dev` (Vite)
- **Concurrent development**: Use `concurrently` or `npm-run-all`
  ```json
  "scripts": {
    "dev": "concurrently \"npm run dev:django\" \"npm run dev:express\" \"npm run dev:react\"",
    "dev:django": "python manage.py runserver 8000",
    "dev:express": "nodemon index.js",
    "dev:react": "vite"
  }
  ```
- **Production**: Gunicorn for Django (`gunicorn xamehi.wsgi:application --bind 0.0.0.0:8000`), PM2 or similar for Express
- Reference: <https://vxlabs.com/2015/12/08/gunicorn-as-your-django-development-server>

### Django + Express Dual-Backend Architecture Patterns (2026)

- **Consolidation recommended**: If Express handles low-traffic endpoints, migrate to DRF to reduce infrastructure
- **If keeping both**:
  - Shared database schema with clear ownership (Django migrations own schema)
  - Express uses raw SQL or Prisma/Drizzle with read-only access to Django-managed tables
  - API gateway pattern: Express handles WebSocket/realtime, Django handles CRUD/auth
  - Shared Redis for caching/sessions across both backends
- **Migration strategy**: Strangler Fig pattern — route new endpoints to Django, deprecate Express routes gradually
- Reference: <https://medium.com/@mmoznu/django-next-js-in-2026-when-to-split-your-frontend-and-backend-and-how-to-wire-them-together-23b4ef68b6df>

### React 18 + CRA → Vite Migration (Step-by-Step)

1. `npm create vite@latest frontend -- --template react`
2. Copy `src/` from CRA to new Vite project
3. Remove `react-scripts`, `@testing-library/react`, etc.
4. Update `package.json` scripts: `"dev": "vite"`, `"build": "vite build"`, `"preview": "vite preview"`
5. Add `vite.config.js` with proxy config for dual backend
6. Install `@vitejs/plugin-react-swc` for faster builds
7. Add `@svgr/rollup` for SVG imports
8. Update `index.html` to reference `/src/main.jsx`
9. Fix any `process.env` references → `import.meta.env.VITE_*`
10. Test HMR, build, preview
- Full guide: <https://dev.to/solitrix02/goodbye-cra-hello-vite-a-developers-2026-survival-guide-for-migration-2a9f>

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| CRA → Vite migration | <https://dev.to/solitrix02/goodbye-cra-hello-vite-a-developers-2026-survival-guide-for-migration-2a9f> | Step-by-step Guide |
| Django CORS | <https://pypi.org/project/django-cors-headers/> | Package |
| pgbouncer | <https://www.pgbouncer.org/> | Connection pooler docs |
| React 19 features | <https://react.dev/blog> | React official blog |
| Vite proxy config | <https://tere.ro/development/vite-s-proxy-overlooked-feature> | Guide |
| DRF proxy | <https://github.com/eofs/django-rest-framework-proxy> | Package |
| API Gateway patterns | <https://oneuptime.com/blog/post/2026-01-30-microservices-api-gateway-patterns/view> | Guide |
| Best API Gateways 2026 | <https://zuplo.com/learning-center/best-api-gateways-2026> | Comparison |

---

## Best Practices

1. **Migrate CRA to Vite** — faster builds, active maintenance, modern ESM support
2. **Consolidate APIs** — consider merging Express routes into Django DRF
3. **pgbouncer for shared DB** — prevent connection pool exhaustion from dual backends
4. **Unified CORS config** — single policy across Django and Express
5. **Document port mapping** — Express `:5000`, Django `:8000`, React `:3000` (dev) / `:5173` (Vite)
6. **Use Vite proxy for dev** — multiple proxy entries for `/api/django` and `/api/express`
7. **Shared JWT secret** — both backends validate same tokens; rotate regularly
8. **Strangler Fig migration** — route new endpoints to Django, deprecate Express gradually
9. **Concurrent dev script** — `concurrently` for running all three services
10. **Production process managers** — Gunicorn (Django), PM2 (Express), static hosting (React)

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| CRA deprecation | no security patches, slow builds | migrate to Vite |
| Dual backend drift | API inconsistency | consolidate API into DRF |
| DB connection exhaustion | application outages | pgbouncer with connection limits |
| Port confusion (3 services) | dev environment errors | document port mapping |
| CORS misconfiguration | blocked API calls | unified CORS origins list |
| Django server-side cursors + pgbouncer | transaction pooling breaks | `DISABLE_SERVER_SIDE_CURSORS = True` |
| Express unmaintained dependencies | security vulnerabilities | audit Express + middleware regularly |
| No shared authentication | auth inconsistency | shared JWT secret + validation lib |

---

## Performance

1. **Vite migration** — 10x faster HMR vs CRA's webpack dev server
2. **Consolidate API** — eliminate Express if low-traffic; reduce infrastructure overhead
3. **pgbouncer** — transaction pooling for high concurrency
4. **Django caching** — add Redis for frequently accessed API endpoints
5. **Vite production build** — Rollup-based, smaller bundles, code splitting
6. **Gunicorn workers** — tune `workers = 2 * CPU + 1` for Django
7. **Express clustering** — PM2 cluster mode for multi-core utilization
8. **PostgreSQL tuning** — `shared_buffers`, `effective_cache_size`, `work_mem`

---

## Security

1. **CORS hardening** — three services = three attack surfaces; restrict each to minimal origins
2. **Express dependency audit** — ensure Express + middleware up to date (legacy risk)
3. **JWT shared secret** — if both backends validate JWTs, rotate regularly
4. **HTTPS required** — all three endpoints (React, Django, Express) need TLS in production
5. **django-cors-headers** — use `CORS_ALLOWED_ORIGINS` not `CORS_ALLOW_ALL_ORIGINS`
6. **Rate limiting** — Django DRF throttling + Express rate-limiter middleware
7. **Security headers** — Helmet.js for Express, django-secure for Django
8. **Secrets management** — never commit `.env`; use Doppler/1Password/Vault

---

## Related Projects (in workspace)

- **xamehi.tv** — same Django + React pattern; xamehi adds Express backend
- **ecom** — simpler (single Django backend + React); xamehi is more complex
- **rhixecompany-comics** — another dual-service architecture (Django + Next.js)

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Vite migration | <https://dev.to/solitrix02/goodbye-cra-hello-vite-a-developers-2026-survival-guide-for-migration-2a9f> | CRA → Vite guide |
| DRF Docs | <https://www.django-rest-framework.org/> | DRF official docs |
| Express.js | <https://expressjs.com/> | Express web framework |
| pgbouncer | <https://www.pgbouncer.org/> | PostgreSQL connection pooler |
| django-cors-headers | <https://pypi.org/project/django-cors-headers/> | Django CORS package |
| Vite proxy | <https://vitejs.dev/config/server-options.html#server-proxy> | Vite proxy config |
| DRF proxy | <https://github.com/eofs/django-rest-framework-proxy> | DRF proxy views |
| API Gateway patterns | <https://oneuptime.com/blog/post/2026-01-30-microservices-api-gateway-patterns/view> | Microservices patterns |
| Best API Gateways 2026 | <https://zuplo.com/learning-center/best-api-gateways-2026> | Gateway comparison |
| Concurrently | <https://www.npmjs.com/package/concurrently> | Run multiple commands |
| PM2 | <https://pm2.keymetrics.io/> | Node process manager |

---

## New Research Added (2026-07-10)

### Vite Multi-Proxy Configuration for Triple-Service Dev
```js
// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
import svgr from '@svgr/rollup'

export default defineConfig({
  plugins: [react(), svgr()],
  server: {
    port: 5173,
    proxy: {
      '/api/django': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api\/django/, '')
      },
      '/api/express': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api\/express/, '')
      }
    }
  }
})
```

### Django Settings for pgbouncer Transaction Pooling
```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'PORT': 6432,  # pgbouncer port
        'CONN_MAX_AGE': 0,  # Disable persistent connections with pgbouncer
        'DISABLE_SERVER_SIDE_CURSORS': True,  # Required for transaction pooling
    }
}
```

### Express pg-pool Configuration
```javascript
// db.js
const { Pool } = require('pg')
const pool = new Pool({
  host: 'localhost',
  port: 6432,  // pgbouncer
  max: 20,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000,
})
module.exports = pool
```

### Consolidated API Migration Strategy
1. **Audit Express routes** — categorize by traffic/complexity
2. **Create DRF equivalents** — serializers, viewsets, routers
3. **Add proxy route in Express** — temporarily forward to Django
4. **Switch frontend calls** — update Axios base URLs
5. **Deprecate Express routes** — monitor, then remove
6. **Decommission Express** — remove from deploy pipeline