# RESEARCH_REPORT.md

## Project: Django-Scrapy-Selenium

**Type:** Web scraping + automation platform  
**Tech Stack:** Python 3.10+, Django 4.x, Django REST Framework, Scrapy, Selenium WebDriver, BeautifulSoup4, Celery + Redis/RabbitMQ, PostgreSQL, Tailwind CSS (Webpack), Docker Compose, Gunicorn  
**Status:** Consolidation target (scraping pipeline consolidated into `projects/rhixecompany-comics`)

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| selenium_webdriver | `projects/selenium_webdriver` | Browser automation sibling; shared ChromeDriver and retry patterns |
| rhixecompany-comics | `projects/rhixecompany-comics` | Consolidation target inheriting scraping pipeline |
| comicwise | `projects/comicwise` | Upstream consumer of scraped comic data |

---

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

**Selenium Problems in 2026:**
- Detectable WebDriver signature → highest block rate (13/100 in benchmarks)
- Slow — 1.42s per page vs 0.08s (Requests) / 0.47s (Playwright)
- High memory — 1.2 GB peak for 100 pages
- No native async — poor concurrency
- Maintenance burden — driver version management

**Selenium Manager (4.6+):** Auto-resolves driver binaries; no more manual ChromeDriver pins [ScrapingBee]. Still requires real browser installed.

**Anti-Detect Browsers:** Modern anti-bot systems evaluate combinations of IP, cookies, user-agent, screen resolution, timezone, fonts, WebGL, Canvas fingerprints. Anti-detect browsers provide isolated profiles with consistent, realistic fingerprints [GoLogin]. Top options:
- **GoLogin** — Proprietary Orbita Chromium, cloud + local API, Puppeteer/Playwright/Selenium support, ~$24/mo Pro
- **Multilogin** — Deep manual fingerprint control (Canvas, WebGL, fonts), €99/mo Scale
- **Octo Browser** — Real-device fingerprint database, €29/mo Starter
- **AdsPower** — RPA + basic API, $9/mo Base
- **Dolphin{Anty}** — Free 10 profiles, ~$10/mo paid

**undetected-chromedriver:** GitHub project for TLS fingerprint/anti-bot bypass, used in production scraping systems [Reddit].

### 3. Celery + Redis/RabbitMQ Production Patterns (2026)

**Broker Choice:** Use Redis if Django already uses Redis for caching/sessions (one fewer infrastructure component). Use RabbitMQ for complex routing, better durability guarantees, acknowledgment semantics surviving broker restarts [Medium @mmoznu].

**Separate Redis Databases:**
```python
CELERY_BROKER_URL = env('REDIS_URL') + '/0'  # Celery broker
CELERY_RESULT_BACKEND = env('REDIS_URL') + '/1'  # Celery results
CACHES = {'default': {'LOCATION': env('REDIS_URL') + '/2'}}  # App cache
```

**Queue Architecture — Critical Decision:** Single default queue is a reliability risk. Define separate queues by priority/type:
```python
CELERY_TASK_QUEUES = {
    'critical': {'exchange': 'critical', 'routing_key': 'critical'},
    'default': {'exchange': 'default', 'routing_key': 'default'},
    'bulk': {'exchange': 'bulk', 'routing_key': 'bulk'},
}
CELERY_TASK_ROUTES = {
    'tasks.send_password_reset': {'queue': 'critical'},
    'tasks.process_webhook': {'queue': 'default'},
    'tasks.generate_report': {'queue': 'bulk'},
}
```
Run separate worker processes per queue with appropriate concurrency [Medium].

**Monitoring & Observability:**
- Queue depth alerts: Monitor Redis queue lengths, alert when growing faster than processing [Medium]
- Celery Inspect API: `i.scheduled()`, `i.active()`, `i.reserved()`, `i.registered()` [Stack Overflow]
- RabbitMQ: `rabbitmqctl list_queues` for message counts
- Redis: `redis-cli LLEN celery` for queue length, `lrange` to view tasks
- Priority queues: Celery separates priorities into different Redis keys (requires summing across priority steps)

