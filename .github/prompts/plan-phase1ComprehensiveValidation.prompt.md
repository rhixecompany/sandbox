# ComicWise: Comprehensive Validation & Enhancement Roadmap

**Status**: 🔴 Planning Complete — Ready for Phase 1 Execution **Created**: 2026-03-06 **Scope**: 3 Phases (Validation + ESLint Modernization + Feature Development) **Approach**: Systematic fix and enhancement with quality gate validation after each phase

---

## Problem Statement

The ComicWise Next.js 16 codebase has **three interconnected layers of work**:

### Layer 1: Immediate Validation Blockers (Phase 1)

- **1 TypeScript Error** — `src/tests/e2e/reading.spec.ts:163` (type mismatch on `toHaveAttribute()`)
- **30 ESLint Errors** — Primarily unused assignments and import order violations
- **21 Test Failures** — Out of 175 tests (logic, mocks, assertions)
- **650 ESLint Warnings** — Code quality degradation (non-blocking)

**Impact**: Quality gate failures prevent any further work. **BLOCKS Phases 2 & 3**.

### Layer 2: Code Quality Infrastructure (Phase 2)

- **ESLint Configuration Debt** — Current config (37 lines, 5 plugins) vs. reference (522 lines, 17+ plugins)
- **Missing Plugins** — `@eslint/js`, `import-x`, `jest`, `n`, `perfectionist`, `react-refresh`, `security`, `testing-library`, `unicorn`, `globals`
- **Code Quality Gap** — 31 lint errors, 650 warnings after Phase 1

**Impact**: Phase 2 enables sustainable development practices for Phase 3 features. **BLOCKS Phase 3 quality**.

### Layer 3: Feature Development Pipeline (Phase 3)

- **Seeding System**: ✅ Complete (274 comics, 1127 chapters, 126 authors/artists, 68 genres)
- **Feature Pipeline**: 5 features in linear dependency chain
- **Prerequisite**: Clean, modern codebase (Phases 1 & 2 complete)

**Impact**: Feature development can only begin once quality gate is clean.

---

## Solution Approach

**Three-phase systematic implementation** with clear dependencies and quality gates:

```
Phase 1: Validation Fixes (CRITICAL)
    ├─ Fix TypeScript errors
    ├─ Fix test failures (case-by-case analysis)
    ├─ Fix ESLint errors
    └─ Verify: pnpm type-check && pnpm lint && pnpm test && pnpm build
         │
         └─ Phase 2: ESLint Modernization (IMPORTANT)
             ├─ Install missing plugins (10+ new)
             ├─ Migrate to hybrid ESLint config
             ├─ Fix remaining lint issues
             └─ Verify: pnpm type-check && pnpm lint && pnpm test && pnpm build
                  │
                  └─ Phase 3: Feature Development (PLANNED - Linear Order)
                      ├─ Phase 3.1: User Profile Features
                      ├─ Phase 3.2: Comics Listing & Discovery
                      ├─ Phase 3.3: Chapter Reader & Progress
                      ├─ Phase 3.4: Bookmarks Management
                      └─ Phase 3.5: Advanced Features (Deferred)
```

---

## PHASE 1: Fix Immediate Validation Issues

**Status**: 🔴 Pending **Prerequisites**: None **Output**: Clean `pnpm type-check`, `pnpm lint`, `pnpm test`, `pnpm build` (zero errors) **Success Criteria**:

- ✅ 0 TypeScript errors
- ✅ 0 test failures
- ✅ 0 ESLint errors (30 → 0)
- ✅ All 4 quality gate checks pass

### Issue Inventory

#### TypeScript Errors (1)

| File | Line | Error | Root Cause | Fix Strategy |
| --- | --- | --- | --- | --- |
| `src/tests/e2e/reading.spec.ts` | 163 | TS2769: No overload matches `toHaveAttribute()` | `initialAriaPressed` is `string \| null`, method expects `string \| RegExp` | Add null assertion or conditional check |

