# Database Migration Guide

**Purpose:** Complete guide to database setup, migrations, and management for ComicWise

**Last Updated:** March 1, 2026 | **Framework:** Next.js 16 | **ORM:** Drizzle | **Database:** PostgreSQL

---

## Quick Start

### For Local Development

```bash
# 1. Set up environment variables
cp .env.local.example .env.local
# Edit .env.local with your DATABASE_URL

# 2. Install dependencies
pnpm install

# 3. Push current schema to database
pnpm db:push

# 4. Verify with Drizzle Studio
pnpm db:studio
```

### For Production Deployment

```bash
# Generate latest migrations
pnpm db:generate

# Review generated migration files in src/database/drizzle/
# Commit all migration files to git

# Apply migrations (on deployment server)
pnpm db:migrate
```

---

## Environment Setup

### Prerequisites

- Node.js 18+ (verify with `node --version`)
- PostgreSQL 13+ (local or cloud)
- pnpm installed (`npm install -g pnpm`)

### Database Connection Options

#### Option 1: Local PostgreSQL

```bash
# .env.local
DATABASE_URL="postgresql://user:password@localhost:5432/comicwise"
```

#### Option 2: Neon (Cloud PostgreSQL)

```bash
# .env.local (Neon PostgreSQL)
DATABASE_URL="postgresql://user:password@ep-xxx.neon.tech/comicwise?sslmode=require"
```

#### Option 3: Supabase (PostgreSQL + Auth)

```bash
# .env.local (Supabase)
DATABASE_URL="postgresql://postgres:your-password@db.xxx.supabase.co:5432/postgres"
```

#### Option 4: Railway (PostgreSQL Hosting)

```bash
# .env.local (Railway)
DATABASE_URL="postgresql://user:password@containers-us-west-xxx.railway.app:5432/railway"
```

### Environment Variable Validation

The project validates `DATABASE_URL` using Zod in `src/lib/env.ts`:

```typescript
// src/lib/env.ts
import { z } from "zod";

const envSchema = z.object({
  DATABASE_URL: z
    .string()
    .url("DATABASE_URL must be a valid database connection URL")
    .refine(
      url => url.includes("postgresql") || url.includes("postgres"),
      "DATABASE_URL must be a PostgreSQL connection string"
    )
  // ... other env vars
});

export const env = envSchema.parse(process.env);
```

---

## Database Commands

### Available Commands

All commands configured in `package.json`:

```bash
pnpm db:check      # Check schema consistency
pnpm db:generate   # Generate migrations for schema changes
pnpm db:migrate    # Apply pending migrations
pnpm db:push       # Push schema directly (dev only, no migrations)
pnpm db:pull       # Introspect existing database
pnpm db:drop       # ⚠️ DROP ALL TABLES (dev/testing only)
pnpm db:reset      # pnpm db:drop && pnpm db:generate && pnpm db:push
pnpm db:studio     # Open interactive Drizzle Studio
```

### Understanding Each Command

| Command | Purpose | Use Case | Safety |
| --- | --- | --- | --- |
| `db:check` | Verify no schema conflicts exist | Before merging PRs | ✅ Read-only |
| `db:generate` | Create migration file for schema changes | Adding new tables/columns | ✅ Safe - creates file only |
| `db:migrate` | Apply generated migrations to database | Production deploys | ⚠️ Warn before running |
| `db:push` | Directly update schema without migrations | Local dev only | ❌ Skip prod changes |
| `db:pull` | Read existing database schema | Syncing with external DB | ✅ Read-only |
| `db:drop` | Delete entire database | Test cleanup | 🔴 DESTRUCTIVE |
| `db:reset` | Drop + regenerate + push | Fresh start (dev) | 🔴 DESTRUCTIVE |
| `db:studio` | Interactive database browser | Exploring/debugging | ✅ Read-only (by default) |

---

## Current Schema Status

### Tables Summary (26 total)

**Authentication (5 tables):**

- `user` - Users with roles (admin, moderator, user)
- `account` - NextAuth OAuth accounts
- `session` - NextAuth sessions
- `authenticator` - WebAuthn authenticators
- `passwordResetToken` - Password reset tokens

**Content Management (8 tables):**

