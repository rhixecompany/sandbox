# Xamehi TV — Project Documentation

## Overview

Xamehi TV is a Django-based video streaming platform that provides a catalog of movies and TV series with user authentication, reviews, and admin content management. The platform uses PostgreSQL for primary data storage with MongoDB integration for analytics, and a React frontend for the user interface.

**Repository:** <https://github.com/Rhixe-company/xamehi.tv>  
**Stack:** Django 4.x | Django REST Framework | React 18 | Redux | PostgreSQL | MongoDB (djongo/pymongo) | Bootstrap 5 | Gunicorn  
**Status:** Active Development

---

## Architecture

### System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                      Users (Browser)                          │
├───────────────┬──────────────────────┬───────────────────────┤
│  Django Views │  REST API (DRF)      │  React SPA            │
│  /movies/     │  /api/movies/        │  Frontend (Port 3000) │
│  /series/     │  /api/series/        │                       │
│  /login/      │  /api/users/         │  Redux Store          │
│  /account/    │  /api/users/login/   │  react-router-dom     │
├───────────────┴──────────────────────┴───────────────────────┤
│                      Django Application                        │
│  ┌────────────────────────────────────────────────────────┐   │
│  │                    video/ App                            │   │
│  │  models.py │ views.py │ serializers.py │ forms.py       │   │
│  │  filters.py │ decorators.py │ admin.py │ tests.py       │   │
│  │  pymongo_views.py (MongoDB integration)                  │   │
│  └────────────────────────────────────────────────────────┘   │
├────────────────────────────────────────────────────────────┤
│                    Data Layer                                 │
│  ┌──────────────────────┐  ┌──────────────────────────────┐  │
│  │    PostgreSQL         │  │    MongoDB (xamehitv)        │  │
│  │  Movies | Series      │  │  movies collection           │  │
│  │  Season | Episode     │  │  (analytics / fast reads)    │  │
│  │  Reviews | Users      │  │                              │  │
│  └──────────────────────┘  └──────────────────────────────┘  │
└────────────────────────────────────────────────────────────┘
```

### Application Structure

```
xamehi.tv/
├── player/                      # Django project configuration
│   ├── settings.py              # Django settings (DB, apps, static)
│   ├── urls.py                  # Root URL configuration
│   ├── wsgi.py                  # WSGI entry point for Gunicorn
│   ├── asgi.py                  # ASGI entry point
│   └── __init__.py
├── video/                       # Main video streaming app
│   ├── models.py                # Movies, Series, Season, Episode, Reviews
│   ├── view.py                  # Django template views (CRUD, auth)
│   ├── serializers.py           # DRF serializers (User, Movies, Series)
│   ├── views/                   # DRF REST API views
│   │   ├── movies_views.py      # Movie API endpoints
│   │   ├── series_views.py      # Series API endpoints
│   │   └── user_views.py        # User/auth API endpoints
│   ├── urls/                    # App URL routing
│   │   ├── movies_urls.py       # Movie REST routes
│   │   ├── series_urls.py       # Series REST routes
│   │   └── user_urls.py         # User REST routes
│   ├── url.py                   # Template view URL routing
│   ├── forms.py                 # Movie, Series, Profile, User forms
│   ├── filters.py               # Movie/Series filtering with django-filter
│   ├── decorators.py            # @admin_only decorator
│   ├── admin.py                 # Django admin configuration
│   ├── pymongo_views.py         # MongoDB Atlas integration
│   ├── migrations/              # Database migrations
│   └── templates/video/         # Django HTML templates
├── frontend/                    # React SPA
│   ├── src/
│   │   ├── actions/             # Redux actions (movie, series, user)
│   │   ├── components/          # UI components (Header, Footer, Movie, Rating)
│   │   ├── constants/           # Redux action types
│   │   ├── reducers/            # Redux state reducers
│   │   ├── screens/             # Page components (13 screens)
│   │   ├── store.js             # Redux store
│   │   └── App.js               # Root React component
│   └── package.json
├── static/                      # Django admin static files
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── Procfile                     # Heroku deployment config
├── runtime.txt                  # Python runtime version
├── gunicorn.service             # Systemd service config
├── gunicorn.socket              # Systemd socket config
├── .env.example                 # Environment template
├── ARCHITECTURE.md
├── CONTRIBUTING.md
├── DEVELOPER_GUIDE.md
└── USER_GUIDE.md
```

---

## Data Model

### Entity Relationship

```
User (Django auth)
  ├── Movies        (created_by, FK user SET_NULL)
  ├── Series        (created_by, FK user SET_NULL)
  ├── Season         (created_by, FK user SET_NULL)
  ├── MoviesReview  (author, FK user SET_NULL)
  └── SeriesReview  (author, FK user SET_NULL)

Series
  └── Season        (FK seriesModel SET_NULL, related_name='season')
        └── Episode (FK season_episode CASCADE)
                     (FK series_season SET_NULL, related_name='episodes')

Movies
  └── MoviesReview  (FK movies SET_NULL)

Series
  └── SeriesReview  (FK series SET_NULL)
```

### Data Flow

```
Upload Flow:
  Admin → CRUD Form → Django View → File Upload → Media Storage
  Admin → REST API  → Serializer  → DB Save     → PostgreSQL

