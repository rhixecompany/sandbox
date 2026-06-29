# Banking - Folder Structure Blueprint

**Project Type:** Next.js 16 (Fintech Banking Application)  
**Detection:** Auto-detected via `package.json`, `next.config.ts`, `drizzle.config.ts`, `bun.lock`  
**Generated:** 2026-06-29  

---

## 1. Structural Overview

This is a Next.js 16 fintech banking application using the App Router architecture with PostgreSQL database via Drizzle ORM, and integrations with Plaid (bank connections) and Dwolla (ACH transfers). The project follows a **feature-organized, layer-separated** structure with clear boundaries between presentation, business logic, and data access layers.

### Organizational Principles
- **By Feature/Domain**: Related functionality grouped together (actions, components, DAL per domain)
- **Layer Separation**: Server Actions → DAL → Database (clean dependency flow)
- **Server-First**: Server Components by default, Client Components only when needed
- **Type Safety**: End-to-end TypeScript with Zod validation at boundaries

### Key Architectural Patterns
- **Server Actions Pattern**: All mutations via Next.js Server Actions (`src/actions/`)
- **Data Access Layer (DAL)**: Constructor-based classes for type-safe queries (`src/dal/`)
- **Database Schema**: Centralized in `src/database/schema.ts` with Drizzle ORM
- **State Management**: Zustand for client-side state (`src/stores/`)

---

## 2. Directory Visualization (ASCII Tree - Depth 3)

```
Banking/
├── .all-contributorsrc
├── .claude/
│   └── skills/
├── .github/
│   ├── copilot/
│   └── workflows/
├── AGENTS.md
├── bun.lock
├── components.json
├── drizzle.config.ts
├── next-auth.d.ts
├── next.config.ts
├── package.json
├── postcss.config.mjs
├── README.md
├── src/
│   ├── actions/                    # Server Actions (mutations)
│   │   ├── auth.actions.ts
│   │   ├── plaid.actions.ts
│   │   ├── dwolla.actions.ts
│   │   ├── transaction.actions.ts
│   │   └── user.actions.ts
│   ├── app/                        # Next.js App Router
│   │   ├── (auth)/                 # Route group: auth pages
│   │   │   ├── signin/
│   │   │   └── signup/
│   │   ├── (root)/                 # Route group: main app
│   │   │   ├── dashboard/
│   │   │   ├── wallets/
│   │   │   └── transactions/
│   │   ├── (admin)/                # Route group: admin panel
│   │   └── api/                    # API routes
│   │       ├── auth/
│   │       ├── plaid/
│   │       └── dwolla/
│   ├── components/                 # React Components
│   │   ├── ui/                     # shadcn/ui base components
│   │   ├── forms/
│   │   ├── layout/
│   │   └── features/
│   ├── dal/                        # Data Access Layer
│   │   ├── user.dal.ts
│   │   ├── bank.dal.ts
│   │   ├── transaction.dal.ts
│   │   └── recipient.dal.ts
│   ├── database/                   # Database Layer
│   │   ├── db.ts                   # Drizzle instance
│   │   └── schema.ts               # All table definitions
│   ├── lib/                        # Utilities & Integrations
│   │   ├── auth.ts                 # NextAuth config
│   │   ├── plaid.ts                # Plaid client
│   │   ├── dwolla.ts               # Dwolla client
│   │   ├── utils.ts                # General utilities
│   │   └── env.ts                  # Env validation
│   ├── stores/                     # Zustand stores
│   │   └── useStore.ts
│   └── types/                      # TypeScript types
│       ├── plaid.ts
│       ├── dwolla.ts
│       └── index.ts
└── tsconfig.json
```

---

## 3. Key Directory Analysis

### `src/actions/` - Server Actions (Mutation Layer)
**Purpose**: All write operations and business logic mutations  
**Pattern**: `dot.camelCase` naming (e.g., `auth.signin.ts`, `plaid.actions.ts`)  
**Conventions**:
- Each action file exports async functions with `"use server"` directive
- Input validation via Zod schemas at entry point
- Return `{ ok: true, data } | { ok: false, error }` pattern
- No direct database access - delegate to DAL