- `comic` - Comic metadata (title, description, status, etc.)
- `chapter` - Chapters per comic with release dates
- `chapterImage` - Pages/images per chapter
- `author` - Comic authors
- `artist` - Comic artists
- `genre` - Comic genres
- `type` - Comic types (manga, manhwa, manhua, etc.)
- `comicImage` - Comic cover images

**User Interactions (6 tables):**

- `bookmark` - User bookmarks (saved comics + status)
- `readingProgress` - Chapters read per user per comic
- `comment` - Comments on chapters (with threading)
- `rating` - User ratings (1-5 stars, optional review)
- `notification` - User notifications
- `readerSettings` - User reader preferences

**Authorization (2 tables):**

- `role` - RBAC roles
- `permission` - RBAC permissions
- `rolePermission` - Role-permission mapping
- `userRole` - User role assignments

**System (5 tables):**

- `auditLog` - Action audit trail
- `verificationToken` - Email verification tokens
- `comicToGenre` - Comic-genre relationship mapping
- `comicGenreRelation` - Many-to-many comic-genre

**Indexes (41 total):**

- Full-text search on comics, authors, artists
- Composite indexes for common queries
- Foreign key indexes for referential integrity

---

## Creating Migrations

### Step 1: Update Schema

Edit `src/database/schema.ts` to add/modify tables:

```typescript
// src/database/schema.ts
import {
  pgTable,
  text,
  integer,
  timestamp
} from "drizzle-orm/pg-core";

// Add new table
export const newFeature = pgTable("newFeature", {
  id: serial("id").primaryKey(),
  name: text("name").notNull(),
  createdAt: timestamp("createdAt").defaultNow().notNull(),
  userId: text("userId")
    .notNull()
    .references(() => user.id, { onDelete: "cascade" })
});
```

**Important Patterns:**

✅ **Always use cascade delete for foreign keys:**

```typescript
.references(() => user.id, { onDelete: "cascade" })
```

✅ **Use timestamps consistently:**

```typescript
createdAt: timestamp("createdAt").defaultNow().notNull(),
updatedAt: timestamp("updatedAt").defaultNow().notNull(),
```

✅ **Use indexes for common queries:**

```typescript
index("newFeature_userId_idx").on(table.userId),
```

### Step 2: Generate Migration

```bash
pnpm db:generate
```

**Output:** New file `src/database/drizzle/0001_xxx_migration_name.sql`

Example generated migration for adding a table:

```sql
-- src/database/drizzle/0001_add_rating_table.sql
CREATE TABLE "rating" (
  "userId" text NOT NULL,
  "comicId" integer NOT NULL,
  "score" integer NOT NULL,
  "reviewText" text,
  "createdAt" timestamp DEFAULT now() NOT NULL,
  "updatedAt" timestamp DEFAULT now() NOT NULL,
  CONSTRAINT "rating_pk" PRIMARY KEY("userId","comicId")
);
--> statement-breakpoint
CREATE INDEX "rating_userId_idx" on "rating" ("userId");
--> statement-breakpoint
CREATE INDEX "rating_comicId_idx" on "rating" ("comicId");
--> statement-breakpoint
ALTER TABLE "rating" ADD CONSTRAINT "rating_userId_fk" FOREIGN KEY ("userId") REFERENCES "user"("id") ON DELETE cascade;
--> statement-breakpoint
ALTER TABLE "rating" ADD CONSTRAINT "rating_comicId_fk" FOREIGN KEY ("comicId") REFERENCES "comic"("id") ON DELETE cascade;
```

### Step 3: Review Migration

```bash
# Open generated migration file
code src/database/drizzle/0001_add_rating_table.sql

# Verify:
# ✅ Column types are correct
# ✅ Foreign keys have ON DELETE CASCADE
# ✅ Indexes are on frequently-queried fields
# ✅ Default values make sense (now(), true, etc.)
```

### Step 4: Apply Migration

**For Local Development:**

```bash
# Push directly (no separate migration file needed)
pnpm db:push
```

**For Production:**

```bash
# 1. Commit migration file to git
git add src/database/drizzle/0001_add_rating_table.sql
git commit -m "feat: add rating table for comic reviews"

# 2. Deploy code to production server

# 3. Run migration
pnpm db:migrate
```

---

## Common Migration Scenarios

### Scenario 1: Add New Column to Existing Table

**Schema change:**

