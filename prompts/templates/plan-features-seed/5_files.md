# 5. Files

> Extracted from `plan-features-seed.prompt.md`.

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
