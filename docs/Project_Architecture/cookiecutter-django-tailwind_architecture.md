# cookiecutter-django-tailwind — Architecture

## Overview
A Cookiecutter template for generating production-ready Django projects with Tailwind CSS integration. This is a scaffolding tool, not a running application.

## Architecture Pattern
- **Type:** Code Generator / Template
- **Pattern:** Cookiecutter project template with Jinja2 rendering
- **Output:** Full Django 5.x project with Tailwind CSS, Docker, CI/CD, and modern tooling

## Components
- **`{{cookiecutter.project_slug}}/`** — Generated Django project structure
- **`hooks/`** — Cookiecutter pre/post-generation hooks
- **`scripts/`** — Utility scripts for template maintenance
- **`tests/`** — Template output validation tests

## Cross-Cutting Concerns
- **CI/CD:** GitHub Actions for lint, test, security checks
- **Security:** pre-commit hooks, pip-audit, django-check-deploy
- **Quality:** ruff, mypy, djlint, pytest with coverage
- **Dev UX:** Docker Compose, hot-reload, environment splitting (local/production)

## Key Dependencies
- Python 3.12+, Django 5.x, Django REST Framework
- Tailwind CSS via django-tailwind, Alpine.js, htmx
- PostgreSQL (production), SQLite (development)
- Gunicorn, WhiteNoise, Sentry
