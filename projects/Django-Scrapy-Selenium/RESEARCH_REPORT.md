# RESEARCH_REPORT — Django-Scrapy-Selenium

> **Type:** Project research report | **Updated:** 2026-07-10

**Type:** Django-based web scraping platform
**Tech Stack:** Django 4.x, DRF, Scrapy, Selenium, BeautifulSoup4, Celery + Redis/RabbitMQ, PostgreSQL, Gunicorn, Webpack 5, Tailwind CSS 3, Alpine.js, htmx
**Status:** Active (legacy — scraping consolidated to rhixecompany-comics)

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| codingforentrepreneurs/Web-Scraping-with-Django-Celery | <https://github.com/codingforentrepreneurs/Web-Scraping-with-Django-Celery> | Django + Celery scraping scheduler |
| scrapy-plugins/scrapy-playwright | <https://github.com/scrapy-plugins/scrapy-playwright> | Official Scrapy + Playwright integration |
| scrapfly/scrapfly-scrapers | <https://github.com/scrapfly/scrapfly-scrapers> | Production scraping patterns 2026 |

---

## Key Findings

### Scrapy + Playwright 2026 (Updated July 2026)

- **Playwright is the dominant default** for JS-rendered content: auto-wait, native CDP, multi-browser (Chromium, Firefox, WebKit) out of the box
- **Scrapy + HTTPX/httpx** remains strongest for high-volume static-page crawling (4x throughput vs requests)
- **Scrapy 2.13+** introduces `async def start()` replacing deprecated `start_requests()` — first-class async support
- **scrapy-playwright integration** processes requests via Playwright download handlers; keeps Scrapy pipeline/middleware intact
- **Hybrid approach recommended**: Scrapy for static/listing pages, Playwright for detail pages requiring JS interaction
- **Configuration**: `DOWNLOAD_HANDLERS` with `scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler` + `TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"`
- **Scheduler improvement**: `DownloaderAwarePriorityQueue` (default in 2.13+) spreads requests evenly across domains

### Django + Celery Scraping Integration (2026)

- **Scrapy spiders best called from Celery tasks**, not coupled to Django views — keeps web tier responsive
- **Django ORM usable inside Scrapy pipelines** for direct persistence (via `django.setup()` in spider settings)
- **`django-celery-beat`** for DB-backed periodic tasks (2026 best practice) — enables Django Admin scheduling
- **`django-celery-results`** for task result inspection via Django Admin
- **Flower** for real-time worker/task dashboard (monitoring, retry, revocation)
- **Worker concurrency**: `--concurrency=CPU*2+1` for I/O-bound scraping workloads
- **Critical production settings**: `task_acks_late=True`, `task_reject_on_worker_lost=True`, `worker_prefetch_multiplier=1`
- **`celery-once` with Redis lock** prevents duplicate execution from retries
- **Queue separation**: dedicated queues for high-priority vs bulk scraping tasks (e.g., `scraping_high`, `scraping_bulk`)
- **Visibility timeout tuning**: set `broker_transport_options = {'visibility_timeout': 3600}` for long-running scrape tasks

### Selenium WebDriver 4.x Best Practices (2026)

- **Selenium 4.x stable** is mainstream default — W3C WebDriver compliant, mature Grid 4, improved driver management
- **Upgrade path**: replace `DesiredCapabilities` with `Options` classes (e.g., `ChromeOptions`), use `Service` objects for driver paths
- **Python-specific**: `executable_path` deprecated — use `Service(executable_path=...)` or ensure driver in PATH
- **Headless mode**: use `headless="new"` (Chrome 109+) for better anti-detection; headed mode for stubborn sites
- **BiDi support** in Selenium 4+ enables CDP-like capabilities (network interception, console logs) but is additive on legacy HTTP architecture
- **Anti-detection**: override `navigator.webdriver` via CDP; `undetected-chromedriver` (Python) remains effective
- **Memory management**: always `driver.quit()` in `finally` block; use `driver.close()` for single tabs

