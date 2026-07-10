# xamehi — Dual-Backend + React Application

> **Stack:** Django + Express + React 18 | **Type:** Triple-Service Web Application | **Status:** Legacy / Active

A legacy dual-backend application combining Django REST Framework (Python) and Express.js (Node.js), with a React 18 frontend via Create React App. Three services running concurrently on different ports.

---

## Technology Stack

### Backend 1: Django + DRF

| Category | Technology |
|---|---|
| **Web Framework** | Django (latest) |
| **API Framework** | Django REST Framework (DRF) |
| **Language** | Python ^3.10+ |
| **Database** | PostgreSQL |
| **Serving** | Gunicorn |

### Backend 2: Express.js

| Category | Technology |
|---|---|
| **Framework** | Express ^4.18.1 |
| **Language** | JavaScript (CommonJS) |
| **Middleware** | CORS |
| **Dev Tool** | Nodemon ^2.0.19 |

### Frontend: React 18 (CRA)

| Category | Technology |
|---|---|
| **UI Framework** | React ^18.2.0 |
| **HTTP Client** | Axios ^0.27.2 |
| **Build Tool** | Create React App (react-scripts 5.0.1) |

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                  xamehi Platform                     │
├──────────────────────┬──────────────────────────────┤
│  Backend 1 (Django)  │  Backend 2 (Express)         │
│  Port: 8000          │  Port: 5000                  │
│  Django REST         │  Express.js                  │
│  PostgreSQL          │  CORS middleware             │
│  Gunicorn            │  Nodemon (dev)               │
├──────────────────────┴──────────────────────────────┤
│  Frontend (React 18)                                │
│  Port: 3000                                         │
│  Create React App                                   │
│  Axios HTTP client                                  │
├─────────────────────────────────────────────────────┤
│  Production                                          │
│  ├── gunicorn xamehi.wsgi:application               │
│  ├── NODE_ENV=production node index.js              │
│  └── CORS; production HTTPS                          │
└─────────────────────────────────────────────────────┘
```

## Project Structure

```
xamehi/
├── backend/                   # Django backend
│   ├── manage.py
│   ├── requirements.txt
│   └── xamehi/               # Django project package
├── frontend/                  # React 18 frontend
│   ├── package.json
│   ├── public/
│   └── src/
├── server/                    # Express backend
│   ├── index.js
│   └── ... (Express routes)
├── package.json               # Root package (manages Express + React)
└── docs/Project_Architecture/
```

## Getting Started

```bash
# Install all dependencies
npm install                    # Frontend + Express
pip install -r requirements.txt  # Django

# Start all services (development)
npm start                      # React frontend (port 3000)
npm run server                 # Express backend (port 5000, nodemon)
python manage.py runserver     # Django backend (port 8000)

# Database setup
python manage.py migrate
python manage.py createsuperuser

# Run tests
npm test                       # React tests
python manage.py test          # Django tests
```

## Production Build

```bash
# Build frontend
npm run build

# Collect Django static files
python manage.py collectstatic

# Start production services
gunicorn xamehi.wsgi:application --bind 0.0.0.0:8000
NODE_ENV=production node index.js
```

## Key Features

- **Dual Backend** — Django REST API + Express.js microservice
- **React 18 Frontend** — Modern UI via Create React App
- **PostgreSQL Database** — Persistent data storage
- **Three-Service Architecture** — Independent services on different ports

## Service Ports

| Service | Port | Description |
|---|---|---|
| **React Frontend** | 3000 | Development server (CRA) |
| **Express Backend** | 5000 | Node.js API (nodemon) |
| **Django Backend** | 8000 | Python REST API |

## Coding Standards

### Python/Django

- PEP 8, Django conventions
- DRF patterns for API development

### React

- ESLint react-app configuration
- ES6 modules, Axios for HTTP

### Express

- CommonJS modules
- Middleware-based routing
- CORS configured for development

## Security

- `.env` never committed; Django `SECRET_KEY` in environment
- Restrict CORS in production
- Validate all inputs
- HTTPS required in production

## License

Not specified.
