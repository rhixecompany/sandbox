---

name: remember

title: Memory Keeper

description: 'Transforms lessons learned into domain-organized memory instructions (global or workspace). Syntax: `/remember [>domain [scope]] lesson clue` where scope is `global` (default), `user`, `workspace`, or `ws`.'

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

  - ml

  - prompts

  - specification

  - typescript

trigger: /remember

dependencies: []

metadata:

  hermes: {}

---

## Goal

Transforms lessons learned into domain-organized memory instructions (global or workspace). Syntax: `/remember [>domain [scope]] lesson clue` where scope is `global` (default), `user`, `workspace`, or `ws`.

## Context

Use when you need to remember for the current workspace or task.

## Input

s

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Output

s

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

## Scope

sMemory instructions can be stored in two scopes:- **Global** (`global` or `user`) - Stored in `<global-prompts>` (`vscode-userdata:/User/prompts/`) and apply to all VS Code projects- **Workspace** (`workspace` or `ws`) - Stored in `<workspace-instructions>` (`<workspace-root>/.github/instructions/`) and apply only to the current projectDefault scope is **global**.Throughout this prompt, `<global-prompts>` and `<workspace-instructions>` refer to these directories.

## Your Mission

Transform debugging sessions, workflow discoveries, frequently repeated mistakes, and hard-won lessons into **domain-specific, reusable knowledge**, that helps the agent to effectively find the best patterns and avoid common mistakes. Your intelligent categorization system automatically:- **Discovers existing memory domains** via glob patterns to find `vscode-userdata:/User/prompts/*-memory.instructions.md` files- **Matches learnings to domains** or creates new domain files when needed- **Organizes knowledge contextually** so future AI assistants find relevant guidance exactly when needed- **Builds institutional memory** that prevents repeating mistakes across all projectsThe result: a **self-organizing, domain-driven knowledge base** that grows smarter with every lesson learned.

## Syntax

```/remember [>domain-name [scope]] lesson content```- `>domain-name` - Optional. Explicitly target a domain (e.g., `>clojure`, `>git-workflow`)- `[scope]` - Optional. One of: `global`, `user` (both mean global), `workspace`, or `ws`. Defaults to `global`- `lesson content` - Required. The lesson to remember**Examples:**- `/remember >shell-scripting now we've forgotten about using fish syntax too many times`- `/remember >clojure prefer passing maps over parameter lists`- `/remember avoid over-escaping`- `/remember >clojure workspace prefer threading macros for readability`- `/remember >testing ws use setup/teardown functions`**Use the todo list** to track your progress through the process steps and keep the user informed.

## Memory File Structure

### Description Frontmatter

Keep domain file descriptions general, focusing on the domain responsibility rather than implementation specifics.

### Apply to Frontmatter

Target specific file patterns and locations relevant to the domain using glob patterns. Keep the glob patterns few and broad, targeting directories if the domain is not specific to a language, or file extensions if the domain is language-specific.

### Main Headline

Use level 1 heading format: `# <Domain Name

> Memory`

### Tag Line

Follow the main headline with a succinct tagline that captures the core patterns and value of that domain's memory file.

### LearningsEach distinct lesson has its own level 2 headline

## Process

> 1. **Parse input** - Extract domain (if `>domain-name` specified) and scope (`gl
> 2. **Glob and Read the start of** existing memory and instruction files to under

## Quality Guidelines

- **Generalize beyond specifics** - Extract reusable patterns rather than task-specific details- Be specific and concrete (avoid vague advice)- Include code examples when relevant- Focus on common, recurring issues- Keep instructions succinct, scannable, and actionable- Clean up redundancy- Instructions focus on what to do, not what to avoid

## Update Triggers

Common scenarios that warrant memory updates:

- Repeatedly forgetting the same shortcuts or commands- Discovering effective workflows- Learning domain-specific best practices- Finding reusable problem-solving approaches- Coding style decisions and rationale- Cross-project patterns that work well

## Template References

Detailed templates in `templates/remember/`:- `process.md`

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

## Goal

Transforms lessons learned into domain-organized memory instructions (global or workspace). Syntax: `/remember [>domain [scope]] lesson clue` where scope is `global` (default), `user`, `workspace`, or `ws`.

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
