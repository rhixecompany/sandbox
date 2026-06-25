# Cookiecutter Django Tailwind

**Naming**: `snake_case` for Python files/variables/functions; `PascalCase` for classes; `UPPER_SNAKE_CASE` for constants/settings; `kebab-case` for CSS classes (Tailwind utility-first); snake_case for Django apps.

**Patterns**: Cookiecutter template for scaffolding new Django projects; settings split across `base.py` → `local.py` → `production.py`; django-environ for secrets; Tailwind CSS utility-first (minimal custom CSS); optional DRF, Alpine.js, htmx; `django-tailwind` integration.

**Structure**: Django project with split settings (`config/settings/`); apps as Python packages; `templates/` for Django templates; `static/` for static assets; `requirements/` for pip dependencies; `docker-compose/` for deployment.

**Python**: Python 3.12+; Django 5.x; PEP 8 via Black formatter; type hints (mypy); ruff for linting; pytest for testing; pre-commit hooks for CI.

**Database**: PostgreSQL (production); SQLite (development); settings-driven connection.

**CSS/Styles**: Tailwind utility-first; `django-tailwind` for build pipeline; minimal custom CSS; responsive design patterns.

**Testing**: pytest with `--cov` for coverage; pre-commit hooks (Black, ruff, mypy, djlint); `pytest-django` for Django-specific testing.

**Security**: django-environ for secrets management; no secrets in VCS; `python manage.py check --deploy` for production readiness; CSRF, XSS, clickjacking protection built-in.

**Production**: Gunicorn + WhiteNoise for static files; Sentry for error tracking; Docker Compose for deployment; `collectstatic` before deploy.

**Commands**: `cookiecutter gh:your-org/cookiecutter-django-tailwind` (scaffold); `python manage.py migrate && python manage.py createsuperuser` (setup); `python manage.py runserver` (dev); `python manage.py tailwind start` (CSS watch); `pytest --cov` (test); `python manage.py check --deploy && python manage.py collectstatic` (production); `docker compose -f production.yml up -d` (deploy).
