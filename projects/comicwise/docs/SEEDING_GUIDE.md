# ComicWise Database Seeding Guide

## Overview

The ComicWise seeding system provides an automated, production-ready solution for populating your database with ~5,000 comics and ~50,000 chapters from JSON data sources. The system supports both CLI (Command-Line Interface) and RESTful API approaches for flexible seeding execution.

**Key Features:**

- **Selective Entity Seeding**: Seed individual entities (types, authors, artists, genres, comics, chapters) or all at once
- **Dry-Run Mode**: Validate data without persisting to database
- **Force Overwrite (Upsert)**: Update existing records or skip duplicates
- **Concurrent Processing**: Configurable batch size and concurrency for optimal performance
- **Multiple Image Strategies**: Use original URLs, download locally, or upload to ImageKit CDN
- **Per-Entity Transactions**: Automatic rollback on errors for data integrity
- **Detailed Progress Tracking**: Real-time metrics with progress bars
- **Admin API**: Secure REST endpoints for remote seeding execution

---

## Quick Start

### 1. Verify Environment Variables

Ensure your `.env.local` has the required variables:

```env
DATABASE_URL="postgresql://user:pass@localhost:5432/comicwise"
AUTH_SECRET="your_secret_key_at_least_32_characters_long"
NEXT_PUBLIC_API_URL="http://localhost:3000"
NODE_ENV="development"   # Use "development" for full permissions

# Optional: For ImageKit image uploads
IMAGEKIT_PUBLIC_KEY="your_public_key"
IMAGEKIT_PRIVATE_KEY="your_private_key"
IMAGEKIT_URL_ENDPOINT="https://ik.imagekit.io/comicwise"
```

### 2. Prepare JSON Data Files

Place your data files in `src/data/`:

- `author.json` or `author-data1.json`, `author-data2.json` (fallback support)
- `artist.json` or `artist-data1.json`, etc.
- `genre.json` or `genre-data1.json`, etc.
- `comic.json` or `comic-data1.json`, `comic-data2.json`
- `chapter.json` or `chapter-data1.json`, `chapter-data2.json`
- `user.json` (optional)

**File Format Example** (comic.json):

```json
[
  {
    "title": "The Beginning After the End",
    "slug": "the-beginning-after-the-end",
    "description": "Manga about a reincarnated hero",
    "coverImage": "https://example.com/cover.jpg",
    "rating": 9.5,
    "status": "Ongoing",
    "url": "https://asuracomic.net/manga/beginning-after-end",
    "type": { "name": "Manga" },
    "author": { "name": "TurtleMe" },
    "artist": { "name": "Fuyuki23" },
    "genres": [
      { "name": "Action" },
      { "name": "Fantasy" },
      { "name": "Supernatural" }
    ],
    "images": [
      { "url": "https://example.com/image1.jpg" },
      { "url": "https://example.com/image2.jpg" }
    ],
    "updatedAt": "2025-03-04T00:00:00Z"
  }
]
```

---

## CLI Usage

### Run via npm Script

The easiest way to seed your database:

```bash
# Start Next.js dev server first (required for proper env loading)
pnpm dev &                                  # Run in background

# Wait a moment for server to start, then seed
pnpm seed                                   # Seed all entities (default)
```

### Available npm Scripts

```bash
# Seed all entities (types → authors → artists → genres → comics → chapters → users)
pnpm seed

# Seed specific entities only
pnpm seed types                             # Seed types only
pnpm seed authors artists                   # Seed authors and artists
pnpm seed comics chapters                   # Seed comics and chapters
pnpm seed users                             # Seed users

# Validation & Testing
pnpm seed --dry-run                         # Validate without persisting
pnpm seed --dry-run --verbose               # Validate with detailed logging

# Advanced Options
pnpm seed --batch-size=50                   # Custom batch size (default: 100)
pnpm seed --concurrency=3                   # Custom concurrency (default: 5)
pnpm seed --force                           # Force overwrite existing records (upsert)
pnpm seed --skip-validation                 # Skip Zod schema validation
pnpm seed --no-transaction                  # Disable per-entity transactions
pnpm seed --image-strategy=local            # Image strategy: urls|local|imagekit

# Maintenance
pnpm seed:validate                          # Dry-run validation only
pnpm seed:clear                             # Delete all seeded data (API DELETE)
pnpm seed:reset                             # Full reset: clear + reseed (API PUT)
```

