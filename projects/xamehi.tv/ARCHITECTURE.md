# Architecture — xamehi.tv

## Overview

xamehi.tv is a full-featured movie streaming website built with Django backend and React frontend. It provides movie discovery, reviews, ratings, and user profile management. The live application is deployed at [xamehi.tv](https://www.xamehi.tv/).

## System Architecture

```
┌──────────────────────────────────────────────────────────┐
│                      Client Browser                       │
│  ┌──────────────────────────────────────────────────────┐ │
│  │              React Frontend (Built)                   │ │
│  │  ┌────────────┐  ┌───────────┐  ┌─────────────────┐ │ │
│  │  │  Components │  │  State    │  │  API Services   │ │ │
│  │  └────────────┘  └───────────┘  └─────────────────┘ │ │
│  └───────────────────────┬──────────────────────────────┘ │
│                          │ REST API                       │
└──────────────────────────┼────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────┐
│              Django Backend Server                        │
│  ┌──────────┐  ┌──────────────┐  ┌────────────────────┐  │
│  │  Views   │  │  Serializers │  │  URL Routing       │  │
│  └──────────┘  └──────────────┘  └────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐ │
│  │  Django AllAuth + DRF SimpleJWT (Authentication)     │ │
│  └──────────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────────┐ │
│  │  WhiteNoise (Static Files) + Django Filter            │ │
│  └──────────────────────────────────────────────────────┘ │
└──────────────────────────┬────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────┐
│                    Database (SQLite/PostgreSQL)            │
└──────────────────────────────────────────────────────────┘
```

## Key Technical Decisions

### Django Backend

- **Django REST Framework** for API endpoints
- **DRF SimpleJWT** for token-based authentication
- **Django AllAuth** for user registration and social auth
- **Django Filter** for movie search and filtering
- **WhiteNoise** for static file serving in production
- **django-storages** for cloud storage integration
- **Gunicorn** as WSGI production server

### React Frontend

- Built and served as static files through Django
- Located in `frontend/` directory
- Compiled via `npm run build` before deployment

### Deployment

- **Heroku** deployment (Procfile, runtime.txt)
- **Gunicorn** service management (gunicorn.service, gunicorn.socket)
- **PostgreSQL** in production (psycopg2-binary), SQLite in development
- **Pillow** for image processing

## Component Relationships

### Backend Structure

- `manage.py` — Django management script
- `player/` — Core Django app for movie/player functionality
- `video/` — Video content management app
- `frontend/` — React application (built to static files)
- `static/` — Collected static assets

### Key Features Architecture

- **Movie Dashboard**: Paginated movie listings with carousel
- **Reviews & Ratings**: User-generated content system
- **Search**: Django Filter backend with React frontend
- **User Profiles**: Personal movie lists and preferences
- **Admin Panel**: Django admin for content management

## Development Workflow

```bash
# Backend setup
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
python manage.py migrate

# Frontend build
cd frontend
npm install
npm run build

# Development server
python manage.py runserver
```

## Dependencies

| Package | Purpose |
|---------|---------|
| Django | Web framework |
| djangorestframework | REST API |
| djangorestframework-simplejwt | JWT authentication |
| django-allauth | User authentication |
| django-filter | Search and filtering |
| django-cors-headers | CORS handling |
| django-storages | Cloud storage |
| gunicorn | Production WSGI server |
| whitenoise | Static file serving |
| psycopg2-binary | PostgreSQL adapter |
| pillow | Image processing |

## Deployment Considerations

- Deployed on Heroku with Gunicorn
- PostgreSQL for production database
- Static files served via WhiteNoise
- Environment variables for secrets (DATABASE_URL, etc.)
