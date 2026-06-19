# RESEARCH_REPORT.md

## Project: profile

**Type:** Blog / profile CMS
**Tech Stack:** Django 4.x, Python 3.11+, PostgreSQL, CKEditor 5, Google Cloud Storage, Docker, django-allauth
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| cookiecutter-django-tailwind | `projects/cookiecutter-django-tailwind` | Django security, settings, and template guidance apply directly |
| xamehi.tv | `projects/xamehi.tv` | Shared Django media, auth, and CMS-like admin concerns |
| ecom | `projects/ecom` | DRF + React admin/media patterns |
| rhixecompany-comics | `projects/rhixecompany-comics` | Dual-stack Django + Next.js; media/CDN patterns |

---

## Key Findings

### Django 4.x Blog/CMS Best Practices (2026) — Wagtail Alternatives

- **Django is a framework, not a CMS** — purpose-built CMS platforms (Wagtail, WordPress, Sanity) provide editorial features Django lacks natively [1]
- **Wagtail vs django-CMS**: Wagtail is developer-first, streamfield-based, more flexible for custom content models; django-CMS is editor-friendly with plugin architecture [2]
- **For blog-only projects**: Consider Wagtail (built on Django, streamfield, image management, versioning) over custom Django — faster time-to-production [2]
- **Enterprise migration trend**: Organizations moving from custom Django to Wagtail/Sanity for editorial autonomy + IT security standards [1]
- **Custom Django CMS still valid** when: unique data models, tight app integration, team has Django expertise, no editorial workflow needs

### Google Cloud Storage + Django (2026)

- **django-storages GCS backend** implements Django File API; use `STORAGES` dict (Django 4.2+) with `staticfiles` + `default` keys for static/media separation [3]
- **Signed URLs via IAM SignBlob API** — default service accounts insufficient; create dedicated service account with `roles/storage.objectCreator` + `roles/storage.objectViewer` [3]
- **Lifecycle policies critical** — configure object lifecycle (age, version count) to prevent media accumulation; `gsutil lifecycle set` [4]
- **Environment separation** — distinct buckets per env (dev/staging/prod); never share `MEDIA_ROOT` across environments [4]
- **Signed URL expiration** — use short TTLs (1hr) for private media; signed URLs bypass Django process for large downloads [3]

### CKEditor 5 + Django Integration (2026)

- **`django-ckeditor-5`** package provides CKEditor 5 with image upload support; configure `CKEDITOR_5_CONFIGS` for toolbar, `CKEDITOR_5_UPLOAD_PATH` for media organization [5]
- **Staff-only uploads by default** — override `ckeditor5/image_upload/` view to remove `is_staff` check for public content editors [6]
- **Custom upload view pattern**: copy ckeditor5 views to `views.py`, remove permission check, override URL in `urls.py` [6]
- **Sanitize on render, not just input** — never trust editor-side sanitization; use `bleach` or `lxml.html.clean` when rendering public content [6]
- **File size/type validation** — enforce server-side before save; prevent DoS via large uploads

### Django on GCP Cloud Run (2026)

- **Cloud Run + Cloud SQL (PostgreSQL)** is recommended serverless stack; connect via Unix socket (`/cloudsql/INSTANCE_CONNECTION_NAME`) [7]
- **Connection pooling mandatory** — Cloud Run scales instances → overwhelms Cloud SQL; use PgBouncer (Aiven) or `django-db-connection-pool` [7]
- **Dockerfile multi-stage** — builder for deps, runtime with `gunicorn` + `whitenoise`; `CMD gunicorn project.wsgi:application --bind 0.0.0.0:$PORT` [8]
- **Cloud Build CI/CD** — `cloudbuild.yaml` for automated deploy on push; secret manager for `SECRET_KEY`, `DATABASE_URL` [7]
- **Static files via `collectstatic` + WhiteNoise** — `STATIC_ROOT` in container; media on GCS (not Cloud Run filesystem) [8]

### Django CBV Patterns (2026)

- **CBVs preferred over FBVs** for CRUD: `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView` reduce boilerplate [9]
- **Mixins for cross-cutting concerns** — `LoginRequiredMixin`, `PermissionRequiredMixin`, `SuccessMessageMixin` compose cleanly [9]
- **Custom base classes** — `BaseModelViewSet` with shared pagination, filtering, serialization for DRF-style consistency [9]
- **Template naming convention** — `<app>/<model>_<viewtype>.html` (e.g., `blog/post_list.html`) enables auto-discovery [9]
- **Override `get_queryset()` not `get()`** — preserves mixin behavior; filter by request/user in queryset [9]

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Wagtail vs django-CMS | https://blog.logrocket.com/comparing-wagtail-vs-django-cms | Comparison |
| Django CMS alternatives | https://www.multidots.com/blog/django-alternatives | Guide |
| Django static/media 2026 | https://oneuptime.com/blog/post/2026-02-02-django-static-media-files/view | Guide |
| django-storages GCS | https://django-storages.readthedocs.io/en/latest/backends/gcloud.html | Docs |
| django-ckeditor-5 | https://djangopackages.org/packages/p/django-ckeditor-5 | Package |
| CKEditor 5 image upload | https://github.com/hvlads/django-ckeditor-5/issues/64 | Issue/Guide |
| Django on Cloud Run | https://oneuptime.com/blog/post/2026-02-17-how-to-build-a-django-application-with-cloud-sql-and-deploy-to-cloud-run-with-cloud-build/view | Guide |
| Deploy Django Cloud Run | https://www.coreyguitar.com/blog/8 | Tutorial |
| Django CBV docs | https://docs.djangoproject.com/en/6.0/topics/class-based-views | Docs |
| CBV implementation | https://oneuptime.com/blog/post/2026-02-02-django-class-based-views/view | Guide |

