# RESEARCH_REPORT — Django-Scrapy-Selenium

> **Type:** Project research report | **Updated:** 2026-06-29

**Type:** Django-based web scraping platform
**Tech Stack:** Django 4.x, DRF, Scrapy, Selenium, BeautifulSoup4, Celery + Redis/RabbitMQ, PostgreSQL, Playwright
**Status:** Active (legacy — scraping consolidated to rhixecompany-comics)

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| codingforentrepreneurs/Web-Scraping-with-Django-Celery | https://github.com/codingforentrepreneurs/Web-Scraping-with-Django-Celery | Django + Celery scraping scheduler |
| scrapingbee/selenium-python | https://www.scrapingbee.com/blog/selenium-python | 2026 modern Selenium guide |

---

## Key Findings

### Scrapy + Playwright 2026
- Playwright is the dominant default: auto-wait, native CDP, and broader browser support than Selenium
- Scrapy + HTTPX remains strongest for high-volume static-page crawling
- Current project mix is reasonable: Selenium for legacy flows, add Playwright for JS-heavy targets

### Django + Celery Scraping Integration (2026)
- Scrapy spiders best called from Celery tasks, not coupled to Django views
- Django ORM usable inside Scrapy pipelines for direct persistence
- `django-celery-beat` for DB-backed periodic tasks (2026 best practice)
- `django-celery-results` for task result inspection via Django Admin
- Flower for real-time worker/task dashboard
- Worker concurrency: `--concurrency=CPU*2+1`

### Selenium Anti-Detection (2026)
- `navigator.webdriver` is primary detection vector — override via CDP
- Headless detection increasing; use `headless: "new"` or headed mode
- undetected-chromedriver (Python) / puppeteer-extra-plugin-stealth (Node)
- Camoufox (Firefox stealth) and playwright-stealth are top 2026 tools

### Celery Reliability (2026)
- Redis is fastest broker; RabbitMQ offers stronger durability
- **Critical settings**: `task_acks_late=True`, `task_reject_on_worker_lost=True`, `worker_prefetch_multiplier=1`
- `celery-once` with Redis lock prevents duplicate execution from retries

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Celery + Django | https://docs.celeryq.dev/en/stable/django/ | Integration Guide |
| Scraping tools 2026 | https://dev.to/agenthustler/top-web-scraping-tools-and-frameworks-in-2026-scrapy-selenium-playwright-beautifulsoup-and-more-3fai | Comparison |
| Selenium waits | https://www.selenium.dev/documentation/webdriver/waits | Official guide |
| Anti-detection tools | https://scrapfly.io/blog/posts/best-anti-bot-bypass-tools | 2026 comparison |

---

## Best Practices

1. **Prefer Playwright over Selenium** — faster, auto-wait, stealth plugins; migrate new scrapers
2. **Robots.txt compliance** — check and respect before spidering any site
3. **Rate limiting** — `DOWNLOAD_DELAY` + `AUTO_THROTTLE`; user-agent rotation mandatory
4. **Data sanitization** — clean scraped data before persistence (XSS prevention)
5. **Celery production settings** — `acks_late`, `reject_on_worker_lost`, `prefetch_multiplier=1`

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Scrapy + Django tight coupling | hard to test/debug | spiders in `crawler/spiders/`; called from Celery |
| Selenium `webdriver` flag detected | CAPTCHA / blocking | override via CDP; use undetected-chromedriver |
| Celery broker not running | tasks silently lost | always verify Redis/RabbitMQ is up |
| No rate limiting | IP ban | `DOWNLOAD_DELAY` + `CONCURRENT_REQUESTS` limits |
| Selenium memory leaks | zombie Chrome | `driver.quit()` in `finally` block |

---

## Performance

1. **Scrapy + httpx** — async HTTP; 4x throughput vs requests
2. **BeautifulSoup4 + lxml** — 3-5x faster DOM parsing
3. **Playwright over Selenium** — 2-3x faster execution
4. **Celery worker concurrency** — `--concurrency=CPU*2+1`
5. **Redis caching** — cache Django API responses

---

## Security

1. **Sanitize scraped data** — escape/clean before storage or display
2. **Proxy rotation** — residential proxies at scale
3. **Celery task validation** — validate parameters; sanitize URLs
4. **Headless detection mitigation** — keep up to date (evolves with anti-bot tech)
5. **Respect robots.txt** — legal and ethical requirement

---

## Related Projects (in workspace)

- **profile** — shares Django + PostgreSQL stack
- **rhixecompany-comics** — scraping consolidated to this project
- **selenium_webdriver** — Node.js Selenium patterns

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Scrapy Docs | https://docs.scrapy.org/ | Scrapy framework docs |
| Selenium Docs | https://www.selenium.dev/documentation/ | Browser automation docs |
| Celery Docs | https://docs.celeryq.dev/ | Task queue docs |
| Playwright | https://playwright.dev/ | Modern browser automation |