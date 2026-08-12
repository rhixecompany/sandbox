---
name: containerize-aspnetcore
title: ASP.NET Core Docker Containerization Prompt
description: Containerize an ASP.NET Core project by creating Dockerfile and .dockerfile files customized for the project.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - terminal
  - file
scripts: []
skills: []
formatter: default
plan: null
tags:
  - docker
  - frontend
  - linux
  - ml
  - performance
  - prompts
  - security
  - specification
  - csharp
  - dotnet
trigger: /containerize-aspnetcore
dependencies: []
metadata:
  hermes: {}
---

## Goal

Containerize an ASP.NET Core project by creating Dockerfile and .dockerfile files customized for the project.

# ASP.NET Core Docker Containerization Prompt

## Containerization Request

Containerize the ASP.NET Core (.NET) project specified in the settings below, focusing **exclusively** on changes required for the application to run in a Linux Docker container. Containerization should consider all settings specified here.Abide by best practices for containerizing .NET Core applications, ensuring that the container is optimized for performance, security, and maintainability.

## Containerization Settings

> This section of the prompt contains the specific settings and configurations req
> Any settings that are not specified will be set to default values. The default v
> **Full content:**

## Scope

- ✅ App configuration modification to ensure application settings and connection strings can be read from environment variables- ✅ Dockerfile creation and configuration for an ASP.NET Core application- ✅ Specifying multiple stages in the Dockerfile to build/publish the application and copy the output to the final image- ✅ Configuration of Linux container platform compatibility (Alpine, Ubuntu, Chiseled, or Azure Linux (Mariner))- ✅ Proper handling of dependencies (system packages, native libraries, additional tools)- ❌ No infrastructure setup (assumed to be handled separately)- ❌ No code changes beyond those required for containerization

## Execution Process

> 1. Review the containerization settings above to understand the containerization
> 2. Create a `progress.md` file to track changes with check marks
> **Full content:**

## Build and Runtime Verification

Confirm that Docker build succeeds once the Dockerfile is completed. Use the following command to build the Docker image:```bashdocker build -t aspnetcore-app:latest .```If the build fails, review the error messages and make necessary adjustments to the Dockerfile or project configuration. Report success/failure.

## Progress Tracking

Maintain a `progress.md` file with the following structure:```markdown# Containerization Progress

## Environment Detection

- [ ] .NET version detection (version: \_\_\_)- [ ] Linux distribution selection (distribution: \_\_\_)

## Configuration Changes

- [ ] Application configuration verification for environment variable support- [ ] NuGet package source configuration (if applicable)

## Containerization

- [ ] Dockerfile creation- [ ] .dockerignore file creation- [ ] Build stage created with SDK image- [ ] csproj file(s) copied for package restore- [ ] NuGet.config copied if applicable- [ ] Runtime stage created with runtime image- [ ] Non-root user configuration- [ ] Dependency handling (system packages, native libraries, tools, etc.)- [ ] Health check configuration (if applicable)- [ ] Special requirements implementation

## Verification

- [ ] Review containerization settings and make sure that all requirements are met
- [ ] Docker build success```Do not pause for confirmation between steps. Continue methodically until the application has been containerized and Docker build succeeds.**YOU ARE NOT DONE UNTIL ALL CHECKBOXES ARE MARKED!** This includes building the Docker image successfully and addressing any issues that arise during the build process.

## Example Dockerfile

> An example Dockerfile for an ASP.NET Core (.NET) application using a Linux base>
>
> # ============================================================

## Adapting this Example

**Note:** Customize this template based on the specific requirements in containerization settings.When adapting this example Dockerfile:1. Replace `YourProject.csproj`, `YourProject.dll`, etc. with your actual project names2. Adjust the .NET version and Linux distribution as needed3. Modify the dependency installation steps based on your requirements and remove any unnecessary ones4. Configure environment variables specific to your application5. Add or remove stages as needed for your specific workflow6. Update the health check endpoint to match your application's health check route

## Linux Distribution Variations

> For smaller image sizes, you can use Alpine Linux:
> FROM mcr.microsoft.com/dotnet/sdk:8.0-alpine AS build
> **Full content:**

## Notes on Stage Naming

- The `AS stage-name` syntax gives each stage a name- Use `--from=stage-name` to copy files from a previous stage- You can have multiple intermediate stages that aren't used in the final image- The `final` stage is the one that becomes the final container image

## Security Best Practices

- Always run as a non-root user in production- Use specific image tags instead of `latest`- Minimize the number of installed packages- Keep base images updated- Use multi-stage builds to exclude build dependencies from the final image

## Template References

Detailed templates in `templates/containerize-aspnetcore/`:- `containerization_settings.md`- `example_dockerfile.md`- `execution_process.md`- `linux_distribution_variations.md`

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

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.


## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section


## Related Prompts

Same-family prompts:

- [`containerize-aspnet-framework.prompt.md`](containerize-aspnet-framework.prompt.md)
