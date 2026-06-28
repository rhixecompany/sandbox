# Django-Scrapy-Selenium — Architecture

## Overview
A full-stack web scraping platform combining Django backend with Scrapy spiders and Selenium browser automation. Uses Celery for async task processing with a Tailwind-styled dashboard.

## Architecture Pattern
- **Type:** Full-stack Web Application with Task Queue
- **Pattern:** Django monolithic + Celery workers
- **Database:** PostgreSQL (production), SQLite (development)

## Components
- **`config/`** — Django project configuration (settings, URLs, WSGI)
- **`api/`** — Django REST Framework API endpoints
- **`crawler/`** — Scrapy spider definitions and pipelines
- **`compose/`** — Docker Compose configurations
- **`webpack/`** — Frontend asset bundling
- **`fixtures/`** — Database fixtures
- **`requirements/`** — Split requirement files (base, local, production)

## Cross-Cutting Concerns
- **Task Queue:** Celery + Redis/RabbitMQ for async scraping
- **Frontend:** Tailwind CSS via Webpack
- **Containerization:** Docker Compose for local and production
- **Deployment:** Gunicorn WSGI, Heroku-ready (Procfile, runtime.txt)

## Data Flow
1. User submits scraping request via Django dashboard
2. Celery task queues the Scrapy spider or Selenium script
3. Scraped data processed through item pipelines
4. Results stored in PostgreSQL, displayed via Django views
