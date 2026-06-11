# Copilot Instructions — cookiecutter-django-tailwind

## Python Code Style
- Black formatter (88 char line length)
- ruff for linting (PEP 8)
- isort for import sorting
- Type hints with mypy

## Django Conventions
- Apps under `apps/` directory
- Settings split: base.py → local.py → production.py
- Never edit existing migrations
- Use django-environ for secrets

## Frontend
- Utility-first with Tailwind CSS
- Minimal custom CSS
- Prefer htmx/Alpine.js over custom JS

## Testing
- pytest for all tests
- Factory Boy for test data
- pytest-cov for coverage
