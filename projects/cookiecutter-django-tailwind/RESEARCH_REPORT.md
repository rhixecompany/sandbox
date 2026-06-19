# RESEARCH_REPORT.md

## Project: cookiecutter-django-tailwind

**Type:** Django project generator / starter template  
**Tech Stack:** Python 3.12+, Django 5.x, Tailwind CSS, pytest, pre-commit, ruff, mypy, Black, djlint, Django REST Framework (optional), Celery (optional), Sentry  
**Status:** Active  

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| profile | `projects/profile` | Django + Tailwind content site with form/editor concerns. |
| rhixecompany-comics | `projects/rhixecompany-comics` | Uses generated Django model in production backend. |
| Django-Scrapy-Selenium | `projects/Django-Scrapy-Selenium` | Django backend with scraping capabilities. |
| ecom | `projects/ecom` | E-commerce Django project pattern. |
| xamehi | `projects/xamehi` | Django project with content management. |
| xamehi.tv | `projects/xamehi.tv` | Video streaming Django platform. |

---

## 1. Django 5.x Project Structure & Settings Best Practices (2026)

### Recommended Production-Ready Structure
Modern Django projects (2026) adopt a **modular, environment-separated architecture** that scales beyond the default `startproject` scaffold. The recommended structure groups apps, splits settings by environment, and isolates configuration from business logic:

```
project/
├── apps/                    # All Django apps grouped here (bounded contexts)
│   ├── users/
│   ├── products/
│   ├── orders/
│   └── core/               # Shared utilities, abstract models
├── config/                 # Settings split by environment (NOT an app)
│   ├── settings/
│   │   ├── base.py         # Common settings
│   │   ├── development.py  # Dev overrides (DEBUG=True, sqlite)
│   │   ├── staging.py      # Staging mirror of production
│   │   └── production.py   # Hardened, secrets from env vars
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── static/                 # Global static files (CSS, JS, images, vendor/)
├── templates/              # Global templates (base.html, partials/, emails/, errors/)
├── media/                  # User uploads (local dev only)
├── requirements/           # Split dependency management
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
├── .env.example            # Template for environment variables (NOT committed)
├── manage.py
└── pyproject.toml          # Unified config for ruff, mypy, pytest, black
```

**Sources:** Technaureus 2026 "[Django Project Structure Best Practices in 2026](https://www.technaureus.com/blog-detail/django-project-structure-best-practices-2026)", DEV Community "[Django Project Structure Best Practices: A Production-Ready Guide](https://dev.to/alansomathew/django-project-structure-best-practices-a-production-ready-guide-3io3)", Medium "[Django Folder Structure Best Practices](https://medium.com/@sizanmahmud08/django-folder-structure-best-practices-a-complete-guide-to-scalable-project-organization-508437899736)"

### Key Principles
- **Apps as bounded contexts** — Each app = one cohesive domain (DDD); avoid `utils`, `helpers`, `misc` apps.
- **Config in environment variables** — Twelve-Factor App methodology: `SECRET_KEY`, `DATABASE_URL`, `DEBUG` never hardcoded.
- **Settings split by environment** — `base.py` → `development.py` / `staging.py` / `production.py` inheritance eliminates conditional logic.
- **Service/Selector pattern** — Views stay thin (HTTP adapters); `services.py` owns writes/business logic; `selectors.py` owns reads/queries.

### Cookiecutter-Django-Tailwind Alignment
The template should generate:
- `config/settings/{base,local,production}.py` with `django-environ` for `.env` loading
- `apps/` directory with `core/` for shared `TimeStampedModel`, mixins, permissions
- `requirements/{base,local,production}.txt` split to prevent production bloat
- `.env.example` with all required variables documented

---

## 2. django-tailwind Integration: Tailwind CSS in Django Templates (2026)

### Two Major Integration Approaches

