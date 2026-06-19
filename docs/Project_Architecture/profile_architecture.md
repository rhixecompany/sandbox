# profile Architecture Blueprint

## Overview
- **Project**: profile
- **Path**: projects/profile
- **Stack**: Django, Python

## Layer Analysis
- **Presentation**: Django templates + optional DRF API
- **Business Logic**: Django views, models, serializers
- **Data Layer**: Django ORM with PostgreSQL/SQLite

## Cross-Cutting Concerns
- **Auth**: Django Auth
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- Django apps modular, Celery tasks
