# 🏗 Technology Stack Blueprint - xamehi

**Project Path:** `projects/xamehi`
**Generated:** 2026-07-28
**Status:** Consolidation Target — Legacy Dual-Backend + React

---

## Architecture Overview

**Pattern:** Three independent services sharing PostgreSQL
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   React 18   │────▶│   Express    │     │    Django    │
│    (CRA)     │     │   (Node.js)  │     │   (Python)   │
│   :3000      │     │   :5000      │     │   :8000      │
└──────────────┘     └──────┬───────┘     └──────┬───────┘
                            │                    │
                     ┌──────▼────────────────────▼──────┐
                     │        PostgreSQL                 │
                     └──────────────────────────────────┘
```

---

## Service Stacks

### Frontend — React (Create React App)

| Category | Technology | Version | License |
|----------|-----------|---------|---------|
| **Framework** | React | ^18.2.0 | MIT |
| **Build** | react-scripts | 5.0.1 | MIT |
| **HTTP** | Axios | ^0.27.2 | MIT |
| **Testing** | @testing-library/react, jest | ^13.3 / ^13.5 | MIT |
| **Language** | JavaScript (ES6+) | - | - |

### Backend 1 — Express.js

| Category | Technology | Version | License |
|----------|-----------|---------|---------|
| **Framework** | Express | ^4.18.1 | MIT |
| **Dev** | Nodemon | ^2.0.19 | MIT |
| **CORS** | cors | ^2.8.5 | MIT |
| **Language** | JavaScript (ES Modules) | Node 18+ | - |

### Backend 2 — Django + DRF

| Category | Technology | Version | License |
|----------|-----------|---------|---------|
| **Framework** | Django | 3.x | BSD |
| **API** | Django REST Framework | 3.13+ | MIT |
| **Auth** | SimpleJWT | 5.2.0 | MIT |
| **Database** | PostgreSQL | Latest | PostgreSQL |
| **Language** | Python | 3.10+ | PSF |

---

## Dependencies

### React (`package.json`)
```json
{
  "dependencies": {
    "@testing-library/jest-dom": "^5.16.5",
    "@testing-library/react": "^13.3.0",
    "@testing-library/user-event": "^13.5.0",
    "axios": "^0.27.2",
    "cors": "^2.8.5",
    "express": "^4.18.1",
    "nodemon": "^2.0.19",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "web-vitals": "^2.1.4"
  }
}
```

### Django (`requirements.txt` - inferred from xamehi.tv pattern)
```text
Django>=4.0,<5.0
djangorestframework>=3.14,<4.0
djangorestframework-simplejwt>=5.2,<6.0
django-cors-headers>=4.0,<5.0
psycopg2-binary>=2.9,<3.0
gunicorn>=20.0,<21.0
whitenoise>=6.0,<7.0
python-dotenv>=1.0,<2.0
```

---

## Ports & Communication

| Service | Port | Protocol | Notes |
|---------|------|----------|-------|
| React Dev | 3000 | HTTP | Proxies API to :5000/:8000 |
| Express | 5000 | HTTP | Supplementary API |
| Django | 8000 | HTTP | Primary API (DRF) |
| PostgreSQL | 5432 | TCP | Shared database |

### CORS Configuration
- Django: `django-cors-headers` for React → Django
- Express: `cors` middleware for React → Express
- Both allow `http://localhost:3000` in development

---

## Project Structure

```
xamehi/
├── frontend/                 # React CRA app
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/         # Axios instances
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   └── package-lock.json
├── backend-express/          # Express server
│   ├── src/
│   │   ├── routes/
│   │   ├── controllers/
│   │   ├── middleware/
│   │   └── index.js          # Entry point
│   ├── package.json
│   └── nodemon.json
├── backend-django/           # Django project
│   ├── config/               # Settings
│   │   ├── base.py
│   │   ├── local.py
│   │   └── production.py
│   ├── apps/                 # Django apps
│   │   ├── core/
│   │   ├── accounts/
│   │   └── api/
│   ├── manage.py
│   ├── requirements.txt
│   └── Pipfile
└── docker-compose.yml        # Optional
```

---

## Commands

### Frontend
```bash
cd frontend
npm install
npm start          # :3000
npm run build      # Production build
npm test           # Jest + Testing Library
```

### Express Backend
```bash
cd backend-express
npm install
npm run server     # nodemon index.js (:5000)
```

### Django Backend
```bash
cd backend-django
pip install -r requirements.txt
# or: pipenv install
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver  # :8000
```

### Full Stack (Development)
```bash
# Terminal 1: Django
cd backend-django && python manage.py runserver

# Terminal 2: Express
cd backend-express && npm run server

# Terminal 3: React
cd frontend && npm start
```

---

## Build & Deploy

### Production Build
```bash
# Frontend
cd frontend && npm run build
# Output: build/

# Django
python manage.py collectstatic
gunicorn config.wsgi:application --bind 0.0.0.0:8000

# Express
NODE_ENV=production node index.js
```

### Docker (Recommended)
```yaml
# docker-compose.yml
services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: xamehi
      POSTGRES_USER: xamehi
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes: [postgres_data:/var/lib/postgresql/data]

  django:
    build: ./backend-django
    command: gunicorn config.wsgi:application --bind 0.0.0.0:8000
    volumes: [./backend-django:/app]
    depends_on: [postgres]

  express:
    build: ./backend-express
    command: node index.js
    volumes: [./backend-express:/app]
    depends_on: [postgres]

  react:
    build: ./frontend
    command: serve -s build -l 3000
    ports: ["3000:3000"]
```

---

## Known Issues & Migration Path

| Issue | Severity | Migration |
|-------|----------|-----------|
| **CRA deprecated** | High | Migrate to Vite or Next.js |
| **Dual backends** | High | Consolidate into Django or Express |
| **React 18 (no Server Components)** | Medium | Next.js 15+ App Router |
| **No TypeScript** | Medium | Add TypeScript |
| **Django 3.x (older)** | Low | Upgrade to 5.x |
| **Separate deployments** | Medium | Single container or platform |

### Recommended Migration
1. **Frontend**: CRA → Next.js 15 (App Router) with TypeScript
2. **Backend**: Consolidate Express endpoints into Django DRF
3. **Database**: Keep PostgreSQL, add Prisma or Drizzle
4. **Auth**: NextAuth.js v5 or Django Allauth
5. **Deploy**: Vercel (frontend) + Railway/Render (backend)

---

## License Summary

| Component | License |
|-----------|---------|
| React/CRA | MIT |
| Express | MIT |
| Django/DRF | BSD / MIT |
| All deps | MIT / BSD |

---

*Generated by Hermes Agent Technology Stack Blueprint Generator*