# Architecture — rhixecompany-comics

## System Overview

Rhixecompany Comics is a consolidated full-stack comics platform. The target design combines a Django backend with a Next.js 16 frontend and preserves the scraping/automation patterns inherited from the source repositories.

## Layers

### Presentation Layer
- Next.js App Router pages and layouts
- Server components by default
- Tailwind CSS for styling
- Metadata lives in `frontend/src/app/layout.tsx`

### API Layer
- Django + DRF
- A simple health endpoint is present now
- Future comic, user, and reading-list endpoints can be layered under `backend/apps/api/`

### Domain / Service Layer
- `backend/apps/comics/` for catalog, chapters, and reading state
- `backend/apps/users/` for profiles and authentication flows
- `backend/apps/core/` for cross-cutting API utilities and health checks

### Scraping Layer
- `backend/apps/scraping/` reserves the Django-side home for Scrapy spiders and Selenium-backed browser tasks
- Selenium automation patterns come from `projects/selenium_webdriver`
- Django/Celery scheduling patterns come from `projects/Django-Scrapy-Selenium`

### Infrastructure Layer
- PostgreSQL-compatible settings in `backend/config/settings.py`
- Redis-backed Celery broker/result settings
- Static/media paths are explicit and environment-driven

## Data Flow

```text
Browser -> Next.js frontend -> Django API -> Domain apps -> Database / external services
                                \-> Scraping workers -> External comic sources
```

## Current State

The repository now has a functional scaffold: backend entry point, Django settings, a health endpoint, and a minimal frontend shell. The remaining work is feature-level growth, not project bootstrapping.
