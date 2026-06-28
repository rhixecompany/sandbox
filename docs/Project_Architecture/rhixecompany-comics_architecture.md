# rhixecompany-comics — Architecture

## Overview
A dual-stack web platform for comic management and scraping. Combines a Django backend API with a Next.js frontend, sharing a PostgreSQL database with Celery for async tasks.

## Architecture Pattern
- **Type:** Dual-stack Web Platform
- **Pattern:** Two independent stacks (Django + Next.js) sharing a database
- **Async:** Celery + Redis for scraping and background tasks

## Components
- **`backend/`** — Django 4.x + DRF backend API
  - REST API endpoints for comic CRUD
  - Scrapy/Selenium integration for scraping
  - Celery task definitions
- **`frontend/`** — Next.js 16 App Router frontend
  - Server Components by default
  - Client Components for interactivity
  - Material UI components
- **`scripts/`** — Utility scripts
- **`docker-compose.yml`** — Container orchestration

## Cross-Cutting Concerns
- **Database:** PostgreSQL shared across both stacks
- **Async Tasks:** Celery + Redis for scheduled scraping
- **Containerization:** Docker Compose for unified deployment
- **Heritage:** Scraping functionality consolidated from `projects/Django-Scrapy-Selenium`

## Data Flow
1. Frontend (Next.js) serves UI, calls backend API
2. Backend (Django) processes API requests, manages data
3. Celery workers handle scraping tasks asynchronously
4. Both stacks read/write to shared PostgreSQL database
