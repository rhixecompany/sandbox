# Ecom — Research Report

> **Project**: RhixeCompany Ecommerce — Full-Stack Ecommerce Platform  
> **Date**: 2026-06-29  
> **Source**: Project code analysis + web research (June 2026)

## 1. Project Overview

A production-ready ecommerce platform featuring product catalog, shopping cart, user reviews, PayPal checkout, and an admin dashboard. The architecture follows a decoupled **Django REST backend + React/Redux SPA frontend** pattern, communicating over a JSON API.

## 2. Tech Stack Summary

| Layer | Technology | Version |
|-------|-----------|---------|
| Backend | Django / DRF | 3.1.14 / 3.13.1 |
| Auth | djangorestframework-simplejwt | 5.2.0 |
| Frontend | React / Redux / React Bootstrap | 18.2 / 4.2.1 / 2.8 |
| Router | React Router DOM | v5 |
| Payments | react-paypal-button-v2 | 2.6.3 |
| HTTP | Axios | 1.4 |
| DB (dev) | SQLite | — |
| DB (prod) | PostgreSQL via psycopg2-binary | 2.9 |
| Storage | AWS S3 (django-storages + boto3) | 1.12 / 1.14 |
| Deployment | Gunicorn + WhiteNoise + Procfile | 20.1 |

## 3. Architecture & API Design

The API follows **DRF ViewSets + Serializers** with JWT token authentication. Three core endpoint groups:

- **`/api/users/`** — Registration, login (JWT obtain/refresh), profile management
- **`/api/products/`** — Product CRUD, search/filter (django-filter), reviews/ratings, image uploads (via django-ckeditor)
- **`/api/orders/`** — Cart operations, order placement, PayPal payment confirmation, order history

The React proxy (`package.json` → `http://127.0.0.1:9000`) forwards API calls during development. Production serves the built frontend via Django's `TemplateView` or a separate CDN.

## 4. Authentication (DRF + SimpleJWT)

Uses short-lived access tokens + refresh tokens for stateless auth. CORS configured with `django-cors-headers`. **2026 recommendations:** enable `ROTATE_REFRESH_TOKENS` + `BLACKLIST_AFTER_ROTATION`, set access tokens to 15-30 min, and add 2FA for admin accounts.

## 5. Frontend State Management (React + Redux Thunk)

Classic Redux with `redux-thunk`: `screens → dispatch → action creator (axios) → reducer → re-render`. State slices: products, cart (server-side persisted), user/auth, orders. Cart lives server-side for cross-device consistency. Redux DevTools enabled.

## 6. Payment Integration (PayPal)

Uses `react-paypal-button-v2` (v2.6.3). Flow: create order via API → PayPal popup → backend verifies + captures payment. **2026 finding:** `@paypal/react-paypal-js` is now the official recommended SDK (better TS support, PayPal Pay Later, Venmo). Server-side verification is critical.

## 7. Deployment Strategy

**Heroku-ready** via `Procfile` (Gunicorn 20.1 + WhiteNoise). Media via django-storages + S3/GCS. Prod DB: PostgreSQL. Secrets via `python-dotenv`. **2026 checklist:** `DEBUG=False`, locked `ALLOWED_HOSTS`, restricted CORS origins, CDN for static files, nginx reverse-proxy for advanced use cases.

## 8. Key Findings & Recommendations

| Area | Current State | Recommendation |
|------|-------------|---------------|
| **PayPal SDK** | react-paypal-button-v2 | Migrate to `@paypal/react-paypal-js` for official support |
| **Redux** | Classic Redux + Thunk | Consider Redux Toolkit (RTK) for less boilerplate |
| **JWT** | Basic SimpleJWT | Enable token rotation + blacklisting |
| **Static files** | WhiteNoise only | Add CDN (CloudFront/Cloudflare) for production |
| **Testing** | Django `manage.py test` + Jest | Add API integration tests; increase frontend coverage |
| **Docker** | Mentioned in context | Add `Dockerfile` and `docker-compose.yml` for reproducible deploy |

---

*Research conducted via project code audit and web search on DRF+React ecommerce architectures, PayPal integration patterns, JWT best practices, Redux state management, and Django production deployment (June 2026).*
