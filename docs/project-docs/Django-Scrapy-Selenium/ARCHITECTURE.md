# Architecture — Django-Scrapy-Selenium

## Overview
A full-stack web scraping platform combining Django backend, Scrapy for crawling, Selenium for browser automation, and Celery for async processing.

## Architecture Layers

### 1. Django Backend
- Django REST Framework for API endpoints
- Admin interface for managing spiders and scraped data
- Authentication via DRF permissions

### 2. Scraping Engine
- **Scrapy**: Configurable spiders with pipelines and middlewares
- **Selenium**: Chrome WebDriver for JavaScript-rendered pages
- **BeautifulSoup**: HTML parsing fallback

### 3. Task Queue (Celery)
- Async execution of scraping tasks
- Redis/RabbitMQ as message broker
- Task scheduling and retry logic

### 4. Frontend Dashboard
- Tailwind CSS dashboard for monitoring
- Webpack-bundled assets
- Alpine.js for interactive UI components

## Data Flow
```
User → Django Admin/API → Celery Task → Scrapy Spider → Target Website
                                  ↓                       ↓
                              Selenium ←→ JS-heavy pages   ↓
                                  ↓                       ↓
                            PostgreSQL ←───────────────────┘
```
