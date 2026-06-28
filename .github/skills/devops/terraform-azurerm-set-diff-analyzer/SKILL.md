---
name: terraform-azurerm-set-diff-analyzer
title: "Terraform AzureRM Set Diff Analyzer"
description: "Analyze Terraform plan JSON output for AzureRM Provider to distinguish between false-positive diffs (order-only changes in Set-type attributes) and actual resource changes."
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: [terraform, azure, diff-analysis, ci-cd, automation]
metadata:
  hermes:
    tags: [imported]
---
# Terraform AzureRM Set Diff Analyzer

## Overview

Analyze Terraform plan JSON output for the AzureRM Provider and separate noisy order-only Set diffs from real resource changes. Use this skill when Azure resources such as Application Gateway, Load Balancer, Firewall, Front Door, and NSGs show spurious diffs in plan output.

## When to Use

- `terraform plan` shows many changes after adding or removing a single element
- Azure resources present “all elements changed” behavior
- CI reviews require filtered diffs before merge
- Validating whether a plan is safe to apply

## When NOT to Use

- Non-Azure or non-Set-based Terraform diffs
- Plans that only require human-readable summary output
- Terraform versions/configurations that do not use AzureRM Set attributes

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Investigate Terraform state and plan errors |
| `log-analysis-and-triage` | Classify Terraform warnings versus real issues |

## Workflow

### Phase 1: Generate Plan JSON

```bash
terraform plan -out=plan.tfplan
terraform show -json plan.tfplan > plan.json
```

### Phase 2: Run Analysis

Use `scripts/analyze_plan.py` and inspect the outputs against relevant reference docs.

```bash
python scripts/analyze_plan.py plan.json
```

Review the exit codes and summary output to understand whether changes are false-positive only.

### Phase 3: Resolve Plan Output

For false-positive diffs:
- Confirm Set ordering differences
- Confirm no meaningful attribute update
- Document reasoning in PR comments

For real changes:
- Update affected resource values intentionally
- Re-run plan and review remaining diff surface

## Verification Checklist

- [ ] `plan.json` generated from current state
- [ ] Analyzer executed successfully
- [ ] False-positive report reviewed
- [ ] Real changes identified and documented
- [ ] Reviewer approval reflects findings

## Pitfalls

- Plan JSON may be large; review summary output first.
- Some Set attributes require multiple apply cycles to stabilize.
- Treat all false-positive conclusions as provisional until final review.
