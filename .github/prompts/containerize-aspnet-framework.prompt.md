---
name: containerize-aspnet-framework
title: Containerize ASP.NET Framework
description: Containerize a legacy ASP.NET Framework application with multi-stage Dockerfiles and production-ready settings.
trigger: /containerize-aspnet-framework
version: 1.0.0
author: Hermes Agent
tags: 
metadata: 
hermes: 
profile: code-architect
priority: medium
copilot: 
model_required: sonnet
opencode: 
enabled: true
codex: 
toolsets: 
skills: 
- skill: using-superpowers
dependencies: []
formatter: markdown
license: MIT
---

## Table of Contents

## Goal
Containerize a legacy ASP.NET Framework application with multi-stage Dockerfiles and production-ready settings.

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [Containerization Settings](#containerization-settings)
- [Scope](#scope)
- [Execution Process](#execution-process)
- [Build and Runtime Verification](#build-and-runtime-verification)
- [Progress Tracking](#progress-tracking)
- [Environment Detection](#environment-detection)
- [Configuration Changes](#configuration-changes)
- [Containerization](#containerization)
- [Verification](#verification)
- [Reference Materials](#reference-materials)
  - [Example Dockerfile](#example-dockerfile)
- [Adapting this Example](#adapting-this-example)
- [Notes on Stage Naming](#notes-on-stage-naming)
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
- [Containerization Settings](#containerization-settings)
- [Scope](#scope)
- [Execution Process](#execution-process)
- [Build and Runtime Verification](#build-and-runtime-verification)
- [Progress Tracking](#progress-tracking)
- [Environment Detection](#environment-detection)
- [Configuration Changes](#configuration-changes)
- [Containerization](#containerization)
- [Verification](#verification)
- [Reference Materials](#reference-materials)
- [Example Dockerfile](#example-dockerfile)
- [Adapting this Example](#adapting-this-example)
- [Notes on Stage Naming](#notes-on-stage-naming)
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





Containerize an ASP.NET .NET Framework project by creating Dockerfile and .dockerfile files customized for the project.

## ASP.NET .NET Framework Containerization PromptContainerize the ASP.NET (.NET Framework) project specified in the containerization settings below, focusing **exclusively** on changes required for the application to run in a Windows Docker container. Containerization should consider all settings specified here.**REMEMBER:** This is a .NET Framework application, not .NET Core. The containerization process will be different from that of a .NET Core application.

## Containerization Settings

> This section of the prompt contains the specific settings and configurations req
> Any settings that are not specified will be set to default values. The default v
> **Full content:**

## Scope

- ✅ App configuration modification to ensure config builders are used to read app settings and connection strings from the environment variables- ✅ Dockerfile creation and configuration for an ASP.NET application- ✅ Specifying multiple stages in the Dockerfile to build/publish the application and copy the output to the final image- ✅ Configuration of Windows container platform compatibility (Windows Server Core or Full)- ✅ Proper handling of dependencies (GAC assemblies, MSIs, COM components)- ❌ No infrastructure setup (assumed to be handled separately)- ❌ No code changes beyond those required for containerization

## Execution Process

> 1. Review the containerization settings above to understand the containerization
> 2. Create a `progress.md` file to track changes with check marks
> **Full content:**

## Build and Runtime Verification

confirm that Docker build succeeds once the Dockerfile is completed. Use the following command to build the Docker image:```bashdocker build -t aspnet-app:latest .```If the build fails, review the error messages and make necessary adjustments to the Dockerfile or project configuration. Report success/failure.

## Progress Tracking

Maintain a `progress.md` file with the following structure:```markdown# Containerization Progress

## Environment Detection

- [ ] .NET Framework version detection (version: \_\_\_)- [ ] Windows Server SKU selection (SKU: \_\_\_)- [ ] Windows Server version selection (Version: \_\_\_)

## Configuration Changes

- [ ] Web.config modifications for configuration builders- [ ] NuGet package source configuration (if applicable)- [ ] Copy LogMonitorConfig.json and adjust if required by settings

## Containerization

- [ ] Dockerfile creation- [ ] .dockerignore file creation- [ ] Build stage created with SDK image- [ ] sln, csproj, packages.config, and (if applicable) NuGet.config copied for package restore- [ ] Runtime stage created with runtime image- [ ] Non-root user configuration- [ ] Dependency handling (GAC, MSI, COM, registry, additional files, etc.)- [ ] Health check configuration (if applicable)- [ ] Special requirements implementation

## Verification

- [ ] Review containerization settings and make sure that all requirements are met
- [ ] Docker build success```Do not pause for confirmation between steps. Continue methodically until the application has been containerized and Docker build succeeds.**YOU ARE NOT DONE UNTIL ALL CHECKBOXES ARE MARKED!** This includes building the Docker image successfully and addressing any issues that arise during the build process.

## Reference Materials

### Example Dockerfile

> An example Dockerfile for an ASP.NET (.NET Framework) application using a Window

## Adapting this Example

**Note:** Customize this template based on the specific requirements in the containerization settings.When adapting this example Dockerfile:1. Replace `YourSolution.sln`, `YourProject.csproj`, etc. with your actual file names2. Adjust the Windows Server and .NET Framework versions as needed3. Modify the dependency installation steps based on your requirements and remove any unnecessary ones4. Add or remove stages as needed for your specific workflow

## Notes on Stage Naming

> - The `AS stage-name` syntax gives each stage a name
> - Use `--from=stage-name` to copy files from a previous stage
> **Full content:**

## Template References

Detailed templates in `templates/containerize-aspnet-framework/`:- `containerization_settings.md`- `execution_process.md`- `notes_on_stage_naming.md`- `reference_materials.md`

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

## Workflow

<content>

Same-family prompts:

- [`containerize-aspnetcore.prompt.md`](containerize-aspnetcore.prompt.md)
```
# Prompt template
Execute the workflow defined in this file.
```
