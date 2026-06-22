# Tasks

> Extracted from `seed-review-and-create.prompt.md`.

## Tasks

### 1. Review Existing Seeders

Review all files in `src/scripts/seed/seeders/` for:

- Correct `BaseSeeder<T>` extension pattern
- Proper cache usage (read from/write to `LookupCache`)
- Accurate `EntityResult` reporting (inserted/updated/skipped counts)
- Error handling and graceful failures
- Data validation via Zod schemas

### 2. Create Missing Seeders

If any of these seeders are missing, create them following the established pattern:

- **UserSeeder** — Seed users with bcryptjs password hashing (10 salt rounds), email deduplication via cache
- **ComicImageSeeder** — Seed comic images from comic JSON data, resolve comicId from cache, use `onConflictDoNothing()` for unique imageUrl
- **ChapterImageSeeder** — Seed chapter images, resolve chapterId via (comicId, chapterNumber) lookup, use `onConflictDoNothing()` for unique (chapterId, pageNumber)

### 3. Fix Issues

Common issues to check and fix:

- Incorrect counter increments (e.g., `updated++` when nothing is actually updated — should be `skipped++`)
- Duplicated utility functions that should be extracted to `helpers/`
- Missing exports in `index.ts`
- Missing switch cases in `seed-orchestrator.ts`
- `LookupCache` missing entries for new entity types
- `SeedConfig.entities` union type missing new entity names

### 4. Implement Improvements

- Extract shared utilities (e.g., `stripHtmlTags`) to `src/scripts/seed/helpers/`
- Ensure all seeders use `onConflictDoNothing()` or `onConflictDoUpdate()` for idempotent seeding
- Verify dependency order in orchestrator matches actual FK constraints
