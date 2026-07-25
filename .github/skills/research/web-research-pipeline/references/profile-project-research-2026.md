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