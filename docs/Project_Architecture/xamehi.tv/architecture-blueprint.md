# Architecture Blueprint: xamehi.tv

**Generated:** 2026-06-29  
**Generator:** architecture-blueprint-generator  

---

## 1. Architecture Detection and Analysis

### Technology Stack

| Category | Technology |
|---|---|
| **Backend** | Django, Django REST Framework |
| **Frontend** | React 17 |
| **Auth** | SimpleJWT (DRF), django-allauth |
| **State** | Redux (Thunk middleware) |
| **Payments** | PayPal (react-paypal-button-v2) |
| **UI Library** | Material-UI 4, React Bootstrap 1 |
| **Admin** | react-admin 4 |
| **Video Player** | video-react |
| **Database** | PostgreSQL (prod), SQLite (dev) |
| **Filtering** | Django Filter |
| **Static Files** | WhiteNoise |
| **Deployment** | Gunicorn, Procfile |
| **Language** | Python, JavaScript |

### Architectural Pattern Detected

**Pattern:** Django REST API + React SPA with Admin Panel  
The project follows a classic **decoupled architecture**:

- **Backend**: Django REST API with JWT auth and Django admin
- **Frontend**: React 17 SPA with Redux state management
- **Admin**: react-admin interface for content management
- **Payment**: PayPal integration for premium content

---

## 2. Architectural Overview

### System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                   Client Browser                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │            React 17 SPA (frontend/build/)               │  │
│  │  ┌───────────┐  ┌───────────┐  ┌───────────────────┐  │  │
│  │  │ Components │  │  Redux    │  │  API Services     │  │  │
│  │  │ (MUI+BS)   │  │  Store    │  │  (Axios)          │  │  │
│  │  └───────────┘  └───────────┘  └───────────────────┘  │  │
│  │  ┌───────────┐  ┌───────────┐                          │  │
│  │  │ video-    │  │ react-    │                          │  │
│  │  │ react     │  │ admin     │                          │  │
│  │  └───────────┘  └───────────┘                          │  │
│  └────────────────────┬───────────────────────────────────┘  │
│                       │ REST API (JWT Auth)                   │
└───────────────────────┼───────────────────────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────────────────────┐
│                  Django Backend Server                        │
│  ┌──────────┐  ┌──────────────┐  ┌────────────────────┐     │
│  │  Views   │  │  Serializers │  │  URL Routing       │     │
│  └──────────┘  └──────────────┘  └────────────────────┘     │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  django-allauth + DRF SimpleJWT (Auth)               │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  WhiteNoise + django-filter + django-storages        │   │
│  └──────────────────────────────────────────────────────┘   │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                    Database Layer                             │
│  ┌──────────────────────┐  ┌──────────────────────────────┐  │
│  │  PostgreSQL (prod)   │  │  Cloud Storage (django-      │  │
│  │  SQLite (dev)        │  │  storages) for media         │  │
│  └──────────────────────┘  └──────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

---

## 3. Key Architectural Decisions

| Decision | Rationale |
|---|---|
| DRF + SimpleJWT | Standard REST API authentication |
| React 17 + Redux | Mature ecosystem, predictable state |
| Material-UI 4 + React Bootstrap | Rich UI component library |
| react-admin 4 | Admin panel without custom dashboard |
| PayPal integration | Monetization for premium content |
| video-react player | Video streaming with React integration |

---

## 4. Data Flow

### Movie Discovery Flow
```
User → React Component → Redux Action → API Call (Axios/Redux Thunk) → DRF ViewSet
                                                                         ↓
                                                                   Serializer
                                                                         ↓
                                                                   Django Model → Database
                                                                         ↓
                                                                   Response → Reducer → Component Re-render
```

### Authentication Flow
```
Login → DRF SimpleJWT → JWT Token → Stored in localStorage → Attached to API requests
```

---

## 5. Implementation Patterns

### Redux Pattern
```
constants/ (action types) → actions/ (action creators) → reducers/ (state changes)
```

### DRF ViewSet Pattern
```python
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['genre', 'year']
```

### React Component Pattern
```jsx
function MovieList() {
  const dispatch = useDispatch();
  const movies = useSelector(state => state.movies);
  
  useEffect(() => {
    dispatch(fetchMovies());
  }, [dispatch]);
  
  return <MovieListUI movies={movies} />;
}
```

---

## 6. Database Models

| Model | Purpose |
|---|---|
| Movie | Movie metadata (title, description, genre, year) |
| Review | User reviews and ratings |
| UserProfile | Extended user profile data |
| Payment | PayPal transaction records |

---

## 7. Extensibility Points

1. **New content types**: Add TV series, documentaries models
2. **Additional payment gateways**: Follow PayPal pattern
3. **Enhanced search**: Integrate with Elasticsearch or Algolia
4. **Streaming quality options**: Add adaptive bitrate streaming

---

*End of architecture blueprint.*
