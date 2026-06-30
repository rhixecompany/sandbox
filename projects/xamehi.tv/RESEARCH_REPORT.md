# RESEARCH_REPORT — xamehi.tv

> **Type:** Project research report | **Updated:** 2026-06-29

**Type:** Django REST + React streaming platform
**Tech Stack:** Django DRF, React 17, MUI 4, Redux, SimpleJWT, django-allauth, PostgreSQL, PayPal
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| DRF + SimpleJWT auth | https://www.django-rest-framework.org/api-guide/authentication/ | DRF JWT authentication |
| MUI v4 → v5 migration | https://mui.com/material-ui/migration/migration-v4/ | Material-UI v4 to v5 migration |

---

## Key Findings

### DRF + SimpleJWT Auth
- djangorestframework-simplejwt: access + refresh token pattern with token blacklist
- django-allauth adds social auth; requires careful URL namespace config to avoid SimpleJWT conflicts
- WorkOS emerging as enterprise SSO/SCIM alternative (2026)

### React 17 + Material-UI 4 Upgrade Path
- MUI v4 uses JSS; v5 replaces with Emotion — biggest breaking change (mui.com)
- Codemods automate 80% of migration: `npx @mui/codemod v5.0.0/preset-safe`
- React 17 → 18: auto-batching and `createRoot()` are key diffs; mostly backward compatible
- Redux Toolkit + RTK Query recommended over redux-thunk

### Production Serving
- Gunicorn + WhiteNoise standard for small-to-medium Django apps
- WhiteNoise auto-generates versioned static files with MD5 hashes
- For larger deployments, replace with nginx/CDN

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| MUI v4→v5 migration | https://mui.com/material-ui/migration/migration-v4/ | Migration Guide |
| React 18 upgrade | https://react.dev/blog/2022/03/08/react-18-upgrade-guide | Guide |
| DRF SimpleJWT | https://django-rest-framework-simplejwt.readthedocs.io/ | Docs |

---

## Best Practices

1. **Upgrade React 17→18** — auto-batching, Concurrent Features; mostly backward compatible
2. **Migrate MUI v4→v5** — use codemods; Emotion replaces JSS
3. **RTK Query** — replace redux-thunk for API data fetching and caching
4. **JWT security** — short-lived access tokens (5–15 min), refresh rotation; memory storage only
5. **CORS restriction** — django-cors-headers with explicit allowed origins

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| MUI v4 JSS → Emotion | Styling breaks | Use codemods |
| React createRoot missing | App won't render | Update to `createRoot()` |
| SimpleJWT + allauth URL conflicts | Auth routes clash | Namespace allauth URLs |
| CORS + proxy confusion | Frontend can't reach backend | Test production config early |

---

## Performance

1. **React 18 auto-batching** — fewer re-renders in async contexts
2. **RTK Query caching** — built-in invalidation and deduplication
3. **MUI v5 Emotion** — smaller runtime than JSS
4. **Gunicorn + WhiteNoise** — sufficient for moderate traffic; CDN for video

---

## Security

1. **SimpleJWT token blacklist** — enable to revoke compromised refresh tokens
2. **PayPal webhook verification** — validate signatures before processing
3. **django-allauth** — restrict allowed social providers; whitelist callback URLs
4. **CORS restriction** — limit to frontend domain only

---

## Related Projects (in workspace)

- **ecom** — shares DRF + PayPal + React; uses React 18/Redux Toolkit (more modern)
- **profile** — Django monolith; xamehi.tv adds React frontend
- **rhixecompany-comics** — dual-stack platform; xamehi.tv is simpler (single Django)
- **selenium_webdriver** — browser automation with Selenium
- **xamehi** — same Django + React pattern; xamehi adds Express backend

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| React 18 Docs | https://react.dev/ | React official documentation |
| MUI v5 | https://mui.com/ | Material-UI v5 documentation |
| SimpleJWT | https://django-rest-framework-simplejwt.readthedocs.io/ | DRF JWT auth docs |
| django-allauth | https://docs.allauth.org/ | Social auth integration |
| PayPal Developer | https://developer.paypal.com/ | PayPal API documentation |
