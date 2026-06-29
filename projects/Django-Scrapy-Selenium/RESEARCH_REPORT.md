# RESEARCH_REPORT — Django-Scrapy-Selenium

> **Type:** Project research report | **Updated:** 2026-06-25

---

**Type:** Django-based web scraping platform
**Tech Stack:** Django 4.x, DRF, Scrapy, Selenium, BeautifulSoup4, Celery + Redis/RabbitMQ, PostgreSQL
**Status:** Active (legacy — scraping consolidated to rhixecompany-comics)

---

## Similar Projects

| Project | URL | Why Relevant |
| ------- | --- | ------------ |
| codingforentrepreneurs/Web-Scraping-with-Django-Celery | https://github.com/codingforentrepreneurs/Web-Scraping-with-Django-Celery | Reference — Django + Celery scraping scheduler |
| scrapingbee/selenium-python | https://www.scrapingbee.com/blog/selenium-python | Modern Selenium scraping guide (2026) |

---

## Key Findings

### Scrapy + Django Integration

- Scrapy spiders work best as standalone components called from Celery tasks, not tightly coupled to Django views (medium.com/@yasykur_rafii)
- Django ORM can be used inside Scrapy pipelines for direct data persistence without intermediate files
- Celery beat schedules periodic scraping runs; `django-celery-beat` provides DB-backed periodic task management (oneuptime.com, 2026)

### Selenium Anti-Detection

- Selenium's `navigator.webdriver` flag is the primary detection vector — use `SeleniumBase` or `undetected-chromedriver` to bypass (scrapfly.io, 2026)
- Camoufox (Firefox-based stealth browser) and `playwright-stealth` are the top Python anti-detection tools in 2026 (scrapfly.io)
- Headless mode is increasingly detected; using headed mode or headful disguises reduces blocking (scrapingbee.com, 2026)

### Celery Monitoring

- Redis is the fastest and most common Celery broker; RabbitMQ offers stronger durability guarantees (oneuptime.com, 2026)
- `django-celery-results` stores task results in the database for inspection via Django Admin
- Flower (real-time Celery monitor) is the recommended dashboard for worker/task monitoring in production

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
| ----- | -------- | ---- |
| Celery + Django | https://oneuptime.com/blog/post/2026-01-26-django-celery-background-tasks/ | Guide |
| Selenium scraping | https://www.scrapingbee.com/blog/selenium-python | Tutorial |
| Anti-detection tools | https://scrapfly.io/blog/posts/best-anti-bot-bypass-tools | Guide |

---

## Best Practices

1. **Robots.txt compliance** — Check and respect `robots.txt` before spidering any site
2. **Rate limiting** — Add `DOWNLOAD_DELAY` and `AUTO_THROTTLE` in Scrapy settings; user-agent rotation mandatory
3. **Data sanitization** — Clean scraped data before persistence to prevent XSS in dashboards
4. **Separate concerns** — Scrapy spiders in `crawler/spiders/`, Celery tasks in `tasks.py`, views in separate apps

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
| ------- | ------ | --------- |
| Missing User-Agent rotation | IP blocking | Use Scrapy's `RotatingUserAgentMiddleware` |
| No rate limiting | Site overload / ban | Configure `DOWNLOAD_DELAY` + `CONCURRENT_REQUESTS` |
| Selenium `webdriver` flag detected | Anti-bot CAPTCHA | Use `undetected-chromedriver` |
| Celery broker not running | Tasks silently lost | Always verify Redis/RabbitMQ is up |

---

## Performance

1. **Scrapy vs Selenium** — Use Scrapy for static content; Selenium only when JS rendering is needed
2. **Celery worker concurrency** — Set `--concurrency=4` per worker, increase worker count for more throughput
3. **BeautifulSoup4 vs lxml** — lxml parser is 3–5x faster than Python's html.parser for DOM parsing
4. **Async scraping** — Scrapy's `Twisted` reactor handles concurrent requests efficiently without thread overhead

---

## Security

1. **Sanitize scraped data** — Always escape/clean before storage or display (XSS prevention)
2. **Proxy rotation** — Use residential proxies to avoid IP-based blocking at scale
3. **Celery task validation** — Validate task parameters; never execute user-supplied URLs without sanitization
4. **Headless detection** — Keep Selenium browser detection mitigation up to date (evolves with anti-bot tech)

---

## Related Projects (in workspace)

- **rhixecompany-comics** — Scraping functionality consolidated here; same Scrapy + Selenium + Celery pattern
- **profile** — Shares Django + PostgreSQL stack

---

## Resources

| Resource | URL | Description |
| -------- | --- | ----------- |
| Scrapy Docs | https://docs.scrapy.org/ | Scrapy framework documentation |
| Selenium Docs | https://www.selenium.dev/documentation/ | Browser automation docs |
| Celery Docs | https://docs.celeryq.dev/ | Celery task queue docs |
| Anti-bot tools | https://scrapfly.io/blog/posts/best-anti-bot-bypass-tools | 2026 anti-detection comparison |

---