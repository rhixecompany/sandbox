# RESEARCH_REPORT.md

## Project: ecom

**Type:** Ecommerce platform
**Tech Stack:** Django REST Framework, Django, React, Redux, PostgreSQL, PayPal, Docker Compose
**Status:** Active, pending frontend stack refresh

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| xamehi | `projects/xamehi` | Shared Django + React multi-service setup. |
| xamehi.tv | `projects/xamehi.tv` | Shared DRF + React shopping flow and admin management. |
| rhixecompany-comics | `projects/rhixecompany-comics` | Dual-stack Django + Next.js; DRF + React admin patterns. |
| cookiecutter-django-tailwind | `projects/cookiecutter-django-tailwind` | Django 5.x production template security/settings. |

---

## Key Findings

### DRF + React Ecommerce Architecture (2026)

- **React + Django/DRF remains solid** in 2026 for ecommerce — robust, battle-tested, AI-compatible stack with clear separation of concerns [1]
- **DRF ViewSets + SimpleRouter** standard for product/order flows; `drf-nested-routers` recommended for order items to enable safe child resource mutations [1]
- **Token-based auth** (DRF) or **SimpleJWT** preferred over sessions for stateless React clients; avoid mixing session and JWT auth [2]
- **API versioning** via URL path (`/api/v1/`) is most common and visible approach; DRF built-in supports namespace, query param, header schemes [3]
- **Pagination + filtering + throttling** built into DRF Generic ViewSets; use `PageNumberPagination` with `DjangoFilterBackend` + `SearchFilter` + `OrderingFilter` [3]

### PayPal Integration (Django + React, 2026)

- **PayPal Checkout (Orders API v2)** is the modern standard — JavaScript SDK on frontend, REST Orders API on backend, webhooks replace IPN [4]
- **Server-side capture mandatory**: create order → client approves → Django calls `/v2/checkout/orders/{id}/capture` → verify webhook before fulfillment [4]
- **Smart Payment Buttons** render on React; Django returns `order_id` to client; never treat approval as payment completion [4]
- **dj-paypal** package provides Django models mirroring PayPal objects; sync plans via management commands [5]

### Redux Toolkit + RTK Query (Performance, 2026)

- **RTK Query** (included in Redux Toolkit) replaces manual async thunks + reducers for server state — auto-generates hooks, caching, invalidation [6]
- **4-layer state model**: URL state → Server state (RTK Query) → Client state (Zustand/Redux) → Ephemeral state (React state) — never store server state in client stores [6]
- **RTK Query vs React Query**: RTK Query excels in Redux-centric apps; React Query more flexible for non-Redux projects [6]
- **Performance patterns**: `keepUnusedDataFor` cache lifetime, `selectFromResult` for derived data, `refetchOnMountOrArgChange` for freshness [6]

### DRF API Versioning, Pagination, Filtering (2026)

- **URL path versioning** (`/api/v1/`) most common; configure `DEFAULT_VERSIONING_CLASS` + `DEFAULT_VERSION` + `ALLOWED_VERSIONS` in settings [3]
- **Pagination**: `PageNumberPagination` + `page_size_query_param` for client control; `CursorPagination` for large datasets [3]
- **Filtering**: `DjangoFilterBackend` + `filterset_fields`/`FilterSet` class; `SearchFilter` for text search; `OrderingFilter` for sorting [3]
- **Throttling**: `AnonRateThrottle` + `UserRateThrottle` per viewset; `ScopedRateThrottle` for granular limits [3]

### Docker Compose Django + React Production (2026)

- **NGINX reverse proxy** pattern: serves React static build, proxies `/api/` to Gunicorn/Django; eliminates CORS in production [7]
- **Multi-stage Dockerfiles**: builder stage for React (`npm run build` → `nginx`), Python stage for Django (`gunicorn + whitenoise`) [7]
- **Separate compose files**: `docker-compose.yml` (dev, hot reload) + `docker-compose.prod.yml` (SSL via Certbot, no dev deps) [7]
- **PostgreSQL + Redis** as services; health checks on DB/Redis before app starts; `depends_on` with `condition: service_healthy` [7]

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| DRF tutorial 2026 | https://tech-insider.org/django-rest-framework-tutorial-python-api-2026 | Guide |
| DRF API versioning | https://oneuptime.com/blog/post/2026-02-02-django-api-versioning/view | Guide |
| PayPal + Django | https://micropyramid.com/blog/e-commerce-paypal-integration-with-django | Guide |
| PayPal + Django + React | https://justdjango.com/blog/django-react-paypal-payments | Tutorial |
| RTK Query basics | https://redux.js.org/tutorials/essentials/part-7-rtk-query-basics | Docs |
| Redux Toolkit 2025 | https://medium.com/@mernstackdevbykevin/redux-toolkit-best-practices-in-2025-the-complete-developers-guide-74de800bfa37 | Guide |
| Docker Django React | https://www.honeybadger.io/blog/docker-django-react | Tutorial |
| Docker Compose Nginx SSL | https://saasitive.com/tutorial/docker-compose-django-react-nginx-let-s-encrypt | Tutorial |
| DRF versioning docs | https://www.django-rest-framework.org/api-guide/versioning | Docs |
| dj-paypal GitHub | https://github.com/HearthSim/dj-paypal | Package |

