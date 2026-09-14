---
name: datadog-installation
description: "Datadog CLI Reference"
version: 1.0.0
author: Alexa
---
     1|# Datadog CLI Reference
     2|
     3|A CLI tool for AI agents to debug and triage using Datadog logs and metrics.
     4|
     5|## Setup
     6|
     7|### Running the CLI
     8|
     9|```bash
    10|bunx @ctdio/datadog-cli <command>
    11|
    12|# Or create an alias for convenience
    13|alias datadog="npx @ctdio/datadog-cli"
    14|```
    15|
    16|### Environment Variables (Required)
    17|
    18|```bash
    19|export DD_API_KEY="your-api-key"
    20|export DD_APP_KEY="your-app-key"
    21|```
    22|
    23|Get keys from: https://app.datadoghq.com/organization-settings/api-keys
    24|
    25|### For Non-US Datadog Sites
    26|
    27|Use `--site` flag:
    28|
    29|```bash
    30|npx @ctdio/datadog-cli logs search --query "*" --site datadoghq.eu
    31|```
    32|