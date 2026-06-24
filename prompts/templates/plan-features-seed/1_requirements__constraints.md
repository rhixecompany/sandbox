# 1. Requirements & Constraints

> Extracted from `plan-features-seed.prompt.md`.

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
