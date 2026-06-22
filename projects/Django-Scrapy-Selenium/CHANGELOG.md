# Django-Scrapy-Selenium — Changelog

## [0.1.0] — 2026-05-27

### Added
- Django 5.0 project with PostgreSQL database
- Django REST Framework for API endpoints (optional)
- django-allauth for authentication
- Scrapy integration with custom spiders
  - Comic spider for scraping comic listings
  - Chapter spider for scraping chapter content
  - Update spider for checking new content
- Scrapy pipelines for database persistence
- Scrapy middlewares for proxy rotation and user-agent rotation
- Selenium WebDriver integration for JavaScript-rendered pages
  - Headless Chrome support
  - Custom wait conditions
  - Screenshot capability
- Webpack 5 build system with Babel + TypeScript
- Alpine.js 3.14 for reactive frontend components
- htmx 1.9 for server-driven dynamic updates
- Tailwind CSS 3.4 with daisyUI and Flowbite
- Celery + Redis for background task processing
- Scheduled scraping via Celery Beat
- Export functionality (JSON/CSV)
- Search with filtering and pagination
- Django admin integration for managing scraped data
- SweetAlert2 for user notifications
- Select2 for enhanced form inputs
- Docker Compose for local and production deployment
- Heroku deployment configuration
- pytest with coverage reporting
- Ruff and Black for Python code quality
- ESLint and Prettier for JavaScript code quality
- Pre-commit hooks for automated checks

### Security
- Django security middleware (SSL, XSS, CSRF)
- Environment variable management for secrets
- Rate limiting on scrape endpoints
- Selenium in headless mode for server safety
- User authentication for admin operations
