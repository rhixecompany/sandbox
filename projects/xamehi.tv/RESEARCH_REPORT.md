# RESEARCH_REPORT — xamehi.tv

> **Type:** Project research report | **Updated:** 2026-06-25

---

**Type:** Django REST + React streaming platform
**Tech Stack:** Django DRF, React 17, MUI 4, Redux, SimpleJWT, django-allauth, PostgreSQL, PayPal
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
| ------- | --- | ------------ |
| DRF + SimpleJWT auth | https://www.django-rest-framework.org/api-guide/authentication/ | DRF JWT authentication docs |
| MUI v4 → v5 migration | https://mui.com/material-ui/migration/migration-v4/ | Material-UI v4 to v5 migration guide |

---

## Key Findings

### DRF + SimpleJWT Auth

- djangorestframework-simplejwt is the most popular JWT auth package for DRF; supports access + refresh token pattern and token blacklist (django-rest-framework.org, 2026)
- django-allauth provides social auth (Google, GitHub) alongside SimpleJWT; requires careful URL namespace configuration to avoid conflicts
- WorkOS (2026) is emerging as an enterprise auth alternative, offering SSO, SCIM, and directory sync out of the box (workos.com, 2026)

### React 17 + Material-UI 4 Upgrade Path

- Material-UI v4 uses JSS for styling; v5 replaces it with Emotion — this is the biggest breaking change in the migration (mui.com)
- Codemods automate 80% of the MUI v4→v5 migration: `npx @mui/codemod v5.0.0/preset-safe` (mui.com)
- React 17 → React 18 migration: no major breaking changes to existing APIs; upgraded `ReactDOM.createRoot()` and automatic batching are key differences (jahed.dev, 2026)
- Redux Toolkit with RTK Query is recommended over classic Redux + redux-thunk for new development (medium.com/@mernstackdevbykevin, 2026)

### Production Serving

- Gunicorn + WhiteNoise is the standard Django production serving stack for small-to-medium applications (reddit.com/r/django)
- WhiteNoise automatically generates versioned static files with MD5 hashes and appropriate Cache-Control headers (reddit.com/r/django)
- For larger deployments, replace WhiteNoise with nginx/CDN for static/media serving

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
| ----- | -------- | ---- |
| MUI v4→v5 migration | https://mui.com/material-ui/migration/migration-v4/ | Migration Guide |
| React 18 upgrade | https://react.dev/blog/2022/03/08/react-18-upgrade-guide | Guide |
| DRF SimpleJWT | https://django-rest-framework-simplejwt.readthedocs.io/ | Docs |

---

## Best Practices

1. **Upgrade React 17→18** — Automatic batching, Concurrent Features, and Suspense improvements; mostly backward compatible
2. **Migrate MUI v4→v5** — Emotion over JSS, improved theming, better TypeScript support; use codemods for efficiency
3. **Redux Toolkit migration** — Replace redux-thunk with RTK Query for API data fetching and cache management
4. **JWT security** — Short-lived access tokens (5–15 min), long-lived refresh tokens with rotation; store in memory not localStorage

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
| ------- | ------ | --------- |
| MUI v4 JSS → Emotion breakage | Styling completely broken after upgrade | Use codemods; run `npx @mui/codemod v5.0.0/preset-safe` |
| React 17 createRoot missing | App doesn't render | Update to `createRoot()` API for React 18 |
| SimpleJWT + allauth URL conflicts | Auth routes clash | Carefully namespace allauth URLs under `/accounts/` |
| CORS + proxy confusion | Frontend can't reach backend | Document CORS + proxy setup; test with production config early |

---

## Performance

1. **React 18 automatic batching** — Fewer re-renders in promises and timeouts, improving UI responsiveness
2. **RTK Query caching** — Replaces manual redux-thunk fetching; built-in cache invalidation and deduplication
3. **MUI v5 Emotion** — Smaller runtime vs JSS; `styled()` API enables cleaner component composition
4. **Gunicorn + WhiteNoise** — Sufficient for moderate traffic; CDN recommended for video assets

---

## Security

1. **SimpleJWT token blacklist** — Enable blacklist app to revoke compromised refresh tokens server-side
2. **PayPal webhook verification** — Validate PayPal webhook signatures to prevent fraudulent payment callbacks
3. **django-allauth social auth** — Configure callback URL whitelist; restrict allowed social providers
4. **CORS restriction** — django-cors-headers with `CORS_ALLOWED_ORIGINS` limited to frontend domain

---

## Related Projects (in workspace)

- **ecom** — Shares DRF + PayPal + React stack; ecom uses React 18/Redux Toolkit (more modern)
- **xamehi** — Shares Django + React pattern; xamehi has dual backends (Django + Express)
- **rhixecompany-comics** — Dual-stack platform; xamehi.tv is simpler (single Django backend)
- **profile** — Django monolith; both use Django but xamehi.tv adds React frontend

---

## Resources

| Resource | URL | Description |
| -------- | --- | ----------- |
| React 18 Docs | https://react.dev/ | React official documentation |
| Material-UI v5 | https://mui.com/ | MUI v5 documentation |
| SimpleJWT | https://django-rest-framework-simplejwt.readthedocs.io/ | DRF JWT auth docs |
| django-allauth | https://docs.allauth.org/ | Social auth integration |
| PayPal Developer | https://developer.paypal.com/ | PayPal API documentation |