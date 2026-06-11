# Architecture — xamehi

## Overview
A full-stack web application with a unique dual-backend architecture combining Django and Express.js.

## Architecture Layers

### 1. Dual Backend Architecture
- **Django**: Main application backend with ORM, admin, and REST API
- **Express.js**: Secondary backend for specific API routes/services

### 2. Frontend (React 18)
- Create React App setup
- Axios for HTTP communication with both backends
- Standard CSS styling (no CSS framework detected)

### 3. Data Flow
```
Browser → React SPA → Axios ──→ Express.js (:5000)
                           └──→ Django REST (:8000)
                                      ↓
                                PostgreSQL
```

### 4. Service Communication
- Frontend communicates with both backends via HTTP
- Django handles primary data operations via ORM
- Express.js provides additional API endpoints
- Both backends can potentially access the same PostgreSQL database

## Key Design Decisions
1. Dual backends for separation of concerns
2. No CSS framework — plain CSS
3. Create React App for frontend scaffolding
4. CommonJS in Express, ES6 in React
