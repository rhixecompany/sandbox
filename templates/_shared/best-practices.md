# Shared Template — Prompt Engineering Best Practices

Cross-cutting best practices applicable to all prompts.

## Content Rules

| Rule | Description |
|------|-------------|
| **DRY** | Never repeat the same instruction across sections. Cross-reference instead. |
| **Action-first** | Lead with the command/action, explain after. |
| **Verification gates** | Every prompt should have explicit success criteria. |
| **Strict sequential** | When a phase depends on the previous, mark it as "only then" — never reorder. |

## Frontmatter Hygiene

- Always include `trigger:` field matching filename
- `dependencies:` for skill references via `skill:<name>` format
- `skills:` for the actual Hermes skills to load
- Tags categorize: `hermes`, `copilot`, `opencode` as appropriate

## Prompt Structure

```
## Goal            — One-paragraph objective
## Context         — When and why to use this prompt
## Rules           — Non-negotiable constraints (top 15% of content)
## Phases          — Step-by-step execution workflow
## Verification    — How to confirm success
## Template Refs   — Link to extracted template files
```

## Safety First

- **Pre-audit** — Extract critical constraints before any transformation
- **During** — Follow rules strictly; no deviation
- **Post-audit** — Verify constraints still preserved
- **Rollback** — If verification fails, revert and report
