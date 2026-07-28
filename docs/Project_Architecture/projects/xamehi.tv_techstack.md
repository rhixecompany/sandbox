# 🏗 Technology Stack Blueprint - xamehi.tv

**Project Path:** `projects/xamehi.tv`
**Generated:** 2026-07-28
**Status:** Active — Django REST + React 17 Streaming Platform

---

## Architecture Overview

**Pattern:** Dual-stack — DRF Backend + React 17 (CRA) Frontend
```
┌─────────────────────┐     ┌─────────────────────┐
│   React 17 (CRA)    │────▶│   Django REST API   │
│   Material-UI 4     │     │   SimpleJWT Auth    │
│   Redux + RTK       │     │   PayPal Payments   │
│   video-react       │     │   django-allauth    │
│   :3000             │     │   :8000             │
└─────────────────────┘     └─────────────────────┘
                            │
                     ┌──────▼──────┐
                     │ PostgreSQL  │
                     └─────────────┘
```

---

## Backend Stack (Django)

| Category | Technology | Version | License |
|----------|-----------|---------|---------|
| **Framework** | Django | Latest (4.x+) | BSD |
| **API** | Django REST Framework | Latest | MIT |
| **Auth (JWT)** | djangorestframework-simplejwt | ^5.3,<6.0 | MIT |
| **Social Auth** | django-allauth | Latest | MIT |
| **CORS** | django-cors-headers | ^4.3,<5.0 | MIT |
| **Filters** | django-filter | ^24.1,<25.0 | MIT |
| **Static Files** | WhiteNoise | ^6.6,<7.0 | MIT |
| **Storage** | django-storages | ^1.12,<2.0 | BSD |
| **Database** | psycopg2-binary | ^2.9,<3.0 | LGPL |
| **WSGI** | Gunicorn | ^22.0,<23.0 | MIT |
| **Env Config** | python-dotenv | ^1.0,<2.0 | BSD |
| **Media** | Pillow | ^10.0,<11.0 | PIL |
| **API Docs** | drf-spectacular | ^0.27,<1.0 | MIT |

### Backend Requirements (`requirements.txt`)
```text
Django>=5.0,<5.2
djangorestframework>=3.15,<4.0
django-cors-headers>=4.3,<5.0
django-filter>=24.1,<25.0
celery>=5.3,<6.0
redis>=5.0,<6.0
psycopg2-binary>=2.9,<3.0
gunicorn>=22.0,<23.0
python-dotenv>=1.0,<2.0
Pillow>=10.0,<11.0
whitenoise>=6.6,<7.0
djangorestframework-simplejwt>=5.3,<6.0
drf-spectacular>=0.27,<1.0
django-allauth>=0.57,<1.0
django-storages>=1.12,<2.0
```

---

## Frontend Stack (React 17 + CRA)

