# xamehi — Technology Stack Blueprint

> **Project:** xamehi — Crypto Currency Dashboard  
> **Generated:** 2024-07-24

---

## 1. Technology Stack Summary

```
┌──────────────────────────────────────────────────────────────┐
│                   XAMEHI TECHNOLOGY STACK                     │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                   PRESENTATION LAYER                  │   │
│  │  ┌──────────┐  ┌───────────┐  ┌──────────────────┐   │   │
│  │  │  React   │  │    CSS3   │  │  HTML5 / JSX     │   │   │
│  │  │  18.2.0  │  │  (Flexbox)│  │  (CRA Template)  │   │   │
│  │  └────┬─────┘  └───────────┘  └──────────────────┘   │   │
│  └───────┼──────────────────────────────────────────────┘   │
│          │                                                 │
│  ┌───────┼──────────────────────────────────────────────┐   │
│  │       │           CLIENT-SIDE LOGIC                   │   │
│  │  ┌────┴─────┐  ┌────────────┐  ┌─────────────────┐   │   │
│  │  │  Axios   │  │ React Hooks│  │  React Testing   │   │   │
│  │  │  0.27.2  │  │ (useState, │  │  Library 13.3.x  │   │   │
│  │  │          │  │ useEffect) │  │                  │   │   │
│  │  └──────────┘  └────────────┘  └─────────────────┘   │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                  API / BFF LAYER                      │   │
│  │  ┌──────────┐  ┌───────────┐  ┌──────────────────┐   │   │
│  │  │ Express  │  │    CORS   │  │  Nodemon 2.0.19  │   │   │
│  │  │  4.18.1  │  │   2.8.5   │  │  (Dev Hot-Reload)│   │   │
│  │  └────┬─────┘  └───────────┘  └──────────────────┘   │   │
│  └───────┼──────────────────────────────────────────────┘   │
│          │                                                 │
│  ┌───────┼──────────────────────────────────────────────┐   │
│  │       │          BACKEND / ADMIN LAYER                │   │
│  │  ┌────┴─────┐  ┌────────────┐  ┌─────────────────┐   │   │
│  │  │  Django  │  │  SQLite3   │  │  Gunicorn (prod)│   │   │
│  │  │  4.0.6   │  │  (dev DB)  │  │  / uWSGI        │   │   │
│  │  └──────────┘  └────────────┘  └─────────────────┘   │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              EXTERNAL INTEGRATIONS                    │   │
│  │  ┌─────────────────────┐  ┌──────────────────────┐   │   │
│  │  │ Alpha Vantage API   │  │ Crypto News Live 3   │   │   │
│  │  │ (via RapidAPI)      │  │ (via RapidAPI)        │   │   │
│  │  └─────────────────────┘  └──────────────────────┘   │   │
│  └──────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────┘
```

---

## 2. Detailed Technology Inventory

### 2.1 Presentation Layer — Frontend

| Technology | Version | Category | Purpose |
|-----------|---------|----------|---------|
| **React** | ^18.2.0 | UI Framework | Component-based SPA with virtual DOM |
| **ReactDOM** | ^18.2.0 | DOM Renderer | `createRoot` API for React 18 concurrent features |
| **Create React App** | react-scripts 5.0.1 | Build Tool | Webpack-based build, dev server, HMR |
| **CSS3** | — | Styling | Flexbox layout, custom properties |
| **HTML5** | — | Markup | Semantic HTML via JSX in CRA template |

### 2.2 Client-Side Logic

| Technology | Version | Category | Purpose |
|-----------|---------|----------|---------|
| **Axios** | ^0.27.2 | HTTP Client | Promise-based requests to Express backend |
| **React Hooks** | 18.2.0 | State Management | `useState` for local state, `useEffect` for data fetching |
| **@testing-library/react** | ^13.3.0 | Testing | Component unit tests |
| **@testing-library/jest-dom** | ^5.16.5 | Testing | Custom DOM matchers for Jest |
| **@testing-library/user-event** | ^13.5.0 | Testing | Simulated user interactions |
| **web-vitals** | ^2.1.4 | Performance | Core Web Vitals measurement |

### 2.3 API / BFF Layer — Express.js

| Technology | Version | Category | Purpose |
|-----------|---------|----------|---------|
| **Express** | ^4.18.1 | Web Framework | HTTP server, routing, middleware |
| **CORS** | ^2.8.5 | Middleware | Cross-origin resource sharing headers |
| **Node.js** | (runtime) | Runtime | JavaScript runtime (version determined by deployment) |
| **Nodemon** | ^2.0.19 | Dev Tool | Auto-restart on file changes |
| **dotenv** | (via Express require) | Config | Load `.env` into `process.env` |
| **Axios** | ^0.27.2 | HTTP Client | Outbound requests to RapidAPI services |

### 2.4 Backend / Admin Layer — Django

| Technology | Version | Category | Purpose |
|-----------|---------|----------|---------|
| **Django** | 4.0.6 | Web Framework | Full-stack Python web framework |
| **Python** | ^3.10+ | Language | Backend programming language |
| **SQLite** | (built-in) | Database | Development database (default) |
| **PostgreSQL** | (intended prod) | Database | Production database (per AGENTS.md) |
| **Gunicorn** | (prod) | WSGI Server | Production Django serving (documented) |
| **Django Admin** | 4.0.6 | Admin UI | Built-in admin interface via `/admin/` |

### 2.5 External Integrations

