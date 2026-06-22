# Technology Stack — rhixecompany-comics

## Overview

A consolidated comics platform that pairs a Django backend with a Next.js 16 frontend.

## Frontend

| Technology | Version | Purpose |
| --- | --- | --- |
| Next.js | ^16.0.0 | App Router, routing, metadata, and server components |
| React | ^19.0.0 | UI rendering |
| React DOM | ^19.0.0 | Client rendering |
| TypeScript | ^5.7.0 | Type safety |
| Tailwind CSS | ^4.0.0 | Styling |
| shadcn/ui primitives | via Radix packages | Accessible UI building blocks |
| Lucide React | ^0.500.0 | Icons |
| class-variance-authority | ^0.7.0 | Variant utilities |
| tailwind-merge | ^3.0.0 | Tailwind class merging |
| clsx | ^2.1.0 | Conditional class helpers |

## Backend

| Technology | Version Range | Purpose |
| --- | --- | --- |
| Django | >=5.0,<5.2 | Web framework |
| Django REST Framework | >=3.15,<4.0 | API layer |
| django-cors-headers | >=4.3,<5.0 | Cross-origin support |
| django-filter | >=24.1,<25.0 | Query filtering |
| Celery | >=5.3,<6.0 | Async jobs |
| Redis | >=5.0,<6.0 | Broker / cache |
| Scrapy | >=2.11,<3.0 | Spider framework |
| Selenium | >=4.20,<5.0 | Browser automation |
| psycopg2-binary | >=2.9,<3.0 | PostgreSQL driver |
| gunicorn | >=22.0,<23.0 | Production server |
| python-dotenv | >=1.0,<2.0 | Env loading |
| Pillow | >=10.0,<11.0 | Image handling |
| whitenoise | >=6.6,<7.0 | Static file serving |
| djangorestframework-simplejwt | >=5.3,<6.0 | JWT auth |
| drf-spectacular | >=0.27,<1.0 | Schema generation |

## Dev Tooling

| Tool | Version | Purpose |
| --- | --- | --- |
| ESLint | ^9.0.0 | Frontend linting |
| Prettier | ^3.4.0 | Formatting |
| Vitest | ^3.0.0 | Test runner |
| Next lint | next lint | Framework-aware linting |
| python compileall | stdlib | Syntax validation |
