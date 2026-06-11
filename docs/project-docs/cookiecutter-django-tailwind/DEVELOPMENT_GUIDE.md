# Cookiecutter Django Tailwind — Development Guide

## Template Development Workflow

### Setup for Template Development

```bash
git clone https://github.com/Rhixe-company/cookiecutter-django-tailwind
cd cookiecutter-django-tailwind
pip install -r requirements.txt
pip install -e .
```

### Running Template Tests

```bash
pytest tests/
```

Test structure:
```
tests/
├── test_bare.sh                      # Basic generation test
├── test_cookiecutter_generation.py   # Full generation + validation
├── test_docker.sh                    # Docker-based generation test
├── test_hooks.py                     # Pre/post generation hooks
└── __init__.py
```

### Modifying the Template

1. **Edit `cookiecutter.json`** — Add/remove prompts
2. **Edit `{{cookiecutter.project_slug}}/`** — Modify generated project files
3. **Edit `hooks/`** — Update pre/post generation logic
4. **Update `docs/`** — Keep documentation in sync

### Testing Changes

```bash
# Generate a test project
cookiecutter . --no-input -o /tmp/test-project

# Check generated structure
ls -la /tmp/test-project/

# Run generated project tests
cd /tmp/test-project/
pytest
```

## Generated Project Development

After generating a project, follow these workflows:

### Django Commands

```bash
python manage.py runserver       # Dev server at :8000
python manage.py shell           # Django shell
python manage.py dbshell         # Database shell
python manage.py show_urls       # List all routes
python manage.py showmigrations  # Migration status
python manage.py makemigrations  # Create new migrations
python manage.py migrate         # Apply migrations
```

### Quality Tools

| Tool | Command | Purpose |
|------|---------|---------|
| Black | `black .` | Code formatting |
| Ruff | `ruff check .` | Python linting |
| mypy | `mypy .` | Type checking |
| pytest | `pytest` | Test runner |
| coverage | `coverage run -m pytest` | Test coverage |

### Pre-commit Hooks

```bash
pre-commit install
pre-commit run --all-files
```

Configured in `.pre-commit-config.yaml`:
- Black formatter
- Ruff linter
- Check YAML/JSON
- End of file fixer
- Trailing whitespace

### Celery (If Enabled)

```bash
celery -A config.celery_app worker -l info
celery -A config.celery_app beat -l info
```

## Style Guide

- **Python**: PEP 8 enforced by Ruff + Black
- **Django**: Follow Django best practices
- **Templates**: django-allauth patterns for auth views
- **Settings**: 12-factor via django-environ
- **CSS**: Tailwind utility classes + custom SCSS variables

## CI/CD for Template

GitHub Actions workflows:

- `ci.yml` — Run template tests on push/PR
- `pre-commit-autoupdate.yml` — Keep hooks updated
- `update-changelog.yml` — Auto-generate changelog
- `issue-manager.yml` — Issue management automation
