# Seed System Architecture

Comprehensive database seeding system for ComicWise with configurable image handling, per-entity transactions, concurrent batch processing, and detailed progress tracking.

## Quick Reference

| Component | Type | Purpose |
| --- | --- | --- |
| **seedOrchestrator.ts** | Orchestrator | Dependency-ordered seeding (types→authors→comics→chapters) |
| **run.ts** | CLI Entry | Command-line interface with Commander.js parsing |
| **baseSeed.ts** | Base Class | Template method pattern for all seeders |
| **comicSeeder.ts** | Seeder | Comics with relations (author, artist, genre, images) |
| **chapterSeeder.ts** | Seeder | Chapters with image linking and chapter number extraction |
| **imageStrategy.ts** | Strategy | Multi-mode image handling (urls, local, imagekit) |
| **progressTracker.ts** | Utility | Real-time progress metrics and ASCII progress bars |
| **transactionManager.ts** | Utility | Drizzle transaction wrapping with rollback |
| **batchProcessor.ts** | Utility | Concurrent batch processing with error isolation |
| **dataLoader.ts** | Utility | JSON loading with fallback pattern (data.json → data-data1.json → data-data2.json) |

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         CLI Entry Point (run.ts)                        │
│                                                                         │
│  Parses: --dry-run, --batch-size, --concurrency, --image-strategy,    │
│          --force, --verbose, --skip-validation, --no-transaction       │
└──────────────────────────────────────┬──────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    SeedOrchestrator (seedOrchestrator.ts)               │
│                                                                         │
│  Dependency Order:                                                      │
│  1. Types (0 deps)                                                      │
│  2. Authors (0 deps)  ──┐                                               │
│  3. Artists (0 deps)  ──┼─→ 4. Comics (depends on types/authors/etc)   │
│  4. Genres (0 deps)   ──┤        │                                      │
│                         │        ▼                                      │
│                         └─→ 5. Chapters (depends on comics)            │
│  6. Users (0 deps)                                                      │
│                                                                         │
│  Creates: LookupCache (shared ID mappings across seeders)             │
└──────────────────────────────────────┬──────────────────────────────────┘
                                       │
         ┌─────────────────────────────┼──────────────┬──────────┬────────┐
         │                             │              │          │        │
         ▼                             ▼              ▼          ▼        ▼
    ┌─────────┐  ┌──────────┐  ┌───────────┐  ┌─────────┐  ┌──────────┐
    │TypeSeeder│  │AuthorSeeder│ │GenreSeeder│  │ComicSeeder│ │ChapterSeeder│
    │ (5 items)│  │(~50 items)│ │(~30 items)│  │(~2k items)│ │(~50k items)│
    └──┬───────┘  └─────┬──────┘ └─────┬─────┘  └─────┬────┘  └─────┬──────┘
       │                │             │              │            │
       └────────────────────────────────────────────────────────────┘
                                  │
                    (each extends) ▼
       ┌──────────────────────────────────────────────┐
       │         BaseSeeder<T> Template Method         │
       │                                              │
       │  1. loadData()      - DataLoader with cache  │
       │  2. validateData()  - Zod schema validation  │
       │  3. processBatches() - BatchProcessor        │
       │      │                                       │
       │      ├─ For each batch:                      │
       │      │   ├─ TransactionManager.withTransaction│
       │      │   ├─ insertBatch() (seeder override)  │
       │      │   ├─ ProgressTracker.record*()        │
       │      │   └─ Catch errors, log, continue      │
       │      │                                       │
       │      └─ Return EntityResult                  │
       │                                              │
       │  4. Return: EntityResult                     │
       │     - inserted, updated, skipped, errors     │
       │     - duration, success status               │
       └──────────────────────────────────────────────┘
                                  │
                                  ▼
       ┌──────────────────────────────────────────────┐
       │         Aggregated SeedReport                │
       │                                              │
       │  results: EntityResult[] (one per seeder)    │
       │  summary: {                                  │
       │    totalInserted, totalUpdated,              │
       │    totalSkipped, totalErrors                 │
       │  }                                           │
       │  duration, warnings, errors                  │
       └──────────────────────────────────────────────┘
                                  │
                      ┌───────────┴─────────────┐
                      ▼                         ▼
                  CLI Output           REST API Response
               (logger.table)         (/api/seed endpoint)
