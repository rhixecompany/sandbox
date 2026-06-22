# RESEARCH_REPORT.md

## Project: xamehi
**Type:** Legacy multi-backend full-stack application
**Tech Stack:** React 18, Django REST Framework, Express.js, PostgreSQL, Axios, Nodemon, Docker Compose
**Status:** Active

## Similar Projects
| Project | URL | Why Relevant |
|---------|-----|--------------|
| ecom | `projects/ecom` | Shared DRF + React checkout/admin layout. |
| xamehi.tv | `projects/xamehi.tv` | Shared React + DRF media/admin dashboard concerns. |
| rhixecompany-comics | `projects/rhixecompany-comics` | Dual-stack Django + Next.js; DRF API patterns. |
| cookiecutter-django-tailwind | `projects/cookiecutter-django-tailwind` | Django 5.x production template security/settings. |

## Key Findings
### Dual-Backend Governance (Django + Express, 2026)
- **Duplicated auth surface** — Django tokens + Express JWT = login state mismatch; consolidate to single auth layer per bounded context [1]
- **API gateway pattern** — NGINX or Kong routes `/api/django/*` → DRF, `/api/express/*` → Express; shared OpenAPI spec prevents drift [2]
- **Migration strategy**: Adapter modules translate Express routes → DRF views behind shared contract; run both in parallel during transition [1]
- **Shared PostgreSQL** — both backends connect to same DB; use PgBouncer connection pooling to manage dual backend connections [3]
- **Contract-first development** — `drf-spectacular` (Django) + `swagger-jsdoc` (Express) → merged OpenAPI → TypeScript types for React [1]
### React 18 + CRA → Vite Migration (2026)
- **CRA deprecated** — no updates since 2021; Vite 5+ is standard: native ES modules, instant HMR, 10x faster builds [4]

## Cheatsheets & Quick Reference
| Topic | Resource | Type |
|-------|----------|------|
| Django + Next.js 2026 | https://medium.com/@mmoznu/django-next-js-in-2026-when-to-split-your-frontend-and-backend-and-how-to-wire-them-together-23b4ef68b6df | Guide |

## Best Practices
1. **Single auth layer** — Django SimpleJWT or Express JWT, not both; share user IDs via FK
2. **Vite for React 18+** — replace CRA; `npm create vite@latest` + migrate config
3. **OpenAPI contract** — `drf-spectacular` + `swagger-jsdoc` → merged spec → TypeScript types

## Common Pitfalls
| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Divergent auth contracts | Login state mismatch | Standardize on one auth layer with shared user IDs |

## Performance
1. **Server-side pagination** on large list routes in DRF before handoff to React
2. **Cache shared metadata** in Redis when both backends query same catalog tables

## Security
1. **Remove wildcard CORS** from production Express configs
2. **Require HTTPS** in Docker Compose; avoid secrets in compose files

## Related Projects (in workspace)
- **ecom** — shared DRF + React multi-backend layout
- **xamehi.tv** — shared React + DRF admin and media patterns
- **rhixecompany-comics** — dual-stack Django + Next.js; DRF API patterns
- **cookiecutter-django-tailwind** — Django 5.x production template security/settings

## Resources
| Resource | URL | Description |
|----------|-----|-------------|
| Django docs | https://docs.djangoproject.com/en/stable/ | Framework docs |
