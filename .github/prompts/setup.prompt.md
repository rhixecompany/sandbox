---
description: "Comprehensive AI agent onboarding prompt for ComicWise — architecture, workflows, real code patterns, and conventions"
agent: "Next.js Expert"
model: "Claude Haiku 4.5 (copilot)"
---

# ComicWise — AI Agent Setup & Onboarding

**ComicWise** is a production-grade manga/comic reader built with Next.js 16.1.6 (App Router), React 19.2.4 Server Components, Drizzle ORM 0.45.1 + PostgreSQL (Neon), NextAuth v5 (database sessions), Zustand 5 + React Query 5, shadcn/Radix UI, Tailwind CSS 4, Vitest + Playwright, and a complete database seeding system with CLI + REST API.

---

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

## 2. Essential Commands

```bash
# ── Development ──
pnpm dev                         # Start dev server (Turbopack, port 3000)
pnpm type-check                  # tsc --noEmit — must be 0 errors before PR
pnpm type-check:watch            # tsc --noEmit --watch (continuous checking)
pnpm lint:fix                    # ESLint flat config + Prettier auto-fix
pnpm lint:strict                 # ESLint with --max-warnings=0
pnpm build                       # Production build (prebuild runs clean:cache + type-gen)
pnpm build:debug                 # Build with --debug-prerender
pnpm format                      # Prettier --write .
pnpm format:check                # Prettier --check .
pnpm type-gen                    # next typegen (runs automatically in prebuild/predev)

# ── Database ──
pnpm db:push                     # Apply schema changes (dev only, no migration files)
pnpm db:generate                 # Generate migration SQL files from schema changes
pnpm db:migrate                  # Run migration files (production)
pnpm db:studio                   # Open Drizzle Studio (browser DB viewer)
pnpm db:reset                    # Drop + regenerate + push (dev only!)
pnpm db:check                    # Verify migration consistency
pnpm db:drop                     # Drop migrations
pnpm db:pull                     # Introspect existing DB into schema

# ── Testing ──
pnpm test                        # Vitest unit tests (jsdom env)
pnpm test:ui                     # Playwright E2E tests
pnpm test:ui:codegen             # Playwright test code generator

# ── Seeding (CLI — direct, no server required) ──
pnpm seed --dry-run --verbose    # Validate all seed data without writing
pnpm seed:all                    # Seed all entities (respects dependency order)
pnpm seed:comics --force         # Upsert comics (idempotent)
pnpm seed:chapters --image-strategy=local --batch-size=500
pnpm seed:validate               # Dry-run validation only (alias)

# ── Seeding (REST API — requires dev server running) ──
pnpm seed:clear                  # DELETE via curl — clear all seed data
pnpm seed:reset                  # PUT via curl — delete + reseed all
curl http://localhost:3000/api/seed                        # GET — validate
curl -X POST http://localhost:3000/api/seed \
  -H 'Content-Type: application/json' \
  -d '{"entities":"all"}'                                  # POST — seed
curl -X DELETE http://localhost:3000/api/seed              # DELETE — clear

# ── Setup Automation ──
bash scripts/setup-dev.sh        # Linux/macOS dev environment setup
.\scripts\setup-dev.ps1          # Windows PowerShell dev environment setup
```

### Quality Gate (Required Before PR)

```bash
pnpm type-check          # Must be 0 TypeScript errors
pnpm lint:fix            # ESLint + Prettier auto-fix
pnpm test                # Vitest unit tests pass
pnpm build               # Production build succeeds
```

---

## 3. Environment Variables

Create `.env.local` from `.env.local.example`:

```bash
# ── Required ──
DATABASE_URL="postgresql://user:pass@localhost:5432/comicbook"
AUTH_SECRET="$(openssl rand -hex 32)"     # min 32 chars
NEXT_PUBLIC_API_URL="http://localhost:3000"
NODE_ENV="development"

# ── Required for NextAuth ──
AUTH_URL="http://localhost:3000"           # Base URL for auth callbacks

# ── Optional: Neon serverless ──
NEON_DATABASE_URL="postgresql://..."      # Neon serverless connection string

# ── Optional: Debug ──
DEBUG="false"                             # Enable debug logging

# ── OAuth (optional — GitHub) ──
GITHUB_CLIENT_ID="your_client_id"
GITHUB_CLIENT_SECRET="your_client_secret"

# ── OAuth (optional — Keycloak) ──
KEYCLOAK_CLIENT_ID="comicwise"
KEYCLOAK_CLIENT_SECRET="your_secret"
KEYCLOAK_ISSUER="https://keycloak.example.com/realms/comicwise"

# ── Image CDN (optional — only for imagekit seed strategy) ──
IMAGEKIT_PUBLIC_KEY="..."
IMAGEKIT_PRIVATE_KEY="..."
IMAGEKIT_URL_ENDPOINT="https://ik.imagekit.io/youraccount"
```

### Runtime Validation (`src/lib/env.ts`)

**Only 6 fields are actively validated** via Zod: `DATABASE_URL`, `NEON_DATABASE_URL`, `AUTH_SECRET`, `NEXT_PUBLIC_API_URL`, `NODE_ENV`, `DEBUG`. The remaining ~60 fields (OAuth, ImageKit, Sentry, Redis, email, etc.) are commented out as stubs for future integration.

Access validated env through `getEnv()` — never use raw `process.env` in app code.

**Known exception:** `auth-config.ts`, `auth-providers.ts`, and `db.ts` use raw `process.env` because they load before app initialization. This is a pragmatic trade-off, not a pattern to follow elsewhere.

---

## 4. Database Schema — Critical Facts

Schema defined in `src/database/schema.ts` (604 lines, **27 tables**, 4 enums).

### Enums

