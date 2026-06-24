# 2. Implementation Steps

> Extracted from `plan-refactor.prompt.md`.

## 2. Implementation Steps

### Implementation Phase 1: Environment Setup & Validation

**GOAL-001:** Validate development environment, dependencies, and initial state

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-001 | Install dependencies and verify pnpm lockfile integrity | ⬜ |  |
| TASK-002 | Run type-check validation - target zero TypeScript errors | ⬜ |  |
| TASK-003 | Run database schema validation (drizzle db:check) | ⬜ |  |
| TASK-004 | Validate authentication configuration files | ⬜ |  |
| TASK-005 | Verify all environment schema definitions in env.ts | ⬜ |  |
| TASK-006 | Check build artifacts for any cached errors | ⬜ |  |

### Implementation Phase 2: Tailwind CSS Class Modernization

**GOAL-002:** Update deprecated Tailwind syntax to modern v4 equivalent

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-007 | Replace `bg-gradient-to-br` with `bg-linear-to-br` in src/app/(root)/page.tsx | ⬜ |  |
| TASK-008 | Replace `bg-gradient-to-br` with `bg-linear-to-br` in src/app/(root)/comics/[slug]/page.tsx | ⬜ |  |
| TASK-009 | Replace `bg-gradient-to-r` with `bg-linear-to-r` in src/app/(root)/comics/[slug]/page.tsx | ⬜ |  |
| TASK-010 | Replace `bg-gradient-to-br` with `bg-linear-to-br` in src/app/(root)/search/page.tsx | ⬜ |  |
| TASK-011 | Replace `aspect-[2/3]` with `aspect-2/3` in src/app/(root)/page.tsx | ⬜ |  |
| TASK-012 | Replace `aspect-[2/3]` with `aspect-2/3` in src/app/(root)/comics/page.tsx | ⬜ |  |
| TASK-013 | Replace `aspect-[3/4]` with `aspect-3/4` in src/app/(root)/search/page.tsx | ⬜ |  |
| TASK-014 | Replace aspect ratio in src/app/(root)/comics/[slug]/page.tsx | ⬜ |  |
| TASK-015 | Replace gradients in src/components/bookmarks/bookmark-card.tsx (line 125, 129) | ⬜ |  |
| TASK-016 | Replace aspect ratio in src/components/bookmarks/bookmark-card.tsx (line 116) | ⬜ |  |
| TASK-017 | Verify all Tailwind classes compile without warnings | ⬜ |  |

### Implementation Phase 3: Markdown Linting & Documentation Fixes

**GOAL-003:** Resolve all markdown linting errors in documentation files

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-018 | Fix MD036 errors in IMPLEMENTATION_NOTES.md (convert emphasis headings to proper headings) | ⬜ |  |
| TASK-019 | Fix MD031 errors in IMPLEMENTATION_NOTES.md (blank lines around fenced code blocks) | ⬜ |  |
| TASK-020 | Fix MD040 errors in IMPLEMENTATION_NOTES.md (add language specifications to code blocks) | ⬜ |  |
| TASK-021 | Fix MD026 error in docs/implementation-status.md (remove trailing punctuation) | ⬜ |  |
| TASK-022 | Fix MD036 errors in docs/implementation-status.md (Phase headers) | ⬜ |  |
| TASK-023 | Fix MD031 errors in docs/implementation-status.md (blank lines around fences) | ⬜ |  |
| TASK-024 | Fix MD033 errors in docs/implementation-status.md (remove inline HTML) | ⬜ |  |
| TASK-025 | Validate all markdown files pass linting standards | ⬜ |  |

### Implementation Phase 4: Code Quality & Linting Compliance

**GOAL-004:** Ensure all TypeScript and JavaScript code passes ESLint validation

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-026 | Run eslint --fix across entire src/ directory | ⬜ |  |
| TASK-027 | Verify no 'any' types exist in codebase (ESLint: no-explicit-any) | ⬜ |  |
| TASK-028 | Check for unused imports and remove them | ⬜ |  |
| TASK-029 | Validate all Server Actions follow ActionResult<T> pattern | ⬜ |  |
| TASK-030 | Verify all DAL classes extend BaseDal and use .with() eager loading | ⬜ |  |
| TASK-031 | Check Zustand stores use devtools(persist()) pattern | ⬜ |  |
| TASK-032 | Validate environment variable usage via getEnv() function | ⬜ |  |

### Implementation Phase 5: Type Safety & Schema Validation

**GOAL-005:** Ensure zero TypeScript compilation errors and type safety

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-033 | Run tsc --noEmit to verify type checking | ⬜ |  |
| TASK-034 | Validate Zod schemas in src/schemas/ directory structure | ⬜ |  |
| TASK-035 | Verify database query return types match schema definitions | ⬜ |  |
| TASK-036 | Check all Server Action input validation uses Zod | ⬜ |  |
| TASK-037 | Validate NextAuth configuration types and callbacks | ⬜ |  |
| TASK-038 | Verify React Query key factory types in src/lib/query-client.ts | ⬜ |  |

### Implementation Phase 6: Database & Seeding Validation

**GOAL-006:** Validate database schema and seeding system integrity

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-039 | Run drizzle-kit check to validate schema | ⬜ |  |
| TASK-040 | Verify all foreign keys include onDelete: cascade | ⬜ |  |
| TASK-041 | Validate comicStatus enum uses Title-Case values | ⬜ |  |
| TASK-042 | Test seeding system with --dry-run flag | ⬜ |  |
| TASK-043 | Verify all seeders follow BaseSeeder template pattern | ⬜ |  |
| TASK-044 | Validate LookupCache implementation in seeding | ⬜ |  |

### Implementation Phase 7: Testing & Final Validation

**GOAL-007:** Run complete validation suite and ensure production readiness

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-045 | Run pnpm type-check (must result in 0 errors) | ⬜ |  |
| TASK-046 | Run pnpm lint:fix (must pass all checks) | ⬜ |  |
| TASK-047 | Run pnpm build (production build validation) | ⬜ |  |
| TASK-048 | Run pnpm test (Vitest unit tests) | ⬜ |  |
| TASK-049 | Run pnpm test:e2e (Playwright E2E tests) | ⬜ |  |
| TASK-050 | Validate all quality gates pass (type-check, lint, build, tests) | ⬜ |  |

---
