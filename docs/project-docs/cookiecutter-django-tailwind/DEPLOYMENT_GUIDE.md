# Cookiecutter Django Tailwind — Deployment Guide

## Deployment Options for Generated Projects

### 1. Docker + Traefik (Recommended for Production)

```bash
cd your-project/
docker-compose -f docker-compose.production.yml build
docker-compose -f docker-compose.production.yml up -d
```

Production Docker setup includes:
- Django with Gunicorn
- PostgreSQL
- Nginx for static/media files
- Traefik with Let's Encrypt SSL
- Celery worker + beat + Flower (optional)
- Redis (optional)

### 2. Heroku

Configured for Heroku deployment:

```bash
heroku create your-app-name
heroku addons:create heroku-postgresql
heroku config:set DJANGO_SETTINGS_MODULE=config.settings.production
git push heroku main
```

### 3. PythonAnywhere

See detailed guide in generated project's `docs/deployment-on-pythonanywhere.rst`.

### 4. Manual Server (Ubuntu/Debian)

```bash
# Install dependencies
sudo apt-get install python3.12 python3.12-venv postgresql nginx

# Set up project
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements/production.txt

# Configure
cp .envs/.production/.django.example .envs/.production/.django
cp .envs/.production/.postgres.example .envs/.production/.postgres

# Run migrations
python manage.py migrate
python manage.py collectstatic

# Run with Gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

## Production Environment Variables

```env
DJANGO_SETTINGS_MODULE=config.settings.production
DJANGO_SECRET_KEY=<generated_key>
DATABASE_URL=postgres://user:***@production-host:5432/mydb
DJANGO_ADMIN_URL=admin/
DJANGO_ALLOWED_HOSTS=.yourdomain.com
REDIS_URL=redis://:password@redis-host:6379/0

# Email
MAILGUN_API_KEY=...
DJANGO_SERVER_EMAIL=...
DJANGO_DEFAULT_FROM_EMAIL=...

# Storage (if using cloud)
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_STORAGE_BUCKET_NAME=...
```

## Pre-Deployment Checklist

- [ ] `SECRET_KEY` set to a unique, random value
- [ ] `DEBUG=False`
- [ ] `ALLOWED_HOSTS` configured
- [ ] Database migrations applied
- [ ] Static files collected
- [ ] SSL certificate configured (Let's Encrypt)
- [ ] Email service configured
- [ ] Sentry DSN set (if enabled)
- [ ] Celery broker configured (if enabled)
- [ ] Database backups scheduled
- [ ] Monitoring tools active

## CI/CD

GitHub Actions (`ci.yml`) runs on push/PR:
1. Lint (Ruff)
2. Type check (mypy)
3. Test (pytest)
4. Build Docker images
5. Deploy (on main branch)
