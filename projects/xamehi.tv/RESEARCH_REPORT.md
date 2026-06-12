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

---

## Key Findings

### Legacy React Upgrade Path
- React 17 means no automatic JSX transform; keep `React` import for compatibility unless upgraded.
- Plan migration to React 18 by replacing `react-redux` flow with Redux Toolkit and modern async thunks.

### Media Catalog UX
- `react-admin` works for simple CRUD but becomes brittle when media catalogs need custom playback UIs; use it for ops and React components for viewer-facing UI.
- Store video URLs in signed field storage or CDN-backed links; never expose source storage paths.

### DRF Media API
- Serialize `video-react` metadata server-side when possible to reduce client bundle pressure.
- Add DRF permissions that restrict admin mutations to staff.

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| DRF docs | https://www.django-rest-framework.org | Docs |
| django-allauth | https://docs.allauth.org | Auth docs |
| PayPal developer docs | https://developer.paypal.com/docs | Payments docs |
| Material-UI docs | https://mui.com/material-ui/getting-started/ | UI docs |
| video-react docs | https://video-react.js.org | Media player docs |

---

## Best Practices
1. Keep JWT refresh flow centralized in axios interceptors.
2. Restrict DRF write endpoints to authenticated staff; limit public reads to movies and metadata.
3. Use WhiteNoise only for static files; keep videos off WhiteNoise and on object storage/CDN.
4. Validate PayPal purchase completion server-side before granting premium access.

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Trusting client playback status | Rights circumvention | Verify entitlements server-side before serving signed media URLs. |
| Case-sensitive search in admin | Missed catalog entries | Normalize search terms before querying. |
| Material-UI + Bootstrap overlap | Inconsistent UI | Choose one system per route family and standardize design tokens. |
| Leaving dev database on SQLite in product | Capacity and durability issues | Switch to PostgreSQL in production. |

---

## Performance
1. Cache movie metadata and top lists in DRF views with short TTLs.
2. Preload video player scripts on detail pages only; avoid shipping `video-react` on the home page.
3. Use DRF pagination for review lists to keep responses small.

---

## Security
1. Verify all JWT and PayPal webhook payloads using official verify methods.
2. Keep `SECRET_KEY` and related production constants in environment variables.
3. Restrict admin panel to authenticated staff; enable Django CSRF protections on forms.

---

## Related Projects (in workspace)

- **xamehi** — shared legacy React + Django architecture
- **ecom** — shared React + DRF admin/payment workflow

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| DRF docs | https://www.django-rest-framework.org | API docs |
| django-allauth docs | https://docs.allauth.org | Auth docs |
| PayPal developer docs | https://developer.paypal.com/docs | Payments docs |
| Material-UI docs | https://mui.com/material-ui/getting-started/ | UI docs |
| WhiteNoise docs | https://whitenoise.readthedocs.io | Static file serving |
