# Research Report: cookiecutter-django-tailwind

## Project Overview

**cookiecutter-django-tailwind** is a Cookiecutter template that scaffolds production-ready Django projects with integrated Tailwind CSS, Docker, CI/CD, and modern Python web best practices. It is a fork/variant of the upstream [`cookiecutter-django`](https://github.com/cookiecutter/cookiecutter-django) (13,400+ GitHub stars) enhanced with Tailwind CSS support via [`django-tailwind`](https://github.com/timonweb/django-tailwind).

**Type**: Cookiecutter project template (not a library or framework) — after generation it produces a standalone Django project.

**Current State**: Targets Django 5.x / Python 3.12+; tailwind-css integration via `django-tailwind` package; optimized for Docker Compose-based local and production environments.

## Similar Projects

| Project | Stars | Differentiator |
|---------|-------|----------------|
| [cookiecutter/cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django) | 13.4K+ | Upstream — vanilla (Bootstrap v5) without Tailwind |
| [Alurith/django-cookiecutter](https://github.com/Alurith/django-cookiecutter) | ~200 | Postgres + htmx + Tailwindcss, Docker-focused |
| [imAsparky/django-cookiecutter](https://codeberg.org/imAsparky/django-cookiecutter) | ~50 | Django 5.0+, moved to Codeberg, CI/CD with GitHub Actions |
| [dantium/django-docker-tailwind](https://github.com/dantium/django-docker-tailwind) | ~100 | Wagtail CMS + Tailwind + Docker, based on cookiecutter |

## Key Findings

1. **Tailwind Integration Path**: Uses `django-tailwind` (by timonweb) which creates a `theme` Django app managing npm-based or standalone-binary Tailwind builds. Hot-reload via `django-browser-reload` middleware in development.

2. **Settings Architecture**: Three-tier settings split — `base.py` → `local.py` → `production.py` — following the pattern popularized by *Two Scoops of Django*. All secrets managed via `django-environ`.

3. **Docker Strategy**: Two Docker Compose files — `compose/local.yml` for development (with live-reload) and `compose/production.yml` for deployment (Gunicorn + Nginx/Traefik + PostgreSQL).

4. **Frontend Flexibility**: Template offers Alpine.js and htmx as opt-in frontend enhancements alongside Tailwind, minimizing custom JavaScript.

5. **CI/CD Pipeline**: GitHub Actions workflow runs lint (ruff, mypy, pre-commit), test (pytest with coverage), and security checks (pip-audit) on every push.

## Best Practices Inferred

| Area | Practice |
|------|----------|
| **Configuration** | 12-Factor app — environment variables via `django-environ`, settings split by environment |
| **Testing** | pytest with pytest-cov, `--cov-fail-under`, factory_boy for fixtures |
| **Code Quality** | pre-commit hooks (ruff, mypy, black, isort, djlint), commitizen for conventional commits |
| **Security** | `python manage.py check --deploy` before deploy, HTTPS enforced, CSP via django-csp (optional), Sentry for error tracking |
| **Docker** | Separate dev/prod compose files, multi-stage builds, health checks |
| **Auth** | django-allauth with custom user model, social auth optional |
| **Static Files** | WhiteNoise for production, ManifestStaticFilesStorage for cache-busting |

## Common Pitfalls

- **Tailwind not building** — Node.js must be available; `NPM_BIN_PATH` may need explicit config on Windows
- **Docker + Tailwind watch** — The Tailwind watcher process inside Docker requires careful volume mapping; use `honcho` (Procfile) to coordinate Django and Tailwind processes
- **Cache-busting** — `ManifestStaticFilesStorage` can break `/css/source.css` paths if not excluded; django-tailwind-cli handles this with `TAILWIND_CSS_PATH`
- **Migration conflicts** — Use `python manage.py makemigrations --merge` to resolve auto-generated migration overlaps

## Performance Considerations

- WhiteNoise with compression and far-future Cache-Control headers for static assets
- PostgreSQL connection pooling (optional PgBouncer in production)
- Gunicorn with `(2 × CPU cores) + 1` workers as baseline
- Celery for background task offloading (optional, opt-in at generation time)
- django-silk or django-debug-toolbar in development only

## Security Checklist

1. **DEBUG=False** in production; **SECRET_KEY** via env var, never committed
2. **HTTPS enforced** via `SECURE_SSL_REDIRECT` + `SECURE_HSTS_SECONDS`
3. **ALLOWED_HOSTS** restricted per environment
4. **Run `manage.py check --deploy`** before deployment
5. **Django defaults** (CSRF, XSS, clickjacking) enabled; Sentry for monitoring

## Related Projects & Resources

- **[django-tailwind](https://github.com/timonweb/django-tailwind)** — Tailwind + Django integration used by this template
- **[cookiecutter-django docs](https://cookiecutter-django.readthedocs.io/)** — Upstream template documentation
- **[SaaS Pegasus](https://www.saaspegasus.com/)** — Paid alternative with Stripe, teams, multi-tenancy
- **[django-cookiecutter (imAsparky)](https://codeberg.org/imAsparky/django-cookiecutter)** — Alternative Django 5.0+ template

---

*Research compiled June 2026. Sources: GitHub, ReadTheDocs, community discussions.*
