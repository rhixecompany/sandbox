# Architecture — Banking

## System Overview

The Banking application follows a modern Next.js 16 architecture with App Router, featuring a clean separation of concerns through Server Actions, Data Access Layer, and external integrations.

## Architecture Layers

### 1. Presentation Layer (App Router)
- **Pages**: Route groups for `(auth)`, `(root)`, `(admin)`
- **Components**: Reusable React components using shadcn/ui
- **Layouts**: Nested layouts for auth, dashboard, and admin sections

### 2. Action Layer (Server Actions)
- All mutations go through Next.js Server Actions
- Input validation via Zod schemas at each entry point
- Returns `{ ok: boolean, error?: string, data?: T }` pattern
- Files named with `dot.camelCase` convention (e.g., `auth.signin.ts`)

### 3. Data Access Layer (DAL)
- Constructor-based DAL classes for type-safe database operations
- Each DAL encapsulates queries for a specific entity
- Exported as singleton instances (e.g., `userDal`)

### 4. Database Layer (Drizzle ORM)
- PostgreSQL database with Drizzle ORM schema definitions
- Tables: `users`, `user_profiles`, `banks`, `transactions`, `recipients`
- Soft-delete support on user data
- Migrations managed via Drizzle Kit

### 5. External Integrations
- **Plaid**: Bank account linking (link token → public_token → access_token)
- **Dwolla**: ACH transfers via Dwolla API
- **Upstash**: Redis-based rate limiting

## Data Flow

```
User → React Component → Server Action → Zod Validation → DAL → Drizzle ORM → PostgreSQL
                                                        ↕
                                              Plaid API / Dwolla API
```

## Key Design Decisions

1. **Server Actions over API Routes**: All mutations use Server Actions for better type safety and co-location
2. **DAL pattern**: Centralizes database queries for testability and reusability
3. **Zod validation at boundaries**: Every external input is validated at the action boundary
4. **Soft delete**: Never hard-deletes user data for audit trail compliance
5. **Idempotency**: Financial transactions implement idempotency keys
