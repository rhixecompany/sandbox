---
name: az-cost-optimize
title: Azure Cost Optimize
description: Analyze Azure resources used in the app (IaC files and/or resources in a target rg) and optimize costs - creating GitHub issues for identified optimizations.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills: []
formatter: default
plan: 'None'
tags:
  - azure
  - backend
  - configuration
  - frontend
  - generator
  - git
  - mcp
  - performance
  - prompts
  - workflow
trigger: /az-cost-optimize
dependencies: []
metadata:
  hermes: {}
---

## Goal

Analyze Azure resources used in the app (IaC files and/or resources in a target rg) and optimize costs - creating GitHub issues for identified optimizations.

# Azure Cost OptimizeThis workflow analyzes Infrastructure-as-Code (IaC) files and Azure resources to generate cost optimization recommendations. It creates individual GitHub issues for each optimization opportunity plus one EPIC issue to coordinate implementation, enabling efficient tracking and execution of cost savings initiatives.

## Prerequisites

- Azure MCP server configured and authenticated
- GitHub MCP server configured and authenticated
- Target GitHub repository identified
- Azure resources deployed (IaC files optional but helpful)
- Prefer Azure MCP tools (`azmcp-*`) over direct Azure CLI when available

## Workflow Steps

### Step 1: Get Azure Best Practices

> **Action**: Retrieve cost optimization best practices before analysis **Tools**:

## 💰 Cost Optimization: [Brief Title]

> **Monthly Savings**: $X | **Risk Level**: [Low/Medium/High] | **Implementation E
> [Clear explanation of the optimization and why it's needed]
> **Full content:**

## 📊 Executive Summary

- **Resources Analyzed**: X- **Optimization Opportunities**: Y- **Total Monthly Savings Potential**: $X- **High Priority Items**: N

## 🏗️ Current Architecture Overview

```mermaid
   graph TB       subgraph "Resource Group: [name]"           [Generated architecture diagram showing current resources and costs]       end```   ````

## 📋 Implementation Tracking

### 🚀 High Priority (Implement First)

- [ ] # [issue-number]: [Title] - $X/month savings   - [ ] # [issue-number]: [Title] - $X/month savings

### ⚡ Medium Priority

- [ ] # [issue-number]: [Title] - $X/month savings   - [ ] # [issue-number]: [Title] - $X/month savings

### 🔄 Low Priority (Nice to Have)

- [ ] # [issue-number]: [Title] - $X/month savings

## 📈 Progress Tracking

- **Completed**: 0 of Y optimizations   - **Savings Realized**: $0 of $X/month   - **Implementation Status**: Not Started

## 🎯 Success Criteria

- [ ] All high-priority optimizations implemented   - [ ]

> 80% of estimated savings realized   - [ ] No performance degradation observed   - [ ] Cost monitoring dashboard updated

## 📝 Notes

- Review and update this EPIC as issues are completed   - Monitor actual vs. estimated savings   - Consider scheduling regular cost optimization reviews   ```   ```

## Error Handling

- **Cost Validation**: If savings estimates lack supporting evidence or seem inconsistent with Azure pricing, re-verify configurations and pricing sources before proceeding
- **Azure Authentication Failure**: Provide manual Azure CLI setup steps
- **No Resources Found**: Create informational issue about Azure resource deployment
- **GitHub Creation Failure**: Output formatted recommendations to console
- **Insufficient Usage Data**: Note limitations and provide configuration-based recommendations only

## Success Criteria

- ✅ All cost estimates verified against actual resource configurations and Azure pricing- ✅ Individual issues created for each optimization (trackable and assignable)- ✅ EPIC issue provides comprehensive coordination and tracking- ✅ All recommendations include specific, executable Azure CLI commands- ✅ Priority scoring enables ROI-focused implementation- ✅ Architecture diagram accurately represents current state- ✅ User confirmation prevents unwanted issue creation

## Template References

Detailed templates in `templates/az-cost-optimize/`:- `cost_optimization_brief_title.md`- `workflow_steps.md`

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Context

Use when implementing, modifying, or debugging code. Read the codebase first, understand patterns, then apply changes with tests.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Read existing code before writing new code.
- Match project conventions and style.
- Add tests for new functionality.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State clearly when something fails.

## Phases

### Phase 1: Intake

- Read the request and identify scope.
- Locate relevant files, diffs, references.

### Phase 2: Execute

- Perform work with smallest safe change set.
- Keep steps explicit and reproducible.

### Phase 3: Verify

- Check result against goal, rules, inputs.
- Confirm output is usable and complete.

### Phase 4: Hand Off

- Return final artifact or findings clearly.
- Stop once the requested result is delivered.

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions
