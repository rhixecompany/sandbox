# Django-Scrapy-Selenium — Scraping Platform

## Architecture
- **Type:** Django-based scraping platform with multiple scraping engines
- **Pattern:** Django monolith with Scrapy spiders + Selenium automation + Celery async tasks
- **Reference:** [Workflow Analysis](docs/Project_Architecture/Workflow_Analysis.md), [Exemplars](docs/Project_Architecture/exemplars.md)

Django + Scrapy + Selenium + Celery + Tailwind dashboard. Combines multiple scraping approaches (Scrapy spiders, Selenium browser automation, Node.js scripts) orchestrated via Celery.

## Stack
- **Backend:** Python 3.10+, Django 4.x, Django REST Framework
- **Scraping:** Scrapy, Selenium, BeautifulSoup4
- **Async:** Celery + Redis/RabbitMQ
- **Database:** PostgreSQL (prod), SQLite (dev)
- **Infra:** Docker Compose, Gunicorn

## Commands
```bash
pip install -r requirements.txt && npm install
python manage.py migrate && python manage.py runserver
celery -A config worker -l info
scrapy crawl spider_name
node src/scrape.js
pytest && npm test
```

## Production
```bash
python manage.py collectstatic
gunicorn config.wsgi:application --bind 0.0.0.0:8000
docker compose up -d
npm run build
```

## Conventions
- Scraping logic consolidated into `projects/rhixecompany-comics` for newer work
- Respect `robots.txt`, rate limit requests, rotate user-agents
- Sanitize scraped data before storing or displaying
- Celery tasks in dedicated `tasks.py` per app
- Separate settings per environment

## Notes
- Legacy project — newer scraping work moved to `rhixecompany-comics`
- Node.js scraping via `src/scrape.js` (Selenium-based)
- Redis required for Celery broker
