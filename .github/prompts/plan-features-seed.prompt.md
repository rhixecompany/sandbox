---
description: "Implement Full-Featured Dynamic Database Seeding System with TypeScript & Next.js Best Practices"
agent: "Next.js Expert"
model: "Claude Haiku 4.5 (copilot)"
tools:
  [
    vscode,
    execute,
    read,
    agent,
    edit,
    search,
    web,
    "github/*",
    "context7/*",
    "modelcontextprotocol-servers-sequentialthinking/*",
    "next-devtools/*",
    "nextjs-docs-mcp/*",
    "sentry/*",
    "shadcn/*",
    "github/*",
    "io.github.chromedevtools/chrome-devtools-mcp/*",
    "io.github.upstash/context7/*",
    "playwright/*",
    vscode.mermaid-chat-features/renderMermaidDiagram,
    github.vscode-pull-request-github/issue_fetch,
    github.vscode-pull-request-github/suggest-fix,
    github.vscode-pull-request-github/searchSyntax,
    github.vscode-pull-request-github/doSearch,
    github.vscode-pull-request-github/renderIssues,
    github.vscode-pull-request-github/activePullRequest,
    github.vscode-pull-request-github/openPullRequest,
    ms-azuretools.vscode-containers/containerToolsConfig,
    prisma.prisma/prisma-migrate-status,
    prisma.prisma/prisma-migrate-dev,
    prisma.prisma/prisma-migrate-reset,
    prisma.prisma/prisma-studio,
    prisma.prisma/prisma-platform-login,
    prisma.prisma/prisma-postgres-create-database,
    todo
  ]
---

# Introduction

