---

name: copilot-instructions-blueprint-generator

title: Copilot Instructions Blueprint Generator

description: 'Technology-agnostic blueprint generator for creating comprehensive copilot-instructions.md files that guide GitHub Copilot to produce code consistent with project standards, architecture patterns, and exact technology versions by analyzing existing codebase patterns and avoiding assumptions.'

version: 1.0.0

license: MIT

author: Hermes Agent

toolsets:

  - file

  - terminal

scripts: []

skills: []

formatter: default

plan: None

tags:

  - ai-assistant

  - architecture

  - frontend

  - generator

  - git

  - prompts

  - specification

  - typescript

trigger: /copilot-instructions-blueprint-generator

dependencies: []

metadata:

  hermes: {}

---

## Goal

Technology-agnostic blueprint generator for creating comprehensive copilot-instructions.md files that guide GitHub Copilot to produce code consistent with project standards, architecture patterns, and exact technology versions by analyzing existing codebase patterns and avoiding assumptions.

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

## Configuration Variables

${PROJECT_TYPE="Auto-detect|.NET|Java|JavaScript|TypeScript|React|Angular|Python|Multiple|Other"} <!-- Primary technology -->${ARCHITECTURE_STYLE="Layered|Microservices|Monolithic|Domain-Driven|Event-Driven|Serverless|Mixed"} <!-- Architectural approach --> ${CODE_QUALITY_FOCUS="Maintainability|Performance|Security|Accessibility|Testability|All"} <!-- Quality priorities -->${DOCUMENTATION_LEVEL="Minimal|Standard|Comprehensive"} <!-- Documentation requirements --> ${TESTING_REQUIREMENTS="Unit|Integration|E2E|TDD|BDD|All"} <!-- Testing approach -->${VERSIONING="Semantic|CalVer|Custom"} <!-- Versioning approach -->

## Generated Prompt

"Generate a comprehensive copilot-instructions.md file that will guide GitHub Copilot to produce code consistent with our project's standards, architecture, and technology versions. The instructions must be strictly based on actual code patterns in our codebase and avoid making any assumptions. Follow this approach:

### 1. Core Instruction Structure

```markdown
# GitHub Copilot Instructions

## Priority GuidelinesWhen generating code for this repository:1. **Version Compatibility**: Always detect and respect the exact versions of languages, frameworks, and libraries used in this project2. **Context Files**: Prioritize patterns and standards defined in the .github/copilot directory3. **Codebase Patterns**: When context files don't provide specific guidance, scan the codebase for established patterns4. **Architectural Consistency**: Maintain our ${ARCHITECTURE_STYLE} architectural style and established boundaries5. **Code Quality**: Prioritize ${CODE_QUALITY_FOCUS == "All" ? "maintainability, performance, security, accessibility, and testability" : CODE_QUALITY_FOCUS} in all generated code

## Technology Version DetectionBefore generating code, scan the codebase to identify:1. **Language Versions**: Detect the exact versions of programming languages in use

- Examine project files, configuration files, and package managers   - Look for language-specific version indicators (e.g., <LangVersion

> in .NET projects)   - Never use language features beyond the detected version2. **Framework Versions**: Identify the exact versions of all frameworks   - Check package.json, .csproj, pom.xml, requirements.txt, etc.   - Respect version constraints when generating code   - Never suggest features not available in the detected framework versions3. **Library Versions**: Note the exact versions of key libraries and dependencies   - Generate code compatible with these specific versions   - Never use APIs or features not available in the detected versions

## Context FilesPrioritize the following files in .github/copilot directory (if they exist):

- **architecture.md**: System architecture guidelines- **tech-stack.md**: Technology versions and framework details- **coding-standards.md**: Code style and formatting standards- **folder-structure.md**: Project organization guidelines- **exemplars.md**: Exemplary code patterns to follow

## Codebase Scanning InstructionsWhen context files don't provide specific guidance:1. Identify similar files to the one being modified or created2. Analyze patterns for:

- Naming conventions   - Code organization   - Error handling   - Logging approaches   - Documentation style   - Testing patterns3. Follow the most consistent patterns found in the codebase4. When conflicting patterns exist, prioritize patterns in newer files or files with higher test coverage5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

> ${CODE_QUALITY_FOCUS.includes("Maintainability") || CODE_QUALITY_FOCUS == "All"
> - Write self-documenting code with clear naming
> **Full content:**

## Documentation Requirements$

DOCUMENTATION_LEVEL == "Minimal" ? `

- Match the level and style of comments found in existing code- Document according to patterns observed in the codebase- Follow existing patterns for documenting non-obvious behavior- Use the same format for parameter descriptions as existing code` : ""}${DOCUMENTATION_LEVEL == "Standard" ? `- Follow the exact documentation format found in the codebase- Match the XML/JSDoc style and completeness of existing comments- Document parameters, returns, and exceptions in the same style- Follow existing patterns for usage examples- Match class-level documentation style and content` : ""}${DOCUMENTATION_LEVEL == "Comprehensive" ? `- Follow the most detailed documentation patterns found in the codebase- Match the style and completeness of the best-documented code- Document exactly as the most thoroughly documented files do- Follow existing patterns for linking documentation- Match the level of detail in explanations of design decisions` : ""}

## Test

ing Approach> ${TESTING_REQUIREMENTS.includes("Unit") || TESTING_REQUIREMENTS == "All" ? `

### >

- Match the exact structure and style of existing unit tests

> **Full content:**

## Technology-Specific Guidelines

> ${PROJECT_TYPE == ".NET" || PROJECT_TYPE == "Auto-detect" || PROJECT_TYPE == "Mu
> - Detect and strictly adhere to the specific .NET version in use
> **Full content:**

## Version Control Guidelines$

VERSIONING == "Semantic" ? `

- Follow Semantic Versioning patterns as applied in the codebase- Match existing patterns for documenting breaking changes- Follow the same approach for deprecation notices` : ""}${VERSIONING == "CalVer" ? `- Follow Calendar Versioning patterns as applied in the codebase- Match existing patterns for documenting changes- Follow the same approach for highlighting significant changes` : ""}${VERSIONING == "Custom" ? `- Match the exact versioning pattern observed in the codebase- Follow the same changelog format used in existing documentation- Apply the same tagging conventions used in the project` : ""}

## General Best Practices

- Follow naming conventions exactly as they appear in existing code- Match code organization patterns from similar files- Apply error handling consistent with existing patterns- Follow the same approach to testing as seen in the codebase- Match logging patterns from existing code- Use the same approach to configuration as seen in the codebase

## Project

-Specific Guidance> - Scan the codebase thoroughly before generating any code> - Respect existing architectural boundaries without exception> **Full content:** 

## Expected Output

A comprehensive copilot-instructions.md file that will guide GitHub Copilot to produce code that is perfectly compatible with your existing technology versions and follows your established patterns and architecture.

## Template References

Detailed templates in `templates/copilot-instructions-blueprint-generator/`:- `code_quality_standards.md`- `project-specific_guidance.md`- `technology-specific_guidelines.md`- `testing_approach.md`

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
|---|------|-----------|
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
|-------|---------|
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

