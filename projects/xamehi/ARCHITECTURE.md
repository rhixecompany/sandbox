# Architecture — xamehi

## Overview

xamehi is a full-stack web application combining a React frontend with an Express.js backend API server. The application provides a modern single-page application experience with server-side API support.

## System Architecture

```
┌─────────────────────────────────────────────────┐
│                   Client Browser                 │
│  ┌─────────────────────────────────────────────┐ │
│  │           React Frontend (SPA)               │ │
│  │  ┌───────────┐  ┌──────────┐  ┌───────────┐ │ │
│  │  │ Components│  │  Hooks   │  │  Services │ │ │
│  │  └───────────┘  └──────────┘  └───────────┘ │ │
│  └──────────────────────┬──────────────────────┘ │
│                         │ HTTP/Axios              │
└─────────────────────────┼─────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────┐
│           Express.js Backend Server              │
│  ┌───────────┐  ┌──────────┐  ┌───────────────┐ │
│  │  Routes   │  │ Middleware│  │  Controllers  │ │
│  └───────────┘  └──────────┘  └───────────────┘ │
└─────────────────────────────────────────────────┘
```

## Key Technical Decisions

### React Frontend

- **React 18** with functional components and hooks
- **react-scripts** (Create React App) for build tooling
- **Axios** for HTTP client communication with backend
- **Testing Library** for component testing

### Express Backend

- **Express.js** for REST API server
- **CORS** enabled for cross-origin frontend requests
- **Nodemon** for hot-reload during development
- **manage.py** suggests Django integration potential

## Component Relationships

### Frontend (`src/`)

- React components organized under `src/`
- Public assets served from `public/`
- Entry point via `src/index.js` (standard CRA pattern)

### Backend (`index.js`)

- Express server entry point
- Handles API routes and business logic
- CORS configured for frontend communication

## Development Workflow

```bash
# Start backend API server
npm run server    # nodemon index.js

# Start React frontend (separate terminal)
npm start         # react-scripts start
```

## Dependencies

| Package | Purpose |
|---------|---------|
| react, react-dom | UI framework |
| express | Backend API server |
| axios | HTTP client |
| cors | Cross-origin resource sharing |
| nodemon | Development hot-reload |
| react-scripts | Build tooling |

## Deployment Considerations

- Frontend: Static hosting (Netlify, Vercel, S3)
- Backend: Node.js hosting (Heroku, Railway, Render)
- Environment variables for API URLs and configuration
# Architecture — xamehi

## Overview

xamehi is a full-stack web application combining a React frontend with an Express.js backend API server. The application provides a modern single-page application experience with server-side API support.

## System Architecture

```
┌─────────────────────────────────────────────────┐
│                   Client Browser                 │
│  ┌─────────────────────────────────────────────┐ │
│  │           React Frontend (SPA)               │ │
│  │  ┌───────────┐  ┌──────────┐  ┌───────────┐ │ │
│  │  │ Components│  │  Hooks   │  │  Services │ │ │
│  │  └───────────┘  └──────────┘  └───────────┘ │ │
│  └──────────────────────┬──────────────────────┘ │
│                         │ HTTP/Axios              │
└─────────────────────────┼─────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────┐
│           Express.js Backend Server              │
│  ┌───────────┐  ┌──────────┐  ┌───────────────┐ │
│  │  Routes   │  │ Middleware│  │  Controllers  │ │
│  └───────────┘  └──────────┘  └───────────────┘ │
└─────────────────────────────────────────────────┘
```

## Key Technical Decisions

### React Frontend

- **React 18** with functional components and hooks
- **react-scripts** (Create React App) for build tooling
- **Axios** for HTTP client communication with backend
- **Testing Library** for component testing

### Express Backend

- **Express.js** for REST API server
- **CORS** enabled for cross-origin frontend requests
- **Nodemon** for hot-reload during development
- **manage.py** suggests Django integration potential

## Component Relationships

### Frontend (`src/`)

- React components organized under `src/`
- Public assets served from `public/`
- Entry point via `src/index.js` (standard CRA pattern)

### Backend (`index.js`)

- Express server entry point
- Handles API routes and business logic
- CORS configured for frontend communication

## Development Workflow

```bash
# Start backend API server
npm run server    # nodemon index.js

# Start React frontend (separate terminal)
npm start         # react-scripts start
```

## Dependencies

| Package | Purpose |
|---------|---------|
| react, react-dom | UI framework |
| express | Backend API server |
| axios | HTTP client |
| cors | Cross-origin resource sharing |
| nodemon | Development hot-reload |
| react-scripts | Build tooling |

## Deployment Considerations

- Frontend: Static hosting (Netlify, Vercel, S3)
- Backend: Node.js hosting (Heroku, Railway, Render)
- Environment variables for API URLs and configuration
