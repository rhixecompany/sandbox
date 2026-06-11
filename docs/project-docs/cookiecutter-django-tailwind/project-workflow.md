# Project Workflow — cookiecutter-django-tailwind

## Generating a New Project

```bash
cookiecutter gh:your-org/cookiecutter-django-tailwind
# Answer prompts: project name, slug, DB choice, etc.
cd my_project
```

## Development Workflow
```bash
# Setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements/local.txt
python manage.py migrate
python manage.py createsuperuser

# Run
python manage.py runserver
python manage.py tailwind start  # CSS dev server

# Quality
pre-commit run --all-files
pip-audit                      # Security check
pytest                          # Run tests
```

## Deployment
```bash
python manage.py check --deploy
python manage.py collectstatic
docker compose -f production.yml up -d
```
