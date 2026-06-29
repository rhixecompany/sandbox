# xamehi.tv — Streaming Platform

> **Stack:** Django REST + React 17 | **Type:** Full-Stack Streaming Platform | **Status:** Active

A streaming platform with a Django REST backend and React 17 frontend using Material-UI 4. Features video playback via video-react and PayPal payment integration.

---

## Technology Stack

### Backend (Django/DRF)

| Category | Technology |
|---|---|
| **Web Framework** | Django (latest) |
| **API Framework** | Django REST Framework (DRF) |
| **Auth** | SimpleJWT (djangorestframework-simplejwt) |
| **Social Auth** | django-allauth |
| **Database** | PostgreSQL (prod), SQLite (dev) |
| **Serving** | Gunicorn, WhiteNoise |
| **Cross-Origin** | django-cors-headers |

### Frontend (React 17)

| Category | Technology |
|---|---|
| **UI Framework** | React ^17.0.1 |
| **UI Library** | Material-UI ^4.12.4, React Bootstrap |
| **State Management** | Redux ^4.0.5, redux-thunk |
| **Routing** | React Router DOM ^5.2.0 |
| **Admin Panel** | React Admin ^4.3.1 |
| **HTTP Client** | Axios ^0.21.1 |
| **Payments** | react-paypal-button-v2 |
| **Video** | video-react ^0.15.0 |
| **Build Tool** | Create React App (react-scripts 4.0.1) |

## Architecture

```
┌─────────────────────────────────────────────────────┐
│              xamehi.tv Platform                      │
├──────────────────┬──────────────────────────────────┤
│  Backend (Django)│  Frontend (React 17)             │
│                  │                                  │
│  Django REST     │  React 17 + Material-UI 4        │
│  SimpleJWT Auth  │  Redux + Redux Thunk             │
│  django-allauth  │  React Admin dashboard           │
│  PostgreSQL      │  video-react player              │
│  Gunicorn        │  PayPal integration              │
│  WhiteNoise      │  React Router 5                  │
│  CORS headers    │  Axios HTTP client               │
├──────────────────┴──────────────────────────────────┤
│  Communication                                      │
│  ├── CORS: django-cors-headers                      │
│  ├── Backend: 127.0.0.1:8000                       │
│  └── Frontend: localhost:3000                      │
└─────────────────────────────────────────────────────┘
```

## Project Structure

```
xamehi.tv/
├── backend/                   # Django REST API
│   ├── requirements.txt
│   ├── manage.py
│   └── apps/                  # Django applications
├── frontend/                  # React 17 application
│   ├── package.json
│   └── src/
│       ├── components/        # React components
│       ├── screens/           # Page components
│       └── store/             # Redux store
└── docs/Project_Architecture/
```

## Getting Started

### Backend

```bash
# Set up virtual environment
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Database setup
python manage.py migrate
python manage.py runserver    # Runs on 127.0.0.1:8000

# Run tests
python manage.py test
```

### Frontend

```bash
cd frontend
npm install
npm start                     # Runs on localhost:3000
npm test
```

## Key Features

- **Video Streaming** — video-react player for media playback
- **User Authentication** — SimpleJWT + django-allauth
- **Admin Dashboard** — React Admin-powered management panel
- **PayPal Integration** — Payment processing for subscriptions/content
- **REST API** — Django REST Framework backend
- **Material-UI** — Modern, responsive design

## Development

```bash
# Backend runs on port 8000
python manage.py runserver

# Frontend runs on port 3000 (proxied to backend)
cd frontend && npm start
```

## Coding Standards

### Backend
- **Python/Django**: DRF ViewSets + Serializers
- **Authentication**: SimpleJWT token-based auth
- **Social Auth**: django-allauth integration
- **CORS**: django-cors-headers configuration

### Frontend
- **React/JS**: ESLint react-app configuration
- **Redux**: `constants/actions/reducers` pattern
- **Material-UI 4**: UI component library
- **Axios**: HTTP client with JWT handling

## Security

- No `.env` committed to VCS
- CORS configured via django-cors-headers
- CORS + proxy troubleshooting common
- Production HTTPS required

## License

Not specified.
