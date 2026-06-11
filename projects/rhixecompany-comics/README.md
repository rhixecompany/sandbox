# Rhixecompany Comics

Comic book and graphic novel platform — discover, read, and track comics across multiple sources.

## Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.11+, Django 5.x, DRF, Celery, PostgreSQL |
| Frontend | Next.js 16 (App Router), TypeScript, Tailwind CSS, shadcn/ui |
| Scraping | Scrapy, Selenium WebDriver |
| Infrastructure | Docker Compose |

## Quick Start

```bash
# Full stack
docker compose up -d

# Or individually:
cd backend && pip install -r requirements.txt && python manage.py runserver
cd frontend && npm install && npm run dev
```

## Repo Origins

Consolidated patterns from:
- `projects/comicwise` — Next.js comic streaming
- `projects/Django-Scrapy-Selenium` — Django scraping platform
- `projects/selenium_webdriver` — Browser automation

## License

MIT
