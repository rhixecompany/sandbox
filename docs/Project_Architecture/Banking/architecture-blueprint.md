# Architecture Blueprint: Banking

**Generated:** 2026-06-29  
**Generator:** architecture-blueprint-generator  

---

## 1. Architecture Detection and Analysis

### Technology Stack

| Category | Technology |
|---|---|
| **Framework** | Next.js 16 (App Router) |
| **Language** | TypeScript (strict mode) |
| **Database** | PostgreSQL |
| **ORM** | Drizzle ORM (with Zod integration) |
| **Authentication** | NextAuth v4 (credentials provider) |
| **State Management** | Zustand |
| **Validation** | Zod |
| **Banking Integration** | Plaid (bank linking) |
| **ACH Transfers** | Dwolla |
| **UI Components** | shadcn/ui (Radix UI primitives) |
| **Styling** | Tailwind CSS |
| **Package Manager** | Bun |
| **Testing** | Playwright (E2E), Vitest (unit) |

### Architectural Pattern Detected

**Pattern:** Layered Architecture with Server Actions  
The project follows a modern Next.js App Router pattern with clearly separated layers:
- **Presentation Layer**: React Server Components + Client Components
- **Application Layer**: Next.js Server Actions (all mutations)
- **Data Access Layer**: DAL classes with constructor pattern
- **Data Layer**: Drizzle ORM → PostgreSQL

### Dependency Flow

```
Browser → Next.js App Router → RSC (data fetching) / Server Action (mutations)
                                    ↓
                              DAL Classes → Drizzle ORM → PostgreSQL
                                    ↓
                        External APIs: Plaid ↔ Dwolla
```

---

## 2. Architectural Overview

### Guiding Principles

1. **Server-first mutations**: All data writes use Next.js Server Actions with Zod validation
2. **DAL abstraction**: Data Access Layer classes encapsulate all database queries
3. **Type safety**: TypeScript strict mode + Zod schemas at every entry point
4. **Security-first**: Encrypted storage for banking credentials, soft-delete for user data
5. **Idempotency**: Financial transactions implement idempotency keys

### Key Architectural Decisions

| Decision | Rationale |
|---|---|
| Server Actions over API routes | Better type safety, co-located logic, no HTTP overhead |
| Drizzle ORM over Prisma | Lighter weight, SQL-like syntax, better TypeScript integration |
| Zustand over Redux | Minimal boilerplate, sufficient for client state needs |
| Plaid + Dwolla | Industry standard for banking data + ACH transfers |

---

## 3. Architecture Visualization

### Component Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    Next.js 16 App Router                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────────┐  │
│  │  (auth)/ │  │  (root)/ │  │  (admin)/│  │  api/       │  │
│  │ signin/  │  │dashboard/│  │ panel/   │  │  routes     │  │
│  │ signup/  │  │ wallets/ │  │          │  │             │  │
│  │          │  │ txns/    │  │          │  │             │  │
│  └──────────┘  └──────────┘  └──────────┘  └─────────────┘  │
└─────────────────────────────────────────────────────────────┘
         │              │              │              │
         ▼              ▼              ▼              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Server Actions Layer                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────────┐  │
│  │ auth.*   │  │ plaid.*  │  │ dwolla.* │  │  register.* │  │
│  └──────────┘  └──────────┘  └──────────┘  └─────────────┘  │
└─────────────────────────────────────────────────────────────┘
         │              │              │              │
         ▼              ▼              ▼              ▼
┌─────────────────────────────────────────────────────────────┐
│                      DAL Layer                                │
│              ┌────────────────────────────┐                   │
│              │  UserDAL, TransactionDAL,  │                   │
│              │  BankDAL, RecipientDAL     │                   │
│              └────────────────────────────┘                   │
└─────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│                      Data Layer                               │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐  │
│  │   PostgreSQL   │  │   Drizzle ORM  │  │   Zustand      │  │
│  │   (Database)   │  │   (Queries)    │  │   (Client)     │  │
│  └────────────────┘  └────────────────┘  └────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. Implementation Patterns

### Server Action Pattern

```typescript
// actions/auth.signin.ts
"use server";
import { z } from "zod";
import { db } from "@/database/db";
import { users } from "@/database/schema";

const Schema = z.object({ email: z.string().email(), password: z.string().min(8) });

export async function signIn(input: unknown) {
  const parsed = Schema.safeParse(input);
  if (!parsed.success) return { error: parsed.error.errors[0]?.message };
  // ... business logic
}
```

### DAL Pattern

```typescript
// dal/user.dal.ts
export class UserDAL {
  async findByEmail(email: string) {
    return db.select().from(users).where(eq(users.email, email)).limit(1);
  }
}
export const userDal = new UserDAL();
```

---

## 5. Database Schema

| Table | Purpose |
|---|---|
| `users` | Core user data with soft-delete |
| `user_profiles` | Extended user profile data |
| `banks` | Connected bank accounts (Plaid) |
| `transactions` | All financial transactions |
| `recipients` | Saved transfer recipients |

---

## 6. Extensibility Points

1. **New payment providers**: Add new Server Actions following the existing Plaid/Dwolla patterns
2. **New database tables**: Add schema → generate migration → create DAL class
3. **New UI components**: Create in `src/components/` using shadcn/ui primitives
4. **Admin features**: Add routes under `(admin)/` route group

---

*End of architecture blueprint.*
