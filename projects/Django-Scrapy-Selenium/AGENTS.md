# Django-Scrapy-Selenium — Scraping Platform

Django + Scrapy + Selenium + Celery + Tailwind dashboard.

## Stack
- Python 3.10+, Django 4.x, DRF
- Scrapy, Selenium, BeautifulSoup4
- Celery + Redis/RabbitMQ
- PostgreSQL (prod), SQLite (dev)
- Docker Compose, Gunicorn

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

## Notes
- Scraping later consolidated into `projects/rhixecompany-comics`
- Respect `robots.txt`, rate limit, rotate user-agents
- Sanitize scraped data before storing/display
