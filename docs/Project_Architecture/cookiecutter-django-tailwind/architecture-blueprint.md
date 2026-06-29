# Architecture Blueprint: cookiecutter-django-tailwind

**Generated:** 2026-06-29  
**Generator:** architecture-blueprint-generator  

---

## 1. Architecture Detection and Analysis

### Technology Stack

| Category | Technology |
|---|---|
| **Template Engine** | Cookiecutter (Jinja2) |
| **Generated Backend** | Python 3.12+, Django 5.x, Django REST Framework |
| **Generated Frontend** | Tailwind CSS (via django-tailwind), Alpine.js, htmx |
| **Generated Database** | PostgreSQL (prod), SQLite (dev) |
| **Generated Infrastructure** | Docker Compose, Gunicorn, WhiteNoise |
| **Generated Quality** | pre-commit, ruff, mypy, djlint, pytest |
| **Generated CI/CD** | GitHub Actions (lint, test, security) |
| **Package Manager** | pip, npm |

### Architectural Pattern Detected

**Pattern:** Cookiecutter Template → Generated Django Project  
This is a **project generator** (cookiecutter template), not a running application. It produces production-ready Django projects with:

- **Settings Split**: `base.py` → `local.py` → `production.py` inheritance
- **Modular Apps**: Django apps under `apps/` namespace
- **Frontend Pipeline**: django-tailwind → npm → Tailwind CSS → compiled CSS
- **Containerized**: Docker Compose for development and production

---

## 2. Architectural Overview

### Template Architecture

```
cookiecutter-django-tailwind/
├── cookiecutter.json          # Prompts and defaults
├── {{cookiecutter.project_slug}}/  # Jinja2-templated project scaffold
├── hooks/                     # Pre/post-generation hooks
└── requirements.txt           # Template development dependencies
```

### Generated Project Architecture

```
my_project/
├── config/
│   ├── settings/
│   │   ├── base.py           # Shared settings
│   │   ├── local.py          # Development overrides
│   │   └── production.py     # Production overrides
│   ├── urls.py
│   └── wsgi.py
├── apps/                     # Modular Django applications
├── static/                   # Collected static files
├── templates/                # Django templates
├── Dockerfile
├── docker-compose.yml
└── pyproject.toml
```

---

## 3. Key Design Decisions

| Decision | Rationale |
|---|---|
| Settings split by environment | Secure defaults per environment, no overlap |
| Apps under `apps/` namespace | Clean organization, avoids naming conflicts |
| django-tailwind for frontend | Tight Django integration, no separate build tool |
| pre-commit for quality | Automated checks before every commit |
| GitHub Actions CI/CD | Industry standard, free for public repos |

---

## 4. Implementation Patterns

### Generated App Structure
Each generated Django app follows a standard pattern: `models.py`, `views.py`, `urls.py`, `admin.py`, `tests/`.

### Frontend Pipeline
1. `python manage.py tailwind start` (dev) compiles Tailwind CSS
2. `python manage.py tailwind build` (production) minifies output
3. Static files served via WhiteNoise or CDN

### Testing Pattern
Generated projects use pytest with django-test-migrations for database migration testing.

---

## 5. Extensibility Points

1. **Additional boilerplate**: Add new app templates under `{{cookiecutter.project_slug}}/`
2. **Alternative frontends**: Swap django-tailwind for Vite/webpack
3. **Additional CI/CD targets**: Add GitLab CI or CircleCI configurations
4. **Cloud-specific configs**: Add Terraform or Pulumi templates

---

*End of architecture blueprint.*
