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

## Cheatsheets & Quick Reference
| Topic | Resource | Type |
|-------|----------|------|
| Cookiecutter | https://cookiecutter.readthedocs.io | Docs |
| django-tailwind | https://django-tailwind.readthedocs.io | Docs |
| django-tailwind-cli | https://github.com/django-commons/django-tailwind-cli | Repo |
| Django 5.2 LTS Release Notes | https://docs.djangoproject.com/en/5.2/releases/5.2/ | Docs |
| Django Deployment Checklist | https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/ | Docs |
| django-csp | https://github.com/mozilla/django-csp | Repo |

---

## Best Practices Summary
1. **Deterministic output** — Pin cookiecutter dependencies; test generated output on Windows/macOS/Linux
2. **Minimal defaults** — Enable optional integrations (DRF, Celery, Sentry, Allauth) only via cookiecutter prompts
3. **Type-check generation** — Include `mypy` config with `django-stubs` so generated projects validate immediately
4. **Documentation-first** — Generated `README.md` explains directory layout, env vars, Tailwind workflow, deploy steps
5. **Security defaults** — Preconfigure `SECRET_KEY` from env; include `.env.example`; `check --deploy` in CI
6. **Split requirements** — `base.txt` / `development.txt` / `production.txt` for safe upgrade paths
7. **Standalone Tailwind** — Default to binary mode (no Node.js); document npm mode for advanced plugins

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

---