```typescript
// src/database/schema.ts - in comic table
englishTitle: text("englishTitle"), // Add new column
```

**Generate and apply:**

```bash
pnpm db:generate  # Creates: 0001_add_english_title_to_comic.sql
pnpm db:push      # Applies locally
```

**Generated SQL:**

```sql
ALTER TABLE "comic" ADD COLUMN "englishTitle" text;
```

### Scenario 2: Add Foreign Key Constraint

**Schema change:**

```typescript
// src/database/schema.ts
moderatorId: text("moderatorId")
  .references(() => user.id, { onDelete: "set null" }),
```

**Generate and apply:**

```bash
pnpm db:generate  # Creates: 0001_add_moderator_constraint.sql
pnpm db:push
```

**Generated SQL:**

```sql
ALTER TABLE "comment" ADD CONSTRAINT "comment_moderatorId_fk"
FOREIGN KEY ("moderatorId") REFERENCES "user"("id") ON DELETE set null;
```

### Scenario 3: Create Index for Performance

**Schema change:**

```typescript
// src/database/schema.ts
index("chapter_releaseDate_idx").on(table.releaseDate),
```

**Generate and apply:**

```bash
pnpm db:generate  # Creates: 0001_add_chapter_release_index.sql
pnpm db:push
```

### Scenario 4: Rename Column

**Drizzle doesn't auto-detect renames - must write custom SQL:**

```bash
# 1. Create migration file manually
# src/database/drizzle/0001_rename_column.sql
ALTER TABLE "comic" RENAME COLUMN "publishDate" TO "releaseDate";

# 2. Update schema in src/database/schema.ts:
releaseDate: timestamp("releaseDate"),

# 3. Apply:
pnpm db:migrate
```

### Scenario 5: Drop Cascade Effect

**When deleting a comic, what happens?**

Based on schema cascade rules:

```text
Comic deleted →
  ├─ Chapters deleted (comicId FK with CASCADE)
  │  ├─ ChapterImages deleted (chapterId FK with CASCADE)
  │  └─ Comments deleted (chapterId FK with CASCADE)
  ├─ Bookmarks deleted (comicId FK with CASCADE)
  ├─ Ratings deleted (comicId FK with CASCADE)
  ├─ ReadingProgress deleted (comicId FK with CASCADE)
  └─ ComicImages deleted (comicId FK with CASCADE)
```

**Verify with:**

```bash
pnpm db:check  # Shows potential cascade issues
```

---

## Testing Migrations

### Unit Test Pattern

**File:** `src/tests/migrations.spec.ts`

```typescript
import { describe, it, expect } from "vitest";
import { db } from "@/database/db";
import { sql } from "drizzle-orm";

describe("Database Migrations", () => {
  it("has rating table with correct schema", async () => {
    // Query information schema to verify table exists
    const result = await db.execute(sql`
      SELECT column_name, data_type 
      FROM information_schema.columns 
      WHERE table_name = 'rating'
    `);

    expect(result).toContainEqual(
      expect.objectContaining({
        column_name: "score",
        data_type: "integer"
      })
    );
  });

  it("enforces foreign key constraints", async () => {
    // Attempt to insert with invalid userId should fail
    const invalidInsert = db.insert(rating).values({
      userId: "nonexistent-user",
      comicId: 1,
      score: 5
    });

    expect(invalidInsert).rejects.toThrow(/foreign key/i);
  });
});
```

---

## Troubleshooting

### Problem: "DATABASE_URL is not defined"

**Solution:**

```bash
# Create .env.local with valid DATABASE_URL
echo 'DATABASE_URL="postgresql://user:password@localhost:5432/comicwise"' > .env.local

# Verify it loads
pnpm db:check
```

### Problem: "no changes detected" on db:generate

**Cause:** Schema matches database

**Solution:**

```bash
# Verify schema file is correct
cat src/database/schema.ts

# If changes were made, ensure file is saved
# Then retry:
pnpm db:generate
```

### Problem: Migration fails with "permission denied"

**Cause:** Database user lacks permissions

**Solution:**

```sql
-- Run as postgres superuser:
ALTER USER myuser CREATEDB;
ALTER USER myuser SUPERUSER;

-- Or grant specific table permissions:
GRANT ALL PRIVILEGES ON DATABASE comicwise TO myuser;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO myuser;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO myuser;
```

