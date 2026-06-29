# Architecture Blueprint: Django-Scrapy-Selenium

**Generated:** 2026-06-29  
**Generator:** architecture-blueprint-generator  

---

## 1. Architecture Detection and Analysis

### Technology Stack

| Category | Technology |
|---|---|
| **Framework** | Django 5.0, Django REST Framework |
| **Web Scraping** | Scrapy, Selenium WebDriver, BeautifulSoup4 |
| **Task Queue** | Celery + Redis/RabbitMQ |
| **Frontend** | Webpack, Tailwind CSS |
| **Database** | PostgreSQL (prod), SQLite (dev) |
| **Language** | Python 3.10+ |
| **Infrastructure** | Gunicorn, Docker Compose |
| **CI/CD** | GitHub Actions |

### Architectural Pattern Detected

**Pattern:** Layered Architecture with Task Queue  

The project integrates three distinct subsystems:
1. **Django Application Layer**: Web UI, REST API, admin interface
2. **Scraping Layer**: Scrapy spiders + Selenium browser automation
3. **Async Processing Layer**: Celery workers for background tasks

---

## 2. Architectural Overview

### System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                        Client Layer                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  Templates  │  │  REST API   │  │  Admin Interface    │  │
│  │  (Django)   │  │  (DRF)      │  │  (Django Admin)     │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                     Application Layer                         │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │  config/     │  │  api/        │  │  crawler/         │  │
│  │  (Django     │  │  (Django     │  │  (Scrapy          │  │
│  │   settings)  │  │   Apps)      │  │   Spiders)        │  │
│  └──────────────┘  └──────────────┘  └───────────────────┘  │
└──────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                      Crawling Layer                           │
│  ┌──────────────────┐  ┌──────────────────────────────────┐  │
│  │  Scrapy Spiders  │  │  Selenium WebDriver (Browser)    │  │
│  └──────────────────┘  └──────────────────────────────────┘  │
│  ┌──────────────────┐                                       │
│  │  Celery Workers  │                                       │
│  └──────────────────┘                                       │
└──────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                        Data Layer                             │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │  PostgreSQL  │  │  SQLite      │  │  JSON Files       │  │
│  └──────────────┘  └──────────────┘  └───────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

---

## 3. Key Architectural Decisions

| Decision | Rationale |
|---|---|
| Django + Scrapy + Selenium | Comprehensive scraping with web framework support |
| Celery for async tasks | Non-blocking scraping operations |
| DRF for API | Standardized REST endpoints for frontend/consumers |
| Docker Compose | Consistent multi-service environment |

---

## 4. Data Flow

### Scraping Flow
```
User Request → Celery Worker → Scrapy Spider → External Website
                                                   ↓
                                            Extract Data
                                                   ↓
                                     Selenium (if JS needed)
                                                   ↓
                                            Django ORM → Database
```

### API Flow
```
Client → DRF ViewSet → Serializer → Django ORM → Database
```

---

## 5. Implementation Patterns

### Scrapy Spider Pattern
```python
class ComicSpider(scrapy.Spider):
    name = 'comic_spider'
    start_urls = ['https://example.com/comics']
    
    def parse(self, response):
        # Extract data, yield items or follow links
        pass
```

### Celery Task Pattern
```python
@app.task
def run_scraping_task(spider_name):
    execute(f'scrapy crawl {spider_name}')
```

---

## 6. Extensibility Points

1. **New spiders**: Add Scrapy spiders under `crawler/` directory
2. **New API endpoints**: Add DRF ViewSets under `api/`
3. **Additional scraped sites**: New parser modules following existing patterns
4. **Data export formats**: Add new serializers or pipelines

---

*End of architecture blueprint.*
