# Architecture — cookiecutter-django-tailwind

## Overview
A Cookiecutter template that generates production-ready Django projects with Tailwind CSS, Docker, CI/CD, and best practices.

## Template Architecture

### 1. Cookiecutter Layer
- `cookiecutter.json` defines prompts and defaults
- Jinja2 templating in `{{cookiecutter.project_slug}}/`
- Pre/post-generation hooks in `hooks/`

### 2. Generated Project Layers

**Settings Split**: `base.py` → `local.py` → `production.py` inheritance chain

**App Structure**: Django apps under `apps/` directory with modular design

**Frontend Pipeline**: django-tailwind → npm → Tailwind CSS → compiled CSS

**Infrastructure**: Docker Compose for local and production environments

## Key Design Decisions
1. Settings split by environment (base/local/production)
2. Django apps organized under `apps/` namespace
3. Frontend assets managed via django-tailwind + npm
4. Docker Compose for consistent environments
5. pre-commit for automated quality checks
6. GitHub Actions for CI/CD with lint, test, security checks