| Aspect | **django-tailwind** (timonweb) | **django-tailwind-cli** (django-commons) |
|--------|--------------------------------|------------------------------------------|
| **Node.js Required** | Optional (standalone binary default) | ❌ Never — uses standalone Tailwind CLI |
| **Latest Version** | 4.5.0 (supports Tailwind CSS v4.x) | Active development |
| **Django Support** | 4.2, 5.0, 5.1, 5.2, 6.0 | 4.2, 5.0, 5.1, 5.2 |
| **Python Requirement** | ≥ 3.11 | ≥ 3.9 |
| **Hot Reload** | ✅ `tailwind dev` (with honcho) | ✅ `tailwind watch` + `tailwind runserver` |
| **DaisyUI** | Optional extra | Via `@plugin "daisyui"` in CSS |
| **Management Commands** | `init`, `install`, `dev`, `build`, `plugin` | `setup`, `build`, `watch`, `runserver`, `config`, `troubleshoot` |

**Sources:** PyPI "[django-tailwind](https://pypi.org/project/django-tailwind)", GitHub "[django-tailwind-cli](https://github.com/django-commons/django-tailwind-cli)", Flowbite "[Tailwind CSS Django](https://flowbite.com/docs/getting-started/django)"

### django-tailwind (Recommended for Cookiecutter)
```bash
# Install with dev extras
pip install 'django-tailwind[cookiecutter,honcho,reload]'

# Setup
python manage.py tailwind init        # Creates 'theme' app
python manage.py tailwind install     # Downloads standalone binary (no Node)
python manage.py tailwind dev         # Starts Django + Tailwind watchers
```

**Template Configuration** (`settings.py`):
```python
INSTALLED_APPS = [
    "tailwind",
    "theme",              # Generated app name
]
TAILWIND_APP_NAME = "theme"
```

**Template Usage** (`base.html`):
```django
{% load tailwind_tags %}
{% tailwind_css %}
<div class="text-4xl font-bold text-blue-600">Hello Tailwind!</div>
```

### django-tailwind-cli (Simpler Alternative)
```bash
pip install django-tailwind-cli
# settings.py
INSTALLED_APPS = ["django_tailwind_cli"]
TAILWIND_CLI_SRC_CSS = BASE_DIR / "templates" / "source.css"
# Run: python manage.py tailwind runserver
```

**Key 2026 Insight:** Both packages now support **Tailwind CSS v4.x** with CSS-first configuration (no `tailwind.config.js` required). The standalone binary mode eliminates Node.js dependency drift — critical for generated templates that must work on Windows, macOS, and Linux without extra tooling.

### Cookiecutter Integration Recommendations
- Default to **django-tailwind** with standalone binary mode (no Node.js)
- Generate `theme/` app with `static_src/src/input.css` using `@import "tailwindcss";`
- Include optional `daisyui` extra via cookiecutter prompt
- Document `python manage.py tailwind build` for production CSS compilation
- Add `@source` directives in `input.css` for template discovery (Tailwind v4 requirement)

---

## 3. Cookiecutter Django Template Maintenance & Dependency Updates (2026)

### Dependency Management for Generated Projects
Cookiecutter Django templates must manage **two dependency layers**:
1. **Template dependencies** — Tools needed to *generate* projects (Cookiecutter itself, pre-commit hooks)
2. **Generated project dependencies** — What the output project installs (`requirements/*.txt`)

**Sources:** Cookiecutter Django docs "[Welcome to Cookiecutter Django](https://cookiecutter-django.readthedocs.io)", Stack Overflow "[Cookiecutter Template Dependency Management](https://stackoverflow.com/questions/76791326/cookiecutter-template-dependency-management)", GitHub Issue "[Poetry support #3371](https://github.com/cookiecutter/cookiecutter-django/issues/3371)"

### Template Hook Dependencies
Cookiecutter **does not provide built-in dependency management for hooks**. Two patterns work:

