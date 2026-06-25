# AGENTS.md

> **Refreshed by AGENTS workflow 2026-06-01**

## Project Overview

A full-stack web scraping platform combining Django backend with modern JavaScript frontend tooling. Provides Scrapy spider management, Selenium-based browser automation, and Celery task queue processing with a Tailwind-styled dashboard.

**Tech Stack:**
- **Backend**: Python 3.10+, Django 4.x, Django REST Framework
- **Scraping**: Scrapy, Selenium WebDriver, BeautifulSoup4
- **Task Queue**: Celery + Redis/RabbitMQ
- **Frontend**: Webpack with Tailwind CSS (pre-Next.js era)
- **Database**: PostgreSQL (production), SQLite (dev)
- **Infrastructure**: Gunicorn, Docker Compose, WSGI/ASGI

> Note: This project's scraping capabilities were later consolidated into `projects/rhixecompany-comics`.

<<<<<<< HEAD
=======
## Hermes and Copilot

- Use the nearest `AGENTS.md` for files under `projects/Django-Scrapy-Selenium/`;
  this file is the local fallback.
- `projects/Django-Scrapy-Selenium/.github/copilot-instructions.md` is the
  primary Copilot guidance file for this project.
- Root Hermes orchestration assets live in `../../.github/agents/hermes.agent.md`
  and `../../.github/prompts/`.
- Keep this file, the local Copilot instructions, and the project README in
  sync when scraping, task, or frontend workflows change.

>>>>>>> 50eadb6 (chore: initial local project setup for Django-Scrapy-Selenium)
## Setup Commands

```bash
# Backend setup
cd backend  # or project root
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Frontend setup
npm install

# Database
python manage.py migrate
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

## Development Workflow

```bash
# Start Django dev server
python manage.py runserver

# Start Celery worker (for async scraping tasks)
celery -A config worker -l info

# Build frontend assets
npm run dev

# Run a Scrapy spider
scrapy crawl spider_name

# Run Selenium script
node src/scrape.js
```

## Testing Instructions

```bash
# Django tests
python manage.py test

# pytest (if configured)
pytest

# Scrapy contract tests
scrapy check spider_name

# Frontend tests
npm test
```

## Code Style

- **Python**: Django coding conventions, PEP 8, Black formatter
- **Scrapy**: Follow Scrapy spider conventions (items, pipelines, middlewares, settings)
- **Selenium**: Use explicit waits, avoid time.sleep(), handle stale elements
- **JavaScript**: Standard ES6+ with Prettier formatting
- **CSS**: Tailwind CSS utility classes
- **Database**: Django ORM for queries, migrations for schema changes

## Build/Deployment

```bash
# Collect static files
python manage.py collectstatic

# Gunicorn production server
gunicorn config.wsgi:application --bind 0.0.0.0:8000

# Docker deployment
docker compose up -d

# Build frontend for production
npm run build
```

Deploy via Docker Compose (Django + PostgreSQL + Redis + Celery) or PaaS.

## Security

- Never commit `.env` or secrets files
- Django `SECRET_KEY` must be in environment, never in code
- Scraping: respect `robots.txt`, implement rate limiting, rotate user-agents
- Sanitize scraped data before storing or displaying
- Use Django's CSRF, XSS, and SQL injection protections
- Restrict API endpoints with DRF permissions

## Troubleshooting

- **Celery tasks not executing**: Verify Redis/RabbitMQ is running, check worker logs
- **Scrapy spider returns empty**: Check target site structure changes, update selectors
- **Selenium WebDriver issues**: Ensure Chrome/Chromium is installed, check driver version compatibility
- **Database migration fails**: `python manage.py migrate --run-syncdb`
- **Static files 404**: Run `python manage.py collectstatic` and verify `STATIC_ROOT` path
- **Docker networking**: Ensure services are on the same Docker network
