---
name: firecrawl-agent
version: 1.0.0
title: Firecrawl Agent
author: Hermes Skills Team
description: |
category: web-development
  AI-powered autonomous data extraction that navigates complex sites and returns structured JSON. Use this skill when the user wants structured data from websites, needs to extract pricing tiers, product listings, directory entries, or any data as JSON with a schema. Triggers on "extract structured data", "get all the products", "pull pricing info", "extract as JSON", or when the user provides a JSON schema for website data. More powerful than simple scraping for multi-page structured extraction.
allowed-tools:
  - Bash(firecrawl *)
  - Bash(npx firecrawl *)
license: MIT
metadata:
  hermes:
    tags: []
---
# firecrawl agent

AI-powered autonomous extraction. The agent navigates sites and extracts structured data (takes 2-5 minutes).


## When to Use

- When you need to automate or structure workflows for `firecrawl-agent`.
- When executing multi-step tasks that benefit from phased orchestration.
- When you need deterministic, verifiable tool execution.

## Overview

Automated reasoning and workflow tool for `firecrawl-agent`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## When to use

- You need structured data from complex multi-page sites
- Manual scraping would require navigating many pages
- You want the AI to figure out where the data lives

## Quick start

```bash
# Extract structured data
firecrawl agent "extract all pricing tiers" --wait -o .firecrawl/pricing.json

# With a JSON schema for structured output
firecrawl agent "extract products" --schema '{"type":"object","properties":{"name":{"type":"string"},"price":{"type":"number"}}}' --wait -o .firecrawl/products.json

# Focus on specific pages
firecrawl agent "get feature list" --urls "<url>" --wait -o .firecrawl/features.json
```

## Options

| Option                 | Description                               |
| ---------------------- | ----------------------------------------- |
| `--urls <urls>`        | Starting URLs for the agent               |
| `--model <model>`      | Model to use: spark-1-mini or spark-1-pro |
| `--schema <json>`      | JSON schema for structured output         |
| `--schema-file <path>` | Path to JSON schema file                  |
| `--max-credits <n>`    | Credit limit for this agent run           |
| `--wait`               | Wait for agent to complete                |
| `--pretty`             | Pretty print JSON output                  |
| `-o, --output <path>`  | Output file path                          |

## Tips

- Always use `--wait` to get results inline. Without it, returns a job ID.
- Use `--schema` for predictable, structured output — otherwise the agent returns freeform data.
- Agent runs consume more credits than simple scrapes. Use `--max-credits` to cap spending.
- For simple single-page extraction, prefer `scrape` — it's faster and cheaper.

## See also

- [firecrawl-scrape](../firecrawl-scrape/SKILL.md) — simpler single-page extraction
- [firecrawl-interact](../firecrawl-interact/SKILL.md) — scrape + interact for manual page interaction (more control)
- [firecrawl-crawl](../firecrawl-crawl/SKILL.md) — bulk extraction without AI

## Pitfalls

- **None identified yet** — Review edge cases and failure modes for this skill's domain.
- **Assumptions** — Verify platform compatibility (Windows/Mac/Linux) before relying on default paths.
- **State management** — Terminal state persists across calls; exported vars and working directory carry forward.
- **Error handling** — Always validate tool output before proceeding to the next step.

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] Firecrawl Agent operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Workflow

### Phase 1: Preparation

Set up required environment, dependencies, and configuration for Firecrawl Agent.

### Phase 2: Execution

Run the primary Firecrawl Agent operations according to the defined requirements.

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
