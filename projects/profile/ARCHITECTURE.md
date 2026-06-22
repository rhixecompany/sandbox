# Architecture — profile

## Overview
A Django-based blog/profile website with rich content editing capabilities and cloud storage integration.

## Architecture Layers

### 1. Django Backend
- **Views**: Class-based views for most endpoints
- **Models**: Profile, Post, Tag, PostComment with proper relationships
- **Admin**: Customized ModelAdmin with list_display, search_fields, list_filter
- **Forms**: django-crispy-forms with Bootstrap rendering

### 2. Content Management
- **CKEditor**: WYSIWYG editor for post content
- **Tagging**: Many-to-many tag relationships
- **Comments**: Threaded comments on posts

### 3. Storage Layer
- **Local**: Media files during development
- **Cloud**: Google Cloud Storage (or AWS S3) in production
- **Static**: WhiteNoise for static file serving

### 4. URL Structure
- Namespaced app-level URL configs
- Clean URL patterns for blog posts (`/blog/<slug>/`)
- Admin interface at `/admin/`
