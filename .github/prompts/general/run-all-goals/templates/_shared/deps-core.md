---
name: deps-core
category: templates/_shared
version: 2.0.0
license: MIT
author: derived from verified prompt references (.github/prompts/*/*.prompt.md) + tree.prompt.txt
description: Shared dependency reference pattern. Used by all run-all-goals artifacts for DRY dependency declaration. tree.prompt.txt is PRIMARY source.
---

# Dependency Patterns — Shared Template

> Sources: verified from `.github/prompts/*/*.prompt.md` references + **`tree.prompt.txt`** (PRIMARY source defining cleanup-first execution). No fabricated dependency names.

## Dependency Prefix Convention (Verified from Batch Audit Patterns)

| Prefix | Meaning | Example (verified) |
|---|---|---|
| `skill:` | Hermes skill | `skill:using-superpowers`, `skill:brainstorming`, `skill:systematic-debugging`, `skill:subagent-driven-development` |
| `tool:` | MCP/native tool | `tool:filesystem`, `tool:github`, `tool:sequential-thinking`, `tool:playwright` |
| `prompt:` | Other prompt (reference only) | `prompt:test-providers-models` (verified present at workspace root reference) |

## Dependency Injection Rule (From `references/batch-skill-injection.md` / `prompt-management` skill)

When adding a new dependency across artifacts:

1. Add to `dependencies:` (YAML list item with prefix): `- skill:<name>`.
2. Also add to `skills:` (bare name list): `- <name>`.
3. Handle 3 states: has both — insert into existing sections; has `dependencies:` only — create `skills:` after `dependencies:`; has neither — create both.
4. Track state with flags (`in_deps`, `in_skills`, `in_metadata`) so insertion lands in correct section (not `toolsets:`).
5. Verify with `yaml.safe_load` after every batch.

## Verified Dependency Set (From `run-all-goals.prompt.md` frontmatter + tree.prompt.txt — Read Directly)

```yaml
dependencies:
  - skill:using-superpowers
  - skill:brainstorming
  - skill:user-communication-preferences
  - skill:mcp-sequential-thinking
  - skill:systematic-debugging
  - skill:subagent-driven-development
  - skill:hermes-diagnostic-repair
  - skill:log-analysis-and-triage
  - tool:filesystem
  - tool:github
  - tool:memory
  - tool:playwright
  - tool:sequential-thinking
```

This list is derived directly from the verified `.prompt.md` frontmatter + tree.prompt.txt directives. Not synthesized.

## Tree-Primary Dependencies (From tree.prompt.txt)

tree.prompt.txt defines the execution scope. Dependencies are derived from tree.prompt.txt's goal directives:
- `/goal` directives imply `skill:using-superpowers`, `skill:brainstorming`, `skill:user-communication-preferences`
- `/mcp-*` directives imply `tool:filesystem`, `tool:ast-grep`, `tool:memory`, `tool:sequential-thinking`
- `/writing-clearly-and-concisely`, `/subagent-driven-development` imply corresponding skills
- Cleanup operations imply `tool:filesystem`, `tool:terminal` for deletion/verification