![Status: Planned](https://img.shields.io/badge/status-Planned-blue)

Implement a comprehensive, production-ready database seeding system for ComicWise that automates population of ~5,000 comics and ~50,000 chapters from JSON sources. The system combines patterns from comicwise v3, bookwise, and comicr reference implementations. Features include: configurable image handling (local/URLs/ImageKit), per-entity transactions, concurrent batch processing with detailed progress tracking, Commander.js CLI, comprehensive Zod validation, and RESTful admin API. All code follows TypeScript strict mode and Next.js App Router conventions.

---

## 1. Requirements & Constraints

### Functional Requirements

- **REQ-001**: CLI support for `pnpm seed [entities] [options]` with selective entity seeding (users, types, authors, artists, genres, comics, chapters, all)
- **REQ-002**: RESTful API endpoints (POST, GET, DELETE, PUT, PATCH) for remote seeding execution
- **REQ-003**: Multi-source JSON loading with automatic fallback (user.json → user-data1.json → user-data2.json)
- **REQ-004**: Zod validation with `.coerce` for flexible date/number format parsing
- **REQ-005**: Per-entity transaction support with automatic rollback on error
- **REQ-006**: Configurable image handling: local filesystem cache, URL-only, or ImageKit upload
- **REQ-007**: Concurrent batch processing (configurable concurrency: default 5, configurable batch size: default 100)
- **REQ-008**: Dry-run mode that validates without persisting to database
- **REQ-009**: Force-overwrite mode for upsert operations (onConflictDoUpdate pattern)
- **REQ-010**: Detailed progress tracking with metrics (inserted, updated, skipped, errors, speed, duration)
- **REQ-011**: Author/artist name deduplication with caching (split on "/" separator, handle "\_" placeholders)
- **REQ-012**: Chapter number extraction via regex from "Chapter 273" format

### Non-Functional Requirements

- **REQ-013**: TypeScript strict mode enabled; zero `any` types except for DAL integration
- **REQ-014**: All code must pass `pnpm type-check` with zero errors
- **REQ-015**: Follows Next.js App Router conventions (no Pages Router patterns)
- **REQ-016**: Compatible with Drizzle ORM v0.45+ and PostgreSQL/Neon
- **REQ-017**: Compatible with NextAuth v5 for API authentication
- **REQ-018**: Supports batch operations on 50,000+ records efficiently
- **REQ-019**: Progress logging every 50 items or 5 seconds

### Security Requirements

- **SEC-001**: API endpoints require admin role in production; dev mode bypass for NODE_ENV=development
- **SEC-002**: All environment variables validated with Zod before use
- **SEC-003**: Database operations use parameterized queries (Drizzle built-in)
- **SEC-004**: No sensitive data logged (passwords hashed, tokens omitted)

### Constraints

- **CON-001**: Comic JSON uses nested objects for relations (author: { name: "X" }); must resolve to FK references
- **CON-002**: Chapter JSON references parent comic by title + slug; must handle fuzzy matching
- **CON-003**: Comic status enum is Title-Case ("Ongoing", not "ongoing")
- **CON-004**: Rating field in JSON is string; must coerce to number
- **CON-005**: Date formats vary ("August 14th 2025" vs ISO-8601); must handle both
- **CON-006**: ~25-30% of comics have author/artist as "\_" (unknown); must handle gracefully
- **CON-007**: Image URLs may be from multiple domains (asuracomic.net, gg.asuracomic.net)
- **CON-008**: ~95% of serialization field is "\_"; skip or set to NULL
- **CON-009**: Chapter images may be 0, 5, 12+; handle variable array lengths
- **CON-010**: ComicToGenre is many-to-many junction table; requires separate insert

### Guidelines

- **GUD-001**: Use factory/builder patterns for seeder instantiation
- **GUD-002**: Implement singleton pattern for DataLoader (cache across seeders)
- **GUD-003**: Use Strategy pattern for image handling (local, urls, imagekit modes)
- **GUD-004**: Export all seeders from `/src/scripts/seed/index.ts` for API consumption
- **GUD-005**: Use consistent error handling pattern: `{ ok: true; data: T } | { ok: false; error: string }`

### Patterns to Follow

- **PAT-001**: Base seeder extends abstract class with template method pattern
- **PAT-002**: DAL singleton instances for all database operations
- **PAT-003**: Server actions return ActionResult<T> type with revalidatePath
- **PAT-004**: Zod schemas with union types for multiple JSON format variants
- **PAT-005**: Transaction manager provides withTransaction<T> helper with rollback
- **PAT-006**: Batch processor with Promise.allSettled() for error isolation
- **PAT-007**: Progress tracker logs metrics every 50 items or 5 seconds
- **PAT-008**: Image strategy context injected into processors (dependency injection)

---

## 2. Implementation Steps

### Implementation Phase 1: Core Infrastructure & Types

**GOAL-001**: Establish type system, logger, data loader, and configuration foundation.

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-001 | Create `/src/scripts/seed/types.ts` with SeedOptions, SeedConfig, EntityResult, SeedReport, DTOs, ActionResult, ImageStrategyContext, BatchOperation, TransactionContext, LookupCache interfaces | ⭘ |  |
| TASK-002 | Create `/src/scripts/seed/logger.ts` with Logger class (info, success, warn, error, debug, section, progress, table methods); export singleton `logger` instance | ⭘ |  |
| TASK-003 | Create `/src/scripts/seed/dataLoader.ts` with DataLoader class supporting multi-file fallback (data.json → data1.json → data2.json); include cache Map; export singleton `dataLoader` instance | ⭘ |  |
| TASK-004 | Create `/src/scripts/seed/config.ts` with parseCliArgs() function and Commander.js argument parsing; validate env with Zod envSchema; support --batch-size, --concurrency, --verbose, --dry-run, --force, --transaction, --skip-validation, --image-strategy options | ⭘ |  |
| TASK-005 | Create directories: `/src/scripts/seed/seeders/`, `/src/scripts/seed/helpers/`, `/src/scripts/seed/database/`, `/src/scripts/seed/images/`, `/src/schemas/seed/` | ⭘ |  |
| TASK-006 | Run `pnpm type-check` to validate Phase 1 types; expect 0 errors | ⭘ |  |

**Acceptance Criteria:**

- ✅ All 4 core modules created with proper exports
- ✅ Logger produces colored output with chalk
- ✅ DataLoader caches loaded JSON arrays
- ✅ Config parser produces SeedConfig from process.argv
- ✅ All TypeScript files pass strict mode type checking
- ✅ 5 new directories created

---

### Implementation Phase 2: Validation Schemas with Zod

**GOAL-002**: Create seed-specific Zod schemas for user, comic, chapter entities with coercion and union types.

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-007 | Create `/src/schemas/seed/user.seed.ts` with userSeedSchema (array of objects): id (UUID, optional), email, name, password, role (enum: user/admin/moderator), image (URL nullable), emailVerified (coerce.date nullable), status (boolean default), createdAt/updatedAt/lastActivityDate (coerce.date) | ⭘ |  |
| TASK-008 | Create `/src/schemas/seed/comic.seed.ts` with comicSeedSchema (array): title, slug, description, url, rating (coerce.number 0-10), status (enum Title-Case), serialization, updatedAt (coerce.date), views (coerce.number), coverImage, type/author/artist (nested objects), genres (array), images (array with url property, optional defaults) | ⭘ |  |
| TASK-009 | Create `/src/schemas/seed/chapter.seed.ts` with chapterSeedSchema (array): url, name ("Chapter 273"), title (default "Untitled Chapter"), slug, chapterNumber (coerce.number), comic (object with title + slug), updatedAt/releaseDate (coerce.date), images (array, optional default []) | ⭘ |  |
| TASK-010 | Create `/src/schemas/seed/index.ts` exporting all three schemas and their inferred types (UserSeed, ComicSeed, ChapterSeed) | ⭘ |  |
| TASK-011 | Update `/src/scripts/seed/types.ts` to import and re-export seed types from schemas; ensure UserSeedDTO, ComicSeedDTO, ChapterSeedDTO align with Zod inferred types | ⭘ |  |
| TASK-012 | Run `pnpm type-check` to validate schemas; expect 0 errors | ⭘ |  |

**Acceptance Criteria:**

- ✅ 3 seed schemas created with proper Zod patterns (.coerce.date(), .pipe(), .union())
- ✅ Schemas handle both string and Date inputs for dates
- ✅ Status enum is Title-Case ("Ongoing", not "ongoing")
- ✅ Rating coerced to number with 0-10 range
- ✅ Optional fields use .default() or .optional().nullable()
- ✅ Schemas export TypeScript types via z.infer<>
- ✅ All 4 files pass type-check

---

### Implementation Phase 3: Logger & Batch Processing Utilities

**GOAL-003**: Implement progress tracking and batch processing with concurrency control.

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-013 | Create `/src/scripts/seed/helpers/progressTracker.ts` with ProgressTracker class: constructor(taskName, total); methods recordInsert/Update/Skip/Error(count); private maybeLog() logs every 50 items or 5s; complete() returns ProgressMetrics with duration, itemsPerSecond, successRate; uses chalk colors and ASCII progress bar | ⭘ |  |
| TASK-014 | Create `/src/scripts/seed/database/batchProcessor.ts` with BatchProcessor<T, R> class: constructor(options); process<U>(items[], processor, taskName?) returns { results, errors }; processBatchConcurrently handles concurrency limit; uses Promise.all with error isolation via catch | ⭘ |  |
| TASK-015 | Add to ProgressTracker: createBar(current, total) private method returns ASCII bar (█░ chars); logProgress() logs percentage, counts, speed, duration with chalk colors | ⭘ |  |
| TASK-016 | Add to BatchProcessor: onBatchComplete callback support; onError callback for per-item errors; Sequential batch processing, concurrent item processing | ⭘ |  |
| TASK-017 | Test ProgressTracker with sample data: 100 items, log output at 50, 100; verify bar display and metrics | ⭘ |  |
| TASK-018 | Test BatchProcessor concurrency: 20 items with concurrency=3, batchSize=5; verify parallel execution | ⭘ |  |

**Acceptance Criteria:**

- ✅ ProgressTracker logs every 50 items or 5 seconds
- ✅ Progress bars display with █░ characters and percentage
- ✅ Metrics calculated: inserted, updated, skipped, errors, duration, itemsPerSecond, successRate
- ✅ BatchProcessor processes batches sequentially, items concurrently
- ✅ Promise.allSettled() prevents one failure from stopping batch
- ✅ Callbacks optional and async-safe

---

### Implementation Phase 4: Base Seeder Abstract Class

**GOAL-004**: Implement abstract base seeder with template method pattern and shared logic.

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-019 | Create `/src/scripts/seed/seeders/baseSeed.ts` with abstract BaseSeeder<T> class: constructor(entityName, schema, cache); abstract methods getDataSources(), getUniqueField(), transformData(), insertBatch(); concrete seed() orchestration method | ⭘ |  |
| TASK-020 | Implement BaseSeeder.seed(): load data (loadData()), validate (validateData() with Zod), check dry-run, call insertBatch(), return EntityResult; add logging sections for each step | ⭘ |  |
| TASK-021 | Implement BaseSeeder.loadData(): iterate getDataSources(), load via dataLoader, concatenate arrays, log record counts | ⭘ |  |
| TASK-022 | Implement BaseSeeder.validateData(): loop items, parse with schema, catch errors, return only valid; silence validation errors in debug unless --verbose | ⭘ |  |
| TASK-023 | Implement BaseSeeder.processBatches(): use BatchProcessor, aggregate EntityResult across batches, handle errors field | ⭘ |  |
| TASK-024 | Add to BaseSeeder: protected `dependencies: string[] = []` field for seeding order (e.g., authors before comics) | ⭘ |  |

**Acceptance Criteria:**

- ✅ Seed orchestration handles load → validate → dry-run check → insert
- ✅ Validation skipped when --skip-validation flag set
- ✅ Dry-run returns inserted count but doesn't persist
- ✅ Error handling logs details without stopping
- ✅ Entity name logged in section headers
- ✅ All abstract methods required in child classes

---

### Implementation Phase 5: Transaction Manager & Conflict Resolver

**GOAL-005**: Implement database transaction and upsert logic.

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-025 | Create `/src/scripts/seed/database/transactionManager.ts` with TransactionManager class; static withTransaction<T>(entityName, options, operation) that wraps in db.transaction() if options.useTransaction=true; logs start/commit/rollback | ⭘ |  |
| TASK-026 | Implement withTransaction error handling: catch and log with entity name; re-throw for orchestrator handling | ⭘ |  |
| TASK-027 | Create `/src/scripts/seed/database/conflictResolver.ts` with logic for onConflictDoUpdate pattern; support forceOverwrite flag behavior (skip vs. update); prepare upsert-friendly data structures | ⭘ |  |
| TASK-028 | Add to TransactionManager: support nested transactions via Drizzle's transaction API | ⭘ |  |

**Acceptance Criteria:**

- ✅ Transactions wrap entire seeder operations
- ✅ Automatic rollback on error
- ✅ Optional transaction toggle via --no-transaction flag
- ✅ onConflictDoUpdate used for all inserts
- ✅ forceOverwrite flag triggers update on conflict vs. skip

---

### Implementation Phase 6: Image Handling Strategy Pattern

**GOAL-006**: Implement three-mode image handling strategy (local, URLs, ImageKit).

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-029 | Create `/src/scripts/seed/images/imageDownloader.ts` with ImageDownloader class: download(url, entityType, entityId) returns ImageDownloadResult; retry logic (3 attempts, exponential backoff); cache check (skipIfExists); local filesystem storage | ⭘ |  |
| TASK-030 | Create `/src/scripts/seed/images/imageKitUploader.ts` with ImageKitUploader class: upload(url, entityType, entityId) returns upload result with fileUrl; handles ImageKit client initialization | ⭘ |  |
| TASK-031 | Create `/src/scripts/seed/images/imageStrategy.ts` with ImageStrategy class: constructor(ImageStrategyContext); processImage(url, entityType, entityId) dispatches to downloader/uploader/return-url based on mode; batchProcess(urls[], entityType, entityId, concurrency) handles parallel processing | ⭘ |  |
| TASK-032 | Add ImageDownloader: exponential backoff retry with 1s × attempt delays; User-Agent header for HTTP requests; file stat check for cache hits | ⭘ |  |
| TASK-033 | Add ImageStrategy: mode="urls" returns original URL unchanged; mode="local" downloads to ./public/comics/; mode="imagekit" uploads and returns CDN URL | ⭘ |  |

**Acceptance Criteria:**

- ✅ Three modes fully functional and switchable
- ✅ Local downloads cache checked before re-downloading
- ✅ Retry logic with exponential backoff
- ✅ Batch processing respects concurrency limit
- ✅ Error handling returns { success: false; error: string }

---

### Implementation Phase 7: Creator Name Resolution & Helper Functions

**GOAL-007**: Implement author/artist name splitting, deduplication, genre/type resolution.

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-034 | Create `/src/scripts/seed/helpers/creatorNameResolver.ts` with functions: splitCreators(input: "A/B/C") returns string[]; normalizeCreatorName(name) trims and lowercases; lookupOrCreateAuthor/Artist (name, cache, dal) with dedup logic | ⭘ |  |
| TASK-035 | Create `/src/scripts/seed/helpers/dateParser.ts` with parseDate(dateStr: "August 14th 2025") returns Date; handle ISO-8601 fallback; return null on unparseable | ⭘ |  |
| TASK-036 | Create `/src/scripts/seed/helpers/chapterNumberExtractor.ts` with extractChapterNumber(name: "Chapter 273") returns number via /Chapter\s+(\d+)/i regex; return null if no match | ⭘ |  |
| TASK-037 | Test creatorNameResolver: "Redice Studio/Indestructible" → ["Redice Studio", "Indestructible"]; "\_" → ["Unknown"]; "Single Name" → ["Single Name"] | ⭘ |  |
| TASK-038 | Test dateParser: "August 14th 2025" → Date object; handle ISO-8601; null on invalid | ⭘ |  |
| TASK-039 | Test chapterNumberExtractor: "Chapter 273" → 273; "Ch. 10" → null; "273" → null (requires "Chapter" prefix) | ⭘ |  |

**Acceptance Criteria:**

- ✅ Creator names split on "/" correctly
- ✅ "\_" replaced with "Unknown"
- ✅ Dates parsed from multiple formats
- ✅ Chapter numbers extracted via regex with proper matching
- ✅ All helpers have unit test coverage

---

### Implementation Phase 8: Specific Entity Seeders

**GOAL-008**: Implement seeders for types, authors, artists, genres (no JSON dependencies); then comics and chapters (with relations).

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-040 | Create `/src/scripts/seed/seeders/typeSeeder.ts`: extends BaseSeeder; seeds predefined types ["Manga", "Manhwa", "Manhua", "Web Comic", "Light Novel"]; getDataSources() returns []; insertBatch uses typeDal.create() or Drizzle insert with onConflictDoUpdate | ⭘ |  |
| TASK-041 | Create `/src/scripts/seed/seeders/authorSeeder.ts`: extends BaseSeeder; getDataSources() ["author.json"]; supports dedup cache; lookupOrCreateAuthor for name resolution; insertBatch calls authorDal.create(); caches author.id → name mapping | ⭘ |  |
| TASK-042 | Create `/src/scripts/seed/seeders/artistSeeder.ts`: mirrors authorSeeder for artists; caches artist.id → name mapping | ⭘ |  |
| TASK-043 | Create `/src/scripts/seed/seeders/genreSeeder.ts`: getDataSources() ["genre.json"] (or auto-extract from comics); insertBatch calls genreDal.create(); caches genre.id → name | ⭘ |  |
| TASK-044 | Create `/src/scripts/seed/seeders/comicSeeder.ts`: extends BaseSeeder; getDataSources() ["comic.json", "comic-data1.json", "comic-data2.json"]; transformData resolves author/artist/type/genres to IDs via cache; handles images (first as coverImage, rest to comicImage table); calls comicDal.create() | ⭘ |  |
| TASK-045 | Create `/src/scripts/seed/seeders/chapterSeeder.ts`: extends BaseSeeder; getDataSources() ["chapter.json", "chapter-data1.json", "chapter-data2.json"]; resolves comic.slug → comicId via cache; extracts chapterNumber from name; calls chapterDal.create(); insertBatch creates chapterImage records with pageNumber | ⭘ |  |
| TASK-046 | Add to ComicSeeder.transformData: strip HTML tags from description; parse rating string to number; coerce status to Title-Case; handle "\_" author/artist via "Unknown" placeholder | ⭘ |  |
| TASK-047 | Add to ChapterSeeder.transformData: extract chapter number via regex; handle missing images array; validate comic reference resolves | ⭘ |  |

**Acceptance Criteria:**

- ✅ 6 seeders created; all extend BaseSeeder
- ✅ Type seeder doesn't load JSON (predefined)
- ✅ Author/Artist seeders cache results for comics/chapters link
- ✅ Comic seeder resolves relations and handles images
- ✅ Chapter seeder extracts chapter numbers and links images
- ✅ All seeders use correct DAL singletons

---

### Implementation Phase 9: Seed Orchestrator & CLI

**GOAL-009**: Orchestrate seeding execution order, handle dependencies, implement CLI entry point.

| Task | Description | Completed | Date |
| --- | --- | --- | --- | --- |
| TASK-048 | Create `/src/scripts/seed/seedOrchestrator.ts` with SeedOrchestrator class: constructor(config: SeedConfig); execute() method orchestrates seeding in dependency order (types → authors/artists → genres → comics → chapters → users); returns SeedReport | ⭘ |  |
| TASK-049 | Implement SeedOrchestrator.execute(): create LookupCache instance; seed types, authors, artists, genres sequentially; seed comics, chapters with cache; aggregate EntityResult into SeedReport with timestamp, totalDuration, success, warnings, errors | ⭘ |  |
| TASK-050 | Add to SeedOrchestrator: validate() method for dry-run; supports verbose logging per config.options.verbose | ⭘ |  |
| TASK-051 | Create `/src/scripts/seed/run.ts` as CLI entry point: call parseCliArgs() → create SeedOrchestrator → await execute() → log results → process.exit(0 | 1) | ⭘ |  |
| TASK-052 | Add npm scripts to package.json: "seed", "seed:users", "seed:comics", "seed:chapters", "seed:clear", "seed:reset", "seed:validate"; all use `tsx src/scripts/seed/run.ts [options]` | ⭘ |  |
| TASK-053 | Handle seeding order: types (0 deps) → authors/artists (0 deps) → genres (0 deps) → comics (depends on type/author/artist/genre) → chapters (depends on comic) → users (0 deps) | ⭘ |  |
| TASK-054 | Implement SeedReport aggregation: sum inserted/updated/skipped/errors across all seeders; track duration per entity; collect warnings/errors for final report | ⭘ |  |

**Acceptance Criteria:**

- ✅ Seeding order respects FK dependencies
- ✅ LookupCache shared across all seeders
- ✅ SeedReport includes all metrics
- ✅ CLI entry point executable via tsx
- ✅ npm scripts added to package.json
- ✅ Verbose logging toggleable

---

### Implementation Phase 10: RESTful API Route

**GOAL-010**: Implement HTTP endpoints for seeding (GET, POST, DELETE, PUT, PATCH).

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-055 | Create `/src/app/api/seed/route.ts` with GET handler: dry-run validation; returns { ok: true; message }; no auth required for validation | ⭘ |  |
| TASK-056 | Implement POST handler: parse body { entities, options }; call SeedOrchestrator.execute(); return SeedReport; admin auth required (or dev bypass) | ⭘ |  |
| TASK-057 | Implement DELETE handler: clear all seeded data; admin auth required; returns { ok: true; message: "All data cleared" } | ⭘ |  |
| TASK-058 | Implement PUT handler: reset (delete all + reseed); admin auth required; orchestrates DELETE then POST | ⭘ |  |
| TASK-059 | Implement PATCH handler: upsert with forceOverwrite=true; admin auth required; returns SeedReport | ⭘ |  |
| TASK-060 | Add isAuthorized(request) helper: check NODE_ENV === "development" (allow all in dev); check NextAuth session user.role === "admin" in production; return 401 if unauthorized | ⭘ |  |
| TASK-061 | Add error handlers: 400 for validation errors, 401 for auth, 500 for server errors; return consistent SeedApiResponse format ({ ok, message, data/error, code }) | ⭘ |  |
| TASK-062 | Add request logging: log all seed API calls (method, entity, options) without sensitive data (passwords, tokens) | ⭘ |  |

**Acceptance Criteria:**

- ✅ All 5 HTTP methods (GET, POST, DELETE, PUT, PATCH) implemented
- ✅ Auth check enforced (admin role required in production)
- ✅ Dev mode allows all requests
- ✅ Response format consistent (ok, message, data/error, code)
- ✅ Error codes meaningful (400, 401, 500)
- ✅ No sensitive data logged

---

### Implementation Phase 11: Integration & Testing

**GOAL-011**: Validate all components work together; test API endpoints; test CLI commands.

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-063 | Run `pnpm type-check` on all new files; expect 0 errors | ⭘ |  |
| TASK-064 | Run `pnpm lint:fix` on all new files; ensure ESLint passes | ⭘ |  |
| TASK-065 | Test CLI: `pnpm seed --dry-run --verbose` on local machine; validates but doesn't insert | ⭘ |  |
| TASK-066 | Test CLI: `pnpm seed types` seeding only types; verify cache population | ⭘ |  |
| TASK-067 | Test CLI: `pnpm seed comics --batch-size=50` with smaller batches; verify performance | ⭘ |  |
| TASK-068 | Test API: GET /api/seed (validation); expect 200 OK with validation summary | ⭘ |  |
| TASK-069 | Test API: POST /api/seed { entities: "all" }; expect 200 OK with SeedReport | ⭘ |  |
| TASK-070 | Test API: POST /api/seed without auth; expect 401 Unauthorized (in production) | ⭘ |  |
| TASK-071 | Test API: PATCH /api/seed { entities: "comics" }; expect upsert with forceOverwrite behavior | ⭘ |  |
| TASK-072 | Database validation: query counts (users, comics, chapters, authors, artists, genres); verify expected totals | ⭘ |  |
| TASK-073 | Verify FK integrity: no NULL authorId in comics (unless handling "Unknown"); no FK orphans | ⭘ |  |
| TASK-074 | Test dry-run mode: `pnpm seed --dry-run` validates without inserting; check database unchanged | ⭘ |  |

**Acceptance Criteria:**

- ✅ All CLI commands execute without errors
- ✅ API endpoints respond with correct status codes
- ✅ Database records inserted with correct counts
- ✅ FK relationships intact (no orphans)
- ✅ Progress logging displays during long operations
- ✅ Dry-run doesn't modify database
- ✅ Type-check: 0 errors
- ✅ Lint-check: 0 errors

---

### Implementation Phase 12: Documentation & Final Validation

**GOAL-012**: Document system usage, parameters, troubleshooting; validate all requirements met.

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-075 | Create `/docs/SEEDING_GUIDE.md`: overview, CLI usage examples, API usage examples, options documentation, troubleshooting | ⭘ |  |
| TASK-076 | Create `/src/scripts/seed/README.md`: architecture overview, file descriptions, seeder dependency diagram, image strategy modes, caching behavior | ⭘ |  |
| TASK-077 | Add TSDoc comments to all classes, methods, interfaces; document params, returns, throws | ⭘ |  |
| TASK-078 | Add inline comments for complex logic: creator name splitting, chapter number extraction, date parsing, transaction management | ⭘ |  |
| TASK-079 | Create `/IMPLEMENTATION_NOTES.md`: decisions made, alternatives considered, performance characteristics, scaling considerations | ⭘ |  |
| TASK-080 | Validate REQ-001 to REQ-019: checklist each requirement met; document evidence | ⭘ |  |
| TASK-081 | Validate SEC-001 to SEC-003: security requirements met; no sensitive data logged | ⭘ |  |
| TASK-082 | Final type-check: `pnpm type-check` zero errors | ⭘ |  |
| TASK-083 | Final lint: `pnpm lint:fix` all files comply | ⭘ |  |

**Acceptance Criteria:**

- ✅ All requirements (REQ-, SEC-, CON-, GUD-, PAT-) documented as met/satisfied
- ✅ User documentation complete with examples
- ✅ Architecture documentation explains design decisions
- ✅ TSDoc comments complete and accurate
- ✅ No outstanding code quality issues
- ✅ Ready for production deployment

---

## 3. Alternatives

- **ALT-001**: Use simple CSV loaders instead of JSON fallback pattern → rejected because JSON supports complex nested relations (author, artist, genres); CSV flat columnar structure insufficient
- **ALT-002**: Image strategy hardcoded to URLs-only mode → rejected because local caching useful for development; ImageKit required for production CDN; flexibility via config superior
- **ALT-003**: Single global transaction for entire seed → rejected because per-entity transactions allow partial success (e.g., comics inserted if users fails); better error isolation and recovery
- **ALT-004**: Automatic retry with exponential backoff for failed batches → rejected because explicit logging preferred; allows user decision on retry vs. skip; prevents infinite loops
- **ALT-005**: Use raw Drizzle queries instead of DAL singletons → rejected because DAL provides abstraction, caching, consistent error handling; reusable across seed & application code
- **ALT-006**: CLI only, no API endpoints → rejected because API enables programmatic seeding (CI/CD, admin dashboards, remote triggers); both modes provide flexibility

---

## 4. Dependencies

### Package Dependencies

- **DEP-001**: `commander` v11+ (CLI argument parsing; already in refs/comicwise)
- **DEP-002**: `chalk` v5+ (colored terminal output; already in refs/comicwise)
- **DEP-003**: `zod` v3+ (schema validation; **already in project**)
- **DEP-004**: `drizzle-orm` v0.45+ (database access; **already in project**)
- **DEP-005**: `drizzle-kit` v0.45+ (migrations; **already in project**)
- **DEP-006**: `next` v16+ (Next.js framework; **already in project**)
- **DEP-007**: `next-auth` v5+ (authentication; **already in project**)

### Database Dependencies

- **DEP-008**: PostgreSQL 14+ (Neon provider; **already deployed**)
- **DEP-009**: Tables: user, type, author, artist, genre, comic, chapter, comicImage, chapterImage, comicToGenre (all **already in schema.ts**)

### Code Dependencies (Already Exist)

- **DEP-010**: `/src/database/db.ts` (Drizzle singleton)
- **DEP-011**: `/src/database/schema.ts` (30+ table definitions)
- **DEP-012**: `/src/auth.ts` and `@/auth` exports (NextAuth session management)
- **DEP-013**: `/src/lib/env.ts` (Zod-validated env vars)

### Files to Create Dependencies

- **DEP-014**: `/src/scripts/seed/types.ts` (types for all seeders)
- **DEP-015**: `/src/scripts/seed/logger.ts` (logging throughout system)
- **DEP-016**: `/src/schemas/seed/` (Zod schemas for validation)

---

## 5. Files

### New Files

- **FILE-001**: [src/scripts/seed/types.ts](src/scripts/seed/types.ts) - 200+ lines; SeedOptions, SeedConfig, EntityResult, SeedReport, userDTO/comicDTO/chapterDTO interfaces
- **FILE-002**: [src/scripts/seed/logger.ts](src/scripts/seed/logger.ts) - 80 lines; Logger class with colors
- **FILE-003**: [src/scripts/seed/config.ts](src/scripts/seed/config.ts) - 120 lines; Commander.js CLI parsing + Zod env validation
- **FILE-004**: [src/scripts/seed/dataLoader.ts](src/scripts/seed/dataLoader.ts) - 100 lines; JSON multi-file fallback loader
- **FILE-005**: [src/scripts/seed/helpers/progressTracker.ts](src/scripts/seed/helpers/progressTracker.ts) - 150 lines; metrics tracking
- **FILE-006**: [src/scripts/seed/helpers/creatorNameResolver.ts](src/scripts/seed/helpers/creatorNameResolver.ts) - 80 lines; name splitting + dedup
- **FILE-007**: [src/scripts/seed/helpers/dateParser.ts](src/scripts/seed/helpers/dateParser.ts) - 40 lines; flexible date parsing
- **FILE-008**: [src/scripts/seed/helpers/chapterNumberExtractor.ts](src/scripts/seed/helpers/chapterNumberExtractor.ts) - 30 lines; regex chapter extraction
- **FILE-009**: [src/scripts/seed/database/batchProcessor.ts](src/scripts/seed/database/batchProcessor.ts) - 120 lines; concurrent batching with Promise.allSettled
- **FILE-010**: [src/scripts/seed/database/transactionManager.ts](src/scripts/seed/database/transactionManager.ts) - 40 lines; Drizzle transaction wrapper
- **FILE-011**: [src/scripts/seed/database/conflictResolver.ts](src/scripts/seed/database/conflictResolver.ts) - 50 lines; onConflictDoUpdate patterns
- **FILE-012**: [src/scripts/seed/seeders/baseSeed.ts](src/scripts/seed/seeders/baseSeed.ts) - 180 lines; abstract base with template method
- **FILE-013**: [src/scripts/seed/seeders/typeSeeder.ts](src/scripts/seed/seeders/typeSeeder.ts) - 80 lines; predefined types
- **FILE-014**: [src/scripts/seed/seeders/authorSeeder.ts](src/scripts/seed/seeders/authorSeeder.ts) - 100 lines; author JSON → DB with cache
- **FILE-015**: [src/scripts/seed/seeders/artistSeeder.ts](src/scripts/seed/seeders/artistSeeder.ts) - 100 lines; artist seeder (mirrors author)
- **FILE-016**: [src/scripts/seed/seeders/genreSeeder.ts](src/scripts/seed/seeders/genreSeeder.ts) - 100 lines; genre seeder
- **FILE-017**: [src/scripts/seed/seeders/comicSeeder.ts](src/scripts/seed/seeders/comicSeeder.ts) - 250 lines; complex comic + image batching + relations
- **FILE-018**: [src/scripts/seed/seeders/chapterSeeder.ts](src/scripts/seed/seeders/chapterSeeder.ts) - 200 lines; chapter + chapterImage + number extraction
- **FILE-019**: [src/scripts/seed/images/imageDownloader.ts](src/scripts/seed/images/imageDownloader.ts) - 150 lines; local file cache + retries
- **FILE-020**: [src/scripts/seed/images/imageKitUploader.ts](src/scripts/seed/images/imageKitUploader.ts) - 80 lines; ImageKit client wrapper
- **FILE-021**: [src/scripts/seed/images/imageStrategy.ts](src/scripts/seed/images/imageStrategy.ts) - 100 lines; strategy pattern dispatcher
- **FILE-022**: [src/scripts/seed/seedOrchestrator.ts](src/scripts/seed/seedOrchestrator.ts) - 180 lines; orchestrate seeding order + dependency management
- **FILE-023**: [src/scripts/seed/run.ts](src/scripts/seed/run.ts) - 30 lines; CLI entry point with main()
- **FILE-024**: [src/scripts/seed/index.ts](src/scripts/seed/index.ts) - 20 lines; seeder exports for API
- **FILE-025**: [src/app/api/seed/route.ts](src/app/api/seed/route.ts) - 200 lines; REST API (GET, POST, DELETE, PUT, PATCH)
- **FILE-026**: [src/schemas/seed/user.seed.ts](src/schemas/seed/user.seed.ts) - 30 lines; Zod user schema
- **FILE-027**: [src/schemas/seed/comic.seed.ts](src/schemas/seed/comic.seed.ts) - 40 lines; Zod comic schema
- **FILE-028**: [src/schemas/seed/chapter.seed.ts](src/schemas/seed/chapter.seed.ts) - 35 lines; Zod chapter schema
- **FILE-029**: [src/schemas/seed/index.ts](src/schemas/seed/index.ts) - 10 lines; schema exports

### Modified Files

- **FILE-030**: [package.json](package.json) - add 7 npm seed scripts (seed, seed:users, seed:comics, etc.)
- **FILE-031**: [tsconfig.json](tsconfig.json) - verify path aliases include @/\* and module resolution correct
- **.env.local** (no changes; uses existing DATABASE*URL, NODE_ENV, optional IMAGEKIT*\* vars)

### Total New Lines: ~3,000 lines of code

---

## 6. Testing

### Unit Tests

- **TEST-001**: ProgressTracker.recordInsert/Update/Skip/Error() increments counters correctly
- **TEST-002**: ProgressTracker.maybeLog() fires at 50-item boundary and 5-second interval
- **TEST-003**: ProgressTracker.complete() returns correct ProgressMetrics with calculated rates
- **TEST-004**: BatchProcessor.process() executes items concurrently with respecting concurrency limit
- **TEST-005**: BatchProcessor error handling via Promise.allSettled() prevents batch failure from stopping
- **TEST-006**: DataLoader.load() caches results; second call returns cached copy
- **TEST-007**: DataLoader.loadWithFallback() tries all candidates in order
- **TEST-008**: Logger.info/success/warn/error output correct chalk colors
- **TEST-009**: CreatorNameResolver.splitCreators() "A/B/C" → ["A", "B", "C"]
- **TEST-010**: CreatorNameResolver.splitCreators() "\_" → ["Unknown"]
- **TEST-011**: DateParser.parseDate() "August 14th 2025" → valid Date object
- **TEST-012**: DateParser.parseDate() ISO-8601 → valid Date object
- **TEST-013**: ChapterNumberExtractor.extract() "Chapter 273" → 273
- **TEST-014**: ChapterNumberExtractor.extract() "Ch. 273" → null (regex doesn't match)
- **TEST-015**: BaseSeeder.seed() loads → validates → returns EntityResult even with errors
- **TEST-016**: BaseSeeder calls insertBatch() only if not dry-run
- **TEST-017**: TypeSeeder seeds predefined types without JSON loading
- **TEST-018**: AuthorSeeder caches author IDs for comic linking
- **TEST-019**: ComicSeeder resolves author/artist/type/genre IDs from cache
- **TEST-020**: ComicSeeder handles images: first→coverImage, rest→comicImage table
- **TEST-021**: ChapterSeeder extracts chapter numbers and links images
- **TEST-022**: SeedOrchestrator.execute() respects dependency order
- **TEST-023**: SeedOrchestrator aggregates EntityResult across seeders

### Integration Tests

- **TEST-024**: Full CLI seed (dry-run): `pnpm seed types --dry-run` validates without inserting
- **TEST-025**: Full CLI seed (all): `pnpm seed` inserts all entities in correct order
- **TEST-026**: Full API POST /api/seed with body { entities: "all" } inserts and returns SeedReport
- **TEST-027**: API GET /api/seed returns validation summary (200 OK)
- **TEST-028**: API auth check: unauthenticated POST returns 401 in production
- **TEST-029**: Database integrity: FK constraints verified; no orphaned records
- **TEST-030**: Database counts: ~2100 comics, ~50000 chapters, 5 types, 4 users inserted
- **TEST-031**: Dry-run mode: database unchanged after `--dry-run`
- **TEST-032**: Force-overwrite: PATCH /api/seed updates existing records instead of skipping
- **TEST-033**: Image strategy modes: --image-strategy=urls|local|imagekit all work
- **TEST-034**: Concurrent batching: batch-size=50, concurrency=5 processes efficiently

### Output Tests

- **TEST-035**: Progress logging at 50-item intervals and 5-second intervals displays correctly
- **TEST-036**: Final SeedReport includes all metrics (inserted, updated, skipped, errors, duration)
- **TEST-037**: Error messages are descriptive (validation errors, FK violations, network timeouts)
- **TEST-038**: Verbose flag (`--verbose`) outputs debug logs; without flag, silent
- **TEST-039**: Success exit code (0) on successful seeding
- **TEST-040**: Error exit code (1) on failures

---

## 7. Risks & Assumptions

### Risks

- **RISK-001**: Large dataset (50,000 chapters): memory consumption during batching; mitigated by configurable batch size and streaming approach
- **RISK-002**: Author/artist name deduplication: fuzzy matching may create duplicates if names differ slightly ("Redice" vs "Redice Studio"); mitigated by case-insensitive normalization and name splitting
- **RISK-003**: Image download failures: network timeouts, 404s, rate limiting; mitigated by retry logic with exponential backoff
- **RISK-004**: Transaction locks on large writes: long-running transactions may block reads; mitigated by per-entity transactions (not single global transaction)
- **RISK-005**: FK constraint violations: parent records missing when chapter seeded before comic; mitigated by seeding order (types → authors → comics → chapters)
- **RISK-006**: Date format parsing edge cases: "January 1st" vs "1st January" vs numeric; mitigated by multiple parse attempts + null fallback
- **RISK-007**: API concurrency: multiple simultaneous seeding requests may exceed DB connection pool; mitigated by connection pooling config + rate limiting documentation
- **RISK-008**: Drizzle transaction API changes: future version compatibility; mitigated by wrapping in TransactionManager abstraction

### Assumptions

- **ASSUMPTION-001**: JSON data in `/src/data/` remains valid during seeding; no external modifications
- **ASSUMPTION-002**: Database connection pool has sufficient capacity for seeding concurrency
- **ASSUMPTION-003**: DAL singleton instances (`authorDal`, `comicDal`, etc.) are properly initialized before seeders run
- **ASSUMPTION-004**: Image URLs in JSON remain accessible and don't require authentication
- **ASSUMPTION-005**: Drizzle ORM v0.45+ available; syntax matches examples in this plan
- **ASSUMPTION-006**: PostgreSQL supports `onConflict` clause (supported in v12+)
- **ASSUMPTION-007**: NextAuth session includes `user.role` field for admin check
- **ASSUMPTION-008**: Zod v3+ installed; `.pipe()` and `.coerce` methods available
- **ASSUMPTION-009**: Commander.js v11+ installed and API matches examples
- **ASSUMPTION-010**: No custom database-level triggers or constraints conflict with seeding logic

---

## 8. Related Specifications / Further Reading

- [ComicWise Copilot Instructions](.github/copilot-instructions.md) - Project-specific conventions, DAL patterns, server actions
- [Next.js App Router Guidelines](.github/instructions/nextjs.instructions.md) - Server components, layouts, error handling
- [TypeScript Development Guidelines](.github/instructions/typescript.instructions.md) - Strict mode, interfaces, error handling
- [Security Best Practices](.github/instructions/security.instructions.md) - Auth, validation, data protection
- [Database Schema Reference](src/database/schema.ts) - Full table definitions, relationships, enums (604 lines)
- [Reference Project: ComicWise v3 Seed Runner](.references/comicwise/src/database/seed/seed-runner-v3.ts) - Inspiration for CLI + batching patterns
- [Reference Project: BookWise Data Seeding](.references/bookwise/database/seed.ts) - Simpler seed pattern with ImageKit integration
- [Reference Project: ComicR DAL Pattern](.references/comicr/src/dal/base-dal.ts) - Abstract base class pattern for data access

---

## 9. Code Samples & Implementation References

### Core Types (`src/scripts/seed/types.ts`)

```typescript
// TypeScript interfaces for the seeding system
export interface SeedOptions {
  verbose?: boolean;
  dryRun?: boolean;
  skipValidation?: boolean;
  useTransaction?: boolean;
  batchSize?: number;
  concurrency?: number;
  imageStrategy?: "urls" | "local" | "imagekit";
  forceOverwrite?: boolean;
}

export interface SeedConfig {
  entities: (
    | "types"
    | "authors"
    | "artists"
    | "genres"
    | "comics"
    | "chapters"
    | "users"
    | "all"
  )[];
  options: SeedOptions;
  timestamp: Date;
}

export interface EntityResult {
  entityName: string;
  inserted: number;
  updated: number;
  skipped: number;
  errors: SeedError[];
  duration: number;
  success: boolean;
}

export interface SeedReport {
  timestamp: Date;
  success: boolean;
  totalDuration: number;
  results: EntityResult[];
  warnings: string[];
  errors: string[];
  summary: {
    totalInserted: number;
    totalUpdated: number;
    totalSkipped: number;
    totalErrors: number;
  };
}

export interface SeedError {
  itemIndex: number;
  value: unknown;
  message: string;
}

export type ActionResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string };

export interface LookupCache {
  authors: Map<string, { id: string; name: string }>;
  artists: Map<string, { id: string; name: string }>;
  types: Map<string, string>; // name → id
  genres: Map<string, string>;
  comics: Map<string, string>; // slug → id
}
```

### Logger Implementation (`src/scripts/seed/logger.ts`)

```typescript
import chalk from "chalk";

export class Logger {
  private verbose: boolean = false;

  constructor(verbose: boolean = false) {
    this.verbose = verbose;
  }

  info(message: string): void {
    console.log(chalk.blue("ℹ"), message);
  }

  success(message: string): void {
    console.log(chalk.green("✓"), message);
  }

  warn(message: string): void {
    console.log(chalk.yellow("⚠"), message);
  }

  error(message: string): void {
    console.log(chalk.red("✗"), message);
  }

  debug(message: string): void {
    if (this.verbose) {
      console.log(chalk.gray("➤"), message);
    }
  }

  section(title: string): void {
    console.log("\n" + chalk.cyan.bold("━".repeat(50)));
    console.log(chalk.cyan.bold(`  ${title}`));
    console.log(chalk.cyan.bold("━".repeat(50)) + "\n");
  }

  progress(message: string): void {
    console.log(chalk.white("→"), message);
  }

  table(data: Record<string, unknown>[]): void {
    console.table(data);
  }
}

export const logger = new Logger();
```

### Zod Schema Example (`src/schemas/seed/user.seed.ts`)

```typescript
import { z } from "zod";

export const userSeedSchema = z.array(
  z.object({
    id: z.string().uuid().optional(),
    email: z.string().email(),
    name: z.string().min(1),
    password: z.string().min(6),
    role: z.enum(["user", "admin", "moderator"]).default("user"),
    image: z.string().url().nullable().optional(),
    emailVerified: z.coerce.date().nullable().optional(),
    status: z.boolean().default(true),
    createdAt: z.coerce.date().default(() => new Date()),
    updatedAt: z.coerce.date().default(() => new Date()),
    lastActivityDate: z.coerce.date().nullable().optional()
  })
);

export type UserSeed = z.infer<typeof userSeedSchema>;
```

### Comic Schema Example (`src/schemas/seed/comic.seed.ts`)

```typescript
import { z } from "zod";

const comicStatusEnum = z.enum([
  "Ongoing",
  "Completed",
  "Hiatus",
  "Dropped",
  "Season End",
  "Coming Soon"
]);

export const comicSeedSchema = z.array(
  z.object({
    title: z.string().min(1),
    slug: z.string().min(1),
    description: z.string().optional(),
    url: z.string().url().optional(),
    rating: z.coerce.number().min(0).max(10).default(0),
    status: comicStatusEnum.default("Ongoing"),
    serialization: z.string().optional(),
    updatedAt: z.coerce.date().default(() => new Date()),
    views: z.coerce.number().default(0),
    coverImage: z.string().url().nullable(),
    type: z
      .object({
        name: z.string()
      })
      .optional(),
    author: z
      .object({
        name: z.string()
      })
      .nullable()
      .optional(),
    artist: z
      .object({
        name: z.string()
      })
      .nullable()
      .optional(),
    genres: z
      .array(
        z.object({
          name: z.string()
        })
      )
      .default([]),
    images: z
      .array(
        z.object({
          url: z.string().url()
        })
      )
      .default([])
  })
);

export type ComicSeed = z.infer<typeof comicSeedSchema>;
```

### DataLoader Implementation (`src/scripts/seed/dataLoader.ts`)

```typescript
import fs from "fs/promises";
import path from "path";
import { Logger } from "./logger";

export class DataLoader {
  private cache = new Map<string, unknown[]>();
  private logger: Logger;

  constructor(logger: Logger) {
    this.logger = logger;
  }

  async loadWithFallback<T>(baseFileName: string): Promise<T[]> {
    const cacheKey = baseFileName;
    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey) as T[];
    }

    const candidates = [
      `${baseFileName}.json`,
      `${baseFileName}-data1.json`,
      `${baseFileName}-data2.json`
    ];

    for (const candidate of candidates) {
      const filePath = path.join(
        process.cwd(),
        "src/data",
        candidate
      );
      try {
        const content = await fs.readFile(filePath, "utf-8");
        const data = JSON.parse(content) as T[];
        this.cache.set(cacheKey, data);
        this.logger.success(
          `Loaded ${data.length} records from ${candidate}`
        );
        return data;
      } catch (error) {
        this.logger.debug(
          `Failed to load ${candidate}, trying next...`
        );
      }
    }

    throw new Error(`No data file found for ${baseFileName}`);
  }

  clearCache(): void {
    this.cache.clear();
  }
}
```

### BaseSeeder Abstract Class Pattern (`src/scripts/seed/seeders/baseSeed.ts`)

```typescript
import { z } from "zod";
import { Logger } from "../logger";
import { EntityResult, LookupCache, SeedOptions } from "../types";

export abstract class BaseSeeder<T> {
  protected entityName: string;
  protected schema: z.ZodType;
  protected cache: LookupCache;
  protected logger: Logger;
  protected options: SeedOptions;
  protected dependencies: string[] = [];

  constructor(
    entityName: string,
    schema: z.ZodType,
    cache: LookupCache,
    logger: Logger,
    options: SeedOptions
  ) {
    this.entityName = entityName;
    this.schema = schema;
    this.cache = cache;
    this.logger = logger;
    this.options = options;
  }

  // Template method pattern
  async seed(): Promise<EntityResult> {
    this.logger.section(`Seeding ${this.entityName}`);

    try {
      const data = await this.loadData();
      const validated = await this.validateData(data);

      if (this.options.dryRun) {
        this.logger.warn("DRY RUN: No data will be persisted");
        return {
          entityName: this.entityName,
          inserted: validated.length,
          updated: 0,
          skipped: 0,
          errors: [],
          duration: 0,
          success: true
        };
      }

      return await this.insertBatch(validated);
    } catch (error) {
      this.logger.error(`Error seeding ${this.entityName}: ${error}`);
      return {
        entityName: this.entityName,
        inserted: 0,
        updated: 0,
        skipped: 0,
        errors: [
          { itemIndex: 0, value: null, message: String(error) }
        ],
        duration: 0,
        success: false
      };
    }
  }

  // Abstract methods - subclasses must implement
  protected abstract getDataSources(): string[];
  protected abstract transformData(raw: T): unknown;
  protected abstract insertBatch(data: T[]): Promise<EntityResult>;

  // Concrete implementations
  protected async loadData(): Promise<T[]> {
    const sources = this.getDataSources();
    // Load from JSON files with fallback pattern
    this.logger.debug(
      `Loading data from sources: ${sources.join(", ")}`
    );
    // Implementation delegates to DataLoader
    return [] as T[];
  }

  protected async validateData(data: T[]): Promise<T[]> {
    if (this.options.skipValidation) {
      return data;
    }

    const validated: T[] = [];
    const errors: Array<{ index: number; error: string }> = [];

    for (let i = 0; i < data.length; i++) {
      const result = this.schema.safeParse(data[i]);
      if (result.success) {
        validated.push(result.data as T);
      } else {
        errors.push({
          index: i,
          error:
            result.error.errors[0]?.message || "Validation failed"
        });
      }
    }

    if (errors.length > 0 && this.options.verbose) {
      this.logger.warn(
        `${errors.length} validation errors encountered`
      );
    }

    return validated;
  }
}
```

### CLI Usage Examples

```bash
# Seed all entities with defaults
pnpm seed

# Seed specific entities
pnpm seed types
pnpm seed authors artists
pnpm seed comics chapters

# Dry-run validation
pnpm seed --dry-run --verbose

# Custom batch and concurrency settings
pnpm seed comics --batch-size=50 --concurrency=3

# Force overwrite (upsert mode)
pnpm seed --force

# No transactions (faster but less safe)
pnpm seed --no-transaction
```

### API Endpoint Examples

```bash
# Validate seeding (no auth required)
curl -X GET http://localhost:3000/api/seed

# Start seeding (admin auth required)
curl -X POST http://localhost:3000/api/seed \
  -H "Content-Type: application/json" \
  -d '{"entities": "all", "options": {"batchSize": 100, "concurrency": 5}}'

# Reset database (delete all seeded data)
curl -X DELETE http://localhost:3000/api/seed

# Upsert with force-overwrite
curl -X PATCH http://localhost:3000/api/seed \
  -H "Content-Type: application/json" \
  -d '{"entities": "comics", "options": {"forceOverwrite": true}}'

# Full reset (delete + reseed)
curl -X PUT http://localhost:3000/api/seed \
  -H "Content-Type: application/json" \
  -d '{"entities": "all"}'
```

### Progress Tracker Output Example

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Seeding Comics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

→ Loading data from sources: comic.json
✓ Loaded 2087 records from comic.json

→ Validating 2087 records...
✓ Validation complete: 2087 valid, 0 errors

→ Processing in batches (batch-size=100, concurrency=5):
  [████████████████████░░░░░░░░░░░░░░░░░░░░░░ ] 52% (1087/2087)
  Inserted 1087 | Speed: 218/sec | ETA: 4.6s

✓ Comics seeding completed
  Inserted: 2087 | Updated: 0 | Skipped: 0 | Errors: 0 | Duration: 9.5s
```

### File Structure Reference

```
src/scripts/seed/
├── types.ts                      # 200+ lines: Core types & interfaces
├── logger.ts                     # 80 lines: Colored logging utility
├── config.ts                     # 120 lines: CLI arg parsing with Commander
├── dataLoader.ts                 # 100 lines: Multi-file JSON loader
├── run.ts                        # 30 lines: CLI entry point
├── index.ts                      # 20 lines: Export all seeders
├── seedOrchestrator.ts          # 180 lines: Orchestrate seeding order
│
├── seeders/
│   ├── baseSeed.ts              # 180 lines: Abstract base class
│   ├── typeSeeder.ts            # 80 lines: Seed predefined types
│   ├── authorSeeder.ts          # 100 lines: Seed authors from JSON
│   ├── artistSeeder.ts          # 100 lines: Seed artists from JSON
│   ├── genreSeeder.ts           # 100 lines: Seed genres from JSON
│   ├── comicSeeder.ts           # 250 lines: Complex comic + image handling
│   └── chapterSeeder.ts         # 200 lines: Chapters + image extraction
│
├── helpers/
│   ├── progressTracker.ts       # 150 lines: Progress metrics & logging
│   ├── creatorNameResolver.ts   # 80 lines: Name splitting & dedup
│   ├── dateParser.ts            # 40 lines: Flexible date parsing
│   └── chapterNumberExtractor.ts # 30 lines: Regex chapter extraction
│
├── database/
│   ├── batchProcessor.ts        # 120 lines: Concurrent batch processing
│   ├── transactionManager.ts    # 40 lines: Drizzle transaction wrapper
│   └── conflictResolver.ts      # 50 lines: Upsert patterns
│
└── images/
    ├── imageDownloader.ts       # 150 lines: Local cache + retries
    ├── imageKitUploader.ts      # 80 lines: ImageKit integration
    └── imageStrategy.ts         # 100 lines: Strategy pattern dispatcher

src/schemas/seed/
├── user.seed.ts                 # 30 lines: User Zod schema
├── comic.seed.ts                # 40 lines: Comic Zod schema
├── chapter.seed.ts              # 35 lines: Chapter Zod schema
└── index.ts                     # 10 lines: Schema exports

src/app/api/seed/
└── route.ts                     # 200 lines: REST API (GET, POST, DELETE, PUT, PATCH)
```

### Config Parser Example (`src/scripts/seed/config.ts`)

```typescript
import { Command } from "commander";
import { z } from "zod";
import { SeedConfig } from "./types";

const envSchema = z.object({
  DATABASE_URL: z.string().url(),
  NODE_ENV: z
    .enum(["development", "production"])
    .default("development"),
  IMAGEKIT_PUBLIC_KEY: z.string().optional(),
  IMAGEKIT_PRIVATE_KEY: z.string().optional()
});

export function parseCliArgs(): SeedConfig {
  const program = new Command();

  program
    .command("seed [entities...]")
    .description("Seed database with test data")
    .option(
      "--batch-size <number>",
      "Batch size for processing",
      "100"
    )
    .option("--concurrency <number>", "Concurrent operations", "5")
    .option("--verbose", "Verbose logging")
    .option("--dry-run", "Validate without persisting")
    .option("--force", "Force overwrite existing data")
    .option("--no-transaction", "Disable transactions")
    .option("--skip-validation", "Skip Zod validation")
    .option(
      "--image-strategy <mode>",
      "Image strategy: urls|local|imagekit",
      "urls"
    )
    .action((entities, options) => {
      const env = envSchema.parse(process.env);

      return {
        entities: entities.length === 0 ? ["all"] : entities,
        options: {
          batchSize: parseInt(options.batchSize),
          concurrency: parseInt(options.concurrency),
          verbose: options.verbose,
          dryRun: options.dryRun,
          useTransaction: options.transaction,
          skipValidation: options.skipValidation,
          forceOverwrite: options.force,
          imageStrategy: options.imageStrategy
        },
        timestamp: new Date()
      } satisfies SeedConfig;
    });

  return program.parse().opts();
}
```

---

**Plan Version**: 1.0  
**Status**: Planned  
**Total Tasks**: 83  
**Estimated Effort**: 40-50 hours development + 10 hours testing  
**Next Step**: Begin Implementation Phase 1 (Core Infrastructure & Types)
