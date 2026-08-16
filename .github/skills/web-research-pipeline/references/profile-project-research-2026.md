# Profile Project Research (2026-07-10)

Research conducted for the **profile** project (Django 4.x blog/CMS with GCS, CKEditor 5, Docker, GCP) using queries from `docs/per-project-research-queries.md` section 6.

## Queries Executed

1. **Django 4.x + Google Cloud Storage media handling 2026**
2. **CKEditor 5 integration with Django admin patterns**
3. **Django CMS blog patterns with cloud media storage**
4. **Docker + GCP deployment for Django applications**
5. **Django collectstatic to GCS bucket configuration**
6. **Wagtail vs custom Django CMS for blog platforms 2026**

## Key Sources

| Source | URL | Relevance |
|--------|-----|-----------|
| django-storages GCS docs | https://django-storages.readthedocs.io/en/latest/backends/gcloud.html | Official backend config, STORAGES dict, signed URLs, IAM Sign Blob |
| Viget GCS article | https://www.viget.com/articles/using-google-cloud-storage-in-your-django-project | Multi-bucket pattern via custom storage classes |
| Corey Guitar tutorial | https://www.coreyguitar.com/blog/8 | End-to-end Docker + Cloud Run + Cloud SQL + Secret Manager + GCS |
| Google Cloud Run Django | https://docs.cloud.google.com/python/django/run | Official GCP tutorial with Cloud Build, migrations, collectstatic |
| django-ckeditor-5 (PyPI) | https://pypi.org/project/django-ckeditor-5 | CKEditor5Field, widget, configs, custom storage, upload perms |
| django-cms CKEditor 5 release | https://www.django-cms.org/en/blog/2026/04/27/full-ckeditor-5-support-lands-in-djangocms-text | Full parity April 2026, text-enabled plugins |
| Wagtail vs Django CMS | https://blog.logrocket.com/comparing-wagtail-vs-django-cms | 2024 comparison, still relevant 2026 |

## Critical Findings for Profile Project

### STORAGES Dict (Django 4.2+)
```python
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        "OPTIONS": {
            "bucket_name": "my-media-bucket",
            "default_acl": "publicRead",  # or None for private + signed URLs
            "querystring_auth": False,     # True for private
            "iam_sign_blob": True,         # Required on Cloud Run
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        "OPTIONS": {
            "bucket_name": "my-static-bucket",
            "gzip": True,
            "gzip_content_types": ("text/css", "application/javascript", "image/svg+xml"),
        },
    },
}
```

### CKEditor 5 + Django Admin
- Package: `django-ckeditor-5` (hvlads, v0.2.20)
- `CKEditor5Field(config_name='extends')` for models
- `CKEDITOR_5_CONFIGS` dict for toolbar, image styles, tables
- `CKEDITOR_5_FILE_STORAGE` for custom GCS storage
- `CKEDITOR_5_FILE_UPLOAD_PERMISSION = "staff"`
- **Server-side sanitization required**: `bleach` or `nh3` — CKEditor 5 only does client-side

### Deployment Stack (2026)
- **Cloud Run** (not App Engine Flex)
- **Cloud Build** with `cloudmigrate.yaml` (build → migrate → collectstatic)
- **Cloud SQL PostgreSQL** + Cloud SQL Auth Proxy (local) / built-in (Cloud Run)
- **Secret Manager** for all secrets
- **Multi-stage Dockerfile** with Gunicorn + Uvicorn workers
- Service account: Cloud SQL Client, Secret Manager Accessor, Storage Object Creator/Viewer

### Wagtail vs Custom Decision
| Choose | When |
|--------|------|
| **Wagtail** | Content editors need StreamField, workflows, multi-site, search, image management |
| **django-cms** | Plugin ecosystem, marketing integrations, versioning, multilingual built-in |
| **Custom Django + CKEditor 5** | Simple blog, team knows Django, full control, minimal deps |

**2026 Verdict**: Wagtail 6.x most active; django-cms 4.x stable with CKEditor 5 parity; custom viable for simple needs.

## Manual vs Automated Pipeline Note

