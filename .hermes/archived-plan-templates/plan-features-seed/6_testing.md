# 6. Testing

> Extracted from `plan-features-seed.prompt.md`.

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