#### ESLint Errors (30)

**Categories**:

- **Unused Assignments** (10-12 instances) — Test setup variables not used in assertions
- **Import Order Violations** (8-10 instances) — Files with incorrect import ordering
- **Filename Casing** (2-3 instances) — Files not following naming conventions
- **Other** (5-7 instances) — Various lint rule violations

**Fixable with `--fix`**: ~10 errors (import order, some unused) **Manual fixes required**: ~20 errors (logic-based)

#### Test Failures (21 / 175)

| File | Count | Issue Type | Analysis Required |
| --- | --- | --- | --- |
| `src/tests/auth.test.ts` | 1 | Assertion logic | Mock setup vs. actual implementation |
| `src/tests/rating.test.ts` | 1 | Assertion failure | Expected vs. actual test result |
| `src/tests/search.actions.test.ts` | 3 | Promise/mock issues | Await patterns and mock configuration |
| `src/tests/comic-dal.spec.ts` | 1 | Missing await | Async operation not awaited |
| `src/tests/comic-schema.spec.ts` | 1 | Schema validation | Validation logic mismatch |
| `src/tests/search-dal.spec.ts` | 2 | Query/data issues | DAL query logic |
| `src/tests/comment.test.ts` | 1 | Logic error | Test assertion or code logic |
| `src/tests/reading-progress.test.ts` | 3 | Async/state issues | Promise handling and state |
| Other files | 8 | Various | Auto-fix vs. manual fix decision |

### Implementation Plan

#### Task 1.1: Fix TypeScript Error

- [ ] Read `src/tests/e2e/reading.spec.ts` around line 163
- [ ] Analyze the type mismatch (null handling)
- [ ] Apply fix (null assertion `!` or optional chaining)
- [ ] Run `pnpm type-check` → verify 0 errors

#### Task 1.2: Analyze & Fix Test Failures

- [ ] Read each failing test file
- [ ] Determine root cause: mock setup, assertion logic, or code bug
- [ ] Apply fix (case-by-case):
  - If mock is wrong: fix mock setup
  - If assertion is wrong: fix assertion
  - If code is wrong: fix implementation
- [ ] Run `pnpm test` after each fix
- **Test files to address** (21 failures):
  - `auth.test.ts` (1)
  - `rating.test.ts` (1)
  - `search.actions.test.ts` (3)
  - `comic-dal.spec.ts` (1)
  - `comic-schema.spec.ts` (1)
  - `search-dal.spec.ts` (2)
  - `comment.test.ts` (1)
  - `reading-progress.test.ts` (3)
  - Other files (8)

#### Task 1.3: Fix ESLint Errors (30 → 0)

- [ ] Run `pnpm lint --fix` → auto-fix ~10 errors (import order, simple violations)
- [ ] Manually fix remaining ~20 errors:
  - Identify unused variable patterns
  - Fix import order in files that don't auto-fix
  - Address filename casing issues
  - Resolve any other lint violations
- [ ] Run `pnpm lint` → verify 0 errors

#### Task 1.4: Auto-Format & Final Verification

- [ ] Run `pnpm format` (auto-format code with Prettier)
- [ ] Run `pnpm type-check` → must pass
- [ ] Run `pnpm lint` → must show 0 errors
- [ ] Run `pnpm test` → must show 0 failures (175/175 passing)
- [ ] Run `pnpm build` → must complete successfully

#### Task 1.5: Phase 1 Commit

- [ ] Create comprehensive commit: "fix: resolve validation issues blocking quality gate"
  - Mention: TypeScript error fixed, 21 tests fixed, 30 ESLint errors resolved
  - Reference: TSV2769, test failures by file, lint rule violations
- [ ] Include trailer: `Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>`
- [ ] Verify commit before pushing

---

## PHASE 2: ESLint Configuration Audit & Modernization

**Status**: 🔴 Pending **Prerequisites**: Phase 1 ✅ Complete **Output**: Comprehensive `eslint.config.mts` with 17+ plugins, zero lint errors **Success Criteria**:

