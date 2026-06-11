# Xamehi — Project Documentation

## Overview

Xamehi is a manga and comic reading platform with a Django REST backend and React frontend. Users can browse a catalog of comics, read chapters in a dedicated reader interface, bookmark series, rate and comment on content. The backend serves content via a RESTful API, while the frontend provides a responsive reading experience.

**Repository:** https://github.com/Rhixe-company/xamehi  
**Stack:** Django 4.x | Django REST Framework | React 18 | Redux | PostgreSQL | Bootstrap 5  
**Status:** Initial Scaffold — Active Development

---

## Architecture

### System Architecture

```
┌────────────────────────────────────────────────────────────┐
│                    React Frontend (SPA)                      │
│  ├── HomeScreen    ├── ComicScreen    ├── Reader            │
│  ├── LoginScreen   ├── ProfileScreen  ├── AdminPanel        │
│  └── Router (react-router-dom)        └── Redux Store       │
└─────────────────────┬──────────────────────────────────────┘
                      │ HTTP/JSON (Axios)
┌─────────────────────▼──────────────────────────────────────┐
│                 Django REST Framework API                     │
│  ├── /api/comics/    ├── /api/chapters/   ├── /api/auth/    │
│  ├── /api/bookmarks/ ├── /api/comments/   ├── /api/ratings/ │
│  └── JWT Authentication (simplejwt)                          │
├────────────────────────────────────────────────────────────┤
│                   Django ORM / PostgreSQL                     │
│  ├── Comic     ├── Chapter     ├── Page      ├── Genre       │
│  ├── Bookmark  ├── Comment     ├── Rating    ├── User        │
└────────────────────────────────────────────────────────────┘
```

### Directory Structure

```
xamehi/
├── xamehi/                    # Django project config
│   ├── settings.py            # Django settings
│   ├── urls.py                # URL routing
│   ├── wsgi.py                # WSGI entry point
│   └── asgi.py                # ASGI entry point
├── comics/                    # Comics app (planned)
│   ├── models.py              # Comic, Chapter, Page, Genre
│   ├── serializers.py         # DRF serializers
│   ├── views.py               # API views
│   ├── urls.py                # App URLs
│   ├── admin.py               # Admin configuration
│   └── tests.py               # Tests
├── users/                     # Users app (planned)
│   ├── models.py              # Bookmark, Profile (extended User)
│   ├── serializers.py         # User/bookmark serializers
│   ├── views.py               # Auth + bookmark views
│   ├── urls.py                # App URLs
│   └── tests.py               # Tests
├── frontend/                  # React application
│   ├── src/
│   │   ├── components/        # Reusable UI components
│   │   ├── screens/           # Page-level components
│   │   ├── actions/           # Redux action creators
│   │   ├── reducers/          # Redux state reducers
│   │   ├── constants/         # Action type constants
│   │   ├── store.js           # Redux store
│   │   └── App.js             # Root component
│   ├── public/                # Static assets
│   └── package.json           # Node dependencies
├── manage.py                  # Django management script
└── requirements.txt           # Python dependencies
```

---

## Development Guide

### Prerequisites

```bash
# Python 3.10+
python --version

# Node.js 18+
node --version

# PostgreSQL
psql --version
```

### Setup

```bash
# Clone repository
git clone https://github.com/Rhixe-company/xamehi.git
cd xamehi

# Python environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Django setup
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# Frontend setup (separate terminal)
cd frontend
npm install
npm start
```

### Environment Variables

```env
DJANGO_SECRET_KEY=your-secret-key
DATABASE_URL=postgres://user:pass@localhost:5432/xamehi
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

---

## User Guide

### Reading Comics

1. **Browse Catalog** — Navigate to `/comics` to see all available series
2. **Filter & Search** — Filter by genre, status, type, or use the search box
3. **Comic Detail** — Click a comic to see synopsis, metadata, and chapter list
4. **Read Chapter** — Click any chapter to enter the reader interface
5. **Reading Experience** — Navigate pages with click/swipe, use keyboard shortcuts

### Account Features

| Feature | Description |
|---------|-------------|
| Registration | Email + password signup |
| Login | JWT-based authentication |
| Profile | View and edit personal information |
| Bookmarks | Save comics with reading status (Reading/Completed/Plan to Read/Dropped) |
| Reading Progress | Auto-tracks last read chapter and page |
| Comments | Discuss chapters with threaded comments |
| Ratings | Rate comics on a 1-10 scale with optional review |

### Bookmark Status

| Status | Meaning |
|--------|---------|
| Reading | Currently reading, shows in "Continue Reading" |
| Completed | Finished all available chapters |
| Plan to Read | Marked for future reading |
| Dropped | Decided not to continue |

---

## API Reference

### Authentication

```
POST /api/auth/register/
  Body: { username, email, password, password2 }
  Response: { token, user }

POST /api/auth/login/
  Body: { username, password }
  Response: { token, user }

POST /api/auth/refresh/
  Body: { token }
  Response: { token }
```

### Comics

```
GET /api/comics/
  Query: ?page=1&genre=action&status=ongoing&type=manhwa&search=tower
  Response: { comics: [...], page: 1, pages: 10 }

GET /api/comics/{slug}/
  Response: { id, title, slug, description, cover_image, status, ... }

GET /api/comics/{slug}/chapters/
  Response: [{ id, chapter_number, title, page_count, ... }]

GET /api/comics/{slug}/chapters/{number}/
  Response: { id, title, pages: [{ page_number, image_url }, ...] }
```

### Bookmarks

```
GET /api/bookmarks/         → User's bookmarks
POST /api/bookmarks/        → Add bookmark { comic_id, status }
DELETE /api/bookmarks/{id}/ → Remove bookmark
PATCH /api/bookmarks/{id}/  → Update status { status, current_chapter_id }
```

---

## Deployment

### Production Setup

```bash
# Build frontend
cd frontend
npm run build
cd ..

# Configure production settings
# Set DEBUG=False, configure DATABASE_URL, ALLOWED_HOSTS

# Collect static files
python manage.py collectstatic --noinput

# Run with Gunicorn
gunicorn xamehi.wsgi:application --workers 4 --bind 0.0.0.0:8000
```

### Nginx Configuration

```nginx
server {
    listen 80;
    server_name xamehi.tv;

    location /static/ {
        alias /path/to/static/;
    }

    location /media/ {
        alias /path/to/media/;
    }

    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location / {
        root /path/to/frontend/build;
        try_files $uri /index.html;
    }
}
```

### Deployment Checklist

- [ ] `DEBUG=False`, unique `SECRET_KEY`
- [ ] PostgreSQL database (not SQLite)
- [ ] Frontend built with `npm run build`
- [ ] CORS configured for production domain
- [ ] HTTPS enabled (Let's Encrypt)
- [ ] Static files served by Nginx/CDN
- [ ] Database backups configured
- [ ] Error monitoring (Sentry)

---

## Testing

```bash
# Django tests
python manage.py test comics
python manage.py test users

# Frontend tests
cd frontend
npm test

# With coverage
coverage run --source='.' manage.py test
coverage report
```

---

## Roadmap

| Phase | Features | Status |
|-------|----------|--------|
| 1 | Django project scaffold, settings | ✅ Done |
| 2 | Comic + Chapter + Page models | ❌ Planned |
| 3 | REST API endpoints | ❌ Planned |
| 4 | React frontend with reader | ❌ Planned |
| 5 | User auth + bookmarks | ❌ Planned |
| 6 | Comments + ratings | ❌ Planned |
| 7 | Search + filters | ❌ Planned |
| 8 | Docker + production deployment | ❌ Planned |