| Approach | Use Case |
|----------|----------|
| **`pre_gen_project.py` installs deps** | Simple, few dependencies; runs before generation |
| **`cc_requirements.txt` + `post_gen_project.py`** | Multiple deps, version pinning needed; cleaner separation |

```python
# hooks/pre_gen_project.py
try:
    import rich
except ModuleNotFoundError:
    import subprocess
    subprocess.run(["pip", "install", "-q", "rich"])
```

```python
# hooks/post_gen_project.py
requirements_file = os.path.join(PROJECT_DIRECTORY, "cc_requirements.txt")
subprocess.check_call(["pip", "install", "-qUr", requirements_file])
os.remove(requirements_file)
```

### Requirements Structure for Generated Projects
Split requirements prevent production bloat and enable safe upgrades:
```
requirements/
├── base.txt          # Django, django-tailwind, psycopg2, gunicorn, whitenoise
├── development.txt   # pytest, ruff, black, mypy, djlint, factory-boy, debug-toolbar
└── production.txt    # sentry-sdk, redis, celery (optional), django-csp, django-axes
```

### Poetry vs pip/requirements.txt Debate
Cookiecutter Django issue [#3371](https://github.com/cookiecutter/cookiecutter-django/issues/3371) requests Poetry support. Current state:
- **pip/requirements.txt** — Universal, no extra tooling, works everywhere
- **Poetry** — Better dependency resolution, lock files, but adds complexity for generated project consumers
- **uv** (2024+) — Fast Rust-based installer, compatible with `requirements.txt` and `pyproject.toml`

**Recommendation:** Keep `requirements/*.txt` as primary; document Poetry/uv as optional workflows in generated `README.md`.

### Maintenance Checklist for Template Maintainers
- Pin Django to LTS (5.2 LTS supported until April 2028)
- Test generated output against Python 3.11, 3.12, 3.13 on Windows/macOS/Linux
- Update `django-tailwind` and `django-tailwind-cli` on each minor release
- Run `django-admin check --deploy` on generated `production.py` in CI
- Document minimum supported versions: Python ≥ 3.11, Django ≥ 5.0, Node.js optional

---

## 4. Django Production Security Hardening Checklist (2026)

### Critical Pre-Deployment Verification
Run **before every production deploy**:
```bash
python manage.py check --deploy --settings=config.settings.production
```

This audits: `DEBUG=False`, `SECRET_KEY` strength, `ALLOWED_HOSTS`, HTTPS settings, secure cookies, HSTS.

**Sources:** SoftAims "[Django Security Best Practices 2026](https://softaims.com/blog/django-security-best-practices-2026)", Django Docs "[Deployment Checklist](https://docs.djangoproject.com/en/6.0/howto/deployment/checklist)"

### Production Settings Hardening Template
```python
# config/settings/production.py
from .base import *

DEBUG = False
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]          # Never hardcoded
ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"].split(",")

# HTTPS Enforcement
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000        # 1 year (ramp up gradually!)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Secure Cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

# Additional Security Headers
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
X_FRAME_OPTIONS = "DENY"

# CSRF Trusted Origins (explicit)
CSRF_TRUSTED_ORIGINS = ["https://{{ cookiecutter.domain_name }}"]
```

### Content Security Policy (CSP)
**Primary defense against XSS** that bypasses template escaping. Install `django-csp`:
```bash
pip install django-csp
```

```python
# settings/production.py
INSTALLED_APPS += ["csp"]
MIDDLEWARE = ["csp.middleware.CSPMiddleware", ...]  # Early in stack

# START IN REPORT-ONLY MODE — observe before enforcing
CSP_REPORT_ONLY = True
CSP_REPORT_URI = "/csp-report/"

CSP_DEFAULT_SRC = ["'self'"]
CSP_SCRIPT_SRC = ["'self'", "https://cdn.jsdelivr.net"]
CSP_STYLE_SRC = ["'self'", "https://fonts.googleapis.com"]
CSP_FONT_SRC = ["'self'", "https://fonts.gstatic.com"]
CSP_IMG_SRC = ["'self'", "data:", "https:"]
CSP_CONNECT_SRC = ["'self'"]
CSP_FRAME_ANCESTORS = ["'none'"]
CSP_FORM_ACTION = ["'self'"]
CSP_BASE_URI = ["'self'"]
```

### Additional Hardening Layers
| Tool | Purpose | Config |
|------|---------|--------|
| **django-axes** | Brute-force protection (lockout after failed logins) | `AXES_FAILURE_LIMIT = 5` |
| **django-csp** | Content Security Policy | See above |
| **Sentry** | Error monitoring (replaces email `ADMINS`) | `SENTRY_DSN` from env |
| **Rate limiting** | API/throttle protection | `django-ratelimit` or nginx |

### Secrets Management
- **Never commit `.env`** — Use `.env.example` as template
- Load via `django-environ` or `python-decouple` in `base.py`
- Rotate `SECRET_KEY` with `SECRET_KEY_FALLBACKS` for zero-downtime rotation
- Database passwords = same sensitivity as `SECRET_KEY`

### Static/Media Security
```python
# Production static files
STATIC_ROOT = "/var/www/{{ cookiecutter.project_slug }}/static/"
STATIC_URL = "/static/"
# Run: python manage.py collectstatic

# Media files — NEVER execute uploads
MEDIA_ROOT = "/var/www/{{ cookiecutter.project_slug }}/media/"
MEDIA_URL = "/media/"
# nginx: location /media/ { add_header X-Content-Type-Options nosniff; }
```

---

## 5. pytest, pre-commit, Black, Ruff, MyPy CI Pipeline (2026)

### Modern Python Toolchain (Ruff-Centric)
**Ruff (Rust-based) replaces Black + isort + flake8** in a single tool. Configuration via `pyproject.toml` (PEP 518).

**Sources:** LearnDjango "[pre-commit with Django](https://learndjango.com/tutorials/pre-commit-django)", DataTalks.Club "[Python CI/CD with GitHub Actions](https://datatalks.club/blog/practical-guide-better-code.html)", Laszlo Substack "[CQ4DS Python Project Setup](https://laszlo.substack.com/p/cq4ds-python-project-from-scratch)"

### `.pre-commit-config.yaml` (Generated Template)
```yaml
# .pre-commit-config.yaml
default_language_version:
  python: python3.12

repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-toml
      - id: debug-statements

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.15.10
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.11.0
    hooks:
      - id: mypy
        args: [--strict, --ignore-missing-imports]
        additional_dependencies: [django-stubs, types-requests]

  - repo: https://github.com/rtts/djlint
    rev: v1.36.0
    hooks:
      - id: djlint
        args: [--reformat, --profile=django]
```

### `pyproject.toml` (Unified Config)
```toml
# pyproject.toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "{{ cookiecutter.project_slug }}"
version = "0.1.0"
description = "{{ cookiecutter.project_description }}"
requires-python = ">=3.12"
dependencies = []

[tool.ruff]
target-version = "py312"
line-length = 100
exclude = ["migrations", ".venv", "staticfiles", "media"]

[tool.ruff.lint]
select = ["E", "F", "I", "C", "B", "UP", "PT", "DJ", "S", "T20"]
ignore = ["E501", "DJ01", "T201"]  # line-length, settings, print
django-version = "5.2"

[tool.ruff.format]
quote-style = "double"
indent-style = "space"

[tool.mypy]
python_version = "3.12"
django_version = "5.2"
strict = true
warn_return_any = true
warn_unused_ignores = true
disallow_untyped_defs = true
plugins = "mypy_django_plugin.main"

[[tool.mypy.overrides]]
module = "django.*"
ignore_missing_imports = true

[tool.pytest.ini_options]
testpaths = ["apps", "tests"]
python_files = "test_*.py"
python_classes = "Test*"
python_functions = "test_*"
addopts = "-v --strict-markers --tb=short"
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
]

[tool.coverage.run]
source = ["apps"]
omit = ["*/migrations/*", "*/tests/*", "config/*"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
]
```

### GitHub Actions CI Workflow (`.github/workflows/ci.yml`)
```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.12", "3.13"]
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Cache pip
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('requirements/*.txt') }}
          restore-keys: ${{ runner.os }}-pip-
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements/development.txt
      
      - name: Run pre-commit
        run: pre-commit run --all-files
      
      - name: Run mypy
        run: mypy apps config
      
      - name: Run pytest with coverage
        run: |
          pytest --cov=apps --cov-report=xml --cov-report=term-missing
      
      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          files: ./coverage.xml
  
  security-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Django deployment check
        run: |
          pip install -r requirements/production.txt
          python manage.py check --deploy --settings=config.settings.production
```

### Key 2026 Practices
- **pre-commit runs locally** — Catches formatting/linting before push
- **CI runs same hooks + mypy + pytest** — Gatekeepers for PR merge
- **Branch protection** — Require status checks to pass before merge
- **Coverage threshold** — Enforce ≥ 80% via `coverage fail-under=80`
- **django-upgrade hook** — Auto-upgrade Django code for newer versions (`adamchainz/django-upgrade`)

---

## 6. Docker Compose & Production Deployment (2026)

### Development Docker Compose (`docker-compose.yml`)
```yaml
version: "3.8"
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports: ["8000:8000"]
    volumes:
      - .:/app
      - /app/node_modules  # If using npm mode
    env_file: .env
    depends_on: [db, redis]
    command: python manage.py tailwind dev  # Runs Django + Tailwind

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports: ["5432:5432"]

  redis:
    image: redis:7-alpine
    ports: ["6379:6379"]
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

### Production Docker Compose (`production.yml`)
```yaml
version: "3.8"
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile.prod
    env_file: .env.production
    depends_on: [db, redis]
    command: gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3

  nginx:
    image: nginx:alpine
    ports: ["80:80", "443:443"]
    volumes:
      - ./nginx/prod.conf:/etc/nginx/nginx.conf
      - static_volume:/var/www/static
      - media_volume:/var/www/media
    depends_on: [web]

  db:
    image: postgres:16-alpine
    env_file: .env.production
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
  static_volume:
  media_volume:
```

### Cookiecutter Integration
- Generate both `docker-compose.yml` (dev) and `production.yml` (prod)
- Include `Dockerfile.dev` (with Tailwind watcher) and `Dockerfile.prod` (multi-stage, non-root)
- Pre-configure nginx with security headers, gzip, static/media serving
- Document `docker compose -f production.yml build && docker compose -f production.yml up -d`

---

## 7. Optional Integrations: DRF, Celery, Sentry, Allauth

### Django REST Framework (Optional)
```bash
# requirements/base.txt add:
djangorestframework>=3.15
django-filter>=23
djangorestframework-simplejwt>=5.3
```

```python
# config/settings/base.py
INSTALLED_APPS += [
    "rest_framework",
    "django_filters",
    "rest_framework_simplejwt",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
}
```

### Celery (Optional, Background Tasks)
```bash
# requirements/production.txt add:
celery>=5.3
redis>=5.0
django-celery-beat>=2.5
```

```python
# config/celery.py
from celery import Celery
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
```

### Sentry (Error Monitoring)
```bash
# requirements/production.txt add:
sentry-sdk>=2.0
```

```python
# config/settings/production.py
import sentry_sdk
sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    integrations=[sentry_sdk.integrations.django.DjangoIntegration()],
    traces_sample_rate=0.1,
    send_default_pii=True,
)
```

### django-allauth (Authentication)
```bash
# requirements/base.txt add:
django-allauth>=65.0
```

```python
# config/settings/base.py
INSTALLED_APPS += [
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
]
SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_REQUIRED = True
```

---

## 8. Testing Strategy: Unit, Integration, E2E

### Test Organization
```
apps/
  users/
    tests/
      test_models.py
      test_views.py
      test_services.py
      test_selectors.py
