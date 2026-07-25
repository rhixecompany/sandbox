---
author: Hermes Agent
description: Suggest relevant GitHub Copilot instruction files from the awesome-copilot repository based on current repository context and chat history. Use when analyzing local instruction coverage, detecting outdated .github/instructions files, or recommending new instructions from the community catalog.
license: MIT
metadata:
  hermes:
    tags: [imported, github, copilot, instructions, recommendations, catalog]
name: suggest-awesome-github-copilot-instructions
tags:
- imported
- github
- copilot
- instructions
- recommendations
- catalog
- scripts
title: Suggest Awesome GitHub Copilot Instructions
version: 1.0.0
---

# Suggest Awesome GitHub Copilot Instructions

## Overview

Analyze current repository context and suggest relevant copilot-instruction files from the [GitHub awesome-copilot repository](https://github.com/github/awesome-copilot/blob/main/docs/README.instructions.md) that are not already available in this repository.

## When to Use

- Analyzing current repository context for missing Copilot instructions
- Detecting outdated `.github/instructions` files that need updates
- Recommending new instructions from the community catalog
- Onboarding teams to Copilot instruction best practices

## When NOT to Use

- Creating new instruction files from scratch (use `prompt-builder`)
- Validating instruction frontmatter (use `validate-prompts`)
- General Copilot usage questions (use `copilot-cli-quickstart`)

## Workflow

### Phase 1: Analyze Repository Context

```bash
# Check existing .github/instructions files
find .github/instructions -name "*.md" 2>/dev/null | head -20

# Get repository language stack
grep -r "language:" .github/ 2>/dev/null | sort -u
```

### Phase 2: Fetch Community Catalog

Download the latest awesome-copilot instructions catalog:

```bash
# Fetch the community catalog
curl -s https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.instructions.md > /tmp/awesome-instructions.md

# Parse available instructions
grep -E "^###|^##" /tmp/awesome-instructions.md
```

### Phase 3: Match & Recommend

Compare local instructions against community catalog and recommend:
- Missing instructions relevant to the repo's tech stack
- Updated versions of existing instructions
- Cross-platform instruction variants

## Verification Checklist

- [ ] Existing `.github/instructions` files inventoried
- [ ] Community catalog fetched successfully
- [ ] Relevance matching performed against repo stack
- [ ] Recommendations include install commands
- [ ] No duplicate suggestions
- [ ] Output saved to actionable format

## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `file` | Read/write files |
| `github` | Access GitHub API for catalog |

## Related Skills

- `suggest-awesome-github-copilot-agents` — Suggest Copilot agent files
- `prompt-builder` — Scaffold new prompt files
- `validate-prompts` — Validate frontmatter schema

## Usage Examples

```bash
# Analyze current repo and suggest instructions
suggest-awesome-github-copilot-instructions --analyze

# Fetch latest catalog and compare
suggest-awesome-github-copilot-instructions --fetch --compare

# Output as JSON for CI integration
suggest-awesome-github-copilot-instructions --format json

# Dry run
suggest-awesome-github-copilot-instructions --dry-run
```

## Error Handling

- **Catalog fetch failed:** Falls back to cached copy, warns user
- **No .github directory:** Creates scaffold, continues with recommendations
- **Network timeout:** Uses `--timeout` flag, defaults to 30s
- **Dry-run mode:** Uses `--dry-run` flag, outputs plan without changes

## Pitfalls

- **Stale catalog:** Community catalog updates frequently — always fetch fresh before recommending
- **Over-recommending:** Only suggest instructions relevant to the repo's actual tech stack
- **Version conflicts:** Local instructions may have customizations — show diff before replacing
- **Auth required:** GitHub API may need token for high-rate requests — use `GITHUB_TOKEN` env var

## References

- GitHub awesome-copilot: <https://github.com/github/awesome-copilot>
- `references/instructions-catalog.md` — Parsed community catalog
- `references/matching-rules.md` — Relevance matching algorithm