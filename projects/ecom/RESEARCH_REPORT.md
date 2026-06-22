# RESEARCH_REPORT.md

## Project: ecom
**Type:** Ecommerce platform
**Tech Stack:** Django REST Framework, Django, React, Redux, PostgreSQL, PayPal, Docker Compose
**Status:** Active, pending frontend stack refresh

## Similar Projects
| Project | URL | Why Relevant |
|---------|-----|--------------|
| xamehi | `projects/xamehi` | Shared Django + React multi-service setup. |
| xamehi.tv | `projects/xamehi.tv` | Shared DRF + React shopping flow and admin management. |
| rhixecompany-comics | `projects/rhixecompany-comics` | Dual-stack Django + Next.js; DRF + React admin patterns. |
| cookiecutter-django-tailwind | `projects/cookiecutter-django-tailwind` | Django 5.x production template security/settings. |

## Key Findings
### DRF + React Ecommerce Architecture (2026)
- **React + Django/DRF remains solid** in 2026 for ecommerce — robust, battle-tested, AI-compatible stack with clear separation of concerns [1]
- **DRF ViewSets + SimpleRouter** standard for product/order flows; `drf-nested-routers` recommended for order items to enable safe child resource mutations [1]
- **Token-based auth** (DRF) or **SimpleJWT** preferred over sessions for stateless React clients; avoid mixing session and JWT auth [2]
- **API versioning** via URL path (`/api/v1/`) is most common and visible approach; DRF built-in supports namespace, query param, header schemes [3]
- **Pagination + filtering + throttling** built into DRF Generic ViewSets; use `PageNumberPagination` with `DjangoFilterBackend` + `SearchFilter` + `OrderingFilter` [3]
### PayPal Integration (Django + React, 2026)
- **PayPal Checkout (Orders API v2)** is the modern standard — JavaScript SDK on frontend, REST Orders API on backend, webhooks replace IPN [4]

## Cheatsheets & Quick Reference
| Topic | Resource | Type |
|-------|----------|------|
| DRF tutorial 2026 | https://tech-insider.org/django-rest-framework-tutorial-python-api-2026 | Guide |

## Best Practices
1. **Server-side PayPal capture** — complete capture in DRF after inventory/order validation; avoid bank-state desync
2. **DRF nested endpoints** — use `drf-nested-routers` for order items so frontend can mutate child resources safely
3. **Media via Django in dev only** — serve media through Django when debugging; prefer S3/CDN or WhiteNoise in production

## Common Pitfalls
| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| PayPal approval treated as payment | Phantom paid orders | Require DRF capture success before order paid status |

## Performance
1. **`select_related()` + `prefetch_related()`** for product categories, order items — eliminates N+1
2. **Cache category trees** with Redis when catalog changes infrequently (TTL 1hr)

## Security
1. **Verify PayPal webhook signatures** before applying capture events — use `dj-paypal` verification or manual HMAC
2. **CSRF on all DRF session-authenticated mutations** — disable unsafe browser exposure for write endpoints

## Related Projects (in workspace)
- **xamehi** — shared Django + React multi-service layout and backend concerns
- **xamehi.tv** — shared DRF + React media/admin experience
- **rhixecompany-comics** — dual-stack Django + Next.js; DRF + React admin patterns
- **cookiecutter-django-tailwind** — Django 5.x production template security/settings
- **profile** — CKEditor + GCS media patterns

## Resources
| Resource | URL | Description |
|----------|-----|-------------|
| DRF docs | https://www.django-rest-framework.org | Official documentation |
