# 1. Project Architecture

> Extracted from `setup.prompt.md`.

## 1. Project Architecture

### Directory Layout

```
src/
├── app/                    # Next.js App Router pages
│   ├── (auth)/             # Auth route group (signin, signup, etc.)
│   ├── (root)/             # Main app routes (comics, chapters, profile)
│   ├── admin/              # Admin dashboard
│   ├── api/                # API route handlers
│   │   ├── auth/[...nextauth]/route.ts   # NextAuth handler
│   │   └── seed/route.ts                 # Seed REST API (5 HTTP methods)
│   ├── layout.tsx          # Root layout (fonts, metadata, providers)
│   ├── loading.tsx         # Root loading skeleton
│   ├── not-found.tsx       # 404 page
│   └── global-error.tsx    # Global error boundary
├── actions/                # Server Actions ("use server") — primary mutation pattern
│   ├── types.ts            # ActionResult<T> discriminated union
│   ├── comic.actions.ts    # Comic CRUD + bookmark actions
│   ├── auth-db.ts          # getUserByUsername, verifyPassword (bcryptjs)
│   ├── bookmark.actions.ts
│   ├── comment.actions.ts
│   ├── rating.actions.ts
│   ├── reading-progress.ts
│   └── ...
├── dal/                    # Data Access Layer — all DB reads go here
│   ├── base-dal.ts         # Abstract BaseDal<T> with handleError()
│   ├── comic-dal.ts        # Reference implementation (423 lines)
│   └── ...                 # One DAL per domain entity (18 total)
├── database/
│   ├── schema.ts           # 604 lines, 27 tables, 4 enums (⚠ no explicit relations())
│   └── db.ts               # Drizzle singleton (postgres-js driver)
├── schemas/                # Zod v4 validation schemas — one per domain
│   └── seed/               # Separate Zod schemas for seed data
├── components/
│   ├── ui/                 # shadcn/Radix primitives
│   ├── layout/             # LayoutProvider, AppSidebar
│   └── shadcn-studio/      # Self-contained feature blocks
├── hooks/
│   ├── use-now.tsx         # SSR-safe Date (null during SSR, value after mount)
│   └── use-pagination.ts
├── lib/
│   ├── env.ts              # Zod-validated env — use getEnv().X, not process.env.X
│   └── query-client.ts     # React Query keys factory + singleton
├── stores/                 # Zustand client stores (create dir if missing)
├── styles/                 # Global CSS
├── tests/                  # Unit test files + setup-env.ts
├── types/                  # Shared TypeScript types
├── scripts/seed/           # Database seeding system (CLI + REST API)
│   ├── run.ts              # CLI entry (Commander.js via tsx)
│   ├── seedOrchestrator.ts # Dependency-aware orchestration
│   ├── seeders/            # BaseSeeder + entity seeders
│   ├── images/             # Image strategy dispatch (urls/local/imagekit)
│   ├── helpers/            # dateParser, creatorNameResolver, etc.
│   └── database/           # Batch processing, transactions
├── auth.ts                 # NextAuth init: exports { handlers, auth, signIn, signOut }
├── auth-config.ts          # Session strategy, callbacks, adapter binding
├── auth-providers.ts       # GitHub OAuth, Credentials, Keycloak
├── auth-adapter.ts         # DrizzleAdapter wiring to schema tables
└── proxy.ts                # Middleware: protects /dashboard only (⚠ /admin unguarded)
```

### Data Flow (Application)

```
Server Component → DAL (Drizzle query with .with()) → props → Client Component → Zustand / React Query
```

### Data Flow (Seeding)

```
CLI/API → SeedOrchestrator → Seeder.seed() → Zod validate → Batch Processor → Database (transaction) → Report
```

### Why This Structure?

| Decision | Rationale |
| --- | --- |
| **DAL layer** | Type-safe queries, N+1 prevention via `.with()`, error normalization |
| **Server Actions for mutations** | No API routes for app mutations — colocated, progressive enhancement |
| **Modular auth** | 4 files (`auth.ts`, `auth-config.ts`, `auth-providers.ts`, `auth-adapter.ts`) for independent testability and provider swapping |
| **Drizzle ORM** | Type-safe SQL, lightweight, Neon-compatible, excellent migration tooling |
| **Separate seed schemas** | Seed data shapes differ from app schemas (e.g., external IDs, author name strings vs FK IDs) |

---
