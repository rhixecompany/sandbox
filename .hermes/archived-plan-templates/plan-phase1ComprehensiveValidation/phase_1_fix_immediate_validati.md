# PHASE 1: Fix Immediate Validation Issues

> Extracted from `plan-phase1ComprehensiveValidation.prompt.md`.

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
