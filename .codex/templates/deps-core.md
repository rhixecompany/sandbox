---
name: deps-core
category: templates/_shared
version: 1.0.0
license: MIT
author: derived from verified prompt references (.github/prompts/*/*.prompt.md references)
description: Shared dependency reference pattern. Used by all run-all-goals artifacts for DRY dependency declaration.
---

# Dependency Patterns — Shared Template

> Source: verified from `.github/prompts/*/*.prompt.md` references (29 matches for `templates/_shared/deps-core.md`). No fabricated dependency names.

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
3. Handle 3 states: has both â insert into existing sections; has `dependencies:` only â create `skills:` after `dependencies:`; has neither â create both.
4. Track state with flags (`in_deps`, `in_skills`, `in_metadata`) so insertion lands in correct section (not `toolsets:`).
5. Verify with `yaml.safe_load` after every batch.

## Verified Dependency Set (From `run-all-goals.prompt.md` frontmatter — Read Directly)

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

This list is derived directly from the verified `.prompt.md` frontmatter (line 17â29). Not synthesized.
