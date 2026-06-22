# Project Workflow — Django-Scrapy-Selenium

## Development Workflow

```bash
# Backend Setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser

# Start Services
python manage.py runserver          # Django dev server
celery -A config worker -l info     # Celery worker
npm run dev                         # Frontend assets

# Run Scrapers
scrapy crawl spider_name            # Run a spider
node selenium_scripts/scrape.js     # Run Selenium script

# Testing
python manage.py test               # Django tests
pytest                              # pytest tests
npm test                            # Frontend tests
```

## Deployment
```bash
python manage.py collectstatic
gunicorn config.wsgi:application --bind 0.0.0.0:8000
docker compose up -d
```