### CLI Output Example

```
══════════════════════════════════════════════════════════════════════════════
  Seeding System Configuration
══════════════════════════════════════════════════════════════════════════════

  Entities: all (types, authors, artists, genres, comics, chapters, users)
  Batch Size: 100 items
  Concurrency: 5 parallel operations
  Dry Run: true
  Verbose Logging: true
  Image Strategy: urls

──────────────────────────────────────────────────────────────────────────────
  Types
──────────────────────────────────────────────────────────────────────────────

✓ Loaded 5 records from predefined types

→ Validating 5 records...
✓ Validation complete: 5 valid, 0 errors

DRY RUN: No data will be persisted
✓ Types seeding completed
  Inserted: 5 | Updated: 0 | Skipped: 0 | Errors: 0 | Duration: 1.2s

──────────────────────────────────────────────────────────────────────────────
  Comics
──────────────────────────────────────────────────────────────────────────────

ℹ Loading data from sources: comic
✓ Loaded 2087 records from comic.json

→ Validating 2087 records...
✓ Validation complete: 2087 valid, 0 errors

→ Processing in batches (batch-size=100, concurrency=5):
  [████████████████████░░░░░░░░░░░░░░░░░░░░░░░░ ] 50% (1044/2087)
  Inserted 1044 | Speed: 218/sec | ETA: 4.6s

✓ Comics seeding completed
  Inserted: 2087 | Updated: 0 | Skipped: 0 | Errors: 0 | Duration: 9.5s

══════════════════════════════════════════════════════════════════════════════
  Final Report
══════════════════════════════════════════════════════════════════════════════

Total Duration: 25.3s
Success: ✓

Summary:
  Total Inserted: 2097
  Total Updated: 0
  Total Skipped: 0
  Total Errors: 0
  Success Rate: 100%
```

---

## API Usage (RESTful)

### Setup

Ensure you have the Next.js development server running:

```bash
pnpm dev                                    # Starts server on http://localhost:3000
```

### Endpoints

All API endpoints are located at `/api/seed` and require authentication in production (admin role).

#### GET /api/seed - Validate Schema

**Purpose**: Validate seeding configuration without persisting data

```bash
curl -X GET http://localhost:3000/api/seed

# Response (200 OK):
{
  "ok": true,
  "message": "Seeding validation successful",
  "data": {
    "timestamp": "2025-03-04T12:00:00Z",
    "success": true,
    "totalDuration": 0,
    "results": [],
    "warnings": [],
    "errors": [],
    "summary": {
      "totalInserted": 0,
      "totalUpdated": 0,
      "totalSkipped": 0,
      "totalErrors": 0
    }
  }
}
```

#### POST /api/seed - Start Full Seeding

**Purpose**: Execute full seeding with specified entities and options

```bash
curl -X POST http://localhost:3000/api/seed \
  -H "Content-Type: application/json" \
  -d '{
    "entities": "all",
    "options": {
      "batchSize": 100,
      "concurrency": 5,
      "verbose": true,
      "dryRun": false,
      "imageStrategy": "urls"
    }
  }'

# Response (200 OK):
{
  "ok": true,
  "message": "Seeding completed successfully",
  "data": {
    "timestamp": "2025-03-04T12:00:00Z",
    "success": true,
    "totalDuration": 45230,
    "results": [
      {
        "entityName": "Types",
        "inserted": 5,
        "updated": 0,
        "skipped": 0,
        "errors": [],
        "duration": 234,
        "success": true
      },
      {
        "entityName": "Comics",
        "inserted": 2087,
        "updated": 0,
        "skipped": 0,
        "errors": [],
        "duration": 9500,
        "success": true
      },
      {
        "entityName": "Chapters",
        "inserted": 50000,
        "updated": 0,
        "skipped": 0,
        "errors": [],
        "duration": 30000,
        "success": true
      }
    ],
    "warnings": [],
    "errors": [],
    "summary": {
      "totalInserted": 52092,
      "totalUpdated": 0,
      "totalSkipped": 0,
      "totalErrors": 0
    }
  }
}
```