```typescript
// Title-Case values for comicStatus
comicStatus: "Ongoing" |
  "Hiatus" |
  "Completed" |
  "Dropped" |
  "Season End" |
  "Coming Soon";

// Lowercase values for userRole
userRole: "user" | "admin" | "moderator";

// RBAC enums (used by permission and auditLog tables)
resourceEnum: "comic" |
  "chapter" |
  "user" |
  "comment" |
  "rating" |
  "bookmark" |
  "notification" |
  "author" |
  "artist" |
  "genre" |
  "type" |
  "system";
actionEnum: "create" | "read" | "update" | "delete" | "manage";
```

### Key Table Facts

| Table | Key Column | Gotcha |
| --- | --- | --- |
| `user` | `id: text` (UUID string) | NOT integer. Password nullable (OAuth users). Has `deletedAt` for soft delete. Has `settings` JSONB column. |
| `comic` | `rating: decimal(10,1)` | Aggregate display rating. NOT integer. `status` must match Title-Case enum. |
| `rating` | `rating: integer` | Per-user 1–5 stars. Different type from `comic.rating`! Use `AVG(rating)` for aggregation. |
| `bookmark` | Composite PK `(userId, comicId)` | Use `onConflictDoUpdate` for upserts |
| `chapter` | Composite unique `(comicId, chapterNumber)` |  |
| All FK cols |  | Must include `{ onDelete: "cascade" }` except `auditLog.userId` → `"set null"` |

### Complete Table List (27 tables)

| Category | Tables |
| --- | --- |
| **Auth/User** | `user`, `account`, `session`, `verificationToken`, `authenticator`, `passwordResetToken` |
| **Content** | `type`, `author`, `artist`, `genre`, `comic`, `chapter`, `comicImage`, `chapterImage`, `comicToGenre` (junction) |
| **User Activity** | `bookmark`, `comment`, `readingProgress`, `readerSettings`, `rating`, `notification`, `userPreference` |
| **RBAC** | `role`, `permission`, `rolePermission`, `userRole2` |
| **Audit** | `auditLog` |

### RBAC Tables

```typescript
role:           { id, name, description, isSystem, createdAt, updatedAt }
permission:     { id, name, resource (resourceEnum), action (actionEnum), createdAt }
rolePermission: { roleId, permissionId }  // Composite PK, cascade deletes both FKs
userRole2:      { userId, roleId, assignedBy (FK → user) }  // Composite PK
```

> **Note:** The JS export is `userRole2` because the enum `userRole` already occupies that name.

### Audit Log Table

```typescript
auditLog: {
  (id,
    userId,
    action,
    resource(resourceEnum),
    resourceId,
    details,
    oldValues,
    newValues,
    ipAddress,
    userAgent,
    sessionId,
    createdAt);
}
// ⚠ EXCEPTION: userId uses onDelete: "set null" (NOT cascade)
// This preserves audit trail when users are deleted
// Has 7 indexes for efficient querying
```

### Supplementary Tables

```typescript
readerSettings:     { userId (1:1 with user), backgroundMode, readingMode, defaultQuality }
passwordResetToken: { email, token (unique), expires }
userPreference:     { userId, ... }
comicImage:         { id, comicId, ... }  // Comic cover/banner images
chapterImage:       { id, chapterId, ... }  // Chapter page images
```

### Soft Delete

`user.deletedAt` exists in schema. **Rule:** Filter `WHERE deletedAt IS NULL` in user queries to exclude soft-deleted users.

### User Settings JSONB

```typescript
user.settings: jsonb("settings").$type<{
  emailNotifications?: boolean;
  profileVisibility?: "private" | "public";
  readingHistoryVisibility?: boolean;
}>()
```

### Search Vector Fields

`comic.searchVector`, `author.searchVector`, `artist.searchVector` — stored as `text` columns (not actual PostgreSQL `tsvector` despite the name). Used for text search indexing.

### Entity Relationships (Simplified)

```
Type ──┐
Author ┼──→ Comic ──→ Chapter ──→ ChapterImage
Artist ┘      │
              ├──→ ComicImage
Genre ←── ComicToGenre (junction)

User ──→ Bookmark, Rating, Comment, ReadingProgress, Notification, ReaderSettings, UserPreference
User ──→ UserRole2 ──→ Role ──→ RolePermission ──→ Permission
User ──→ AuditLog (set null on delete)
```

### Cascade Delete Scenarios

| Scenario | Cascades To | Exception |
| --- | --- | --- |
| **Delete User** | bookmark, rating, comment, readingProgress, notification, readerSettings, userPreference, userRole2 | `auditLog.userId` → SET NULL (not cascade) |
| **Delete Comic** | chapter, bookmark, rating, comment, comicToGenre, comicImage, readingProgress | — |
| **Delete Chapter** | chapterImage, readingProgress (for that chapter) | `bookmark.lastReadChapterId` → SET NULL |

---

## 5. Authentication System

### Architecture (4 modular files)

```
src/auth.ts             → NextAuth({ ...authConfig })  → exports { handlers, auth, signIn, signOut }
src/auth-config.ts      → session strategy, callbacks (session, jwt, signIn, redirect)
src/auth-providers.ts   → [GitHub, Credentials, Keycloak] provider array
src/auth-adapter.ts     → DrizzleAdapter(db, { usersTable, accountsTable, ... })
```

> **Note:** Auth files (`auth-config.ts`, `auth-providers.ts`, `db.ts`) use raw `process.env` as a known exception — they load before app initialization. Do not follow this pattern elsewhere.

### Session Strategy

- **Database sessions** (not JWT) — `strategy: "database"`, `maxAge: 30 days`, `updateAge: 1 day`
- Session stored in `session` table, linked to `user` via `userId`

### Credentials Provider (`src/auth-providers.ts`)

```typescript
async authorize(
  credentials: Partial<Record<"username" | "password", unknown>>
): Promise<User | null> {
  const username = typeof credentials.username === "string" ? credentials.username : undefined;
  const password = typeof credentials.password === "string" ? credentials.password : undefined;
  if (!username || !password) return null;

  const user = await getUserByUsername(username);      // src/actions/auth-db.ts
  if (user?.passwordHash && (await verifyPassword(password, user.passwordHash))) return user;
  return null;
}
```

