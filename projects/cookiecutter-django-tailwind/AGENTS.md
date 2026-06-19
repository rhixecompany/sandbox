# cookiecutter-django-tailwind
## Architecture

- **Blueprint**: [cookiecutter-django-tailwind Architecture](../docs/Project_Architecture/cookiecutter_django_tailwind_architecture.md)
- **Folders**: [cookiecutter-django-tailwind Folder Structure](../docs/Project_Architecture/cookiecutter_django_tailwind_folders.md)
- **Tech Stack**: [cookiecutter-django-tailwind Technology Stack](../docs/Project_Architecture/cookiecutter_django_tailwind_techstack.md)
- **Stack Type**: Django


Django 5.x + Tailwind generator (template repo).

## Stack
- Python 3.12+, Django 5.x, optional DRF
- django-tailwind; optional Alpine/htmx
- PostgreSQL (prod), SQLite (dev)
- Docker Compose, Gunicorn, WhiteNoise, Sentry
- pytest, pre-commit, Black, ruff, mypy, djlint

## Commands
```bash
cookiecutter gh:your-org/cookiecutter-django-tailwind
cd my_project
python -m venv .venv && source .venv/bin/activate
pip install -r requirements/local.txt
python manage.py migrate && python manage.py createsuperuser
python manage.py runserver
python manage.py tailwind start
pytest --cov
```

## Production
```bash
python manage.py check --deploy && python manage.py collectstatic
docker compose -f production.yml build && docker compose -f production.yml up -d
```

## Notes
- Settings: `base.py` → `local.py` → `production.py`
- django-environ for secrets; never commit secrets
- Tailwind utility-first; minimal custom CSS
