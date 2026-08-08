---
name: multi-stage-dockerfile
title: Multi Stage Dockerfile
description: Create optimized multi-stage Dockerfiles for any language or framework.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - terminal
  - file
scripts: []
skills: []
formatter: default
plan: 'None'
tags:
  - docker
  - ml
  - performance
  - prompts
  - specification
  - typescript
trigger: /multi-stage-dockerfile
dependencies: []
metadata:
  hermes: {}
---

## Goal

Create optimized multi-stage Dockerfiles for any language or framework.

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

## Multi-Stage Structure- Use a builder stage for compilation, dependency installation, and other build-time operations- Use a separate runtime stage that only includes what's needed to run the application- Copy only the necessary artifacts from the builder stage to the runtime stage- Use meaningful stage names with the `AS` keyword (e.g., `FROM node:18 AS builder`)- Place stages in logical order: dependencies → build → test → runtime

## Base Images

- Start with official, minimal base images when possible- Specify exact version tags to ensure reproducible builds (e.g., `python:3.11-slim` not just `python`)- Consider distroless images for runtime stages where appropriate- Use Alpine-based images for smaller footprints when compatible with your application- Ensure the runtime image has the minimal necessary dependencies

## Layer Optimization

- Organize commands to maximize layer caching- Place commands that change frequently (like code changes) after commands that change less frequently (like dependency installation)- Use `.dockerignore` to prevent unnecessary files from being included in the build context- Combine related RUN commands with `&&` to reduce layer count- Consider using COPY --chown to set permissions in one step

## Security Practices

- Avoid running containers as root - use `USER` instruction to specify a non-root user- Remove build tools and unnecessary packages from the final image- Scan the final image for vulnerabilities- Set restrictive file permissions- Use multi-stage builds to avoid including build secrets in the final image

## Performance Considerations

- Use build arguments for configuration that might change between environments- Leverage build cache efficiently by ordering layers from least to most frequently changing- Consider parallelization in build steps when possible- Set appropriate environment variables like NODE_ENV=production to optimize runtime behavior- Use appropriate healthchecks for the application type with the HEALTHCHECK instruction

## Template References

Templates in `templates/multi-stage-dockerfile/`:- `phases.md`

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
