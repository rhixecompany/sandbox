# Architecture — university-libary-jsm

## Overview
A full-stack library management system (BookWise) with serverless PostgreSQL, Redis caching, and async workflows.

## Architecture Layers

### 1. Presentation Layer
- Next.js 15 App Router with Turbopack
- shadcn/ui component library
- Tailwind CSS 4 for styling
- Server Components by default, Client Components for interactivity

### 2. Application Layer
- **Server Actions**: All mutations handled via Next.js Server Actions
- **Validation**: Zod 4 schema validation at all entry points
- **DAL**: Data Access Layer via Drizzle ORM with Zod integration

### 3. Data Layer
- **Database**: Neon serverless PostgreSQL via Drizzle ORM
- **Cache**: Upstash Redis for rate limiting and caching
- **Jobs**: Upstash Workflow + QStash for async processing

### 4. Authentication
- NextAuth v5 for session management
- Protected routes via `auth()` helper
- Rate limiting via Upstash Ratelimit

### 5. External Services
- ImageKit for image uploads and optimization
- React Email + Nodemailer for email notifications

## Data Flow
```
Browser → Server Action → Zod Validation → Drizzle ORM → Neon PostgreSQL
                                    ↓
                              Upstash Redis (rate limit)
                                    ↓
                              Upstash Workflow (async)
                                    ↓
                              ImageKit (media)
```
