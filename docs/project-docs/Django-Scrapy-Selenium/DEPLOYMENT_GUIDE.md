# Django-Scrapy-Selenium — Deployment Guide

## Deployment Options

### 1. Docker (Recommended)

```bash
docker-compose -f docker-compose.production.yml build
docker-compose -f docker-compose.production.yml up -d
```

Docker Compose services:
- **Django** with Gunicorn
- **PostgreSQL**
- **Redis**
- **Celery Worker**
- **Nginx** (static/media)
- **Traefik** (SSL, routing)

### 2. Manual Server

```bash
# System dependencies
sudo apt-get install python3.12 python3.12-venv postgresql nginx redis-server chromium-browser

# Set up project
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements/production.txt

# Configure environment
export DJANGO_SETTINGS_MODULE=config.settings.production
export DATABASE_URL=postgres://user:***@localhost:5432/dbname
export CELERY_BROKER_URL=redis://localhost:6379/0

# Run
python manage.py migrate
python manage.py collectstatic --noinput

# Start services
gunicorn config.wsgi:application --bind 0.0.0.0:8000
celery -A config.celery_app worker -l info --detach
celery -A config.celery_app beat -l info --detach
```

### 3. Heroku

```bash
heroku create your-app
heroku addons:create heroku-postgresql
heroku addons:create heroku-redis
heroku buildpacks:add heroku/python
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-chromedriver
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-google-chrome
git push heroku main
```

## Environment Variables

```env
DJANGO_SETTINGS_MODULE=config.settings.production
DJANGO_SECRET_KEY=<gener...n
# Selenium (headless Chrome)
SELENIUM_HEADLESS=true
# Celery
CELERY_BROKER_URL=redis://...
```

## Pre-Deployment Checklist

- [ ] `DEBUG=False` in settings
- [ ] `ALLOWED_HOSTS` configured
- [ ] Database migrations applied
- [ ] Static files collected
- [ ] Celery broker configured (Redis)
- [ ] Selenium configured for headless mode
- [ ] Chrome/Chromium installed on server
- [ ] Scrapy rate limits configured
- [ ] Database backups scheduled
- [ ] Monitoring and logging active