```

## File Descriptions

### Core Modules

#### `types.ts` (210 lines)

Central type definitions for entire seeding system.

**Key Types:**

- `SeedOptions` - CLI/API configuration flags
- `SeedConfig` - Complete configuration object
- `EntityResult` - Per-entity seeding metrics
- `SeedReport` - Final aggregated report
- `LookupCache` - Shared ID mappings across seeders
- `ImageStrategyContext` - Image handling configuration
- `ActionResult<T>` - Standard success/error response

**Usage:**

```typescript
import type { SeedConfig, EntityResult, LookupCache } from "./types";
```

#### `logger.ts` (80 lines)

Colored terminal output with chalk.

**Methods:**

- `info(msg)` - Blue ℹ info message
- `success(msg)` - Green ✓ success message
- `warn(msg)` - Yellow ⚠ warning message
- `error(msg)` - Red ✗ error message
- `debug(msg)` - Gray ➤ debug (only if verbose)
- `section(title)` - Section header with separator
- `progress(msg)` - Arrow → bullet point
- `table(data)` - Formatted table output

**Example:**

```typescript
logger.section("Seeding Comics");
logger.success(`Loaded ${data.length} records`);
logger.warn(`Skipped 5 invalid items`);
```

#### `config.ts` (120 lines)

Commander.js CLI argument parsing and Zod env validation.

**CLI Arguments:**

- `--dry-run` - Validate without persisting
- `--verbose` - Detailed logging
- `--batch-size <num>` - Items per batch (default: 100)
- `--concurrency <num>` - Parallel operations (default: 5)
- `--force` - Force overwrite (upsert)
- `--skip-validation` - Skip Zod validation
- `--no-transaction` - Disable transactions
- `--image-strategy <mode>` - urls|local|imagekit

**Output:**

```typescript
const config: SeedConfig = parseCliArgs();
// {
//   entities: ["types", "authors", "comics", ...],
//   options: {
//     verbose: true,
//     dryRun: false,
//     batchSize: 100,
//     ...
//   }
// }
```

#### `dataLoader.ts` (150 lines)

JSON file loading with fallback pattern and caching.

**Feature:**

- Tries `user.json` → `user-data1.json` → `user-data2.json` (etc.)
- Caches loaded arrays to avoid re-reading
- Returns typed data via generic `<T>`

**Example:**

```typescript
const comics = await dataLoader.loadWithFallback<ComicSeed>("comic");
// Tries: comic.json → comic-data1.json → comic-data2.json
// Caches result for subsequent calls
```

#### `seedOrchestrator.ts` (180 lines)

Orchestrates seeding execution in dependency order.

**Seeding Order:**

1. **Types** (0 dependencies)
2. **Authors** (0 dependencies) - Cache populated
3. **Artists** (0 dependencies) - Cache populated
4. **Genres** (0 dependencies) - Cache populated
5. **Comics** (depends on types, authors, artists, genres) - Uses cache to resolve IDs
6. **Chapters** (depends on comics) - Uses cache to resolve comic IDs
7. **Users** (0 dependencies)

**LookupCache:**

```typescript
interface LookupCache {
  authors: Map<string, { id: string; name: string }>;
  artists: Map<string, { id: string; name: string }>;
  types: Map<string, string>; // name → id
  genres: Map<string, string>; // name → id
  comics: Map<string, string>; // slug → id
}
```

### Seeders

#### `baseSeed.ts` (310 lines)

Abstract base class implementing template method pattern.

**Template Method: `seed()`**

1. Load data via `getDataSources()`
2. Validate with Zod schema
3. Check dry-run flag
4. Call `insertBatch()` (seeder-specific)
5. Return `EntityResult`

**Abstract Methods (child classes must implement):**

- `getDataSources(): string[]` - JSON file names
- `transformData(raw: T): unknown` - Transform before inserting
- `insertBatch(data: T[]): Promise<EntityResult>` - DB insert logic

**Example:**

```typescript
export class ComicSeeder extends BaseSeeder<ComicSeed> {
  protected getDataSources() {
    return ["comic"]; // comic.json → comic-data1.json → etc.
  }

