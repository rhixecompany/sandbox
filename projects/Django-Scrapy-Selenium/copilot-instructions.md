# Django-Scrapy-Selenium — Scraping Platform

**Naming**: `snake_case` for Python files/variables/functions; `PascalCase` for Django models/classes; `UPPER_SNAKE_CASE` for settings/constants; camelCase for JavaScript; `kebab-case` for JS files.

**Patterns**: Django MTV architecture with DRF API; Scrapy spiders with items/pipelines/middlewares; Selenium WebDriver with explicit waits (never `time.sleep()`); stale element re-try with retry wrapper; Celery async task queue for long-running scrapes; `driver.quit()` in `finally` block always; WebSocket for live updates.

**Structure**: Django project with `config/` settings; Django apps for each domain; `scrapy_spiders/` for Scrapy spider definitions; `selenium_scrapers/` for Selenium scripts; `celery_tasks/` for async workers; `templates/` (Tailwind dashboard).

**Python**: Python 3.10+; Django 4.x; DRF (Django REST Framework); Scrapy + Selenium + BeautifulSoup4; Celery + Redis/RabbitMQ; pytest for testing; Black formatter; ruff linter.

**Database**: PostgreSQL (production); SQLite (development); Django ORM for models.

**Scraping**: Respect `robots.txt`; rate limiting with delays; rotate user-agents; sanitize scraped data before storage/display; Scrapy items define data contracts; Selenium uses `WebDriverWait` with expected conditions; retry on `StaleElementReferenceException`.

**JS/Frontend**: Vanilla ES6+; Prettier formatting; Webpack for bundling; Tailwind CSS for styling.

**Security**: No `.env` in VCS; sanitize all scraped output; rate limit all external requests; respect website terms of service; credentials via environment variables only.

**Commands**: `pip install -r requirements.txt && npm install` (setup); `python manage.py migrate && python manage.py runserver` (dev); `celery -A config worker -l info` (worker); `scrapy crawl spider_name` (scrape); `node src/scrape.js` (Selenium); `pytest && npm test` (test); `python manage.py collectstatic && gunicorn config.wsgi:application --bind 0.0.0.0:8000` (production); `docker compose up -d` (deploy).
