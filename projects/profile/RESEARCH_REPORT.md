# RESEARCH_REPORT.md

## Project: profile
**Type:** Blog / profile CMS
**Tech Stack:** Django 4.x, Python 3.11+, PostgreSQL, CKEditor 5, Google Cloud Storage, Docker, django-allauth
**Status:** Active

## Similar Projects
| Project | URL | Why Relevant |
|---------|-----|--------------|
| cookiecutter-django-tailwind | `projects/cookiecutter-django-tailwind` | Django security, settings, and template guidance apply directly |
| xamehi.tv | `projects/xamehi.tv` | Shared Django media, auth, and CMS-like admin concerns |
| ecom | `projects/ecom` | DRF + React admin/media patterns |
| rhixecompany-comics | `projects/rhixecompany-comics` | Dual-stack Django + Next.js; media/CDN patterns |

## Key Findings
### Django 4.x Blog/CMS Best Practices (2026) — Wagtail Alternatives
- **Django is a framework, not a CMS** — purpose-built CMS platforms (Wagtail, WordPress, Sanity) provide editorial features Django lacks natively [1]
- **Wagtail vs django-CMS**: Wagtail is developer-first, streamfield-based, more flexible for custom content models; django-CMS is editor-friendly with plugin architecture [2]
- **For blog-only projects**: Consider Wagtail (built on Django, streamfield, image management, versioning) over custom Django — faster time-to-production [2]
- **Enterprise migration trend**: Organizations moving from custom Django to Wagtail/Sanity for editorial autonomy + IT security standards [1]
- **Custom Django CMS still valid** when: unique data models, tight app integration, team has Django expertise, no editorial workflow needs
### Google Cloud Storage + Django (2026)
- **django-storages GCS backend** implements Django File API; use `STORAGES` dict (Django 4.2+) with `staticfiles` + `default` keys for static/media separation [3]

## Cheatsheets & Quick Reference
| Topic | Resource | Type |
|-------|----------|------|
| Wagtail vs django-CMS | https://blog.logrocket.com/comparing-wagtail-vs-django-cms | Comparison |

## Best Practices
1. **GCS lifecycle policies** — auto-delete old versions, move to cold storage after 30 days
2. **CKEditor sanitization on render** — `bleach.clean(html, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRS)`
3. **Allauth redirect safety** — `ACCOUNT_LOGIN_REDIRECT_URL` + `LOGIN_REDIRECT_URL` whitelist

## Common Pitfalls
| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Trusting CKEditor HTML | XSS on public pages | Sanitize with `bleach` on every render |

## Performance
1. **Cache public profile pages** — `cache_page(60*15)` on detail views; invalidate on `post_save` signal
2. **GCS signed URLs with expiration** — large images bypass Django; 1hr TTL for private media

## Security
1. **Validate CKEditor image URLs + file sizes** before storing — reject >5MB, non-image MIME
2. **HTTPS everywhere + secure cookies** — `SESSION_COOKIE_SECURE = True`, `CSRF_COOKIE_SECURE = True`

## Related Projects (in workspace)
- **cookiecutter-django-tailwind** — shared Django security, settings, and template guidance
- **xamehi.tv** — shared Django CMS/admin and media handling concerns
- **ecom** — DRF + React admin/media patterns
- **rhixecompany-comics** — dual-stack Django + Next.js; media/CDN patterns

## Resources
| Resource | URL | Description |
|----------|-----|-------------|
| Django docs | https://docs.djangoproject.com/en/stable/ | Official docs |
