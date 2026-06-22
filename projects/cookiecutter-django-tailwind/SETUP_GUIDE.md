# Cookiecutter Django Tailwind — Setup Guide

Two types of setup: **Template Setup** (for template developers) and **Project Setup** (for generated project users).

## 1. Template Developer Setup

You want to work on the template itself.

```bash
git clone https://github.com/Rhixe-company/cookiecutter-django-tailwind
cd cookiecutter-django-tailwind
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

### Test Template Generation

```bash
cookiecutter . --no-input  # Generate with defaults
cd my-awesome-project/
python manage.py migrate
python manage.py runserver
```

## 2. Generated Project Setup

You generated a project from the template and want to run it.

### Without Docker

```bash
cd your-project/

# Create environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements/local.txt

# Set up database
createdb your-db-name
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### With Docker

```bash
cd your-project/
docker-compose -f docker-compose.local.yml build
docker-compose -f docker-compose.local.yml up
```

### Tailwind CSS Setup

If Tailwind was selected as frontend pipeline:

```bash
npm install
npm run dev  # Watches and compiles Tailwind
```

## Environment Variables

Generated projects use `django-environ`:

```bash
# .envs/.local/.django
USE_DOCKER=no
DATABASE_URL=postgres://user:***@localhost:5432/dbname
CELERY_BROKER_URL=redis://localhost:6379/0

# .envs/.production/.django
DJANGO_SETTINGS_MODULE=config.settings.production
DATABASE_URL=postgres://user:***@production-host:5432/dbname
```

## Prerequisites

- **Python** 3.12+
- **PostgreSQL** 12–16
- **Docker** (optional, for containerized development)
- **Node.js** 18+ (for Tailwind/Webpack)
- **Cookiecutter** ≥ 1.7.0 (to generate from template)

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `cookiecutter` command not found | `pip install cookiecutter` |
| Database connection error | Ensure PostgreSQL is running and `DATABASE_URL` is correct |
| Tailwind not compiling | Run `npm install` in project root |
| Docker build fails | Check Docker is running and ports are available |
