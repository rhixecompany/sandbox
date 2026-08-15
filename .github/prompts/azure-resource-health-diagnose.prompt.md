---
name: azure-resource-health-diagnose
title: "Azure Resource Health & Issue Diagnosis"
description: |
  No description
version: 1.0.0
license: MIT
author: Hermes Agent
trigger: /azure-resource-health-diagnose
toolsets:
  - file
  - terminal
skills: []
dependencies: []
formatter: default
plan: null
metadata:
  hermes:
    profile: default
    mcp_servers:
      - filesystem
      - terminal
    context_size: medium
  copilot:
    context_size: medium
    extensions: []
  opencode:
    command: "opencode /azure-resource-health-diagnose"
    flags: {}
  codex:
    model_override: null
tags:
  - complexity:intermediate
  - domain:debug
  - tool:azure
scripts: []
---
## Goal

Analyze Azure resource health, diagnose issues from logs and telemetry, and create a remediation plan for identified problems.

## Context

Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.

## Phases

### Phase 1: Intake

- Read the request and identify the exact scope.
- Locate the relevant files, diffs, or references.

### Phase 2: Execute

- Perform the requested work with the smallest safe change set.
- Keep the steps explicit and reproducible.

### Phase 3: Verify

- Check the result against the goal, rules, and inputs.
- Confirm the output is usable and complete.

### Phase 4: Hand off

- Return the final artifact or findings clearly.
- Stop once the requested result is delivered.

## Prerequisites

- Azure MCP server configured and authenticated
- Target Azure resource identified (name and optionally resource group/subscription)
- Resource must be deployed and running to generate logs/telemetry
- Prefer Azure MCP tools (`azmcp-*`) over direct Azure CLI when available

## Workflow Steps

### Step 1: Get Azure Best Practices

> **Action**: Retrieve diagnostic and troubleshooting best practices **Tools**: Az

## 🔍 Executive Summary

[Brief overview of health status and key findings]

## 📊 Health Metrics

- **Availability**: X% over last 24h- **Performance**: [Average response time/throughput]- **Error Rate**: X% over last 24h- **Resource Utilization**: [CPU/Memory/Storage percentages]

## 🚨 Issues Identified

### Critical Issues

- **[Issue 1]**: [Description]  - **Root Cause**: [Analysis]  - **Impact**: [Business impact]  - **Immediate Action**: [Required steps]

### High Priority Issues

- **[Issue 2]**: [Description]  - **Root Cause**: [Analysis]  - **Impact**: [Performance/reliability impact]  - **Recommended Fix**: [Solution steps]

## 🛠️ Remediation Plan

### Phase 1: Immediate Actions (0-2 hours)

```bash
# Critical fixes to restore service
[Azure CLI commands with explanations]
```

### Phase 2: Short-term Fixes (2-24 hours)

```bash
# Performance and reliability improvements
[Azure CLI commands with explanations]
```

### Phase 3: Long-term Improvements (1-4 weeks)

```bash
# Architectural and preventive measures
[Azure CLI commands and configuration changes]
```

## 📈 Monitoring Recommendations

- **Alerts to Configure**: [List of recommended alerts]
- **Dashboards to Create**: [Monitoring dashboard suggestions]
- **Regular Health Checks**: [Recommended frequency and scope]

## ✅ Validation Steps

- [ ] Verify issue resolution through logs
- [ ] Confirm performance improvements
- [ ] Test application functionality
- [ ] Update monitoring and alerting
- [ ] Document lessons learned

## 📝 Prevention Measures

- [Recommendations to prevent similar issues]
- [Process improvements]
- [Monitoring enhancements]

## Error Handling

- **Resource Not Found**: Provide guidance on resource name/location specification
- **Authentication Issues**: Guide user through Azure authentication setup
- **Insufficient Permissions**: List required RBAC roles for resource access
- **No Logs Available**: Suggest enabling diagnostic settings and waiting for data
- **Query Timeouts**: Break down analysis into smaller time windows
- **Service-Specific Issues**: Provide generic health assessment with limitations noted

## Success Criteria

- ✅ Resource health status accurately assessed- ✅ All significant issues identified and categorized- ✅ Root cause analysis completed for major problems- ✅ Actionable remediation plan with specific steps provided- ✅ Monitoring and prevention recommendations included- ✅ Clear prioritization of issues by business impact- ✅ Implementation steps include validation and rollback procedures

## Template References

Detailed templates in `templates/azure-resource-health-diagnose/`:- `workflow_steps.md`

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

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.


## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section




