# cookiecutter-django-tailwind
**Python**: Black line-88, ruff, isort, mypy.
**Django**: apps under `apps/`; settings split `base.py`/`local.py`/`production.py`; never edit existing migrations; django-environ.
**Frontend**: Tailwind utility-first; minimal custom CSS; prefer htmx/Alpine over custom JS.
**Testing**: pytest; Factory Boy; `pytest-cov`.