#### POST Request Options

```typescript
{
  // Entities to seed (string or array)
  "entities": "all",  // or: "types" | "authors" | "artists" | "genres" | "comics" | "chapters" | "users"

  "options": {
    "batchSize": 100,              // Items per batch (default: 100)
    "concurrency": 5,              // Parallel operations (default: 5)
    "verbose": false,              // Enable detailed logging
    "dryRun": false,               // Validate without persisting
    "skipValidation": false,       // Skip Zod validation
    "useTransaction": true,        // Wrap in transactions
    "forceOverwrite": false,       // Update existing (upsert mode)
    "imageStrategy": "urls"        // Image mode: "urls" | "local" | "imagekit"
  }
}
```

#### PATCH /api/seed - Upsert Mode

**Purpose**: Seed with force-overwrite (update existing records)

```bash
curl -X PATCH http://localhost:3000/api/seed \
  -H "Content-Type: application/json" \
  -d '{
    "entities": ["comics"],
    "options": {
      "forceOverwrite": true
    }
  }'

# Response: Same format as POST, with updated being > 0
```

#### PUT /api/seed - Full Reset

**Purpose**: Delete all seeded data and reseed from scratch

```bash
curl -X PUT http://localhost:3000/api/seed \
  -H "Content-Type: application/json" \
  -d '{
    "entities": "all"
  }'

# Performs DELETE followed by INSERT for complete reset
```

#### DELETE /api/seed - Clear All Data

**Purpose**: Delete all seeded data without reseeding

```bash
curl -X DELETE http://localhost:3000/api/seed

# Response:
{
  "ok": true,
  "message": "All seeded data cleared successfully",
  "data": {
    "deleted": 52097,
    "timestamp": "2025-03-04T12:00:00Z"
  }
}
```

#### Error Responses

**400 Bad Request** - Invalid input:

```json
{
  "code": 400,
  "error": "Invalid entities: 'comics' must be one of [types, authors, ...]",
  "ok": false
}
```

**401 Unauthorized** - Missing authentication (production only):

```json
{
  "code": 401,
  "error": "Unauthorized: Admin role required for seeding",
  "ok": false
}
```

**500 Server Error** - Seeding failure:

```json
{
  "code": 500,
  "error": "Database connection failed",
  "ok": false
}
```

---

## Image Strategies

### Strategy: `urls` (Default)

Uses original image URLs without downloading or uploading.

**Pros:**

- Fastest (no network operations)
- Minimal storage usage
- No ImageKit credentials needed

**Cons:**

- Depends on original URL availability
- No local caching
- Broken links not detected until used

**Usage:**

```bash
pnpm seed --image-strategy=urls
```

### Strategy: `local`

Downloads images to local filesystem with caching.

**Pros:**

- Images stored locally (reliable availability)
- Automatic retry with exponential backoff
- Cache prevents re-downloading
- Perfect for development

**Cons:**

- Requires filesystem space (~5-20GB for 50K images)
- Slower initial seeding
- Images served from local filesystem

**Usage:**

```bash
pnpm seed --image-strategy=local
```

**Cache Location:**

- Default: `./public/comics/`
- Structure: `{entity_type}/{entity_id}-{url_hash}.{extension}`

### Strategy: `imagekit`

Uploads images to ImageKit CDN.

**Pros:**

- Global CDN distribution
- Optimized image delivery
- Automatic resizing and optimization
- Production-ready

**Cons:**

- Requires ImageKit account and API keys
- Upload time overhead
- ImageKit storage costs

**Setup:**

1. Create ImageKit account at https://imagekit.io
2. Get API credentials from dashboard
3. Set environment variables:
   ```env
   IMAGEKIT_PUBLIC_KEY="your_public_key"
   IMAGEKIT_PRIVATE_KEY="your_private_key"
   IMAGEKIT_URL_ENDPOINT="https://ik.imagekit.io/your_account"
   ```

**Usage:**

```bash
pnpm seed --image-strategy=imagekit
```

---

## Data Schema & Formats

### Comics Schema

