---
name: firecrawl-crawl
version: 1.0.0
title: Firecrawl Crawl
author: Hermes Skills Team
description: |
category: web-development
  Bulk extract content from an entire website or site section. Use this skill when the user wants to crawl a site, extract all pages from a docs section, bulk-scrape multiple pages following links, or says "crawl", "get all the pages", "extract everything under /docs", "bulk extract", or needs content from many pages on the same site. Handles depth limits, path filtering, and concurrent extraction.
allowed-tools:
  - Bash(firecrawl *)
  - Bash(npx firecrawl *)
license: MIT
metadata:
  hermes:
    tags: []
---
# firecrawl crawl

Bulk extract content from a website. Crawls pages following links up to a depth/limit.


## When to Use

- When you need to automate or structure workflows for `firecrawl-crawl`.
- When executing multi-step tasks that benefit from phased orchestration.
- When you need deterministic, verifiable tool execution.

## Overview

Automated reasoning and workflow tool for `firecrawl-crawl`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## When to use

- You need content from many pages on a site (e.g., all `/docs/`)
- You want to extract an entire site section
- Step 4 in the [workflow escalation pattern](firecrawl-cli): search → scrape → map → **crawl** → interact

## Quick start

```bash
# Crawl a docs section
firecrawl crawl "<url>" --include-paths /docs --limit 50 --wait -o .firecrawl/crawl.json

# Full crawl with depth limit
firecrawl crawl "<url>" --max-depth 3 --wait --progress -o .firecrawl/crawl.json

# Check status of a running crawl
firecrawl crawl <job-id>
```

## Options

| Option                    | Description                                 |
| ------------------------- | ------------------------------------------- |
| `--wait`                  | Wait for crawl to complete before returning |
| `--progress`              | Show progress while waiting                 |
| `--limit <n>`             | Max pages to crawl                          |
| `--max-depth <n>`         | Max link depth to follow                    |
| `--include-paths <paths>` | Only crawl URLs matching these paths        |
| `--exclude-paths <paths>` | Skip URLs matching these paths              |
| `--delay <ms>`            | Delay between requests                      |
| `--max-concurrency <n>`   | Max parallel crawl workers                  |
| `--pretty`                | Pretty print JSON output                    |
| `-o, --output <path>`     | Output file path                            |

## Tips

- Always use `--wait` when you need the results immediately. Without it, crawl returns a job ID for async polling.
- Use `--include-paths` to scope the crawl — don't crawl an entire site when you only need one section.
- Crawl consumes credits per page. Check `firecrawl credit-usage` before large crawls.

## See also

- [firecrawl-scrape](../firecrawl-scrape/SKILL.md) — scrape individual pages
- [firecrawl-map](../firecrawl-map/SKILL.md) — discover URLs before deciding to crawl
- [firecrawl-download](../firecrawl-download/SKILL.md) — download site to local files (uses map + scrape)

## Pitfalls

- **None identified yet** — Review edge cases and failure modes for this skill's domain.
- **Assumptions** — Verify platform compatibility (Windows/Mac/Linux) before relying on default paths.
- **State management** — Terminal state persists across calls; exported vars and working directory carry forward.
- **Error handling** — Always validate tool output before proceeding to the next step.

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] Firecrawl Crawl operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Workflow

### Phase 1: Preparation

Set up required environment, dependencies, and configuration for Firecrawl Crawl.

### Phase 2: Execution

Run the primary Firecrawl Crawl operations according to the defined requirements.

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
