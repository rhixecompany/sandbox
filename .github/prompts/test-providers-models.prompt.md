---
name: test-providers-models
title: 'Test Providers & Models'
description: 'Inventory providers, discover models, benchmark accessible free models, compare providers, analyze rate limits/fallbacks, create/update automation scripts, and enrich findings with web research and external API documentation.'
version: 1.1.0
license: MIT
author: Hermes Agent
tags:
  - ai-assistant
  - configuration
  - prompts
  - testing
  - typescript
  - workflow
trigger: /test-providers-models
formatter: default
dependencies:
  - skill:using-superpowers
  - skill:user-communication-preferences
  - skill:verification-before-completion
metadata:
  hermes: {}
toolsets: None
scripts: []
skills: []
plan: None
---
## Goal

Inventory providers, discover models, benchmark accessible free models, compare providers, analyze rate limits/fallbacks, create/update automation scripts, and enrich findings with web research and external API documentation.

# Test Providers & Models

## Context

- **Hermes config/profile:** use live `hermes auth list` + provider config as source of truth.
- **Progress artifact:** `docs/orchestrator-progress.md`
- **Verification artifact:** `docs/orchestrator-verification.md`

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

1. Execute phases in order; do not reorder.
2. Treat rate-limit findings as volatile; re-check before depending on them.
3. If a benchmark path or script is missing, report the exact missing path instead of fabricating results.

## Phases

Full phase instructions live in `templates/test-providers-models/phases.md`.

| Order | Phase | Gate |
| --- | --- | --- |
| 0 | Auth & Provider Inventory | all authorized providers captured and documented |
| 1 | Model Catalog Discovery | catalog entries documented per provider |
| 2 | Free Model Extraction | free-tier model table complete |
| 3 | Provider-by-Provider Benchmarking | benchmark outputs saved per provider/model |
| 4 | Cross-Provider Comparison & Report | comparison report generated and reviewed |
| 5 | Rate Limit & Fallback Chain Analysis | fallback recommendation completed |
| 6 | Script Creation & Automation | scripts runnable and preserved |

## Verification Checklist

- [ ] Phase 0 completed and verified
- [ ] Phase 1 completed and verified
- [ ] Phase 2 completed and verified
- [ ] Phase 3 completed and verified
- [ ] Phase 4 completed and verified
- [ ] Phase 5 completed and verified
- [ ] Phase 6 completed and verified
- [ ] Progress logged in `docs/orchestrator-progress.md`
- [ ] Final verification report in `docs/orchestrator-verification.md`

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

## Workflow

See [`templates/_shared/section-skeleton.md`](templates/_shared/section-skeleton.md) for workflow structure.

1. **Read** — Understand existing code.
2. **Plan** — Design approach.
3. **Implement** — Write code with tests.
4. **Test** — Run all tests.
5. **Review** — Check quality and edge cases.

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

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
