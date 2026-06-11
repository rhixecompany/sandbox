# Rhixe Audit - Scripts Documentation

## Overview

This directory contains the orchestration scripts for the 5-phase Rhixe cross-repo audit and fix system.

## Files

### Configuration

- `config/repo-inventory.json` - 17 repos with metadata (priority, stack, paths)
- `config/diagnostics-config.json` - Per-stack diagnostic commands

### Libraries

- `lib/repo-scanner.js` - Auto-detect stack and run diagnostics
- `lib/finding-parser.js` - Parse diagnostic output into Finding objects

### Phases

- `phase-1-deep-triage.sh` - Deep diagnostics (CRITICAL+HIGH repos)
- `phase-2-light-inventory.sh` - Light snapshot (MEDIUM+LOW repos)
- `phase-3-consolidation.js` - Merge findings into batches
- `phase-4-batch-executor.js` - Apply fixes with verification
- `phase-5-final-summary.js` - Generate final report

### Orchestration

- `run-audit.sh` - Master script that runs all phases

## Usage

### Full Audit

```bash
bash ./scripts/run-audit.sh
```

### Individual Phases

```bash
# Phase 1: Deep Triage
bash ./scripts/phase-1-deep-triage.sh

# Phase 2: Light Inventory
bash ./scripts/phase-2-light-inventory.sh

# Phase 3: Consolidation
node ./scripts/phase-3-consolidation.js

# Phase 4: Batch Execution
node ./scripts/phase-4-batch-executor.js

# Phase 5: Final Summary
node ./scripts/phase-5-final-summary.js
```

## Outputs

After running the audit, you'll find:

- **`docs/audits/`** - Diagnostic results and findings for each repo
  - `{repo-id}_diagnostic_{timestamp}.json` - Raw diagnostic output
  - `{repo-id}_findings_{timestamp}.txt` - Parsed findings
  - `{repo-id}_inventory_{timestamp}.json` - Light inventory metadata

- **`BATCH_LOGS/`** - Batch execution logs
  - `BATCH-XXX_log.json` - Execution log for each batch

- **`CONSOLIDATED_PROPOSED_FIXES.md`** - Main report of all proposed fixes grouped by batch

- **`BATCHES.json`** - Machine-readable batch definitions

- **`FINAL_AUDIT_SUMMARY.md`** - Executive summary of audit results

## Process Flow

```
Phase 1: Deep Triage
  ↓ (run diagnostics on CRITICAL+HIGH repos)
Phase 2: Light Inventory
  ↓ (quick snapshot of MEDIUM+LOW repos)
Phase 3: Consolidation
  ↓ (merge findings → propose fixes → group into batches)
Phase 4: Batch Execution
  ↓ (apply each batch, verify with tests/lint/build)
Phase 5: Final Summary
  ↓ (generate executive summary)
COMPLETE
```

## Key Features

- **Sequential Execution**: Phases run in order for safer diagnostics before fixes
- **Batch Safety**: Max 7 modified files per batch, hard cap enforced
- **Partial Accept**: Failed batches are noted, passing fixes applied
- **Traceability**: Every finding has unique ID, batch log, verification record
- **No Speculation**: Only fixes from diagnostic results, no manual additions

## Requirements

- Node.js 14+
- Bash 4+
- For Python repos: Python 3.8+, pip
- For Node repos: npm 6+

## Repos Audited (17 total)

### CRITICAL (1)

- comicwise (148 issues)

### HIGH (3)

- Banking
- rhixe_scans
- university-libary-jsm

### MEDIUM (8)

- cookiecutter-django-tailwind
- Django-Scrapy-Selenium
- Python-projects
- youtube-downloader
- ecom
- profile
- selenium_webdriver
- xamehitv

### LOW (5)

- rhixe.company
- xamehi
- xamehi.tv
- my-opencode-config
- rhixecompany

---

_Generated with Rhixe Audit System_