### DB Lookup & Password Verification (`src/actions/auth-db.ts`)

```typescript
import bcrypt from "bcryptjs";
import { eq } from "drizzle-orm";
import { db } from "../database/db";
import { user as userTable } from "../database/schema";

export async function getUserByUsername(
  username: string
): Promise<User | null> {
  const result = await db
    .select()
    .from(userTable)
    .where(eq(userTable.name, username));
  if (!result[0]) return null;
  return {
    id: result[0].id,
    name: result[0].name ?? undefined,
    email: result[0].email,
    role: result[0].role,
    passwordHash: result[0].password ?? undefined
  };
}

export async function verifyPassword(
  plain: string,
  hash: string
): Promise<boolean> {
  return bcrypt.compare(plain, hash);
}
```

### Server-Side Usage

```typescript
// Server Component or Server Action
import { auth } from "@/auth";
const session = await auth();
if (!session?.user) redirect("/auth/signin");

// Check admin role
const u = session.user as { role?: unknown };
const isAdmin = typeof u?.role === "string" && u.role === "admin";
```

### Client-Side Usage

```typescript
// Client Component — read session
import { useSession } from "next-auth/react";
const { data: session } = useSession();

// Client Component — OAuth sign-in
import { signIn } from "next-auth/react";
await signIn("github", { redirectTo: "/dashboard" });

// Client Component — Credentials sign-in (no redirect, handle in-page)
const result = await signIn("credentials", {
  username: "user",
  password: "pass",
  redirect: false
});
if (result?.error) showError(result.error);
```

### Auth API Route (`src/app/api/auth/[...nextauth]/route.ts`)

```typescript
export { GET, POST } from "@/auth";
```

### Known Bugs

- `auth-config.ts` `signIn` callback: currently blocks users without email — may need adjustment for OAuth-only providers
- `redirect` callback: falls back to `/dashboard` for external URLs — should respect original intent

---

## 6. Data Access Layer (DAL)

### Base Class (`src/dal/base-dal.ts`)

```typescript
export interface DalOptions {
  limit?: number;
  offset?: number;
}

export abstract class BaseDal<T> {
  abstract list(options?: DalOptions): Promise<T[]>;
  abstract getById(id: string | number): Promise<T | null>;
  abstract create(data: unknown): Promise<T>;
  abstract update(
    id: string | number,
    data: unknown
  ): Promise<T | null>;
  abstract delete?(id: string | number): Promise<void>;

  protected handleError(error: unknown, operation: string): never {
    console.error(
      `[${this.constructor.name}] ${operation} failed:`,
      error
    );
    if (error instanceof Error) {
      if (error.message.includes("UNIQUE"))
        throw new Error("This record already exists");
      if (error.message.includes("FOREIGN KEY"))
        throw new Error("Related record not found");
      if (error.message.includes("NOT NULL"))
        throw new Error("Required field is missing");
    }
    throw new Error(`Failed to ${operation.toLowerCase()}`);
  }
}
```

### Implementation Pattern (`src/dal/comic-dal.ts`)

```typescript
import { db } from "@/database/db";
import { comic } from "@/database/schema";
import { BaseDal, type DalOptions } from "./base-dal";

type ComicType = typeof comic.$inferSelect; // IMPORTANT: use $inferSelect, not raw typeof

export class ComicDal extends BaseDal<ComicType> {
  async list(options?: ComicListOptions) {
    // Uses .with() for eager loading — NEVER loop + query (N+1)
    return db.query.comic.findMany({
      limit: options?.limit ?? 20,
      offset: options?.offset ?? 0,
      with: {
        author: true,
        artist: true,
        type: true,
        comicToGenre: { with: { genre: true } }
      }
    });
  }
  async getById(id: string) {
    /* ... */
  }
  async create(data: CreateComicInput) {
    /* ... */
  }
  async update(id: string, data: UpdateComicInput) {
    /* ... */
  }
}

export const comicDal = new ComicDal(); // Singleton export — REQUIRED
```

### DAL Query Patterns

| Pattern | When | Example |
| --- | --- | --- |
| `db.query.*.findMany/findFirst` with `.with()` | Primary pattern — eager loading of relations | `comic-dal`, `bookmark-dal`, `chapter-dal` |
| `db.select().from(table)` | Simple lookups without relations | `user-dal`, `type-dal`, `notification-dal`, `comic-image-dal` |

### ⚠ CRITICAL: No Explicit `relations()` in Schema

**There are zero `relations()` definitions in `schema.ts`.** DALs rely entirely on Drizzle's FK inference from `.references()` column declarations. This means:

- **Simple FK relations** (`comic.authorId → author.id`) auto-infer → `.with({ author: true })` works.
- **Junction tables** (`comicToGenre`) are inferred from FKs → `.with({ genres: { with: { genre: true } } })` works.
- **`comment.parentId` has NO `.references()` call** → parent/replies relation **cannot** be used with `db.query`. This is a known gap.
- **Self-referential, multi-FK-to-same-table, and custom-named relations** require explicit `relations()` to be added to schema.ts.

Current DALs work because they only use simple FK-inferred relations. **If you need advanced relations, you must add `relations()` definitions to schema.ts first.**

### N+1 Anti-Pattern Catalog

| Trap | ❌ Wrong | ✅ Right |
| --- | --- | --- |
| Comics + Authors | `for (comic of comics) { await getAuthor(comic.authorId) }` | `.with({ author: true })` |
| Bookmarks + Comics + Genres | Loop through bookmarks, fetch each comic | `db.query.bookmark.findMany({ with: { comic: { with: { genres: true } } } })` |
| Comment Threading | `comment.parentId` has no FK ref — can't use `.with()` | Manual SQL JOIN or add `relations()` to schema |
| Reading Progress Dashboard | Separate queries for each stat | `count()`, `sum()`, `avg()` in single aggregate query |

