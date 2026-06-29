# Django-Scrapy-Selenium — Web Scraping Platform

> **Stack:** Django 4.x + Scrapy + Selenium + Celery | **Type:** Web Scraping Platform | **Status:** Active

A comprehensive web scraping platform combining Django (admin/dashboard), Scrapy (spiders), Selenium (dynamic content), and Celery (async task processing). Features a Tailwind-styled dashboard for managing scraping operations.

---

## Technology Stack

### Backend

| Category | Technology |
|---|---|
| **Web Framework** | Django 4.x |
| **API Framework** | Django REST Framework (DRF) |
| **Language** | Python 3.10+ / 3.12 |
| **Scraping** | Scrapy, Selenium, BeautifulSoup4 |
| **Async Tasks** | Celery + Redis/RabbitMQ |
| **Database** | PostgreSQL (prod), SQLite (dev) |
| **Serving** | Gunicorn |

### Frontend

| Category | Technology |
|---|---|
| **Build Tool** | Webpack 5 (dev/prod config) |
| **CSS Framework** | Tailwind CSS 3, daisyui, flowbite |
| **JavaScript** | Alpine.js, htmx, hyperscript, jQuery |
| **UI Components** | SweetAlert2, SortableJS, highlight.js |
| **Icons** | Font Awesome |
| **Language** | TypeScript ^5.4.5 |

## Architecture

The platform follows an **ETL Pipeline Pattern** with dual scraping engines:

```
User Request → Django Views/REST API
                    ↓
              URL Router
                    ↓
        ┌───────────┴───────────┐
        ↓                       ↓
    Scrapy Spider          Selenium Driver
        ↓                       ↓
    BeautifulSoup          DOM Parsing
        ↓                       ↓
        └───────────┬───────────┘
                    ↓
            Django ORM Models
                    ↓
            PostgreSQL Database
                    ↓
          ┌─────────┴─────────┐
          ↓                   ↓
    Tailwind Dashboard    REST API (DRF)
```

## Project Structure

```
Django-Scrapy-Selenium/
├── config/                    # Django project configuration
│   └── settings/
├── api/                       # Django REST API apps
│   ├── apps/
│   ├── home/
│   └── contrib/
├── crawler/                   # Scrapy spider definitions
│   └── spiders/
├── src/                       # Frontend source (Node.js)
│   ├── scrape.js              # Selenium scraper entry
│   └── sass/
├── templates/                 # Django templates (Tailwind)
├── static/                    # Static assets
├── webpack/                   # Webpack configurations
│   ├── dev.config.js
│   └── prod.config.js
├── compose/                   # Docker Compose variants
├── requirements/
└── docs/Project_Architecture/
```

## Getting Started

```bash
# Prerequisites: Python 3.10+, Node.js, Redis/RabbitMQ

# Backend setup
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend setup
npm install
npm run dev            # Webpack dev server

# Start Celery worker
celery -A config worker -l info

# Run a Scrapy spider
scrapy crawl spider_name

# Run Selenium scraper
node src/scrape.js

# Run tests
pytest
npm test
```

## Key Features

- **Dual Scraping Engines** — Scrapy for static content, Selenium for JavaScript-heavy sites
- **Async Task Processing** — Celery workers handle long-running scraping tasks
- **Tailwind Dashboard** — Modern UI for managing scraping operations
- **REST API** — DRF-powered API for scraped data access
- **Docker Support** — Multi-environment Docker Compose
- **Quality Tooling** — pytest, ruff, mypy, Black, djlint

## Development Workflow

```bash
# Backend
python manage.py runserver
python manage.py test

# Frontend
npm run dev           # Development build with watcher
npm run build         # Production build

# Scraping
celery -A config worker -l info
scrapy crawl spider_name
node src/scrape.js
```

## Coding Standards

### Python
- **PEP 8**: Python style guide
- **Black formatting**: 119 character line limit
- **ruff + mypy**: Strict linting and type checking
- **Django best practices**: Standard Django/DRF conventions

### Frontend
- **ES6+**: Modern JavaScript
- **Prettier**: Code formatting
- **Webpack**: Module bundling

## Production

```bash
# Collect static files
python manage.py collectstatic

# Start Gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000

# Start Docker services
docker compose up -d

# Build frontend
npm run build
```

## Security

- No secrets in VCS (`.env` never committed)
- Respect `robots.txt`
- Rate limit scrapers
- Sanitize scraped data before storage/display
- User-agent rotation

## Notes

Scraping functionality later consolidated into `projects/rhixecompany-comics`.

## License

Not specified.
