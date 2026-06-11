# Django-Scrapy-Selenium Project Documentation

## Overview

A full-stack web scraping platform that automates comic data collection from external sources. Combines Django REST API for data serving, Scrapy for web crawling, Selenium for JavaScript-rendered page handling, and PostgreSQL for persistent storage.

**Repository:** https://github.com/Rhixe-company/Django-Scrapy-Selenium  
**Stack:** Python 3.10+ | Django 4.x | DRF | Scrapy | Selenium | PostgreSQL  
**Status:** Active Development / Maintenance

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      External Sources                         │
│           AsuraComic, MangaDex, Other Comic Sites             │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP Requests
┌──────────────────────▼──────────────────────────────────────┐
│                    Scrapy Crawler                             │
│  ┌────────────┐  ┌─────────────────┐  ┌──────────────────┐  │
│  │  Spiders    │  │  Selenium        │  │  Pipelines       │  │
│  │  asuracomic │──│  Middleware      │──│  CrawlerAppsDb   │  │
│  └────────────┘  │  (JS Rendering)  │  │  (Django ORM)    │  │
│                  └─────────────────┘  └────────┬─────────┘  │
└─────────────────────────────────────────────────┼────────────┘
                                                   │
┌──────────────────────────────────────────────────▼──────────┐
│                    PostgreSQL Database                        │
│  Comic | Chapter | ChapterImage | Genre | Author | Artist   │
│  Bookmark | Comment | Rating | Follow | CrawlLog | ScrapeJob │
└──────────────────────────────────┬──────────────────────────┘
                                   │
┌──────────────────────────────────▼──────────────────────────┐
│                    Django REST API                            │
│  /api/comics/ | /api/chapters/ | /api/genres/               │
│  /api/bookmarks/ | /api/comments/ | /api/ratings/           │
│  /api/auth/ | /api/users/                                    │
└──────────────────────────────────┬──────────────────────────┘
                                   │ JSON Response
┌──────────────────────────────────▼──────────────────────────┐
│                    Frontend Client                            │
│  React SPA, Mobile App, or Third-party Integrations          │
└─────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **Crawl Initiation** — Spider starts from configured seed URLs
2. **Page Rendering** — Selenium middleware intercepts Scrapy requests, renders JS, returns HTML
3. **Data Extraction** — Spider parses HTML using Scrapy selectors, yields structured Items
4. **Pipeline Processing** — Items flow through pipeline, resolved to Django ORM objects
5. **API Serving** — REST endpoints expose crawled data to clients
6. **User Interaction** — Bookmarking, commenting, rating via authenticated API

---

## Setup Guide

### Prerequisites

- Python 3.10+
- PostgreSQL 12+
- Chrome/Chromium browser (for Selenium WebDriver)
- ChromeDriver (matching Chrome version)

### Installation

```bash
# Clone repository
git clone https://github.com/Rhixe-company/Django-Scrapy-Selenium.git
cd Django-Scrapy-Selenium

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install ChromeDriver (if not in PATH)
# Download from https://chromedriver.chromium.org/
```

### Database Setup

```bash
# Create PostgreSQL database
createdb comic_crawler

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# (Optional) Load sample data
python manage.py loaddata fixtures/sample_data.json
```

### Running the Crawler

```bash
# Activate Scrapy project
cd crawler

# Run AsuraComic spider
scrapy crawl asuracomics

# Run with output to JSON
scrapy crawl asuracomics -o output.json

# Run with custom settings
scrapy crawl asuracomics -s DOWNLOAD_DELAY=5.0
```

### Running the API Server

```bash
# Start Django development server
python manage.py runserver

# API available at http://localhost:8000/api/
# Admin at http://localhost:8000/admin/
```

---

## Feature Guide

### Web Crawling

- **AsuraComic Integration** — Primary spider scrapes series listing and individual comic pages
- **JavaScript Rendering** — Selenium middleware handles dynamically loaded content
- **Anti-Bot Measures** — Configurable delays, rotating proxies, user-agent rotation
- **Error Recovery** — Crawl failures logged with source URL for retry
- **Atomic Data** — `get_or_create` pattern prevents duplicate entries

### REST API

- **Comic Endpoints** — Full CRUD with filtering by status, genre, type
- **Chapter Endpoints** — Ordered chapter retrieval with pagination
- **User Authentication** — JWT-based auth with token refresh
- **Bookmark System** — Users can save comics with reading status
- **Comment System** — Chapter-level discussions
- **Rating System** — 1-5 star ratings per comic

### Data Model Features

- **Composite Unique Constraints** — Prevent duplicate chapters and images
- **Gradual Data Collection** — All FKs nullable to allow multi-pass crawling
- **Soft Delete Ready** — Models support future soft-delete implementation
- **Audit Trail** — CrawlLog tracks every scraping session

---

## Scrapy Configuration

### Basic Settings

```python
# settings.py
BOT_NAME = 'crawler'
ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 3.0
COOKIES_ENABLED = False

# Middleware
DOWNLOADER_MIDDLEWARES = {
    'crawler.middlewares.sele.NewSeleniumMiddleware': 543,
}

# Pipeline
ITEM_PIPELINES = {
    'crawler.pipelines.appsdb.CrawlerAppsDbPipeline': 300,
}
```

### Proxy Configuration

```python
ROTATING_PROXY_LIST = [
    'proxy1.example.com:8080',
    'proxy2.example.com:8080',
]
```

---

## Testing

```bash
# Run Django tests
python manage.py test

# Run with coverage
coverage run --source='api,crawler' manage.py test
coverage report

# Test specific app
python manage.py test api.tests.test_models
python manage.py test api.tests.test_api
```

### Test Coverage Focus
- Model validation and constraints
- API endpoint behavior (auth, CRUD, permissions)
- Pipeline item processing
- Spider parsing logic (using cached HTML fixtures)

---

## Deployment

### Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Install Chrome for Selenium
RUN apt-get update && apt-get install -y chromium chromium-driver
CMD ["gunicorn", "api.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### Production Considerations

- Set `DEBUG=False` and configure `ALLOWED_HOSTS`
- Use PostgreSQL in production (not SQLite)
- Configure proper secret key via environment variable
- Set up database connection pooling (PgBouncer)
- Schedule crawls via Celery or cron
- Monitor Selenium memory usage — restart Chrome periodically
- Use ASGI server (Uvicorn) for async API performance
