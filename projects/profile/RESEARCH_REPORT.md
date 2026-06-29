# RESEARCH_REPORT.md

## Project: profile

**Type:** Django blog/profile CMS for RhixeCompany
**Tech Stack:** Django 3.x, CKEditor 4, SQLite (dev) / PostgreSQL (prod), Google Cloud Storage (django-storages), django-crispy-forms (Bootstrap 4), django-filter, Gunicorn, Docker
**Status:** Active

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|-------------|
| Django Blog (MDN) | https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django | Reference Django blog tutorial |
| Wagtail CMS | https://wagtail.org | Production Django CMS alternative |

## Key Findings

### Django Blog CMS Patterns (2026)
- Function-based views (FBVs) are still used in the codebase; class-based views (CBVs) reduce boilerplate for CRUD operations significantly (docs.djangoproject.com)
- CKEditor 4 is maintenance-only as of 2024; CKEditor 5 offers real-time collaboration and better security
- django-crispy-forms with Bootstrap 4 remains a standard pattern for form rendering

### Google Cloud Storage Integration
- django-storages[google] is the industry standard for serving media from GCS (django-storages.readthedocs.io)
- Development uses local filesystem; GCS settings currently commented out in settings.py
- Bucket permissions and CORS configuration are essential for production media serving

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Django CBVs | https://docs.djangoproject.com/en/4.2/topics/class-based-views/ | Official Docs |
| GCS + Django | https://django-storages.readthedocs.io/en/latest/backends/gcloud.html | Integration Guide |

## Best Practices

1. **Extract SECRET_KEY** to environment variable — currently hardcoded in settings.py
2. **Migrate from FBVs to CBVs** — Reduces code duplication for CRUD views (post_list/create/update/delete)
3. **Add SEO infrastructure** — django-meta or custom meta tags + sitemap for search indexing
4. **Upgrade CKEditor 4 → 5** — CKEditor 4 is end-of-life; 5 provides security patches and modern editing
5. **Enable GCS for all environments** — Prevents local-vs-production media path drift

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Hardcoded SECRET_KEY | Full site compromise if committed | Use django-environ with .env file |
| CKEditor 4 EOL | No security patches | Plan migration to CKEditor 5 |
| FBV code duplication | Higher maintenance cost | Refactor common patterns into CBVs |
| GCS settings commented out | Media won't serve in production | Uncomment and configure bucket |

## Performance

1. **Django select_related/prefetch_related** reduces N+1 query count for blog post listings
2. **GCS media offload** reduces server bandwidth vs serving files directly
3. **Django template caching** (`{% cache %}`) for blog post content
4. **Gunicorn worker tuning** — 2-4 workers per CPU core for optimal throughput
5. **Database indexing** on created_at and slug fields for fast queries

## Security

1. **Move SECRET_KEY to .env** — currently hardcoded in settings.py (critical risk)
2. **Enable HTTPS redirect** in production settings
3. **Configure CORS** if REST API is consumed by client-side apps
4. **Update DEBUG=False** in production — currently defaults to True
5. **GCS bucket permissions** — use signed URLs for private content, public-read for public media

## Related Projects (in workspace)

- **xamehi.tv** — Django 4 + DRF + Gunicorn, shares Django deployment patterns
- **rhixecompany-comics** — Django + Next.js, shares Django backend architecture
- **ecom** — Django DRF + React + PayPal, shares Django production configuration

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Django Docs | https://docs.djangoproject.com | Official Django documentation |
| django-storages GCS | https://django-storages.readthedocs.io/en/latest/backends/gcloud.html | Google Cloud Storage integration |
| CKEditor 5 Migration | https://ckeditor.com/docs/ckeditor5/latest/installation/upgrading-from-ckeditor-4.html | Migration guide |
| Gunicorn Settings | https://docs.gunicorn.org/en/stable/settings.html | WSGI server configuration |
