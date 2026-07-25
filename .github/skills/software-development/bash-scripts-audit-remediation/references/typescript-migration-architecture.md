# TypeScript Migration Architecture

> **Session:** 2026-05-27 bash-scripts-fix modernization project  
> **Pattern:** AST-safe migration framework for Bash/PowerShell/BAT → TypeScript with behavior preservation

## Overview

This document captures the architectural pattern discovered during the comprehensive bash scripts modernization project (290+ scripts cataloged, 21 marked for migration, 149+ for deletion).

**Key Design Decisions:**
- Bun runtime (faster startup, native TypeScript, smaller footprint)
- ts-morph for AST transformations (type-safe vs. regex-based)
- Orchestrator pattern (thin shell wrappers preserve interfaces, TypeScript handles logic)
- Dry-run everywhere (all destructive operations gated)
- Behavior tests mandatory (input→output equivalence)
- 30-day quarantine for dead code

## Architecture Components

### 1. Core TypeScript Modules

**Location:** `Bash/src/core/`

```
src/core/
├── ast-transformer.ts    # AST-based code transformations with ts-morph
├── dry-run.ts           # DryRunExecutor for safe destructive operations
├── behavior-test.ts     # BehaviorTestRunner for equivalence testing
└── script-runner.ts     # Shell orchestration utilities
```

#### ast-transformer.ts (181 lines, 9.4 KB)

**Purpose:** Type-safe AST transformations using ts-morph

**Key Features:**
- `AstTransformer` class with ts-morph project management
- Pattern-based transformations (function renames, import updates, type annotations)
- Validation before applying changes
- Git checkpoint integration (`migration/pre-{name}` tags)

**Example Usage:**
```typescript
const transformer = new AstTransformer();
await transformer.addTransformation({
  pattern: /oldFunction/,
  transform: (node) => {
    if (Node.isIdentifier(node) && node.getText() === 'oldFunction') {
      node.replaceWithText('newFunction');
    }
  }
});
await transformer.applyTransformations('src/example.ts');
```

#### dry-run.ts (2.8 KB)

**Purpose:** DryRunExecutor for safe destructive operations

**Key Features:**
- `writeFile()`, `exec()`, `removeFile()` methods with `--dry-run` flag
- Logging all operations (both dry-run and real)
- Return values consistent between modes

**Example Usage:**
```typescript
const dryRun = new DryRunExecutor(isDryRun);
await dryRun.writeFile('config.json', content);
await dryRun.exec('rm -rf dist/');
await dryRun.removeFile('temp.log');
```

#### behavior-test.ts (2.9 KB)

**Purpose:** BehaviorTestRunner for input→output equivalence testing

**Key Features:**
- `addTest()` to register input/expected output pairs
- `runTests()` executes both original and TypeScript implementations
- Diff generation for failures
- CI integration support

**Example Usage:**
```typescript
const tester = new BehaviorTestRunner('cache-clean', './cache-clean.sh', './dist/cache-clean.js');
tester.addTest({ args: ['--dry-run'], expectedExitCode: 0, expectedOutput: /Dry run/ });
await tester.runTests();
```

#### script-runner.ts (2.8 KB)

**Purpose:** Shell orchestration utilities

**Key Features:**
- `spawnShell()` for executing shell commands with proper exit code handling
- `detectShell()` for cross-platform shell detection (bash/pwsh/cmd)
- Environment variable propagation
- Argument forwarding

### 2. Migration Utilities

**Location:** `Bash/Bash/` (nested convention)

```
Bash/Bash/
├── migrate-script.sh        # Scaffolding for new migrations
├── finalize-migration.sh    # Post-test completion
└── mark-dead-code.sh        # 30-day quarantine marker
```

#### migrate-script.sh (3.0 KB)

**Purpose:** Automated scaffolding for script migrations

**Usage:**
```bash
./Bash/Bash/migrate-script.sh cache-clean.sh
```

**Actions:**
1. Creates `src/implementations/{name}.ts` from template
2. Creates `tests/behavior/{name}.test.ts` from template
3. Creates git checkpoint tag `migration/pre-{name}`
4. Converts original to thin orchestrator wrapper

#### finalize-migration.sh (1.2 KB)

**Purpose:** Complete migration after tests pass

**Usage:**
```bash
./Bash/Bash/finalize-migration.sh cache-clean
```

**Actions:**
1. Verifies behavior tests passed
2. Updates `package.json` with new npm script
3. Commits changes with `feat: migrate {name} to TypeScript`
4. Removes checkpoint tag

#### mark-dead-code.sh (1.6 KB)

**Purpose:** Mark scripts for 30-day quarantine before deletion

**Usage:**
```bash
./Bash/Bash/mark-dead-code.sh path/to/script.sh "No longer used after refactor"
```

