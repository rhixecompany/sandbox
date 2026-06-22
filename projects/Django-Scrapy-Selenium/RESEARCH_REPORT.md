## Project: Django-Scrapy-Selenium
**Type:** Web scraping + automation platform  
**Tech Stack:** Python 3.10+, Django 4.x, Django REST Framework, Scrapy, Selenium WebDriver, BeautifulSoup4, Celery + Redis/RabbitMQ, PostgreSQL, Tailwind CSS (Webpack), Docker Compose, Gunicorn  
**Status:** Consolidation target (patterns extracted → rhixecompany-comics)

## Similar Projects
| Project | URL | Why Relevant |
|---------|-----|--------------|
| selenium_webdriver | `projects/selenium_webdriver` | Browser automation sibling; shared ChromeDriver and retry patterns |
| rhixecompany-comics | `projects/rhixecompany-comics` | Consolidation target inheriting scraping pipeline |
| comicwise | `projects/comicwise` | Upstream consumer of scraped comic data |

## Key Findings
### 1. Scrapy + Django + Celery Integration (2026 Patterns)
**Async-First Architecture:** Scrapy 2.14+ is async-first; migrate `start_requests` to `async def start()` and prefer `AsyncCrawlerProcess` inside Celery workers [Real Python]. The traditional Twisted callback chains are being replaced by modern async patterns.
**Task Queue Integration:** Production systems at scale use Celery to orchestrate Scrapy spiders across Kubernetes workers. A documented system achieves ~12,000 pages/second targeting 2M sites/week using Scrapy + Celery + pandas + Kubernetes with self-hosted PostgreSQL [Reddit r/webscraping]. Critical success factors: quality proxy providers (not VPNs), message queues for horizontal scaling, targeting structured data sources (ATS platforms), undetectable ChromeDriver, and self-hosted databases.
**Django-Celery Setup Pattern:** 
1. Create `celery.py` with `app = Celery("project")` and `app.config_from_object("django.conf:settings", namespace="CELERY")` [Real Python]
2. Configure `CELERY_BROKER_URL` and `CELERY_RESULT_BACKEND` in Django settings (Redis or RabbitMQ)
3. Use `@shared_task` decorator for reusable Django apps
4. Run 3 terminals: Django, Redis, Celery worker (`celery -A project worker -l info`)
### 2. Selenium Modernization & Anti-Detection (2026)
**Tool Selection Reality:** In 2026, the scraping tool hierarchy is: **Requests + BeautifulSoup (70% of jobs)**, **Playwright (29%)**, **Selenium (legacy only)** [dev.to/agenthustler]. Playwright is "the scraping tool built for the modern web" with native async, auto-waiting, network interception, and better anti-bot bypass.

## Cheatsheets & Quick Reference
| Topic | Resource | Type |
|-------|----------|------|
| Scrapy docs | https://docs.scrapy.org | Docs |
| Selenium with Python | https://selenium-python.readthedocs.io | Docs |

## Best Practices (Updated 2026)
1. **Async-first scraping** — Migrate to `AsyncCrawlerProcess` and avoid Twisted callback chains. Use Scrapy's native async for >10k pages.
2. **Selenium for auth flows only** — Use `scrapy-playwright` or Crawlee for JS-rendered sites; keep Selenium only for login/MFA where Playwright fails.
3. **Dead-letter scraping logs** — Store raw HTML and parse failures for later reprocessing instead of silent drops.
4. **DRF permissions** — Restrict scraping control APIs to admin users; do not expose queue endpoints publicly.

## Common Pitfalls
| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Mixing Selenium and Scrapy state | Flaky pipeline coupling | Use async task boundaries with retries |
| Blind `time.sleep` waits | Slow scrapes and timeouts | Replace with explicit waits and expect conditions |

## Performance Targets
| Metric | Target | Method |
|--------|--------|--------|
| Scrapy concurrent requests | 16-50 per domain | `CONCURRENT_REQUESTS=16`, tune via queue depth |

## Security Checklist
1. **Sanitize all scraped HTML/JSON** before render or storage (prevent stored XSS)
2. **Restrict DRF endpoints** to authenticated staff; no unauthenticated crawl triggers
3. **Avoid hardcoded target URLs** — load from signed configuration or admin UI

## Related Projects (in workspace)
- **selenium_webdriver** — Browser automation sibling; shared retry + Selenium utilities
- **comicwise** — Upstream consumer of scraped comic data
- **rhixecompany-comics** — Consolidation target inheriting scraping pipeline
- **Django-Scrapy-Selenium** — Mark as consolidation source in downstream reports

## Resources
| Resource | URL | Description |
|----------|-----|-------------|
| Scrapy docs | https://docs.scrapy.org | Framework docs |
| Selenium docs | https://www.selenium.dev/documentation | Browser automation docs |
