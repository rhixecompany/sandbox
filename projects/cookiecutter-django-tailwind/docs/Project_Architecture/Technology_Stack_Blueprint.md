# Technology Stack Blueprint

## Project: cookiecutter-django-tailwind — Django Template

> **Generated:** 2026-06-25  
> **Generator:** technology-stack-blueprint-generator  
> **Analysis Depth:** Comprehensive

---

## Overview

A cookiecutter project template for generating Django 5.x projects with Tailwind CSS, providing a modern, production-ready starting point with best practices baked in.

**Project Type:** Project Generator / Template  
**Stack Type:** Django

---

## Technology Stack

### Languages & Runtimes

| Technology | Version | Usage |
|---|---|---|
| Python | ^3.12 | Backend language |
| Django | ^5.x | Web framework |
| JavaScript | — | Frontend (Tailwind) |
| HTML (Django Templates) | — | Server-side rendering |
| CSS (Tailwind) | — | Styling |

### Core Dependencies (Generated Project)

| Category | Technologies |
|---|---|
| **Web Framework** | Django 5.x |
| **API Framework** | Django REST Framework (optional) |
| **Frontend** | Tailwind CSS (via django-tailwind), Alpine.js, htmx |
| **Database** | PostgreSQL (production), SQLite (development) |
| **ASGI/WSGI** | Gunicorn, uvicorn |
| **Static Files** | WhiteNoise |
| **Monitoring** | Sentry SDK |
| **Security** | django-environ |

### Development Tools

| Tool | Purpose |
|---|---|
| pytest + pytest-cov | Testing & coverage |
| pre-commit | Git hook management |
| Black | Code formatting |
| ruff | Linting |
| mypy | Type checking |
| djlint | Django template linting |
| isort | Import sorting |

---

## Licensing

| Component | License |
|---|---|
| cookiecutter-django-tailwind | (template - license varies per generated project) |

---

## Project Structure (Generated)

```
my_project/
├── config/
│   ├── settings/
│   │   ├── base.py         # Shared settings
│   │   ├── local.py        # Development settings
│   │   └── production.py   # Production settings
│   ├── urls.py
│   └── wsgi.py
├── apps/                    # Django applications
├── static/                  # Static assets
├── templates/               # Django templates
├── requirements/
│   ├── base.txt
│   ├── local.txt
│   └── production.txt
├── Dockerfile
├── docker-compose.yml
└── pyproject.toml
```

---

## Scripts

| Command | Description |
|---|---|
| `cookiecutter gh:your-org/cookiecutter-django-tailwind` | Generate new project |
| `python manage.py runserver` | Development server |
| `python manage.py tailwind start` | Tailwind CSS build watcher |
| `pytest --cov` | Run tests with coverage |
| `python manage.py check --deploy` | Production readiness check |
| `python manage.py collectstatic` | Static file collection |

---

## Coding Conventions

- **Settings layering**: `base.py` → `local.py` → `production.py`
- **Environment variables**: Via django-environ (never commit secrets)
- **Tailwind utility-first**: Minimal custom CSS
- **PEP 8**: Python code style
- **Type hints**: Modern Python typing
- **12-factor app principles**: Config from environment

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│           Generated Django Project                    │
├─────────────────────────────────────────────────────┤
│  Django 5.x                                          │
│  ├── Apps (modular Django applications)              │
│  ├── REST API (optional DRF)                         │
│  └── Admin Interface                                 │
├─────────────────────────────────────────────────────┤
│  Frontend                                            │
│  ├── Tailwind CSS (utility-first)                    │
│  ├── Alpine.js / htmx (optional interactivity)       │
│  └── Django Templates (server-rendered)              │
├─────────────────────────────────────────────────────┤
│  Infrastructure                                      │
│  ├── PostgreSQL (prod) / SQLite (dev)               │
│  ├── Gunicorn + WhiteNoise                          │
│  ├── Docker Compose                                 │
│  └── Sentry (error monitoring)                      │
├─────────────────────────────────────────────────────┤
│  Quality                                            │
│  ├── pytest + coverage                               │
│  ├── Black + ruff + mypy                            │
│  ├── pre-commit hooks                               │
│  └── djlint (template linting)                      │
└─────────────────────────────────────────────────────┘
```

---

## Cookiecutter Template

| Aspect | Details |
|---|---|
| Template Engine | Cookiecutter (Jinja2-based) |
| Variables | `project_slug`, `author_name`, etc. |
| Post-generation hooks | Git init, pip install, migrations |
