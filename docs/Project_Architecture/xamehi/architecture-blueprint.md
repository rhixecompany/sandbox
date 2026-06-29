# Architecture Blueprint: xamehi

**Generated:** 2026-06-29  
**Generator:** architecture-blueprint-generator  

---

## 1. Architecture Detection and Analysis

### Technology Stack

| Category | Technology |
|---|---|
| **Frontend** | React 18 (Create React App) |
| **Backend 1** | Express.js (Node.js) |
| **Backend 2** | Django + Django REST Framework (Python) |
| **Language** | JavaScript (React/Express), Python (Django) |
| **Database** | PostgreSQL (via Django ORM) |
| **HTTP Client** | Axios |
| **Dev Server** | Nodemon (Express) |
| **CORS** | cors middleware (Express) |
| **Styling** | Standard CSS |
| **Testing** | React Testing Library, Django TestCase |
| **Package Manager** | npm, pip |

### Architectural Pattern Detected

**Pattern:** Dual-Backend Architecture with SPA Frontend  
The project has a **unique dual-backend design**:

- **React Frontend (CRA)**: SPA served on port 3000
- **Express Backend**: Node.js API server (port 5000)
- **Django Backend**: Python API server (port 8000)
- **Communication**: Axios HTTP from frontend to both backends

---

## 2. Architectural Overview

### System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                   Client Browser                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │              React 18 SPA (frontend/)                   │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │  │
│  │  │ Components   │  │    Hooks     │  │   Services   │ │  │
│  │  └──────────────┘  └──────────────┘  └──────────────┘ │  │
│  └────────────────────┬───────────────────────────────────┘  │
│                       │ Axios HTTP                            │
└───────────────────────┼───────────────────────────────────────┘
          ┌─────────────┴─────────────┐
          ▼                           ▼
┌──────────────────┐      ┌──────────────────────────┐
│  Express.js      │      │  Django + DRF             │
│  (index.js)      │      │  (manage.py)              │
│  Port: 5000      │      │  Port: 8000               │
│  Node.js API     │      │  Python API + Admin       │
│  CORS enabled    │      │  PostgreSQL Database      │
│  Nodemon (dev)   │      │  Django ORM               │
└──────────────────┘      └──────────────────────────┘
                                    │
                                    ▼
                          ┌──────────────────┐
                          │   PostgreSQL     │
                          │   (Database)     │
                          └──────────────────┘
```

---

## 3. Key Architectural Decisions

| Decision | Rationale |
|---|---|
| Dual-backend (Express + Django) | Express for lightweight API, Django for ORM/admin |
| Create React App | Standard React tooling, no custom webpack config |
| Axios for HTTP | Promise-based, interceptor support |
| CORS enabled | Cross-origin requests between frontend and backends |

---

## 4. Data Flow

```
User Action → React Component → Axios → Express/Django → Database
                                              ↓
                                        Response JSON → Component Re-render
```

---

## 5. Development Workflow

Three concurrent dev servers:
- **Terminal 1**: `node index.js` (Express on port 5000)
- **Terminal 2**: `python manage.py runserver` (Django on port 8000)
- **Terminal 3**: `npm start` (React on port 3000)

---

## 6. Extensibility Points

1. **API consolidation**: Migrate Express routes to Django REST Framework
2. **Frontend upgrade**: Migrate from CRA to Next.js or Vite
3. **Additional backends**: Follow existing patterns for new services
4. **State management**: Add Redux or Zustand for complex UI state

---

*End of architecture blueprint.*