### Pagination Response Shape

```typescript
interface PaginatedResponse<T> {
  success: boolean;
  data: T[];
  meta: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
    hasNextPage: boolean;
    hasPrevPage: boolean;
  };
}
```

### DAL Rules

- **Every DAL** extends `BaseDal<typeof table.$inferSelect>` — NOT raw `typeof table`
- **Use `.with()`** for all related data — never `for` loop + individual queries
- **Singleton exports** at file bottom — required for import consumers
- **DAL is for app code only** — seeders bypass DAL for batch performance (see §8)

---

## 7. Server Actions — Primary Mutation Pattern

### ActionResult Type (`src/actions/types.ts`)

```typescript
export type ActionResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string };
```

### Standard Pattern (`src/actions/comic.actions.ts`)

```typescript
"use server";

import { auth } from "@/auth";
import { revalidatePath } from "next/cache";
import { CreateComicSchema } from "@/schemas/comic.schema";
import { comicDal } from "@/dal/comic-dal";
import type { ActionResult } from "./types";

export async function createComicAction(
  input: unknown
): Promise<ActionResult<ComicType>> {
  // 1. Auth check
  const session = await auth();
  if (!session?.user?.id)
    return { ok: false, error: "Not authenticated" };

  // 2. Zod validation
  const parsed = CreateComicSchema.safeParse(input);
  if (!parsed.success)
    return {
      ok: false,
      error: parsed.error.errors[0]?.message ?? "Invalid"
    };

  // 3. DAL operation
  try {
    const comic = await comicDal.create(parsed.data);
    revalidatePath("/comics");
    return { ok: true, data: comic };
  } catch (e) {
    return { ok: false, error: "Failed to create comic" };
  }
}
```

### Rules

- **All app mutations** go through Server Actions — NOT API routes
- **Always validate** with Zod before passing to DAL
- **Always check auth** as first step
- **Return `ActionResult<T>`** — never throw from actions
- **Call `revalidatePath()`** after mutations to bust Next.js cache

---

## 8. Seeding System (CLI + REST API)

### When to Use What

| Context | Pattern | Why |
| --- | --- | --- |
| **App code** (UI mutations) | Server Action → DAL | Type-safe, auth, validation, cache invalidation |
| **Seeding** (bulk insert) | Seeder → direct Drizzle | Batch performance (50k items in ~8 min vs hours via DAL) |

### Seeder Template (`BaseSeed<T>`)

All seeders extend `BaseSeed<T>` and override 4 methods:

```typescript
import { BaseSeed } from "./baseSeed";
import { db } from "@/database/db";
import { myEntity } from "@/database/schema";

export class MyEntitySeeder extends BaseSeed<MyEntity> {
  entityName = "MyEntity"; // Display name
  entityDataKey = "myEntities"; // Root key in JSON file
  dependencies = []; // Seeders that must run first
  dataSourceName = "my-entity"; // Filename: src/data/my-entity.json

  protected getDataSources() {
    return [this.dataSourceName];
  }

  protected transformData(items: unknown[]): MyEntity[] {
    return items.map(item => {
      /* normalize raw JSON → typed entity */
    });
  }

  protected async insertBatch(data: MyEntity[]): Promise<void> {
    await db
      .insert(myEntity)
      .values(data)
      .onConflictDoUpdate({
        target: myEntity.id,
        set: { updatedAt: new Date() }
      });
  }
}

export const myEntitySeeder = new MyEntitySeeder(); // Singleton
```

### Dependency Graph

```
types ──┐
        ├─→ authors ──┐
        │             ├─→ comics ──→ chapters
genres ─┤             │
        ├─→ artists ──┘
users (independent)
```

### CLI Flags (Full Reference)

```bash
--dry-run                             # Validate without writing to database
--verbose                             # Detailed output logging
--image-strategy=urls|local|imagekit  # Image handling strategy
--batch-size=N                        # Records per batch (default varies per entity)
--concurrency=N                       # Parallel batch limit (default: 3)
--skip-validation                     # Skip Zod validation (⚠ dangerous)
--no-transaction                      # Disable per-batch transactions
--force                               # Upsert mode (onConflictDoUpdate)
```

### Image Strategies (swap at runtime)

```bash
--image-strategy=urls      # Default: use original URLs as-is
--image-strategy=local     # Download to ./public/comics/{type}/{id}.{ext}
--image-strategy=imagekit  # Upload to ImageKit CDN
```

### REST API (`src/app/api/seed/route.ts`)

| Method   | Purpose                      | Auth Required (prod) |
| -------- | ---------------------------- | -------------------- |
| `GET`    | Validate (dry-run)           | No                   |
| `POST`   | Full seed (clear + populate) | Yes (admin)          |
| `PATCH`  | Upsert only                  | Yes (admin)          |
| `PUT`    | Reset (delete + reseed)      | Yes (admin)          |
| `DELETE` | Clear all seed data          | Yes (admin)          |

### REST API Request Body Schema

```json
{
  "entities": "all | comics | chapters | authors | artists | genres | types",
  "options": {
    "batchSize": 100,
    "concurrency": 3,
    "verbose": false,
    "dryRun": false,
    "skipValidation": false,
    "useTransaction": true,
    "forceOverwrite": false,
    "imageStrategy": "urls"
  }
}
```

> **Note:** In production, seed API endpoints require admin role authentication (401 without it). `pnpm seed:clear` and `pnpm seed:reset` use `curl` under the hood and require the dev server to be running.

---

## 9. Next.js Configuration (`next.config.ts`)

Key settings active in this project:

