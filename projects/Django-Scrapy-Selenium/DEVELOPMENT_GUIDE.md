# Django-Scrapy-Selenium — Development Guide

## Development Workflow

### Daily Commands

```bash
python manage.py runserver       # Django dev server
npm run dev                      # Webpack dev server (frontend)
celery -A config.celery_app worker -l info  # Celery worker
```

### Before Committing

```bash
# Lint Python
ruff check .
black .

# Lint JavaScript
eslint static/js/

# Type check
mypy api/

# Run tests
pytest

# Build frontend
npm run build
```

## Scrapy Development

### Adding a New Spider

```python
# scraping/spiders/new_spider.py
import scrapy

class NewSpider(scrapy.Spider):
    name = "new_spider"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com/comics"]

    def parse(self, response):
        for comic in response.css(".comic-item"):
            yield {
                "title": comic.css("h2::text").get(),
                "url": comic.css("a::attr(href)").get(),
            }

        next_page = response.css(".next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
```

### Running Spiders

```bash
scrapy list                           # Show all spiders
scrapy crawl comic_spider             # Run spider
scrapy crawl comic_spider -o data.json  # Export to JSON
scrapy crawl comic_spider -s LOG_LEVEL=ERROR  # Quiet mode
```

### Scrapy Pipeline

```python
# scraping/pipelines.py
class DatabasePipeline:
    def process_item(self, item, spider):
        # Save to Django ORM
        Comic.objects.update_or_create(
            url=item["url"],
            defaults={**item}
        )
        return item
```

## Selenium Development

### Using the Selenium Scraper

```python
from selenium_scraper.scraper import SeleniumScraper

scraper = SeleniumScraper()

# Scrape a JS-rendered page
data = scraper.scrape_page("https://example.com/dynamic-page")

# Wait for specific element
data = scraper.scrape_page(
    url="https://example.com",
    wait_for=".comic-list",
    timeout=10
)
```

### WebDriver Configuration

```python
# selenium_scraper/drivers.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(options=options)
```

## Frontend Development

### Alpine.js Components

```html
<div x-data="{ open: false }">
    <button @click="open = !open">Toggle</button>
    <div x-show="open" x-transition>
        Content
    </div>
</div>
```

### htmx Patterns

```html
<!-- Trigger search on input -->
<input type="search"
       name="q"
       hx-get="/search/"
       hx-trigger="keyup changed delay:500ms"
       hx-target="#results">

<!-- Infinite scroll pagination -->
<div hx-get="/comics/page/2/"
     hx-trigger="revealed"
     hx-swap="afterend">
    Load more...
</div>
```

### Webpack Build

```javascript
// webpack/common.config.js
module.exports = {
  entry: {
    main: './static/js/main.js',
    vendors: './static/js/vendors.js',
  },
  output: {
    path: path.resolve(__dirname, '../dist'),
    filename: '[name].[contenthash].js',
  },
  module: {
    rules: [
      { test: /\.ts$/, use: 'ts-loader' },
      { test: /\.scss$/, use: ['style-loader', 'css-loader', 'sass-loader'] },
    ],
  },
};
```

## Celery Tasks

```python
# config/celery_app.py
from celery import Celery

app = Celery("api")
app.config_from_object("django.conf:settings", namespace="CELERY")

@app.task(bind=True, max_retries=3)
def scrape_comic_task(self, url):
    try:
        # Execute Scrapy spider programmatically
        from scrapy.crawler import CrawlerProcess
        # ... scraping logic
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)
```

## Scripts

```bash
python manage.py run_scraper        # Run main scraper
python manage.py cleanup_old_data   # Data retention cleanup
python manage.py export_data        # Export all scraped data
npm run clean                       # Clean frontend build
npm run build:prod                  # Production frontend build
```
