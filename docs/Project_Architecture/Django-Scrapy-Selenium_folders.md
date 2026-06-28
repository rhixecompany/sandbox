# Django-Scrapy-Selenium — Folder Structure

```
Django-Scrapy-Selenium/
├── api/                  # REST API application
├── compose/              # Docker Compose configs
├── config/               # Django project settings
├── crawler/              # Scrapy spiders and pipelines
├── docs/                 # Documentation
├── fixtures/             # Database fixtures
├── locale/               # Internationalization
├── requirements/         # Split requirement files
├── tests/                # Test suite
├── webpack/              # Frontend asset bundling
├── manage.py             # Django management CLI
├── justfile              # Task runner
├── Makefile              # Build automation
├── pyproject.toml        # Python project config
├── tsconfig.json         # TypeScript config
├── tailwind.config.cjs   # Tailwind CSS config
├── postcss.config.cjs    # PostCSS config
├── package.json          # Node.js dependencies
└── docker-compose.*.yml  # Docker Compose environments
```

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `crawler/` | Scrapy spider definitions, item pipelines, middlewares |
| `api/` | Django REST Framework serializers and viewsets |
| `config/` | Django settings, URLs, WSGI/ASGI configuration |
| `compose/` | Docker Compose files for local/production |
| `requirements/` | Split: base, local, production |
