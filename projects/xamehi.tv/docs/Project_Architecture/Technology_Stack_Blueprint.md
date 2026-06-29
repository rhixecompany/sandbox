# Technology Stack Blueprint

## Project: xamehi.tv — Django + React Streaming

> **Generated:** 2026-06-25  
> **Generator:** technology-stack-blueprint-generator  
> **Analysis Depth:** Comprehensive

---

## Overview

A streaming platform with a Django REST backend and React 17 frontend using Material-UI 4. Features video playback via video-react and PayPal payment integration.

**Project Type:** Full-Stack Streaming Platform  
**Stack Type:** Django (+ React Frontend)

---

## Technology Stack

### Languages & Runtimes

| Technology | Version | Usage |
|---|---|---|
| Python | — | Backend language |
| JavaScript (ES6+) | — | Frontend language |
| React | ^17.0.1 | UI framework |
| Node.js | — | Frontend runtime |

### Backend Stack (Django/DRF)

| Category | Technologies |
|---|---|
| **Web Framework** | Django (latest) |
| **API Framework** | Django REST Framework |
| **Auth** | SimpleJWT (djangorestframework-simplejwt) |
| **Social Auth** | django-allauth |
| **Database** | PostgreSQL (prod), SQLite (dev) |
| **Serving** | Gunicorn, WhiteNoise |
| **Cross-Origin** | django-cors-headers |

### Frontend Stack (React 17)

| Category | Dependencies |
|---|---|
| **UI Framework** | react ^17.0.1, react-dom ^17.0.1 |
| **UI Library** | @material-ui/core ^4.12.4, react-bootstrap ^1.4.0 |
| **State Management** | redux ^4.0.5, redux-thunk ^2.3.0 |
| **Routing** | react-router-dom ^5.2.0 |
| **Admin Panel** | react-admin ^4.3.1, ra-data-simple-rest |
| **HTTP Client** | axios ^0.21.1 |
| **Payments** | react-paypal-button-v2 ^2.6.2 |
| **Video** | video-react ^0.15.0 |
| **Build** | react-scripts 4.0.1 (CRA) |
| **Dev Tools** | redux-devtools-extension |

---

## Licensing

| Component | License |
|---|---|
| xamehi.tv | (not specified) |

---

## Project Structure

```
xamehi.tv/
├── backend/               # Django REST API
│   ├── requirements.txt
│   └── manage.py
├── frontend/              # React 17 application
│   ├── package.json
│   └── src/
│       ├── components/
│       ├── pages/
│       └── redux/         # Redux store
└── AGENTS.md
```

---

## Key Scripts

| Command | Description |
|---|---|
| `python manage.py runserver` | Backend on 127.0.0.1:8000 |
| `python manage.py test` | Django tests |
| `npm start` | Frontend on localhost:3000 |
| `npm test` | Frontend tests |

---

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
│  ├── Proxy: backend 127.0.0.1:8000                 │
│  └── Proxy: frontend localhost:3000                │
└─────────────────────────────────────────────────────┘
```

---

## Notes

- Backend runs on port 8000, frontend on port 3000
- CORS configuration via django-cors-headers
- CORS + proxy troubleshooting is common
- `.env` never committed
