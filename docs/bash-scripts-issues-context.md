# Bash Scripts Audit - Issues to Fix

**Generated:** 2026-05-29  
**Phase:** 3 (Code Review - Preparatory Document)  
**Scope:** 54 scripts across 7 batches

---

## Issues by Category

### Critical Issues (Must Fix Before Migration)

These issues prevent scripts from running correctly post-migration:

| Issue | Count | Details |
|-------|-------|---------|
| Hard-coded absolute paths | ~15 | `C:\\Users\\Alexa\\Desktop\\SandBox` paths need update |
| Missing `set -euo pipefail` | ~20 | Bash scripts without strict mode |
| Missing `shellcheck shell=bash` | ~25 | No shellcheck directive after shebang |
| Placeholder comments | ~8 | `@author Adminbot`, `Description placeholder` |
| Wrong shebang | ~5 | Not `#!/usr/bin/env bash` or `#!/usr/bin/env pwsh` |

### High-Priority Issues (Fix During Phase 3)

These should be addressed before Phase 4 migration:

| Issue | Count | Action |
|-------|-------|--------|
| Missing `Set-StrictMode` in PowerShell | ~30 | Add `Set-StrictMode -Version Latest` |
| Hardcoded relative paths | ~8 | Convert to environment vars or parameters |
| Undefined variables in strict mode | ~12 | Add safe defaults with `${VAR:-}` |
| Missing dry-run support | ~10 | Add `--dry-run` flag where applicable |
| ANSI/terminal artifacts in batch | ~3 | Remove from `.bat` files |

### Medium-Priority Issues (Document During Phase 3)

These require awareness but may not block migration:

| Issue | Count | Notes |
|-------|-------|-------|
| Deprecated PowerShell patterns | ~6 | `PSIsContainer` → `-Directory` switch |
| Monolithic shell functions | ~4 | 200+ line functions (consider consolidation) |
| Duplicate logic across variants | ~8 | .sh vs .ps1 vs .bat duplicating same logic |
| Missing help documentation | ~12 | Add `--help` or `-Help` support |

### Low-Priority Issues (Track During Phase 3)

- Inconsistent variable naming (CAPS vs camelCase)
- Comment formatting inconsistencies
- Log output not using standard logger
- Missing error handling patterns

---

## Per-Batch Issues (High-Level)

### Banking Scripts Issues

**Batch 1 (Orchestrators):**
- `orchestrator.sh`: Check for hardcoded paths to Banking project
- Wrapper variants: Ensure all three (.sh, .ps1, .bat) have identical behavior

**Batch 2 (Install Framework):**
- `install.sh` main script: ~300 lines (candidate for modularization)
- Library modules (00-08): Check each for dependencies on others
- Hard-coded paths for dependency locations

**Batch 3 (MCP & Plugin):**
- Cross-variant drift (sh vs ps1 vs bat likely differ)
- OpenCode references and path dependencies
- Exit code propagation in delegators

**Batch 4 (Utilities):**
- Diagnostic scripts may have hardcoded paths
- Verification scripts may have strict runtime dependencies
- Mixed script types (some pure bash, some bash + node, some powershell)

### comicwise Scripts Issues

**Batch 5 (Development Workflows):**
- VSCode extension installer: May require specific environment
- Quality gate: Likely has hardcoded project paths
- Setup-dev: May have dependency order issues
- All variants should have matching dry-run output

### rhixe_scans Scripts Issues

**Batch 6 (Utilities):**
- Docker scripts: Check for Docker daemon assumptions
- Browser install scripts: OS-specific logic, conditional execution
- All shell, no PowerShell variants

### Root/ecom Issues

**Batch 7:**
- `analyze-scripts.sh`: May self-reference (will break post-migration)
- `sandbox-runtime-commands.ps1`: Likely has hardcoded paths
- `ecom/install.sh`: Embedded environment setup

---

## Standards to Apply (Phase 3 Audit Checklist)

- [ ] All `.sh` files have shebang: `#!/usr/bin/env bash`
- [ ] All `.sh` files have `# shellcheck shell=bash` directive
- [ ] All `.sh` files have `set -euo pipefail` (or justified exception)
- [ ] All `.ps1` files have shebang: `#!/usr/bin/env pwsh`
- [ ] All `.ps1` files have `Set-StrictMode -Version Latest`
- [ ] All `.bat` files are thin delegators to `.ps1` (where applicable)
- [ ] No hardcoded user paths (`C:\\Users\\...`)
- [ ] No placeholder comments (`Adminbot`, `Description placeholder`)
- [ ] All scripts have consistent error handling
- [ ] All wrappers propagate exit codes correctly
- [ ] Dry-run mode consistent across all variants of same script

---

## Status

This document is preparatory for Phase 3.

Phase 3 will:
1. Read this document
2. Audit each batch for listed issues
3. Create explicit fix specifications
4. Categorize by severity (CRITICAL → LOW)
5. Create execution prompts for Phase 4

---

**Project:** Bash Scripts Modernization (bash-scripts-fix)  
**Version:** 2.0  
**Last Updated:** 2026-05-29
