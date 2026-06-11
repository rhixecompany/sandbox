---
name: customization-audit
description:
  'Audit AGENTS and customization drift in monorepo workspaces, then produce an
  actionable remediation report'
---

# Customization Audit


## When to Use

- Use this skill when working with customization audit tasks
- Triggered by: `customization-audit` related operations

## Purpose

Run a targeted audit of chat customization assets and instruction routing, then
return a concise remediation report that can be executed immediately.

## Use When

- The workspace has many AGENTS.md and instruction files.
- Agents are applying the wrong conventions in subprojects.
- Inventory counts or references may be stale.
- New customization files were added and you need drift validation.

## Inputs

- Optional target scope (root, subproject path, or glob)
- Optional strict mode flag (true or false)
- Optional include list for asset types (instructions, prompts, skills, agents)

## Audit Workflow

### Step 1: Discover scope and precedence

- Locate all AGENTS.md files.
- Resolve nearest AGENTS precedence for target scope.
- Identify matching instruction files for representative extensions.

### Step 2: Validate inventory alignment

- Read
  reports/copilot-skills-agents-hooks-plugins-prompts-instructions-report.md.
- Compare discovered files with documented counts and references.
- Flag stale counts or missing referenced paths.

### Step 3: Detect duplication and routing risks

- Find same-purpose files with overlapping names or descriptions.
- Flag root-only guidance that ignores local override files.
- Flag applyTo patterns that are too broad for specialized guidance.

### Step 4: Generate remediation report

Produce a Markdown report with these sections in order:

1. Scope
2. Findings
3. Severity
4. Recommended fixes
5. Command checklist

## Output Contract

- Findings must include file paths.
- Each finding must include severity: high, medium, or low.
- Each finding must include one concrete fix action.
- Keep total findings under 15 unless strict mode is enabled.

## Guardrails

- Do not edit code files during audit.
- Prefer linking existing docs instead of duplicating policy text.
- If no findings are detected, explicitly report that and include residual risk
  notes.
