# 4. Dependencies

> Extracted from `plan-features-seed.prompt.md`.

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
