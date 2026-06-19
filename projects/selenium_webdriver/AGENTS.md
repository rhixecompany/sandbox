# selenium_webdriver — Chrome Scraper
## Architecture

- **Blueprint**: [selenium_webdriver Architecture](../docs/Project_Architecture/selenium_webdriver_architecture.md)
- **Folders**: [selenium_webdriver Folder Structure](../docs/Project_Architecture/selenium_webdriver_folders.md)
- **Tech Stack**: [selenium_webdriver Technology Stack](../docs/Project_Architecture/selenium_webdriver_techstack.md)
- **Stack Type**: Node.js


Node.js 18+ Selenium scraper for comics/manga (JS modules).

## Stack
- `selenium-webdriver` 4.x + ChromeDriver
- Prettier (2-space), ES Modules
- Manual testing via `node src/scrape.js`

## Commands
```bash
npm install
npm test               # runs scrape.js
node src/scrape.js
npm run format
```

## Patterns
- Explicit `WebDriverWait`; never sleeps
- Retry on `StaleElementReferenceException`
- Consistent `By` selectors
- `driver.quit()` in `finally`

## Notes
- No build step; no deployment
- No ChromeDriver/profiles in VCS
- `robots.txt` + polite delays