**Task Patterns That Hold Up:**
1. **Idempotency first** — Celery delivers at-least-once, not exactly-once. Check processed status before work [Medium]
2. **Pass IDs, not objects** — Fetch fresh from DB inside task to avoid stale data [Medium]
3. **Bind tasks for retry logic** — Use `bind=True`, `max_retries`, exponential backoff `countdown=2 ** self.request.retries` [Medium]
4. **Don't retry forever** — Set `max_retries=5`, `autoretry_for=(Exception,)`, dead-letter queues for poison pills

### 4. Robots.txt Compliance & Rate Limiting (2026)

**Legal Landscape:** 2022 Supreme Court (*Van Buren v. United States*) and Ninth Circuit (*hiQ v. LinkedIn*) established scraping publicly accessible data is not a CFAA violation [dev.to/agenthustler]. However, respect robots.txt, ToS, GDPR, CCPA.

**Robots.txt in 2026:** Voluntary, non-enforceable protocol from 1994. Modern AI scrapers often ignore it. Emerging alternatives: **AI.txt** and **LLMs.txt** — plain text/Markdown files at site root defining which AI systems can access content for model training [cookie-script.com].

**Best Practices for Ethical Scraping [Dexodata, dev.to]:**
- Always check and honor `robots.txt` (`example.com/robots.txt`)
- Add random delays: `time.sleep(random.uniform(2, 5))` between requests
- Rotate user agents to appear as multiple users
- Use rotating proxies to distribute load and respect rate limits
- Implement retry logic with exponential backoff
- Minimum 1-3 second delays; hammering 100 req/sec → instant IP ban
- Handle 429 (Too Many Requests) with exponential backoff

**Proxy Strategy:** Residential proxies = lowest detection risk for protected sites; mobile proxies = highest trust for social media; datacenter = speed-critical tasks. Quality residential proxies = highest success rates [Dexodata].

### 5. BeautifulSoup4 vs Scrapy Selector Performance (2026 Benchmarks)

**Benchmark Result:** Scrapy outperformed standard BeautifulSoup scripts by **39x** in controlled tests (1,000 pages on AWS EC2 t3.medium) [hasdata.com].
| Architecture | Stack | Time (1000 pages) | Speed |
|--------------|-------|-------------------|-------|
| **Async Framework** | **Scrapy** | **24.41s** | **~41 pages/sec** |
| Sync (Blocking) | BS4 + Requests | 954.29s (~16 min) | ~1 page/sec |
| Threaded | BS4 + ThreadPool | 120.63s (~2 min) | ~8.3 pages/sec |
| Custom Async | BS4 + aiohttp | 17.79s | ~56 pages/sec |

**Why Scrapy Wins:** Non-blocking event loop (Twisted) fires requests concurrently, keeping dozens in flight. BS4 + Requests blocks on each request — CPU idle 90% waiting for network I/O.

**The "Unfair Comparison" Nuance:** BS4 + aiohttp + asyncio (custom async) was actually faster than Scrapy (17.79s vs 24.41s) due to lacking Scrapy's middleware overhead. But achieving this requires manually building: event loop management, semaphore logic, error handling/retry logic, data export handlers. Scrapy gives 90% of that performance with zero boilerplate [hasdata.com].

**When to Use Each:**
- **BeautifulSoup:** Targeted extraction, quick prototyping, learning fundamentals, <100 pages, messy HTML parsing [cloro.dev]. 43.5% adoption among Python developers.
- **Scrapy:** ETL pipelines, >10k pages, data products, large-scale crawling (millions of pages), mature middleware ecosystem [hasdata.com, use-apify.com].
- **Crawlee (Apify):** New projects targeting modern SPAs — built-in Playwright, fingerprinting, proxy rotation, session management [use-apify.com].

### 6. Django REST Framework + Scraping Control APIs

**Security Patterns:** Restrict scraping control APIs to admin users; do not expose queue endpoints publicly [existing report]. Use DRF permissions (`IsAdminUser`, custom permissions) for crawl triggers.

**Task Schema Design:** Celery tasks should include `status`, `started_at`, `finished_at`, `source_repo`, `payload_ref` for observability [existing report + Medium].

**Sanitization:** Sanitize all scraped HTML and JSON before render or storage to prevent stored XSS [existing report].

### 7. Frontend Dashboard Modernization

