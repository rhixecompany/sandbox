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

---

## Key Findings

### Dual-Backend Governance
- Having both Django and Express means duplicated auth and search surface; consolidate to one API per bounded context.
- Use axios interceptors with environment-driven base URLs to avoid hardcoding localhost across branches.

### Modernization Path
- Create adapter modules that translate Express routes into DRF views so migration can happen behind a shared contract.
- Introduce shared OpenAPI output on both sides in parallel to find contract drift before merging them.

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Django docs | https://docs.djangoproject.com/en/stable/ | Docs |
| DRF docs | https://www.django-rest-framework.org | Docs |
| Express docs | https://expressjs.com/en/resources/getting-started.html | Docs |
| React docs | https://react.dev/learn | Docs |

---

## Best Practices
1. Use one auth layer; either DRF tokens or Express JWT, not both.
2. Validate request payloads on both Express and DRF even when one proxies the other.
3. Remove dead CORS wildcards in Express and replace with explicit callers.
4. Use container health checks so Django and Express do not start during transient migration failures.

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Divergent auth contracts | Login state mismatch across backends | Standardize on one auth path with shared user ids. |
| Localhost port assumptions | Works in one branch only | Load API base URL from environment in both clients. |
| Release without migration guard | Data drift | Require migration plan before merging backend changes. |

---

## Performance
1. Use server-side pagination on large list routes in DRF before handoff to React.
2. Cache shared metadata lookups in Redis when both backends query the same catalog tables.
3. Prefer `select_related()` optimized DRF queries to avoid N+1 in admin views.

---

## Security
1. Remove wildcard CORS from production Express configs.
2. Require HTTPS in Docker Compose services and avoid storing secrets in compose files.
3. Enforce Django `SECRET_KEY` loaded from env everywhere; remove warning branches.
4. Use separate read and write database users at scale; restrict admin access.

---

## Related Projects (in workspace)

- **ecom** — shared DRF + React multi-backend layout
- **xamehi.tv** — shared React + DRF admin and media patterns

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Django docs | https://docs.djangoproject.com/en/stable/ | Framework docs |
| DRF docs | https://www.django-rest-framework.org | API docs |
| Express docs | https://expressjs.com/en/resources/getting-started.html | Runtime docs |
| React docs | https://react.dev/learn | Frontend docs |