### Scrapy Spider Architecture for Dynamic Content Sites

- **Spider structure**: define `async def start()` for entry points; `parse` callbacks yield items + follow-up requests
- **Dynamic content**: use `meta={"playwright": True}` on requests requiring JS rendering
- **Infinite scroll**: `page.evaluate("window.scrollTo(0, document.body.scrollHeight)")` + wait for new elements
- **Element interaction**: `page.click()`, `page.fill()`, `page.wait_for_selector()` via Playwright page object in `meta`
- **Custom contexts**: define `PLAYWRIGHT_CONTEXTS` in settings for viewport/locale/timezone profiles per spider
- **Middleware**: downloader middleware handles proxy rotation, user-agent rotation, cookie persistence
- **Pipelines**: validation → cleaning → deduplication (via `ON CONFLICT` upsert) → storage

### Playwright vs Selenium for Django Scraping (2026)

| Dimension | Selenium 4.x | Playwright |
|-----------|--------------|------------|
| **Protocol** | HTTP/REST (W3C WebDriver) | WebSocket (CDP) — persistent connection |
| **Wait mechanism** | External polling (`WebDriverWait`) | Internal event loop (`requestAnimationFrame`) |
| **Speed** | Baseline | 2-3x faster (2.3x in benchmarks) |
| **Memory/Process** | 1 process per browser | Browser contexts (isolated profiles) per task |
| **Network control** | MITM proxy required (BrowserMob) | Native CDP interception (no proxy) |
| **Browser support** | Chrome, Firefox, Safari, Edge, IE | Chromium, Firefox, WebKit (no IE) |
| **Mobile testing** | Via Appium | Built-in device emulation |
| **Language support** | Java, C#, Python, Ruby, JS | TS/JS, Python, Java, .NET |
| **Best for** | Legacy grids, IE, enterprise compliance | New scraping projects, SPAs, scale |

**Verdict for Django-Scrapy-Selenium**: Migrate new scrapers to **Playwright** (via `scrapy-playwright`). Keep Selenium only for legacy flows requiring IE or specific Appium mobile testing. Playwright's architecture eliminates the "flaky test" class of bugs caused by external polling.

### Rate Limiting and robots.txt Compliance (2026)

- **Robots.txt**: **always check first** — `robotparser` (stdlib) or `scrapy-robots` middleware
- **Rate limiting layers**:
  - Scrapy: `DOWNLOAD_DELAY = 1` (project template default), `CONCURRENT_REQUESTS_PER_DOMAIN = 1`
  - Scrapy AutoThrottle: `AUTOTHROTTLE_ENABLED = True`, `AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0`
  - Playwright: `page.wait_for_load_state("networkidle")` between actions
  - Celery: `celery.task.rate_limit` per task type
- **User-Agent rotation**: middleware rotating from realistic UA pool (not just `scrapy` default)
- **Proxy rotation**: residential proxies at scale; datacenter for low-risk targets
- **Legal/ethical**: Respect `robots.txt`, Terms of Service; public data scraping generally legal (US CFAA precedent, EU GDPR considerations for personal data)

### Scraping Data Sanitization and Storage Patterns (2026)

- **PostgreSQL (recommended for structured data)**:
  - `ON CONFLICT (external_id) DO UPDATE` upsert pattern prevents duplicates on re-scrapes
  - `UNIQUE` constraint on `external_id` (source-specific identifier)
  - `JSONB` column for flexible raw payload storage (re-parse later)
  - Batch inserts via `psycopg2.extras.execute_values` (10-50x faster than single inserts)
  - Index on `scraped_at`, `source_url` for time-series queries
