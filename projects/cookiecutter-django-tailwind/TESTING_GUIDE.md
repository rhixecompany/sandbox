# Cookiecutter Django Tailwind — Testing Guide

## Testing the Template

### Running Template Tests

```bash
# From template root
pip install -r requirements.txt
pytest

# Run specific test modules
pytest tests/test_cookiecutter_generation.py
pytest tests/test_hooks.py

# Bash-based tests
bash tests/test_bare.sh
bash tests/test_docker.sh
```

### Test Structure

```
tests/
├── __init__.py
├── test_bare.sh                      # Quick CLI generation test
├── test_cookiecutter_generation.py   # Full generation pipeline
├── test_docker.sh                    # Docker-based generation
└── test_hooks.py                     # Pre/post hook execution
```

### What Tests Cover

#### `test_cookiecutter_generation.py`
- Full project generation with various option combinations
- Generated project structure validation
- Django check passes on generated project
- Pytest runs successfully on generated project
- Database migrations work

#### `test_hooks.py`
- `pre_gen_project.py` validation logic
- `post_gen_project.py` cleanup operations
- Proper error handling for invalid inputs

## Testing Generated Projects

After generating a project, test the output:

```bash
cd /path/to/generated-project

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install production requirements
pip install -r requirements/local.txt

# Run Django checks
python manage.py check

# Run tests
pytest

# Coverage report
coverage run -m pytest
coverage html
```

### What Generated Project Tests Cover

Generated `{{project_slug}}/users/tests/`:

```
tests/
├── factories.py          # Test factories
├── test_admin.py         # Admin interface tests
├── test_drf_urls.py      # DRF URL resolution
├── test_drf_views.py     # DRF view tests
├── test_forms.py         # Form validation
├── test_managers.py      # User manager tests
├── test_models.py        # Model tests
├── test_swagger.py       # API schema tests
├── test_tasks.py         # Celery task tests
├── test_urls.py          # URL resolution
└── test_views.py         # View tests
```

## Tox Testing

The template uses `tox.ini` for multi-environment testing:

```bash
tox
```

Tests across Python 3.12 and Django 5.0.

## CI Integration

GitHub Actions CI runs:

```yaml
# .github/workflows/ci.yml
- name: Test
  run: |
    pip install -r requirements.txt
    pytest
    bash tests/test_bare.sh
```