```typescript
{
  reactCompiler: true,          // React Compiler is ON — do NOT use useMemo/useCallback/memo
  typedEnv: true,               // Typed process.env
  typedRoutes: true,            // Typed Link href
  cacheComponents: true,        // "use cache" directive enabled
  staleTimes: { dynamic: 30, static: 180 },
  serverExternalPackages: ["postgres", "bcryptjs", "sharp", "nodemailer"],
  serverActions: { bodySizeLimit: "10mb" },
  images: {
    formats: ["image/avif", "image/webp"],
    minimumCacheTTL: 31536000,  // 1 year
    remotePatterns: [/* mangadex, imgur, imagekit, etc. */],
  },
  // Security headers: HSTS, X-Frame-Options DENY, X-Content-Type-Options, Referrer-Policy
}
```

---

## 10. Provider Stack & Root Layout

### Root Layout (`src/app/layout.tsx`)

- 7 custom fonts loaded via `next/font/local` (IBM Plex Sans, Bebas Neue, Schibsted Grotesk, Martian Mono, Fira Sans, Fira Mono)
- Metadata: title "ComicWise", Open Graph, viewport with light/dark theme colors
- Body → `<Suspense>` → `<LayoutProvider>`

### Provider Order (`src/components/layout/layout-provider.tsx`)

```
SessionProvider → QueryClientProvider → ThemeProvider → TooltipProvider → children + lazy Toaster
```

- `ReactQueryDevtools` rendered only in development
- `Toaster` lazy-loaded
- `ThemeProvider` receives theme config props

---

## 11. React Query Keys (`src/lib/query-client.ts`)

```typescript
export const queryKeys = {
  comics: {
    all: ["comics"],
    list: (filters: Record<string, unknown>) => [
      "comics",
      "list",
      filters
    ],
    detail: (slug: string) => ["comics", "detail", slug],
    chapters: (comicId: string) => ["comics", comicId, "chapters"]
  },
  bookmarks: {
    all: ["bookmarks"],
    list: (userId: string) => ["bookmarks", "list", userId],
    check: (userId: string, comicId: string) => [
      "bookmarks",
      "check",
      userId,
      comicId
    ]
  },
  readingProgress: {
    /* ... */
  },
  users: {
    /* ... */
  },
  search: {
    /* ... */
  },
  genres: { all: ["genres"] },
  authors: { all: ["authors"] }
};
```

- **Server**: new `QueryClient` per request
- **Browser**: singleton with `staleTime: 60s`, `gcTime: 5min`, retry 3 exponential backoff

---

## 12. Middleware (`src/proxy.ts`)

```typescript
export function proxy(request: NextRequest) {
  const token = request.cookies.get("auth-token");
  if (request.nextUrl.pathname.startsWith("/dashboard")) {
    if (!token)
      return NextResponse.redirect(new URL("/login", request.url));
  }
  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard/:path*", "/admin/:path*"]
};
```

> **⚠ Incomplete middleware:** Only `/dashboard` is actually protected. Despite `/admin/:path*` being in the matcher, the function has no `admin` check — it falls through to `NextResponse.next()`. Additionally, it checks for a cookie named `"auth-token"`, not a NextAuth session — this may not integrate with the actual auth system. See §21 (Technical Debt).

---

## 13. TypeScript & Tooling Conventions

### tsconfig.json

- `strict: true`, `target: ES2022`, `module: esnext`, `jsx: "react-jsx"`
- Path aliases: `@/*` → `./src/*`, plus shortcuts: `@database`, `@env`, `@hooks`, `@lib`, `@schemas`, `@ui`, etc.
- Next.js plugin enabled, incremental builds

### ESLint (Flat Config — `eslint.config.mts`)

- Extends `next/core-web-vitals` + `next/typescript`
- **Plugins registered:** `prettier`, `better-tailwindcss`, `playwright`, `vitest`, `drizzle`, `zod`
- **Only 3 active custom rules:** `no-explicit-any: "error"`, `no-unused-vars` (ignore `^_` prefix), `no-import-type-side-effects`
- **Note:** Plugins like `better-tailwindcss`, `playwright`, `vitest`, `drizzle`, `zod` are registered but have **no custom rules enabled**. Their built-in recommended configs may still apply through the plugin registration.

### Vitest (`vitest.config.mts`)

- Environment: `jsdom`
- Setup: `src/tests/setup-env.ts`
- Include: `src/**/*.test.{ts,tsx}`
- Exclude: `.references/`, `tests/e2e/`, `node_modules/`

---

## 14. Unique Project Conventions

### React Compiler is ON

**Do NOT** manually add `useMemo`, `useCallback`, or `memo()`. The React Compiler handles memoization automatically. Adding manual memoization will conflict.

> **⚠ Conflict note:** `.github/instructions/performance.instructions.md` says "Use `React.memo` for expensive components" — this directly contradicts the React Compiler rule. **This setup prompt is authoritative.** `memo()`, `useMemo`, `useCallback` are all forbidden. The performance instructions file needs updating.

### Next.js 16 `searchParams` is a Promise

In Next.js 16, `searchParams` must be `await`ed:

```typescript
// ❌ WRONG (Next.js 15 pattern)
export default function Page({
  searchParams
}: {
  searchParams: { page?: string };
}) {
  const page = searchParams.page;
}

// ✅ CORRECT (Next.js 16)
export default async function Page({
  searchParams
}: {
  searchParams: Promise<{ page?: string }>;
}) {
  const params = await searchParams;
  const page = params.page;
}
```

### Next.js App Router Rules

From `.github/instructions/nextjs.instructions.md`:

- Every route directory needs `loading.tsx` + `error.tsx`
- Never access `Date.now()`, `localStorage`, `window`, `document` in Server Components
- Use Next.js `<Image>` for all images — never raw `<img>`
- Use `next/font` for all fonts — never manual `@font-face`
- Prefer static generation over SSR when possible
- All code must be Turbopack-compatible

### SSR-Safe Date Handling

```typescript
// WRONG in Server Component or shared code
const year = new Date().getFullYear();

// CORRECT — use SSR-safe hook
("use client");
import { useCurrentYear } from "@/hooks/use-now";
const year = useCurrentYear(); // null during SSR, number after hydration
```

