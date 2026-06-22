# Django-Scrapy-Selenium — Setup Guide

## Prerequisites

- **Python** 3.12+
- **Node.js** 22.13+
- **PostgreSQL** 14+
- **Redis** (for Celery)
- **Chrome/Chromium** (for Selenium)

## 1. Backend Setup

```bash
git clone <repo-url>
cd api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements/local.txt
```

## 2. Database Setup

```bash
createdb django_scraping

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

## 3. Environment Variables

```bash
cp .envs/.local/.django.example .envs/.local/.django
cp .envs/.local/.postgres.example .envs/.local/.postgres
```

Required variables in `.envs/.local/.django`:

```env
USE_DOCKER=no
DATABASE_URL=postgres://user:***@localhost:5432/django_scraping
CELERY_BROKER_URL=redis://localhost:6379/0
DJANGO_SECRET_KEY=your-development-secret-key
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_DEBUG=true
```

## 4. Frontend Setup

```bash
# Install Node dependencies
npm install

# Development build with watch
npm run dev

# Production build
npm run build
```

## 5. Start Services

```bash
# Terminal 1: Django development server
python manage.py runserver

# Terminal 2: Celery worker
celery -A config.celery_app worker -l info

# Terminal 3: Frontend (if developing CSS/JS)
npm run dev
```

## 6. Test Scraping

```bash
# Run a Scrapy spider
scrapy crawl comic_spider

# Test Selenium scraper
python manage.py shell
>>> from selenium_scraper.scraper import SeleniumScraper
>>> scraper = SeleniumScraper()
>>> result = scraper.scrape_page("https://example.com")
```

## 7. Verify Installation

```bash
# Django checks
python manage.py check

# Run tests
pytest

# Frontend build
npm run build
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: psycopg2` | Install PostgreSQL dev libraries |
| Selenium fails | Install ChromeDriver matching Chrome version |
| Celery won't connect | Ensure Redis is running: `redis-server` |
| Webpack build fails | `npm install` and check Node version ≥ 22 |
| Database connection error | Verify PostgreSQL running and DATABASE_URL correct |
