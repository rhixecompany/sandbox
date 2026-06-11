# ComicWise — Complete Development Reference

**Last Updated:** March 13, 2026 **Framework:** Next.js 16.1.6 + React 19.2.4 + Drizzle ORM 0.45.1 + PostgreSQL + TypeScript 5.9.3 **Status:** ✅ Production-Grade (Phase 4.3 ✅ | Batch 4 ✅ | Quality: 98/100 | Tests: 241/241)

**Quick Access Prompts:**

- **Session Quick Reference** (400 lines): `.github/prompts/comicwise-session.prompt.md`
- **Full Development Guide** (2500+ lines): `.github/prompts/comicwise-development.prompt.md`

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Technology Stack](#technology-stack)
3. [Architecture & Data Flow](#architecture--data-flow)
4. [Essential Commands](#essential-commands)
5. [Environment Configuration](#environment-configuration)
6. [Database Schema](#database-schema)
7. [Authentication System](#authentication-system)
8. [Data Access Layer (DAL)](#data-access-layer-dal)
9. [Server Actions & Mutations](#server-actions--mutations)
10. [Seeding System (CLI + REST API)](#seeding-system-cli--rest-api)
11. [Frontend Architecture](#frontend-architecture)
12. [Next.js Configuration](#nextjs-configuration)
13. [TypeScript & Tooling](#typescript--tooling)
14. [Project Conventions](#project-conventions)
15. [Common Tasks Workflow](#common-tasks-workflow)
16. [Testing Standards](#testing-standards)
17. [Performance Guidelines](#performance-guidelines)
18. [Security Standards](#security-standards)
19. [Deployment Checklist](#deployment-checklist)
20. [Technical Debt & Known Issues](#technical-debt--known-issues)
21. [Implementation Phases](#implementation-phases)

---

## Project Overview

**ComicWise** is a full-stack web application for discovering, reading, managing, and sharing manga/comics. It features:

- 📖 **Comic Catalog** — Browse thousands of comics with filtering, search, and pagination
- 👤 **User Profiles** — Personalized reading preferences, bookmarks, and progress tracking
- 📔 **Chapter Reader** — Immersive reader with progress tracking, keyboard shortcuts, zoom controls
- ⭐ **Rating System** — User ratings (1-5 stars), aggregate display, review writing
- 💬 **Comments & Discussion** — Chapter-level comments with threading support
- 🔖 **Bookmark Management** — Track reading progress, status categories (reading, plan to read, completed)
- 👨‍💼 **Admin Dashboard** — Full CRUD for all entities, user management, moderation, audit logs
- 🔐 **RBAC** — Role-based access control (user, moderator, admin) with fine-grained permissions

### Project Goals

- ✅ Zero TypeScript errors
- ✅ Zero ESLint errors
- ✅ 80%+ test coverage
- ✅ Production build succeeds
- ✅ All pages accessible and responsive
- ✅ Core Web Vitals passing
- ✅ Zero security vulnerabilities

---

## Technology Stack

### Core Framework & Runtime

| Layer | Technology | Version | Purpose |
| --- | --- | --- | --- |
| **Frontend Framework** | Next.js | 16.1.6 | App Router, Server Components, Turbopack |
| **React** | React / React DOM | 19.2.4 | UI library with Server Components |
| **Runtime TypeScript** | TypeScript | 5.9.3 | Static type checking (strict mode) |
| **Node Runtime** | Node.js | 18+ | JavaScript runtime |

### Database & ORM

| Component | Technology | Version | Purpose |
| --- | --- | --- | --- |
| **Database** | PostgreSQL | 14+ | Primary relational database |
| **ORM** | Drizzle ORM | 0.45.1 | Type-safe database queries |
| **ORM CLI** | Drizzle Kit | 0.45.1 | Migrations and schema management |
| **Driver** | postgres-js | — | PostgreSQL protocol driver |

### Authentication & Authorization

| Component | Technology | Version | Purpose |
| --- | --- | --- | --- |
| **Auth Framework** | NextAuth.js | v5.0.0-beta.30 | Session & OAuth management |
| **Auth Adapter** | @auth/drizzle-adapter | — | NextAuth ↔ Drizzle integration |
| **Password Hashing** | bcryptjs | — | Secure password hashing |
| **OAuth Providers** | GitHub, Keycloak | — | 3rd-party authentication |

### State Management & Validation

| Component | Technology | Version | Purpose |
| --- | --- | --- | --- |
| **Client State** | Zustand | 5.0.11 | Minimal client-side state |
| **Data Fetching** | React Query | 5.x | Server-state caching on client |
| **Validation** | Zod | 4.3.6 | Runtime schema validation (⚠️ v4 API) |
| **Form State** | React Hook Form | — | Form state management |

### UI & Styling

| Component | Technology | Purpose |
| --- | --- | --- | --- |
| **CSS Framework** | Tailwind CSS | 4.x | Utility-first styling |
| **Component Library** | shadcn/ui | Accessible pre-built components |
| **Primitives** | Radix UI | Accessible component primitives |
| **Icons** | Tabler Icons | Icon library |
| **Charts** | Recharts | Data visualization |
| **Tables** | TanStack Table | Advanced data tables |

### Development & Testing

| Component | Technology | Version | Purpose |
| --- | --- | --- | --- |
| **Build Tool** | Turbopack | Built-in | Default Next.js bundler (file system caching) |
| **Linting** | ESLint | Flat config | Code quality |
| **Formatting** | Prettier | — | Code formatting |
| **Unit Testing** | Vitest | 4.0.18 | Unit test framework (jsdom) |
| **E2E Testing** | Playwright | — | Browser automation testing |
| **Package Manager** | pnpm | 8+ | Monorepo-ready package management |

### Monitoring & Observability

| Component | Technology | Purpose |
| --- | --- | --- |
| **Error Tracking** | Sentry | Error monitoring (optional, stubs present) |
| **Caching** | Redis/Upstash | Session caching (optional, stubs present) |

---

## Architecture & Data Flow

### Application Architecture

```
┌─────────────────────────────────────────────────────┐
│              Next.js 16 App Router                  │
│  (src/app with route groups, layouts, API routes)  │
└────────────────┬────────────────────────────────────┘
                 ↓
         ┌───────────────┐
         │ Server        │
         │ Components    │ ← Default component type
         │ (RSC)         │   Fetch data here
         └───────┬───────┘
                 ↓
      ┌──────────────────────┐
      │  Server Actions      │
      │  ("use server")      │ ← Primary mutation pattern
      │  (src/actions/)      │
      └────────┬─────────────┘
               ↓
      ┌────────────────────────────┐
      │  Data Access Layer (DAL)   │
      │  (src/dal/)                │ ← All DB reads go here
      │  - Eager loading via .with()
      │  - Type-safe queries       │
      │  - Singleton exports       │
      └────────┬───────────────────┘
               ↓
      ┌────────────────────────────┐
      │  Drizzle ORM               │
      │  (src/database/)           │
      │  - Schema (27 tables)      │
      │  - Query builders          │
      │  - Migrations              │
      └────────┬───────────────────┘
               ↓
      ┌────────────────────────────┐
      │  PostgreSQL Database       │
      │  (Neon or Local)           │
      └────────────────────────────┘
```

### Data Flow Sequence

1. **Server Component** → Renders on server
2. **Data Fetching** → DAL calls `db.query.*` with `.with()` eager loading
3. **Result** → Returns typed data to component
4. **Rendering** → Server renders HTML + RSC payload
5. **Hydration** → Client hydrates to interactive state
6. **Mutations** → Server Actions handle form submissions

### Key Pattern: Server Action Flow

```typescript
// 1. Server Action (src/actions/my-feature.actions.ts)
"use server";
export async function createItem(input: unknown) {
  // 2. Auth check
  const session = await auth();
  if (!session) return { ok: false, error: "Not authenticated" };

  // 3. Zod validation
  const parsed = MySchema.safeParse(input);
  if (!parsed.success) return { ok: false, error: "Invalid" };

  // 4. DAL operation
  const result = await myDal.create(parsed.data);

  // 5. Cache invalidation
  revalidatePath("/items");

  // 6. Return ActionResult
  return { ok: true, data: result };
}

// In Client Component:
const result = await createItem(formData);
if (result.ok) showSuccess();
else showError(result.error);
```

---

## Essential Commands

### Development

```bash
# Start development server (Turbopack, port 3000)
pnpm dev

# Type checking (tsc --noEmit)
pnpm type-check
pnpm type-check:watch    # Watch mode

# Linting & formatting
pnpm lint:fix            # ESLint + Prettier auto-fix
pnpm lint:strict         # ESLint with --max-warnings=0
pnpm format              # Prettier --write
pnpm format:check        # Check without writing

# Production build
pnpm build               # Full build + type generation
pnpm build:debug         # Build with --debug-prerender

# Type generation (runs automatically in prebuild/predev)
pnpm type-gen            # Generate next-env.d.ts + typed routes
```

### Database

```bash
# Development (no migration files)
pnpm db:push             # Apply schema changes to dev DB

# Production (creates migration files)
pnpm db:generate         # Generate SQL migration files
pnpm db:migrate          # Run migration files

# Utilities
pnpm db:studio           # Open Drizzle Studio UI
pnpm db:reset            # Drop + regenerate + push (dev only!)
pnpm db:check            # Verify migration consistency
pnpm db:drop             # Drop all migrations
pnpm db:pull             # Introspect existing DB
```

### Testing

```bash
# Unit tests (Vitest, jsdom)
pnpm test                # Run all tests
pnpm test:watch          # Watch mode
pnpm test:coverage       # Coverage report

# E2E tests (Playwright)
pnpm test:ui             # Run E2E tests
pnpm test:ui:codegen     # Record new E2E tests
```

### Seeding

```bash
# CLI (direct, no server required)
pnpm seed --dry-run --verbose     # Validate without writing
pnpm seed:all                     # Seed all entities
pnpm seed:comics --force          # Upsert comics
pnpm seed:chapters --image-strategy=local --batch-size=500

# REST API (requires dev server: pnpm dev)
curl http://localhost:3000/api/seed                  # GET - validate
curl -X POST http://localhost:3000/api/seed \
  -H 'Content-Type: application/json' \
  -d '{"entities":"all"}'                            # POST - seed
curl -X DELETE http://localhost:3000/api/seed        # DELETE - clear
```

### Quality Gate (Required Before PR)

```bash
pnpm type-check          # Must be 0 TypeScript errors
pnpm lint:fix            # ESLint + Prettier auto-fix
pnpm test                # All unit tests pass
pnpm build               # Production build succeeds
```

---

## Environment Configuration

### Create `.env.local`

Copy from `.env.local.example` and fill in:

```env
# ── Required ──
DATABASE_URL="postgresql://user:pass@localhost:5432/comicbook"
AUTH_SECRET="$(openssl rand -hex 32)"    # Min 32 chars
NEXT_PUBLIC_API_URL="http://localhost:3000"
NODE_ENV="development"

# ── NextAuth URLs ──
AUTH_URL="http://localhost:3000"         # Base URL for callbacks

# ── Optional: Neon Serverless ──
NEON_DATABASE_URL="postgresql://..."

# ── Optional: Debug ──
DEBUG="false"

# ── Optional: OAuth (GitHub) ──
GITHUB_CLIENT_ID="your_client_id"
GITHUB_CLIENT_SECRET="your_client_secret"

# ── Optional: OAuth (Keycloak) ──
KEYCLOAK_CLIENT_ID="comicwise"
KEYCLOAK_CLIENT_SECRET="your_secret"
KEYCLOAK_ISSUER="https://keycloak.example.com/realms/comicwise"

# ── Optional: Image CDN (ImageKit) ──
IMAGEKIT_PUBLIC_KEY="..."
IMAGEKIT_PRIVATE_KEY="..."
IMAGEKIT_URL_ENDPOINT="https://ik.imagekit.io/youraccount"
```

### Runtime Validation

Only **6 fields** are actively validated via Zod in `src/lib/env.ts`:

- `DATABASE_URL`, `NEON_DATABASE_URL`, `AUTH_SECRET`, `NEXT_PUBLIC_API_URL`, `NODE_ENV`, `DEBUG`

Remaining ~60 fields (OAuth, ImageKit, Sentry, Redis, email) are stubs for future integration.

**Access via `getEnv()`** — Never use raw `process.env` in app code:

```typescript
import { getEnv } from "@/lib/env";
const apiUrl = getEnv().NEXT_PUBLIC_API_URL; // ✅ Type-safe
```

**Known Exception:** `auth-config.ts`, `auth-providers.ts`, `db.ts` use raw `process.env` as they load before app initialization. Do not follow this pattern elsewhere.

---

## Database Schema

### Overview

**27 tables** defined in `src/database/schema.ts` (604 lines), **4 enums**, **zero explicit `relations()`** definitions (FK-inferred only).

### Enums

```typescript
// Comic status (Title-Case)
comicStatus: "Ongoing" |
  "Hiatus" |
  "Completed" |
  "Dropped" |
  "Season End" |
  "Coming Soon";

// User roles (lowercase)
userRole: "user" | "admin" | "moderator";

// RBAC enums
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

### Table Categories

| Category | Tables | Count |
| --- | --- | --- |
| **Auth/User** | `user`, `account`, `session`, `verificationToken`, `authenticator`, `passwordResetToken` | 6 |
| **Content** | `type`, `author`, `artist`, `genre`, `comic`, `chapter`, `comicImage`, `chapterImage` | 8 |
| **Junctions** | `comicToGenre` | 1 |
| **User Activity** | `bookmark`, `comment`, `readingProgress`, `readerSettings`, `rating`, `notification`, `userPreference` | 7 |
| **RBAC** | `role`, `permission`, `rolePermission`, `userRole2` | 4 |
| **Audit** | `auditLog` | 1 |
| **TOTAL** | — | **27** |

### Key Table Details

| Table | Key Column | Critical Notes |
| --- | --- | --- |
| `user` | `id: text (UUID)` | NOT integer. Password nullable (OAuth). Soft delete via `deletedAt`. JSONB `settings` column. |
| `comic` | `rating: decimal(10,1)` | Aggregate display rating. NOT integer. `status` is Title-Case enum. |
| `rating` | `rating: integer (1-5)` | Per-user stars. Different type from `comic.rating`! Aggregate via `AVG()`. |
| `bookmark` | Composite PK `(userId, comicId)` | Upsert via `onConflictDoUpdate`. |
| `chapter` | Composite unique `(comicId, chapterNumber)` | — |
| `comment` | `parentId` FK missing `.references()` | ⚠️ Cannot use `.with()` for threading. Manual SQL JOIN needed. |
| `auditLog` | `userId` → `"set null"` | ⚠️ Exception: NOT cascade (preserves audit trail). |

### Foreign Keys & Cascade Rules

```typescript
// Rule: All FK columns must have { onDelete: "cascade" }
comic.authorId        → CASCADE
comic.artistId        → CASCADE
chapter.comicId       → CASCADE
bookmark.userId       → CASCADE
comment.userId        → CASCADE
// ... etc

// Exception: auditLog.userId → "set null" (preserve audit trail)
auditLog.userId → SET NULL
```

### Detailed Table Schemas

> For complete entity relationships and constraints, see `docs/database-context-map.md`.

#### User Table

| Column | Type | Notes |
| --- | --- | --- |
| `id` | `text` (UUID) | Primary key. NOT integer. |
| `name` | `text` | Nullable |
| `email` | `text` | UNIQUE, NOT NULL |
| `emailVerified` | `timestamp` | Nullable |
| `image` | `text` | Profile picture URL |
| `password` | `text` | bcrypt hash, nullable for OAuth users |
| `role` | `userRole` enum | `user \| admin \| moderator`, default: `user` |
| `status` | `boolean` | Account active/inactive |
| `settings` | `jsonb` | `{ emailNotifications, profileVisibility, readingHistoryVisibility }` |
| `deletedAt` | `timestamp` | Soft delete, nullable |
| `createdAt` / `updatedAt` | `timestamp` | Auto-managed |

**Indexes:** `userEmailIdx`, `userRoleIdx` **⚠️ Common mistake:** Forgetting to filter `WHERE deletedAt IS NULL` in queries.

#### Comic Table

| Column | Type | Notes |
| --- | --- | --- |
| `id` | `serial` | Primary key |
| `title` | `text` | UNIQUE |
| `slug` | `text` | UNIQUE, URL-friendly — primary query parameter |
| `description` | `text` | — |
| `coverImage` | `text` | Image URL |
| `status` | `comicStatus` enum | Title-Case only |
| `publicationDate` | `timestamp` | — |
| `rating` | `decimal(10,1)` | Aggregate display rating, default 0. NOT integer. |
| `views` | `integer` | View counter, default 0 |
| `authorId` / `artistId` / `typeId` | `integer` FK | CASCADE delete |
| `searchVector` | `text` | For full-text search (not PostgreSQL `tsvector`) |
| `createdAt` / `updatedAt` | `timestamp` | Auto-managed |

**Indexes:** 9 indexes covering slug, title, status, rating, views.

#### Chapter Table

| Column                    | Type         | Notes          |
| ------------------------- | ------------ | -------------- |
| `id`                      | `serial`     | Primary key    |
| `slug`                    | `text`       | UNIQUE         |
| `title`                   | `text`       | —              |
| `chapterNumber`           | `integer`    | Release order  |
| `comicId`                 | `integer` FK | CASCADE delete |
| `views`                   | `integer`    | Default 0      |
| `createdAt` / `updatedAt` | `timestamp`  | Auto-managed   |

**Unique:** `slug`, composite `(comicId, chapterNumber)` — critical for idempotent upserts.

#### Bookmark Table

| Column | Type | Notes |
| --- | --- | --- |
| `userId` | `text` FK | CASCADE delete |
| `comicId` | `integer` FK | CASCADE delete |
| `lastReadChapterId` | `integer` FK | Nullable |
| `status` | `text` | Reading, Plan to Read, Completed, On Hold, Dropped |
| `notes` | `text` | User notes |
| `createdAt` / `updatedAt` | `timestamp` | Auto-managed |

**Primary Key:** Composite `(userId, comicId)` — enables idempotent upserts via `onConflictDoUpdate`.

#### Reading Progress Table

| Column | Type | Notes |
| --- | --- | --- |
| `id` | `serial` | Primary key |
| `userId` | `text` FK | CASCADE delete |
| `comicId` / `chapterId` | `integer` FK | CASCADE delete |
| `pageNumber` | `integer` | Current page in chapter |
| `scrollPosition` / `scrollPercentage` | `integer` | Scroll tracking |
| `progressPercent` | `integer` | 0-100, how far through comic |
| `completedAt` | `timestamp` | Nullable, when finished |
| `lastReadAt` | `timestamp` | Tracks reading activity |

**Indexes:** userId, comicId, chapterId, lastReadAt, composite (userId, comicId). **Analytics:** `lastReadAt` and `progressPercent` enable "recently read" feed, progress bars, "continue reading" resume, and engagement tracking.

#### Notification Table

| Column | Type | Notes |
| --- | --- | --- |
| `id` | `serial` | Primary key |
| `userId` | `text` FK | CASCADE delete |
| `type` | `text` | `new_chapter \| comment_reply \| system` |
| `title` / `message` | `text` | Notification content |
| `link` | `text` | Nullable, URL to navigate to |
| `read` | `boolean` | Default false |
| `comicId` / `chapterId` | `integer` FK | Nullable, CASCADE delete |

**Indexes:** userId, read, type, createdAt, composite (userId, read).

#### Comment Table

| Column | Type | Notes |
| --- | --- | --- |
| `id` | `serial` | Primary key |
| `userId` | `text` FK | CASCADE delete |
| `chapterId` | `integer` FK | CASCADE delete |
| `content` | `text` | — |
| `parentId` | `integer` | Nullable, self-reference for threaded replies |
| `deletedAt` | `timestamp` | Soft delete |

**⚠️ Known issue:** `parentId` is missing `.references()` — cannot use `.with()` for threading.

### Soft Delete Pattern

Filter `WHERE deletedAt IS NULL` in user queries:

```typescript
// ✅ Correct
const users = await db.query.user.findMany({
  where: isNull(user.deletedAt)
});

// ❌ Wrong (includes soft-deleted users)
const users = await db.query.user.findMany();
```

### ⚠️ Missing Relations

**No explicit `relations()` definitions exist** in schema.ts. DALs rely entirely on FK inference:

- **FK-inferred relations work:** `comic.authorId` → `.with({ author: true })` ✅
- **Junction tables work:** `comicToGenre` → `.with({ genres: { with: { genre: true } } })` ✅
- **comment.parentId broken:** Has NO `.references()` → `.with()` cannot load parent/replies ❌

If you need advanced relations, add `relations()` to schema.ts first.

### Search Vector Fields

`comic.searchVector`, `author.searchVector`, `artist.searchVector` are stored as `text` columns (not PostgreSQL `tsvector`). Used for text search indexing.

---

## Authentication System

### 4-File Modular Architecture

```typescript
src / auth.ts; // NextAuth init, exports { handlers, auth, signIn, signOut }
src / auth - config.ts; // Session strategy, callbacks (session, jwt, signIn, redirect)
src / auth - providers.ts; // GitHub, Credentials, Keycloak provider array
src / auth - adapter.ts; // DrizzleAdapter wiring to schema tables
```

### Session Strategy

- **Type:** Database sessions (NOT JWT)
- **Duration:** `maxAge: 30 days`, `updateAge: 1 day`
- **Storage:** `session` table, linked to `user` via `userId`

### Credentials Provider

```typescript
async authorize(
  credentials: Partial<Record<"username" | "password", unknown>>
): Promise<User | null> {
  const username = typeof credentials.username === "string" ? credentials.username : undefined;
  const password = typeof credentials.password === "string" ? credentials.password : undefined;
  if (!username || !password) return null;

  const user = await getUserByUsername(username);      // src/actions/auth-db.ts
  if (user?.passwordHash && await verifyPassword(password, user.passwordHash)) return user;
  return null;
}
```

### Password Verification (`src/actions/auth-db.ts`)

```typescript
import bcrypt from "bcryptjs";
export async function verifyPassword(
  plain: string,
  hash: string
): Promise<boolean> {
  return bcrypt.compare(plain, hash);
}
```

### Server-Side Usage

```typescript
import { auth } from "@/auth";
const session = await auth();
if (!session?.user) redirect("/auth/signin");

// Check admin role
const u = session.user as { role?: unknown };
const isAdmin = typeof u?.role === "string" && u.role === "admin";
```

### Client-Side Usage

```typescript
import { useSession } from "next-auth/react";
const { data: session } = useSession();

// OAuth sign-in
await signIn("github", { redirectTo: "/dashboard" });

// Credentials sign-in
const result = await signIn("credentials", {
  username: "user",
  password: "pass",
  redirect: false
});
```

### Auth API Route

```typescript
// src/app/api/auth/[...nextauth]/route.ts
export { GET, POST } from "@/auth";
```

### Known Bugs

- `signIn` callback blocks users without email → May fail for OAuth-only providers
- `redirect` callback falls back to `/dashboard` for external URLs → Doesn't respect intent
- `proxy.ts` checks cookie `"auth-token"`, not NextAuth session → May not integrate with auth
- `/admin` routes unguarded despite `proxy.ts` matcher → Security gap

---

## Data Access Layer (DAL)

### Base Class Pattern (`src/dal/base-dal.ts`)

All DALs extend `BaseDal<T>` and implement 5 core methods:

```typescript
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
    // Error normalization: UNIQUE → "already exists", FK → "related not found", etc.
  }
}
```

### Implementation Template

```typescript
import { db } from "@/database/db";
import { comic } from "@/database/schema";
import { BaseDal, type DalOptions } from "./base-dal";

type ComicType = typeof comic.$inferSelect; // ✅ Use $inferSelect, NOT typeof comic

export class ComicDal extends BaseDal<ComicType> {
  async list(options?: DalOptions) {
    // ✅ Use .with() for eager loading — NEVER loop + query (N+1)
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
    return db.query.comic.findFirst({
      where: eq(comic.id, id),
      with: { author: true, chapters: true }
    });
  }

  async create(data: CreateComicInput) {
    /* ... */
  }
  async update(id: string, data: UpdateComicInput) {
    /* ... */
  }
  async delete(id: string) {
    /* ... */
  }
}

export const comicDal = new ComicDal(); // ✅ Singleton export — REQUIRED
```

### Critical Rules

- **Type Definition:** Always use `typeof table.$inferSelect`, NOT raw `typeof table`
- **Eager Loading:** Use `.with()` for all related data — NEVER `for` loop + queries
- **Singleton Exports:** Export DAL instance at file bottom
- **Error Handling:** Use `handleError()` for consistent normalization
- **N+1 Prevention:** See anti-patterns below

### N+1 Anti-Pattern Catalog

| Trap | ❌ Wrong | ✅ Right |
| --- | --- | --- |
| Comics + Authors | `for (comic of comics) { await getAuthor(id) }` | `.with({ author: true })` |
| Bookmarks + Comics | Loop through bookmarks, fetch each | `.with({ comic: { with: { genres: true } } })` |
| Comment Threading | `comment.parentId` has no FK ref | Manual SQL JOIN (add `relations()` to fix) |
| Dashboard Stats | Separate count/sum/avg queries | Single aggregation query |

### N+1 Solutions with Code Examples

#### Problem 1: Comics with Authors

```typescript
// ❌ N+1: 101 queries for 100 comics
const comics = await db.select().from(comic);
for (const c of comics) {
  c.author = await db
    .select()
    .from(author)
    .where(eq(author.id, c.authorId));
}

// ✅ Solution: 1-2 queries with eager loading
const comicsWithAuthors = await db.query.comic.findMany({
  with: { author: true, artist: true, type: true, genres: true }
});
```

#### Problem 2: Bookmarks with Comic + Genres

```typescript
// ❌ N+1: 41 queries for 20 bookmarks
const bookmarks = await db
  .select()
  .from(bookmark)
  .where(eq(bookmark.userId, userId));
for (const b of bookmarks) {
  b.comic = await db
    .select()
    .from(comic)
    .where(eq(comic.id, b.comicId));
  b.comic.genres = await db
    .select()
    .from(comicToGenre)
    .leftJoin(genre, eq(comicToGenre.genreId, genre.id))
    .where(eq(comicToGenre.comicId, b.comicId));
}

// ✅ Solution: Single query with nested eager loading
const bookmarksWithComics = await db.query.bookmark.findMany({
  where: eq(bookmark.userId, userId),
  with: {
    comic: {
      with: {
        author: true,
        artist: true,
        genres: { with: { genre: true } }
      }
    },
    lastReadChapter: true
  },
  orderBy: b => desc(b.updatedAt)
});
```

#### Problem 3: Threaded Comments

```typescript
// ❌ Exponential queries for nested replies
const comments = await db
  .select()
  .from(comment)
  .where(eq(comment.chapterId, chapterId));
for (const c of comments) {
  c.user = await db.select().from(user).where(eq(user.id, c.userId));
  if (c.parentId) {
    c.parent = await db
      .select()
      .from(comment)
      .where(eq(comment.id, c.parentId));
  }
}

// ✅ Solution: Eager loading with user projection
const comments = await db.query.comment.findMany({
  where: eq(comment.chapterId, chapterId),
  with: {
    user: { columns: { id: true, name: true, image: true } },
    parent: { with: { user: true } }
  }
});
```

### Performance Index Strategy

| Table | Index | Columns | Purpose |
| --- | --- | --- | --- |
| `user` | `userEmailIdx` | email | Auth login |
| `comic` | `comicSlugIdx` | slug | URL lookups |
| `comic` | `comicStatusIdx` | status | Filter by status |
| `chapter` | `chapterComicIdIdx` | comicId | Get chapters for comic |
| `chapter` | `chapterComicChapterIdx` | (comicId, chapterNumber) | Get specific chapter |
| `bookmark` | `bookmarkUserIdIdx` | userId | Get user's bookmarks |
| `readingProgress` | `readingProgressUserComicIdx` | (userId, comicId) | Get progress for comic |
| `comment` | `commentChapterIdIdx` | chapterId | Comments on chapter |
| `notification` | `notificationUserReadIdx` | (userId, read) | Unread notifications |

**Rule:** If your WHERE clause includes a column not indexed, queries will full-table scan.

### Current DAL Files (18 total)

All extend `BaseDal<T>` with proper eager loading via `.with()`.

---

## Server Actions & Mutations

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
  // 1. Auth check (first!)
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

    // 4. Cache invalidation
    revalidatePath("/comics");

    // 5. Return ActionResult (never throw!)
    return { ok: true, data: comic };
  } catch (e) {
    return { ok: false, error: "Failed to create comic" };
  }
}
```

### Rules

- **All mutations** go through Server Actions — NOT API routes
- **Always validate** with Zod before DAL
- **Always check auth** as first step
- **Return `ActionResult<T>`** — never throw
- **Call `revalidatePath()`** after mutations
- **Never expose internal errors** to client

---

## Seeding System (CLI + REST API)

### When to Use What

| Context | Pattern | Why |
| --- | --- | --- |
| **App mutations** (UI) | Server Action → DAL | Type-safe, auth, validation, cache invalidation |
| **Bulk seeding** | Seeder → direct Drizzle | Batch performance (50k items in ~8 min vs hours) |

### Seeder Template (`BaseSeed<T>`)

All seeders extend `BaseSeed<T>` and override 4 methods:

```typescript
import { BaseSeed } from "./baseSeed";
import { db } from "@/database/db";
import { myEntity } from "@/database/schema";

export class MyEntitySeeder extends BaseSeed<MyEntity> {
  entityName = "MyEntity";
  entityDataKey = "myEntities";
  dependencies = []; // Seeders that must run first
  dataSourceName = "my-entity";

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

export const myEntitySeeder = new MyEntitySeeder();
```

### Dependency Graph

```
types ──┐
        ├─→ authors ──┐
genres ─┤             ├─→ comics ──→ chapters
        ├─→ artists ──┘
users (independent)
```

### CLI Commands

```bash
# Validate (dry-run)
pnpm seed --dry-run --verbose

# Seed all with options
pnpm seed:all --image-strategy=urls --batch-size=100 --concurrency=3

# Seed specific entity
pnpm seed:comics --force --image-strategy=local

# Flags
--dry-run                              # Validate without writing
--verbose                              # Detailed output
--image-strategy=urls|local|imagekit   # Image handling
--batch-size=N                         # Records per batch
--concurrency=N                        # Parallel batches
--skip-validation                      # Skip Zod (⚠️ dangerous)
--no-transaction                       # Disable per-batch transactions
--force                                # Upsert mode (onConflictDoUpdate)
```

### Image Strategies

```bash
--image-strategy=urls      # Default: use original URLs
--image-strategy=local     # Download to ./public/comics/{type}/{id}.{ext}
--image-strategy=imagekit  # Upload to ImageKit CDN
```

### Image Helper (`src/lib/imageHelper.ts`)

The image helper provides robust image downloading for seeding:

```typescript
export async function downloadImage(
  url: string,
  targetPath: string,
  options?: { maxRetries?: number; timeout?: number }
): Promise<{ success: boolean; path: string }>;

export function validateImageFormat(url: string): boolean; // jpeg, png, webp, avif
export function getImageSizeLimit(): number; // SEED_MAX_IMAGE_SIZE_BYTES, default 5MB
```

**Features:**

- Format validation (jpeg, png, webp, avif only)
- Size limits (configurable, default 5MB)
- Retry logic with exponential backoff (default 3 retries)
- Timeout handling (default 10s)
- Fallback to placeholder on failure

### Seed Configuration (`src/scripts/seed/config.ts`)

```typescript
export const seedConfig = {
  userBatchSize: 50,
  comicBatchSize: 100,
  chapterBatchSize: 500,
  downloadImages: true,
  imageDirectory: "/comics",
  maxImageRetries: 3,
  imageTimeout: 10000,
  validateBeforeSeed: true,
  skipInvalidRecords: false,
  verbose: process.env.SEED_VERBOSE === "true",
  logProgress: true
};
```

### REST API (`src/app/api/seed/route.ts`)

| Method   | Purpose                      | Auth Required (prod) |
| -------- | ---------------------------- | -------------------- |
| `GET`    | Validate (dry-run)           | No                   |
| `POST`   | Full seed (clear + populate) | Yes (admin)          |
| `PATCH`  | Upsert only                  | Yes (admin)          |
| `PUT`    | Reset (delete + reseed)      | Yes (admin)          |
| `DELETE` | Clear all seed data          | Yes (admin)          |

### Request Body Schema

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

---

## Frontend Architecture

### Root Layout & Provider Stack (`src/app/layout.tsx` + `src/components/layout/layout-provider.tsx`)

```
Root Layout
├── 7 Fonts (next/font/local)
│   ├── IBM Plex Sans, Bebas Neue, Schibsted Grotesk
│   ├── Martian Mono, Fira Sans, Fira Mono
│   └── Plus 1 more
├── Metadata (title, OpenGraph, viewport)
├── Body
│   └── Suspense boundary
│       └── LayoutProvider
│           ├── SessionProvider (NextAuth)
│           ├── QueryClientProvider (React Query)
│           ├── ThemeProvider
│           ├── TooltipProvider
│           ├── Children
│           ├── ReactQueryDevtools (dev only)
│           └── Toaster (lazy-loaded)
```

### React Query Keys (`src/lib/query-client.ts`)

```typescript
export const queryKeys = {
  comics: {
    all: ["comics"],
    list: filters => ["comics", "list", filters],
    detail: slug => ["comics", "detail", slug],
    chapters: comicId => ["comics", comicId, "chapters"]
  },
  bookmarks: {
    all: ["bookmarks"],
    list: userId => ["bookmarks", "list", userId],
    check: (userId, comicId) => [
      "bookmarks",
      "check",
      userId,
      comicId
    ]
  }
  // ... etc
};
```

- **Server:** New `QueryClient` per request
- **Browser:** Singleton with `staleTime: 60s`, `gcTime: 5min`, retry 3 exponential backoff

### Middleware (`src/proxy.ts`)

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

⚠️ **Incomplete:** Only `/dashboard` protected. `/admin` routes unguarded. Cookie check may not align with NextAuth sessions.

---

## Next.js Configuration

### Key Settings (`next.config.ts`)

```typescript
{
  reactCompiler: true,          // React Compiler is ON
  typedEnv: true,               // Typed process.env
  typedRoutes: true,            // Typed Link href
  cacheComponents: true,        // "use cache" directive enabled
  staleTimes: { dynamic: 30, static: 180 },
  serverExternalPackages: ["postgres", "bcryptjs", "sharp", "nodemailer"],
  serverActions: { bodySizeLimit: "10mb" },
  images: {
    formats: ["image/avif", "image/webp"],
    minimumCacheTTL: 31536000,  // 1 year
    remotePatterns: [
      // MangaDex, Imgur, ImageKit, etc.
    ],
  },
  // Security headers: HSTS, X-Frame-Options, CSP, etc.
}
```

---

## TypeScript & Tooling

### `tsconfig.json` Highlights

- `strict: true`, `target: ES2022`, `module: esnext`
- Path aliases: `@/*` → `./src/*`, plus shortcuts: `@database`, `@env`, `@hooks`, `@lib`, `@schemas`, `@ui`
- Next.js plugin enabled, incremental builds

### ESLint (Flat Config — `eslint.config.mts`)

- Extends `next/core-web-vitals`, `next/typescript`
- Plugins: `prettier`, `better-tailwindcss`, `playwright`, `vitest`, `drizzle`, `zod`
- **Active rules:**
  - `no-explicit-any: "error"`
  - `no-unused-vars` (ignores `^_` prefix)
  - `no-import-type-side-effects`

### Vitest (`vitest.config.mts`)

- Environment: `jsdom`
- Setup: `src/tests/setup-env.ts`
- Include: `src/**/*.test.{ts,tsx}`
- Exclude: `.references/`, `tests/e2e/`, `node_modules/`

### VSCode Configuration

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.tabSize": 2,
  "eslint.useFlatConfig": true,
  "explorer.fileNesting.enabled": true,
  "explorer.fileNesting.patterns": {
    "*.ts": "${capture}.test.ts, ${capture}.spec.ts",
    "*.tsx": "${capture}.test.tsx, ${capture}.spec.tsx"
  }
}
```

Recommended extensions: ESLint, Prettier, Tailwind CSS, Next.js Snippets, Vitest Explorer

---

## Project Conventions

### React Compiler is ON

**DO NOT** use `useMemo`, `useCallback`, or `memo()`. The React Compiler handles memoization automatically. Manual memoization will conflict.

### Next.js 16: `searchParams` is a Promise

```typescript
// ✅ CORRECT (Next.js 16)
export default async function Page({
  searchParams
}: {
  searchParams: Promise<{ page?: string }>;
}) {
  const params = await searchParams;
  const page = params.page;
}

// ❌ WRONG (Next.js 15 pattern)
export default function Page({
  searchParams
}: {
  searchParams: { page?: string };
}) {
  const page = searchParams.page;
}
```

### SSR-Safe Date Handling

```typescript
// ❌ WRONG in Server Component or shared code
const year = new Date().getFullYear();

// ✅ CORRECT — use SSR-safe hook
("use client");
import { useCurrentYear } from "@/hooks/use-now";
const year = useCurrentYear(); // null during SSR, number after hydration
```

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

### Force-Dynamic Ban

Never use `export const dynamic = "force-dynamic"`. Use `<Suspense>` boundaries or small `"use client"` wrappers instead.

### Tailwind Conventions

- Container queries: `@container/card`, `@[540px]/card:hidden`
- Important modifier: `h-4!` (NOT `!h-4`)
- Class ordering follows Tailwind Merge conventions

### Field Naming Gotchas

| Table    | Field               | ✅ Correct | ❌ Wrong |
| -------- | ------------------- | ---------- | -------- |
| `rating` | User's rating (1-5) | `rating`   | `score`  |
| `comic`  | Aggregate rating    | `rating`   | `score`  |

---

## Common Tasks Workflow

### Add a New Page

1. Create `src/app/(root)/my-feature/page.tsx` (Server Component by default)
2. Fetch data via DAL: `const data = await myDal.list()`
3. Create `loading.tsx` and `error.tsx` in same directory
4. Add navigation link in `src/components/layout/app-sidebar.tsx`
5. Add metadata: `export const metadata = { title: "..." }`

### Add a New Database Table

1. Define in `src/database/schema.ts` with proper FKs (`onDelete: "cascade"`)
2. Add `relations()` if needed for complex relationships
3. Run `pnpm db:push` (dev) or generate migrations (prod)
4. Create DAL: `src/dal/my-table-dal.ts` extending `BaseDal<typeof myTable.$inferSelect>`
5. Create Zod schema: `src/schemas/my-table.schema.ts`
6. Create Server Actions: `src/actions/my-table.actions.ts`

### Protect a Page with Authentication

```typescript
import { auth } from "@/auth";
import { redirect } from "next/navigation";

export default async function ProtectedPage() {
  const session = await auth();
  if (!session?.user) redirect("/auth/signin");

  // Check role
  const isAdmin = session.user.role === "admin";

  return <div>Protected content</div>;
}
```

### Create a Server Action

1. Create `src/actions/my-feature.actions.ts` with `"use server"` directive
2. Check `auth()` → validate with Zod → call DAL → `revalidatePath()` → return `ActionResult<T>`
3. Never throw — always return `{ ok: false, error }`

### Create a Client Component

1. Add `"use client"` at file top
2. Use hooks: `useState`, `useEffect`, event handlers, browser APIs
3. DO NOT use `useMemo`/`useCallback`/`memo` — React Compiler handles this
4. Use `useCurrentYear()` instead of `new Date()` for SSR safety

---

## Testing Standards

### Unit Tests (Vitest)

```bash
pnpm test           # Run all
pnpm test --watch   # Watch mode
pnpm test:coverage  # Coverage report
```

- Files: `src/**/*.test.{ts,tsx}`
- Environment: `jsdom` with setup at `src/tests/setup-env.ts`
- Mock external deps (database, auth)
- Test behavior, not implementation
- Use `describe` / `it` blocks

### E2E Tests (Playwright)

```bash
pnpm test:ui        # Run E2E tests
pnpm test:ui --ui   # UI mode
```

- Page Object pattern
- Fixtures for test data
- Cross-browser testing

### Pre-PR Checklist

```bash
pnpm type-check     # 0 TypeScript errors
pnpm lint:fix       # 0 ESLint errors
pnpm test           # All unit tests pass
pnpm build          # Production build succeeds
```

---

## Performance Guidelines

### React Performance

- ✅ Component optimization: React Compiler handles memoization
- ✅ Hook dependencies: Properly manage useEffect and useMemo dependencies
- ✅ State management: Keep state minimal and localized
- ✅ Code splitting: Use dynamic imports for route-based splitting

### Next.js Performance

- ✅ Image optimization: Use next/image with proper sizing
- ✅ Font loading: Use next/font for optimized fonts
- ✅ Static generation: Prefer static generation over SSR
- ✅ Bundle optimization: Use optimizePackageImports in next.config
- ✅ Caching: Use appropriate cache headers and strategies

### Database Performance

- ✅ Query optimization: Use database indexes effectively
- ✅ Connection pooling: Implement proper connection management
- ✅ Data fetching: Use `.with()` to prevent N+1 queries
- ✅ Pagination: Implement efficient pagination for large datasets

### Core Web Vitals Targets

| Metric | Target  | Status |
| ------ | ------- | ------ |
| LCP    | < 2.5s  | 🟡     |
| FID    | < 100ms | ✅     |
| CLS    | < 0.1   | ✅     |

---

## Security Standards

### Authentication & Authorization

- ✅ NextAuth with database sessions
- ✅ Password hashing via bcryptjs
- ✅ Role-based access control (RBAC)
- ✅ Protected routes via `auth()` check

### Input Validation

- ✅ Zod schemas for all user input
- ✅ Validation on both client AND server
- ✅ Type guards for runtime narrowing

### Database Security

- ✅ Parameterized queries (Drizzle)
- ✅ Never string-concatenate SQL
- ✅ Soft deletes where needed
- ✅ Cascade deletes on related records

### Error Handling

- ✅ Avoid exposing sensitive information
- ✅ No stack traces in production
- ✅ Secure error messages
- ✅ Proper logging without sensitive data

### Data Protection

- ✅ HTTPS enforcement
- ✅ CSRF protection
- ✅ XSS prevention via escaping
- ✅ Rate limiting for APIs
- ✅ No sensitive data in localStorage

---

## Deployment Checklist

### Pre-Deployment

- [ ] `pnpm type-check` returns 0 errors
- [ ] `pnpm lint:fix` passes with 0 errors
- [ ] `pnpm test` passes with 80%+ coverage
- [ ] `pnpm build` succeeds without warnings
- [ ] All environment variables configured
- [ ] Database migrations applied
- [ ] Seed data loaded (optional)
- [ ] Error tracking enabled (Sentry)

### Production Build

```bash
pnpm build          # Full production build
pnpm start          # Production server
```

### Vercel Deployment

```bash
git push origin main
# Automatically deploys to Vercel
# Database migrations run automatically
# Environment variables auto-configured
```

---

## Technical Debt & Known Issues

| Issue | Impact | File | Fix |
| --- | --- | --- | --- |
| `/admin` routes unguarded | Security gap | `src/proxy.ts` | Add admin check to middleware |
| Cookie check for auth | May not align with NextAuth | `src/proxy.ts` | Use NextAuth session instead |
| `comment.parentId` no FK ref | Can't use `.with()` for threading | `src/database/schema.ts` | Add `.references()` + `relations()` |
| No `relations()` in schema | Limited to FK-inferred relations | `src/database/schema.ts` | Add explicit `relations()` definitions |
| ~60 commented env stubs | Only 6 fields actively validated | `src/lib/env.ts` | Uncomment and validate as needed |
| `performance.instructions.md` outdated | Conflicts with React Compiler | `.github/instructions/` | Update to remove memo/useMemo rules |

---

## Implementation Phases

### Phase 1: Foundation Setup (2-3 hours)

- [ ] Environment configuration (`.env.local`)
- [ ] Database setup (PostgreSQL or Neon)
- [ ] `pnpm install` and dependencies
- [ ] TypeScript validation (`pnpm type-check`)
- [ ] ESLint validation (`pnpm lint:fix`)
- [ ] Dev server startup (`pnpm dev`)

**Success:** `pnpm type-check` and `pnpm build` both succeed

### Phase 2: Core Features (4-6 hours)

- [ ] Authentication system (sign-in, sign-up)
- [ ] User profile page
- [ ] Comic listing with filters
- [ ] Comic detail page
- [ ] Bookmark management

**Success:** All user-facing flows functional

### Phase 3: Advanced Features (6-8 hours)

- [ ] Chapter reader with progress tracking
- [ ] Rating system
- [ ] Comments & discussion
- [ ] Search functionality
- [ ] Admin dashboard

**Success:** 80%+ feature coverage

### Phase 4: Quality Assurance (3-4 hours)

- [ ] Unit tests (80%+ coverage)
- [ ] E2E tests (critical paths)
- [ ] Performance optimization
- [ ] Security audit
- [ ] Accessibility checks

**Success:** All quality gates passing

### Phase 5: Deployment (1-2 hours)

- [ ] CI/CD pipeline configuration
- [ ] Production build verification
- [ ] Database backup setup
- [ ] Error tracking (Sentry)
- [ ] Monitoring & alerts
- [ ] Final deployment to Vercel

**Success:** Production deployment live with zero downtime

---

## 22. Reference Code Patterns

Production-quality implementations from project references for logging, search, batch processing, and validation.

### 22.1 Enhanced Logger (Pino)

```typescript
import pino from "pino";

const logger = pino({
  level: process.env.LOG_LEVEL || "info",
  transport:
    process.env.NODE_ENV === "development"
      ? {
          target: "pino-pretty",
          options: { colorize: true, translateTime: "SYS:HH:MM:ss" }
        }
      : undefined
});

// Context-specific child loggers
export const dbLogger = logger.child({ context: "database" });
export const authLogger = logger.child({ context: "auth" });
export const apiLogger = logger.child({ context: "api" });
export const seedLogger = logger.child({ context: "seed" });
export const cacheLogger = logger.child({ context: "cache" });

export default logger;
```

### 22.2 Batch Processor (Chunked Concurrency)

```typescript
export function chunkArray<T>(array: T[], chunkSize: number): T[][] {
  const chunks: T[][] = [];
  for (let i = 0; i < array.length; i += chunkSize) {
    chunks.push(array.slice(i, i + chunkSize));
  }
  return chunks;
}

export async function processInBatches<T, R>(
  items: T[],
  batchSize: number,
  processor: (item: T) => Promise<R>
): Promise<PromiseSettledResult<R>[]> {
  const chunks = chunkArray(items, batchSize);
  const results: PromiseSettledResult<R>[] = [];
  for (const chunk of chunks) {
    const batchResults = await Promise.allSettled(
      chunk.map(processor)
    );
    results.push(...batchResults);
  }
  return results;
}
```

### 22.3 Image Validator

```typescript
interface ImageValidationResult {
  isValid: boolean;
  url: string;
  mimeType?: string;
  width?: number;
  height?: number;
  sizeBytes?: number;
  error?: string;
}

const SUPPORTED_MIME_TYPES = [
  "image/jpeg",
  "image/png",
  "image/webp",
  "image/avif"
];
const MAX_IMAGE_SIZE = 10 * 1024 * 1024; // 10 MB

export async function validateImage(
  url: string
): Promise<ImageValidationResult> {
  try {
    const response = await fetch(url, { method: "HEAD" });
    if (!response.ok)
      return {
        isValid: false,
        url,
        error: `HTTP ${response.status}`
      };

    const contentType = response.headers.get("content-type") ?? "";
    const contentLength = parseInt(
      response.headers.get("content-length") ?? "0",
      10
    );

    if (!SUPPORTED_MIME_TYPES.some(t => contentType.includes(t))) {
      return {
        isValid: false,
        url,
        error: `Unsupported type: ${contentType}`
      };
    }
    if (contentLength > MAX_IMAGE_SIZE) {
      return {
        isValid: false,
        url,
        error: `Too large: ${contentLength} bytes`
      };
    }
    return {
      isValid: true,
      url,
      mimeType: contentType,
      sizeBytes: contentLength
    };
  } catch (error) {
    return { isValid: false, url, error: String(error) };
  }
}
```

### 22.4 Full-Text Search Service

```typescript
import { db } from "@/database/db";
import { comic, author, genre, comicGenre } from "@/database/schema";
import {
  ilike,
  eq,
  and,
  gte,
  lte,
  inArray,
  sql,
  desc,
  asc
} from "drizzle-orm";

interface SearchOptions {
  query?: string;
  genres?: number[];
  authorId?: number;
  status?: string;
  minRating?: number;
  sortBy?: "title" | "rating" | "latest" | "popular";
  page?: number;
  limit?: number;
}

export async function searchComics(options: SearchOptions) {
  const {
    query,
    genres,
    authorId,
    status,
    minRating,
    sortBy = "latest",
    page = 1,
    limit = 20
  } = options;
  const conditions = [];

  if (query) conditions.push(ilike(comic.title, `%${query}%`));
  if (authorId) conditions.push(eq(comic.authorId, authorId));
  if (status) conditions.push(eq(comic.status, status));
  if (minRating) conditions.push(gte(comic.averageRating, minRating));

  const orderBy = {
    title: asc(comic.title),
    rating: desc(comic.averageRating),
    latest: desc(comic.createdAt),
    popular: desc(comic.viewCount)
  }[sortBy];

  const offset = (page - 1) * limit;
  const where =
    conditions.length > 0 ? and(...conditions) : undefined;

  const [results, [{ total }]] = await Promise.all([
    db.query.comic.findMany({
      where,
      orderBy: [orderBy],
      limit,
      offset,
      with: { author: true, type: true }
    }),
    db
      .select({ total: sql<number>`count(*)` })
      .from(comic)
      .where(where)
  ]);

  return {
    results,
    total,
    page,
    totalPages: Math.ceil(total / limit)
  };
}
```

### 22.5 DAL Compliance Verification Script

```typescript
// scripts/verify-dal-usage.ts — Run: npx tsx scripts/verify-dal-usage.ts
import { readFileSync, readdirSync, statSync } from "fs";
import { join } from "path";

const VIOLATIONS_PATTERNS = [
  /db\.query\./, // Direct db.query usage
  /db\.select\(/, // Direct db.select usage
  /db\.insert\(/, // Direct db.insert usage
  /db\.update\(/, // Direct db.update usage
  /db\.delete\(/ // Direct db.delete usage
];

function scanFile(filePath: string): string[] {
  const content = readFileSync(filePath, "utf-8");
  const violations: string[] = [];
  const lines = content.split("\n");

  lines.forEach((line, index) => {
    for (const pattern of VIOLATIONS_PATTERNS) {
      if (pattern.test(line) && !filePath.includes("/dal/")) {
        violations.push(`${filePath}:${index + 1} — ${line.trim()}`);
      }
    }
  });
  return violations;
}

// Scan src/actions/ for direct DB access (should use DAL instead)
const actionsDir = join(process.cwd(), "src/actions");
// ... recursively scan and report violations
```

### 22.6 Seed Data Transfer Objects (Zod)

```typescript
import { z } from "zod";

export const userSeedSchema = z.object({
  username: z.string().min(3).max(50),
  email: z.string().email(),
  password: z.string().min(8),
  name: z.string().optional(),
  role: z.enum(["user", "moderator", "admin"]).default("user"),
  image: z.string().url().optional()
});

export const comicSeedSchema = z.object({
  title: z.string().min(1).max(200),
  slug: z.string().min(1).max(200),
  synopsis: z.string().optional(),
  status: z
    .enum(["ongoing", "completed", "hiatus", "cancelled"])
    .default("ongoing"),
  coverImage: z.string().url().optional(),
  authorName: z.string().min(1),
  typeName: z.string().min(1),
  genreNames: z.array(z.string()).default([])
});

export const chapterSeedSchema = z.object({
  comicSlug: z.string().min(1),
  chapterNumber: z.number().positive(),
  title: z.string().optional(),
  content: z.string().optional(),
  pageCount: z.number().positive().default(1),
  images: z.array(z.string().url()).default([])
});

export type UserSeed = z.infer<typeof userSeedSchema>;
export type ComicSeed = z.infer<typeof comicSeedSchema>;
export type ChapterSeed = z.infer<typeof chapterSeedSchema>;
```

---

## 23. Feature Implementation Patterns

Complete code samples for common features following ComicWise architecture.

### 23.1 Rating System (Composite Key + Aggregates)

**Schema:**

```typescript
export const rating = pgTable(
  "rating",
  {
    userId: text("userId")
      .notNull()
      .references(() => user.id, { onDelete: "cascade" }),
    comicId: integer("comicId")
      .notNull()
      .references(() => comic.id, { onDelete: "cascade" }),
    score: integer("score").notNull().$type<1 | 2 | 3 | 4 | 5>(),
    reviewText: text("reviewText"),
    isRecommended: boolean("isRecommended").default(false),
    isSpoiler: boolean("isSpoiler").default(false),
    helpfulCount: integer("helpfulCount").default(0),
    createdAt: timestamp("createdAt").defaultNow().notNull(),
    updatedAt: timestamp("updatedAt").defaultNow().notNull()
  },
  table => [primaryKey({ columns: [table.userId, table.comicId] })]
);
```

**DAL (Single-Query Aggregate):**

```typescript
async getComicRatingStats(comicId: number) {
  const stats = await db
    .select({
      averageRating: avg(rating.score),
      ratingCount: count(rating.userId),
    })
    .from(rating)
    .where(eq(rating.comicId, comicId));
  return stats[0];
}
```

### 23.2 Reading Progress (Idempotent Upsert)

**Schema:**

```typescript
export const readingProgress = pgTable(
  "readingProgress",
  {
    userId: text("userId")
      .notNull()
      .references(() => user.id),
    comicId: integer("comicId")
      .notNull()
      .references(() => comic.id),
    currentChapterId: integer("currentChapterId").references(
      () => chapter.id
    ),
    currentPageNumber: integer("currentPageNumber").default(0),
    progressPercent: decimal("progressPercent", {
      precision: 5,
      scale: 2
    }),
    lastReadAt: timestamp("lastReadAt"),
    status: text("status").default("Reading"),
    createdAt: timestamp("createdAt").defaultNow().notNull()
  },
  table => [
    primaryKey({
      columns: [table.userId, table.comicId],
      name: "readingProgress_pk"
    }),
    index("readingProgress_user_lastRead_idx").on(
      table.userId,
      table.lastReadAt
    )
  ]
);
```

**DAL (Idempotent Upsert):**

```typescript
async updateProgress(data: UpdateProgressInput) {
  const [result] = await db
    .insert(readingProgress)
    .values({
      userId: data.userId,
      comicId: data.comicId,
      currentChapterId: data.currentChapterId,
      lastReadAt: new Date(),
    })
    .onConflictDoUpdate({
      target: [readingProgress.userId, readingProgress.comicId],
      set: { currentChapterId: data.currentChapterId, lastReadAt: new Date() },
    })
    .returning();
  return result;
}
```

**"Continue Reading" Query (Single JOIN):**

```typescript
async getContinueReadingList(userId: string, limit = 10) {
  return db
    .select({
      comicId: readingProgress.comicId,
      comicTitle: comic.title,
      currentChapterId: readingProgress.currentChapterId,
      progressPercent: readingProgress.progressPercent,
      lastReadAt: readingProgress.lastReadAt,
      chapterNumber: chapter.chapterNumber,
    })
    .from(readingProgress)
    .innerJoin(comic, eq(readingProgress.comicId, comic.id))
    .leftJoin(chapter, eq(readingProgress.currentChapterId, chapter.id))
    .where(eq(readingProgress.userId, userId))
    .orderBy(desc(readingProgress.lastReadAt))
    .limit(limit);
}
```

### 23.3 Comic Listing Page (Server/Client Split)

**Server Component:**

```typescript
export default async function ComicsPage({ searchParams }: { searchParams: Promise<Record<string, string>> }) {
  const params = await searchParams;
  const page = parseInt(params.page ?? "1", 10);
  const sort = params.sort ?? "latest";

  return (
    <Suspense fallback={<ComicListSkeleton />}>
      <ComicList page={page} sort={sort} />
    </Suspense>
  );
}
```

**Client Component (URL-driven filters):**

```typescript
"use client";

export function ComicFilters({
  defaultSort
}: {
  defaultSort: string;
}) {
  const router = useRouter();
  const searchParams = useSearchParams();

  const handleFilterChange = (filters: Record<string, string>) => {
    const params = new URLSearchParams(searchParams);
    Object.entries(filters).forEach(([key, value]) =>
      params.set(key, value)
    );
    router.push(`?${params.toString()}`);
  };
  // URL-driven state keeps server and client in sync
}
```

---

## 24. Entity Relationship Diagram & Cascade Rules

### 24.1 ERD Overview

```text
┌───────────────────────────────────────────────┐
│  Type / Author / Artist / Genre (Lookups)     │
└──────────────┬────────────────────────────────┘
               │ FK
               ↓
    ┌──────────────────┐
    │      Comic       │ ← ComicImage (1:N)
    │  (authorId, typeId)│ ← ComicGenre (M:N junction)
    └────────┬─────────┘   ← ComicArtist (M:N junction)
             │ FK
             ↓
    ┌──────────────────┐
    │     Chapter      │ ← ChapterImage (1:N)
    │   (comicId)      │
    └──────────────────┘

USER LAYER:
    User ──→ Bookmark (userId, comicId)          ← composite PK, idempotent
         ──→ Comment (userId, chapterId)          ← parentId for threading
         ──→ Rating (userId, comicId)             ← composite PK, one per pair
         ──→ ReadingProgress (userId, comicId)    ← composite PK, upsert
         ──→ Notification (userId)
         ──→ UserRole → Role → RolePermission → Permission  (RBAC)
```

### 24.2 Cascade Delete Rules

| When Deleted | Cascades To |
| --- | --- |
| **User** | account, session, bookmark, comment, rating, readingProgress, notification, userRole |
| **Comic** | chapter → chapterImage, comicImage, comicGenre, comicArtist, bookmark, rating, readingProgress |
| **Chapter** | chapterImage, comment, readingProgress (where currentChapterId) |
| **Role** | rolePermission, userRole |

### 24.3 Key RBAC Query

```sql
-- Get user permissions
SELECT DISTINCT p.resource, p.action
FROM permission p
JOIN rolePermission rp ON p.id = rp.permissionId
JOIN role r ON rp.roleId = r.id
JOIN userRole ur ON r.id = ur.roleId
WHERE ur.userId = ?;
```

---

## 25. Proposed Fixes & Type Error Patterns

### 25.1 Drizzle ORM Type Handling

```typescript
// ❌ Wrong: Drizzle returns null, but TypeScript expects undefined
const user = result[0]; // { name: null } but type expects { name?: string }

// ✅ Fix: Map null → undefined for external types
function mapUser(dbUser: typeof user.$inferSelect): User {
  return {
    ...dbUser,
    name: dbUser.name ?? undefined,
    email: dbUser.email ?? undefined,
    image: dbUser.image ?? undefined
  };
}
```

### 25.2 Unknown Payload Type Guards (Recharts)

```typescript
// ❌ Wrong: Using `any` for external library payloads
const renderTooltip = (payload: any[]) => { ... };

// ✅ Fix: Use `unknown` + type guard
const renderTooltip = (payload: unknown[]) => {
  const items = payload.filter(
    (item): item is { type: string; value: number; name: string } =>
      typeof item === "object" && item !== null && "type" in item && (item as any).type !== "none"
  );
};
```

### 25.3 Tailwind CSS v4 Class Fixes

| Wrong (v3)                     | Correct (v4)                  |
| ------------------------------ | ----------------------------- |
| `bg-gradient-to-br`            | `bg-linear-to-br`             |
| `aspect-[2/3]`                 | `aspect-2/3`                  |
| `[-moz-appearance:_textfield]` | `[-moz-appearance:textfield]` |
| `start-0`                      | `inset-s-0`                   |

---

## 26. Database Troubleshooting

### Connection Errors

```bash
# Test database connection
psql $DATABASE_URL -c "SELECT 1"

# Open visual database browser
pnpm db:studio
```

**Common causes:** Invalid `DATABASE_URL` in `.env.local`, Neon database sleeping (free tier), network/firewall issues.

### Seed Errors

```bash
# Run with verbose logging for detailed error output
SEED_VERBOSE=true pnpm seed:all

# Validate data without writing to database
pnpm seed --dry-run --verbose
```

**Common causes:** Missing dependencies (seed order matters — types before comics), invalid image URLs, Zod validation failures on transformed data.

### Migration Issues

```bash
# Generate fresh migration from current schema
pnpm db:generate

# Push schema directly to database (dev only, no migration files)
pnpm db:push

# Drop all tables and start fresh (⚠️ DESTRUCTIVE)
pnpm db:drop
```

**Common causes:** Schema drift between local and remote, conflicting migration files, column type changes on existing data.

### Common Entity Operations

When adding a new entity to the system, follow this checklist:

1. Add table to `src/database/schema.ts`
2. Create Zod schema in `src/schemas/{entity}.schema.ts`
3. Create DAL class in `src/dal/{entity}-dal.ts` (extends `BaseDal<T>`)
4. Create server actions in `src/actions/{entity}.actions.ts`
5. Run `pnpm db:push` to apply schema
6. Run `pnpm type-check` to verify types

### Adding Database Indexes

```typescript
// In schema.ts — index frequently queried columns
export const comicSlugIndex = index("comic_slug_idx").on(comic.slug);
export const bookmarkUserIndex = index("bookmark_user_idx").on(
  bookmark.userId
);
```

---

**Document Version:** 2.0 **Last Updated:** March 2026 **Maintained By:** GitHub Copilot / Expert Next.js Developer **Sections:** 26 (expanded from 21 with reference patterns, feature implementations, ERD, fixes, and database troubleshooting)