```javascript
{
  "title": "String (required)",
  "slug": "string-slug-format (required)",
  "description": "String (optional, HTML tags removed automatically)",
  "url": "https://source-url.com (optional)",
  "rating": "0-10 (coerced to number, optional)",
  "status": "Ongoing | Completed | Hiatus | Dropped | Season End | Coming Soon",
  "coverImage": "https://image-url.jpg (optional)",
  "type": { "name": "Manga | Manhwa | Manhua | Web Comic | Light Novel" },
  "author": { "name": "Author Name" } or null,
  "artist": { "name": "Artist Name" } or null,
  "genres": [
    { "name": "Action" },
    { "name": "Fantasy" }
  ],
  "images": [
    { "url": "https://page1.jpg" },
    { "url": "https://page2.jpg" }
  ],
  "updatedAt": "2025-03-04T12:00:00Z (ISO-8601 date)"
}
```

### Chapters Schema

```javascript
{
  "name": "Chapter 273 (extracted automatically to chapterNumber: 273)",
  "title": "Chapter Title (optional, defaults to 'Untitled Chapter')",
  "slug": "chapter-slug (required)",
  "url": "https://source-url.com (optional)",
  "comic": {
    "title": "Comic Title",
    "slug": "comic-slug"  // Used to resolve comic ID from cache
  },
  "releaseDate": "2025-03-04T12:00:00Z (optional)",
  "updatedAt": "2025-03-04T12:00:00Z",
  "images": [
    { "url": "https://page1.jpg" },
    { "url": "https://page2.jpg" }
  ]
}
```

---

## Troubleshooting

### Problem: "Database connection failed"

**Cause**: DATABASE_URL is invalid or database server is down

**Solution**:

1. Verify PostgreSQL is running: `psql -U user -h localhost`
2. Check DATABASE_URL format: `postgresql://user:pass@host:5432/dbname`
3. Ensure credentials are correct in `.env.local`

### Problem: "AUTH_SECRET not found"

**Cause**: Environment variables not loaded

**Solution**:

1. Verify `.env.local` exists and has AUTH_SECRET
2. Restart Next.js dev server: `pnpm dev`
3. Use API approach instead of CLI (API loads env first)

### Problem: "Image download failed after retries"

**Cause**: Image URL is broken or server is blocking requests

**Solution**:

1. Verify image URLs are valid and accessible
2. Check if image server requires authentication
3. Try `--image-strategy=urls` to skip downloading
4. Manually update coverImage in JSON if URL is invalid

### Problem: "Chapter number extraction failed"

**Cause**: Chapter name format doesn't match expected pattern

**Expected Format**: "Chapter 273" or "Ch. 273"

**Regex Used**: `/Chapter\s+(\d+)/i`

**Solution**:

1. Update JSON data to use correct format
2. Or update `chapterNumberExtractor.ts` regex if needed

### Problem: "Author/artist name duplication"

**Cause**: Names that differ slightly create duplicate entries

**Solution**:

1. Pre-process JSON to normalize names (lowercase, trim whitespace)
2. Use `--force` flag to merge duplicates during upsert
3. Manually clean up duplicates after seeding

### Problem: "Timeout: operation took too long"

**Cause**: Network or database performance issues

**Solution**:

1. Reduce `--batch-size` (default 100): `pnpm seed --batch-size=50`
2. Reduce `--concurrency` (default 5): `pnpm seed --concurrency=3`
3. Increase database connection timeout in DATABASE_URL
4. Check database server load/resources

---

## Performance Benchmarks

Expected seeding performance (on standard hardware):

| Entity   | Count  | Strategy | Duration | Speed    |
| -------- | ------ | -------- | -------- | -------- |
| Types    | 5      | N/A      | <1s      | -        |
| Authors  | 50     | DB only  | <1s      | -        |
| Artists  | 50     | DB only  | <1s      | -        |
| Genres   | 30     | DB only  | <1s      | -        |
| Comics   | 2,087  | URLs     | 8-12s    | ~200/sec |
| Comics   | 2,087  | Local    | 30-45s   | ~60/sec  |
| Comics   | 2,087  | ImageKit | 60-120s  | ~20/sec  |
| Chapters | 50,000 | URLs     | 45-60s   | ~900/sec |
| Chapters | 50,000 | Local    | 120-180s | ~300/sec |
| Chapters | 50,000 | ImageKit | 300-600s | ~100/sec |

