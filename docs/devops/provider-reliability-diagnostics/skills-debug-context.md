# Skill Audit: `provider-reliability-diagnostics`

**Category:** devops  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\devops\provider-reliability-diagnostics\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** A-  
**Issues:** 0 critical / 0 major / 1 minor  

---

## Frontmatter Check

```yaml
name: provider-reliability-diagnostics
title: Provider Reliability Diagnostics — Chain Tracing, ACPX Validation, Auxiliary Fallback
description: "Diagnose and fix provider chain failures in Hermes: trace failures across main → fallback → auxiliary → aggregator layers, validate provider health via ACPX exec, fix MCP transport mismatches, and configure auxiliary fallbacks."
author: Hermes Agent
version: 1.0.0
tags: [hermes, diagnostics, providers, reliability, mcp, fallback]
trigger: |
  • User says "provider not working", "API failing", "model not responding"
  • errors.log shows repeated provider failure patterns (ConnectionError, 402, 429, 401)
  • Multiple provider retries visible in logs
  • Vision/compression/title gen silently failing
  • MCP server connection failures at startup
  • User asks "why did my session fail?"
```

## Issues Found

| Severity | Code | Description |
|----------|------|-------------|
| MINOR | C1 | Stale pattern: stale_model: old model name big-pickle |

## Sections Present

- ✅ `## When to Use`
- ✅ `## Workflow`
- • `## Verification Checklist`
- • `## The Provider Chain`
- • `## Phase 1: Quick Health Sweep`
- • `## Phase 2: Log Trace — Identify the Broken Link`
- • `## Phase 3: Apply Fix at the Broken Link`
- • `## Phase 4: Verify Fix`
- • `## Pitfalls`
- • `## Best Practices`
- • `## Related Skills`
- • `## Reference Files`

## Recommendations

- Fix `C1`: Stale pattern: stale_model: old model name big-pickle