- ✅ 0 ESLint errors (improvements on Phase 1)
- ✅ All 10+ missing plugins installed
- ✅ Config file migrated from 37 → 500+ lines (feature-rich)
- ✅ All 4 quality gate checks still pass

### ESLint Audit Results

#### Current State

- **Config Size**: 37 lines
- **Plugins**: 5 (better-tailwindcss, drizzle, playwright, vitest, zod)
- **Issues**: Minimal configuration, missing critical plugins

#### Target State (from `.references/comicwise/eslint.config.ts`)

- **Config Size**: 522 lines
- **Plugins**: 17+ (@eslint/js, import-x, jest, n, perfectionist, react-refresh, security, testing-library, unicorn, globals, + others)
- **Coverage**: Comprehensive source, test, config file handling

#### Plugin Additions Needed

| Plugin | Category | Purpose | Required |
| --- | --- | --- | --- |
| `@eslint/js` | Core | JavaScript recommended rules | ✅ Critical |
| `eslint-plugin-import-x` | Import | Import order, duplicate detection | ✅ Critical |
| `eslint-plugin-jest` | Testing | Jest-specific rules | ✅ Important |
| `eslint-plugin-n` | Node.js | Node.js best practices | ✅ Important |
| `eslint-plugin-perfectionist` | Code Quality | Sorting/organization | ⚠️ Nice-to-have |
| `eslint-plugin-react-refresh` | React | React Refresh compatibility | ✅ Important |
| `eslint-plugin-security` | Security | Security vulnerability detection | ✅ Critical |
| `eslint-plugin-testing-library` | Testing | Testing Library best practices | ✅ Important |
| `eslint-plugin-unicorn` | Code Quality | Awesome code patterns | ⚠️ Nice-to-have |
| `globals` | Core | Global variables (Node, browser) | ✅ Critical |

**Installation Command**:

```bash
pnpm add -D @eslint/js eslint-plugin-import-x eslint-plugin-jest \
  eslint-plugin-n eslint-plugin-perfectionist eslint-plugin-react-refresh \
  eslint-plugin-security eslint-plugin-testing-library eslint-plugin-unicorn \
  globals
```

### Implementation Plan

#### Task 2.1: Install Missing Plugins

- [ ] Run `pnpm add -D [plugins]` (see command above)
- [ ] Verify all 10 plugins installed in `package.json`
- [ ] Confirm no peer dependency conflicts

#### Task 2.2: Create New ESLint Config

- [ ] Read `.references/comicwise/eslint.config.ts` (reference)
- [ ] Create backup of current `eslint.config.mts`
- [ ] Write new config from reference:
  - Global ignores (node_modules, dist, build artifacts)
  - Base TypeScript/JavaScript rules
  - Language options and globals
  - File-specific overrides:
    - `*.d.ts` files (types) — relax some rules
    - `src/scripts/seed/**/*.ts` — relax rules for build scripts
    - `src/**/*.test.ts` / `src/**/*.spec.ts` — relax for tests
    - `*.mts` / `next.config.ts` — config file rules
    - `src/**/*.tsx` — React component rules
  - Plugin configurations:
    - `@eslint/js` → Recommended rules
    - `import-x` → Import ordering, no circular deps
    - `@typescript-eslint` → TypeScript strict mode
    - `jest` → Jest test patterns
    - `testing-library` → Testing Library best practices
    - `react-refresh` → React Fast Refresh compatibility
    - `security` → Security vulnerability detection
    - `prettier` → LAST (to override formatting conflicts)
  - Special rules:
    - `no-explicit-any: "error"` for source, `"warn"` for tests
    - `no-unused-vars: "warn"` with `_` prefix ignore
- [ ] Ensure proper rule scoping (file-by-file overrides)

#### Task 2.3: Fix Remaining Lint Issues

