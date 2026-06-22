# Technology Stack — cookiecutter-django-tailwind

## Overview
Cookiecutter template for Django projects with Tailwind CSS integration.

## Backend
| Technology | Purpose |
|------------|---------|
| Python 3.12+ | Runtime |
| Django 5.x | Web framework |
| Django REST Framework | API layer (optional) |
| Gunicorn | WSGI server |
| WhiteNoise | Static file serving |
| django-environ | Environment config |
| django-allauth | Social auth |
| django-crispy-forms | Form rendering |
| Sentry | Error tracking |

## Frontend
| Technology | Purpose |
|------------|---------|
| Tailwind CSS | Utility-first CSS |
| django-tailwind | Tailwind integration |
| Alpine.js | Lightweight JS (optional) |
| htmx | AJAX/HTML (optional) |

## Database & Infrastructure
| Technology | Purpose |
|------------|---------|
| PostgreSQL | Production database |
| SQLite | Development database |
| Docker Compose | Containerization |
| Redis | Cache/queues (optional) |

## Quality & CI/CD
| Tool | Purpose |
|------|---------|
| pytest | Testing framework |
| pytest-cov | Coverage reports |
| pre-commit | Git hooks |
| ruff | Python linter |
| mypy | Type checking |
| djlint | HTML template linting |
| GitHub Actions | CI/CD pipeline |
| pip-audit | Security auditing |
