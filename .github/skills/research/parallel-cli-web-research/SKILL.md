---
name: parallel-cli-web-research
title: "Parallel CLI — Web Research & Monitoring"
description: "Guide for parallel-cli — web search, content extraction, entity discovery, and change monitoring CLI. Covers extract, findall, and monitor subcommands."
version: 1.0.0
author: "Hermes Assistant"
tags: [research, web-scraping, monitoring, search]
---

# Parallel CLI — Web Research & Monitoring

## When to Use
- Extracting clean content from URLs (`parallel-cli extract`)
- Discovering entities from the web by natural language (`parallel-cli findall`)
- Monitoring web pages for changes (`parallel-cli monitor`)

## Key Commands

### Content Extraction
```bash
parallel-cli extract <url> [url...]
parallel-cli extract --objective "<goal>" <url>
parallel-cli extract --full-content <url>
parallel-cli extract --query "<keyword>" <url>
```

### Entity Discovery (FindAll)
```bash
parallel-cli findall ingest "<natural language objective>"  # Generate schema
parallel-cli findall run <run-id>                            # Execute search
parallel-cli findall poll <run-id>                           # Wait for results
parallel-cli findall enrich <run-id>                         # Add enrichments
parallel-cli findall extend <run-id>                         # Get more matches
parallel-cli findall result <run-id>                         # Fetch results
```

### Web Monitoring
```bash
parallel-cli monitor create <config>    # Create monitor
parallel-cli monitor list               # List monitors
parallel-cli monitor events <id>        # View events
parallel-cli monitor delete <id>        # Delete monitor
```

## Pitfalls
- `--full-content` can be expensive — use `--objective` for targeted extraction
- FindAll is async — use `poll` to wait for completion
- Monitors persist across sessions
- OAuth credentials at `~/.config/parallel-web-tools/credentials.json`
