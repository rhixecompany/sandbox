# RESEARCH_REPORT.md

## Project: xamehi.tv

**Type:** Movie & TV series streaming platform
**Tech Stack:** Django 4.x, DRF, SimpleJWT, React 17, Redux (Thunk), Material-UI 4, React Bootstrap, react-admin 4, PostgreSQL, video-react, PayPal, django-allauth, Gunicorn
**Status:** Active (deployed at xamehi.tv)

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| Streaming Platform (DRF+React) | https://github.com/p-schlickmann/streaming-platform | Same DRF + React architecture |

## Key Findings

### DRF + React Streaming (2026)
- DRF ViewSets + ModelSerializers remain the standard approach for REST APIs in Django media platforms
- React 17 is a mature, stable choice for long-lived SPAs — no breaking upgrade pressure yet
- The dual-database pattern (PostgreSQL + MongoDB) supports structured data + analytics separately

### Material-UI 4 + react-admin
- react-admin 4 provides out-of-the-box CRUD UIs with `ra-data-simple-rest` for DRF backends
- Material-UI 4 is LTS and stable, but MUI 5 offers improved theming and performance

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| DRF Docs | https://www.django-rest-framework.org | Official Docs |
| React 17 | https://17.reactjs.org | Docs |
| Material-UI 4 | https://v4.mui.com | UI Framework |

## Best Practices

1. **JWT authentication** — SimpleJWT + Blacklist model for token revocation
2. **Redux Thunk pattern** — REQUEST/SUCCESS/FAIL action triad for async state handling
3. **Separate admin + API auth** — Django admin for internal users, JWT for API consumers
4. **Proxy in CRA** — `"proxy": "http://127.0.0.1:8000"` simplifies development CORS
5. **react-admin CRUD** — Consistent patterns for user/movie/series management

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| React 17 without concurrent features | No streaming SSR or Suspense | Plan upgrade to React 18/19 for new features |
| video-react on direct file URLs | No adaptive bitrate streaming | Consider HLS.js for long-form content |
| hybrid Django session + JWT auth | Confusion between auth systems | Document which auth is used where |
| Material-UI 4 deprecated | No new features/security patches | Plan migration to MUI 5 or 6 |

## Performance

1. **DRF pagination** reduces payload size for movie/series listings
2. **Redux memoization** via `connect()` prevents unnecessary re-renders
3. **CRA build optimizes** JS bundle via Webpack tree-shaking and code splitting
4. **PostgreSQL indexing** on search fields improves query performance
5. **Gunicorn worker scaling** for concurrent user requests

## Security

1. **JWT tokens** with short expiry and refresh rotation
2. **Django CSRF & XSS protections** enabled by default
3. **PayPal client ID** server-side only — never in client bundle
4. **restrict CORS_ALLOWED_ORIGINS** to frontend domain in production
5. **Never commit SECRET_KEY** or database credentials

## Related Projects (in workspace)

- **xamehi** — Django DRF + React 18, shares DRF/React integration patterns
- **ecom** — Django DRF + React 18 + PayPal, shares payment integration model
- **rhixecompany-comics** — Django + Next.js 16, shares Django backend architecture
- **profile** — Django blog CMS with GCS, shares Django deployment patterns

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Django REST Framework | https://www.django-rest-framework.org | REST API framework |
| SimpleJWT | https://django-rest-framework-simplejwt.readthedocs.io | JWT auth plugin |
| Material-UI 4 | https://v4.mui.com | UI component library |
| react-admin | https://marmelab.com/react-admin | Admin panel framework |
