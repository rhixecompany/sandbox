# Project Structure

> Extracted from `comicwise-development.prompt.md`.

## Project Structure

```
src/
├── app/                     # Next.js App Router pages
│   ├── (auth)/             # Public auth pages (/sign-in, /sign-up)
│   ├── (root)/             # Main app pages
│   ├── admin/              # Admin-only routes (middleware-protected)
│   └── api/                # API routes (auth/, health-checks)
│
├── dal/                    # Data Access Layer (Drizzle queries)
│   ├── base-dal.ts         # Abstract BaseDal<T> base class
│   ├── comic-dal.ts        # Comic queries with .with() eager loading
│   ├── chapter-dal.ts      # Chapter queries
│   ├── bookmark-dal.ts     # Bookmark queries
│   └── ...                 # One DAL per entity
│
├── actions/                # Server Actions (mutations)
│   ├── types.ts            # ActionResult<T> discriminated union
│   ├── comic.actions.ts    # Comic mutations
│   ├── bookmark.actions.ts # Bookmark mutations
│   └── ...                 # One file per domain
│
├── schemas/                # Zod validation schemas
│   ├── comic.schema.ts     # Comic validation (create, update, filter)
│   ├── bookmark.schema.ts  # Bookmark validation
│   └── ...                 # One schema per domain
│
├── components/             # React components (120+)
│   ├── ui/                 # shadcn/Radix primitives
│   ├── comics/             # Comic-specific components
│   ├── bookmarks/          # Bookmark components
│   ├── reading/            # Reader components
│   ├── analytics/          # Analytics dashboard
│   └── layout/             # Layout components (Sidebar, Header)
│
├── database/
│   ├── db.ts               # Drizzle singleton (postgres-js driver)
│   └── schema.ts           # 27 table definitions, 4 enums, relations
│
├── hooks/                  # Custom React hooks
│   ├── use-now.tsx         # SSR-safe useCurrentYear()
│   ├── use-debounce.ts     # Debounced values
│   ├── use-mobile.ts       # Mobile detection
│   └── ...
│
├── stores/                 # Zustand client state
│   ├── use-bookmark-store.ts
│   ├── use-reader-store.ts
│   └── ...
│
├── lib/
│   ├── env.ts              # Zod-validated getEnv() singleton
│   ├── utils.ts            # cn() tailwind class merger
│   ├── query-client.ts     # React Query config
│   └── ...
│
├── scripts/                # CLI scripts
│   └── seed/               # Seeding system with dependency orchestration
│
├── tests/                  # Test setup
│   └── setup-env.ts        # Vitest jsdom mocks + setup
│
├── auth.ts                 # NextAuth init
├── auth-config.ts          # Session strategy, callbacks
├── auth-providers.ts       # OAuth/Credentials/OIDC providers
├── auth-adapter.ts         # Drizzle adapter
└── proxy.ts                # Middleware for route protection

docs/                       # Documentation
├── dev.content.md          # 26 sections with patterns & examples
├── DEVELOPMENT.md          # Developer guide
├── database-context-map.md # Entity relationships
└── MASTER_PHASE_PLAN_4-6.md # Phase planning

.github/
├── copilot-instructions.md # Complete 2500+ line guide
├── instructions/           # Auto-loaded by file pattern:
│   ├── design-system.instructions.md
│   ├── security-and-owasp.instructions.md
│   ├── performance-optimization.instructions.md
│   ├── testing.instructions.md
│   ├── typescript.instructions.md
│   ├── nextjs.instructions.md
│   └── ...                 # 15+ instruction files
└── prompts/
    ├── comicwise-session.prompt.md       # Quick reference
    └── comicwise-development.prompt.md   # This file
```
