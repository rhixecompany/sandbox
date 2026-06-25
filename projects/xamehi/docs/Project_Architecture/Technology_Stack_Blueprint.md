# Technology Stack Blueprint

## Project: xamehi — Dual-Backend + React

> **Generated:** 2026-06-25  
> **Generator:** technology-stack-blueprint-generator  
> **Analysis Depth:** Comprehensive

---

## Overview

A legacy dual-backend application combining Django REST Framework (Python) and Express.js (Node.js), with a React 18 frontend via Create React App. Three services running concurrently on different ports.

**Project Type:** Full-Stack Web Application (Triple-Service)  
**Stack Type:** Django (+ Express + React)

---

## Technology Stack

### Languages & Runtimes

| Technology | Version | Usage |
|---|---|---|
| Python | ^3.10+ | Django backend |
| JavaScript (ES6+) | — | Express backend & React frontend |
| Node.js | — | Express + React runtime |
| React | ^18.2.0 | UI framework |

### Backend 1: Django + DRF

| Category | Technologies |
|---|---|
| **Web Framework** | Django (latest) |
| **API Framework** | Django REST Framework |
| **Database** | PostgreSQL |
| **Serving** | Gunicorn |

### Backend 2: Express.js

| Dependency | Version | Purpose |
|---|---|---|
| express | ^4.18.1 | HTTP server |
| cors | ^2.8.5 | Cross-Origin middleware |
| nodemon | ^2.0.19 | Development auto-restart |

### Frontend: React 18 (CRA)

| Dependency | Version | Purpose |
|---|---|---|
| react | ^18.2.0 | UI framework |
| react-dom | ^18.2.0 | DOM rendering |
| react-scripts | 5.0.1 | Build/start tooling |
| axios | ^0.27.2 | HTTP client |
| web-vitals | ^2.1.4 | Performance metrics |

### Testing

| Dependency | Version | Purpose |
|---|---|---|
| @testing-library/jest-dom | ^5.16.5 | DOM assertions |
| @testing-library/react | ^13.3.0 | React component tests |
| @testing-library/user-event | ^13.5.0 | User event simulation |

---

## Licensing

| Component | License |
|---|---|
| xamehi | (not specified) |

---

## Key Scripts

| Command | Description |
|---|---|
| `npm start` | React frontend (port 3000) |
| `npm run server` | Express backend (port 5000, via nodemon) |
| `python manage.py runserver` | Django backend (port 8000) |
| `python manage.py test` | Django tests |
| `npm test` | React tests |
| `npm run build` | React production build |
| `python manage.py collectstatic` | Collect Django static files |

---

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
│  ├── gunicorn xamehi.wsgi:application --bind 0.0.0.0:8000 │
│  ├── NODE_ENV=production node index.js               │
│  └── CORS; production HTTPS                          │
└─────────────────────────────────────────────────────┘
```

---

## Notes

- Three services: Django (8000), Express (5000), React (3000)
- `.env` never committed; Django `SECRET_KEY` in environment
- CORS configured for production HTTPS
- React via Create React App (react-scripts 5.0.1)
- Express with nodemon for development hot-reload
