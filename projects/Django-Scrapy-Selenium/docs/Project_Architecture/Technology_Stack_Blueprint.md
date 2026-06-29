# Technology Stack Blueprint

## Project: Django-Scrapy-Selenium — Scraping Platform

> **Generated:** 2026-06-25  
> **Generator:** technology-stack-blueprint-generator  
> **Analysis Depth:** Comprehensive

---

## Overview

A comprehensive web scraping platform combining Django (admin/dashboard), Scrapy (spiders), Selenium (dynamic content), and Celery (async task processing). Features a Tailwind-styled dashboard for managing scraping operations.

**Project Type:** Web Scraping Platform  
**Stack Type:** Django

---

## Technology Stack

### Languages & Runtimes

| Technology | Version | Usage |
|---|---|---|
| Python | ^3.10 / 3.12 | Primary backend language |
| Django | ^4.x | Web framework & admin |
| TypeScript | ^5.4.5 | Frontend scripting |
| Node.js | 22.13 | JavaScript runtime |
| HTML/CSS | — | Templates & styling |

### Backend Dependencies

| Category | Technologies |
|---|---|
| **Web Framework** | Django 4.x |
| **API Framework** | Django REST Framework |
| **Scraping** | Scrapy, Selenium, BeautifulSoup4 |
| **Async Tasks** | Celery + Redis/RabbitMQ |
| **Database** | PostgreSQL (prod), SQLite (dev) |
| **Serving** | Gunicorn |
| **Testing** | pytest, django-coverage-plugin |
| **Linting** | ruff, mypy (Python 3.12), djlint |
| **Formatting** | Black (line-length 119), isort |

### Frontend Dependencies

| Category | Technologies |
|---|---|
| **Build Tool** | Webpack 5 (dev/prod config) |
| **CSS Framework** | Tailwind CSS 3, daisyui, flowbite |
| **JavaScript** | Alpine.js, htmx, hyperscript, jQuery, Select2 |
| **UI Components** | SweetAlert2, SortableJS, highlight.js |
| **Icons** | Font Awesome |
| **Preprocessors** | Sass, PostCSS (preset-env, nesting, imports) |
| **Babel** | ES6+ transpilation |

---

## Licensing

| Component | License |
|---|---|
| Django-Scrapy-Selenium | (not specified) |

---

## Project Structure

```
Django-Scrapy-Selenium/
├── config/                # Django project configuration
│   └── settings/
│       ├── base.py
│       ├── local.py
│       ├── production.py
│       └── test.py
├── api/                   # Django apps
├── src/
│   ├── spiders/           # Scrapy spiders
│   └── scrape.js          # Selenium/Node.js scraper
├── templates/             # Django templates (Tailwind)
├── static/                # Static assets
├── webpack/               # Webpack configs
│   ├── dev.config.js
│   └── prod.config.js
├── requirements.txt
└── package.json
```

---

## Key Scripts

| Command | Description |
|---|---|
| `python manage.py runserver` | Django dev server |
| `celery -A config worker -l info` | Celery worker |
| `scrapy crawl spider_name` | Run a Scrapy spider |
| `node src/scrape.js` | Run Selenium scraper |
| `pytest` | Run Python tests |
| `npm run build` | Webpack production build |
| `npm run dev` | Webpack dev server |

---

## Coding Conventions

- **Python 3.10+**: Modern Python features
- **ruff + mypy**: Strict linting and type checking (target: Python 3.12)
- **Black formatting**: 119 character line limit
- **PEP 8**: Standard Python conventions
- **djlint**: Django template linting (profile: django)

---

## Architecture Diagram

```
┌──────────────────────────────────────────────────────────┐
│              Django-Scrapy-Selenium Platform              │
├──────────────────────────────────────────────────────────┤
│  Django Web Layer                                        │
│  ├── Admin Dashboard (Tailwind UI)                       │
│  ├── REST API (DRF)                                      │
│  └── Authentication                                      │
├──────────────────────────────────────────────────────────┤
│  Scraping Layer                                          │
│  ├── Scrapy Spiders (static content)                     │
│  ├── Selenium WebDriver (dynamic content)                │
│  └── BeautifulSoup4 (parsing)                            │
├──────────────────────────────────────────────────────────┤
│  Async Processing                                        │
│  └── Celery + Redis/RabbitMQ                             │
├──────────────────────────────────────────────────────────┤
│  Frontend                                                │
│  ├── Tailwind 3 + daisyui + Flowbite                    │
│  ├── Alpine.js + htmx                                   │
│  ├── Webpack 5 build pipeline                           │
│  └── jQuery, Select2, SweetAlert2                       │
├──────────────────────────────────────────────────────────┤
│  Infrastructure                                          │
│  ├── PostgreSQL / SQLite                                 │
│  ├── Gunicorn                                            │
│  └── Docker Compose                                     │
└──────────────────────────────────────────────────────────┘
```

---

## Notes

- Scraping functionality later consolidated into `projects/rhixecompany-comics`
- Respects `robots.txt`, rate limiting, and user-agent rotation
- Scraped data sanitized before storage
- Webpack 5 with extensive PostCSS plugin chain for styles
