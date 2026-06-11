# Architecture — xamehi.tv

## Overview
A movie/television streaming website with Django REST backend and React 17 frontend.

## Architecture

### 1. Backend (Django REST)
- **API**: DRF ViewSets and Serializers for movies, reviews, users
- **Auth**: SimpleJWT for API authentication
- **Media**: video-react for video playback
- **Admin**: django-allauth for social auth, react-admin for admin panel

### 2. Frontend (React 17 + Redux)
- **UI**: Material-UI 4 components with React Bootstrap
- **State**: Redux with Thunk middleware
- **Routing**: React Router v5
- **API**: Axios proxied through React dev server

### 3. Data Flow
```
User → React SPA → Axios API calls (proxy) → Django REST API → PostgreSQL
                        ↓                                      ↓
                   Redux Store ←──────────────────────── JSON Response
```

## Key Features
- Movie/listing with carousels and pagination
- User reviews and ratings
- Search functionality
- PayPal payment integration
- Admin management via react-admin