### Problem: Can't connect to Neon/Supabase database

**Solution:**

```bash
# Verify connection string includes ?sslmode=require for cloud DBs
DATABASE_URL="postgresql://user:pass@host.neon.tech/db?sslmode=require"

# Test connection
pnpm db:check
```

### Problem: Cascade delete has unwanted effects

**Solution:** Use `SET NULL` or `RESTRICT` instead:

```typescript
// Change from CASCADE to SET NULL
moderatorId: text("moderatorId")
  .references(() => user.id, { onDelete: "set null" }), // User deleted → moderatorId = NULL

// Or RESTRICT (prevent deletion)
required: integer("required")
  .references(() => requiredTable.id, { onDelete: "restrict" }), // Prevent deletion if referenced
```

---

## Development Workflow

### Adding a New Feature (e.g., Comic Ratings)

**Step 1: Update schema** (30 seconds)

```typescript
// src/database/schema.ts
export const rating = pgTable("rating", {
  userId: text("userId")
    .notNull()
    .references(() => user.id, { onDelete: "cascade" }),
  comicId: integer("comicId")
    .notNull()
    .references(() => comic.id, { onDelete: "cascade" }),
  score: integer("score").notNull()
  // ... more fields
});
```

**Step 2: Generate migration** (5 seconds)

```bash
pnpm db:generate  # Creates 0001_add_rating_table.sql
```

**Step 3: Apply to local DB** (2 seconds)

```bash
pnpm db:push
```

**Step 4: Verify in Drizzle Studio** (30 seconds)

```bash
pnpm db:studio  # Open browser, check table exists with correct columns
```

**Step 5: Create DAL, schemas, components** (hours) Follow [example-feature-implementation.md](./example-feature-implementation.md)

**Step 6: Test migrations** (30 seconds)

```bash
pnpm test  # Unit tests verify schema
```

**Step 7: Commit** (30 seconds)

```bash
git add src/database/schema.ts src/database/drizzle/0001_add_rating_table.sql
git commit -m "feat: add rating table and migration"
```

---

## Production Deployment

### Pre-Deployment Checklist

- [ ] All migrations generated: `pnpm db:generate`
- [ ] No schema conflicts: `pnpm db:check`
- [ ] Migrations committed to git
- [ ] Database credentials provided to deployment platform
- [ ] Backup scheduled before deployment
- [ ] Rollback plan documented

### Deployment Process

**1. On development machine:**

```bash
# Ensure schema is finalized
pnpm db:check

# Generate any pending migrations
pnpm db:generate

# Commit to git
git add -A
git commit -m "feat: database changes for new feature"
git push origin feature/new-feature
```

**2. On deployment server (during CI/CD):**

```bash
# Install dependencies
pnpm install --frozen-lockfile

# Apply pending migrations
pnpm db:migrate

# Verify application starts
pnpm build
pnpm start
```

### Rollback Procedure

**If migration fails in production:**

```bash
# 1. Immediately revert to previous code version
git revert <commit-hash>
cd deployment-server
pnpm install

# 2. Do NOT run db:migrate (downgrade not automated)
# 3. Contact DBA to restore database backup
# 4. Restart application with reverted code
pnpm start

# 5. Investigation & Fix
# On dev machine:
pnpm db:check  # Verify no schema conflicts
# Fix schema issues
pnpm db:generate  # Create corrected migration
git commit -m "fix: correct migration issues"

# 6. Re-deploy with verified migration
```

---

## Migration History

### Current Schema Version

**Last Generated:** March 1, 2026  
**Total Tables:** 26  
**Total Migrations:** 1 (initial schema)  
**Status:** All migrations applied ✅

**Migration Log:**

| Migration | Date | Tables Added | Changes |
| --- | --- | --- | --- |
| `0000_sparkling_moonstone.sql` | Mar 1, 2026 | 26 | Initial schema: auth, content, interactions, RBAC |

---

## References

- [Drizzle Documentation](https://orm.drizzle.team)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Database Context Map](./database-context-map.md)
- [Example Feature Implementation](./example-feature-implementation.md)

---

**Version:** 1.0.0 | **Updated:** March 1, 2026 | **Framework:** Next.js 16 | **ORM:** Drizzle
