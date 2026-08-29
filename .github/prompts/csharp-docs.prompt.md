---
name: csharp-docs
title: C# API Documentation
description: "Generate comprehensive XML documentation comments and API docs for C# classes, methods, properties, and exceptions following .NET documentation conventions."
trigger: /csharp-docs
version: 1.0.0
author: Hermes Agent
tags:
- csharp
- dotnet
- documentation
- api
- xml-docs
- coding
- tooling
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
- [Guidance for all APIs](#guidance-for-all-apis)
- [Method](#method)
- [Constructors](#constructors)
- [Properties](#properties)
- [Exceptions](#exceptions)
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
- [Guidance for all APIs](#guidance-for-all-apis)
- [Method](#method)
- [Constructors](#constructors)
- [Properties](#properties)
- [Exceptions](#exceptions)
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





Ensure that C# types are documented with XML comments and follow best practices for documentation.

## C# Documentation Best Practices- Public members should be documented with XML comments.

- It is encouraged to document internal members as well, especially if they are complex or not self-explanatory.

## Guidance for all APIs

- Use `<summary

> ` to provide a brief, one sentence, description of what the type or member does. Start the summary with a present-tense, third-person verb.

- Use `<remarks>` for additional information, which can include implementation details, usage notes, or any other relevant context.
- Use `<see langword>` for language-specific keywords like `null`,`true`,`false`,`int`,`bool`, etc.
- Use`<c>` for inline code snippets.
- Use `<example>` for usage examples on how to use the member. - Use `<code>` for code blocks. `<code>` tags should be placed within an `<example>` tag. Add the language of the code example using the `language` attribute, for example, `<code language="csharp">`.- Use`<see cref>` to reference other types or members inline (in a sentence).- Use `<seealso>` for standalone (not in a sentence) references to other types or members in the "See also" section of the online docs.
- Use `<inheritdoc/>` to inherit documentation from base classes or interfaces. - Unless there is major behavior change, in which case you should document the differences.

## Method

s- Use `<param>` to describe method parameters. - The description should be a noun phrase that doesn't specify the data type. - Begin with an introductory article. - If the parameter is a flag enum, start the description with "A bitwise combination of the enumeration values that specifies...". - If the parameter is a non-flag enum, start the description with "One of the enumeration values that specifies...". - If the parameter is a Boolean, the wording should be of the form "`<see langword="true" />` to ...; otherwise, `<see langword="false" />`.". - If the parameter is an "out" parameter, the wording should be of the form "When this method returns, contains .... This parameter is treated as uninitialized.".- Use `<paramref>` to reference parameter names in documentation.

- Use `<typeparam>` to describe type parameters in generic types or methods.
- Use `<typeparamref>` to reference type parameters in documentation.
- Use `<returns>` to describe what the method returns. - The description should be a noun phrase that doesn't specify the data type. - Begin with an introductory article. - If the return type is Boolean, the wording should be of the form "`<see langword="true" />` if ...; otherwise, `<see langword="false" />`.".

## Constructors

- The summary wording should be "Initializes a new instance of the <Class

> class [or struct].".

## Properties

- The `<summary

> ` should start with: - "Gets or sets..." for a read-write property. - "Gets..." for a read-only property. - "Gets [or sets] a value that indicates whether..." for properties that return a Boolean value.

- Use `<value>` to describe the value of the property. - The description should be a noun phrase that doesn't specify the data type. - If the property has a default value, add it in a separate sentence, for example, "The default is `<see langword="false" />`". - If the value type is Boolean, the wording should be of the form "`<see langword="true" />` if ...; otherwise, `<see langword="false" />`. The default is ...".

## Exceptions

- Use `<exception cref

> ` to document exceptions thrown by constructors, properties, indexers, methods, operators, and events.

- Document all exceptions thrown directly by the member.
- For exceptions thrown by nested members, document only the exceptions users are most likely to encounter.
- The description of the exception describes the condition under which it's thrown. - Omit "Thrown if ..." or "If ..." at the beginning of the sentence. Just state the condition directly, for example "An error occurred when accessing a Message Queuing API."

## Template References

Templates in `templates/csharp-docs/`:- `methods.md`

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

Same-family prompts:

- [`csharp-async.prompt.md`](csharp-async.prompt.md)
- [`csharp-mcp-server-generator.prompt.md`](csharp-mcp-server-generator.prompt.md)
- [`csharp-mstest.prompt.md`](csharp-mstest.prompt.md)
- [`csharp-nunit.prompt.md`](csharp-nunit.prompt.md)
- [`csharp-tunit.prompt.md`](csharp-tunit.prompt.md)
- [`csharp-xunit.prompt.md`](csharp-xunit.prompt.md)