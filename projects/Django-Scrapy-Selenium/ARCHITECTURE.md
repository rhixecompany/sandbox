# Architecture - Django Scrapy Selenium Crawler

## System Overview

A comprehensive web crawling and content management platform built with Django 5.0, Scrapy, and Selenium. This project combines Django's robust web framework with Scrapy's powerful crawling engine and Selenium's browser automation to create a full-featured comic content aggregation and management system.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        Client Layer                              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Web Browser / API Consumer                              │   │
│  │  ┌─────────────┐ ┌─────────────┐ ┌───────────────────┐  │   │
│  │  │  Django     │ │  REST API   │ │  Admin Interface  │  │   │
│  │  │  Templates  │ │  (DRF)      │ │  (Django Admin)   │  │   │
│  │  └─────────────┘ └─────────────┘ └───────────────────┘  │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     Application Layer                            │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Django Project (config/)                                │   │
│  │  ┌─────────────┐ ┌─────────────┐ ┌───────────────────┐  │   │
│  │  │  api/       │ │  crawler/   │ │  fixtures/        │  │   │
│  │  │  (Django    │ │  (Scrapy    │ │  (Test data)      │  │   │
│  │  │   Apps)     │ │   Spiders)  │ │                   │  │   │
│  │  └─────────────┘ └─────────────┘ └───────────────────┘  │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Crawling Layer                              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Scrapy + Selenium Integration                           │   │
│  │  ┌─────────────┐ ┌─────────────┐ ┌───────────────────┐  │   │
│  │  │  Scrapy     │ │  Selenium   │ │  sel.py           │  │   │
│  │  │  Spiders    │ │  (Browser)  │ │  (Direct Selenium)│  │   │
│  │  └─────────────┘ └─────────────┘ └───────────────────┘  │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                        Data Layer                                │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │  PostgreSQL  │  │  SQLite      │  │  JSON Files          │  │
│  │  (Primary)   │  │  (api.sqlite3)│ │  (comics, chapters) │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## Key Technical Decisions

1. **Cookiecutter Django Template** - Built on the industry-standard cookiecutter-django template with Tailwind CSS v5 integration, providing production-ready configuration out of the box.

2. **Scrapy + Selenium Hybrid** - Scrapy handles efficient HTTP crawling while Selenium manages JavaScript-rendered pages and dynamic content that Scrapy cannot access.

3. **Docker-First Deployment** - Docker Compose configurations for both local development and production with Traefik reverse proxy and Let's Encrypt SSL.

4. **Celery Task Queue** - Asynchronous task processing for long-running crawl jobs, email sending, and background data processing.

5. **Multi-Environment Settings** - Separate configuration for local, production, and test environments via django-environ.

6. **Ruff Linting** - Modern Python linting with Ruff for fast code quality checks.

## Component Relationships

| Component | Responsibility | Dependencies |
|-----------|---------------|--------------|
| `config/` | Django settings, URLs, Celery config | django-environ, celery |
| `api/` | Django applications (models, views, API) | Django, DRF, PostgreSQL |
| `crawler/` | Scrapy spiders and crawling logic | Scrapy, Selenium |
| `compose/` | Docker Compose configurations | Docker, Traefik |
| `tests/` | Test suite | pytest, coverage |
| `fixtures/` | Test data fixtures | Django fixtures |
| `webpack/` | Frontend asset bundling | Webpack, Tailwind CSS |
| `locale/` | Internationalization files | Django i18n |

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| django | 5.0 | Web framework |
| scrapy | Latest | Web crawling framework |
| selenium | Latest | Browser automation |
| celery | Latest | Async task queue |
| psycopg2 | Latest | PostgreSQL adapter |
| django-environ | Latest | Environment configuration |
| django-allauth | Latest | Authentication |
| djangorestframework | Latest | REST API |
| ruff | Latest | Python linter |
| tailwindcss | 5.1.3 | CSS framework |
| gunicorn | Latest | Production WSGI server |
| traefik | Latest | Reverse proxy (Docker) |

## Data Flow

1. **Crawl Initiation**: Admin triggers crawl via Django admin or Celery beat schedule
2. **Scrapy Spider**: Spider navigates to target website, extracts structured data
3. **Selenium Fallback**: For JS-rendered content, Selenium browser extracts dynamic data
4. **Data Pipeline**: Extracted items flow through Scrapy pipelines → Django models → PostgreSQL
5. **API Access**: REST API serves crawled content to frontend or external consumers
6. **Admin Management**: Django admin provides UI for managing crawled content and users

## Deployment Considerations

### Production Stack
- **Web Server**: Gunicorn with Django ASGI/WSGI
- **Reverse Proxy**: Traefik with automatic Let's Encrypt SSL
- **Database**: PostgreSQL 12-16 (configurable version)
- **Task Queue**: Celery workers + Redis/RabbitMQ broker
- **Email**: Mailgun, Amazon SES, or configurable provider
- **Storage**: Amazon S3, Google Cloud Storage, Azure, or Whitenoise

### Docker Services
- **Django**: Web application container
- **PostgreSQL**: Database container
- **Celery**: Background task worker
- **Traefik**: Reverse proxy and SSL termination
- **Mailpit**: Local email testing (development)

### Environment Variables
- `DATABASE_URL` - PostgreSQL connection string
- `DJANGO_SECRET_KEY` - Django secret key
- `CELERY_BROKER_URL` - Celery message broker URL
- `EMAIL_*` - Email service credentials
- `AWS_*` / `GOOGLE_*` / `AZURE_*` - Cloud storage credentials

### Important Notes
- `geckodriver.exe` should be downloaded at runtime, not committed
- `api.sqlite3`, `chapters.json`, `comics.json` should be in `.gitignore`
- Celery requires running from the `api/` directory for proper imports
