---
name: openapi-to-application-code
title: OpenAPI Spec to Application Code
description: Generates a complete, idiomatic application scaffold (controllers, services, models, tests) from an OpenAPI specification in the target framework.
version: 1.0.0
author: Hermes Agent
tags:
  - openapi
  - api
  - codegen
  - backend
  - scaffolding
  - documentation
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
# Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand off](#phase-4:-hand-off)
- [Input Requirements](#input-requirements)
- [Generation Process](#generation-process)
  - [Step 1: Analyze the OpenAPI Specification](#step-1:-analyze-the-openapi-specification)
- [Output Structure](#output-structure)
- [Best Practices Applied](#best-practices-applied)
- [Next Steps](#next-steps)
- [Questions to Ask if Needed](#questions-to-ask-if-needed)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
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


## Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Intake](#phase-1:-intake)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Hand off](#phase-4:-hand-off)
- [Input Requirements](#input-requirements)
- [Generation Process](#generation-process)
- [Step 1: Analyze the OpenAPI Specification](#step-1:-analyze-the-openapi-specification)
- [Output Structure](#output-structure)
- [Best Practices Applied](#best-practices-applied)
- [Next Steps](#next-steps)
- [Questions to Ask if Needed](#questions-to-ask-if-needed)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
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




## Goal

Generate a complete, production-ready application from an OpenAPI specification.

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

- Return the final artifact or findings .
- Stop once the requested result is delivered.

## Input Requirements

1. **OpenAPI Specification**: Provide either:

- A URL to the OpenAPI spec (e.g., `https://api.example.com/openapi.json`) - A local file path to the OpenAPI spec - The full OpenAPI specification content pasted directly2. **Project Details** (if not in spec): - Project name and description - Target framework and version - Package/namespace naming conventions - Authentication method (if not specified in OpenAPI)

## Generation Process

### Step 1: Analyze the OpenAPI Specification

>
> - Validate the OpenAPI spec for completeness and correctness
> **Full content:**

## Output Structure

The generated application will include:```project-name/├── README.md # Setup and usage instructions├── [build-config] # Framework-specific build files (pom.xml, build.gradle, package.json, etc.)├── src/│ ├── main/│ │ ├── [language]/│ │ │ ├── controllers/ # HTTP endpoint handlers│ │ │ ├── services/ # Business logic│ │ │ ├── models/ # Data models and DTOs│ │ │ ├── repositories/ # Data access (if applicable)│ │ │ └── config/ # Application configuration│ │ └── resources/ # Configuration files│ └── test/│ ├── [language]/│ │ ├── controllers/ # Controller tests│ │ └── services/ # Service tests│ └── resources/ # Test configuration├── .gitignore├── .env.example # Environment variables template└── docker-compose.yml # Optional: Docker setup (if applicable)```

## Best Practices Applied

- **Framework Conventions**: Follows framework-specific naming, structure, and patterns- **Separation of Concerns**: Clear layers with controllers, services, and repositories- **Error Handling**: Comprehensive error handling with meaningful responses- **Validation**: Input validation and schema validation throughout- **Logging**: Structured logging for debugging and monitoring- **Testing**: Unit tests for services and controllers- **Documentation**: Inline code documentation and setup instructions- **Security**: Implements authentication/authorization from OpenAPI spec- **Scalability**: Design patterns support growth and maintenance

## Next Steps

After generation:1. Review the generated code structure and make customizations as needed2. Install dependencies according to framework requirements3. Configure environment variables and database connections4. Run tests to verify generated code5. Start the development server6. Test endpoints using the provided examples

## Questions to Ask if Needed

- Should the application include database/ORM setup, or just in-memory/mock data?- Do you want Docker configuration for containerization?- Should authentication be JWT, OAuth2, API keys, or basic auth?- Do you need integration tests or just unit tests?- Any specific database technology preferences?- Should the API include pagination, filtering, and sorting examples?

## Template References

Detailed templates in `templates/openapi-to-application-code/`:- `generation_process.md`

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

## Related Prompts

Same-family prompts:

- [`migrate-to-next16.prompt.md`](migrate-to-next16.prompt.md)