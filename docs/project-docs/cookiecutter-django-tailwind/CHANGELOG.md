# Cookiecutter Django Tailwind — Changelog

## [0.1.0] — 2026-05-27

### Added
- Initial Cookiecutter Django template with Tailwind CSS integration
- Django 5.0 support with Python 3.12
- PostgreSQL 12–16 support (configurable at generation)
- django-environ for 12-Factor settings
- django-allauth for user registration and social auth
- Custom Django user model included in generated projects
- Tailwind CSS v5 with automatic recompilation
- Production-ready Docker Compose setup with Traefik + Let's Encrypt
- Development Docker Compose for local containerized development
- Celery integration with Redis broker (optional)
- Django REST Framework integration (optional)
- Sentry error tracking (optional)
- Heroku deployment configuration
- CI/CD with GitHub Actions, GitLab CI, Travis CI (configurable)
- Pre-commit hooks (Black, Ruff, check YAML/JSON)
- Pytest with 100% starting test coverage
- Coverage reports for generated projects
- Anymail integration for transactional email (Mailgun, SES, etc.)
- Cloud storage support: S3, GCS, Azure
- npm/webpack for frontend asset compilation
- ReadTheDocs documentation
- Issue templates and contributing guidelines
- FUNDING.yml for project sponsorship
- Dependabot configuration for dependency updates
- PostgreSQL backup scripts for Docker production setup
- Nginx configuration for production static/media serving
- ASGI/WebSocket support (optional)

### Changed
- Initial release

### Security
- SECURE_SSL_REDIRECT enabled in production
- CSRF_COOKIE_SECURE = True in production
- SESSION_COOKIE_SECURE = True in production
- X_FRAME_OPTIONS = DENY
- Password validation enabled
- Environment secrets managed via .env files (never committed)
- HTTPS enforced via Traefik (Docker) or platform defaults
