---
description: "This prompt outlines the steps for setting up the ComicWise development environment and implementing code quality refactoring."
agent: "Next.js Expert"
model: "Claude Haiku 4.5 (copilot)"
---

# ComicWise Setup & Code Quality Refactoring Implementation Plan

![Status: In progress](https://img.shields.io/badge/status-In%20progress-yellow)

## Introduction

This implementation plan establishes a systematic approach to setting up the ComicWise development environment and refactoring code to meet quality standards. The plan encompasses environment validation, type safety, lint error resolution, and comprehensive testing validation.

ComicWise is a Next.js 16 + React 19 manga/comic reader application with production-ready database seeding infrastructure. The project is in Phase 2, transitioning from infrastructure setup to core feature development and test coverage.

**Tech Stack:**

- Frontend: Next.js 16.1.6, React 19, TypeScript, Tailwind CSS v4, shadcn/Radix UI
- Backend: Next.js App Router, Server Components, Server Actions
- Database: PostgreSQL (Neon), Drizzle ORM + 30+ tables
- Auth: NextAuth.js v5 (database sessions, role-based access)
- State: Zustand + React Query
- Testing: Vitest (unit) + Playwright (E2E)
- Seeding: Production CLI + REST API with ~5,000 comics/50,000 chapters

---

## 1. Requirements & Constraints

- **REQ-001**: All TypeScript files must pass strict type checking with zero errors
- **REQ-002**: All markdown files must comply with markdown linting standards
- **REQ-003**: All Tailwind CSS classes must use modern syntax (Tailwind v4 compatible)
- **REQ-004**: All code must follow ComicWise architecture patterns from copilot-instructions.md
- **REQ-005**: Database schema and seeding system must be validated
- **REQ-006**: Server Actions must follow ActionResult<T> pattern
- **REQ-007**: DAL classes must use Drizzle eager loading with .with()
- **SEC-001**: Environment variables must be validated with Zod schema at runtime
- **SEC-002**: NextAuth database sessions must be properly configured
- **CON-001**: React Compiler is ON - no manual memoization allowed
- **CON-002**: No force-dynamic page-level exports allowed
- **CON-003**: All components must handle SSR safely
- **GUD-001**: Follow Next.js App Router best practices for Server/Client Components
- **GUD-002**: Maintain consistent code formatting with Prettier
- **GUD-003**: Use template method pattern for seeding (BaseSeeder inheritance)
- **PAT-001**: Implement Service Locator pattern via singleton exports
- **PAT-002**: Use Factory pattern for complex object creation

---

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

## 3. Alternatives

- **ALT-001**: Automated batch fixing via ESLint and Prettier instead of manual fixes
- **ALT-002**: Use migration scripts for large-scale refactoring instead of file-by-file edits
- **ALT-003**: Create GitHub Actions workflow for continuous validation instead of manual validation

---

## 4. Dependencies

- **DEP-001**: TypeScript 5.x compiler
- **DEP-002**: ESLint with @typescript-eslint plugins
- **DEP-003**: Prettier code formatter
- **DEP-004**: Drizzle ORM and Drizzle Kit
- **DEP-005**: Next.js 16.1.6 with App Router
- **DEP-006**: Vitest and Playwright for testing
- **DEP-007**: Tailwind CSS v4 with plugins
- **DEP-008**: React 19.x Server Components
- **DEP-009**: NextAuth v5 with Drizzle adapter
- **DEP-010**: Zod for runtime schema validation

---

## 5. Files Affected

- **FILE-001**: src/app/(root)/page.tsx - Update Tailwind gradients and aspect ratios
- **FILE-002**: src/app/(root)/comics/page.tsx - Update Tailwind aspect ratios
- **FILE-003**: src/app/(root)/comics/[slug]/page.tsx - Update Tailwind gradients and aspect ratios
- **FILE-004**: src/app/(root)/search/page.tsx - Update Tailwind gradients and aspect ratios
- **FILE-005**: src/components/bookmarks/bookmark-card.tsx - Update Tailwind gradients and aspect ratios
- **FILE-006**: IMPLEMENTATION_NOTES.md - Fix markdown formatting
- **FILE-007**: docs/implementation-status.md - Fix markdown formatting
- **FILE-008**: All .ts/.tsx files in src/ - Verify ESLint compliance
- **FILE-009**: All .md files in docs/ and root - Verify Markdown compliance
- **FILE-010**: src/database/schema.ts - Validate database schema integrity

---

## 6. Testing & Validation

- **TEST-001**: Validate TypeScript compilation with zero errors via `tsc --noEmit`
- **TEST-002**: Validate ESLint passes all checks via `eslint --max-warnings=0`
- **TEST-003**: Validate Prettier formatting compliance
- **TEST-004**: Run Vitest unit tests in jsdom environment
- **TEST-005**: Run Playwright E2E tests against running dev server
- **TEST-006**: Validate Next.js production build succeeds
- **TEST-007**: Validate database schema with drizzle-kit check
- **TEST-008**: Validate seeding system with --dry-run flag
- **TEST-009**: Validate all markdown files comply with linting standards
- **TEST-010**: Verify Tailwind CSS compilation without warnings

---

## 7. Risks & Assumptions

**Risks:**

- **RISK-001**: Large-scale code changes may introduce integration issues - mitigated by running full test suite
- **RISK-002**: Tailwind class updates may affect styling - mitigated by automated build validation

**Assumptions:**

- **ASSUMPTION-001**: All team members have identical development environment setup
- **ASSUMPTION-002**: Database is in sync with ORM schema definition
- **ASSUMPTION-003**: No sensitive data in codebase that requires special handling
- **ASSUMPTION-004**: All external APIs and services are accessible for validation

---

## 8. Related Specifications & Further Reading

- [ComicWise Copilot Instructions](../copilot-instructions.md)
- [Code Review Standards](../instructions/code-review.instructions.md)
- [Documentation Guidelines](../instructions/documentation.instructions.md)
- [Testing Standards](../instructions/testing.instructions.md)
- [TypeScript Standards](../instructions/typescript.instructions.md)
- [nextauth.js Configuration Documentation](https://authjs.dev/)
- [Drizzle ORM Documentation](https://orm.drizzle.team/)
- [Tailwind CSS v4 Migration Guide](https://tailwindcss.com/docs/upgrade-guide)
- [Next.js 16 App Router Documentation](https://nextjs.org/docs/app)

---

## Notes & Considerations

1. **React 19 Breaking Change:** params and searchParams are now async in Next.js 16 - must await them
2. **React Compiler:** Code must be compatible with automatic memoization
3. **Server Components:** Default to Server Components; only use Client Components for interactivity
4. **Type Generation:** Runs automatically via pre-dev and pre-build hooks; can manually trigger with `pnpm type-gen`
5. **Pre-commit Hooks:** Husky + lint-staged auto-runs ESLint on staged files; type-check failure blocks commits
6. **Turbopack:** Now default bundler with file system caching - no manual configuration needed
7. **Error Handling:** Use error.tsx for route-level error boundaries and loading.tsx for loading states
8. **Metadata API:** Use Metadata API in layout.tsx for SEO; support dynamic metadata in page.tsx
9. **Image Optimization:** Use next/image with explicit width/height; blur placeholders supported
10. **Seeding Production-Ready:** System handles 50K+ chapters; batch processing with concurrency controls

---

## Quality Gate (Must Pass Before PR)

```bash
pnpm type-check          # 0 TypeScript errors
pnpm lint:fix            # Auto-fix linting
pnpm test                # Vitest (jsdom environment)
pnpm build               # Production build validation
```

## Essential Commands

```bash
# Development
pnpm dev                 # Turbopack dev server (port 3000)
pnpm type-check:watch    # Watch mode for types

# Database
pnpm db:push             # Apply schema changes
pnpm db:studio           # Open Drizzle Studio (browser)

# Seeding
pnpm seed --dry-run --verbose
pnpm seed:all            # Seed all entities
pnpm seed:comics --force # Upsert comics

# Testing
pnpm test --watch        # Vitest watch mode
pnpm test:ui             # Playwright E2E
```
