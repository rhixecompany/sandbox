# RESEARCH_REPORT.md

## Project: xamehi.tv

**Type:** Movie / media streaming site
**Tech Stack:** Django, Django REST Framework, SimpleJWT, React 17, Redux, Material-UI 4, React Bootstrap, react-admin 4, PayPal, video-react, Gunicorn, WhiteNoise
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| ecom | `projects/ecom` | Shared DRF + React admin and commerce-related UX. |
| xamehi | `projects/xamehi` | Legacy React + Django path dependencies. |
| rhixecompany-comics | `projects/rhixecompany-comics` | Dual-stack Django + Next.js; DRF + media patterns. |
| cookiecutter-django-tailwind | `projects/cookiecutter-django-tailwind` | Django 5.x production template security/settings. |

---

## Key Findings

### Legacy React 17 + DRF Streaming Platform (2026)

- **React 17 maintenance mode** — no automatic JSX transform; keep `import React from 'react'` unless upgraded; React 18+ required for concurrent features [1]
- **DRF + React 17 patterns** — `react-admin` for ops CRUD; custom React components for viewer-facing playback UI; separate route families [1]
- **Media catalog UX** — signed URL generation in DRF serializer (`get_video_url`) returns short-lived CDN links; never expose source storage paths [1]
- **Video metadata server-side** — serialize duration, thumbnails, HLS manifest in DRF to reduce client bundle pressure (`video-react` only on detail page) [1]

### SimpleJWT + django-allauth Authentication (2026)

- **SimpleJWT for DRF** — JWT access (5-15min) + refresh (1-7d) tokens; `JWT_AUTH_COOKIE` for HttpOnly cookie storage; rotation + blacklist on logout [2]
- **django-allauth for social/OAuth** — handles email verification, social login (Google, GitHub); headless mode for React SPA via `/api/auth/` endpoints [3]
- **Token strategy**: access token in memory (React), refresh in HttpOnly cookie; `axios` interceptor handles 401 → refresh → retry [3]
- **Stateful vs stateless**: database sessions (SimpleJWT `token_blacklist`) enable instant revoke; JWT-only = stateless but no revoke without blocklist [2]
- **Allauth + SimpleJWT integration** — custom adapter creates SimpleJWT tokens on allauth login; `JWT_AUTH_COOKIE` bridges both [3]

### Material-UI v4 → v5 Migration (React 2026)

- **Breaking changes**: JSS → Emotion (styled-components optional); `@material-ui/*` → `@mui/*` packages; `makeStyles` → `styled()`/`sx` prop [4]
- **Codemod automation** — `@mui/codemod` handles 80% of imports, props, theme changes; run per-module to catch errors incrementally [4]
- **React 17 minimum** — MUI v5 requires React 17+; upgrade React first, then MUI [4]
- **Theme migration** — `createMuiTheme` → `createTheme`; `theme.palette.type` → `theme.palette.mode`; spacing array → single value [4]
- **Coexistence strategy** — `UnifiedTheme` (Backstage) supports v4 + v5 simultaneously for gradual migration [5]

### Gunicorn + WhiteNoise Django Production (2026)

- **WhiteNoise limitations** — without CDN, large file downloads block Gunicorn workers; **always pair with CDN (Cloudflare, CloudFront)** or NGINX reverse proxy [6]
- **Static files only** — WhiteNoise serves `STATIC_ROOT`; media files → object storage (GCS/S3) + signed URLs; never serve media via Gunicorn [7]
- **Gunicorn config**: `workers = (2 * CPU) + 1`; `worker_class = "gevent"` for async; `--preload` for memory sharing; `timeout = 30` [6]
- **Docker multi-stage** — builder installs deps + `collectstatic`; runtime copies `STATIC_ROOT`; non-root user; `HEALTHCHECK` on `/health/` [6]
- **NGINX reverse proxy** — terminates SSL, gzip/brotli, rate limiting; proxies to Gunicorn; offloads static to CDN [6]

### React 17 → 18 + Redux Toolkit Migration (2026)

- **React 18 automatic batching** — multiple state updates in async callbacks batched automatically; reduces renders [8]
- **Concurrent features** — `useTransition`, `useDeferredValue`, `Suspense` for streaming; requires React 18+ [8]
- **Redux Toolkit v2 + RTK Query** — replaces hand-rolled Redux + thunks; auto-generates hooks, caching, invalidation [8]
- **Migration path**: 1) Upgrade React (`npm install react@18 react-dom@18`) 2) Test with `act()` warnings 3) Migrate Redux slices to `createSlice` 4) Replace thunks with RTK Query 5) Enable concurrent features [9]
- **React-Redux v9** requires React 18+; v8 supports React 17 but no concurrent features [9]

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| DRF + React MUI | https://github.com/mehfoozdev/User-Auth-App-React-MaterialUI-and-Django-DRF | Example |
| SimpleJWT docs | https://django-rest-framework-simplejwt.readthedocs.io | Docs |
| django-allauth JWT | https://docs.allauth.org/en/dev/headless/token-strategies/jwt-tokens.html | Docs |
| MUI v4→v5 migration | https://mui.com/material-ui/migration/migration-v4 | Docs |
| MUI migration guide | https://backstage.io/docs/tutorials/migrate-to-mui5 | Guide |
| WhiteNoise + Gunicorn | https://dev.to/doridoro/make-a-django-project-production-ready-create-a-docker-image-and-use-github-cicd-to-automate-the-push-of-the-docker-image-fm3 | Tutorial |
| WhiteNoise drawbacks | https://stackoverflow.com/questions/50318233/django-whitenoise-drawback | Discussion |
| React 18 migration | https://www.sardine.ai/engineering/react-18-migration-guide-production-infrastructure | Guide |
| Migrate React 17→18 | https://jahed.dev/2023/06/19/migrating-from-react-17-to-18 | Guide |
| Redux Toolkit 2025 | https://medium.com/@mernstackdevbykevin/redux-toolkit-best-practices-in-2025-the-complete-developers-guide-74de800bfa37 | Guide |

