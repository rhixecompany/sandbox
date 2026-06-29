# GitHub Copilot Instructions — cookiecutter-django-tailwind

## Priority Guidelines

When generating code for this repository:

1. **Version Compatibility**: Always detect and respect the exact versions of languages, frameworks, and libraries used in this project
2. **Context Files**: Prioritize patterns and standards defined in the .github/copilot directory
3. **Codebase Patterns**: When context files don't provide specific guidance, scan the codebase for established patterns
4. **Architectural Consistency**: Maintain our **Layered** architectural style and established boundaries
5. **Code Quality**: Prioritize **maintainability, testability, and security** in all generated code

## Technology Version Detection

Before generating code, scan the codebase to identify:

1. **Language Versions**: Detect the exact versions of programming languages in use
   - **Python** — check `pyproject.toml` for `target-version` (Python 3.12)
   - **JavaScript/Node.js** — check generated project's `package.json`

2. **Framework Versions**: Identify the exact versions of all frameworks
   - **Django 5.x** — check `pyproject.toml` and generated project requirements
   - **Django REST Framework** (optional) — check install configuration
   - **Tailwind CSS** via django-tailwind
   - **Alpine.js** (optional) — check cookiecutter options
   - **htmx** (optional) — check cookiecutter options

3. **Library Versions**: Note the exact versions of key libraries and dependencies
   - **PostgreSQL** (production), SQLite (development)
   - **Celery** for async tasks (if configured)
   - **pytest** with coverage
   - **ruff** for linting, **black** for formatting (line-length 119)
   - **pre-commit** hooks
   - **Sentry** for error tracking
   - **WhiteNoise** for static files
   - **Gunicorn** for production WSGI

## Context Files

Prioritize the following files in .github/copilot directory (if they exist):

- **architecture.md**: System architecture guidelines
- **tech-stack.md**: Technology versions and framework details
- **coding-standards.md**: Code style and formatting standards
- **folder-structure.md**: Project organization guidelines
- **exemplars.md**: Exemplary code patterns to follow

## Codebase Scanning Instructions

When context files don't provide specific guidance:

1. Identify similar files to the one being modified or created
2. Analyze patterns for:
   - **Naming conventions**: snake_case for Python, PascalCase for classes, lowercase with underscores for modules
   - **Code organization**: Django apps under `{{cookiecutter.project_slug}}/`, settings split into `base.py`, `local.py`, `production.py`
   - **Testing**: pytest with Django test markers
   - **Templates**: Django template language with crispy forms
   - **CSS**: Utility-first with Tailwind, minimal custom CSS
   - **JavaScript**: Minimal — prefer htmx/Alpine.js over custom JS
3. Follow the most consistent patterns found in the codebase
4. When conflicting patterns exist, prioritize patterns in newer files or files with higher test coverage
5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

- Write self-documenting code with clear naming
- Follow Black formatting (line-length 119) and ruff linting
- Use isort with Black-compatible profile for imports
- Use pre-commit hooks for automated quality checks
- Maintain type hints with mypy

## Documentation Requirements

- Follow the exact documentation format found in the codebase
- Match the style and completeness of existing comments
- Document parameters, returns, and exceptions in the same style
- Follow existing patterns for usage examples

## Testing Approach

- Match the exact structure and style of existing tests
- **Unit tests**: pytest with Django test configuration
- **Coverage**: use `pytest --cov` for coverage reports
- Follow existing patterns for test organization

## Technology-Specific Guidelines

### Python/Django
- Follow Django's coding style and project conventions
- Use PEP 8 conventions, type hints with mypy
- Split settings into `base.py`, `local.py`, `production.py`
- Always create new migrations, never edit existing ones
- Use django-environ for environment variable management

### Tailwind CSS
- Utility-first approach — prefer Tailwind utility classes over custom CSS
- Use django-tailwind for integration
- Configure via `tailwind.config.js` in generated projects

### Pre-commit
- Use pre-commit hooks for automated quality checks
- Run `pre-commit run --all-files` before commits

## Version Control Guidelines

- Follow Semantic Versioning patterns as applied in the codebase
- Match existing patterns for documenting breaking changes

## General Best Practices

- Follow naming conventions exactly as they appear in existing code
- Match code organization patterns from similar files
- Apply error handling consistent with existing patterns
- Follow the same approach to testing as seen in the codebase
- Never commit SECRET_KEY, database passwords, or API keys
- Use environment variables for all secrets via django-environ

## Project-Specific Guidance

- Scan the codebase thoroughly before generating any code
- Respect existing architectural boundaries without exception
- This is a **Cookiecutter template** — generated output goes into `{{cookiecutter.project_slug}}/`
- Django settings split by environment: base.py, local.py, production.py
- Default database: PostgreSQL (production), SQLite (development)
- Deployment targets: Docker (DigitalOcean, Railway, Fly.io) or PaaS (Heroku)
- Docker Compose for local development and production
