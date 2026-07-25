---
author: Alexa
description: Suggest relevant GitHub Copilot Custom Agents from the awesome-copilot repository based on repository context and chat history. Use when analyzing local .github/agents coverage, detecting outdated Custom Agents, and recommending new agents from the awesome-copilot catalog.
license: MIT
metadata:
  hermes:
    tags: [imported, github, copilot, agents, recommendations, catalog]
name: suggest-awesome-github-copilot-agents
tags:
- imported
- github
- copilot
- agents
- recommendations
- catalog
- scripts
title: Suggest Awesome GitHub Copilot Agents
version: 1.1.0
---

# Suggest Awesome GitHub Copilot Agents

## Overview

Analyze current repository context and suggest relevant Custom Agents files from the [GitHub awesome-copilot repository](https://github.com/github/awesome-copilot/blob/main/docs/README.agents.md) that are not already available in this repository. Custom Agent files are located in the [agents](https://github.com/github/awesome-copilot/tree/main/agents) folder of the awesome-copilot repository.

## When to Use

- Analyzing current repository context for missing Copilot Custom Agents
- Detecting outdated `.github/agents` files that need updates
- Recommending new agents from the community catalog
- Onboarding teams to Copilot agent best practices

## When NOT to Use

- Creating new agent files from scratch (use `prompt-builder`)
- Validating agent frontmatter (use `validate-prompts`)
- General Copilot usage questions (use `copilot-cli-quickstart`)

## Workflow

### Phase 1: Fetch Available Custom Agents

```bash
# Fetch the community agents catalog
curl -s https://raw.githubusercontent.com/github/awesome-copilot/main/docs/README.agents.md > /tmp/awesome-agents.md

# Parse available agents
grep -E "^###|^##" /tmp/awesome-agents.md
```

### Phase 2: Scan Local Custom Agents

```bash
# Discover existing agent files
find .github/agents -name "*.agent.md" 2>/dev/null | head -20

# Extract descriptions from front matter
for f in .github/agents/*.agent.md; do
  echo "=== $f ==="
  head -30 "$f" | grep -A5 "description:"
done
```

### Phase 3: Extract Descriptions

Read front matter from local agent files to get descriptions and tool configurations.

### Phase 4: Fetch Remote Versions

For each local agent, fetch the corresponding version from awesome-copilot:

```bash
# Pattern for raw GitHub URLs
https://raw.githubusercontent.com/github/awesome-copilot/main/agents/<filename>
```

### Phase 5: Compare Versions

Compare local agent content with remote versions to identify:
- Agents that are up-to-date (exact match)
- Agents that are outdated (content differs)
- Key differences in outdated agents (tools, description, content)

### Phase 6: Analyze Context

Review chat history, repository files, and current project needs:
- Programming languages used (.cs, .js, .py, etc.)
- Framework indicators (ASP.NET, React, Azure, etc.)
- Project types (web apps, APIs, libraries, tools)
- Documentation needs (README, specs, ADRs)

### Phase 7: Match Relevance

Compare available agents against identified patterns and requirements.

### Phase 8: Present Options

Display relevant agents with descriptions, rationale, and availability status including outdated agents.

### Phase 9: Validate

Ensure suggested agents would add value not already covered by existing agents.

### Phase 10: Output

Provide structured table with suggestions, descriptions, and links to both awesome-copilot agents and similar local agents.

**AWAIT** user request to proceed with installation or updates of specific agents. DO NOT INSTALL OR UPDATE UNLESS DIRECTED TO DO SO.

### Phase 11: Download/Update Assets

For requested agents:
- Download new agents to `.github/agents/` folder
- Update outdated agents by replacing with latest version
- Do NOT adjust content of the files
- Use `fetch` tool to download assets

## Verification Checklist

- [ ] Community catalog fetched successfully
- [ ] Local `.github/agents/` files inventoried
- [ ] Front matter descriptions extracted
- [ ] Remote versions fetched for comparison
- [ ] Version differences documented with specifics
- [ ] Context analysis performed against repo stack
- [ ] Relevance matching completed
- [ ] Output table generated with all columns
- [ ] User approval awaited before any install/update
- [ ] Downloads use fetch tool, track with todos

## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `fetch` | HTTP requests to GitHub |
| `github` | GitHub API access |
| `prompt-builder` | Scaffold new agent files |

## Related Skills

- `suggest-awesome-github-copilot-instructions` — Suggest Copilot instruction files
- `copilot-cli-quickstart` — Learn Copilot CLI basics
- `copilot-sdk` — Embed Copilot in applications
- `github` — GitHub API operations

## Usage Examples

```bash
# Analyze current repo and suggest agents
suggest-awesome-github-copilot-agents --analyze

# Fetch latest catalog and compare
suggest-awesome-github-copilot-agents --fetch --compare

# Output as JSON for CI integration
suggest-awesome-github-copilot-agents --format json

# Dry run
suggest-awesome-github-copilot-agents --dry-run
```

## Error Handling

- **Catalog fetch failed:** Falls back to cached copy, warns user
- **No .github directory:** Creates scaffold, continues with recommendations
- **Network timeout:** Uses `--timeout` flag, defaults to 30s
- **Dry-run mode:** Uses `--dry-run` flag, outputs plan without changes

## Pitfalls

- **GitHub API rate limits:** Fetching from raw.githubusercontent.com may hit unauthenticated rate limits (~60 requests/hour). When scanning many agents, batch fetches and add delays between batches.
- **Tool configuration drift:** The `tools` array in agent frontmatter changes frequently as new MCP tools are added or renamed. Minor differences (e.g., `'web/fetch'` vs `'fetch'`) change agent capabilities — always surface exact tool differences.
- **Overwhelming suggestions:** Presenting more than 5-7 agent suggestions at once overwhelms the user. Prioritize by relevance: outdated agents first, then new highly-relevant agents, then nice-to-have additions.
- **False duplicates:** Two agents may have different names but nearly identical functionality. Check not just filenames but also tool arrays and descriptions when detecting duplicates.
- **User approval required:** The scan and suggestion workflow is separate from installation. Never install or update agents without explicit user direction, regardless of how clear the need seems.

## References

- GitHub awesome-copilot: <https://github.com/github/awesome-copilot>
- `references/agents-catalog.md` — Parsed community catalog
- `references/matching-rules.md` — Relevance matching algorithm
- `references/tool-config-drift.md` — Tracking tool array changes