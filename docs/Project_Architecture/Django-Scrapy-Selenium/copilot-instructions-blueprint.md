# GitHub Copilot Instructions — Django-Scrapy-Selenium

## Priority Guidelines

When generating code for this repository:

1. **Version Compatibility**: Always detect and respect the exact versions of languages, frameworks, and libraries used in this project
2. **Context Files**: Prioritize patterns and standards defined in the .github/copilot directory
3. **Codebase Patterns**: When context files don't provide specific guidance, scan the codebase for established patterns
4. **Architectural Consistency**: Maintain our **Monolithic (with async task queue)** architectural style and established boundaries
5. **Code Quality**: Prioritize **maintainability, performance, and testability** in all generated code

## Technology Version Detection

Before generating code, scan the codebase to identify:

1. **Language Versions**: Detect the exact versions of programming languages in use
   - **Python** — check `pyproject.toml` (Python 3.12) and `runtime.txt`
   - **JavaScript** — check `package.json` for frontend tooling
   - **TypeScript** — check `tsconfig.json` if present

2. **Framework Versions**: Identify the exact versions of all frameworks
   - **Django 4.x** — check `pyproject.toml` and requirements
   - **Django REST Framework** — check installed apps
   - **Scrapy** — check `scrapy.cfg` and spider configurations
   - **Selenium WebDriver** — check for WebDriver usage patterns
   - **Celery** — check Celery configuration for async task queue
   - **Tailwind CSS** — check `tailwind.config.cjs`

3. **Library Versions**: Note the exact versions of key libraries and dependencies
   - **Redis/RabbitMQ** for Celery broker
   - **BeautifulSoup4** for HTML parsing
   - **Webpack** for frontend asset bundling
   - **PostgreSQL** (production), SQLite (dev)

## Context Files

Prioritize the following files in .github/copilot directory (if they exist):

- **architecture.md**: System architecture guidelines
- **tech-stack.md**: Technology versions and framework details
- **folder-structure.md**: Project organization guidelines

## Codebase Scanning Instructions

When context files don't provide specific guidance:

1. Identify similar files to the one being modified or created
2. Analyze patterns for:
   - **Scrapy spiders**: Item definitions, pipelines, middlewares, settings
   - **Selenium scripts**: WebDriverWait patterns, retry logic for stale elements
   - **Django views**: Class-based views preferred over function-based
   - **Celery tasks**: Task definitions in `tasks.py` per app
   - **Frontend**: Webpack bundle with Tailwind CSS
3. Follow the most consistent patterns found in the codebase
4. When conflicting patterns exist, prioritize patterns in newer files or files with higher test coverage
5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

- Write self-documenting code with clear naming
- Follow Django coding conventions and PEP 8
- Respect `robots.txt` in Scrapy spiders
- Implement rate limiting and user-agent rotation in scrapers
- Use explicit WebDriverWait in Selenium (avoid time.sleep)

## Documentation Requirements

- Match the level and style of comments found in existing code
- Document according to patterns observed in the codebase
- Follow existing patterns for documenting non-obvious behavior

## Testing Approach

- Match the exact structure and style of existing tests
- **Django tests**: `python manage.py test` or pytest
- **Scrapy contract tests**: `scrapy check spider_name`
- Follow existing patterns for test organization

## Technology-Specific Guidelines

### Python/Django
- Follow Django conventions for models, views, URLs, and templates
- Use Django REST Framework ViewSets + Serializers for API endpoints
- Django ORM for database queries (avoid raw SQL)

### Scrapy
- Follow Scrapy spider conventions (items, pipelines, middlewares, settings)
- Define items in `items.py`, pipelines in `pipelines.py`
- Respect `robots.txt` and implement polite crawling delays

### Selenium
- Use explicit WebDriverWait patterns (not implicit waits or sleep)
- Handle StaleElementReferenceException with retry logic
- Clean up with `driver.quit()` in finally blocks

### Celery
- Define tasks in `tasks.py` per Django app
- Use Redis/RabbitMQ as message broker
- Handle task failures with retries

## Version Control Guidelines

- Follow Semantic Versioning patterns as applied in the codebase
- Match existing patterns for documenting breaking changes

## General Best Practices

- Follow naming conventions exactly as they appear in existing code
- Match code organization patterns from similar files
- Apply error handling consistent with existing patterns
- Never commit `.env` or secrets files
- Django SECRET_KEY must be in environment, never in code

## Project-Specific Guidance

- Scan the codebase thoroughly before generating any code
- Respect existing architectural boundaries without exception
- Full-stack web scraping platform combining Django with frontend tooling
- Scrapy spider management with Selenium browser automation
- Celery task queue for async scraping tasks
- Tailwind-styled dashboard with Webpack
- Deploy via Docker Compose (Django + PostgreSQL + Redis + Celery)