**Current Stack:** Tailwind CSS + Webpack manual build. Consider migrating to Next.js dashboard for richer telemetry visualizations if scraping surface needs it [existing report]. Next.js provides server-side rendering, built-in API routes, and better developer experience for real-time scraping metrics.

### 8. Docker Compose Production Deployment

**Multi-Service Architecture:**
```yaml
services:
  web:
    image: myapp:latest
    command: gunicorn config.wsgi:application --bind 0.0.0.0:8000
    env_file: .env
  
  celery-critical:
    image: myapp:latest
    command: celery -A config worker -Q critical --concurrency=4
    env_file: .env
  
  celery-default:
    image: myapp:latest
    command: celery -A config worker -Q default --concurrency=2
    env_file: .env
  
  celery-bulk:
    image: myapp:latest
    command: celery -A config worker -Q bulk --concurrency=1
    env_file: .env
  
  redis:
    image: redis:7-alpine
    volumes: [redis_data:/data]
  
  postgres:
    image: postgres:15
    env_file: .env
    volumes: [postgres_data:/var/lib/postgresql/data]
```
Separate worker services per queue prevent slow tasks from starving critical ones [Medium].

### 9. Monitoring & Alerting Stack

**Queue Health:** Alert on queue depth growth rate, not just absolute size [Medium]. Use `celery inspect` commands or Redis `LLEN` for programmatic monitoring.

**Task Metrics:** Track task duration, success/failure rates, retry counts per task type. Celery Flower or custom Prometheus exporters for metrics collection.

**Scraping-Specific Metrics:** Pages/sec, success rate by domain, proxy health, CAPTCHA encounter rate, robots.txt compliance violations.

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Scrapy docs | https://docs.scrapy.org | Docs |
| Selenium with Python | https://selenium-python.readthedocs.io | Docs |
| Celery docs | https://docs.celeryq.dev | Docs |
| DRF docs | https://www.django-rest-framework.org | Docs |
| BeautifulSoup docs | https://www.crummy.com/software/BeautifulSoup/bs4/doc | Docs |
| Playwright Python | https://playwright.dev/python | Docs |
| Celery + Django (Real Python) | https://realpython.com/asynchronous-tasks-with-django-and-celery | Tutorial |
| Scrapy vs BS4 Benchmark | https://hasdata.com/blog/scrapy-vs-beautifulsoup | Benchmark |
| Anti-Detect Browsers | https://gologin.com/blog/best-anti-detect-browsers-for-web-scraping | Guide |
| Celery Production Patterns | https://medium.com/@mmoznu/celery-and-django-in-production-the-patterns-that-actually-hold-up-under-real-load-2974fe3fb481 | Article |

---

## Best Practices (Updated 2026)

1. **Async-first scraping** — Migrate to `AsyncCrawlerProcess` and avoid Twisted callback chains. Use Scrapy's native async for >10k pages.
2. **Selenium for auth flows only** — Use `scrapy-playwright` or Crawlee for JS-rendered sites; keep Selenium only for login/MFA where Playwright fails.
3. **Dead-letter scraping logs** — Store raw HTML and parse failures for later reprocessing instead of silent drops.
4. **DRF permissions** — Restrict scraping control APIs to admin users; do not expose queue endpoints publicly.
5. **Separate queues by priority** — Critical/default/bulk queues with dedicated workers prevent starvation.
6. **Idempotent tasks** — Design every Celery task to be safely retried; check processed status before work.
7. **Pass IDs, not objects** — Fetch fresh from database inside task to avoid stale serialized data.
8. **Exponential backoff retries** — `countdown=2 ** self.request.retries` gives external services recovery time.
9. **Respect robots.txt + rate limits** — Random delays (2-5s), rotating proxies, rotating user agents.
10. **Proxy hygiene** — Quality residential proxies for protected sites; never use VPNs or free proxies.
11. **Monitor queue depth** — Alert when queue grows faster than processing capacity.
12. **Sanitize before storage** — Prevent stored XSS from scraped content.

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Mixing Selenium and Scrapy state | Flaky pipeline coupling | Use async task boundaries with retries |
| Blind `time.sleep` waits | Slow scrapes and timeouts | Replace with explicit waits and expect conditions |
| Storing raw secrets for proxies | Credential leak | Load proxy auth from environment only |
| No robots obeyance | Legal or rate-limit risk | Enforce `ROBOTSTXT_OBEY=True` and rate-limit all crawls |
| Single default Celery queue | Slow tasks starve critical ones | Separate queues: critical/default/bulk with dedicated workers |
| Non-idempotent tasks | Duplicate processing on retry | Check processed status before work; use DB constraints |
| Passing ORM objects to tasks | Stale data, serialization issues | Pass IDs only; fetch fresh inside task |
| No queue monitoring | Silent backlog buildup | Alert on queue depth growth rate |
| Ignoring 429 responses | IP ban, service degradation | Exponential backoff + proxy rotation |
| Using Selenium for everything | 39x slower than Scrapy for static sites | Requests/BS4 for static, Playwright for JS, Selenium only for auth |