  protected async insertBatch(
    data: ComicSeed[]
  ): Promise<EntityResult> {
    // Insert comics with relation resolution
    // Return EntityResult with counts
  }
}
```

#### `comicSeeder.ts` (250 lines)

Complex seeder handling relations, images, and HTML stripping.

**Process:**

1. Load comics from JSON
2. Resolve author/artist/type/genre IDs from cache
3. Strip HTML tags from descriptions
4. Handle first image as coverImage, rest as comicImage table entries
5. Insert genre relations into comicToGenre junction table
6. Track progress with ProgressTracker

#### `chapterSeeder.ts` (200 lines)

Handles chapter extraction with number parsing and image linking.

**Process:**

1. Load chapters from JSON
2. Extract chapter number from name via regex: `/Chapter\s+(\d+)/i`
3. Resolve comic.slug → comicId from cache
4. Insert chapters and link images to chapterImage table
5. Maintain chapter order via imageOrder field

### Utilities

#### `progressTracker.ts` (150 lines)

Real-time progress metrics and ASCII progress bars.

**Features:**

- Logs every 50 items OR every 5 seconds (whichever comes first)
- ASCII progress bar: `[███████░░░░░░░░░░░░]`
- Calculates: speed (items/sec), ETA, duration
- Tracks: inserted, updated, skipped, errors

**Methods:**

- `recordInsert(count)` - Increment inserted counter
- `recordUpdate(count)` - Increment updated counter
- `recordSkip(count)` - Increment skipped counter
- `recordError(count)` - Increment error counter
- `complete()` - Return final ProgressMetrics

**Example Output:**

```
Processing 2087 items (batch=100, concurrency=5):
  [████████████████░░░░░░░░░░░░░░░░░░░░░░] 45% (940/2087)
  Inserted: 940 | Updated: 0 | Skipped: 0 | Errors: 0
  Speed: 218/sec | Duration: 4.3s | ETA: 5.1s
```

#### `batchProcessor.ts` (150 lines)

Concurrent batch processing with Promise.allSettled for error isolation.

**Features:**

- Sequential batches, concurrent items within each batch
- Respects concurrency limit (default: 5)
- Promise.allSettled prevents one error from stopping batch
- Optional callbacks: onBatchComplete, onError

**Usage:**

```typescript
const processor = new BatchProcessor({
  batchSize: 100,
  concurrency: 5
});
const result = await processor.process(items, async item => {
  // Process each item
  return result;
});
// Returns: { results: T[], errors: Error[] }
```

#### `transactionManager.ts` (80 lines)

Drizzle transaction wrapping with automatic rollback.

**Usage:**

```typescript
return await TransactionManager.withTransaction(
  "Comics",
  options,
  async (tx) => {
    // All DB operations wrapped in transaction
    const result = await tx.insert(comic).values(...);
    return result;
  }
);
// Auto-rollback if error thrown
```

#### `conflictResolver.ts` (50 lines)

Upsert pattern support for onConflictDoUpdate.

**Usage:**

```typescript
// Insert or update if exists
await db.insert(comic)
  .values(data)
  .onConflictDoUpdate({
    target: comic.slug,
    set: { updatedAt: new Date(), ... }
  });
```

### Image Handling

#### `imageStrategy.ts` (120 lines)

Strategy pattern dispatcher for image handling (3 modes).

**Modes:**

1. **urls** - Return original URLs unchanged (no network)
2. **local** - Download to `./public/comics/{type}/` with caching
3. **imagekit** - Upload to ImageKit CDN and return CDN URLs

**Methods:**

- `processImage(url, entityType, entityId)` - Process single image
- `batchProcess(urls[], entityType, entityId, concurrency)` - Process multiple with concurrency
- `getMode()` / `setMode()` - Runtime mode switching

**Usage:**

```typescript
const strategy = new ImageStrategy({ mode: "local" });
const result = await strategy.processImage(
  "https://example.com/image.jpg",
  "comic",
  1
);
// Returns: { success: true, url: "/comics/comic/1-hash.jpg" }
```

#### `imageDownloader.ts` (180 lines)

Local filesystem caching with exponential backoff retry.

**Features:**

- 3 attempts with exponential backoff (1s, 2s, 4s delays)
- File existence check (cache hit detection)
- Consistent filename generation from URL hash
- 10-second HTTP timeout via AbortController
- User-Agent header for requests

**Usage:**

```typescript
const result = await imageDownloader.download(
  "https://example.com/image.jpg",
  "comic",
  1
);
// Returns: { success: true, filePath: "/comics/comic/1-hash.jpg" }
```

#### `imageKitUploader.ts` (80 lines)

ImageKit CDN integration for cloud image storage.

**Features:**

- API key validation
- CDN URL construction
- Fallback to original URL on error

**Setup:**

```env
IMAGEKIT_PUBLIC_KEY="..."
IMAGEKIT_PRIVATE_KEY="..."
IMAGEKIT_URL_ENDPOINT="https://ik.imagekit.io/account"
```

### Helpers

#### `progressTracker.ts` - See Utilities section

#### `creatorNameResolver.ts` (80 lines)

Author/artist name deduplication with caching.

**Functions:**

- `splitCreators("A/B/C")` → `["A", "B", "C"]`
- `normalizeCreatorName("Name ")` → `"name"`
- `lookupOrCreateAuthor(name, cache, dal)` - Get or create with dedup

**Features:**

- Handles "/" separator for multiple creators
- "\_" placeholder replaced with "Unknown"
- Case-insensitive deduplication
- Cache-backed lookups

#### `dateParser.ts` (40 lines)

Flexible date parsing handling multiple formats.

**Formats:**

- ISO-8601: `2025-03-04T12:00:00Z`
- English: `August 14, 2025` or `August 14th 2025`
- Numeric: `03/04/2025` or `2025-03-04`
- Other: Via Date constructor fallback

**Usage:**

```typescript
const date = parseDate("August 14th 2025"); // Returns Date object
const date = parseDate("invalid"); // Returns null
```

#### `chapterNumberExtractor.ts` (30 lines)

Chapter number extraction via regex.

**Pattern:** `/Chapter\s+(\d+)/i`

**Examples:**

- `"Chapter 273"` → `273`
- `"CHAPTER 10"` → `10`
- `"Ch. 5"` → `null` (doesn't match pattern)
- `"273"` → `null` (requires "Chapter" prefix)

## Seeding Order Dependencies

```
┌────────────────────────────────────────────────┐
│              No Dependencies                   │
├────────────────────────────────────────────────┤
│  • Types  (5 predefined items)                │
│  • Authors  (JSON load)                       │
│  • Artists  (JSON load)                       │
│  • Genres  (JSON load)                        │
│  • Users  (JSON load)                         │
└────────────────────────────────────────────────┘
                      │
                      ▼