- **MongoDB**: when schemas vary significantly across sources (e.g., some products have reviews, others specs)
- **Flat files (CSV/JSONL)**: prototyping only; migrate to DB at >100K rows
- **Cloud storage (S3/GCS)**: raw HTML/JSON archival for compliance/reprocessing
- **Data validation before storage**: required fields, type checks, length limits, price > 0
- **Price history**: separate `price_history` table with FK to product, insert only on change
- **Sanitization**: `bleach.clean()` for HTML content; regex/allowlist for text fields; XSS prevention for any rendered output

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Celery + Django | <https://docs.celeryq.dev/en/stable/django/> | Integration Guide |
| Scrapy Architecture | <https://docs.scrapy.org/en/latest/topics/architecture.html> | Official Architecture |
| Scrapy + Playwright | <https://scrapfly.io/blog/posts/web-scraping-dynamic-websites-with-scrapy-playwright> | Tutorial 2026 |
| Scraping tools 2026 | <https://dev.to/agenthustler/top-web-scraping-tools-and-frameworks-in-2026-scrapy-selenium-playwright-beautifulsoup-and-more-3fai> | Comparison |
| Selenium waits | <https://www.selenium.dev/documentation/webdriver/waits> | Official guide |
| Anti-detection tools | <https://scrapfly.io/blog/posts/best-anti-bot-bypass-tools> | 2026 comparison |
| Scrapy Playwright config | <https://github.com/scrapy-plugins/scrapy-playwright> | GitHub repo |
| Celery best practices | <https://denibertovic.com/posts/celery-best-practices> | Deni Bertović guide |
| Scraped data storage | <https://dev.to/agenthustler/how-to-store-web-scraped-data-in-2026-postgresql-mongodb-csv-and-cloud-storage-2f5c> | Storage patterns 2026 |
| Web scraping best practices | <https://iproyal.com/blog/best-web-scraping-practises> | IPRoyal 2026 guide |
| Playwright vs Selenium | <https://dev.to/deepak_mishra_35863517037/playwright-vs-selenium-a-2026-architecture-review-347d> | Architecture review |
| Selenium 4 upgrade | <https://www.selenium.dev/documentation/webdriver/troubleshooting/upgrade_to_selenium_4> | Official upgrade guide |

---

## Best Practices

1. **Prefer Playwright over Selenium** — faster, auto-wait, stealth plugins; migrate new scrapers via `scrapy-playwright`
2. **Robots.txt compliance** — check and respect before spidering any site; use `robotparser` or `scrapy-robots`
3. **Rate limiting** — `DOWNLOAD_DELAY` + `AUTO_THROTTLE`; user-agent rotation mandatory; proxy rotation at scale
4. **Data sanitization** — clean scraped data before persistence (XSS prevention, type validation)
5. **Celery production settings** — `acks_late`, `reject_on_worker_lost`, `prefetch_multiplier=1`
6. **Queue separation** — dedicated Celery queues for priority vs bulk scraping tasks
7. **Upsert pattern** — `ON CONFLICT (external_id) DO UPDATE` in PostgreSQL for idempotent storage
8. **Batch inserts** — `execute_values` for bulk persistence (10-50x speedup)
9. **Observability** — Flower for Celery monitoring; structured logging in spiders/pipelines
10. **Headless mitigation** — `headless="new"`, CDP `navigator.webdriver` override, undetected-chromedriver for Selenium

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Scrapy + Django tight coupling | hard to test/debug | spiders in `crawler/spiders/`; called from Celery |
| Selenium `webdriver` flag detected | CAPTCHA / blocking | override via CDP; use undetected-chromedriver |
| Celery broker not running | tasks silently lost | always verify Redis/RabbitMQ is up |
| No rate limiting | IP ban | `DOWNLOAD_DELAY` + `CONCURRENT_REQUESTS` limits |
| Selenium memory leaks | zombie Chrome | `driver.quit()` in `finally` block |
| Single Celery queue for all tasks | priority starvation | separate queues: `scraping_high`, `scraping_bulk` |
| Visibility timeout too short | duplicate task execution | set `visibility_timeout > max_task_duration` |
| Passing ORM objects to Celery tasks | stale data | pass IDs only; re-fetch in task |
| No data validation before storage | corrupt DB | validate required fields, types, ranges in pipeline |
| Ignoring robots.txt | legal/ethical risk | check via middleware before crawling |