**Total Seeding Time** (estimate):

- URLs strategy: **~70 seconds**
- Local strategy: **~240 seconds** (4 minutes)
- ImageKit strategy: **~700 seconds** (12 minutes)

---

## Security & Best Practices

### Authentication

- **Development**: All seeding endpoints are available
- **Production**: Only users with `admin` role can seed data

```typescript
// Check your session role before seeding
if (session?.user?.role !== "admin") {
  return { ok: false, error: "Unauthorized" };
}
```

### Data Validation

All input data is validated with Zod schemas:

- Dates are coerced to proper Date objects
- Numbers are coerced from strings
- Status enums are validated (Title-Case required)
- URLs are validated for proper format

### Transaction Safety

Each entity seeding is wrapped in a transaction:

- All-or-nothing for each entity
- Automatic rollback on error
- FK constraints verified incrementally

### Logging

Sensitive data is never logged:

- Passwords are omitted
- API keys are not logged
- Only essential metrics are shown

---

## Advanced Usage

### Custom Batch Size & Concurrency

Optimize based on your database and network:

```bash
# For fast local database with good network
pnpm seed --batch-size=500 --concurrency=10

# For slower network or constrained resources
pnpm seed --batch-size=25 --concurrency=2
```

### Seeding Specific Entities

```bash
# Seed only authors and artists
pnpm seed authors artists

# Seed comics without chapters
pnpm seed comics
```

### Force Overwrite Mode

Update existing records instead of skipping:

```bash
# Update all comics if they exist
pnpm seed comics --force
```

### Skip Validation

For trusted data sources:

```bash
# Skip Zod validation (faster, but risky)
pnpm seed --skip-validation
```

---

## File Structure

```
src/scripts/seed/
├── types.ts                    # Core type definitions
├── logger.ts                   # Logger utility
├── config.ts                   # CLI configuration
├── dataLoader.ts               # JSON file loading with fallback
├── seedOrchestrator.ts         # Orchestration & dependency order
├── run.ts                      # CLI entry point
├── index.ts                    # Seeder exports
│
├── seeders/                    # Entity seeders
│   ├── baseSeed.ts            # Abstract base class
│   ├── typeSeeder.ts          # Types (predefined)
│   ├── authorSeeder.ts        # Authors from JSON
│   ├── artistSeeder.ts        # Artists from JSON
│   ├── genreSeeder.ts         # Genres from JSON
│   ├── comicSeeder.ts         # Comics with relations
│   └── chapterSeeder.ts       # Chapters with images
│
├── helpers/                    # Utility functions
│   ├── progressTracker.ts     # Progress metrics & bars
│   ├── creatorNameResolver.ts # Name splitting & dedup
│   ├── dateParser.ts          # Flexible date parsing
│   └── chapterNumberExtractor.ts # Chapter number regex
│
├── database/                   # Database operations
│   ├── batchProcessor.ts      # Concurrent batching
│   ├── transactionManager.ts  # Transaction wrapping
│   └── conflictResolver.ts    # Upsert patterns
│
└── images/                     # Image handling
    ├── imageDownloader.ts     # Local cache & retry
    ├── imageKitUploader.ts    # ImageKit integration
    └── imageStrategy.ts       # Strategy dispatcher

src/app/api/seed/
└── route.ts                    # REST API endpoints

src/schemas/seed/               # Zod validation schemas
├── user.seed.ts
├── comic.seed.ts
├── chapter.seed.ts
├── author.seed.ts
├── artist.seed.ts
├── genre.seed.ts
├── type.seed.ts
└── index.ts

src/data/                       # JSON data files (not in repo)
├── author.json
├── artist.json
├── genre.json
├── comic.json
└── chapter.json
```

---

## Support & Contributing

For issues, questions, or improvements:

1. Check this guide's troubleshooting section
2. Review code comments in `/src/scripts/seed/`
3. Check database schema in `/src/database/schema.ts`
4. Review implementation notes in `/IMPLEMENTATION_NOTES.md`

---

**Version**: 1.0  
**Last Updated**: 2026-03-04  
**Status**: Production Ready ✓