┌────────────────────────────────────────────────┐
│         Comics (needs types, authors,          │
│         artists, genres via cache)            │
└────────────────────────────────────────────────┘
                      │
                      ▼
┌────────────────────────────────────────────────┐
│         Chapters (needs comics via cache)     │
└────────────────────────────────────────────────┘
```

## Caching Pattern

### LookupCache Usage

Seeders share a single LookupCache instance populated during execution:

```typescript
// Author seeder populates:
cache.authors.set("TurtleMe", { id: "123", name: "TurtleMe" });

// Comic seeder reads:
const authorId = cache.authors.get("TurtleMe")?.id; // "123"

// Chapter seeder reads to resolve comic:
const comicId = cache.comics.get("the-beginning-after-the-end"); // "456"
```

**Benefits:**

- Single database query per entity
- No N+1 problem
- type-safe ID resolution
- Prevents orphaned FK references

## Error Handling

### Per-Seeder Errors

```typescript
// Each seeder catches errors per item
try {
  // Insert item
} catch (error) {
  errors.push({
    itemIndex: i,
    value: data[i],
    message: error.message
  });
  // Continue processing next item
}

// Return: { inserted: N, skipped: 0, errors: [...] }
// No DB rollback, partial success allowed per seeder
```

### Transaction Errors

```typescript
// If transaction fails for entity:
try {
  return await withTransaction("Comics", options, async tx => {
    // DB operations
  });
} catch (error) {
  // Rollback automatic
  // Log error and return failure
  // Continue to next seeder
}
```

### Validation Errors

```typescript
// Zod schema validation
const result = schema.safeParse(item);
if (!result.success) {
  errors.push({
    itemIndex: i,
    message: result.error.errors[0].message
  });
  // Skip this item, continue processing
}
```

## Performance Optimizations

1. **Batch Processing**: Concurrent items within each batch (default: 5 concurrent)
2. **Caching**: Single load per data source, reused cache for ID resolution
3. **Deduplication**: Author/artist names deduplicated via normalizeCreatorName()
4. **Progress Logging**: Every 50 items or 5 seconds (not every item)
5. **Promise.allSettled**: Errors don't block other items in batch
6. **File Stat Check**: Image cache hit detection (no re-download)
7. **Exponential Backoff**: Intelligent retry delay for network failures

## Examples

### Seed Only Comics

```bash
pnpm seed comics
```

**Execution:**

1. SeedOrchestrator checks: Comics needs Types, Authors, Artists, Genres
2. Types, Authors, Artists, Genres seeded first (fast, <5s total)
3. Comics loaded, validated, inserted with images
4. Final report returned

### Dry-Run with Verbose

```bash
pnpm seed --dry-run --verbose
```

**Behavior:**

- Loads and validates all data
- Skips insertBatch() call
- Returns counts as if seeded (for estimation)
- Debug logs show detailed processing
- Database unchanged

### Upsert Mode

```bash
pnpm seed comics --force
```

**Behavior:**

- Existing comics by slug are updated
- New comics are inserted
- Updated count > 0 in report

---

**Status**: Production Ready ✓  
**Last Updated**: 2026-03-04  
**Maintainer**: ComicWise Team
