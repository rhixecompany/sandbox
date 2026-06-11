# Copilot Instructions — Django-Scrapy-Selenium

## Python Code Style
- Django coding conventions, PEP 8
- Black formatter
- Scrapy: items, pipelines, middlewares pattern
- Selenium: explicit waits, never time.sleep()

## JavaScript
- ES6+ with Prettier formatting
- Webpack for asset bundling

## Security
- Never commit .env files
- Respect robots.txt
- Rate limiting on scrapers
- Sanitize scraped data before storing

## Commands
- `python manage.py runserver` - Dev server
- `celery -A config worker -l info` - Worker
- `scrapy crawl spider_name` - Run spider