### `src/app/` - Next.js App Router (Presentation Layer)
**Purpose**: Route definitions, layouts, and page components  
**Route Groups**:
- `(auth)`: Public auth pages (signin, signup) - no sidebar/layout
- `(root)`: Main authenticated app - shared dashboard layout
- `(admin)`: Admin panel - separate layout with admin sidebar
- `api/`: REST endpoints for webhooks (Plaid, Dwolla callbacks)

**Conventions**:
- Server Components by default
- Client Components only for interactivity (`"use client"`)
- Colocate page-specific components in same route segment
- Loading/error/not-found pages per segment

### `src/components/` - React Components (UI Layer)
**Purpose**: Reusable UI components  
**Organization**:
- `ui/`: shadcn/ui primitive components (button, card, dialog, etc.)
- `forms/`: Form-specific components with React Hook Form + Zod
- `layout/`: Layout components (Header, Sidebar, Footer)
- `features/`: Feature-specific composite components

**Naming**: PascalCase for components (`BankInfo.tsx`, `Pagination.tsx`)

### `src/dal/` - Data Access Layer (Query Layer)
**Purpose**: Type-safe database queries, read operations  
**Pattern**: Constructor-based classes with singleton exports  
**Example**:
```typescript
// dal/user.dal.ts
export class UserDAL {
  async findByEmail(email: string) { ... }
  async findById(id: number) { ... }
}
export const userDal = new UserDAL();
```
**Conventions**:
- One DAL class per domain entity
- Methods return typed query builders or executed results
- No business logic - pure data access

### `src/database/` - Database Schema & Connection
**Purpose**: Drizzle ORM configuration and schema definitions  
**Files**:
- `db.ts`: Drizzle instance with PostgreSQL connection
- `schema.ts`: All table definitions (users, banks, transactions, recipients, user_profiles)

**Conventions**:
- Tables: `snake_case` (`users`, `user_profiles`, `transactions`)
- Columns: `snake_case` with descriptive names
- Relations defined via Drizzle relations API
- Soft deletes via `deletedAt` timestamp

### `src/lib/` - Utilities & External Integrations
**Purpose**: Shared utilities, external service clients, configuration  
**Key Files**:
- `auth.ts`: NextAuth v5 configuration
- `plaid.ts`: Plaid SDK client initialization
- `dwolla.ts`: Dwolla SDK client initialization
- `utils.ts`: General helpers (cn, formatCurrency, etc.)
- `env.ts`: Runtime environment validation (Zod)

### `src/stores/` - Client State (Zustand)
**Purpose**: Global client-side state management  
**Pattern**: Single store or feature-scoped stores with TypeScript types

### `src/types/` - TypeScript Definitions
**Purpose**: Shared type definitions for external APIs and internal contracts  
**Files**: `plaid.ts`, `dwolla.ts`, `index.ts` (re-exports)

---

## 4. File Placement Patterns

| File Type | Location | Convention |
|-----------|----------|------------|
| Server Actions | `src/actions/` | `feature.action.ts` (dot.camelCase) |
| DAL Classes | `src/dal/` | `entity.dal.ts` |
| Database Schema | `src/database/schema.ts` | Centralized, single file |
| React Components | `src/components/` | PascalCase, feature-grouped |
| Pages/Layouts | `src/app/(group)/` | Route segment = folder |
| API Routes | `src/app/api/` | RESTful, webhook endpoints |
| Utilities | `src/lib/` | camelCase, single responsibility |
| Types | `src/types/` | Domain-separated files |
| Client State | `src/stores/` | Feature-scoped stores |
| Config Files | Root | TypeScript config (tsconfig.json) |

### Environment-Specific Configuration
- `.env.local` - Local development (gitignored)
- `.env.example` - Template with required variables
- No environment-specific config folders - all via `lib/env.ts`

---

## 5. Naming and Organization Conventions

