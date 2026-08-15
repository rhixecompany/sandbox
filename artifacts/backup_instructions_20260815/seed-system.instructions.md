---
applyTo: "src/scripts/seed/**/*.ts"
description: "Seed system design patterns, architecture conventions, and implementation standards"
---

# Seed System Instructions

ComicWise uses a **Template Method Pattern** for seeding all database entities. All seeders extend `BaseSeeder<T>` and follow strict conventions for deduplication, type safety, and idempotent operations.

## Core Architecture

### Template Method Pattern

Every seeder must extend `BaseSeeder<T>` and implement the template method flow:

```
seed() → loadData() → validateData() → processBatches() → insertBatch() → EntityResult
```

**Required abstract methods:**

```typescript
export class MySeeder extends BaseSeeder<MyType> {
  // Return array of data source identifiers (JSON file names without .json)
  protected getDataSources(): string[] {
    return ["my-data"];
  }

  // Return the unique field name for deduplication cache lookups
  protected getUniqueField(): string {
    return "email"; // or "slug", "name", etc.
  }

  // Transform raw data into validated shape (Zod coercion, field mapping)
  protected async transformData(raw: MyType): Promise<unknown> {
    return { ...raw, createdAt: new Date() };
  }

  // Perform actual database insertion with conflict handling
  async insertBatch(data: MyType[]): Promise<EntityResult> {
    // Use onConflictDoNothing() or onConflictDoUpdate()
    // Return EntityResult with accurate counts
  }
}
```

## Key Patterns

### 1. LookupCache Discipline

**Every seeder must:**

- Read from `this.cache` before inserting (check for duplicates across dependencies)
- Write to `this.cache` immediately after successful insert/update
- Use the unique field as the cache key

```typescript
// Check cache first
const cached = this.cache.users.get(raw.email);
if (cached) {
  skipped++;
  return cached; // Use cached ID for relations
}

// Insert new entity
const result = await db.insert(user).values({...}).returning();

// Write to cache immediately after insert
if (result.length > 0) {
  inserted++;
  this.cache.users.set(raw.email, result[0].id);
}
```

### 2. Counter Accuracy

**Golden rule:** Counters must reflect actual database operations, not conditional checks.

```typescript
let inserted = 0;
let skipped = 0;
const errors: SeedError[] = [];

if (existing) {
  // Entity already exists in DB
  skipped++;  // NOT updated++ (unless you actually changed something)
  this.cache.types.set(item.name, existing.id); // Still add to cache!
} else {
  // New entity being inserted
  const result = await db.insert(...).returning();
  if (result.length > 0) {
    inserted++;
    this.cache.types.set(item.name, result[0].id);
  }
}

// Return accurate counts
return {
  entityName: this.entityName,
  inserted,
  updated: 0,  // Only increment if you do partial updates (rare)
  skipped,
  errors,
  duration,
  success: errors.length === 0,
};
```

**Never hardcode zero counts**:

```typescript
// ❌ Bad: hardcoded skipped: 0
return { ..., skipped: 0, ... };

// ✅ Good: use actual variable
return { ..., skipped, ... };
```

### 3. Idempotent Seeding

All seeders must support **re-running without duplication**. Use Drizzle's conflict handlers:

```typescript
// For unique constraints
await db.insert(comicImage).values(data).onConflictDoNothing(); // Don't fail if duplicate

// For composite unique constraints
await db
  .insert(chapterImage)
  .values(data)
  .onConflictDoNothing({
    target: [chapterImage.chapterId, chapterImage.pageNumber]
  });

// For updates if needed (rare)
await db
  .insert(type)
  .values({ name, description })
  .onConflictDoUpdate({
    target: type.name,
    set: { description }
  });
```

### 4. Password Hashing (Security)

When seeding users, **always use bcryptjs** with consistent salt rounds:

```typescript
import bcrypt from "bcryptjs";

const BCRYPT_SALT_ROUNDS = 10; // Project standard (don't change)

// Hash password before inserting
const hash = await bcrypt.hash(raw.password, BCRYPT_SALT_ROUNDS);

// Insert with hashed password
await db.insert(user).values({
  ...userFields,
  password: hash
});
```

**Never hardcode rounds inline** — use the constant.

### 5. Relation Resolution

Seeders must resolve foreign keys from `LookupCache` before inserting:

```typescript
// Resolve author ID from cache (populated by earlier seeder)
const authorId = this.cache.authors.get(raw.authorName);
if (!authorId) {
  errors.push({
    itemIndex: i,
    message: `Author "${raw.authorName}" not found in cache`,
    value: raw
  });
  continue;
}

// Use resolved ID in insert
await db.insert(comic).values({
  ...comicFields,
  authorId // Foreign key from cache
});
```

### 6. Utility Extraction

**Never duplicate utility functions** across seeders. Extract to `src/scripts/seed/helpers/`:

```typescript
// ❌ Bad: stripHtmlTags defined in multiple seeders
function stripHtmlTags(html: string): string {
  return html.replaceAll(/<[^>]*>/g, "");
}

// ✅ Good: extract to helpers
// src/scripts/seed/helpers/html-utils.ts
export function stripHtmlTags(html: string): string {
  return html.replaceAll(/<[^>]*>/g, "");
}

// Then import in seeders
import { stripHtmlTags } from "../helpers/html-utils";
```

## Integration Checklist

When creating a new seeder, update **all** of these:

### 1. Seeder Class (`src/scripts/seed/seeders/my-seeder.ts`)

- [ ] Extends `BaseSeeder<T>` with correct type
- [ ] Implements all 4 abstract methods
- [ ] Uses `LookupCache` for reads and writes
- [ ] Accurate counter increments
- [ ] Error handling with `errors` array
- [ ] Returns complete `EntityResult`