---

## Best Practices

1. **JWT refresh flow centralized** — axios interceptor handles 401 → POST `/api/auth/refresh/` → retry original request
2. **Restrict DRF write endpoints** — `IsAdminUser` or custom `IsStaff` permission; public reads limited to movies/metadata
3. **WhiteNoise + CDN mandatory** — Cloudflare/CloudFront in front; never serve media through Gunicorn
4. **Verify PayPal server-side** — capture order in DRF after inventory check; never trust client approval
5. **Signed media URLs** — DRF serializer generates short-lived CDN links; expired links return 403
6. **MUI v5 codemod per module** — `@mui/codemod v5.0.0/preset-safe` per package; test incrementally
7. **React 18 upgrade first** — enables concurrent features; run `npm install react@18 react-dom@18` + test suite
8. **Redux Toolkit + RTK Query** — replace hand-rolled Redux + thunks; auto-caching, `selectFromResult` for derived data
9. **Gunicorn behind NGINX** — SSL termination, gzip, rate limiting, static offload to CDN
10. **Video URL signing** — `django-signed-urls` or custom HMAC; 1hr TTL for premium content

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Trusting client playback status | Rights circumvention | Verify entitlements server-side before serving signed media URLs |
| Case-sensitive search in admin | Missed catalog entries | Normalize search terms: `q.lower()` + `TrigramSimilarity` |
| Material-UI + Bootstrap overlap | Inconsistent UI, bundle bloat | Choose one system per route family; standardize design tokens |
| SQLite in production | Capacity/durability issues | PostgreSQL required; `dj-database-url` for config |
| WhiteNoise serving large media | Gunicorn worker starvation | CDN + object storage for videos; WhiteNoise for static only |
| React 17 + MUI v5 | Broken hooks, missing features | Upgrade React 18 before MUI v5 |
| JWT in localStorage | XSS steals tokens | HttpOnly cookie (`JWT_AUTH_COOKIE`) + CSRF protection |
| PayPal approval = payment | Phantom premium access | DRF capture order after verification |
| `video-react` on home page | Bundle bloat, slow FCP | Lazy-load: `const VideoPlayer = lazy(() => import('./VideoPlayer'))` |

---

## Performance

1. **Cache movie metadata + top lists** — DRF `cache_page(60*5)` on listing views; invalidate on `post_save`
2. **Preload video player scripts on detail only** — `React.lazy` + `Suspense` for `video-react`; avoid shipping on home
3. **DRF pagination** — `PageNumberPagination(page_size=20)` for review lists; `CursorPagination` for large feeds
4. **NGINX gzip/brotli + Cache-Control** — `immutable, max-age=31536000` on React static build
5. **Redis session cache** — `django-redis` for SimpleJWT token blacklist; sub-ms lookups
6. **Gunicorn workers** — `(2 * CPU) + 1` with `gevent` worker class for async I/O
7. **Database indexing** — composite index on `(release_year, -rating)` for catalog queries

---

## Security

1. **Verify all JWT + PayPal webhook payloads** — `SimpleJWT` verification + PayPal webhook signature validation
2. **Environment secrets** — `SECRET_KEY`, `PAYPAL_CLIENT_ID`, `STRIPE_SECRET` in env/secret manager; never in compose
3. **Admin panel restricted** — `IsAdminUser` + IP allowlist middleware on `/admin/`, `/api/admin/`
4. **Django CSRF on forms** — `CsrfViewMiddleware` enabled; `react-admin` uses DRF session auth + CSRF
5. **Signed media URLs expire** — 1hr TTL; HMAC-SHA256 with rotating keys
6. **Content Security Policy** — `django-csp` with `script-src 'self'` for MUI emotion runtime
7. **Dependency scanning** — `pip-audit` + `npm audit` in CI; Renovate for auto-updates

---

## Related Projects (in workspace)

- **xamehi** — shared legacy React + Django architecture
- **ecom** — shared React + DRF admin/payment workflow
- **rhixecompany-comics** — dual-stack Django + Next.js; DRF + media patterns
- **cookiecutter-django-tailwind** — Django 5.x production template security/settings

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| DRF docs | https://www.django-rest-framework.org | API docs |
| django-allauth docs | https://docs.allauth.org | Auth docs |
| PayPal developer docs | https://developer.paypal.com/docs | Payments docs |
| Material-UI docs | https://mui.com/material-ui/getting-started/ | UI docs |
| video-react docs | https://video-react.js.org | Media player docs |
| WhiteNoise docs | https://whitenoise.readthedocs.io | Static file serving |
| SimpleJWT | https://django-rest-framework-simplejwt.readthedocs.io | JWT auth |
| React 18 migration | https://www.sardine.ai/engineering/react-18-migration-guide-production-infrastructure | Migration guide |
| MUI v4→v5 | https://mui.com/material-ui/migration/migration-v4 | Migration guide |

---

*Last updated: 2026-06-17 | All findings backed by web_search + web_extract citations*