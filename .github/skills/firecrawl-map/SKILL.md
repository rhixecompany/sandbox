---
name: firecrawl-map
version: 1.0.0
title: Firecrawl Map
author: Hermes Skills Team
description: |
category: web-development
  Discover and list all URLs on a website, with optional search filtering. Use this skill when the user wants to find a specific page on a large site, list all URLs, see the site structure, find where something is on a domain, or says "map the site", "find the URL for", "what pages are on", or "list all pages". Essential when the user knows which site but not which exact page.
allowed-tools:
  - Bash(firecrawl *)
  - Bash(npx firecrawl *)
license: MIT
metadata:
  hermes:
    tags: []
---
# firecrawl map

Discover URLs on a site. Use `--search` to find a specific page within a large site.


## When to Use

- When you need to automate or structure workflows for `firecrawl-map`.
- When executing multi-step tasks that benefit from phased orchestration.
- When you need deterministic, verifiable tool execution.

## Overview

Automated reasoning and workflow tool for `firecrawl-map`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## When to use

- You need to find a specific subpage on a large site
- You want a list of all URLs on a site before scraping or crawling
- Step 3 in the [workflow escalation pattern](firecrawl-cli): search → scrape → **map** → crawl → interact

## Quick start

```bash
# Find a specific page on a large site
firecrawl map "<url>" --search "authentication" -o .firecrawl/filtered.txt

# Get all URLs
firecrawl map "<url>" --limit 500 --json -o .firecrawl/urls.json
```

## Options

| Option                            | Description                  |
| --------------------------------- | ---------------------------- |
| `--limit <n>`                     | Max number of URLs to return |
| `--search <query>`                | Filter URLs by search query  |
| `--sitemap <include\|skip\|only>` | Sitemap handling strategy    |
| `--include-subdomains`            | Include subdomain URLs       |
| `--json`                          | Output as JSON               |
| `-o, --output <path>`             | Output file path             |

## Tips

- **Map + scrape is a common pattern**: use `map --search` to find the right URL, then `scrape` it.
- Example: `map https://docs.example.com --search "auth"` → found `/docs/api/authentication` → `scrape` that URL.

## See also

- [firecrawl-scrape](../firecrawl-scrape/SKILL.md) — scrape the URLs you discover
- [firecrawl-crawl](../firecrawl-crawl/SKILL.md) — bulk extract instead of map + scrape
- [firecrawl-download](../firecrawl-download/SKILL.md) — download entire site (uses map internally)

## Pitfalls

- **None identified yet** — Review edge cases and failure modes for this skill's domain.
- **Assumptions** — Verify platform compatibility (Windows/Mac/Linux) before relying on default paths.
- **State management** — Terminal state persists across calls; exported vars and working directory carry forward.
- **Error handling** — Always validate tool output before proceeding to the next step.

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] Firecrawl Map operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Workflow

### Phase 1: Preparation

Set up required environment, dependencies, and configuration for Firecrawl Map.

### Phase 2: Execution

Run the primary Firecrawl Map operations according to the defined requirements.

### Phase 3: Verification

Verify output, handle any errors, and confirm results meet expectations.

### Phase 4: Completion

Document results, clean up resources, and finalize any deliverables.

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