- [ ] Run `pnpm lint` to identify remaining violations
- [ ] Address by category:
  - `no-explicit-any` (23 instances) — May be auto-resolved by type-strict overrides
  - `react/no-unescaped-entities` (4 instances) — SearchResultsContent.tsx
  - `no-unused-vars` (4 instances) — Rename to `_var` or remove
  - Import/export order issues — May be auto-fixed
- [ ] Run `pnpm lint:fix` for auto-fixable violations
- [ ] Manually fix remaining violations

#### Task 2.4: Verify & Quality Gate

- [ ] Run `pnpm type-check` → must pass (0 errors)
- [ ] Run `pnpm lint:fix` → auto-fix any remaining warnings
- [ ] Run `pnpm lint` → must show 0 errors (minimal warnings with reason)
- [ ] Run `pnpm test` → must still pass (175/175)
- [ ] Run `pnpm build` → must succeed

#### Task 2.5: Documentation & Commit

- [ ] Update `.github/copilot-instructions.md` to reference new ESLint config
- [ ] Document plugin additions and their purposes
- [ ] Create comprehensive commit: "refactor(lint): modernize eslint.config.mts with 17+ plugins and file-specific rules"
  - Mention: 10 plugins added, config size 37 → 500+ lines, 0 errors
  - Reference: Plugin purposes, file-specific overrides, security/quality improvements
- [ ] Include trailer: `Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>`

---

## PHASE 3: Feature Development Pipeline

**Status**: 🔴 Pending **Prerequisites**: Phase 1 ✅ + Phase 2 ✅ Complete **Approach**: Linear feature development (each phase builds on previous) **Dependencies**: Seeding system ✅ complete (provides test data)

### Feature Breakdown

#### Phase 3.1: User Profile Features

**Scope**:

- User profile view page (`/profile`)
- Profile edit form (name, email, avatar)
- Password change form
- Settings page (theme, language preferences)
- Account deletion (with confirmation)

**Dependencies**: NextAuth (auth.ts) ✅, Database schema ✅

#### Phase 3.2: Comics Listing & Discovery

**Scope**:

- Comics index page (`/comics`) with server-side filtering
- Comics grid with search, filters (genre, author, artist, status)
- Comic detail page (`/comics/[id]`)
- Author/artist/genre listing pages
- Trending and new comics sections
- Comic recommendations (basic)

**Dependencies**: Seeding data ✅, ComicDal ✅, Database schema ✅

#### Phase 3.3: Chapter Reader & Progress Tracking

**Scope**:

- Full-screen chapter reader component
- Image navigation (prev/next, keyboard shortcuts)
- Zoom controls (fit to width/height, custom zoom)
- Reading settings (brightness, scrolling mode)
- Reading progress tracking (last read page per chapter)
- Bookmark resume feature (jump to last read position)

**Dependencies**: Comics & Chapters DAL ✅, Zustand for reader state ✅

#### Phase 3.4: Bookmarks Management

**Scope**:

- Bookmarks list page with filtering (current reading, completed, dropped, etc.)
- Status management (add/remove bookmark, change status)
- Quick resume reading button
- Bookmarks sorting (by date added, by status, custom)
- Batch operations (mark multiple as read, delete)

**Dependencies**: BookmarkDal ✅, Server Actions ✅, Reading progress ✅

#### Phase 3.5: Advanced Features (Deferred)

- Comments & discussion threads
- Ratings & reviews
- User notifications
- Recommendations & suggestions
- Social features (follow, share)
- Admin panel & moderation
- Full-text search with Elasticsearch/Meilisearch
- Image optimization pipeline
- Analytics & user behavior tracking

**Note**: Not in initial release. Will be planned after Phases 3.1-3.4.

### Phase 3 Implementation Order

1. **Phase 3.1**: User Profile (Foundation for user personalization)
2. **Phase 3.2**: Comics Listing (Core feature, enables discovery)
3. **Phase 3.3**: Chapter Reader (Primary user interaction)
4. **Phase 3.4**: Bookmarks (Completes core reading loop)
5. **Phase 3.5+**: Advanced (Post-launch, community features)

