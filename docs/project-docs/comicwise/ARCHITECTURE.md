# Architecture — comicwise

## System Overview
A Next.js-based comic streaming frontend with TypeScript, Tailwind CSS, and shadcn/ui. The project provides the frontend UI for browsing and reading comics.

## Architecture Layers

### 1. Presentation Layer
- Next.js App Router with route groups
- React Server Components for data fetching
- Client Components for interactivity
- shadcn/ui primitives for consistent UI

### 2. Data Layer
- Drizzle ORM for database operations
- Server Actions for mutations
- TanStack Query for client-side data fetching
- Zustand for client state management

### 3. State Management
- Server State: React Server Components + Server Actions
- Client State: Zustand stores
- Cache State: Upstash Redis

### 4. Authentication
- NextAuth v5 with credentials/OAuth providers
- Session management via JWT
- Protected routes via middleware

### 5. External Services
- ImageKit/Cloudinary for image optimization and storage
- Stripe/PayPal for payments
- Resend for transactional emails
- Sentry for error monitoring
- Upstash for rate limiting and caching

## Data Flow
```
Browser → Next.js App Router → RSC/Server Action → Drizzle ORM → PostgreSQL
                                          ↓
                                    Upstash Redis (cache)
                                          ↓
                                    ImageKit (images)
```