**Actions:**
1. Adds `# DEAD_CODE: marked for removal [DATE]` comment
2. Logs entry to `docs/dead-code-queue.md`
3. Sets 30-day deletion timer

### 3. Configuration

#### tsconfig.json

**Key Settings:**
```json
{
  "compilerOptions": {
    "strict": true,
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "types": ["bun-types"],
    "paths": { "@/*": ["./src/*"] }
  }
}
```

#### package.json

**Dependencies:**
- `ts-morph@^21.0.0` — AST transformations
- `bun-types` — Bun runtime types
- `prettier` — Code formatting

**Scripts Pattern:**
```json
{
  "scripts": {
    "clean:cache": "bun run src/implementations/cache-clean.ts",
    "clean:cache:dry": "bun run src/implementations/cache-clean.ts --dry-run",
    "upgrade": "bun run src/implementations/upgrade.ts",
    "upgrade:debug": "DEBUG=1 bun run src/implementations/upgrade.ts"
  }
}
```

## Orchestrator Pattern

### Thin Wrapper Contract

**Bash (.sh):**
```bash
#!/usr/bin/env bash
# shellcheck shell=bash
set -euo pipefail

# Thin orchestrator: delegates to TypeScript implementation
bun run "$(dirname "$0")/src/implementations/cache-clean.ts" "$@"
```

**PowerShell (.ps1):**
```powershell
#!/usr/bin/env pwsh
Set-StrictMode -Version Latest

# Thin orchestrator: delegates to TypeScript implementation
$ScriptDir = Split-Path -Parent $PSCommandPath
& bun run "$ScriptDir/src/implementations/cache-clean.ts" $args
exit $LASTEXITCODE
```

**BAT (.bat):**
```bat
@echo off
REM Thin orchestrator: delegates to PowerShell wrapper
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0cache-clean.ps1" %*
if errorlevel 1 exit /b %errorlevel%
```

### Business Logic in TypeScript

**Template Structure:**
```typescript
#!/usr/bin/env bun
import { DryRunExecutor } from '@/core/dry-run';
import { parseArgs } from '@/lib/cli';

async function main() {
  const { dryRun, ...options } = parseArgs(process.argv.slice(2));
  const executor = new DryRunExecutor(dryRun);
  
  // Business logic here
  await executor.removeFile('temp.log');
  
  process.exit(0);
}

main().catch(err => {
  console.error(err.message);
  process.exit(1);
});
```

## Safety Protocols

### AST Transformation Validation

**Required Before Any Transformation:**
- [ ] Generate visual AST comparison (original vs transformed)
- [ ] Run behavior-identical test suite on both versions
- [ ] Verify semantic equivalence (identical inputs → identical outputs)
- [ ] Maintain code coverage above 95%
- [ ] Require peer review for every AST transformation
- [ ] Document transformation rationale with before/after samples
- [ ] Create regression test suite for transformed functionality

### Dry-Run Fidelity Verification

**Process:**
- [ ] Compare dry-run output with real execution on identical test data
- [ ] Verify dry-run captures all side-effect checks (file writes, API calls, etc.)
- [ ] Document any differences between dry-run and real behavior
- [ ] **Fail if dry-run behavior diverges from real behavior**
- [ ] Test dry-run mode on new scripts before deploying real mode

### Behavior Parity

**Contract Preservation:**
- [ ] Create behavior test suite for each script (input→output mappings)
- [ ] Run test suite on original and refactored versions
- [ ] **Fail refactoring if behavior changes detected**
- [ ] If changes necessary, document approved behavior changes with explicit rationale
- [ ] Get 2-person sign-off for behavior modifications
- [ ] Create migration guide for scripts with behavior changes

### Dead Code Deletion

**30-Day Quarantine Process:**
1. Tag dead code with `// DEAD_CODE: marked for removal [DATE]`
2. Wait 30 days for late dependencies to surface
3. Search codebase for remaining references
4. Require written justification for each file deletion
5. Maintain deleted code archive for 6 months (in git history with tag)
6. Notify all dependent scripts/tests before final deletion
7. Require 2-person approval for irreversible deletion
8. Create git commit with clear explanation of what was removed and why

## Risk Distribution (from catalog)

**Total scripts analyzed:** 290+

| Risk Level | Count | Pattern |
|------------|-------|---------|
| HIGH RISK | 8 | `rm -rf`, `chmod`, `git branch -D` |
| MIGRATE | 21 | Operational scripts with business logic |
| KEEP | 68 | Library/reference/framework-required |
| DELETE | 149+ | Dead code, duplicates, one-shot artifacts |

### Priority 1 Safety Audit Results

**HIGH RISK Scripts Audited (3 examples):**

