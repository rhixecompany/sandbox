---
name: sandbox-audit-system
description: "5-Phase Audit System"
version: 1.0.0
author: Alexa
---
     1|# 5-Phase Audit System
     2|
     3|## Location
     4|
     5|`scripts/` directory
     6|
     7|## Configuration
     8|
     9|- `config/repo-inventory.json` - 17 repos with metadata (priority, stack, paths)
    10|- `config/diagnostics-config.json` - Per-stack diagnostic commands
    11|
    12|## Libraries
    13|
    14|- `lib/repo-scanner.js` - Auto-detect stack (by detection files) and run diagnostics
    15|- `lib/finding-parser.js` - Parse diagnostic output into Finding objects
    16|- `lib/` PowerShell utils: clone-utils, git-operations, validation, triage-utils
    17|
    18|## Phases
    19|
    20|### Phase 1: Deep Triage
    21|
    22|- Script: `phase-1-deep-triage.sh` / `.ps1`
    23|- Target: CRITICAL + HIGH priority repos
    24|- Action: Run full diagnostics per stack
    25|
    26|### Phase 2: Light Inventory
    27|
    28|- Script: `phase-2-light-inventory.sh` / `.ps1`
    29|- Target: MEDIUM + LOW priority repos
    30|- Action: Quick snapshot, no deep diagnostics
    31|
    32|### Phase 3: Consolidation
    33|
    34|- Script: `phase-3-consolidation.js`
    35|- Action: Merge findings → propose fixes → group into batches
    36|- Output: `BATCHES.json`, `CONSOLIDATED_PROPOSED_FIXES.md`
    37|
    38|### Phase 4: Batch Execution
    39|
    40|- Script: `phase-4-batch-executor.js`
    41|- Action: Apply each batch, verify with tests/lint/build
    42|- Safety: Max 7 modified files per batch (hard cap)
    43|- Partial accept: Failed batches noted, passing fixes applied
    44|
    45|### Phase 5: Final Summary
    46|
    47|- Script: `phase-5-final-summary.js`
    48|- Action: Generate executive summary
    49|- Output: `FINAL_AUDIT_SUMMARY.md`
    50|
    51|## Outputs
    52|
    53|- `docs/audits/` - `{repo}_diagnostic_{timestamp}.json`, `{repo}_findings_{timestamp}.txt`
    54|- `BATCH_LOGS/` - `BATCH-XXX_log.json`
    55|- `CONSOLIDATED_PROPOSED_FIXES.md` - All proposed fixes grouped by batch
    56|- `BATCHES.json` - Machine-readable batch definitions
    57|- `FINAL_AUDIT_SUMMARY.md` - Executive summary
    58|
    59|## Repo Priorities
    60|
    61|- CRITICAL (1): comicwise (148 issues)
    62|- HIGH (3): Banking, rhixe_scans, university-libary-jsm
    63|- MEDIUM (8): cookiecutter-django-tailwind, Django-Scrapy-Selenium, Python-projects, youtube-downloader, ecom, profile, selenium_webdriver, xamehitv
    64|- LOW (5): rhixe.company, xamehi, xamehi.tv, my-opencode-config, rhixecompany
    65|
    66|## Key Rules
    67|
    68|- Sequential execution only (phases build on each other)
    69|- No speculation - only fixes from diagnostic results
    70|- Every finding has unique ID, batch log, verification record
    71|