# Django-Scrapy-Selenium — Contributing Guide

## How to Contribute

We welcome contributions! Follow these guidelines to ensure quality.

## Quick Start

```bash
git clone <repo-url>
cd api
python -m venv venv
source venv/bin/activate
pip install -r requirements/local.txt
npm install
python manage.py migrate
python manage.py runserver
```

## Development Process

1. **Fork and branch** from `main`
2. **Set up environment** (see SETUP_GUIDE.md)
3. **Make changes** following project conventions
4. **Run quality checks**:
   ```bash
   ruff check .
   black --check .
   mypy api/
   pytest
   npm run lint
   ```
5. **Test your changes** — add tests for new spiders/scrapers
6. **Submit a PR** with clear description

## Code Standards

### Python
- **Style**: Black (line length 88), Ruff linting
- **Typing**: Type hints for all functions
- **Django**: Follow Django best practices
- **Scrapy**: Follow Scrapy spider conventions
- **Tests**: pytest with factory_boy

### JavaScript
- **Formatting**: Prettier with tailwindcss plugin
- **Linting**: ESLint with TypeScript config
- **Framework**: Alpine.js patterns (no heavy frameworks)

### Scrapy Spiders
- Name spiders descriptively
- Use `allowed_domains` to prevent unwanted crawling
- Respect `robots.txt` in production
- Implement polite crawl delays (`DOWNLOAD_DELAY`)

## Adding a New Spider

1. Create `scraping/spiders/new_spider.py`
2. Define `name`, `allowed_domains`, `start_urls`
3. Implement `parse()` method
4. Add item pipeline if needed
5. Add to spider list in settings
6. Write tests for spider output

## Commit Convention

```
feat(scraping): add manga reader spider
fix(selenium): resolve ChromeDriver timeout
docs: update deployment guide for Docker
chore: upgrade Scrapy to 2.12
test: add pipeline processing tests
```

## Testing

```bash
pytest                          # All Python tests
pytest scraping/tests/          # Scrapy-specific tests
pytest selenium_scraper/tests/  # Selenium-specific tests
npm test                        # Frontend tests (if any)
```

## Questions?

Open a [GitHub Issue](https://github.com/your-org/django-scrapy-selenium/issues).
