# 2. Implementation Steps

> Extracted from `plan-features-seed.prompt.md`.

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