### Error Handling with `cause`

```typescript
// Pattern used in src/lib/env.ts
throw new Error(`Validation failed:\n${errors}`, {
  cause: originalError
});
```

### Force-Dynamic Ban

Never use `export const dynamic = "force-dynamic"` at page level. Use `<Suspense>` boundaries or small `"use client"` wrappers instead.

### Zustand Store Pattern

```typescript
"use client";
import { create } from "zustand";
import { devtools, persist } from "zustand/middleware";

export const useMyStore = create<State>()(
  devtools(
    persist(
      set => ({
        /* initial state + actions */
      }),
      { name: "store-name" }
    ),
    { name: "MyStore" }
  )
);
```

### Tailwind Conventions

- Container queries: `@container/card`, `@[540px]/card:hidden`
- Important modifier: `h-4!` (not `!h-4`)
- Class ordering follows Tailwind Merge conventions

### Charts (Recharts)

`ResponsiveContainer` must be guarded with `isMounted` state — see `src/components/ui/chart.tsx`.

### Security Rules

From `.github/instructions/security.instructions.md`:

- Validate on both client AND server
- Never string-concatenate DB queries — always use Drizzle query builders
- Rate limiting for API routes
- Never expose stack traces in production
- Escape user-generated content (XSS prevention)
- Don't store sensitive data in `localStorage` / `sessionStorage`

---

## 15. VSCode Configuration

### Settings (`.vscode/settings.json`)

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.tabSize": 2,
  "eslint.lintTask.enable": true,
  "eslint.useFlatConfig": true,
  "eslint.validate": ["javascript", "typescript", "typescriptreact"],
  "explorer.fileNesting.enabled": true,
  "explorer.fileNesting.patterns": {
    "*.ts": "${capture}.test.ts, ${capture}.spec.ts",
    "*.tsx": "${capture}.test.tsx, ${capture}.spec.tsx"
  }
}
```

### Extensions (`.vscode/extensions.json`)

```json
{
  "recommendations": [
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "bradlc.vscode-tailwindcss",
    "PulkitGangwar.nextjs-snippets",
    "vitest.explorer"
  ],
  "unwantedRecommendations": [
    "hookyqr.beautify",
    "dbaeumer.jshint",
    "eg2.tslint"
  ]
}
```

---

## 16. Common Tasks — Step-by-Step

### Feature Discovery Checklist

Before implementing any feature, answer these questions:

1. **What entity/entities are involved?** → Check `schema.ts` for existing tables
2. **What relationships exist?** → Check FK references + junction tables (remember: no `relations()` — see §6)
3. **What validation rules apply?** → Define/check Zod schemas (separate create + update schemas)
4. **What auth level is required?** → Public, authenticated, admin, or role-based?
5. **What cache paths need invalidation?** → List all `revalidatePath()` targets
6. **Does a DAL already exist?** → Check `src/dal/` for existing implementations (18 DAL files)
7. **Are there composite keys?** → Override BaseDal methods to redirect (e.g., `"Use getUserRating(userId, comicId) instead"`)
8. **What tests are needed?** → Unit (mock DB/auth), integration (real DB), E2E (Playwright)

### Add a New Page

1. Create `src/app/(root)/my-feature/page.tsx` (Server Component by default)
2. Fetch data via DAL in the component body
3. Add `loading.tsx` and `error.tsx` in the same directory
4. Add navigation link in `src/components/layout/app-sidebar.tsx`
5. Add metadata via `export const metadata` or `generateMetadata()`

### Add a New Database Table

1. Define table in `src/database/schema.ts` with proper types, FKs (`onDelete: "cascade"`), indexes
2. Add `relations()` if the table has complex relationships (see §6 warning)
3. Run `pnpm db:push` (dev) or `pnpm db:generate` + `pnpm db:migrate` (prod)
4. Create DAL: `src/dal/my-table-dal.ts` extending `BaseDal<typeof myTable.$inferSelect>`
5. Create Zod schema: `src/schemas/my-table.schema.ts`
6. Create Server Actions: `src/actions/my-table.actions.ts`

### Add Authentication to a Page

```typescript
import { auth } from "@/auth";
import { redirect } from "next/navigation";

