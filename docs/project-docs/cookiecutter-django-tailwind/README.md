# cookiecutter-django-tailwind — Django + Tailwind Template

A Cookiecutter template for Django projects with Tailwind CSS integration. Generates production-ready Django projects with modern frontend tooling.

## Tech Stack
- **Backend**: Python 3.12+, Django 5.x, DRF
- **Frontend**: Tailwind CSS, Alpine.js, htmx
- **Infrastructure**: Docker Compose, Gunicorn, WhiteNoise
- **Quality**: pytest, pre-commit, ruff, mypy, GitHub Actions

## Quick Start
```bash
cookiecutter gh:your-org/cookiecutter-django-tailwind
cd my_project
pip install -r requirements/local.txt
python manage.py migrate
python manage.py runserver
```

## Documentation Links
- [Technology Stack](technology-stack.md)
- [Architecture](architecture.md)
- [Folder Structure](folder-structure.md)
- [Code Exemplars](code-exemplars.md)
