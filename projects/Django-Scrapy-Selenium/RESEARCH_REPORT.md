# RESEARCH_REPORT.md

## Project: Django-Scrapy-Selenium

**Type:** Production web scraping platform (full-stack)
**Tech Stack:** Django 4.x, DRF, Scrapy, Selenium WebDriver, BeautifulSoup4, Celery + Redis/RabbitMQ, Webpack, Tailwind CSS, PostgreSQL, Docker Compose, Gunicorn
**Status:** Active

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|-------------|
| Scrapy RTFM | https://scrapy.org | Official Scrapy framework |
| Celery Docs | https://docs.celeryq.dev | Async task queue docs |
| Selenium with Python | https://selenium-python.readthedocs.io | Automating browser interactions |

## Key Findings

### Scrapy + Selenium Integration (2026)
- Scrapy's `scrapy-playwright` middleware is now preferred over Selenium for JS-heavy pages (scrapy.org, 2026)
- Scrapy handles crawling/scraping; Selenium fills gaps for complex browser interactions
- The Celery-mediated architecture (Scrapy spiders as tasks) scales horizontally with worker count
- Item pipelines handle data cleaning, validation, and storage in a unified flow

### Celery Async Patterns
- Celery + Redis provides reliable task queuing with result backend for status tracking
- Flower (Celery monitoring) is recommended for production observability
- Task retry with exponential backoff is essential for transient scraping failures
- Beat scheduler enables periodic scraping jobs

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Scrapy Docs | https://docs.scrapy.org | Scrapy framework docs |
| Selenium Python | https://selenium-python.readthedocs.io | Selenium guide |
| Celery Django | https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html | Celery + Django |
| Docker Compose | https://docs.docker.com/compose | Container orchestration |

## Best Practices

1. **Scrapy-Selenium hybrid** — Use Scrapy for crawling, Selenium only for JS-gated content
2. **Celery task idempotency** — Ensure scraping tasks can be safely retried (use unique job IDs)
3. **Item pipelines for storage** — Keep spiders stateless; delegate storage to pipelines
4. **Rate limiting via Scrapy settings** — `CONCURRENT_REQUESTS_PER_DOMAIN` and `DOWNLOAD_DELAY`
5. **Separate Docker services** — Django web, Celery worker, Celery beat, Redis, PostgreSQL

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Headless detection by target sites | Scraping blocked | Rotate user-agents + add random delays |
| Memory leaks in long-running spiders | OOM kills in production | Restart workers periodically |
| Celery task retry storms | DDoS target site | Cap max_retries and add jitter |
| Selenium ChromeDriver version mismatch | Driver errors | Pin versions in Dockerfile |

## Performance

1. **Scrapy's async engine** handles hundreds of concurrent requests per spider
2. **Celery horizontal scaling** — Add workers for parallel scraping
3. **Database connection pooling** — Use PgBouncer for PostgreSQL under heavy load
4. **Redis as broker** — Fastest Celery message broker compared to RabbitMQ for simple workloads
5. **Django caching** — Cache scraped results to avoid redundant re-scraping

## Security

1. **Proxy rotation** — Avoid IP-based blocking by using residential proxy pools
2. **Scrapy downloader middlewares** — Strip sensitive headers from outgoing requests
3. **Celery task input validation** — Prevent task injection via serialized payloads
4. **Rate-limit Django DRF endpoints** — Prevent API abuse via django-ratelimit
5. **Store credentials in environment variables** — Database, Redis, proxy credentials

## Related Projects (in workspace)

- **selenium_webdriver** — Standalone Node.js Selenium scraper, shares retry-on-stale patterns
- **rhixecompany-comics** — Target for scraping capabilities consolidation
- **Python-projects** — Contains standalone Python scraping scripts with BeautifulSoup4

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Scrapy | https://docs.scrapy.org | Web crawling framework |
| Selenium Python | https://selenium-python.readthedocs.io | Browser automation |
| Celery | https://docs.celeryq.dev | Task queue |
| scrapy-playwright | https://github.com/scrapy-plugins/scrapy-playwright | Scrapy + Playwright middleware |
