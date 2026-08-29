---
name: dotnet-upgrade
title: .NET Upgrade Assistant
description: Drives a comprehensive .NET framework upgrade analysis and execution across projects, dependencies, and runtime targets.
trigger: /dotnet-upgrade
version: 1.0.0
author: Hermes Agent
date: '2026-08-25'
tags:
  - csharp
  - dotnet
  - upgrade
  - migration
  - tooling
  - backend
  - refactor
metadata:
  hermes:
    profile: code-architect
    priority: medium
  copilot:
    model_required: sonnet
  opencode:
    enabled: true
  codex:
    enabled: true
---
## Table of Contents

## Goal

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
  - [Domain Rules](#domain-rules)
  - [Standing Rules](#standing-rules)
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand Off](#phase-4:-hand-off)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)



- [Goal](#goal)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
- [Domain Rules](#domain-rules)
- [Standing Rules](#standing-rules)
- [Phases](#phases)
- [Phase 1: Intake](#phase-1:-intake)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Hand Off](#phase-4:-hand-off)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)





Ready-to-use prompts for comprehensive .NET framework upgrade analysis and execution.

## Project Discovery & Assessment- name: "Project Classification Analysis" prompt: "Identify all projects in the solution and classify them by type (`.NET Framework`, `.NET Core`, `.NET Standard`). Analyze each `.csproj` for its current `TargetFramework` and SDK usage."- name: "Dependency Compatibility Review" prompt: "Review external and internal dependencies for framework compatibility. Determine the upgrade complexity based on dependency graph depth."- name: "Legacy Package Detection" prompt: "Identify legacy `packages.config` projects needing migration to `PackageReference` format."# Upgrade Strategy & Sequencing- name: "Project Upgrade Ordering" prompt: "Recommend a project upgrade order from least to most dependent components. Suggest how to isolate class library upgrades before API or Azure Function migrations."- name: "Incremental Strategy Planning" prompt: "Propose an incremental upgrade strategy with rollback checkpoints. Evaluate the use of **Upgrade Assistant** or **manual upgrades** based on project structure."- name: "Progress Tracking Setup" prompt: "Generate an upgrade checklist for tracking build, test, and deployment readiness across all projects."# Framework Targeting & Code Adjustments- name: "Target Framework Selection" prompt: "Suggest the correct `TargetFramework` for each project (e.g., `net8.0`). Review and update deprecated SDK or build configurations."- name: "Code Modernization Analysis" prompt: "Identify code patterns needing modernization (e.g., `WebHostBuilder` → `HostBuilder`). Suggest replacements for deprecated .NET APIs and third-party libraries."- name: "Async Pattern Conversion" prompt: "Recommend conversion of synchronous calls to async where appropriate for improved performance and scalability."# NuGet & Dependency Management- name: "Package Compatibility Analysis" prompt: "Analyze outdated or incompatible NuGet packages and suggest compatible versions. Identify third-party libraries that lack .NET 8 support and provide migration paths."- name: "Shared Dependency Strategy" prompt: "Recommend strategies for handling shared dependency upgrades across projects. Evaluate usage of legacy packages and suggest alternatives in Microsoft-supported namespaces."- name: "Transitive Dependency Review" prompt: "Review transitive dependencies and potential version conflicts after upgrade. Suggest resolution strategies for dependency conflicts."# CI/CD & Build Pipeline Updates- name: "Pipeline Configuration Analysis" prompt: "Analyze YAML build definitions for SDK version pinning and recommend updates. Suggest modifications for `UseDotNet@2` and `NuGetToolInstaller` tasks."- name: "Build Pipeline Modernization" prompt: "Generate updated build pipeline snippets for .NET 8 migration. Recommend validation builds on feature branches before merging to main."- name: "CI Automation Enhancement" prompt: "Identify opportunities to automate test and build verification in CI pipelines. Suggest strategies for continuous integration validation."# Testing & Validation- name: "Build Validation Strategy" prompt: "Propose validation checks to ensure the upgraded solution builds and runs successfully. Recommend automated test execution for unit and integration suites post-upgrade."- name: "Service Integration Verification" prompt: "Generate validation steps to verify logging, telemetry, and service connectivity. Suggest strategies for verifying backward compatibility and runtime behavior."- name: "Deployment Readiness Check" prompt: "Recommend UAT deployment verification steps before production rollout. Create comprehensive testing scenarios for upgraded components."# Breaking Change Analysis- name: "API Deprecation Detection" prompt: "Identify deprecated APIs or removed namespaces between target versions. Suggest automated scanning using `.NET Upgrade Assistant` and API Analyzer."- name: "API Replacement Strategy" prompt: "Recommend replacement APIs or libraries for known breaking areas. Review configuration changes such as `Startup.cs` → `Program.cs` refactoring."- name: "Regression Testing Focus" prompt: "Suggest regression testing scenarios focused on upgraded API endpoints or services. Create test plans for critical functionality validation."# Version Control & Commit Strategy- name: "Branching Strategy Planning" prompt: "Recommend branching strategy for safe upgrade with rollback capability. Generate commit templates for partial and complete project upgrades."- name: "PR Structure Optimization" prompt: "Suggest best practices for creating structured PRs (`Upgrade to .NET [Version]`). Identify tagging strategies for PRs involving breaking changes."- name: "Code Review Guidelines" prompt: "Recommend peer review focus areas (build, test, and dependency validation). Create checklists for effective upgrade reviews."# Documentation & Communication- name: "Upgrade Documentation Strategy" prompt: "Suggest how to document each project's framework change in the PR. Propose automated release note generation summarizing upgrades and test results."- name: "Stakeholder Communication" prompt: "Recommend communicating version upgrades and migration timelines to consumers. Generate documentation templates for dependency updates and validation results."- name: "Progress Tracking Systems" prompt: "Suggest maintaining an upgrade summary dashboard or markdown checklist. Create templates for tracking upgrade progress across multiple projects."# Tools & Automation- name: "Upgrade Tool Selection" prompt: "Recommend when and how to use: `.NET Upgrade Assistant`, `dotnet list package --outdated`, `dotnet migrate`, and `graph.json` dependency visualization."- name: "Analysis Script Generation" prompt: "Generate scripts or prompts for analyzing dependency graphs before upgrading. Propose AI-assisted prompts for Copilot to identify upgrade issues automatically."- name: "Multi-Repository Validation" prompt: "Suggest how to validate automation output across multiple repositories. Create standardized validation workflows for enterprise-scale upgrades."# Final Validation & Delivery- name: "Final Solution Validation" prompt: "Generate validation steps to confirm the final upgraded solution passes all validation checks. Suggest production deployment verification steps post-upgrade."- name: "Deployment Readiness Confirmation" prompt: "Recommend generating final test results and build artifacts. Create a checklist summarizing completion across projects (builds/tests/deployment)."- name: "Release Documentation" prompt: "Generate a release note summarizing framework changes and CI/CD updates. Create comprehensive upgrade summary documentation."---

## Template References

Detailed templates in `templates/dotnet-upgrade/`:

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


Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Fix root causes, not symptoms.
- Check siblings for the same flaw.
- Restore from git clean before retrying.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State when something fails.


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

- Return final artifact or findings .
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

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section

## Related Prompts

Same-family prompts:

- [`dotnet-best-practices.prompt.md`](dotnet-best-practices.prompt.md)
- [`dotnet-design-pattern-review.prompt.md`](dotnet-design-pattern-review.prompt.md)