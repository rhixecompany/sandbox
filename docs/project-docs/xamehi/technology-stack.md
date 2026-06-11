# Technology Stack — xamehi

## Overview
Full-stack web application with dual-backend architecture: Django (Python) + Express.js (Node.js) + React frontend.

## Backend 1 — Django
| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.10+ | Runtime |
| Django | — | Web framework |
| Django REST Framework | — | REST API |
| PostgreSQL | — | Database |

## Backend 2 — Express.js
| Technology | Version | Purpose |
|------------|---------|---------|
| Node.js | 18+ | Runtime |
| Express.js | 4.18.1 | HTTP server |
| Nodemon | 2.0.19 | Dev auto-restart |
| CORS | 2.8.5 | Cross-origin support |

## Frontend
| Technology | Version | Purpose |
|------------|---------|---------|
| React | 18.2.0 | UI library (Create React App) |
| Axios | 0.27.2 | HTTP client |
| React Scripts | 5.0.1 | Build tooling |

## Database
| Technology | Purpose |
|------------|---------|
| PostgreSQL | Production database (via Django ORM) |

## Service Ports
| Service | Default Port |
|---------|-------------|
| Express backend | 5000 |
| Django backend | 8000 |
| React frontend | 3000 |
