# TypeScript Consolidation Utilities — Utility-First Pattern

This reference captures the utility-first consolidation approach used in Batch 3 (Banking TypeScript consolidation) and applies to future phases when multiple runners or wrappers share duplicated logic.

## Pattern: Utility-First Before Consumer Refactoring

**Principle:** When consolidating duplicated logic across multiple runners, create the shared utility FIRST, verify its interface, then stage the migration of consumers. Do NOT refactor all consumers immediately.

**Benefits:**
- Minimizes risk by validating the new utility interface before widespread adoption
- Allows verification of the utility pattern against real use cases
- Enables staged rollout: prioritize high-value consumers first
- Reduces merge conflicts and rollback scope if the utility design needs adjustment

## Example: orchestrator-spawn.ts

**File:** `rhixecompany/Banking/scripts/ts/utils/orchestrator-spawn.ts` (269 lines)

**Problem:** `run-ci-checks.ts` and `run-verify-and-validate.ts` both implement step-based orchestration with duplicated spawn/stdio/logging patterns.

**Solution:** Extract common patterns into a canonical utility.

### Exported Interfaces

```typescript
interface StepDefinition {
  name: string;           // Unique step name (used in --only/--skip filters)
  cmd: string;            // Shell command to run
  description?: string;   // Optional log description
}

interface ParsedFilters {
  only: string[];         // Steps to run (--only filter)
  skip: string[];         // Steps to skip (--skip filter)
  dryRun: boolean;        // Enable dry-run mode (--dry-run)
}

interface RunStepsResult {
  total: number;          // Total steps in sequence
  passed: string[];       // Steps that ran successfully
  failed: string[];       // Steps that failed
  exitCode: number;       // Overall exit code (0 on success)
}
```

### Exported Functions

```typescript
spawnStep(cmd, args = [], dryRun = false): number
  // Run a single shell command; returns exit code or error code

parseStepFilters(argv): ParsedFilters
  // Parse --only, --skip, --dry-run from process.argv

parseStepNames(s?: string): string[]
  // Parse comma-separated step list

resolveSteps(allSteps, filters): string[]
  // Apply filters to full step sequence; validates unknown step names

runSteps(steps, filters, options = {}): RunStepsResult
  // Orchestrate complete step sequence with logging and result tracking
```

### Key Features

1. **Dry-run support** — all functions honor `--dry-run` flag
2. **Flexible filtering** — supports both `--only foo,bar` and `--only=foo,bar` forms
3. **Consistent error handling** — validates unknown steps, exits cleanly, returns summary
4. **Full stdio inheritance** — runners see all output (logging, errors, command output)
5. **Extensible** — can be imported and used by future step-based runners

## Migration Pattern

### Phase 1: Create Utility (IMMEDIATE)

Create shared utility with rich interface, export all types and functions, add inline docs.

**Verification:**
- TypeScript AST validation (no syntax errors)
- Import path resolution (all dependencies exist)
- Interface completeness (all exported types are used/useful)
- Documentation (each exported function has JSDoc with examples)

### Phase 2: Document Consolidation Opportunities (IMMEDIATE)

Create `BATCH_3_CONSOLIDATION_SUMMARY.md` (or similar) documenting:
- Which existing runners should migrate to the new utility
- What refactoring would look like (line count reduction, deferral reason)
- Integration points for future batches (can Comicwise runners use this? Bash runners?)

Example from Banking consolidation:
```markdown
### Immediate Consolidation Candidates

1. **run-ci-checks.ts** — 141 lines; ~80 lines are argument parsing/step orchestration
   - Proposed: Import runSteps, reduce to ~30 lines actual logic
   - Impact: Eliminates duplicate spawn/filter boilerplate

2. **run-verify-and-validate.ts** — 32 lines; consistency benefit
   - Proposed: Use StepDefinition interface for parity
   - Impact: Uniform interface across all step-based runners
```

### Phase 3: Defer Consumer Refactoring (NEXT CHECKPOINT)

After Phase 2 completes, defer active refactoring to:
- Batch 3.5 (post-wrapper-stabilization checkpoint), OR
- Post-Batch 4 review (once Comicwise wrappers are stable), OR
- Batch 6+ (consolidation and cleanup phase)

**Reason:** Refactoring consumers carries refactoring risk. Wrapping them up immediately after utility creation contradicts the principle of minimal risk during stabilization phases. Deferral allows verification of the utility interface in the wild.

### Phase 4: Staged Consumer Migration (LATER CHECKPOINT)

When deferral period ends:
1. Migrate highest-value consumers first (e.g., run-ci-checks — used by all builds)
2. Verify parity after each migration (output, exit codes, dry-run behavior)
3. Remove old utility functions only after all consumers migrated
4. Mark deprecated utilities for Batch 7 dead-code sweep

## Consolidation Checklist

When consolidating duplicated logic into a new TypeScript utility:

- [ ] **Create utility** with rich JSDoc, exports, and types
- [ ] **Verify syntax** — TypeScript AST parser, no import errors
- [ ] **Document deferral** — record which consumers should migrate and why
- [ ] **Identify integration points** — can other repos (Comicwise, Bash) use this?
- [ ] **Plan staged migration** — which consumer first? How verify parity?
- [ ] **Defer active refactoring** — document when consumer migration should happen
- [ ] **Add reference doc** — create `.md` summary for future phases
- [ ] **Update skill** — patch this skill with lessons learned

## Anti-Patterns to Avoid

1. **Immediate universal refactoring** — DON'T refactor all consumers on utility creation. Verify the utility interface first.
2. **Over-parameterization** — don't add flags/options to utilities "just in case". Keep interfaces focused on actual consolidation targets.
3. **Breaking existing code** — utilities should provide new patterns, not displace existing code until consumers are ready.
4. **Missing documentation** — always document which consumers should migrate and when; don't leave it implicit.

## Future Applications

This pattern applies to:
- **Bash orchestrators** — Bash/scripts/lib/*.sh patterns that repeat across multiple runners
- **Comicwise setup/cleanup** — dev.sh, setup-dev.sh, quality-gate.sh duplication (Batch 4–5)
- **Plugin validation** — common patterns in plugin-verify.ts and plugin-repair.ts (Batch 6+)
- **Generic consolidation** — any codebase with repeated boilerplate logic across multiple files
