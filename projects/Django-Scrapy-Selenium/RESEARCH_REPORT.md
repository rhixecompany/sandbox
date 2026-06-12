# RESEARCH_REPORT.md

## Project: Django-Scrapy-Selenium

**Type:** Web scraping + automation platform
**Tech Stack:** Python 3.10+, Django 4.x, Django REST Framework, Scrapy, Selenium WebDriver, BeautifulSoup4, Celery + Redis, PostgreSQL, Tailwind CSS (Webpack), Docker Compose
**Status:** Consolidation target

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| selenium_webdriver | `projects/selenium_webdriver` | Browser automation sibling; shared ChromeDriver and retry patterns. |
| rhixecompany-comics | `projects/rhixecompany-comics` | Consolidation target inheriting scraping pipeline. |

---

## Key Findings

### Scrapy 2026 Pattern
- Scrapy 2.14+ is async-first; migrate `start_requests` to `async def start()` and prefer `AsyncCrawlerProcess` inside Celery workers.
- Use Scrapy item pipelines for normalization before DB writes; avoid duplicate parsing logic in views.

### Selenium Modernization
- Selenium Manager now auto-resolves driver binaries; avoid pinned ChromeDriver commits.
- Use explicit waits plus retry decorators; centralize wait logic in `utils.js`-style helpers.

### Django + Celery Coordination
- Celery task schemas should include `status`, `started_at`, `finished_at`, `source_repo`, and `payload_ref`.
- Use RabbitMQ or Redis with appropriate visibility timeout and dead-letter queue handling for scraping tasks.

### Frontend Dashboard
- Replace Webpack + Tailwind manual build with optional Next.js dashboard telemetry if the scraping surface needs richer visualizations.

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Scrapy docs | https://docs.scrapy.org | Docs |
| Selenium with Python | https://selenium-python.readthedocs.io | Docs |
| Celery docs | https://docs.celeryq.dev | Docs |
| DRF docs | https://www.django-rest-framework.org | Docs |
| BeautifulSoup docs | https://www.crummy.com/software/BeautifulSoup/bs4/doc | Docs |

---

## Best Practices
1. **Async-first scraping** — migrate to `AsyncCrawlerProcess` and avoid Twisted callback chains.
2. **Selenium for-auth flows only** — use `scrapy-playwright` for JS-rendered sites; keep Selenium for login and MFA.
3. **Dead-letter scraping logs** — store raw HTML and parse failures for later reprocessing instead of silent drops.
4. **DRF permissions** — restrict scraping control APIs to admin users; do not expose queue endpoints publicly.

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Mixing Selenium and Scrapy state | Flaky pipeline coupling | Use async task boundaries with retries. |
| Blind `time.sleep` waits | Slow scrapes and timeouts | Replace with explicit waits and expect conditions. |
| Storing raw secrets for proxies | Credential leak | Load proxy auth from environment only. |
| No robots obeyance | Legal or rate-limit risk | Enforce `ROBOTSTXT_OBEY=True` and rate-limit all crawls. |

---

## Performance
1. Run Scrapy `CONCURRENT_REQUESTS=16` with DOMAIN parallelism; tune via queue depth monitors.
2. Use Redis caching for repeated anti-bot solutions like Cloudflare challenge tokens.
3. Separate Celery queues by source site so one slow domain cannot block others.
4. Keep Docker images lean and reuse layers across Django + Scrapy + Selenium services.

---

## Security
1. Sanitize all scraped HTML and JSON before render or storage to prevent stored XSS.
2. Restrict DRF endpoints to authenticated staff; do not allow unauthenticated crawl triggers.
3. Avoid hardcoded target URLs; load them from signed configuration or admin UI.
4. Validate all uploads and outputs when exercising Selenium upload flows.

---

## Related Projects (in workspace)

- **selenium_webdriver** — browser automation sibling; shared retry + Selenium utilities
- **comicwise** — upstream consumer of scraped comic data
- **Django-Scrapy-Selenium** — should be marked consolidation source in downstream reports

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Scrapy docs | https://docs.scrapy.org | Framework docs |
| Selenium docs | https://www.selenium.dev/documentation | Browser automation docs |
| Celery docs | https://docs.celeryq.dev | Task queue |
| DRF docs | https://www.django-rest-framework.org | API framework |
| Playwright | https://playwright.dev | Modern browser automation |