---

## Best Practices

1. **Server-side PayPal capture** — complete capture in DRF after inventory/order validation; avoid bank-state desync
2. **DRF nested endpoints** — use `drf-nested-routers` for order items so frontend can mutate child resources safely
3. **Media via Django in dev only** — serve media through Django when debugging; prefer S3/CDN or WhiteNoise in production
4. **Read model for carts** — compute cart totals on server and return finalized totals to client
5. **Audit admin actions** — log order status changes with user, timestamp, and prior state
6. **RTK Query for server state** — replace manual thunks; auto-caching, invalidation, optimistic updates
7. **API versioning from day one** — URL path versioning (`/api/v1/`) enables backward-compatible evolution
8. **NGINX reverse proxy in production** — serves React build, proxies API, terminates SSL; no CORS needed
9. **Multi-stage Docker builds** — separate builder/runtime stages; non-root users; minimal attack surface
10. **Database-backed sessions for cart durability** — anonymous carts persist across browser sessions

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| PayPal approval treated as payment | Phantom paid orders | Require DRF capture success before order paid status |
| Frontend-only quantity math | Inventory race conditions | Validate stock on server before confirming line items |
| Django media path leaks between envs | Mixed dev/prod uploads | Use environment-specific media roots |
| Redundant cart state | Sync bugs | Treat DRF cart endpoint as source of truth |
| No API versioning | Breaking changes in prod | Enable DRF versioning from project start |
| CORS in production | Security/performance overhead | NGINX reverse proxy serves both frontend + API |
| Missing webhook verification | Fraudulent order completion | Verify PayPal webhook signatures before fulfillment |
| React dev server in prod | Slow, insecure | Build static assets; serve via NGINX/WhiteNoise |
| Hardcoded API URLs | Environment coupling | Load base URL from env in both client + server |
| Sequential migration without guard | Data drift | Require migration plan before merging backend changes |

---

## Performance

1. **`select_related()` + `prefetch_related()`** for product categories, order items — eliminates N+1
2. **Cache category trees** with Redis when catalog changes infrequently (TTL 1hr)
3. **Database-backed sessions** for cart durability across anonymous sessions
4. **RTK Query cache** — `keepUnusedDataFor: 60*60` (1hr) for product listings
5. **CursorPagination** for large order histories — avoids OFFSET/LIMIT degradation
6. **NGINX gzip/brotli + Cache-Control** on React static assets — `immutable, max-age=31536000`
7. **Gunicorn workers** = `(2 * CPU cores) + 1`; `--preload` for memory sharing

---

## Security

1. **Verify PayPal webhook signatures** before applying capture events — use `dj-paypal` verification or manual HMAC
2. **CSRF on all DRF session-authenticated mutations** — disable unsafe browser exposure for write endpoints
3. **Validate uploaded product images** — limit sizes, scan MIME types, strip EXIF
4. **Record admin action log** for order refunds/cancellations — preserve financial audit trail
5. **JWT short expiry + refresh rotation** — 15min access, 7d refresh; revoke on password change
6. **NGINX rate limiting** — `limit_req_zone` on `/api/` endpoints (100 req/min per IP)
7. **Content Security Policy** — `django-csp` in REPORT_ONLY first, then enforce
8. **Environment secrets** — `django-environ` + `.env` never committed; Vercel/AWS secrets for prod

---

## Related Projects (in workspace)

- **xamehi** — shared Django + React multi-service layout and backend concerns
- **xamehi.tv** — shared DRF + React media/admin experience
- **rhixecompany-comics** — dual-stack Django + Next.js; DRF + React admin patterns
- **cookiecutter-django-tailwind** — Django 5.x production template security/settings
- **profile** — CKEditor + GCS media patterns

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| DRF docs | https://www.django-rest-framework.org | Official documentation |
| Django admin docs | https://docs.djangoproject.com/en/stable/ref/contrib/admin/ | Admin reference |
| PayPal dev docs | https://developer.paypal.com/docs | Payments |
| Redux Toolkit | https://redux-toolkit.js.org | Frontend state |
| WhiteNoise docs | https://whitenoise.readthedocs.io | Static/media serving |
| DRF versioning | https://www.django-rest-framework.org/api-guide/versioning | Versioning guide |
| dj-paypal | https://github.com/HearthSim/dj-paypal | PayPal Django integration |
| RTK Query docs | https://redux-toolkit.js.org/rtk-query/overview | Data fetching |
| Docker Django React | https://github.com/cglusky/docker-django-react | Full-stack template |

---

*Last updated: 2026-06-17 | All findings backed by web_search + web_extract citations*