---

## Performance Targets

| Metric | Target | Method |
|--------|--------|--------|
| Scrapy concurrent requests | 16-50 per domain | `CONCURRENT_REQUESTS=16`, tune via queue depth |
| Pages/second (Scrapy) | 25-50+ | Async event loop, proper concurrency |
| Celery task latency (critical) | <100ms queue time | Dedicated critical queue, 4+ workers |
| Celery task latency (bulk) | <5s queue time | Dedicated bulk queue, 1 worker |
| Redis memory per 10k tasks | ~50MB | Separate DBs for broker/results/cache |
| Proxy success rate | >95% | Residential rotation, health checks |
| Scraping success rate | >90% | Retry logic, anti-detect, proper delays |

**Scaling Pattern:** Separate Celery queues by source site so one slow domain cannot block others. Run Scrapy `CONCURRENT_REQUESTS=16` with domain parallelism. Use Redis caching for repeated anti-bot solutions (Cloudflare challenge tokens). Keep Docker images lean and reuse layers across Django + Scrapy + Selenium services.

---

## Security Checklist

1. **Sanitize all scraped HTML/JSON** before render or storage (prevent stored XSS)
2. **Restrict DRF endpoints** to authenticated staff; no unauthenticated crawl triggers
3. **Avoid hardcoded target URLs** — load from signed configuration or admin UI
4. **Validate all uploads/outputs** when exercising Selenium upload flows
5. **Load proxy auth from environment only** — never store in code or DB
6. **Use separate Redis DBs** for broker, results, cache (isolation)
7. **Implement rate limiting** on crawl trigger APIs (prevent DoS via scraping)
8. **Audit robots.txt compliance** — log violations, alert on pattern
9. **Rotate user agents and proxies** — prevent fingerprinting
10. **Use PostgreSQL for production** — handle high write throughput from scrapers

---

## Related Projects (in workspace)

- **selenium_webdriver** — Browser automation sibling; shared retry + Selenium utilities
- **comicwise** — Upstream consumer of scraped comic data
- **rhixecompany-comics** — Consolidation target inheriting scraping pipeline
- **Django-Scrapy-Selenium** — Mark as consolidation source in downstream reports

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Scrapy docs | https://docs.scrapy.org | Framework docs |
| Selenium docs | https://www.selenium.dev/documentation | Browser automation docs |
| Celery docs | https://docs.celeryq.dev | Task queue |
| DRF docs | https://www.django-rest-framework.org | API framework |
| Playwright | https://playwright.dev | Modern browser automation |
| Crawlee (Apify) | https://crawlee.dev | Unified HTTP + browser scraping |
| undetected-chromedriver | https://github.com/ultrafunkamsterdam/undetected-chromedriver | Anti-detection ChromeDriver |
| GoLogin | https://gologin.com | Anti-detect browser platform |
| Dexodata Proxies | https://dexodata.com | Ethical residential/mobile proxies |
| ScraperAPI | https://www.scraperapi.com | Managed scraping API (5K free/mo) |

---

*Report updated: 2026-06-17*  
*Sources: 5 web searches × 3 extractions each = 15 primary sources covering Scrapy/Django/Celery integration, Selenium anti-detection, Celery production patterns, robots.txt/rate limiting, and BS4 vs Scrapy benchmarks.*