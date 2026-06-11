# Copilot Instructions

Project-wide guidance for the Django + Scrapy + Selenium platform.

## Source of truth

- `projects/Django-Scrapy-Selenium/AGENTS.md`
- `README.md`
- `backend/`
- `frontend/`

## Commands

Run from the project root:

```bash
python manage.py runserver
python manage.py test
pytest
scrapy crawl spider_name
scrapy check spider_name
celery -A config worker -l info
node src/scrape.js
npm install
npm test
npm run dev
npm run build
```

## Architecture

- Django backend coordinates scraping, APIs, and task orchestration.
- Scrapy spiders and Selenium scripts handle crawl/automation flows.
- Celery workers process async scraping jobs with Redis or RabbitMQ.
- Webpack/Tailwind frontend is a separate dashboard surface.

## Conventions

- Use Django ORM and migrations for backend data changes.
- Follow Scrapy item/pipeline/middleware patterns.
- Use explicit Selenium waits and retry stale elements.
- Respect `robots.txt` and rate limits when scraping.

