# Django-Scrapy-Selenium — API Reference

## Django Views & Endpoints

### Web Interface (htmx/HTML)

| URL Pattern | Method | Purpose | Template |
|-------------|--------|---------|----------|
| `/` | GET | Home page with recent comics | `pages/home.html` |
| `/comics/` | GET | Browse comics with filters | `comics/list.html` |
| `/comics/<id>/` | GET | Comic detail | `comics/detail.html` |
| `/search/` | GET | Search comics | `search/results.html` |
| `/admin/` | GET | Django admin interface | admin templates |
| `/accounts/` | GET/POST | Auth (allauth) | allauth templates |

### htmx Endpoints (Partial HTML)

| URL Pattern | htmx Trigger | Purpose |
|-------------|--------------|---------|
| `GET /comics/filter/` | htmx:form | Filter comic list |
| `GET /comics/page/<n>/` | htmx:click | Paginate results |
| `POST /scrape/run/` | htmx:submit | Trigger scrap job |
| `GET /scrape/status/<id>/` | htmx:load | Poll scrap status |

### Scraping Management

#### `POST /scrape/run/`
- **Purpose:** Trigger a scraping job
- **Body:** `{ "url": "...", "type": "comic|chapter|update" }`
- **Response:** htmx partial with job ID and status

#### `GET /scrape/status/<job_id>/`
- **Purpose:** Poll status of a scraping job
- **Response:** htmx partial with progress/status

#### `POST /scrape/schedule/`
- **Purpose:** Schedule recurring scraping
- **Body:** `{ "spider": "comic_spider", "interval": "daily" }`

### Scrapy Management Commands

```bash
# Run a spider
scrapy crawl comic_spider
scrapy crawl chapter_spider -a url="https://example.com/chapter/1"

# List all spiders
scrapy list

# Run with output
scrapy crawl comic_spider -o output.json
```

### Selenium API (Internal)

```python
# selenium_scraper/scraper.py
class SeleniumScraper:
    def scrape_page(self, url: str) -> dict:
        """Scrape a JS-rendered page"""
        pass

    def scrape_multiple(self, urls: list) -> list:
        """Scrape multiple pages"""
        pass

    def screenshot(self, url: str, path: str):
        """Take screenshot of a page"""
        pass
```

### Celery Tasks

```python
# Available Celery tasks
run_comic_spider.delay()             # Run Scrapy spider
run_selenium_scrape.delay(url)       # Run Selenium scraper
export_data.delay(format, filters)   # Export scraped data
cleanup_old_data.delay()             # Retention cleanup
```

### Django Admin

| URL | Description |
|-----|-------------|
| `/admin/` | Admin dashboard |
| `/admin/scraping/comic/` | Manage scraped comics |
| `/admin/scraping/chapter/` | Manage chapters |
| `/admin/scraping/scrapejob/` | View scrape job history |
| `/admin/users/user/` | User management |

## Response Formats

### htmx (HTML Fragments)
Standard HTML partials returned for htmx requests, swapped into the DOM.

### JSON (AJAX/axios)
```json
{
  "status": "success",
  "data": { ... },
  "message": "Scraping job started"
}
```