export default async function ProtectedPage() {
  const session = await auth();
  if (!session?.user) redirect("/auth/signin");
  return <div>Protected content</div>;
}
```

### Create a Server Action

1. Create `src/actions/my-feature.actions.ts` with `"use server"` directive
2. Check `auth()` → validate with Zod → call DAL → `revalidatePath()` → return `ActionResult<T>`
3. Never throw — always return `{ ok: false, error }` for failures

### Create a Client Component

1. Add `"use client"` at file top
2. Use hooks: `useState`, `useEffect`, event handlers, browser APIs
3. Do NOT use `useMemo`/`useCallback`/`memo` — React Compiler handles this
4. Use `useCurrentYear()` instead of `new Date()` for SSR safety

---

## 17. Testing

### Unit Tests (Vitest)

```bash
pnpm test                        # Run all
pnpm test -- --watch             # Watch mode
```

- Files: `src/**/*.test.{ts,tsx}`
- Environment: `jsdom` with setup at `src/tests/setup-env.ts`
- Mock external deps (database, auth)
- Test behavior, not implementation details
- Use `describe` / `it` blocks

### Testing Conventions (from `.github/instructions/testing.instructions.md`)

- **Accessibility:** Include accessibility checks in component tests
- **Test config:** Use `.env.test` for test-specific configuration
- **Cleanup:** Tests must clean up after themselves (no state leakage between tests)
- **Auth mocking:** Mock auth for unit tests; use real auth for E2E
- **Assertions:** Use Vitest built-in assertions (not external assertion libraries)
- **Naming:** Test files mirror source files: `my-feature.ts` → `my-feature.test.ts`

### E2E Tests (Playwright)

```bash
pnpm test:ui                     # Run E2E tests
pnpm test:ui:codegen             # Test code generator
```

- Page Object pattern
- Fixtures for test data
- Cross-browser testing

### Pre-PR Checklist

```bash
pnpm type-check          # 0 TypeScript errors
pnpm lint:fix            # 0 ESLint errors
pnpm test                # All unit tests pass
pnpm build               # Clean production build
```

---

## 18. Key Files Quick Reference

| File | Purpose |
| --- | --- |
| `src/database/schema.ts` | 27 tables, 4 enums, no `relations()` (604 lines) |
| `src/dal/base-dal.ts` | Abstract `BaseDal<T>` + error normalization |
| `src/dal/comic-dal.ts` | Reference DAL with eager loading via `.with()` |
| `src/actions/comic.actions.ts` | Reference Server Action with auth + Zod + DAL |
| `src/actions/types.ts` | `ActionResult<T>` discriminated union |
| `src/actions/auth-db.ts` | `getUserByUsername`, `verifyPassword` (bcryptjs) |
| `src/auth.ts` | NextAuth init — `{ handlers, auth, signIn, signOut }` |
| `src/auth-config.ts` | Session strategy, all callbacks (known bugs noted) |
| `src/auth-providers.ts` | GitHub + Credentials + Keycloak providers |
| `src/auth-adapter.ts` | DrizzleAdapter wiring |
| `src/lib/env.ts` | Zod-validated env vars — `getEnv()` not `process.env` (6 active fields) |
| `src/lib/query-client.ts` | React Query key factory + singleton |
| `src/hooks/use-now.tsx` | SSR-safe Date hook |
| `src/components/layout/layout-provider.tsx` | Provider stack order |
| `src/proxy.ts` | Middleware — protects `/dashboard` only (⚠ `/admin` unguarded) |
| `next.config.ts` | React Compiler, Turbopack, images, security headers |
| `appConfig.ts` | Structured config — mostly stubs (see §21) |
| `src/scripts/seed/seeders/baseSeed.ts` | Template method for all seeders |
| `src/scripts/seed/seedOrchestrator.ts` | Seed dependency resolution + orchestration |
| `src/app/api/seed/route.ts` | Seed REST API (5 HTTP methods) |
| `drizzle.config.ts` | Drizzle Kit config (schema path, dialect, pool) |

---

## 19. External Dependencies Map

| Category | Package | Version | Purpose |
| --- | --- | --- | --- |
| **Framework** | `next` | 16.1.6 | App Router, Server Components, Turbopack |
| **React** | `react` / `react-dom` | 19.2.4 | UI rendering, Server Components |
| **ORM** | `drizzle-orm` / `drizzle-kit` | 0.45.1 | Type-safe SQL, migrations |
| **DB Driver** | `postgres` | — | PostgreSQL client |
| **Auth** | `next-auth` | 5.0.0-beta.30 | Authentication, database sessions |
| **Auth Adapter** | `@auth/drizzle-adapter` | — | NextAuth ↔ Drizzle bridge |
| **Validation** | `zod` | 4.3.6 | Runtime schema validation (⚠ v4 — different API from v3) |
| **State** | `zustand` | 5.0.11 | Client state management |
| **Data Fetching** | `@tanstack/react-query` | 5.x | Client-side caching |
| **UI** | `@radix-ui/*` | — | Accessible primitives (via shadcn) |
| **Styling** | `tailwindcss` | 4.x | Utility-first CSS |
| **Icons** | `@tabler/icons-react` | — | Icon library |
| **Password** | `bcryptjs` | — | Password hashing |
| **CLI** | `commander` | 14.0.3 | Seed CLI (devDependency, not runtime) |
| **Monitoring** | `@sentry/nextjs` | — | Error tracking |
| **Testing** | `vitest` | 4.0.18 | Unit tests (jsdom) |
| **E2E Testing** | `playwright` | — | Browser E2E tests |
| **TypeScript** | `typescript` | 5.9.3 | Static type checking |

> **⚠ Zod v4 note:** This project uses Zod 4.3.6, which has a different API surface from the widely-documented Zod v3. Key differences include schema definition syntax, error formatting, and validation methods. Consult Zod v4 docs, not v3 tutorials.

---

## 20. Coding Standards Summary

### Core Rules

- **No `any` types** — ESLint enforces `no-explicit-any: "error"`
- **No manual memoization** — React Compiler is ON (`memo`, `useMemo`, `useCallback` forbidden)
- **No `force-dynamic`** — use Suspense boundaries instead
- **No raw `process.env`** — use `getEnv()` from `src/lib/env.ts` (auth files excepted)
- **No N+1 queries** — use `.with()` in DAL for related data
- **No API routes for mutations** — use Server Actions
- **Always validate inputs** — Zod schemas before DB operations
- **Always check auth** — `auth()` as first line in Server Actions
- **Always return `ActionResult<T>`** — never throw from actions
- **Always cascade deletes** — `{ onDelete: "cascade" }` on all FKs (exception: `auditLog.userId` → `"set null"`)
- **Use Title-Case** for `comicStatus` enum values
- **Use `$inferSelect`** for DAL type parameters, not raw table type
- **Use SSR-safe hooks** for Date/time in components (`useCurrentYear`, `useNow`)

### TypeScript Conventions (from `.github/instructions/typescript.instructions.md`)

- Use `interface` for object shapes, not `type` aliases
- Implement type guards for runtime narrowing (`unknown` → specific type)
- PascalCase component names matching file names
- Export prop interfaces for reusable components
- Create barrel exports (`index.ts`) for directories
- Functional components only — no class components
- No conditional hooks (hooks must always be called in same order)

### Documentation Standards (from `.github/instructions/documentation.instructions.md`)

- TSDoc comments required on functions, classes, hooks, complex types
- Document component props with descriptions
- Comment workarounds with reasons ("Why" not just "What")
- Keep docs in sync with code changes

### Security Standards (from `.github/instructions/security.instructions.md`)

- Validate on both client AND server
- Never string-concatenate DB queries — always use Drizzle query builders
- Escape user-generated content before rendering (XSS prevention)
- Never expose stack traces in production error responses
- Don't store sensitive data in `localStorage` / `sessionStorage`

---

## 21. Known Technical Debt

| Item | Impact | Location |
| --- | --- | --- |
| `proxy.ts` only protects `/dashboard`, not `/admin` | Admin routes unguarded | `src/proxy.ts` |
| `proxy.ts` checks cookie `"auth-token"`, not NextAuth session | May not integrate with actual auth system | `src/proxy.ts` |
| Raw `process.env` in auth files | Convention violation (accepted exception) | `auth-config.ts`, `auth-providers.ts`, `db.ts` |
| `env.ts` has ~60 commented-out field stubs | Only 6 active validations | `src/lib/env.ts` |
| No Drizzle `relations()` definitions | `.with()` limited to FK-inferred relations; `comment.parentId` broken | `src/database/schema.ts` |
| `performance.instructions.md` contradicts React Compiler | Says "use React.memo" — wrong per project config | `.github/instructions/performance.instructions.md` |
| `comment-rating-dal.ts` has no matching schema table | DAL references non-existent `commentRating` table | `src/dal/comment-rating-dal.ts` |
| Two comic schema files coexist | `comic-schema.ts` and `comic.schema.ts` — unclear which is canonical | `src/schemas/` |
| `appConfig.ts` mostly empty stubs | Only `database`, `auth.secret`, and `app` sections active; providers, email, redis, imageKit, cloudinary, sentry all commented out | `appConfig.ts` |

---

## 22. Feature Implementation Workflow

Full template — Discovery → Schema → DAL → Zod → Action → Component → Test → Docs:

1. **Discovery** — Run the Feature Discovery Checklist (§16)
2. **Schema** — Define table in `src/database/schema.ts` with types, FKs (`onDelete: "cascade"`), indexes. Add `relations()` if needed for complex relationships.
3. **DAL** — Create `src/dal/my-entity-dal.ts` extending `BaseDal<typeof myEntity.$inferSelect>`. Export as singleton.
4. **Zod Schemas** — Create `src/schemas/my-entity-schema.ts` with separate `createMyEntitySchema` and `updateMyEntitySchema`. Remember: Zod v4 API.
5. **Server Action** — Create `src/actions/my-entity.actions.ts`: `"use server"` → `auth()` → Zod validate → DAL call → `revalidatePath()` → return `ActionResult<T>`
6. **Server Component Page** — `src/app/(root)/my-feature/page.tsx` + `loading.tsx` + `error.tsx`
7. **Client Component** (if needed) — `"use client"`, no manual memo, SSR-safe hooks
8. **Tests** — Unit tests in `src/tests/`, mock DB/auth, test behavior not implementation, include accessibility checks
9. **Docs** — Update related documentation, add TSDoc comments to all public functions

---

## 23. Instruction Files Reference

Seven instruction files in `.github/instructions/` provide file-pattern-specific conventions for AI agents:

| File | Applies To | Purpose |
| --- | --- | --- |
| `code-review.instructions.md` | `**/*` | Code review standards and GitHub review guidelines |
| `documentation.instructions.md` | `**/*.md, **/*.ts, **/*.tsx` | TSDoc, README, and architecture documentation standards |
| `nextjs.instructions.md` | `**/app/**/*.tsx, **/app/**/*.ts` | App Router, Server/Client Components, data fetching |
| `performance.instructions.md` | `**/*.ts, **/*.tsx, **/*.css` | React, Next.js, DB, and runtime performance (**⚠ React.memo rule is outdated — contradicts React Compiler**) |
| `security.instructions.md` | `**/*.ts, **/*.tsx, **/*.js, **/*.jsx` | Auth, input validation, data protection, XSS prevention |
| `testing.instructions.md` | `**/*.test.ts, **/*.test.tsx, **/*.spec.ts` | Vitest unit tests, Playwright E2E, test environment setup |
| `typescript.instructions.md` | `**/*.ts, **/*.tsx` | Strict mode, interfaces, type guards, React component standards |

Key conventions from these files are merged into this setup prompt (§14, §17, §20). When conflicts exist between instruction files and this setup prompt, **this prompt is authoritative**.

---

## 24. Quality Gate Debugger

When debugging and fixing errors/warnings/deprecations, follow this workflow:

### Phase 1: Run Validation Scripts

```powershell
# Windows / PowerShell
pnpm type-check    # TypeScript errors
pnpm lint:fix      # ESLint errors/warnings
pnpm test          # Vitest unit tests
pnpm build         # Production build
```

### Phase 2: Document Issues

For each issue found, document in `docs/proposedFixes.MD` and `docs/proposedFixes.json`:

- File path and line number
- Error code and severity
- Root cause analysis
- Before/after code snippets
- Fix rationale and references

### Phase 3: Batch Fixes

Apply fixes in this order (highest impact first):

1. Import resolution errors
2. Type errors
3. Build errors
4. Test failures
5. Lint warnings

### Phase 4: Verify

Rerun all validation scripts until all gates pass with zero errors/warnings.

### Key Debugging Patterns

| Pattern | Problem | Solution |
| --- | --- | --- |
| `new Date()` in Server Component | `NEXT_PRERENDER_CURRENT_TIME` | Use `useCurrentYear()` hook |
| `toHaveText()` without argument | Playwright 1.58+ requires arg | Use `toBeVisible()` instead |
| `try { ... } catch { throw err }` | Useless try/catch | Remove try/catch wrapper |
| Duplicate export | `TS2300` error | Use `export type { X }` for types |
| `isolatedModules` type re-export | `TS1205` error | Separate type exports from value exports |

### Documentation Requirements

Every significant fix must be recorded in both:

1. `docs/proposedFixes.MD` - human readable format
2. `docs/proposedFixes.json` - structured JSON with keys: file, line, issue, fix, before, after, rationale, references
