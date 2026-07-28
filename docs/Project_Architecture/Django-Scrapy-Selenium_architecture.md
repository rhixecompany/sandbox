# Django-Scrapy-Selenium Architecture

**Generated:** 2026-07-28  
**Project Type:** Python/Django (Full Stack)  
**Architecture Pattern:** Django MVT + Scrapy + Selenium + Next.js frontend

## Overview

Full-stack web scraping platform with Django REST API, Scrapy spiders, Selenium JS rendering, and Next.js frontend.

## Technology Stack

Django 5, Python 3.11, Scrapy, Selenium, Next.js, TypeScript, PostgreSQL, Docker

## Source Layout

api/, config/, crawler/, compose/

## Architecture Diagram

```mermaid
graph TD
    subgraph "Django-Scrapy-Selenium"
        MAIN[Main Entry Point]
        SRC[Source Code]
        BUILD[Build System]
    end
    subgraph "Dependencies"
        DEPS[Package Dependencies]
        EXT[External Services]
    end
    MAIN --> SRC
    SRC --> BUILD
    BUILD --> DEPS
    SRC --> EXT
```

## Key Patterns

- **Django MVT + Scrapy + Selenium + Next.js frontend**
- Version control: Shared monorepo git

## Cross-Cutting Concerns

- **Linting/Formatting:** Aligned with workspace root configs (ESLint, Prettier, Ruff)
- **Documentation:** AGENTS.md + standard doc files per project convention
- **Dependencies:** Managed via project-specific package manager

## Related Documents

- [Folder Structure](./Django-Scrapy-Selenium_folders.md)
- [Technology Stack](./Django-Scrapy-Selenium_techstack.md)
