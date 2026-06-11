# Script Modernization Implementation Plan

**Created:** May 26, 2026  
**Task:** t_716b7e7f Phase 2  
**Scope:** Migrate 1,139 scripts to TypeScript-backed orchestrator architecture

## 1. Migration Strategy

### 1.1 Phased Rollout

**Phase A: Foundation (Week 1)**
- Set up TypeScript infrastructure
- Create ts-morph base utilities
- Implement dry-run framework
- Create test harness templates

**Phase B: High-Value Scripts (Week 2-3)**
- PowerShell orchestrators (Banking, 9 scripts)
- Large Bash scripts (phase-5-verify-install.sh, 5 scripts)
- Active utilities (3 scripts)

**Phase C: Batch Migration (Week 4-5)**
- ComicWise batch script (1 script)
- Remaining Bash utilities (consolidate into fewer scripts)

**Phase D: Cleanup (Week 6)**
- Archive/delete 26 commit batch scripts
- Consolidate duplicates
- Update documentation

**Phase E: TypeScript Scripts (Week 7-10)**
- Triage 1,092 TypeScript files in ComicWise
- Apply ts-morph patterns
- Eliminate dead code (932 uncategorized scripts)

### 1.2 Dependency Order

```
1. TypeScript infrastructure
   ↓
2. Common utilities (fs, exec, ast)
   ↓
3. Dry-run framework
   ↓
4. Banking PowerShell scripts (delegates to TS)
   ↓
5. Bash orchestrators (delegates to TS)
   ↓
6. ComicWise modernization
   ↓
7. Cleanup and consolidation
```

### 1.3 Priority Matrix

| Priority | Script Type | Count | Rationale |
|----------|-------------|-------|-----------|
| **P0** | Infrastructure | 0 → new | Required for all other work |
| **P1** | PowerShell orchestrators | 9 | Banking project, active use |
| **P2** | Large Bash scripts | 5 | High complexity, high value |
| **P3** | Small Bash utilities | 3 | Active, quick wins |
| **P4** | ComicWise batch | 1 | Single file, low risk |
| **P5** | Archived Bash | 26 | Consider deletion |
| **P6** | TypeScript triage | 1,092 | Massive scope, requires analysis |

## 2. Task Breakdown

### 2.1 Foundation Tasks (Phase A)

**Task A1: TypeScript Infrastructure Setup**
- Create `lib/core/` directory structure
- Set up tsconfig.json with strict mode
- Install dependencies: ts-morph, @types/node, commander, chalk
- Configure build pipeline (esbuild/tsc)

**Task A2: Common Utilities**
- `lib/core/fs-utils.ts` - File system operations with dry-run
- `lib/core/exec-utils.ts` - Shell command execution with dry-run
- `lib/core/ast-utils.ts` - ts-morph AST manipulation helpers
- `lib/core/logger.ts` - Structured logging with levels

**Task A3: Dry-run Framework**
- `lib/core/dry-run.ts` - Global dry-run state management
- `lib/core/preview.ts` - Change preview formatting
- Integration with fs-utils and exec-utils

**Task A4: Test Infrastructure**
- `tests/helpers/` - Test utilities
- `tests/fixtures/` - Sample files for testing
- Configure Vitest or Jest
- Create test templates

### 2.2 Banking PowerShell Scripts (Phase B, Priority 1)

**Task B1: orchestrator.ps1**
- Extract logic → `lib/banking/orchestrator.ts`
- Shell script becomes CLI wrapper
- Add dry-run support
- Tests: `tests/banking/orchestrator.test.ts`

**Task B2: verify-agents.ps1**
- Extract logic → `lib/banking/verify-agents.ts`
- Use ts-morph for agent config validation
- Add dry-run support
- Tests: `tests/banking/verify-agents.test.ts`