### File Naming
| Type | Convention | Example |
|------|------------|---------|
| Server Actions | dot.camelCase | `plaid.actions.ts`, `auth.signin.ts` |
| DAL Files | dot.camelCase | `user.dal.ts`, `transaction.dal.ts` |
| Components | PascalCase | `BankInfo.tsx`, `TransactionCard.tsx` |
| Hooks/Utils | camelCase | `useMediaQuery.ts`, `formatCurrency.ts` |
| Types | PascalCase + .ts | `PlaidTypes.ts`, `DwollaTypes.ts` |
| Database Tables | snake_case | `users`, `user_profiles` |
| Columns | snake_case | `first_name`, `access_token` |

### Folder Naming
- Route groups: `(parentheses)` for layout grouping
- Feature folders: kebab-case (`wallets`, `transactions`)
- Component categories: lowercase (`ui`, `forms`, `layout`)
- No abbreviations in folder names

### Namespace/Module Patterns
- `@/` path alias maps to `src/`
- Imports: `@/actions/...`, `@/components/...`, `@/lib/...`
- DAL imports: `import { userDal } from '@/dal/user.dal'`
- Database: `import { db } from '@/database/db'`

---

## 6. Navigation and Development Workflow

### Entry Points
1. **App Entry**: `src/app/layout.tsx` - Root layout, providers
2. **Auth Entry**: `src/app/(auth)/signin/page.tsx` - Sign in page
3. **Dashboard Entry**: `src/app/(root)/dashboard/page.tsx` - Main dashboard
4. **API Webhooks**: `src/app/api/plaid/webhook/route.ts`, `src/app/api/dwolla/webhook/route.ts`

### Common Development Tasks

| Task | Location | Steps |
|------|----------|-------|
| Add Server Action | `src/actions/` | 1. Create `feature.action.ts` 2. Add Zod schema 3. Implement with DAL 4. Export |
| Add Database Table | `src/database/schema.ts` | 1. Define table 2. Run `bun run db:generate` 3. Run `bun run db:migrate` 4. Create DAL |
| Add Component | `src/components/` | 1. Create in appropriate subfolder 2. Use shadcn/ui primitives 3. Export from index |
| Add Page | `src/app/(group)/` | 1. Create route folder 2. Add `page.tsx` 3. Add `loading.tsx` if needed |

### Dependency Flow
```
Server Actions → DAL → Database (Drizzle)
       ↓
   Components (read via Server Components or DAL)
       ↓
   Client Components (via props or Zustand)
```

### Adding New Features
1. **Domain-first**: Create DAL class in `src/dal/`
2. **Actions**: Add Server Actions in `src/actions/`
3. **UI**: Build components in `src/components/features/`
4. **Routes**: Add pages in `src/app/(root)/feature/`
5. **Types**: Define in `src/types/` if external API involved

---

## 7. Build and Output Organization

### Build Configuration
- **Package Manager**: Bun (`bun.lock`, `bun run` commands)
- **Build Command**: `bun run build` (Next.js production build)
- **Dev Command**: `bun run dev` (Turbopack)
- **Type Check**: `bun run type-check` (`tsc --noEmit`)
- **Lint**: `bun run lint:strict` (ESLint with strict rules)
- **Format**: `bun run format` (Prettier)

### Database Commands
- `bun run db:push` - Push schema directly (dev)
- `bun run db:generate` - Generate migration files
- `bun run db:migrate` - Apply migrations
- `bun run db:studio` - Open Drizzle Studio

### Output Structure
- `.next/` - Next.js build output (gitignored)
- `node_modules/` - Dependencies (gitignored)
- No separate `dist/` - Next.js handles output

### Environment Builds
- **Development**: Turbopack, hot reload, `.env.local`
- **Production**: Optimized build, `.env.production` (Vercel env vars)

---

## 8. Technology-Specific Organization

### Next.js 16 Specific Patterns
- **App Router**: File-system based routing with route groups
- **Server Components**: Default, no `"use client"` needed
- **Server Actions**: `"use server"` directive for mutations
- **Route Handlers**: `route.ts` files for API endpoints
- **Middleware**: `middleware.ts` at root for auth/rate limiting

