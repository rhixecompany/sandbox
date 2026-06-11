# Developer Guide — Xamehi.tv

This guide covers setup, development workflow, and contribution process for Xamehi.tv.

## Prerequisites

- Python 3.8+
- Node.js 16+ (for frontend)
- pip
- Git
- Virtual environment tool

## Project Overview

Xamehi.tv is a full-stack movie streaming website built with:
- **Backend**: Django with Django REST Framework
- **Frontend**: React (built as static files)
- **Database**: SQLite (dev) / PostgreSQL (production)
- **Authentication**: Django AllAuth + DRF SimpleJWT
- **Deployment**: Heroku with Gunicorn

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/rhixecompany/xamehi.tv.git
cd xamehi.tv
```

### 2. Set Up Backend

```bash
# Create virtual environment
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Create superuser (optional, for admin access)
python manage.py createsuperuser
```

### 3. Set Up Frontend

```bash
cd frontend
npm install
npm run build
cd ..
```

### 4. Start Development Server

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`.

## Project Structure

```
xamehi.tv/
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── player/             # Core Django app (movie/player functionality)
├── video/              # Video content management app
├── frontend/           # React application
├── static/             # Collected static assets
├── Procfile            # Heroku deployment config
├── runtime.txt         # Python runtime version
├── gunicorn.service    # Systemd service file
└── gunicorn.socket     # Systemd socket file
```

## Django Apps

| App | Purpose |
|-----|---------|
| `player` | Core movie player functionality, views, and models |
| `video` | Video content management and streaming |
| `frontend` | React SPA (built to static files) |

## Available Commands

| Command | Description |
|---------|-------------|
| `python manage.py runserver` | Start development server |
| `python manage.py migrate` | Run database migrations |
| `python manage.py createsuperuser` | Create admin user |
| `python manage.py collectstatic` | Collect static files |
| `npm run build` (in frontend/) | Build React frontend |

## Testing

```bash
# Run Django tests
python manage.py test

# Run frontend tests (if configured)
cd frontend && npm test
```

## Code Style

- Follow PEP 8 for Python code
- Use ESLint for JavaScript/React code
- Django REST Framework serializers for API endpoints

## API Endpoints

The backend provides REST API endpoints for:
- Movie listings and details
- User authentication (JWT)
- Reviews and ratings
- Search and filtering

## Contribution Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make changes and test locally
4. Commit with Conventional Commits format
5. Push and open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## Deployment

### Heroku Deployment

```bash
# Install Heroku CLI
# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Set environment variables
heroku config:set DATABASE_URL=your_database_url
heroku config:set SECRET_KEY=your_secret_key

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate
heroku run python manage.py collectstatic --noinput
```

### Production Considerations

- Use PostgreSQL in production (configured via `DATABASE_URL`)
- Set `DEBUG=False` in production
- Configure allowed hosts
- Use WhiteNoise for static file serving
- Gunicorn handles production WSGI serving