### 2. Types (`src/scripts/seed/types.ts`)

- [ ] Add entity key to `LookupCache` interface if new entity (e.g., `users: Map<string, string>`)
- [ ] Add entity name to `SeedConfig["entities"]` union type (alphabetically)

### 3. Exports (`src/scripts/seed/index.ts`)

- [ ] Export the seeder class: `export { MySeeder } from "./seeders/my-seeder"`

### 4. Orchestrator (`src/scripts/seed/seed-orchestrator.ts`)

- [ ] Import the seeder: `import { MySeeder } from "./seeders/my-seeder"`
- [ ] Add entity to `initializeCache()` if new cache needed (e.g., `users: new Map()`)
- [ ] Add entity to `entityOrder` array in **dependency order** (dependencies come first)
- [ ] Add `case "my-entity"` in switch statement with proper instantiation
- [ ] Update `entitiesToSeed` filter type assertion to include new entity name

### 5. Schema (`src/schemas/seed/my.seed.ts`)

- [ ] Define Zod schema for single item: `const mySeedItemSchema = z.object({...})`
- [ ] Export inferred type: `export type MySeedItem = z.infer<typeof mySeedItemSchema>`

## Entity Dependency Order

**Critical:** Seeders must run in dependency order. Update `seed-orchestrator.ts` `entityOrder`:

```typescript
const entityOrder = [
  "users", // No dependencies
  "types", // No dependencies
  "authors", // No dependencies
  "artists", // No dependencies
  "genres", // No dependencies
  "comics", // Depends on: authors, artists, types, genres
  "comic-images", // Depends on: comics
  "chapters", // Depends on: comics
  "chapter-images" // Depends on: chapters
];
```

## Common Issues & Fixes

### Issue: "skipped: 0" hardcoded in return

**Fix:** Always use the variable, never hardcode:

```typescript
// Define at top of insertBatch
let skipped = 0;

// Increment in condition
if (existing) skipped++;

// Use in return
return { ..., skipped, ... };
```

### Issue: Seeder doesn't add to cache after insert

**Fix:** Cache write must happen immediately after insert:

```typescript
const result = await db.insert(...).returning();
if (result.length > 0) {
  inserted++;
  this.cache.authors.set(raw.name, result[0].id); // <- Add this!
}
```

### Issue: New seeder added but orchestrator doesn't instantiate it

**Fix:** Add switch case in orchestrator:

```typescript
case "my-entity":
  if (entitiesToSeed.includes("my-entity")) {
    const seeder = new MySeeder(this.cache, this.config.options);
    this.results.push(await seeder.seed());
  }
  break;
```

### Issue: TypeScript error "Cannot find name 'MySeeder'"

**Fix:** Import seeder at top of orchestrator:

```typescript
import { MySeeder } from "./seeders/my-seeder";
```

## Testing Patterns

When writing tests for seeders:

```typescript
// Mock BaseSeeder if needed
jest.mock("../seeders/base-seed");

// Mock cache
const mockCache: LookupCache = {
  users: new Map(),
  authors: new Map()
  // ... other entities
};

// Mock db
const mockDb = {
  insert: jest.fn(),
  query: jest.fn()
};

// Create seeder instance
const seeder = new MySeeder(mockCache, {
  dryRun: false,
  verbose: false
});

// Verify cache updates
expect(mockCache.authors.get("Author Name")).toBe(expectedId);

// Verify EntityResult accuracy
expect(result.inserted).toBe(expectedCount);
expect(result.skipped).toBe(expectedSkipped);
expect(result.errors).toEqual([]);
```

## Type Safety

**No `any` types allowed** in seed system:

```typescript
// ❌ Bad
const result: any = await db.insert(...).returning();

// ✅ Good
const result = await db.insert(user).values(...).returning();
// Type inferred from schema: Array<typeof user.$inferSelect>
```

Use Drizzle's `$inferSelect` for proper typing:

```typescript
type UserRow = typeof user.$inferSelect;

async insertBatch(data: UserSeedItem[]): Promise<EntityResult> {
  const results: UserRow[] = await db.insert(user).values(...).returning();
  // results is properly typed
}
```

## Code Organization

```
src/scripts/seed/
├── seeders/
│   ├── base-seed.ts              # Abstract base class (don't modify unless template changes)
│   ├── user-seeder.ts            # User entity seeder
│   ├── comic-seeder.ts           # Comic entity seeder
│   ├── chapter-seeder.ts         # Chapter entity seeder
│   ├── comic-image-seeder.ts     # Comic images seeder
│   ├── chapter-image-seeder.ts   # Chapter images seeder
│   ├── type-seeder.ts            # Type entity seeder
│   ├── author-seeder.ts          # Author entity seeder
│   ├── artist-seeder.ts          # Artist entity seeder
│   └── genre-seeder.ts           # Genre entity seeder
├── helpers/
│   ├── html-utils.ts             # Shared HTML utilities (stripHtmlTags)
│   ├── chapter-number-extractor.ts
│   ├── creator-name-resolver.ts
│   └── ... other utilities
├── database/
│   ├── batch-processor.ts        # Batch operations
│   └── transaction-manager.ts    # Transaction handling
├── seed-orchestrator.ts          # Main coordinator
├── index.ts                      # Central exports
├── types.ts                      # Core types
├── logger.ts                     # Logging utility
└── data-loader.ts               # JSON data loading
```

**Rule:** One seeder per entity type. Utilities in `helpers/` directory.

## Quality Gates

Before committing seed changes:

```bash
pnpm type-check      # Must be 0 TypeScript errors
pnpm test            # All tests must pass
pnpm lint:fix        # Code style consistent
```

All changes to seed system must pass the **Quality Gate**.