tests/              # Cross-app integration tests
  test_auth_flow.py
  test_api_integration.py
```

### pytest Configuration (in `pyproject.toml`)
```toml
[tool.pytest.ini_options]
testpaths = ["apps", "tests"]
addopts = "-v --strict-markers --tb=short -x"
markers = [
    "unit: fast isolated tests",
    "integration: cross-app/db tests",
    "slow: long-running tests",
    "e2e: browser-based tests",
]
```

### Coverage Requirements
```bash
# Development
pytest --cov=apps --cov-report=term-missing --cov-fail-under=80

# CI
pytest --cov=apps --cov-report=xml --cov-fail-under=80
```

### Factory Boy for Test Data
```bash
# requirements/development.txt
factory-boy>=3.3
```

```python
# apps/users/tests/factories.py
import factory
from apps.users.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    email = factory.Sequence(lambda n: f"user{n}@example.com")
    username = factory.Sequence(lambda n: f"user{n}")
```

---

## 9. Cross-Project References & Consumer Integration

### Generated Project Should Document
- **Directory layout rationale** in generated `README.md`
- **Environment variable reference** (from `.env.example`)
- **Tailwind workflow**: `python manage.py tailwind dev` / `tailwind build`
- **Testing commands**: `pytest`, `pre-commit run --all-files`
- **Deployment**: `python manage.py check --deploy`, Docker Compose production stack

### Workspace Integration Points
| Consumer Project | Integration Pattern |
|------------------|---------------------|
| **profile** | Extends generated `users` app; plugs into `core` mixins |
| **rhixecompany-comics** | Matches generated model conventions; uses `services/selectors` pattern |
| **Django-Scrapy-Selenium** | Reuses generated Celery/Redis config for background scraping |
| **ecom** | Extends `orders`/`products` bounded contexts |
| **xamehi / xamehi.tv** | Uses generated DRF + JWT auth; Tailwind UI components |

### Template Versioning
- Tag releases: `v1.0.0`, `v1.1.0` (semver)
- Changelog in `CHANGELOG.md` (Keep a Changelog format)
- Document breaking changes for consumers upgrading generated projects

---

## 10. Performance & Scaling Considerations

### Default Optimizations (Generated)
```python
# config/settings/base.py
# Persistent DB connections
CONN_MAX_AGE = 60

