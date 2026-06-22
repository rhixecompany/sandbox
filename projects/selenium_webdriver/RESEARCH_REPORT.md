# RESEARCH_REPORT.md

## Project: selenium_webdriver
**Type:** Browser automation / scraping utility
**Tech Stack:** Node.js 18+, selenium-webdriver 4.x, ChromeDriver, Prettier
**Status:** Consolidation target (patterns extracted → rhixecompany-comics)

## Similar Projects
| Project | URL | Why Relevant |
|---------|-----|--------------|
| Django-Scrapy-Selenium | `projects/Django-Scrapy-Selenium` | Shared browser automation task concerns. |
| rhixecompany-comics | `projects/rhixecompany-comics` | Consolidation target consuming scraping utilities. |
| Python-projects | `projects/Python-projects` | Python Selenium + scraping patterns. |

## Key Findings
### Selenium 4 Modernization (Node.js, 2026)
- **Selenium Manager built-in** — handles driver binaries automatically; remove manual ChromeDriver management from developer setup [1]
- **Selenium 4.x architecture** — W3C WebDriver standard; `selenium-webdriver` npm package is official JS bindings [1]
- **ES Modules required** — `"type": "module"` in `package.json`; `import { Builder, By, until } from 'selenium-webdriver'` [2]
- **Node.js 18+** — native `fetch`, test runner, `globalThis`; prefer `--experimental-vm-modules` for Jest [2]
- **Playwright alternative** — faster, built-in waiting, auto-wait, stealth plugins; migration path for new scrapers [3]
### ChromeDriver Headless Anti-Detection (2026)
- **Detection vectors**: `navigator.webdriver`, Chrome headless flags, missing permissions, canvas fingerprint, WebGL vendor [4]

## Cheatsheets & Quick Reference
| Topic | Resource | Type |
|-------|----------|------|
| Selenium JS docs | https://www.selenium.dev/documentation | Official docs |

## Best Practices
1. **Selenium Manager for drivers** — zero-config; `const driver = await new Builder().forBrowser('chrome').build();`
2. **Explicit waits everywhere** — `driver.wait(until.elementLocated(By.css('...')), 10000)`; no `sleep()`
3. **Centralized retry utils** — `safeClick`, `safeGetText`, `safeSendKeys` with 3x stale element retry

## Common Pitfalls
| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Hardcoded target URLs | Fragile scraper | Load URLs from config/env (`process.env.TARGET_URL`) |

## Performance
1. **Session reuse** — single browser session for batch scrape; avoid repeated startup (~3-5s each)
2. **Headless optimizations** — `--disable-dev-shm-usage`, `--disable-extensions`, `--disable-images` (if not needed)

## Security
1. **Never commit ChromeDriver binaries** — Selenium Manager handles; `.gitignore` `chromedriver*`
2. **Respect `robots.txt`** — parse + check before each target; polite delays (2s+)

## Related Projects (in workspace)
- **Django-Scrapy-Selenium** — shared Selenium + Celery automation concerns
- **rhixecompany-comics** — target where scraping utilities should migrate
- **Python-projects** — Python Selenium + scraping patterns

## Resources
| Resource | URL | Description |
|----------|-----|-------------|
| Selenium docs | https://www.selenium.dev/documentation | Browser automation docs |
