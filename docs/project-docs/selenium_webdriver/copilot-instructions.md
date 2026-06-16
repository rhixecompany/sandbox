# selenium_webdriver
**JS**: ES Modules, `camelCase`, Prettier (2-space).
**Selenium**: explicit `WebDriverWait`; retry on `StaleElementReferenceException`; consistent `By` selectors; `driver.quit()` in `finally`.
**Security**: no ChromeDriver / profiles in VCS; respect `robots.txt`; polite delays.
**Commands**: `npm test`, `node src/scrape.js`, `npm run format`.