---

## Performance

1. **Scrapy + httpx** — async HTTP; 4x throughput vs requests
2. **BeautifulSoup4 + lxml** — 3-5x faster DOM parsing than html.parser
3. **Playwright over Selenium** — 2-3x faster execution (2.3x benchmarked)
4. **Celery worker concurrency** — `--concurrency=CPU*2+1` for I/O-bound scraping
5. **Redis caching** — cache Django API responses; `django-redis` for session/cache backend
6. **Batch database inserts** — `psycopg2.extras.execute_values` for bulk upserts
7. **Scrapy concurrency tuning** — `CONCURRENT_REQUESTS=32`, `CONCURRENT_REQUESTS_PER_DOMAIN=8` (framework defaults); project template defaults more conservative
8. **Playwright browser contexts** — reuse browser process, spawn isolated contexts per task (lower memory than new browsers)
9. **Connection pooling** — `pgbouncer` for PostgreSQL; `redis-py` connection pool for Celery broker
10. **Async Scrapy** — `async def parse()` + `AsyncCrawlerProcess` for full async pipeline (Scrapy 2.13+)

---

## Security

1. **Sanitize scraped data** — escape/clean before storage or display (bleach, allowlists)
2. **Proxy rotation** — residential proxies at scale; avoid datacenter IP blocks
3. **Celery task validation** — validate parameters; sanitize URLs (SSRF prevention)
4. **Headless detection mitigation** — keep up to date (evolves with anti-bot tech); Camoufox for Firefox
5. **Respect robots.txt** — legal and ethical requirement
6. **Credential isolation** — never hardcode API keys/proxy creds; use env vars / secret manager
7. **Rate limit your own endpoints** — Django REST Framework throttling on scraped data APIs
8. **PII handling** — detect and redact personal data before storage (GDPR/CCPA)
9. **Task idempotency** — design scrapers to be safely re-runnable (upsert, not insert)

---

## Related Projects (in workspace)

- **profile** — shares Django + PostgreSQL stack
- **rhixecompany-comics** — scraping consolidated to this project
- **selenium_webdriver** — Node.js Selenium patterns

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Scrapy Docs | <https://docs.scrapy.org/> | Scrapy framework docs |
| Scrapy Architecture | <https://docs.scrapy.org/en/latest/topics/architecture.html> | Core architecture diagram |
| Scrapy Playwright | <https://github.com/scrapy-plugins/scrapy-playwright> | Official integration |
| Selenium Docs | <https://www.selenium.dev/documentation/> | Browser automation docs |
| Selenium 4 Upgrade | <https://www.selenium.dev/documentation/webdriver/troubleshooting/upgrade_to_selenium_4> | Migration guide |
| Celery Docs | <https://docs.celeryq.dev/> | Task queue docs |
| Celery Best Practices | <https://denibertovic.com/posts/celery-best-practices> | Production patterns |
| Playwright | <https://playwright.dev/> | Modern browser automation |
| Playwright vs Selenium | <https://dev.to/deepak_mishra_35863517037/playwright-vs-selenium-a-2026-architecture-review-347d> | 2026 architecture review |
| Scraped Data Storage | <https://dev.to/agenthustler/how-to-store-web-scraped-data-in-2026-postgresql-mongodb-csv-and-cloud-storage-2f5c> | PostgreSQL/MongoDB patterns |
| Web Scraping Best Practices | <https://iproyal.com/blog/best-web-scraping-practises> | IPRoyal 2026 guide |
| Rate Limiting/AutoThrottle | <https://docs.scrapy.org/en/latest/topics/autothrottle.html> | Scrapy AutoThrottle docs |
| robots.txt parser | <https://docs.python.org/3/library/urllib.robotparser.html> | stdlib compliance |
| Flower Monitoring | <https://flower.readthedocs.io/> | Celery monitoring UI |
| Playwright | <https://playwright.dev/> | Modern browser automation |
