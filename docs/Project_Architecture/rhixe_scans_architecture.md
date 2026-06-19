# rhixe_scans Architecture Blueprint

## Overview
- **Project**: rhixe_scans
- **Path**: projects/rhixe_scans
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
