# Wrapper Delegation Discovery & Verification

## Overview

When normalizing wrapper families, you must first identify the **canonical runner** that the thin wrapper should delegate to. This is discovered from the package manifest or entrypoint configuration.

## Discovery Pattern

### Step 1: Check Package Manifest

Examine the package manager configuration to identify command mappings:

| Package Manager | Files to Check | Command Mapping |
|---|---|---|
| npm/pnpm | `package.json` | `"scripts": { "command": "runner ..." }` |
| Bun | `bunfig.toml` or `package.json` | Same as npm/pnpm; Bun uses package.json scripts |
| Make | `Makefile` | `.PHONY: target` and `target: command` |
| Custom runners | `Dockerfile`, `.github/workflows/`, shell source | May require inspecting shell sourcing or CI config |

### Step 2: Trace the Command

Once identified, trace the command to find the actual runner:

```bash
# Example: Comicwise
$ grep '"dev":' package.json
"dev": "cross-env NODE_OPTIONS='--max-old-space-size=4096' next dev",

# The runner is 'next dev' (Next.js dev server)
# Thin wrapper should delegate to: pnpm dev
```

```bash
# Example: Comicwise setup
$ grep '"setup":' package.json
"setup": "tsx src/scripts/unified-dev-setup.ts",

# The runner is 'tsx src/scripts/unified-dev-setup.ts' (TypeScript runner)
# Thin wrapper should delegate to: pnpm setup
```

### Step 3: Verify Runner Exists

Before converting the wrapper, confirm the runner:
- Is executable or callable
- Exists at the path specified
- Accepts the flags/arguments the wrapper intends to forward

```bash
# For pnpm commands, verify in package.json
$ pnpm run --help     # Shows available scripts

# For TypeScript runners, check the file exists
$ ls -la src/scripts/unified-dev-setup.ts

# For executables, check in PATH
$ which next
```

## Verification Pattern: Delegation Testing

After creating thin wrappers, verify delegation works correctly:

### Test 1: Help Output

```bash
# Test bash wrapper
./dev.sh --help

# Test PowerShell wrapper
.\dev.ps1 -Help

# Test BAT wrapper
dev.bat -help
```

**Expected**: Help output from the canonical runner (not from the wrapper itself).

### Test 2: Argument Forwarding

```bash
# Pass a meaningful flag through the wrapper
./dev.sh --dry-run --verbose

# Verify the canonical runner receives it
# (Look for --dry-run in runner output or behavior)
```

**Expected**: Arguments reach the runner unchanged; wrapper does not intercept or modify them.

### Test 3: Exit Code Propagation

```bash
# Run with a non-existent/invalid argument
./dev.sh nonexistent

# Check exit code
echo $?

# Run the canonical runner directly with same argument
pnpm dev nonexistent
echo $?

# Compare exit codes
```

**Expected**: Wrapper exit code matches canonical runner exit code exactly.

### Test 4: Size/Complexity Baseline

After normalization, measure wrapper reduction:

```bash
# Before: measure original wrapper
wc -l dev.sh.original    # 174 lines

# After: measure new wrapper
wc -l dev.sh              # 30 lines

# Calculate reduction
# (174 - 30) / 174 × 100 = 82.8% reduction
```

**Expected**: Thin wrappers should be ≤40 lines; reductions of 70%+ are common when moving business logic to canonical runners.

## Batch Execution Checklist

When normalizing a wrapper family that delegates to a canonical runner:

1. **Discover the canonical runner** — Check package.json / Makefile / config
2. **Trace the command** — Identify the actual entrypoint (e.g., `next dev`, `tsx src/scripts/...`)
3. **Verify runner exists** — Confirm file/command is callable and accepts expected flags
4. **Create thin wrapper** — Implement standard contract (accept all args, forward to runner, propagate exit code)
5. **Verify delegation**:
   - [ ] Help output shows runner help, not wrapper help
   - [ ] Arguments forward unchanged (test with `--flag value`)
   - [ ] Exit codes match canonical runner (test with invalid args)
6. **Measure impact** — Record before/after line counts and reduction percentage
7. **Update progress log** — Include delegation target and size reduction metrics
8. **Test in context** — If possible, run the wrapper end-to-end to confirm behavior is preserved

## Pitfalls

- **Missing runner**: Wrapper delegates to a command that no longer exists or moved. Always verify file/command exists before creating the wrapper.
- **Silent delegation failures**: A wrapper that silently fails (e.g., runner exits 0 but does nothing) is a sign the delegation target is wrong. Test help output and at least one meaningful flag to catch this early.
- **Partial argument forwarding**: PowerShell and Batch have different splatting semantics. Always test with multi-argument flags (e.g., `--flag=value` vs `--flag value`) to catch edge cases.
- **Exit code mismatch**: Most common with PowerShell when using `try/catch`. Remember to use `exit $LASTEXITCODE` (not just `$LASTEXITCODE`) to propagate the runner's exit code.
- **Stale runner references**: If a runner was renamed or moved, the thin wrapper still references the old path. Update discovery and re-test after any package manifest changes.

## Related Patterns

- **Wrapper orchestration contract**: See `references/wrapper-orchestration-contract.md` for cross-platform implementation details
- **Batch verification workflow**: See `references/batch-remediation-checkpoint-workflow.md` for checkpoint process