---

## Quality Gates & Validation

**All phases must pass these checks before completion**:

```bash
# Run after each phase
pnpm type-check          # 0 TypeScript errors required
pnpm lint                # 0 ESLint errors (minimal warnings OK)
pnpm test                # All tests passing (X/Y)
pnpm build               # Production build succeeds
```

**Additional checks for Phase 3 features**:

- `pnpm test src/path/to/feature.test.tsx` — Feature tests passing
- Manual testing in browser (`pnpm dev`)
- Lighthouse audit (performance, accessibility)
- Database schema consistency check

---

## Risk Mitigation & Rollback Strategy

### Phase 1 Risks

**Risk**: Test fixes break existing functionality **Mitigation**: Analyze each test failure before fixing; prefer fixing code over tests when logic is clear **Rollback**: `git checkout -- src/` then start over (each fix is incremental)

### Phase 2 Risks

**Risk**: New ESLint config is too strict, breaks build **Mitigation**: Use file-specific overrides to relax rules where needed; test each plugin integration **Rollback**: Revert to backup of old `eslint.config.mts`; reinstall only original 5 plugins

### Phase 3 Risks

**Risk**: Feature conflicts with existing code or introduces bugs **Mitigation**: Write tests first, follow established patterns from DAL/actions, code review before merge **Rollback**: `git revert` the feature commit; verify tests still pass

---

## Notes & Considerations

### Phase 1

- TypeScript error is a **blocker** — fix first
- Test failures likely due to mock setup or assertion mismatches — analyze before fixing
- Auto-fix will resolve ~10 lint errors; ~20 require manual attention
- Some warnings may be acceptable with documentation (e.g., intentional console.logs)

### Phase 2

- ESLint config is a **leverage point** for code quality — worth investing time
- Hybrid approach: use reference config as template but apply selectively
- `perfectionist` and `unicorn` are nice-to-have; focus on critical plugins first
- Security plugin is **important** for catching vulnerabilities early

### Phase 3

- Linear order ensures no dependency issues
- Seeding system ✅ provides 274 test comics, so features can use real-like data
- Start with User Profile to establish patterns (DAL, actions, components)
- Comics Listing is critical path; chapter reader depends on it
- Bookmarks completes the core loop; advanced features are post-MVP

### General

- Commit frequently (after each task, not just phase end)
- Quality gate must pass before moving to next phase
- Documentation in `.github/copilot-instructions.md` should be updated
- No breaking changes to existing APIs or database schema without migration

---

## References & Documentation

- **Project Root**: `C:\Users\Alexa\Desktop\SandBox\comicbook`
- **ESLint Reference**: `.references/comicwise/eslint.config.ts` (522 lines)
- **TypeScript Config**: `tsconfig.json` (strict mode enabled)
- **Copilot Instructions**: `.github/copilot-instructions.md`
- **Project Docs**: `.github/instructions/` (18 instruction files)
- **Stack**: Next.js 16, React 19 Server Components, Drizzle + PostgreSQL, Zustand, React Query, shadcn/ui, Tailwind v4
- **Seeding System**: `src/scripts/seed/` (complete, 274 comics seeded)

---

## Summary

| Phase | Status | Blocker | Duration | Success Criteria |
| --- | --- | --- | --- | --- |
| **1: Validation Fixes** | 🔴 Pending | **YES** | ~2h | 0 errors, all tests pass |
| **2: ESLint Modernization** | 🔴 Pending | NO (Phase 1) | ~3h | 17+ plugins, 0 errors |
| **3: Feature Development** | 🔴 Pending | NO (Phases 1+2) | TBD | MVP complete, 0 regressions |

**Next Step**: As Implementer persona, reference .github/prompts/setup-enhanced.prompt.md and docs/dev.content.md, Start Phase 1 execution. Read current TypeScript error and first failing test, then proceed with fixes.
