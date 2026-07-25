---
author: Hermes Agent
description: Audit AGENTS and customization drift in monorepo workspaces, then produce
  an actionable remediation report.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: customization-audit
tags:
- audit
- monorepo
- agents
- drift
- customization
title: Customization Audit
version: 1.0.0

---
# Customization Audit

## Overview

Run a targeted audit of chat customization assets and instruction routing in a monorepo, then return a concise remediation report.

## When to Use

- Workspaces contain many AGENTS.md and instruction files
- Agents or tools are applying wrong conventions in subprojects
- Inventory counts or references may be stale
- New customization files were added and drift validation is needed

## When NOT to Use

- Single-project repos without hierarchy
- Audits that require source code changes
- Performance profiling unrelated to customization drift

## Skills Required

| Skill | Purpose |
|-------|---------|
| `workspace-audit` | Inspect repo-level and project-level customization files |
| `hermes-setup` | Verify profile and environment conventions |

## Workflow

### Phase 1: Discover scope and precedence

1. Locate all AGENTS.md and related instruction files.
2. Resolve nearest precedence for the target scope.
3. Identify representative instruction files for each extension type.

### Phase 2: Validate inventory alignment

1. Read documented inventory or reports.
2. Compare discovered files against documented counts and paths.
3. Flag stale counts, missing references, or unexpected files.

### Phase 3: Detect duplication and routing risks

1. Find same-purpose files with overlapping names or descriptions.
2. Flag root-only guidance that ignores local overrides.
3. Flag overly broad `applyTo` patterns.

### Phase 4: Generate remediation report

1. Report scope and method.
2. Report findings with severity and file paths.
3. Provide one recommended concrete fix per finding.
4. Include an executable command checklist.

## Verification Checklist

- [ ] Scope documented and bounded
- [ ] All relevant customization files inventoried
- [ ] Inventory compared against documented references
- [ ] Duplicates and routing risks listed by severity
- [ ] Remediation commands provided
- [ ] No code files edited during audit

## Pitfalls

- Skipping precedence checks leads to incorrect root vs local attribution.
- Treating duplicate names as duplicates without inspecting content misses semantic differences.
- Broad `applyTo` patterns often mask special-case guidance.
- Updates during audit may invalidate findings; freeze target scope when possible.
