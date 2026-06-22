# RESEARCH_REPORT.md

## Project: xamehi.tv
**Type:** Movie / media streaming site
**Tech Stack:** Django, Django REST Framework, SimpleJWT, React 17, Redux, Material-UI 4, React Bootstrap, react-admin 4, PayPal, video-react, Gunicorn, WhiteNoise
**Status:** Active

## Similar Projects
| Project | URL | Why Relevant |
|---------|-----|--------------|
| ecom | `projects/ecom` | Shared DRF + React admin and commerce-related UX. |
| xamehi | `projects/xamehi` | Legacy React + Django path dependencies. |
| rhixecompany-comics | `projects/rhixecompany-comics` | Dual-stack Django + Next.js; DRF + media patterns. |
| cookiecutter-django-tailwind | `projects/cookiecutter-django-tailwind` | Django 5.x production template security/settings. |

## Key Findings
### Legacy React 17 + DRF Streaming Platform (2026)
- **React 17 maintenance mode** — no automatic JSX transform; keep `import React from 'react'` unless upgraded; React 18+ required for concurrent features [1]
- **DRF + React 17 patterns** — `react-admin` for ops CRUD; custom React components for viewer-facing playback UI; separate route families [1]
- **Media catalog UX** — signed URL generation in DRF serializer (`get_video_url`) returns short-lived CDN links; never expose source storage paths [1]
- **Video metadata server-side** — serialize duration, thumbnails, HLS manifest in DRF to reduce client bundle pressure (`video-react` only on detail page) [1]
### SimpleJWT + django-allauth Authentication (2026)
- **SimpleJWT for DRF** — JWT access (5-15min) + refresh (1-7d) tokens; `JWT_AUTH_COOKIE` for HttpOnly cookie storage; rotation + blacklist on logout [2]
- **django-allauth for social/OAuth** — handles email verification, social login (Google, GitHub); headless mode for React SPA via `/api/auth/` endpoints [3]

## Cheatsheets & Quick Reference
| Topic | Resource | Type |
|-------|----------|------|
| DRF + React MUI | https://github.com/mehfoozdev/User-Auth-App-React-MaterialUI-and-Django-DRF | Example |

## Best Practices
1. **JWT refresh flow centralized** — axios interceptor handles 401 → POST `/api/auth/refresh/` → retry original request
2. **Restrict DRF write endpoints** — `IsAdminUser` or custom `IsStaff` permission; public reads limited to movies/metadata
3. **WhiteNoise + CDN mandatory** — Cloudflare/CloudFront in front; never serve media through Gunicorn

## Common Pitfalls
| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Trusting client playback status | Rights circumvention | Verify entitlements server-side before serving signed media URLs |

## Performance
1. **Cache movie metadata + top lists** — DRF `cache_page(60*5)` on listing views; invalidate on `post_save`
2. **Preload video player scripts on detail only** — `React.lazy` + `Suspense` for `video-react`; avoid shipping on home

## Security
1. **Verify all JWT + PayPal webhook payloads** — `SimpleJWT` verification + PayPal webhook signature validation
2. **Environment secrets** — `SECRET_KEY`, `PAYPAL_CLIENT_ID`, `STRIPE_SECRET` in env/secret manager; never in compose

## Related Projects (in workspace)
- **xamehi** — shared legacy React + Django architecture
- **ecom** — shared React + DRF admin/payment workflow
- **rhixecompany-comics** — dual-stack Django + Next.js; DRF + media patterns
- **cookiecutter-django-tailwind** — Django 5.x production template security/settings

## Resources
| Resource | URL | Description |
|----------|-----|-------------|
| DRF docs | https://www.django-rest-framework.org | API docs |