---

## Best Practices

1. **GCS lifecycle policies** — auto-delete old versions, move to cold storage after 30 days
2. **CKEditor sanitization on render** — `bleach.clean(html, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRS)`
3. **Allauth redirect safety** — `ACCOUNT_LOGIN_REDIRECT_URL` + `LOGIN_REDIRECT_URL` whitelist
4. **Static fallback for offline dev** — local `MEDIA_ROOT` when `DEBUG=True`
5. **Model field provenance** — `upload_to` callables with UUID + date prefixes to avoid collisions
6. **Dedicated GCS service account** — least privilege (`storage.objectCreator/Viewer`); no default compute SA
7. **PgBouncer for Cloud Run** — prevents connection exhaustion during scale events
8. **WhiteNoise for static only** — media on GCS signed URLs; never serve media through Gunicorn
9. **CBV mixin composition** — single-responsibility mixins over deep inheritance hierarchies
10. **Email verification in allauth** — `ACCOUNT_EMAIL_VERIFICATION = "mandatory"` for public profiles

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Trusting CKEditor HTML | XSS on public pages | Sanitize with `bleach` on every render |
| Missing GCS permissions | Upload 403/500 errors | Grant dedicated SA `roles/storage.objectCreator` |
| Media path shared across envs | Dev uploads visible in prod | Separate bucket per environment |
| Password reset emails fail | User lockouts | Configure `EMAIL_BACKEND` + test with Mailpit in dev |
| No connection pooling on Cloud Run | DB saturation on scale | PgBouncer sidecar or Aiven PgBouncer |
| `collectstatic` missing in Docker | 404 on static assets | Run in Dockerfile build stage |
| Allauth social providers in prod | Unused attack surface | Disable unused providers in `settings/production.py` |
| Hardcoded `SECRET_KEY` | Security breach | Load from env; rotate via secret manager |
| CKEditor uploads to root `media/` | Disorganized, collision risk | Set `CKEDITOR_5_UPLOAD_PATH = "uploads/ckeditor5/"` |

---

## Performance

1. **Cache public profile pages** — `cache_page(60*15)` on detail views; invalidate on `post_save` signal
2. **GCS signed URLs with expiration** — large images bypass Django; 1hr TTL for private media
3. **Avoid N+1 in profile listings** — `prefetch_related('tags', 'categories', 'author__profile')`
4. **WhiteNoise compression** — `WHITENOISE_USE_FINDERS = True` + gzip/brotli for static
5. **Database indexing** — composite indexes on `(author, -created_at)` for profile feeds
6. **Lazy-load CKEditor** — only load editor JS on admin/edit pages via `Media` class

---

## Security

1. **Validate CKEditor image URLs + file sizes** before storing — reject >5MB, non-image MIME
2. **HTTPS everywhere + secure cookies** — `SESSION_COOKIE_SECURE = True`, `CSRF_COOKIE_SECURE = True`
3. **Limit admin access** — `ADMIN_ALLOWED_IPS` middleware; disable unused allauth providers
4. **Rotate `SECRET_KEY`** — environment variable; secret manager rotation every 90 days
5. **Content Security Policy** — `django-csp` with `script-src 'self'` for CKEditor inline scripts
6. **File upload validation** — magic bytes check, extension allowlist, dimension limits
7. **Allauth rate limiting** — `django-axes` for brute-force protection on login

---

## Related Projects (in workspace)

- **cookiecutter-django-tailwind** — shared Django security, settings, and template guidance
- **xamehi.tv** — shared Django CMS/admin and media handling concerns
- **ecom** — DRF + React admin/media patterns
- **rhixecompany-comics** — dual-stack Django + Next.js; media/CDN patterns

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Django docs | https://docs.djangoproject.com/en/stable/ | Official docs |
| CKEditor 5 docs | https://ckeditor.com/docs/ckeditor5/latest/ | Editor docs |
| django-allauth docs | https://docs.allauth.org | Auth setup |
| Google Cloud Storage docs | https://cloud.google.com/storage/docs | Storage docs |
| Django security checklist | https://docs.djangoproject.com/en/stable/topics/security/ | Security baseline |
| django-storages GCS | https://django-storages.readthedocs.io/en/latest/backends/gcloud.html | GCS backend |
| Cloud Run Django | https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python | GCP deployment |

---

*Last updated: 2026-06-17 | All findings backed by web_search + web_extract citations*