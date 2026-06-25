<<<<<<< HEAD
# AGENTS.md

> **Refreshed by AGENTS workflow 2026-06-01**

## Project Overview

RhixeCompany Profile — a Django-based blog/profile website with rich content editing, tagging, commenting, and Google Cloud Storage integration. Serves as the company's content management and profile platform.

**Tech Stack:**
- **Backend**: Python 3.10, Django 3.x, Django REST Framework
- **Content**: django-ckeditor (rich text), django-crispy-forms, django-filter
- **Storage**: Google Cloud Storage (django-storages[google]), Amazon S3 also supported
- **Database**: PostgreSQL (via psycopg2-binary)
- **Deployment**: Gunicorn, WhiteNoise for static files
- **Models**: Profile, Post, Tag, PostComment (blog-style content)

## Setup Commands

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

## Development Workflow

```bash
# Start dev server
python manage.py runserver

# Make migrations after model changes
python manage.py makemigrations
python manage.py migrate

# Collect static files
python manage.py collectstatic
```

## Testing Instructions

```bash
# Run Django tests
python manage.py test

# Or with pytest
pytest
```

## Code Style

- **Python**: Django standard conventions, PEP 8
- **Models**: Follow Django model best practices with `__str__`, `Meta`, `get_absolute_url`
- **Admin**: Custom ModelAdmin classes with list_display, search_fields, list_filter
- **Templates**: Django template language with crispy forms for rendering
- **URLs**: App-level url configs with namespacing
- **Views**: Class-based views preferred over function-based where possible

## Build/Deployment

```bash
# Production build
python manage.py check --deploy
python manage.py collectstatic

# Run with Gunicorn
gunicorn profile.wsgi:application --bind 0.0.0.0:8000

# Environment variables needed
DJANGO_SECRET_KEY=
DATABASE_URL=
GS_BUCKET_NAME=  # or AWS_STORAGE_BUCKET_NAME
```

Deploy to Google Cloud Run, App Engine, or any VPS with Gunicorn + Nginx.

## Security

- Never commit `SECRET_KEY` or any credentials
- Use django-environ for environment variable management
- CKEditor allows HTML — sanitize user input carefully to prevent XSS
- CSRF protection enabled by default (Django)
- SQL injection protection via Django ORM (never raw queries)
- Set `DEBUG=False` in production
- Use HTTPS in production

## Troubleshooting

- **CKEditor not loading**: Ensure `django-ckeditor` is in INSTALLED_APPS and static files are collected
- **Google Cloud Storage errors**: Verify `GS_BUCKET_NAME` and credentials in environment
- **Static files 404**: Run `python manage.py collectstatic`, check `STATIC_URL` and `STATIC_ROOT`
- **Migration conflicts**: `python manage.py makemigrations --merge`
- **Admin panel issues**: Ensure `django.contrib.admin` is in INSTALLED_APPS
=======
# Profile - Django Blog/CMS Context

Django blog/profile CMS with Google Cloud Storage and CKEditor.

## Architecture
- **Framework**: Django 4.x
- **Language**: Python 3.11+
- **Database**: PostgreSQL
- **Storage**: Google Cloud Storage (media files)
- **Editor**: CKEditor 5
- **Deployment**: Docker + GCP

## Conventions
- PEP 8, type hints everywhere
- Django Class-Based Views
- Templates in `templates/`
- Static files via GCS
- Environment variables in `.env`

## Commands
```bash
# Dev server
pip install -r requirements.txt
python manage.py runserver

# Database
python manage.py migrate
python manage.py makemigrations

# Collect static
python manage.py collectstatic

# Tests
python manage.py test
```

## Important Notes
- GCS credentials in `.env` — never commit
- CKEditor config in `ckeditor/` directory
- Media uploads go to GCS bucket
>>>>>>> 4ae124d (chore: initial local project setup for profile)
