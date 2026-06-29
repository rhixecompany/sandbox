# Architecture Blueprint: university-libary-jsm (BookWise)

**Generated:** 2026-06-29  
**Generator:** architecture-blueprint-generator  

---

## 1. Architecture Detection and Analysis

### Technology Stack

| Category | Technology |
|---|---|
| **Frontend** | Next.js 15 (App Router, Turbopack), React 19 |
| **Language** | TypeScript 5 (strict) |
| **Database** | Neon PostgreSQL (serverless) |
| **ORM** | Drizzle ORM (with Zod integration) |
| **Authentication** | NextAuth v5 (beta) |
| **Rate Limiting** | Upstash Ratelimit + Upstash Redis |
| **Async Workflows** | Upstash Workflow + QStash |
| **Image Storage** | ImageKit |
| **Email** | React Email + Nodemailer |
| **Validation** | Zod 4 |
| **UI Components** | shadcn/ui, Radix UI primitives |
| **Styling** | Tailwind CSS 4 |
| **Forms** | React Hook Form + Zod resolvers |
| **Drag-and-Drop** | @dnd-kit |
| **Data Tables** | @tanstack/react-table |
| **Charts** | recharts |

### Architectural Pattern Detected

**Pattern:** Modern Next.js Full-Stack with Serverless Services  
The project follows a **serverless-first architecture** using:

- **Server Actions**: All mutations via Next.js Server Actions
- **Serverless Database**: Neon PostgreSQL (serverless Postgres)
- **Serverless Cache/Queue**: Upstash Redis + Workflow
- **Server Components**: Default React paradigm
- **Server Actions**: Drizzle ORM with Zod input validation

---

## 2. Architectural Overview

### Architecture Layers

```
┌──────────────────────────────────────────────────────────────┐
│                    Presentation Layer                         │
│  Next.js 15 App Router + Turbopack                           │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  Server Components (default) → Client Components (on)  │  │
│  │  shadcn/ui + Tailwind CSS 4 + Radix UI primitives      │  │
│  └────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                    Application Layer                          │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  Server Actions (all mutations) → Zod 4 → DAL          │  │
│  │  NextAuth v5 → Upstash Ratelimit                       │  │
│  └────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                      Data Layer                               │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐  │
│  │  Neon          │  │  Upstash       │  │  Upstash       │  │
│  │  PostgreSQL    │  │  Redis (cache) │  │  Workflow      │  │
│  │  + Drizzle ORM │  │  + Ratelimit   │  │  + QStash      │  │
│  └────────────────┘  └────────────────┘  └────────────────┘  │
│  ┌────────────────┐  ┌────────────────┐                      │
│  │  ImageKit      │  │  Nodemailer   │                      │
│  │  (media)       │  │  (email)      │                      │
│  └────────────────┘  └────────────────┘                      │
└──────────────────────────────────────────────────────────────┘
```

---

## 3. Key Architectural Decisions

| Decision | Rationale |
|---|---|
| Drizzle ORM over Prisma | Lighter weight, SQL-like, better Zod integration |
| Neon PostgreSQL | Serverless database, auto-scaling |
| Upstash Workflow + QStash | Async job processing without managing Celery |
| NextAuth v5 with Upstash | Rate-limited authentication |
| Server Actions over API routes | Co-located logic, type-safe, no HTTP overhead |

---

## 4. Data Flow

```
Browser → Server Action → Zod Validation → Drizzle ORM → Neon PostgreSQL
                         ↓
                   Upstash Redis (rate limit check)
                         ↓
                   Upstash Workflow (async job)
                         ↓
                   ImageKit (media upload) / Nodemailer (email)
```

---

## 5. Implementation Patterns

### Server Action with Rate Limiting
```typescript
"use server";
import { ratelimit } from "@/lib/ratelimit";
import { z } from "zod";
import { db } from "@/database/db";

export async function createBook(input: unknown) {
  const { success } = await ratelimit.limit("create-book");
  if (!success) throw new Error("Too many requests");
  
  const parsed = schema.safeParse(input);
  // ... database operation
}
```

### Database Access Layer
```typescript
import { db } from "@/database/db";
import { books } from "@/database/schema";

export async function getBooks() {
  return db.select().from(books);
}
```

---

## 6. Database Schema

| Table | Purpose |
|---|---|
| `books` | Library book catalog |
| `users` | User accounts |
| `borrow_records` | Book borrowing history |
| `requests` | Book reservation requests |

---

## 7. Extensibility Points

1. **New library features**: Add Server Actions + Drizzle schema migrations
2. **Additional external services**: Follow ImageKit/Nodemailer integration patterns
3. **New UI components**: Use shadcn/ui primitives, add to components library
4. **Enhanced workflows**: Add Upstash Workflow for complex async processes

---

*End of architecture blueprint.*
