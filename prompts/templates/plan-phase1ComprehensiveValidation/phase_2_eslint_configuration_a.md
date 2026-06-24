# PHASE 2: ESLint Configuration Audit & Modernization

> Extracted from `plan-phase1ComprehensiveValidation.prompt.md`.

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
