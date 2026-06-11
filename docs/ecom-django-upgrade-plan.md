# ecom — Django 3.1 → 5.x Upgrade Plan

Generated: 2026-05-30
Priority: HIGH (Django 3.1 is EOL with known CVEs)

## Current Stack
- Django 3.1.14 (EOL — December 2021)
- DRF 3.11.2, SimpleJWT 4.7.2
- django-cors-headers 3.11.0, django-filter 21.1
- django-crispy-forms 1.14.0, django-ckeditor 6.3.2
- Python 3.10, PostgreSQL
- React 18 frontend (separate)

## Upgrade Path

### Stage 1: Django 3.1 → 4.2 LTS (estimated: 4-6 hours)

**Breaking changes:**
1. `url()` from `django.conf.urls` is deprecated → use `re_path()` or `path()` (current codebase already uses `path()` — low risk)
2. `MIDDLEWARE_CLASSES` → `MIDDLEWARE` (already using `MIDDLEWARE` — no change)
3. `ugettext()` / `ugettext_lazy()` removed → use `gettext()` / `gettext_lazy()`
4. `force_text()` → `force_str()`
5. `is_safe_url()` → `url_has_allowed_host_and_scheme()`
6. `DEFAULT_FILE_STORAGE` → `STORAGES` setting
7. `STATICFILES_STORAGE` → `STORAGES` setting
8. PostgreSQL `django.db.backends.postgresql_psycopg2` → `django.db.backends.postgresql`

**Dependency bumps:**
- djangorestframework: 3.11.2 → 3.15.x
- djangorestframework-simplejwt: 4.7.2 → 5.x
- django-cors-headers: 3.11.0 → 4.x
- django-filter: 21.1 → 24.x
- django-crispy-forms: 1.14.0 → 2.x
- django-ckeditor: 6.3.2 → check compatibility

### Stage 2: Django 4.2 → 5.x (estimated: 2-4 hours)

**Breaking changes:**
1. `django.db.models.NullBooleanField` → `BooleanField(null=True)`
2. `django.db.models.index_together` → `Meta.indexes`
3. Serializer `many=True` behavior change
4. Default `app_label` from `AppConfig.name` → `AppConfig.label`
5. `django.contrib.sessions` serialization changes

**Dependency bumps:**
- Verify all packages support Django 5.x
- DRF 3.15.x supports Django 5.x
- SimpleJWT 5.x supports Django 5.x

## Migration Procedure

1. **Create new branch:** `git checkout -b upgrade/django-5`
2. **Update requirements.txt** with new version pins
3. **Run `python manage.py check --deploy`** — identifies deprecated settings
4. **Fix each deprecation warning** iteratively
5. **Run `python manage.py test`** — ensure existing functionality
6. **Deploy stage 1 (4.2 LTS)** — validate in staging
7. **Proceed to stage 2 (5.x)** — repeat check/fix/test cycle
8. **Add missing ignore files:** .dockerignore, .prettierignore, .eslintignore

## Key Test Points
- JWT authentication flow (login, token refresh)
- PayPal integration (sandbox mode)
- Product CRUD operations
- Order lifecycle (create, pay, deliver)
- Admin panel functionality
- Image uploads