**Task B3: diagnose-and-fix-git.ps1**
- Extract logic → `lib/banking/git-diagnostics.ts`
- Use exec-utils for git commands
- Add dry-run support (show commands without executing)
- Tests: `tests/banking/git-diagnostics.test.ts`

**Task B4: opencode-*.ps1 scripts (3 files)**
- Consolidate into `lib/banking/opencode-manager.ts`
- Single entry point: `scripts/Banking/opencode.ps1`
- Subcommands: mcp, repair, verify
- Tests: `tests/banking/opencode-manager.test.ts`

**Task B5: plan-ensure.ps1 & run-verify-and-validate.ps1**
- Extract → `lib/banking/plan-validation.ts`
- Extract → `lib/banking/verification-runner.ts`
- Tests for both

### 2.3 Bash Scripts (Phase B, Priority 2-3)

**Task B6: phase-5-verify-install.sh**
- Extract → `lib/bash-utils/verify-install.ts`
- Shell wrapper: `Bash/scripts/verify-install.sh`
- Tests: `tests/bash-utils/verify-install.test.ts`

**Task B7: Other Bash/scripts/**
- Audit remaining 4 scripts
- Extract common patterns
- Consolidate where possible

**Task B8: Root utilities (upgrade.sh, etc.)**
- Extract → `lib/bash-utils/upgrade.ts`
- Shell wrappers remain minimal

### 2.4 ComicWise (Phase C, Priority 4)

**Task C1: Batch script migration**
- Identify batch script in comicwise/
- Convert to TypeScript entry point
- Create npm script in package.json

### 2.5 Cleanup (Phase D, Priority 5)

**Task D1: Archive commit batches**
- Review 26 archived scripts
- **Decision:** Archive or delete?
- Document in CHANGELOG.md

**Task D2: Consolidation**
- Merge duplicate logic across scripts
- Create shared utilities
- Update all scripts to use shared code

### 2.6 TypeScript Triage (Phase E, Priority 6)

**Task E1: Categorize 1,092 TypeScript files**
- Run AST analysis to categorize
- Identify dead code (no imports)
- Create categorization report

**Task E2: Apply ts-morph patterns**
- Refactor based on categories
- Extract common patterns
- Consolidate utilities

**Task E3: Dead code elimination**
- Remove unused exports
- Remove orphaned files
- Update package.json

## 3. TypeScript Module Design

### 3.1 Directory Structure

```
lib/
├── core/
│   ├── fs-utils.ts          # File operations
│   ├── exec-utils.ts        # Command execution
│   ├── ast-utils.ts         # ts-morph helpers
│   ├── dry-run.ts           # Dry-run state
│   ├── preview.ts           # Change previews
│   └── logger.ts            # Logging
├── banking/
│   ├── orchestrator.ts
│   ├── verify-agents.ts
│   ├── git-diagnostics.ts
│   ├── opencode-manager.ts
│   ├── plan-validation.ts
│   └── verification-runner.ts
├── bash-utils/
│   ├── verify-install.ts
│   └── upgrade.ts
└── comicwise/
    └── batch-runner.ts

tests/
├── core/
│   ├── fs-utils.test.ts
│   ├── exec-utils.test.ts
│   └── ast-utils.test.ts
├── banking/
│   └── *.test.ts
└── bash-utils/
    └── *.test.ts
```

### 3.2 Module Patterns

**Pattern 1: Command Module**
```typescript
// lib/banking/verify-agents.ts
import { DryRunContext } from '../core/dry-run';
import { execCommand } from '../core/exec-utils';
import { logger } from '../core/logger';

export interface VerifyAgentsOptions {
  configPath: string;
  fix?: boolean;
  dryRun?: boolean;
}

export async function verifyAgents(options: VerifyAgentsOptions): Promise<void> {
  const ctx = new DryRunContext(options.dryRun || false);
  
  logger.info('Verifying agents...', { configPath: options.configPath });
  
  // Check config file exists
  if (!ctx.fileExists(options.configPath)) {
    throw new Error(`Config not found: ${options.configPath}`);
  }
  
  // Run verification command
  const result = await ctx.exec('hermes verify-agents', { 
    cwd: path.dirname(options.configPath) 
  });
  
  if (result.exitCode !== 0) {
    logger.error('Verification failed', { output: result.output });
    if (options.fix && !options.dryRun) {
      await fixAgents(options);
    }
  }
  
  logger.success('Verification complete');
}
```

**Pattern 2: AST Transformation Module**
```typescript
// lib/core/ast-utils.ts
import { Project, SourceFile, SyntaxKind } from 'ts-morph';

export class ASTTransformer {
  private project: Project;
  
  constructor() {
    this.project = new Project();
  }
  
  public addSourceFile(filePath: string): SourceFile {
    return this.project.addSourceFileAtPath(filePath);
  }
  
  public removeUnusedImports(sourceFile: SourceFile): void {
    const importDeclarations = sourceFile.getImportDeclarations();
    
    for (const importDecl of importDeclarations) {
      const namedImports = importDecl.getNamedImports();
      
      for (const namedImport of namedImports) {
        const references = namedImport.findReferencesAsNodes();
        if (references.length === 1) { // Only the import itself
          namedImport.remove();
        }
      }
      
      if (importDecl.getNamedImports().length === 0) {
        importDecl.remove();
      }
    }
  }
  
  public async save(): Promise<void> {
    await this.project.save();
  }
}
```

### 3.3 Shell Orchestrator Pattern

**PowerShell orchestrator template:**
```powershell
# scripts/Banking/verify-agents.ps1
param(
    [string]$ConfigPath = "agents.config.json",
    [switch]$Fix,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

# Construct TypeScript command
$tsScript = "lib/banking/verify-agents.ts"
$args = @(
    "--config-path", $ConfigPath
)

if ($Fix) { $args += "--fix" }
if ($DryRun) { $args += "--dry-run" }

# Execute TypeScript module
tsx $tsScript @args

if ($LASTEXITCODE -ne 0) {
    Write-Error "verify-agents failed with exit code $LASTEXITCODE"
    exit $LASTEXITCODE
}
```

**Bash orchestrator template:**
```bash
#!/usr/bin/env bash
# Bash/scripts/verify-install.sh

set -euo pipefail

# Parse arguments
CONFIG_PATH="${1:-install.config.json}"
DRY_RUN="${2:-false}"

# Construct TypeScript command
TS_SCRIPT="lib/bash-utils/verify-install.ts"
ARGS=(
    "--config-path" "$CONFIG_PATH"
)

if [[ "$DRY_RUN" == "true" ]]; then
    ARGS+=("--dry-run")
fi

# Execute TypeScript module
tsx "$TS_SCRIPT" "${ARGS[@]}"
```

## 4. Dry-run Mode Specification

### 4.1 Core Dry-run Framework

```typescript
// lib/core/dry-run.ts
export class DryRunContext {
  private isDryRun: boolean;
  private changes: Change[] = [];
  
  constructor(dryRun: boolean = false) {
    this.isDryRun = dryRun;
  }
  
  public get enabled(): boolean {
    return this.isDryRun;
  }
  
  public fileExists(path: string): boolean {
    return fs.existsSync(path);
  }
  
  public async writeFile(path: string, content: string): Promise<void> {
    if (this.isDryRun) {
      this.changes.push({
        type: 'write',
        path,
        content,
        preview: content.substring(0, 200)
      });
      logger.info(`[DRY-RUN] Would write ${path}`, { bytes: content.length });
    } else {
      await fs.promises.writeFile(path, content, 'utf-8');
      logger.info(`Wrote ${path}`, { bytes: content.length });
    }
  }
  
  public async exec(command: string, options?: ExecOptions): Promise<ExecResult> {
    if (this.isDryRun) {
      this.changes.push({
        type: 'exec',
        command,
        options
      });
      logger.info(`[DRY-RUN] Would execute: ${command}`);
      return { exitCode: 0, output: '', dryRun: true };
    } else {
      return await execCommand(command, options);
    }
  }
  
  public getChanges(): Change[] {
    return this.changes;
  }
  
  public printSummary(): void {
    if (!this.isDryRun) return;
    
    console.log(chalk.yellow('\n=== DRY-RUN SUMMARY ===\n'));
    
    for (const change of this.changes) {
      if (change.type === 'write') {
        console.log(chalk.blue('WRITE:'), change.path);
        console.log(chalk.gray(`  ${change.preview}...`));
      } else if (change.type === 'exec') {
        console.log(chalk.green('EXEC:'), change.command);
      }
    }
    
    console.log(chalk.yellow(`\nTotal changes: ${this.changes.length}`));
    console.log(chalk.yellow('Run without --dry-run to apply.\n'));
  }
}

interface Change {
  type: 'write' | 'exec' | 'delete';
  path?: string;
  command?: string;
  content?: string;
  preview?: string;
  options?: any;
}
```

### 4.2 Integration Example

```typescript
// lib/banking/orchestrator.ts
import { DryRunContext } from '../core/dry-run';

export async function orchestrate(options: OrchestrateOptions): Promise<void> {
  const ctx = new DryRunContext(options.dryRun);
  
  // Read config
  const config = JSON.parse(await fs.promises.readFile(options.configPath, 'utf-8'));
  
  // Update config
  config.lastRun = new Date().toISOString();
  await ctx.writeFile(options.configPath, JSON.stringify(config, null, 2));
  
  // Run commands
  await ctx.exec('npm run build');
  await ctx.exec('npm test');
  
  // Print summary if dry-run
  ctx.printSummary();
}
```

## 5. Testing Strategy

### 5.1 Test Structure

```
tests/
├── unit/               # Pure function tests
│   ├── core/
│   ├── banking/
│   └── bash-utils/
├── integration/        # Multi-module tests
│   └── end-to-end/
└── fixtures/           # Test data
    ├── configs/
    └── sample-files/
```

### 5.2 Test Template

```typescript
// tests/banking/verify-agents.test.ts
import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { verifyAgents } from '../../lib/banking/verify-agents';
import * as fs from 'fs/promises';
import * as path from 'path';

describe('verifyAgents', () => {
  const testDir = path.join(__dirname, '../fixtures/banking');
  const configPath = path.join(testDir, 'agents.config.json');
  
  beforeEach(async () => {
    // Setup test fixture
    await fs.mkdir(testDir, { recursive: true });
    await fs.writeFile(configPath, JSON.stringify({
      agents: ['agent1', 'agent2']
    }, null, 2));
  });
  
  afterEach(async () => {
    // Cleanup
    await fs.rm(testDir, { recursive: true, force: true });
  });
  
  it('should verify agents successfully', async () => {
    await expect(verifyAgents({ 
      configPath,
      dryRun: true 
    })).resolves.not.toThrow();
  });
  
  it('should throw if config missing', async () => {
    await expect(verifyAgents({ 
      configPath: 'nonexistent.json',
      dryRun: true 
    })).rejects.toThrow('Config not found');
  });
  
  it('should support dry-run mode', async () => {
    const result = await verifyAgents({ 
      configPath,
      dryRun: true 
    });
    
    // Verify no actual changes
    const config = JSON.parse(await fs.readFile(configPath, 'utf-8'));
    expect(config.lastRun).toBeUndefined();
  });
});
```

### 5.3 Coverage Goals

- **Unit tests:** 80%+ coverage for core modules
- **Integration tests:** All major workflows
- **Dry-run tests:** Every destructive operation
- **Error cases:** All error paths tested

## 6. Code Samples

### 6.1 Before: Bash with Business Logic

```bash
#!/usr/bin/env bash
# Bash/scripts/phase-5-verify-install.sh (BEFORE)

set -euo pipefail

echo "Verifying installation..."

# Check Node.js version
NODE_VERSION=$(node --version | cut -d'v' -f2)
MAJOR_VERSION=$(echo $NODE_VERSION | cut -d'.' -f1)

if [ "$MAJOR_VERSION" -lt 18 ]; then
    echo "Error: Node.js 18+ required, found $NODE_VERSION"
    exit 1
fi

# Check npm packages
MISSING_PACKAGES=()
for pkg in "tsx" "ts-morph" "commander"; do
    if ! npm list -g $pkg &>/dev/null; then
        MISSING_PACKAGES+=("$pkg")
    fi
done

if [ ${#MISSING_PACKAGES[@]} -gt 0 ]; then
    echo "Missing packages: ${MISSING_PACKAGES[*]}"
    exit 1
fi

echo "Installation verified successfully"
```

### 6.2 After: Orchestrator + TypeScript

**TypeScript module:**
```typescript
// lib/bash-utils/verify-install.ts
import { Command } from 'commander';
import { execCommand } from '../core/exec-utils';
import { logger } from '../core/logger';
import { DryRunContext } from '../core/dry-run';

export interface VerifyInstallOptions {
  minNodeVersion?: number;
  requiredPackages?: string[];
  dryRun?: boolean;
}

export async function verifyInstall(options: VerifyInstallOptions): Promise<void> {
  const ctx = new DryRunContext(options.dryRun || false);
  const minVersion = options.minNodeVersion || 18;
  const packages = options.requiredPackages || ['tsx', 'ts-morph', 'commander'];
  
  logger.info('Verifying installation...');
  
  // Check Node.js version
  const nodeVersionResult = await ctx.exec('node --version');
  const nodeVersion = nodeVersionResult.output.replace('v', '').trim();
  const majorVersion = parseInt(nodeVersion.split('.')[0], 10);
  
  if (majorVersion < minVersion) {
    throw new Error(`Node.js ${minVersion}+ required, found ${nodeVersion}`);
  }
  logger.success(`Node.js version OK: ${nodeVersion}`);
  
  // Check npm packages
  const missingPackages: string[] = [];
  for (const pkg of packages) {
    const result = await ctx.exec(`npm list -g ${pkg}`);
    if (result.exitCode !== 0) {
      missingPackages.push(pkg);
    }
  }
  
  if (missingPackages.length > 0) {
    throw new Error(`Missing packages: ${missingPackages.join(', ')}`);
  }
  logger.success(`All packages installed: ${packages.join(', ')}`);
  
  logger.success('Installation verified successfully');
}

// CLI entry point
if (require.main === module) {
  const program = new Command();
  
  program
    .name('verify-install')
    .description('Verify installation requirements')
    .option('--min-node-version <version>', 'Minimum Node.js version', '18')
    .option('--required-packages <packages>', 'Comma-separated package list')
    .option('--dry-run', 'Preview without executing')
    .action(async (options) => {
      try {
        await verifyInstall({
          minNodeVersion: parseInt(options.minNodeVersion, 10),
          requiredPackages: options.requiredPackages?.split(','),
          dryRun: options.dryRun
        });
        process.exit(0);
      } catch (error) {
        logger.error('Verification failed', { error });
        process.exit(1);
      }
    });
  
  program.parse();
}
```

**Shell orchestrator (minimal):**
```bash
#!/usr/bin/env bash
# Bash/scripts/verify-install.sh (AFTER)

set -euo pipefail

# Delegate to TypeScript
tsx lib/bash-utils/verify-install.ts "$@"
```

### 6.3 ts-morph AST Manipulation Example

```typescript
// lib/core/ast-utils.ts - Example: Remove unused imports
import { Project, SourceFile, SyntaxKind } from 'ts-morph';
import { DryRunContext } from './dry-run';

export async function removeUnusedImports(
  filePath: string,
  ctx: DryRunContext
): Promise<void> {
  const project = new Project();
  const sourceFile = project.addSourceFileAtPath(filePath);
  
  const importDeclarations = sourceFile.getImportDeclarations();
  const removed: string[] = [];
  
  for (const importDecl of importDeclarations) {
    const namedImports = importDecl.getNamedImports();
    
    for (const namedImport of namedImports) {
      const name = namedImport.getName();
      const references = namedImport.findReferencesAsNodes();
      
      // If only referenced once (the import itself), it's unused
      if (references.length === 1) {
        if (ctx.enabled) {
          removed.push(name);
        }
        namedImport.remove();
      }
    }
    
    // Remove entire import if no named imports left
    if (importDecl.getNamedImports().length === 0) {
      importDecl.remove();
    }
  }
  
  if (ctx.enabled) {
    logger.info(`[DRY-RUN] Would remove unused imports from ${filePath}`, { 
      removed 
    });
  } else {
    await sourceFile.save();
    logger.info(`Removed unused imports from ${filePath}`, { removed });
  }
}
```

## 7. File Reference Manifest

### 7.1 New Files to Create

**Core infrastructure:**
```
lib/core/fs-utils.ts
lib/core/exec-utils.ts
lib/core/ast-utils.ts
lib/core/dry-run.ts
lib/core/preview.ts
lib/core/logger.ts
```

**Banking modules:**
```
lib/banking/orchestrator.ts
lib/banking/verify-agents.ts
lib/banking/git-diagnostics.ts
lib/banking/opencode-manager.ts
lib/banking/plan-validation.ts
lib/banking/verification-runner.ts
```

**Bash utilities:**
```
lib/bash-utils/verify-install.ts
lib/bash-utils/upgrade.ts
```

**Tests:**
```
tests/core/*.test.ts
tests/banking/*.test.ts
tests/bash-utils/*.test.ts
tests/helpers/test-utils.ts
tests/fixtures/*
```

**Configuration:**
```
tsconfig.json
vitest.config.ts
.gitignore (update)
```

### 7.2 Files to Modify

**Shell scripts (convert to orchestrators):**
```
rhixecompany/Banking/scripts/orchestrator.ps1
rhixecompany/Banking/scripts/verify-agents.ps1
rhixecompany/Banking/scripts/diagnose-and-fix-git.ps1
rhixecompany/Banking/scripts/opencode-mcp.ps1
rhixecompany/Banking/scripts/opencode-plugin-repair.ps1
rhixecompany/Banking/scripts/opencode-plugin-verify.ps1
rhixecompany/Banking/scripts/plan-ensure.ps1
rhixecompany/Banking/scripts/run-verify-and-validate.ps1
Bash/scripts/phase-5-verify-install.sh
Bash/upgrade.sh
(+ 3 other Bash scripts)
```

**Package.json:**
```
Add dependencies: ts-morph, commander, chalk, @types/node
Add devDependencies: vitest, @types/vitest, tsx
Add scripts: test, build, lint
```

### 7.3 Files to Delete/Archive

**After review and migration:**
```
Bash/archive_batch_*_commits/*.sh (26 files)
(Any other dead code identified in Phase E)
```

## 8. Package.json Updates

```json
{
  "name": "sandbox-scripts",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "build": "tsc",
    "test": "vitest run",
    "test:watch": "vitest",
    "test:coverage": "vitest run --coverage",
    "lint": "eslint lib/ tests/",
    "format": "prettier --write lib/ tests/"
  },
  "dependencies": {
    "ts-morph": "^21.0.0",
    "commander": "^11.0.0",
    "chalk": "^5.3.0"
  },
  "devDependencies": {
    "@types/node": "^20.10.0",
    "vitest": "^1.0.0",
    "@vitest/coverage-v8": "^1.0.0",
    "tsx": "^4.7.0",
    "typescript": "^5.3.0",
    "eslint": "^8.56.0",
    "prettier": "^3.1.0"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
```

## 9. Success Criteria

### 9.1 Per-Script Criteria

✓ **Each shell script must:**
- Be minimal orchestrator (< 20 lines)
- Delegate all logic to TypeScript
- Support --dry-run flag
- Support --help flag
- Exit with appropriate codes
- Have no business logic

✓ **Each TypeScript module must:**
- Have single responsibility
- Use DryRunContext for all mutations
- Have 80%+ test coverage
- Use ts-morph for AST operations
- Export testable functions
- Have CLI entry point with commander

### 9.2 Phase Completion Criteria

**Phase A Complete when:**
- [ ] TypeScript builds with zero errors
- [ ] Core utilities have 90%+ coverage
- [ ] Dry-run framework works across all utility modules
- [ ] Test infrastructure runs successfully

**Phase B Complete when:**
- [ ] All 9 Banking scripts migrated
- [ ] All 5 large Bash scripts migrated
- [ ] All 3 utility scripts migrated
- [ ] All tests passing
- [ ] Dry-run mode works for all scripts

**Phase C Complete when:**
- [ ] ComicWise batch script migrated
- [ ] Tests passing

**Phase D Complete when:**
- [ ] Archived scripts reviewed (delete or keep decision)
- [ ] Duplicates consolidated
- [ ] CHANGELOG.md updated

**Phase E Complete when:**
- [ ] 1,092 TypeScript files categorized
- [ ] Dead code removed
- [ ] ts-morph patterns applied
- [ ] Test coverage > 70%

### 9.3 Overall Success Criteria

**Project complete when:**
1. All shell scripts are orchestrators only
2. All business logic in TypeScript
3. Dry-run mode works universally
4. 80%+ test coverage overall
5. Zero dead code
6. All tests passing
7. Documentation updated
8. CHANGELOG.md complete

## 10. Risk Mitigation

### 10.1 Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Breaking existing workflows | HIGH | Dry-run testing, backwards compatibility shims |
| Test coverage insufficient | MEDIUM | Require 80% minimum, review gates |
| ts-morph learning curve | MEDIUM | Start with simple examples, build library |
| ComicWise scope explosion | HIGH | Time-box Phase E, focus on high-value wins |
| Dependencies outdated | LOW | Pin versions, test before upgrading |

### 10.2 Rollback Plan

**If migration fails:**
1. Git revert to pre-migration state
2. Document lessons learned
3. Re-plan with smaller scope
4. Pilot with single script category

### 10.3 Validation Gates

**Pre-flight (before starting each phase):**
- Review plan
- Dependencies installed
- Tests pass
- Workspace clean

**Revision (after each task):**
- Tests pass
- Dry-run works
- Code reviewed
- Documentation updated

**Escalation (if stuck):**
- Block task with reason
- Gather context
- Request guidance
- Don't guess

**Abort (if fundamentally wrong):**
- Stop work
- Document issues
- Propose alternative
- Get approval to continue

---

## Appendix A: Command Reference

### A.1 Development Commands

```bash
# Install dependencies
npm install

# Run tests
npm test

# Run tests in watch mode
npm run test:watch

# Generate coverage report
npm run test:coverage

# Build TypeScript
npm run build

# Lint code
npm run lint

# Format code
npm run format
```

### A.2 Migration Commands

```bash
# Test a single script migration (dry-run)
tsx lib/banking/verify-agents.ts --dry-run

# Run migrated script
./rhixecompany/Banking/scripts/verify-agents.ps1 --dry-run

# Verify all scripts
npm test

# Build and validate
npm run build && npm test
```

---

## Appendix B: Resources

- **ts-morph docs:** https://ts-morph.com/
- **commander docs:** https://github.com/tj/commander.js
- **vitest docs:** https://vitest.dev/
- **TypeScript handbook:** https://www.typescriptlang.org/docs/

---

**End of Implementation Plan**
