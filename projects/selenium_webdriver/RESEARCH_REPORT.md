# RESEARCH_REPORT.md

## Project: selenium_webdriver

**Type:** Browser automation / scraping utility
**Tech Stack:** Node.js 18+, selenium-webdriver 4.x, ChromeDriver, Prettier
**Status:** Consolidation target

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| Django-Scrapy-Selenium | `projects/Django-Scrapy-Selenium` | Shared browser automation task concerns. |
| rhixecompany-comics | `projects/rhixecompany-comics` | Consolidation target consuming scraping utilities. |

---

## Key Findings

### Selenium 4 Modernization
- Selenium Manager handles driver binaries; remove manual ChromeDriver management from developer setup.
- Prefer WebDriverWait with explicit conditions over delays and implicit waits.

### Node.js Automation Patterns
- Centralize retry and navigation helpers so scraper hacks do not duplicate stale-element handling.
- Keep driver lifecycle in a context manager or try/finally so headless browser processes do not leak.

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Selenium docs | https://www.selenium.dev/documentation | Browser automation docs |
| Selenium Manager | https://www.selenium.dev/documentation/dev_tools/grid/grid_4/how_it_works/#selenium-manager | Driver management |
| Node.js best practices | https://nodejs.org/en/learn/getting-started/an-introduction-to-the-npm-package-manager | Package management |
| Playwright docs | https://playwright.dev | Modern browser automation alternative |

---

## Best Practices
1. Use explicit waits and element checks instead of sleep-based flows.
2. Keep selectors close to page semantics and isolate them from parser data access.
3. Scrape with retries only where necessary; prefer smaller, deterministic fixtures first.
4. Log chrome failures into files for later repro when automation is flaky.

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Hardcoded target URLs | Fragile scraper | Load URLs from config or env. |
| Forgetting driver.quit() | Zombie browser processes | Wrap automation in managed lifecycle. |
| Sleep-based waits | Slow and flaky runs | Replace with WebDriverWait and expected conditions. |
| ChromeDriver version mismatch | Automation failures | Use Selenium Manager or pin compatible driver versions. |

---

## Performance
1. Reuse browser sessions within a scrape batch to avoid repeated browser startup.
2. Use headless facts such as `--disable-dev-shm-usage` to reduce container memory usage during Docker execution.

---

## Security
1. Never commit ChromeDriver binaries or browser profiles.
2. Respect `robots.txt` and implement polite delays between requests.
3. Validate scraped content before posting to shared storage or downstream APIs.

---

## Related Projects (in workspace)

- **Django-Scrapy-Selenium** — shared Selenium + Celery automation concerns
- **rhixecompany-comics** — target where scraping utilities should migrate

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Selenium docs | https://www.selenium.dev/documentation | Browser automation docs |
| Playwright docs | https://playwright.dev | Modern automation alternative |
| ChromeDriver docs | https://chromedriver.chromium.org | Driver management |
| Prettier docs | https://prettier.io | Formatting |
| Node.js docs | https://nodejs.org/docs | Runtime docs |
