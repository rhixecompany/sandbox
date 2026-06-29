# Architecture Blueprint: ecom

**Generated:** 2026-06-29  
**Generator:** architecture-blueprint-generator  

---

## 1. Architecture Detection and Analysis

### Technology Stack

| Category | Technology |
|---|---|
| **Backend** | Django 3.1, Django REST Framework |
| **Frontend** | React 18, Redux (Thunk) |
| **Auth** | SimpleJWT (djangorestframework-simplejwt) |
| **Payments** | PayPal (react-paypal-button-v2) |
| **Database** | SQLite (dev), PostgreSQL (prod) |
| **Storage** | AWS S3 / Google Cloud Storage |
| **Deployment** | Gunicorn, WhiteNoise, Procfile |
| **Language** | Python 3.10, JavaScript |
| **Frontend UI** | React Bootstrap, React Router v5 |
| **CORS** | django-cors-headers |

### Architectural Pattern Detected

**Pattern:** Monolithic Django REST API + SPA Frontend  
The project follows a classic **decoupled frontend/backend** architecture:

- **Backend**: Django REST API server with JWT authentication
- **Frontend**: React SPA served separately (development) or via Django (production)
- **Communication**: REST API over HTTP with JWT tokens

---

## 2. Architectural Overview

### System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                   Client Browser                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │              React SPA (frontend/)                      │  │
│  │  ┌─────────┐  ┌────────┐  ┌────────┐  ┌────────────┐  │  │
│  │  │Screens │  │Actions │  │Reducers│  │ Constants  │  │  │
│  │  └─────────┘  └────────┘  └────────┘  └────────────┘  │  │
│  └────────────────────┬───────────────────────────────────┘  │
│                       │ REST API (JWT Auth)                   │
└───────────────────────┼───────────────────────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────────────────────┐
│                  Django REST API Server                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────────┐  │
│  │ViewSets  │  │Serializers│  │  Models  │  │  JWT Auth   │  │
│  └──────────┘  └──────────┘  └──────────┘  └─────────────┘  │
└──────────────────────────────────────────────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────────────────────┐
│                     Database Layer                            │
│  ┌───────────────┐  ┌────────────────────────────────────┐   │
│  │  PostgreSQL   │  │  AWS S3 / GCS (Media Storage)      │   │
│  └───────────────┘  └────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────┘
```

---

## 3. Key Architectural Decisions

| Decision | Rationale |
|---|---|
| Django REST + React SPA | Clean separation, independent scaling |
| Redux with Thunk | Predictable state management for complex cart flows |
| PayPal integration | Widely used payment gateway |
| SimpleJWT | Lightweight JWT auth without OAuth complexity |

---

## 4. Data Flow

### Shopping Flow
```
User → React Component → Redux Action → API Call (Axios) → DRF ViewSet
                                                               ↓
                                                         Serializer
                                                               ↓
                                                         Django Model → Database
```

### Payment Flow
```
User → PayPal Button → PayPal SDK → Backend Webhook → Order Update → Database
```

---

## 5. Implementation Patterns

### Redux Pattern
```
constants/ → action creators → reducers → store → components
```

### DRF ViewSet Pattern
```python
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
```

---

## 6. Extensibility Points

1. **New product types**: Add Django models + DRF ViewSets
2. **Additional payment gateways**: Follow PayPal integration pattern
3. **New frontend features**: Add React components following Redux pattern
4. **API versioning**: Add `/api/v2/` namespace for breaking changes

---

*End of architecture blueprint.*