### Drizzle ORM Patterns
- Schema in single `schema.ts` file
- Relations via `relations()` helper
- Type-safe queries via DAL classes
- Migrations in `migrations/` folder (generated)

### shadcn/ui Integration
- Components in `src/components/ui/`
- Configured via `components.json`
- Tailwind CSS 4 with CSS variables
- Class variance authority (CVA) for variants

### External Integrations
- **Plaid**: `lib/plaid.ts` client, actions in `actions/plaid.actions.ts`
- **Dwolla**: `lib/dwolla.ts` client, actions in `actions/dwolla.actions.ts`
- **NextAuth**: `lib/auth.ts` config, API route at `app/api/auth/[...nextauth]/`

---

## 9. Extension and Evolution

### Extension Points
1. **New Domain**: Add DAL → Actions → Components → Routes
2. **New Integration**: Add client in `lib/`, actions in `actions/`, types in `types/`
3. **New UI Pattern**: Add to `components/ui/` or create feature components

### Scalability Patterns
- **Feature Folders**: Group related actions, components, types together
- **DAL per Entity**: Single responsibility, easy to split
- **Route Groups**: Isolate layouts without URL impact
- **Zustand Stores**: Feature-scoped, avoid global state bloat

### Refactoring Patterns
- **Extract DAL**: Move queries from actions to DAL
- **Colocate**: Move feature-specific components near routes
- **Type Sharing**: Central types in `src/types/`, feature types near features

---

## 10. Structure Templates

### New Feature Template
```
src/
├── actions/
│   └── feature.actions.ts        # Server Actions
├── dal/
│   └── feature.dal.ts            # Data Access Layer
├── components/
│   └── features/
│       └── feature/              # Feature components
│           ├── FeatureList.tsx
│           ├── FeatureCard.tsx
│           └── FeatureForm.tsx
├── app/
│   └── (root)/
│       └── feature/              # Routes
│           ├── page.tsx
│           ├── loading.tsx
│           └── [id]/
│               └── page.tsx
└── types/
    └── feature.ts                # Types (if needed)
```

### New Server Action Template
```typescript
// src/actions/feature.action.ts
"use server";

import { z } from "zod";
import { featureDal } from "@/dal/feature.dal";

const FeatureSchema = z.object({
  name: z.string().min(1),
  // ... fields
});

export async function createFeatureAction(input: unknown) {
  const parsed = FeatureSchema.safeParse(input);
  if (!parsed.success) {
    return { error: parsed.error.errors[0]?.message, ok: false };
  }
  try {
    const result = await featureDal.create(parsed.data);
    return { ok: true, data: result };
  } catch {
    return { error: "Operation failed", ok: false };
  }
}
```

### New DAL Template
```typescript
// src/dal/feature.dal.ts
import { db } from "@/database/db";
import { featureTable } from "@/database/schema";
import { eq } from "drizzle-orm";

export class FeatureDAL {
  async findById(id: number) {
    return db.select().from(featureTable).where(eq(featureTable.id, id)).limit(1);
  }
  
  async findAll() {
    return db.select().from(featureTable);
  }
  
  async create(data: typeof featureTable.$inferInsert) {
    return db.insert(featureTable).values(data).returning();
  }
}

export const featureDal = new FeatureDAL();
```

---

## 11. Structure Enforcement

### Validation Tools
- **TypeScript**: Strict mode, catches structural issues
- **ESLint**: `lint:strict` with Next.js, React, TypeScript rules
- **Prettier**: Consistent formatting via `format` command
- **Zod**: Runtime validation at action boundaries

### Documentation Practices
- **AGENTS.md**: Canonical source for conventions and patterns
- **README.md**: Setup and common commands
- **Inline Comments**: Complex business logic only
- **Schema Comments**: Table/column purposes in `schema.ts`

### Structure Evolution
- **Migrations**: Drizzle migrations track schema changes
- **Git History**: Commit messages reference structural changes
- **AGENTS.md Updates**: Updated when conventions change

---

**Last Updated**: 2026-06-29  
**Generated By**: folder-structure-blueprint-generator  
**Project Root**: `C:\Users\Alexa\Desktop\SandBox\projects\Banking`