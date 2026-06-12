# RESEARCH_REPORT.md

## Project: profile

**Type:** Blog / profile CMS
**Tech Stack:** Django 4.x, Python 3.11+, PostgreSQL, CKEditor 5, Google Cloud Storage, Docker, django-allauth
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| cookiecutter-django-tailwind | `projects/cookiecutter-django-tailwind` | Django settings and security guidance apply directly. |
| xamehi.tv | `projects/xamehi.tv` | Shared Django media, auth, and CMS-like admin concerns. |

---

## Key Findings

### CKEditor + Media Storage
- CKEditor 5 configs should be explicit about allowed upload endpoints; prevent open redirects by validating URLs before mark-save.
- Keep media uploads CDN-backed when possible; GCS signed URLs reduce Django process exposure.

### Auth + Profiles
- `django-allauth` handles social login and email verification well; keep email templates in dedicated templates dir for easier CSS updates.
- Profile public visibility should be controlled in the view layer, not by accidentally omitting serializer fields.

### Tailwind Integration
- The README/AGENTS do not yet declare Tailwind directly for this repo, but the workspace frequently uses it; if added, prefer `django-tailwind` over Node-only pipelines for consistency.

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Django docs | https://docs.djangoproject.com/en/stable/ | Docs |
| CKEditor 5 | https://ckeditor.com/docs/ckeditor5/latest/ | Docs |
| django-allauth | https://docs.allauth.org | Docs |
| Google Cloud Storage | https://cloud.google.com/storage/docs | Docs |
| Django security checklist | https://docs.djangoproject.com/en/stable/topics/security/ | Docs |

---

## Best Practices
1. **GCS lifecycle** — configure object lifecycle so media does not accumulate indefinitely.
2. **CKEditor sanitization on render** — never trust editor-side sanitization alone for public pages.
3. **Allauth redirect safety** — whitelist allowed post-login redirect hosts.
4. **Static fallback** — keep local media fallback working for offline development.
5. **Model field provenance** — use `upload_to` callables to organize media and avoid collisions.

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Trusting CKEditor HTML | XSS risk | Sanitize HTML on render and when imported. |
| Missing GCS permissions | Upload failures | Grant least-privilege service account roles. |
| Media path across envs | Data leakage | Separate bucket per environment. |
| Password reset emails misconfigured | Lockouts | Keep SMTP/Mailpit config ready in dev. |

---

## Performance
1. Cache public profile pages; invalidate cache when profile content changes.
2. Use GCS signed URLs with expirations so large images do not stream through Django.
3. Avoid N+1 queries in profile post listing by prefetching related tags or categories.

---

## Security
1. Validate CKEditor image URLs and file sizes before storing.
2. Use HTTPS everywhere and secure cookies in production.
3. Limit admin and staff access to needed sections; disable unused allauth providers in production.
4. Rotate `SECRET_KEY` via environment; never keep hardcoded Django secrets.

---

## Related Projects (in workspace)

- **cookiecutter-django-tailwind** — shared Django security, settings, and template guidance
- **xamehi.tv** — shared Django CMS/admin and media handling concerns

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Django docs | https://docs.djangoproject.com/en/stable/ | Official docs |
| CKEditor Docs | https://ckeditor.com/docs | Editor docs |
| django-allauth docs | https://docs.allauth.org | Auth setup |
| Google Cloud Storage docs | https://cloud.google.com/storage/docs | Storage docs |
| Django security checklist | https://docs.djangoproject.com/en/stable/topics/security/ | Security baseline |
