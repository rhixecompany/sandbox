# Skill Audit: `log-analysis-and-triage`

**Category:** devops  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\devops\log-analysis-and-triage\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** A  
**Issues:** 0 critical / 0 major / 0 minor  

---

## Frontmatter Check

```yaml
name: log-analysis-and-triage
title: Log Analysis and Triage — False Positives, Categorization, Cleanup
description: >-
  Systematic workflow for analyzing multi-file log directories, categorizing by type and age,
  detecting false positives vs. real failures, and deciding what to keep vs. delete.
  Includes heuristics for distinguishing tool unavailability from detection/interop failures.
trigger: |
  • User asks to "read logs" or "identify issues" in a directory
  • Multiple log files with different timestamps/types
  • Need to distinguish signal from noise
  • Log cleanup or archival required
  • System diagnostic errors need root-cause triage
```

## Issues Found

_No issues — skill passes all checks._

## Sections Present

- ✅ `## When to Use`
- • `## Verification Checklist`
- • `## Overview`
- ✅ `## Workflow`
- • `## Pitfalls`
- • `## Heuristics for Real vs. False Positives`
- • `## Example: Triage Report`
- • `## Hermes-Specific Log Analysis`
- • `## See Also`

## Recommendations

- None. Skill is well-formed.
