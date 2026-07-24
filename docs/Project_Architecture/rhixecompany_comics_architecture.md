# rhixecompany-comics Architecture Blueprint

## Overview
- **Project**: rhixecompany-comics
- **Path**: projects/rhixecompany-comics
- **Stack**: Dual-stack (Django + Next.js)

## Layer Analysis
- **Presentation**: Next.js/React frontend with App Router

## Cross-Cutting Concerns
- **Auth**: NextAuth.js
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- Django apps modular, Celery tasks
