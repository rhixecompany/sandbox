# Cookiecutter Django Tailwind — Contributing Guide

## How to Contribute

We welcome contributions! Whether you're fixing bugs, adding features, or improving documentation, here's how.

## Quick Start

```bash
git clone https://github.com/Rhixe-company/cookiecutter-django-tailwind
cd cookiecutter-django-tailwind
pip install -r requirements.txt
pip install -e .
```

## Development Process

1. **Fork the repo** and create your branch from `master`
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Make your changes** to template files or hooks
4. **Test your changes**:
   ```bash
   pytest tests/
   # Or generate a test project
   cookiecutter . --no-input -o /tmp/test
   ```
5. **Run pre-commit**: `pre-commit run --all-files`
6. **Submit a PR** with clear description

## What We're Looking For

- **Bug fixes** for template generation issues
- **Feature additions** that benefit most users (keep configurable)
- **Updated integrations** (new Django/Celery/DRF versions)
- **Documentation improvements**
- **Test coverage** for edge cases

## Code Standards

- **Python**: PEP 8 (enforced by Ruff + Black, line length 88)
- **Django**: Follow Django's style and conventions
- **Templates**: Jinja2 for `{{cookiecutter.*}}` variables, keep readable
- **Hooks**: Clean Python with type hints
- **Documentation**: RST for generated docs, Markdown for template docs

## Pull Request Guidelines

- Keep changes focused — one feature/fix per PR
- Include tests for new functionality
- Update documentation for user-facing changes
- Test generated project with `cookiecutter . --no-input`
- Ensure CI passes

## Testing

```bash
# Run all tests
pytest

# Test generation specifically
pytest tests/test_cookiecutter_generation.py

# Test hooks
pytest tests/test_hooks.py

# Bash-based tests
bash tests/test_bare.sh
```

## Questions?

- Open an [issue](https://github.com/Rhixe-company/cookiecutter-django-tailwind/issues)
- Join the [Discord](https://discord.gg/rAWFUP47d2)
- Read the [docs](https://cookiecutter-django.readthedocs.io/)