| Script | Pattern | Verdict |
|--------|---------|---------|
| `install.sh` | `rm -rf $TEMP_DIR` in trap | ✅ SAFE (temp cleanup only) |
| `diagnose-and-fix-git.sh` | `rm -f $LOCK_PATH` | ✅ SAFE (lock file removal) |
| `delete-gone-branches.sh` | `git branch -D` | ✅ SAFE (has dry-run by default, --apply required) |

**All Priority 1 scripts approved for TypeScript migration.**

## Migration Workflow

### Phase 1: Scaffold Migration

```bash
./Bash/Bash/migrate-script.sh cache-clean.sh
```

**Creates:**
- TypeScript implementation template
- Behavior test template
- Git checkpoint tag
- Thin wrapper conversion

### Phase 2: Implement TypeScript Logic

**Edit:** `Bash/src/implementations/cache-clean.ts`

**Pattern:**
```typescript
import { DryRunExecutor } from '@/core/dry-run';

async function main() {
  const dryRun = process.argv.includes('--dry-run');
  const executor = new DryRunExecutor(dryRun);
  
  // Original bash logic converted to TypeScript
  await executor.removeFile('~/.cache/bun');
  await executor.removeFile('~/.npm');
  
  console.log('Cache cleaned successfully');
}
```

### Phase 3: Create Behavior Tests

**Edit:** `Bash/tests/behavior/cache-clean.test.ts`

**Pattern:**
```typescript
import { BehaviorTestRunner } from '@/core/behavior-test';

const tester = new BehaviorTestRunner(
  'cache-clean',
  './cache-clean.sh',
  './dist/cache-clean.js'
);

tester.addTest({
  name: 'dry-run mode',
  args: ['--dry-run'],
  expectedExitCode: 0,
  expectedOutput: /Would remove/
});

await tester.runTests();
```

### Phase 4: Verify & Finalize

```bash
# Run behavior tests
bun test tests/behavior/cache-clean.test.ts

# Finalize migration
./Bash/Bash/finalize-migration.sh cache-clean
```

## Project Deliverables (from session)

**Architecture & Planning:**
- `plan/bash-scripts-architecture.md` (807 lines, 20.9 KB)
- `docs/bash-scripts-safety-audit.md` (16.8 KB)
- `docs/MIGRATION-GUIDE.md` (13.7 KB user tutorial)
- `docs/FINAL-SUMMARY.md` (11.8 KB completion report)

**Core Implementation:**
- `Bash/src/core/*.ts` (4 modules, verified functional)
- `Bash/Bash/*.sh` (3 migration utilities, executable)
- `Bash/tsconfig.json` + `Bash/package.json` (configured + deps installed)

**Test Infrastructure:**
- `Bash/src/core/__tests__/` (created, empty)
- `Bash/tests/behavior/` (created, empty)
- `Bash/tests/integration/` (created, empty)

## Lessons Learned

### Subagent Timeout → Direct Implementation

**Context:** Phase 1 subagent delegation timed out on large cataloging task (290+ files).

**Decision:** Switched to direct implementation for Phases 2-6.

**Result:** All phases completed faster than re-attempting delegation.

**Takeaway:** Reserve subagents for reasoning-heavy tasks (design, audits, reviews), not mechanical file enumeration.

### Bun Over Node.js

**Rationale:**
- 3x faster startup time for CLI scripts
- Native TypeScript support (no transpilation step)
- Smaller footprint (single binary)
- Compatible with npm packages

**Trade-off:** Bun-specific APIs (like `Bun.file()`) create vendor lock-in, but benefits outweigh for CLI tools.

### ts-morph Over Regex

**Rationale:**
- Type-safe transformations (compiler catches errors)
- AST awareness (understands code structure)
- Refactoring-safe (renames across files)

**Trade-off:** Heavier dependency (957 packages), but essential for safe large-scale migrations.

## Next Steps (User-Driven)

1. **Test first migration:** Run `./Bash/Bash/migrate-script.sh` on simple script like `cache-clean.sh`
2. **Implement TypeScript logic** in generated template
3. **Create behavior tests** comparing original vs. TypeScript output
4. **Run finalization** with `./Bash/Bash/finalize-migration.sh`
5. **Batch mark dead code** with `mark-dead-code.sh` (149+ scripts)
6. **Migrate priority scripts** (21 operational candidates)
7. **Monitor deletion queue** (30 days after marking)

## References

**Session artifacts:**
- Priority 1 safety audit verdicts
- TypeScript architecture specification
- Migration utilities (scaffold, finalize, mark-dead)
- Behavior test framework
- Dry-run executor patterns

**Related skills:**
- `dispatching-parallel-agents` — orchestration patterns
- `subagent-driven-development` — delegation workflows
- `systematic-debugging` — root cause analysis
- `simplify` — complexity reduction

**External dependencies:**
- ts-morph documentation: https://ts-morph.com/
- Bun runtime: https://bun.sh/
- ShellCheck: https://www.shellcheck.net/
