---
title: Bash Scripts — Migration Guide
description: Step-by-step guide for migrating operational scripts into the Bash/ canonical location.
status: final
tags: [migration, guide, bash, canonical-location]
updated: 2026-05-27
---

     1|# Bash Scripts Modernization — User Guide
     2|
     3|**Welcome!** This guide will walk you through modernizing bash/PowerShell/batch scripts to TypeScript using the framework created in this project.
     4|
     5|---
     6|
     7|## Table of Contents
     8|
     9|1. [What is This Framework?](#what-is-this-framework)
    10|2. [Why TypeScript?](#why-typescript)
    11|3. [Getting Started](#getting-started)
    12|4. [Migrating Your First Script](#migrating-your-first-script)
    13|5. [Understanding Dry-Run Mode](#understanding-dry-run-mode)
    14|6. [Testing for Behavior Preservation](#testing-for-behavior-preservation)
    15|7. [Marking Dead Code](#marking-dead-code)
    16|8. [Troubleshooting](#troubleshooting)
    17|9. [Next Steps](#next-steps)
    18|
    19|---
    20|
    21|## What is This Framework?
    22|
    23|This framework helps you modernize shell scripts (bash, PowerShell, bat) into TypeScript while:
    24|- ✅ Preserving exact behavior (input→output equivalence)
    25|- ✅ Adding dry-run safety for destructive operations
    26|- ✅ Improving maintainability (TypeScript type safety)
    27|- ✅ Keeping thin shell wrappers (no breaking changes for users)
    28|
    29|**Architecture:**
    30|```
    31|Shell Script (thin wrapper) → TypeScript Implementation (all logic)
    32|```
    33|
    34|Example:
    35|```bash
    36|# upgrade.sh (5 lines)
    37|#!/usr/bin/env bash
    38|set -euo pipefail
    39|SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    40|bun run "$SCRIPT_DIR/src/upgrade.ts" "$@"
    41|```
    42|
    43|```typescript
    44|// src/upgrade.ts (50 lines with type safety, error handling, tests)
    45|import { withDryRun } from '@/core/dry-run';
    46|// ... full implementation
    47|```
    48|
    49|---
    50|
    51|## Why TypeScript?
    52|
    53|| Before (Bash) | After (TypeScript) |
    54||---------------|-------------------|
    55|| No type checking | Type-safe parameters |
    56|| Error handling is manual | Built-in error types |
    57|| Hard to test | Easy to unit test |
    58|| No IDE autocomplete | Full IntelliSense |
    59|| Complex string manipulation | Native data structures |
    60|
    61|**You still keep the shell wrapper** — so existing usage doesn't change:
    62|```bash
    63|$ ./upgrade.sh --dry-run  # Still works exactly the same!
    64|```
    65|
    66|---
    67|
    68|## Getting Started
    69|
    70|### Prerequisites
    71|
    72|- **Bun** (JavaScript runtime) — Install: `curl -fsSL https://bun.sh/install | bash`
    73|- **Git** (version control)
    74|- **Basic TypeScript knowledge** (optional, but helpful)
    75|
    76|### Install Dependencies
    77|
    78|```bash
    79|cd Bash
    80|bun install
    81|```
    82|
    83|This installs:
    84|- `ts-morph` — For AST transformations
    85|- `bun-types` — TypeScript definitions
    86|- `prettier` — Code formatting
    87|- `typescript` — Type checking
    88|
    89|---
    90|
    91|## Migrating Your First Script
    92|
    93|Let's migrate a simple script step-by-step.
    94|
    95|### Example: Migrating `hello.sh`
    96|
    97|**Original Script:**
    98|```bash
    99|#!/usr/bin/env bash

100|set -euo pipefail 101| 102|NAME="${1:-World}"
   103|echo "Hello, $NAME!"
   104|```
   105|
   106|### Step 1: Run Migration Tool
   107|
   108|```bash
   109|cd Bash
   110|./Bash/migrate-script.sh path/to/hello.sh
   111|```
   112|
   113|**Output:**
   114|```
   115|🔄 Migrating: path/to/hello.sh → TypeScript
   116|📝 Generating TypeScript implementation...
   117|📝 Creating bash orchestrator...
   118|📝 Generating behavior test stub...
   119|
   120|✅ Migration scaffolding created:
   121|   TypeScript: src/scripts/hello.ts
   122|   Orchestrator: scripts/hello.sh
   123|   Tests: tests/behavior/hello.test.ts
   124|
   125|⚠️  MANUAL STEPS REQUIRED:
   126|   1. Implement logic in src/scripts/hello.ts
   127|   2. Add behavior tests in tests/behavior/hello.test.ts
   128|   3. Run: bun test tests/behavior/hello.test.ts
   129|   4. If tests pass, run: ./finalize-migration.sh path/to/hello.sh
   130|```
   131|
   132|### Step 2: Implement TypeScript Logic
   133|
   134|Edit `src/scripts/hello.ts`:
   135|
   136|```typescript
   137|#!/usr/bin/env bun
   138|import { withDryRun, DryRunExecutor } from '@/core/dry-run';
   139|
   140|interface HelloOptions {
   141|  dryRun?: boolean;
   142|  name?: string;
   143|}
   144|
   145|async function helloImpl(
   146|  opts: HelloOptions,
   147|  executor: DryRunExecutor
   148|): Promise<void> {
   149|  const name = opts.name ?? 'World';
   150|  console.log(`Hello, ${name}!`);
   151|}
   152|
   153|// CLI entry point
   154|if (import.meta.main) {
   155|  const args = process.argv.slice(2);
   156|  const opts: HelloOptions = {
   157|    dryRun: args.includes('--dry-run'),
   158|    name: args.find((arg) => !arg.startsWith('--')),
   159|  };
   160|
   161|  const wrappedImpl = withDryRun(helloImpl);
   162|  await wrappedImpl(opts);
   163|}
   164|
   165|export { helloImpl };
   166|```
   167|
   168|### Step 3: Add Behavior Tests
   169|
   170|Edit `tests/behavior/hello.test.ts`:
   171|
   172|```typescript
   173|import { test, expect } from 'bun:test';
   174|import { BehaviorTester } from '@/core/behavior-test';
   175|
   176|test('hello behavior preservation', async () => {
   177|  await BehaviorTester.verifyBehavior(
   178|    'path/to/hello.sh',
   179|    'scripts/hello.sh',
   180|    [
   181|      {
   182|        name: 'default name',
   183|        input: {},
   184|        expectedOutput: 'Hello, World!\n',
   185|        expectedExitCode: 0,
   186|      },
   187|      {
   188|        name: 'custom name',
   189|        input: { name: 'Alice' },
   190|        expectedOutput: 'Hello, Alice!\n',
   191|        expectedExitCode: 0,
   192|      },
   193|    ]
   194|  );
   195|});
   196|```
   197|
   198|### Step 4: Run Tests
   199|
   200|```bash
   201|bun test tests/behavior/hello.test.ts
   202|```
   203|
   204|**Expected Output:**
   205|```
   206|✓ hello behavior preservation > default name
   207|✓ hello behavior preservation > custom name
   208|
   209|2 tests passed (0.05s)
   210|```
   211|
   212|### Step 5: Finalize Migration
   213|
   214|If tests pass:
   215|
   216|```bash
   217|./Bash/finalize-migration.sh path/to/hello.sh
   218|```
   219|
   220|**Output:**
   221|```
   222|🔄 Finalizing migration: hello
   223|🧪 Running behavior tests...
   224|✓ All tests passed
   225|🗑️  Deleting original script: path/to/hello.sh
   226|✅ Migration complete: hello
   227|   Original script deleted: path/to/hello.sh
   228|   New orchestrator: scripts/hello.sh
   229|```
   230|
   231|**Done!** Your script is now:
   232|- ✅ TypeScript-based (type-safe, testable)
   233|- ✅ Behavior-preserved (tests prove equivalence)
   234|- ✅ User-facing interface unchanged (`scripts/hello.sh` still works)
   235|
   236|---
   237|
   238|## Understanding Dry-Run Mode
   239|
   240|**Dry-run mode** is a safety feature that previews destructive operations without executing them.
   241|
   242|### When to Use Dry-Run
   243|
   244|Use dry-run for operations that:
   245|- Write or delete files
   246|- Modify permissions (chmod)
   247|- Execute git commands (commit, push, delete branches)
   248|- Make network requests (POST, DELETE)
   249|
   250|### Example: File Deletion with Dry-Run
   251|
   252|```typescript
   253|import { DryRunExecutor } from '@/core/dry-run';
   254|
   255|interface CleanupOptions {
   256|  dryRun?: boolean;
   257|  path: string;
   258|}
   259|
   260|async function cleanupImpl(
   261|  opts: CleanupOptions,
   262|  executor: DryRunExecutor
   263|): Promise<void> {
   264|  // Use executor for destructive operations
   265|  await executor.deleteFile(opts.path);
   266|}
   267|```
   268|
   269|**Usage:**
   270|
   271|```bash
   272|# Preview what would be deleted (safe)
   273|$ ./cleanup.sh /tmp/old-file.txt --dry-run 274|[DRY RUN] file-delete: Delete file: /tmp/old-file.txt 275| Args: { "path": "/tmp/old-file.txt" } 276| 277|# Actually delete (requires explicit confirmation) 278|$ ./cleanup.sh /tmp/old-file.txt 279|File deleted: /tmp/old-file.txt 280|``    281|    282|### Dry-Run Best Practices    283|    284|1. **Always test dry-run first** before running for real    285|2. **Use executor methods** for all destructive operations:    286|   - `executor.writeFile(path, content)`    287|   - `executor.deleteFile(path)`    288|   - `executor.exec(command, args)`    289|3. **Compare dry-run vs real output** in tests (should be identical logic)    290|    291|---    292|    293|## Testing for Behavior Preservation    294|    295|**Behavior preservation** means: refactored script produces identical output to original.    296|    297|### Why This Matters    298|    299|❌ **Bad refactoring:**    300|``bash 301|# Original: "File created: /tmp/test.txt" 302|# Refactored: "Created file at /tmp/test.txt" 303|`    304|Different output = broken scripts that depend on parsing output!    305|    306|✅ **Good refactoring:**    307|`bash 308|# Original: "File created: /tmp/test.txt" 309|# Refactored: "File created: /tmp/test.txt" 310|`    311|Identical output = no breaking changes.    312|    313|### Writing Behavior Tests    314|    315|`typescript 316|import { BehaviorTester } from '@/core/behavior-test'; 317| 318|await BehaviorTester.verifyBehavior( 319| 'old-script.sh', 320| 'new-script.sh', 321| [ 322| { 323| name: 'test case description', 324| input: { arg1: 'value1', arg2: 'value2' }, 325| expectedOutput: 'exact output string', 326| expectedExitCode: 0, 327| }, 328| ] 329|); 330|`    331|    332|### Test Checklist    333|    334|For every migrated script:    335|- [ ] Test normal execution (happy path)    336|- [ ] Test error cases (invalid input)    337|- [ ] Test dry-run mode (if applicable)    338|- [ ] Test edge cases (empty input, large input)    339|    340|---    341|    342|## Marking Dead Code    343|    344|**Dead code** = scripts no longer used, but kept "just in case."    345|    346|### The Problem with Dead Code    347|    348|- ❌ Clogs up repository (hard to find active scripts)    349|- ❌ Misleading (looks operational, but isn't)    350|- ❌ Wastes time (maintaining code nobody uses)    351|    352|### The Solution: 30-Day Quarantine    353|    354|Instead of deleting immediately, mark for deletion with a 30-day review period:    355|    356|`bash 357|./Bash/mark-dead-code.sh path/to/old-script.sh 358|``    359|    360|**What This Does:**    361|1. Adds marker comment to file: `# DEAD_CODE: marked for removal 2026-05-27`    362|2. Commits with explanation: "Mark for deletion (30-day quarantine)"    363|3. Tags in git: `dead-code/old-script.sh/2026-05-27`    364|    365|### After 30 Days    366|    367|If nobody complained (no references found):    368|1. Search codebase for any usage: `git grep old-script`    369|2. Get 2-person approval (confirm safe to delete)    370|3. Delete file: `git rm path/to/old-script.sh`    371|4. Commit: "Delete old-script.sh after 30-day quarantine"    372|    373|### Recovering Marked Files    374|    375|**Need it back?**    376|``bash 377|# Find the tag 378|git tag -l "dead-code/_" 379| 380|# Restore from tag 381|git checkout tags/dead-code/old-script.sh/2026-05-27 -- path/to/old-script.sh 382| 383|# Remove the marker 384|sed -i '1d' path/to/old-script.sh # Remove first line (marker) 385|git commit -m "Restore old-script.sh (still needed)" 386|`    387|    388|---    389|    390|## Troubleshooting    391|    392|### Issue: "Git working directory has uncommitted changes"    393|    394|**Cause:** AST transformer requires clean git state (safety protocol).    395|    396|**Solution:**    397|`bash 398|# Option 1: Commit your changes 399|git add . 400|git commit -m "WIP: current work" 401| 402|# Option 2: Stash your changes 403|git stash 404|`    405|    406|### Issue: "Behavior tests failing"    407|    408|**Cause:** Refactored script output doesn't match original.    409|    410|**Solution:**    411|1. Run both scripts manually to see difference:    412|   `bash 413| ./old-script.sh --test > old-output.txt 414| ./new-script.sh --test > new-output.txt 415| diff old-output.txt new-output.txt 416| `    417|2. Fix TypeScript implementation to match original output exactly    418|3. Re-run tests    419|    420|### Issue: "Module not found: @/core/dry-run"    421|    422|**Cause:** TypeScript path aliases not configured.    423|    424|**Solution:**    425|`bash 426|# Verify tsconfig.json has baseUrl and paths: 427|cat Bash/tsconfig.json | grep -A 3 "baseUrl" 428| 429|# Should show: 430|# "baseUrl": ".", 431|# "paths": { 432|# "@/_": ["./src/*"] 433|# } 434|`    435|    436|### Issue: "Dry-run mode doesn't work"    437|    438|**Cause:** Script not using DryRunExecutor for operations.    439|    440|**Solution:**    441|`typescript 442|// ❌ Wrong: Direct file operations 443|await writeFile('/tmp/test.txt', 'content'); 444| 445|// ✅ Correct: Use executor 446|await executor.writeFile('/tmp/test.txt', 'content'); 447|``    448|    449|---    450|    451|## Next Steps    452|    453|### Migrate More Scripts    454|    455|Use the workflow from "Migrating Your First Script" for:    456|- Operational scripts (generic tools → migrate to `Bash/`)    457|- Project-specific scripts (keep in place, still benefit from TypeScript)    458|    459|### Clean Up Dead Code    460|    461|1. Review scripts marked "DELETE" in Phase 1 catalog (149+ scripts)    462|2. Batch mark for 30-day quarantine:    463|   ``bash 464| for script in $(cat docs/dead-code-list.txt); do
   465|     ./Bash/mark-dead-code.sh "$script" 466| done 467| ```   468|3. Set calendar reminder for 30 days from now    469|    470|### Improve Core Modules    471|    472|Enhance the framework as needed:    473|- Add more executor methods (chmod, chown, network requests)    474|- Improve error messages    475|- Add progress bars for long operations    476|- Create template generators for common patterns    477|    478|### Share Your Experience    479|    480|If you improve this framework:    481|1. Document your changes (add to this guide)    482|2. Submit a pull request (help others)    483|3. Write a blog post (teach the community)    484|    485|---    486|    487|## Resources    488|    489|- **Architecture Doc:**`plan/bash-scripts-architecture.md`— Technical design details    490|- **Safety Audit:**`docs/bash-scripts-safety-audit.md`— Security review    491|- **Phase 1 Catalog:**`docs/bash-scripts-list-context.md`— Script inventory    492|- **Verification Report:**`docs/phase5-verification-report.md` — Implementation status 493| 494|**Questions?** Open an issue or ask in discussions. 495| 496|**Happy Modernizing!** 🚀 497|
