# Django-Scrapy-Selenium — Testing Guide

## Test Framework

| Layer | Tool | Scope |
|-------|------|-------|
| Python Unit Tests | pytest + pytest-django | Models, views, forms |
| Scrapy Tests | pytest + scrapy testing utilities | Spider output, pipelines |
| Selenium Tests | pytest + Selenium WebDriver | Browser scraping |
| Frontend Tests | ESLint + manual | JS components |

## Running Tests

```bash
# All Python tests
pytest

# With coverage
coverage run -m pytest
coverage html
open htmlcov/index.html

# Specific test modules
pytest scraping/tests/
pytest selenium_scraper/tests/
pytest api/tests/

# Verbose output
pytest -v

# Run tests matching keyword
pytest -k "spider"
```

## Test Structure

```
api/
├── scraping/
│   └── tests/
│       ├── test_spiders.py       # Spider parsing tests
│       ├── test_pipelines.py     # Pipeline processing
│       └── test_middlewares.py    # Middleware behavior
├── selenium_scraper/
│   └── tests/
│       ├── test_scraper.py       # Scraper functionality
│       └── test_drivers.py       # WebDriver management
├── config/
│   └── tests/                    # Django project tests
└── users/
    └── tests/                    # User model tests
```

## What to Test

### Scrapy Spiders
- Spider parses HTML correctly
- Items contain expected fields
- Pagination/navigation logic works
- Edge cases: empty pages, missing elements, redirects

### Pipelines
- Items saved correctly to database
- Duplicate handling (update vs create)
- Data transformation (cleanup, normalization)

### Selenium Scraper
- Initialization and teardown
- JavaScript-rendered content extraction
- Wait conditions for dynamic elements
- Error handling for timeouts

### Django Views
- Page loads with correct status code
- htmx endpoints return partial HTML
- Authentication checks for protected views
- Form validation

### Celery Tasks
- Tasks execute without error
- Task retry on failure
- Task result persistence

## Mocking External Services

```python
# Example: Mocking HTTP requests in Scrapy tests
from scrapy.http import HtmlResponse

def test_spider_parse():
    spider = ComicSpider()
    response = HtmlResponse(
        url="https://example.com",
        body=open("fixtures/page.html").read(),
        encoding="utf-8",
    )
    results = list(spider.parse(response))
    assert len(results) == 20
    assert results[0]["title"] is not None
```

## CI Integration

```yaml
# .github/workflows/ci.yml
- name: Python Tests
  run: |
    pytest
    coverage run -m pytest

- name: Frontend Lint
  run: |
    npm run lint
```