| Category | Technology | Version | License |
|----------|-----------|---------|---------|
| **Framework** | React | ^17 | MIT |
| **Build** | react-scripts | 5.x | MIT |
| **UI Library** | Material-UI (MUI) | ^4.x | MIT |
| **State** | Redux + Redux Toolkit | Latest | MIT |
| **Data Fetching** | ra-data-simple-rest | Latest | MIT |
| **Admin** | react-admin | Latest | MIT |
| **Video Player** | video-react | Latest | MIT |
| **HTTP** | Axios | Latest | MIT |
| **Routing** | react-router-dom | ^6 | MIT |
| **Testing** | @testing-library/* | Latest | MIT |

### Frontend Dependencies (inferred from structure)
```json
{
  "dependencies": {
    "@material-ui/core": "^4.x",
    "@testing-library/jest-dom": "^5.x",
    "@testing-library/react": "^13.x",
    "@testing-library/user-event": "^14.x",
    "axios": "^1.x",
    "caniuse-lite": "^1.x",
    "ra-data-simple-rest": "^4.x",
    "react": "^17.x",
    "react-admin": "^4.x",
    "react-dom": "^17.x",
    "react-router-dom": "^6.x",
    "redux": "^4.x",
    "video-react": "^0.x",
    "web-vitals": "^2.x"
  }
}
```

---

## Key Features

### Authentication
- **JWT**: SimpleJWT for API tokens (access + refresh)
- **Social Login**: django-allauth (Google, GitHub, etc.)
- **Frontend**: React-admin authProvider with JWT storage

### Payments (PayPal)
- **Integration**: PayPal REST SDK or Smart Payment Buttons
- **Flow**: Client-side button → Server verification → Order fulfillment
- **Webhooks**: PayPal IPN for subscription events

### Video Streaming
- **Player**: video-react (HTML5 video wrapper)
- **Delivery**: Direct file serving or CDN
- **Formats**: MP4 (H.264), WebM (VP9)

### Admin Interface
- **Backend**: Django Admin (customized)
- **Frontend**: react-admin (CRUD for content management)

---

## Project Structure

```
xamehi.tv/
├── backend/                  # Django project
│   ├── config/              # Settings
│   │   ├── base.py
│   │   ├── local.py
│   │   └── production.py
│   ├── apps/
│   │   ├── accounts/        # User management
│   │   ├── content/         # Video/content models
│   │   ├── payments/        # PayPal integration
│   │   └── api/             # DRF views/serializers
│   ├── manage.py
│   ├── requirements.txt
│   └── Pipfile
├── frontend/                 # React CRA app
│   ├── public/
│   ├── src/
│   │   ├── components/      # Reusable components
│   │   ├── pages/           # Page components
│   │   ├── admin/           # react-admin resources
│   │   ├── services/        # API clients
│   │   ├── store/           # Redux store/slices
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   └── package-lock.json
├── docker-compose.yml
├── Dockerfile.backend
├── Dockerfile.frontend
└── README.md
```

---

## Commands

### Backend
```bash
cd backend

# Setup
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Database
python manage.py migrate
python manage.py createsuperuser

# Development
python manage.py runserver  # :8000

# Production
python manage.py collectstatic --noinput
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

### Frontend
```bash
cd frontend
npm install
npm start          # :3000 (proxies to :8000)
npm test           # Jest + Testing Library
npm run build      # Production build
```

### Full Stack (Docker)
```bash
docker-compose up -d
# backend: :8000, frontend: :3000, postgres: :5432
```

---

## Environment Variables

### Backend (`.env`)
```env
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database
DATABASE_URL=postgres://user:pass@host:5432/dbname

# Django
DJANGO_SETTINGS_MODULE=config.settings.production

# JWT
SIMPLE_JWT_ACCESS_TOKEN_LIFETIME=60
SIMPLE_JWT_REFRESH_TOKEN_LIFETIME=1440

# PayPal
PAYPAL_CLIENT_ID=...
PAYPAL_CLIENT_SECRET=...
PAYPAL_MODE=live  # or sandbox

# Allauth
SOCIALACCOUNT_GOOGLE_CLIENT_ID=...
SOCIALACCOUNT_GOOGLE_SECRET=...

# Email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=...
EMAIL_HOST_PASSWORD=...
```

### Frontend (`.env`)
```env
REACT_APP_API_URL=http://localhost:8000/api
REACT_APP_PAYPAL_CLIENT_ID=...
```

---

## CI/CD

**Workflow:** `.github/workflows/xamehi-tv-ci.yml`

```yaml
# Backend
- pip install -r requirements.txt
- python manage.py check --deploy
- ruff check .
- mypy .
- pytest

# Frontend
- npm ci
- npm run lint
- npm run test -- --watchAll=false
- npm run build

# Docker
- docker build -t xamehi-backend ./backend
- docker build -t xamehi-frontend ./frontend
```

---

## Known Issues & Modernization

| Issue | Recommendation |
|-------|---------------|
| React 17 (CRA) | Migrate to Next.js 15 + TypeScript |
| Material-UI v4 | Upgrade to MUI v5+ |
| Redux (legacy) | Use Redux Toolkit + RTK Query |
| Django 5.x (new) | Good - stay current |
| SimpleJWT | Good - standard choice |
| PayPal SDK | Consider PayPal JS SDK v2 |
| No TypeScript | Add TypeScript across stack |

---

## License Summary

| Component | License |
|-----------|---------|
| Django/DRF | BSD / MIT |
| React/MUI | MIT |
| Redux | MIT |
| PayPal | Proprietary (PayPal) |
| All others | MIT / BSD |

---

*Generated by Hermes Agent Technology Stack Blueprint Generator*