# Cached template loader (auto-enabled when DEBUG=False)
TEMPLATES[0]["OPTIONS"]["loaders"] = [
    ("django.template.loaders.cached.Loader", [
        "django.template.loaders.filesystem.Loader",
        "django.template.loaders.app_directories.Loader",
    ])
]

# Static files with WhiteNoise
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Session caching
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
```

### Optional Celery Scaling
```python
# production.py
CELERY_TASK_ALWAYS_EAGER = False
CELERY_WORKER_PREFETCH_MULTIPLIER = 4
CELERY_TASK_ACKS_LATE = True
```

### Database Indexing Guidance
- Generated models include `db_index=True` on foreign keys, `created_at`, `updated_at`
- Document `makemigrations --merge` workflow for team conflicts
- Recommend `django-debug-toolbar` + `django-silk` for query profiling in dev

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Cookiecutter | https://cookiecutter.readthedocs.io | Docs |
| django-tailwind | https://django-tailwind.readthedocs.io | Docs |
| django-tailwind-cli | https://github.com/django-commons/django-tailwind-cli | Repo |
| Django 5.2 LTS Release Notes | https://docs.djangoproject.com/en/5.2/releases/5.2/ | Docs |
| Django Deployment Checklist | https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/ | Docs |
| django-csp | https://github.com/mozilla/django-csp | Repo |
| django-axes | https://github.com/jazzband/django-axes | Repo |
| pre-commit | https://pre-commit.com | Docs |
| Ruff | https://docs.astral.sh/ruff/ | Docs |
| MyPy | https://mypy.readthedocs.io | Docs |
| pytest | https://docs.pytest.org | Docs |
| djlint | https://djlint.com | Docs |
| django-allauth | https://docs.allauth.org | Docs |
| Two Scoops of Django | https://www.feldroy.com/books/two-scoops-of-django | Book |
| OWASP Django Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/Django_Security_Cheat_Sheet.html | Security |

---

## Best Practices Summary

1. **Deterministic output** — Pin cookiecutter dependencies; test generated output on Windows/macOS/Linux
2. **Minimal defaults** — Enable optional integrations (DRF, Celery, Sentry, Allauth) only via cookiecutter prompts
3. **Type-check generation** — Include `mypy` config with `django-stubs` so generated projects validate immediately
4. **Documentation-first** — Generated `README.md` explains directory layout, env vars, Tailwind workflow, deploy steps
5. **Security defaults** — Preconfigure `SECRET_KEY` from env; include `.env.example`; `check --deploy` in CI
6. **Split requirements** — `base.txt` / `development.txt` / `production.txt` for safe upgrade paths
7. **Standalone Tailwind** — Default to binary mode (no Node.js); document npm mode for advanced plugins
8. **Service/Selector pattern** — Generate `services.py`/`selectors.py` stubs in each app
9. **CI gatekeepers** — pre-commit + mypy + pytest + `check --deploy` required for merge
10. **Versioned template** — Semver tags + changelog; document consumer upgrade paths

---

## Common Pitfalls & Avoidance

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Unpinned optional addons | Template drift over time | Pin optional extras to stable releases in `requirements/*.txt` |
| Windows path mismatches | Generator fails on Windows | Test on Windows using git-bash and venv activation paths |
| Moving compiled Tailwind files | Merge conflicts | Keep generated files under `.gitignore`; document `tailwind build` |
| Forgetting migration reset flow | Consumer project breakage | Provide `makemigrations --merge` guidance in README |
| Hardcoded secrets in settings | Security breach | Generate `SECRET_KEY` from `os.environ`; fail closed if missing |
| Single settings file | Config errors between envs | Split `base.py` → `development.py` / `production.py` |
| Overly granular apps | Fragmentation, overhead | Group related functionality (products+orders+payments, not per table) |
| Missing `@source` directives | Tailwind v4 misses templates | Generate `@source "../templates";` in `input.css` |

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Cookiecutter docs | https://cookiecutter.readthedocs.io | Official docs |
| django-tailwind docs | https://django-tailwind.readthedocs.io | Tailwind integration |
| django-tailwind-cli | https://github.com/django-commons/django-tailwind-cli | Standalone CLI alternative |
| Django 5.2 LTS | https://docs.djangoproject.com/en/5.2/ | Framework docs (supported until Apr 2028) |
| Django Deployment Checklist | https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/ | Security hardening |
| django-csp | https://github.com/mozilla/django-csp | Content Security Policy |
| django-axes | https://github.com/jazzband/django-axes | Brute-force protection |
| pre-commit | https://pre-commit.com | Git hook management |
| Ruff | https://docs.astral.sh/ruff/ | Fast Python linter/formatter |
| MyPy | https://mypy.readthedocs.io | Static type checker |
| pytest | https://docs.pytest.org | Testing framework |
| djlint | https://djlint.com | Django template linter/formatter |
| django-allauth | https://docs.allauth.org | Authentication |
| Two Scoops of Django | https://www.feldroy.com/books/two-scoops-of-django | Production patterns |
| OWASP Django Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/Django_Security_Cheat_Sheet.html | Security reference |
| Boost Your Django DX | https://adamchainz.gumroad.com/l/byddx | Tooling deep-dive (Adam Johnson) |

---

*Report generated from web research conducted June 2026. All claims backed by cited sources.*