Streaming Flow:
  User → React App → Django View → Query DB → Serve Video File
  User → DRF API   → Serializer  → JSON Response

MongoDB Flow:
  Django View → pymongo → MongoDB Atlas → Analytics Data
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
git clone https://github.com/Rhixe-company/xamehi.tv.git
cd xamehi.tv

# Python virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with:
#   - DATABASE_URL for PostgreSQL
#   - DJANGO_SECRET_KEY
#   - MONGODB_URI for MongoDB Atlas (if using)
#   - EMAIL_HOST_USER/GMAIL_APP_PASSWORD for contact form

# Create database
createdb xamehitv

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start Django server
python manage.py runserver

# Frontend (separate terminal)
cd frontend
npm install
npm start
```

### Environment Variables

```env
DJANGO_SECRET_KEY=your-secret-key-here
DATABASE_URL=postgres://user:pass@localhost:5432/xamehitv
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# MongoDB (optional)
MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net/xamehitv

# Email (contact form)
EMAIL_HOST_USER=your-email@gmail.com
GMAIL_APP_PASSWORD=your-app-password

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

### MongoDB Setup

The MongoDB integration uses pymongo directly (not djongo ORM). Connection is configured in `video/pymongo_views.py`:

```python
import pymongo

# Production: read URI from environment variable
client = pymongo.MongoClient(os.getenv('MONGODB_URI'))
db = client['xamehitv']
collection = db['movies']
```

**⚠️ IMPORTANT:** The current code has hardcoded credentials in `pymongo_views.py`. Move the connection string to `MONGODB_URI` environment variable before production deployment.

### Available Management Commands

```bash
python manage.py migrate          # Apply database migrations
python manage.py makemigrations   # Create new migrations
python manage.py createsuperuser  # Create admin user
python manage.py collectstatic    # Collect static files
python manage.py test video       # Run app tests
```

---

## User Guide

### Browsing Content

| Page | URL | Description |
| ------ | ----- | ------------- |
| Home | `/` | Featured movies carousel, recently added |
| Movies | `/movies/` | Paginated movie catalog with filters |
| Movie Detail | `/movies/<slug>/` | Movie info, video player, reviews |
| Series | (REST API) | Series catalog via `/api/series/` |

### Authentication

| Page | URL | Description |
| ------ | ----- | ------------- |
| Login | `/login/` | Email + password login |
| Register | `/register/` | Create account with CustomUserCreationForm |
| Account | `/account/` | View profile information |
| Update Profile | `/update_profile/` | Edit display name, photo, bio |

### Admin Features

Admin users can access CRUD operations via:

| Action | Template URL | API Endpoint |
| -------- | ------------- | ------------- |
| Create Movie | `/create_movie/` | `POST /api/movies/` |
| Update Movie | `/update_movie/<slug>/` | `PUT /api/movies/:pk/` |
| Delete Movie | `/delete_movie/<slug>/` | `DELETE /api/movies/:pk/` |
| List Users | — | `GET /api/users/` |
| Update User | — | `PUT /api/users/:pk/update/` |

### Contact Form

The `/send_email/` page allows visitors to send messages to the admin. Uses Django's `EmailMessage` with Gmail SMTP. Requires valid `EMAIL_HOST_USER` and `GMAIL_APP_PASSWORD`.

---

## Deployment

### Docker Deployment (if configured)

```bash
docker-compose up --build -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --noinput
```

### Manual Deployment (VPS)

```bash
# Build frontend
cd frontend && npm run build && cd ..

# Collect static files
python manage.py collectstatic --noinput

# Run with Gunicorn
gunicorn player.wsgi:application --workers 4 --bind 0.0.0.0:8000
```

### Nginx Configuration

```nginx
server {
    listen 80;
    server_name xamehi.tv;

    location /static/ { alias /path/to/static/; }
    location /media/  { alias /path/to/media/;  }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Production Checklist

- [ ] `DEBUG=False`, unique `SECRET_KEY`
- [ ] PostgreSQL with strong credentials
- [ ] MongoDB connection string in env var (not hardcoded)
- [ ] `ALLOWED_HOSTS` set to production domain
- [ ] Frontend built and served as static files or via CDN
- [ ] HTTPS configured (Let's Encrypt)
- [ ] CORS restricted to production domain
- [ ] Gmail app password rotated (not hardcoded)
- [ ] Database backups configured
- [ ] Gunicorn systemd service configured

---

## Testing

```bash
# Django tests
python manage.py test video

# Frontend tests
cd frontend && npm test

# With coverage
coverage run --source='video' manage.py test video
coverage report
```

### Test Coverage Areas

- Model creation, string representation, constraints
- View response status codes and template rendering
- Form validation and error handling
- Authentication (login, register, logout flows)
- Admin decorator permission checks
- REST API endpoint behavior (DRF)

---

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed guidelines.

### Quick Guidelines

1. Branch from `main`: `git checkout -b feature/description`
2. Write tests for new functionality
3. Run full test suite before committing
4. Update documentation for significant changes
5. Submit pull request with clear description

### Code Style

- Python: Django coding style, Black formatting (`black .`)
- JavaScript: Standard JS style, Prettier formatting
- Import ordering: isort for Python
- Docstrings: Google-style for Python functions and classes