| Service | Endpoint | Purpose | Authentication |
|---------|----------|---------|---------------|
| **Alpha Vantage** (via RapidAPI) | `https://alpha-vantage.p.rapidapi.com/query` | Real-time currency exchange rates | `X-RapidAPI-Key` header |
| **Crypto News Live 3** (via RapidAPI) | `https://crypto-news-live3.p.rapidapi.com/news` | Cryptocurrency news headlines | `X-RapidAPI-Key` header |

### 2.6 Development Tooling

| Tool | Purpose |
|------|---------|
| **VS Code** | Primary editor (`.vscode/` config provided) |
| **ESLint** | Code linting (react-app config) |
| **Browserslist** | Target browser compatibility matrix |
| **Git** | Version control |

---

## 3. Dependency Relationship Diagram

```mermaid
graph TD
    subgraph "Node.js Ecosystem (npm)"
        package[package.json]
        package --> react[react ^18.2.0]
        package --> react-dom[react-dom ^18.2.0]
        package --> react-scripts[react-scripts 5.0.1]
        package --> axios[axios ^0.27.2]
        package --> express[express ^4.18.1]
        package --> cors[cors ^2.8.5]
        package --> nodemon[nodemon ^2.0.19]
        package --> testing-lib[@testing-library/react ^13.3.0]
        package --> jest-dom[@testing-library/jest-dom ^5.16.5]
        package --> user-event[@testing-library/user-event ^13.5.0]
        package --> web-vitals[web-vitals ^2.1.4]
    end

    subgraph "Python Ecosystem (pip)"
        django[Django 4.0.6]
        django --> sqlite3[SQLite3 - built-in]
        note[Django DRF not yet installed]
    end

    subgraph "External APIs"
        rapidapi[RapidAPI Platform]
        rapidapi --> alphavantage[Alpha Vantage API]
        rapidapi --> cryptonews[Crypto News Live 3]
    end

    note -.->|pending| django
    react-scripts -->|bundles| react
    react-scripts -->|bundles| react-dom
    axios -->|calls| express
    express -->|proxies| rapidapi
```

---

## 4. Runtime Configuration

| Variable | Where Used | Purpose |
|----------|-----------|---------|
| `REACT_APP_RAPID_API_KEY` | Express `index.js` | API key for RapidAPI services |
| `REACT_APP_API_URL` | `.env.example` (intended for React) | Backend API base URL |
| `SECRET_KEY` | Django `settings.py` | Django cryptographic signing |
| `DEBUG` | Django `settings.py` | Debug mode toggle |
| `ALLOWED_HOSTS` | Django `settings.py` | Allowed hostnames |
| `DATABASE_URL` | `.env.example` | Database connection string |
| `NODE_ENV` | `.env.example` | Node environment mode |
| `PORT` | `.env.example` | Development server port |

---

## 5. Version Matrix

| Dependency | package.json (declared) | Actual (resolved) |
|-----------|------------------------|-------------------|
| react | ^18.2.0 | ~18.2.x |
| react-dom | ^18.2.0 | ~18.2.x |
| react-scripts | 5.0.1 | 5.0.1 |
| axios | ^0.27.2 | ~0.27.x |
| express | ^4.18.1 | ~4.18.x |
| cors | ^2.8.5 | ~2.8.x |
| nodemon | ^2.0.19 | ~2.0.x |
| @testing-library/react | ^13.3.0 | ~13.3.x |
| @testing-library/jest-dom | ^5.16.5 | ~5.16.x |
| @testing-library/user-event | ^13.5.0 | ~13.5.x |
| web-vitals | ^2.1.4 | ~2.1.x |

---

## 6. Stack Evaluation & Recommendations

| Layer | Current Score | Issues | Recommended Upgrade |
|-------|--------------|--------|-------------------|
| **React Build** | ⚠️ Outdated | CRA is deprecated; slow builds | Vite 5.x or Next.js 14+ |
| **React Version** | ✅ Current | React 18 is stable | Stay current |
| **Express** | ✅ Stable | Works as BFF; well-tested | Stay or migrate endpoints to Django DRF |
| **Django** | ✅ Current | Django 4.0.6 is stable | Upgrade to 5.x LTS when available |
| **Database** | ⚠️ Dev Only | SQLite in settings ≠ PostgreSQL per docs | Add `psycopg2` and dual-config (dev SQLite, prod PostgreSQL) |
| **State Management** | ⚠️ Limited | Only `useState`/props drilling | Add Zustand, Jotai, or React Context for shared state |
| **Testing** | ⚠️ Configured Only | Testing lib included but no tests written | Add test coverage for all components |
| **Django REST** | ❌ Missing | No DRF or API endpoints | Install `djangorestframework` if Django API is needed |
| **Error Handling** | ⚠️ Minimal | Console.log only | Add error boundaries, toast notifications |
| **Styling** | ⚠️ Basic | Plain CSS, no preprocessor | Add Tailwind CSS or CSS Modules |
| **Linting** | ✅ Configured | ESLint with react-app config | Extend with Prettier, import sorting |
| **CI/CD** | ❌ Missing | No pipeline | Add GitHub Actions for test + build |

---

## 7. Glossary

| Term | Definition |
|------|-----------|
| **BFF** | Backend For Frontend — a dedicated backend API that serves a specific frontend client |
| **CRA** | Create React App — official React scaffolding/build tool (deprecated in favor of frameworks) |
| **DRF** | Django REST Framework — toolkit for building Django REST APIs |
| **RapidAPI** | API marketplace/hub providing unified access to third-party APIs |
| **SPA** | Single-Page Application — client-side rendered web app that loads once, updates dynamically |
| **WSGI/ASGI** | Python web server gateway interfaces (sync and async) |
