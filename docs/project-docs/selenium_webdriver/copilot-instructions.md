# Copilot Instructions — selenium_webdriver

## JavaScript Style
- ES Modules (import/export)
- camelCase for files and functions
- Prettier with 2-space indentation

## Selenium Patterns
- Always use explicit `WebDriverWait`
- Handle `StaleElementReferenceException` with retry logic
- Use `By` selectors consistently
- Clean up with `driver.quit()` in finally blocks

## Security
- Never commit ChromeDriver binary or browser profiles
- Respect robots.txt
- Implement polite scraping delays

## Commands
- `npm test` - Run main scraper
- `node src/scrape.js` - Run scraper directly
- `npm run format` - Format code
