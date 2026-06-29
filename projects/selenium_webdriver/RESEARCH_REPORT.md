# RESEARCH_REPORT.md

## Project: selenium_webdriver

**Type:** Node.js Selenium WebDriver web scraper
**Tech Stack:** Node.js 18+, selenium-webdriver 4.x, ChromeDriver, ES Modules, Prettier
**Status:** Consolidation target (patterns extracted → rhixecompany-comics)

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| Scrapy | https://scrapy.org | Python-based scraping alternative |
| Playwright | https://playwright.dev | Modern browser automation with better DX |
| puppeteer | https://pptr.dev | Headless Chrome without WebDriver |

## Key Findings

### Selenium 4.x Best Practices (2026)
- Explicit `WebDriverWait` + retry-on-stale is the industry-standard pattern (selenium.dev/documentation)
- Selenium Manager auto-manages ChromeDriver binaries — no manual downloads needed (v4.11+)
- `--headless=new` uses the same rendering engine as headed mode, reducing discrepancies (chromium.org)

### Stale Element Handling
- StaleElementReferenceException occurs when DOM re-renders between location and interaction
- Re-finding the element before each action is the prescribed fix — never cache references across navigations
- The project's retry wrapper is the canonical pattern for production scrapers

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Selenium WebDriver JS | https://www.selenium.dev/documentation/webdriver/ | Official Docs |
| WebDriver Wait Patterns | https://www.selenium.dev/documentation/webdriver/waits/ | Guide |
| Headless Chrome | https://developer.chrome.com/docs/chromium/new-headless | Setup Guide |

## Best Practices

1. **Explicit waits over sleep()** — The project correctly uses `until.elementLocated()` exclusively
2. **Retry-on-stale pattern** — Industry-standard approach for dynamic DOMs
3. **Isolated browser profiles** — Fresh Chrome user-data-dir per run prevents state leaks
4. **Guaranteed cleanup** — `driver.quit()` in `finally` block prevents memory leaks
5. **`setPageLoadStrategy("eager")`** — Stops on DOMContentLoaded, significantly faster scraping

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| XPath class-match brittleness | Scraper breaks on minor CSS changes | Use `contains(@class, ...)` instead of exact match |
| Code duplication across scrape files | Maintenance burden, drift risk | Extract shared `driver.js` module |
| No rate limiting | IP bans, server load | Add inter-request delay (`driver.sleep()`) |
| String-based error type checks | Fragile across locales | Use `instanceof` checks from selenium-webdriver |

## Performance

1. **`--headless=new`** renders at full speed without GPU overhead
2. **`setPageLoadStrategy("eager")** cuts page load time by ignoring sub-resources
3. **Retry wrapper** adds worst-case 500ms per element — optimize by reducing maxRetries
4. **Parallel sessions** possible with multiple driver instances for batch scraping
5. **Chrome profile isolation** adds ~200ms per run — acceptable for production scrapers

## Security

1. **Respect robots.txt** — Currently no check against target site's scraping policy
2. **Rate limiting** — Add delays between requests to avoid being classified as a DoS attack
3. **Chrome profile cleanup** — Already handled via `fs.rmSync` in finally block
4. **Anti-detection** — `excludeSwitches("enable-automation")` is good practice

## Related Projects (in workspace)

- **Django-Scrapy-Selenium** — Python-based scraping with Selenium, shares retry-on-stale patterns
- **rhixecompany-comics** — Consolidation target for scraping capabilities
- **comicwise** — Shares Stripe/PayPal payment patterns with the target site

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Selenium WebDriver Docs | https://www.selenium.dev/documentation/webdriver/ | Official documentation |
| ChromeDriver | https://chromedriver.chromium.org | ChromeDriver downloads & setup |
| Selenium Manager | https://www.selenium.dev/blog/2022/introducing-selenium-manager/ | Auto driver management |