The `scripts/pipeline-execute.py` uses a hardcoded query and single-topic output directory. For per-project research with **multiple distinct queries** (like this profile project's 6 queries), manual `web_search` + `web_extract` + targeted `write_file` to the project's `RESEARCH_REPORT.md` was more effective. The automated script is better suited for single-topic deep dives.

---

## Update: 2026-07-24 — Tavily Deep Searches

**New queries executed** (4 Tavily deep searches, `search_depth=advanced`, `time_range=year`):

1. **Django 5.2 LTS / 6.0 migration best practices 2026**
2. **CKEditor 5 Django integration 2026**
3. **Google Cloud Storage Django media files 2026**
4. **Django PostgreSQL production optimization 2026**

### Key Sources (2025-2026)

| Source | URL | Relevance |
|--------|-----|-----------|
| Django 5.2 migration guide | https://medium.com/@anas-issath/migrating-to-django-5-2-what-changed-in-production-deployment-ac55e7717ebc | Three-production-app migration, PostgreSQL 14+ requirement |
| Django upgrade strategy | https://acquaintsoft.com/blog/django-version-upgrade-strategy | LTS-to-LTS methodology, django-upgrade/codemod automation |
| Django 6 + CKEditor 5 guide | https://www.desarrollolibre.net/blog/django/incorporate-ckeditor-5-into-django-3-ways | Django 6 integration, `django-ckeditor-5` package, image uploads |
| OneUptime Django GCS guide | https://oneuptime.com/blog/post/2026-02-02-django-static-media-files/view | STORAGES dict for GCS, separate buckets, IAM Sign Blob |
| Google Cloud Run Django codelab | https://codelabs.developers.google.com/codelabs/cloud-run-django | Official GCP tutorial with STORAGES config |
| PostgreSQL 2026 tutorial | https://tech-insider.org/postgresql-tutorial-complete-database-guide-2026 | PostgreSQL 17 features, extensions, memory tuning |
| DB tuning guide 2026 | https://www.softomatesolutions.com/blog/database-performance-tuning-guide | shared_buffers, work_mem, PgBouncer, random_page_cost |

### Critical New Findings

#### Django Version Posture (July 2026)
- **Django 4.2 LTS EOL: April 7, 2026** — no security patches since. Urgent upgrade to **5.2 LTS** (supported through April 2028).
- **Django 6.0 (Dec 2025)** — non-LTS; upgrade path: 5.2 → 6.0 → 6.2 LTS (expected Apr 2027).
- **Breaking in 5.2:** requires PostgreSQL 14+, removes deprecated APIs, adds async views, built-in CSP (`SECURE_CSP`).
- **Migration playbook:** `django-upgrade` + `django-codemod` → audit deprecation warnings → dual-version compat → staged deploy → PgBouncer + `CONN_MAX_AGE=600`.

#### CKEditor 5 Security (New)
- **`django-ckeditor-5`** (hvlads) is the active package — verified compatible with Django 5.x/6.x.
- **Server-side sanitization is MANDATORY** — CKEditor 5 only sanitizes client-side. Use **`nh3`** (Rust, ~10× faster than `bleach`) before saving/rendering HTML.
- Image uploads work with proper `MEDIA_URL/MEDIA_ROOT` config; serve via GCS in production.

#### GCS Hardening (2026)
- Modern config uses `STORAGES` dict for both `default` (media) and `staticfiles` — separate buckets per environment.
- **Production must-haves:**
  - `GS_IAM_SIGN_BLOB=True` for signed private URLs
  - `GS_DEFAULT_ACL='private'` (not `publicRead`)
  - Cloud CDN fronting via `GS_CUSTOM_ENDPOINT`
  - `GS_BLOB_CHUNK_SIZE` for large uploads
- Required env vars: `GS_BUCKET_NAME`, `GS_PROJECT_ID`, `GOOGLE_APPLICATION_CREDENTIALS` (service account JSON).

#### PostgreSQL 17 / Production Tuning (2026)
- **PostgreSQL 17 (2025):** parallel BRIN builds, SIMD-accelerated B-tree (AVX-512), improved partitioning.
- **Critical extensions:** `pg_stat_statements` (query perf), `pgcrypto`/`uuid-ossp` (UUIDs), `pg_trgm` (fuzzy search), `btree_gist` (exclusion constraints), `pg_repack` (online vacuum), `timescaledb` (time-series).
- **Memory tuning:** `shared_buffers=25% RAM`, `effective_cache_size=75% RAM`, `work_mem=64MB`, `maintenance_work_mem=512MB`, `max_worker_processes=8`.
- **Connection pooling:** **PgBouncer (transaction mode)** + Django `CONN_MAX_AGE=600` — essential above ~30 concurrent workers.
- **SSD tuning:** `random_page_cost=1.1`, `effective_io_concurrency=200`.
- **Django-level:** `select_related`/`prefetch_related` for N+1 elimination, partial/composite indexes, `EXPLAIN ANALYZE` on slow queries.

### Updated RESEARCH_REPORT.md
The project's `RESEARCH_REPORT.md` has been fully rewritten (2026-07-24) incorporating all new findings, cross-referenced with 6 workspace Django projects (cookiecutter-django-tailwind, ecom, Django-Scrapy-Selenium, rhixecompany-comics, xamehi, xamehi.tv). Report size: ~8KB, structured with Quick Reference, Best Practices, Common Pitfalls, Performance Targets, Security Checklist, and Related Projects sections.