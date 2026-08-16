# Django-Scrapy-Selenium Research Reference

Condensed findings from July 2026 research for the Django-Scrapy-Selenium scraping platform project.

## Key Sources (Verified 2026)

| Source | URL | Focus |
|--------|-----|-------|
| GroupBWT Scrapy Tutorial | https://groupbwt.com/blog/scrapy-tutorial | Scrapy 2.13+ architecture, async `start()`, Playwright integration |
| Scrapfly Scrapy Playwright | https://scrapfly.io/blog/posts/web-scraping-dynamic-websites-with-scrapy-playwright | Step-by-step scrapy-playwright setup, infinite scroll, element interaction |
| AgentHustler Storage | https://dev.to/agenthustler/how-to-store-web-scraped-data-in-2026-postgresql-mongodb-csv-and-cloud-storage-2f5c | PostgreSQL upsert patterns, batch inserts, MongoDB for variable schemas |
| Deni Bertović Celery | https://denibertovic.com/posts/celery-best-practices | Queue separation, priority workers, error handling, Flower monitoring |
| Playwright vs Selenium 2026 | https://dev.to/deepak_mishra_35863517037/playwright-vs-selenium-a-2026-architecture-review-347d | Protocol comparison (HTTP vs WebSocket), auto-wait internals, BiDi reality |
| UK Data Services Comparison | https://ukdataservices.co.uk/blog/articles/selenium-vs-playwright-comparison | Performance benchmarks (2.3x faster), migration timeline |
| IPRoyal Best Practices | https://iproyal.com/blog/best-web-scraping-practises | robots.txt, rate limiting, proxy rotation, legal compliance 2026 |
| Selenium 4 Upgrade | https://www.selenium.dev/documentation/webdriver/troubleshooting/upgrade_to_selenium_4 | Options vs DesiredCapabilities, Service objects, Python deprecations |

## Architecture Patterns for This Stack

### Scrapy + Playwright (Primary for JS-heavy sites)
```python
# settings.py
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
PLAYWRIGHT_BROWSER_TYPE = "chromium"
PLAYWRIGHT_LAUNCH_OPTIONS = {"headless": True, "timeout": 60000}
```

```python
# Spider using Playwright
async def parse(self, response):
    page = response.meta["playwright_page"]
    await page.wait_for_selector(".dynamic-content")
    # scroll, click, fill forms via page.evaluate(), page.click()
    yield {"data": await page.content()}
```

### Celery Task Orchestration
```python
# tasks.py
@app.task(bind=True, queue="scraping_high", max_retries=3, default_retry_delay=300)
def run_spider(self, spider_name, params):
    from scrapy.crawler import CrawlerProcess
    process = CrawlerProcess(settings)
    process.crawl(spider_name, **params)
    process.start()
```

**Queue separation**: `scraping_high` (priority) + `scraping_bulk` (volume)
**Production settings**: `task_acks_late=True`, `worker_prefetch_multiplier=1`, `visibility_timeout=3600`

### PostgreSQL Storage with Upsert
```python
# pipeline.py
def save_item(self, item):
    cur.execute("""
        INSERT INTO products (external_id, name, price, source_url, raw_json)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (external_id) DO UPDATE SET
            name = EXCLUDED.name,
            price = EXCLUDED.price,
            updated_at = NOW()
    """, (item["external_id"], item["name"], item["price"], item["url"], json.dumps(item)))
```

**Batch**: `psycopg2.extras.execute_values()` for 10-50x speedup.

## Decision Matrix

| Scenario | Tool |
|----------|------|
| Static listing pages, high volume | Scrapy + httpx (async) |
| SPAs, infinite scroll, auth flows | Scrapy + Playwright |
| Legacy IE / Appium mobile | Selenium 4.x |
| New scrapers (2026+) | **Default: Playwright** |

## Anti-Detection Checklist
- [ ] `headless="new"` (Chrome 109+) or headed mode
- [ ] CDP override: `navigator.webdriver = undefined`
- [ ] `undetected-chromedriver` if Selenium required
- [ ] Realistic UA rotation middleware
- [ ] Residential proxies at scale
- [ ] `robots.txt` check via `scrapy-robots` or stdlib `robotparser`
- [ ] Rate limits: `DOWNLOAD_DELAY=1`, `AUTOTHROTTLE_ENABLED=True`

## Compliance Notes
- Public data scraping generally legal (US CFAA precedent, EU GDPR for PII)
- Always respect `robots.txt` and ToS
- Sanitize PII before storage (`bleach.clean()` for HTML, regex allowlists for text)
- Design idempotent scrapers (upsert, not insert)