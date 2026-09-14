---
name: codemap-readme
description: "Codemap Skill"
version: 1.0.0
author: Alexa
---
     1|# Codemap Skill
     2|
     3|Repository understanding and hierarchical codemap generation.
     4|
     5|## Overview
     6|
     7|Codemap helps orchestrators map and understand codebases by:
     8|
     9|1. Selecting relevant code/config files using LLM judgment
    10|2. Creating `.slim/codemap.json` for change tracking
    11|3. Generating empty `codemap.md` templates for fixers to fill in
    12|
    13|Legacy `.slim/cartography.json` state is migrated to `.slim/codemap.json` automatically.
    14|
    15|## Commands
    16|
    17|```bash
    18|# Initialize mapping
    19|node codemap.mjs init --root /repo --include "src/**/*.ts" --exclude "node_modules/**"
    20|
    21|# Check what changed
    22|node codemap.mjs changes --root /repo
    23|
    24|# Update hashes
    25|node codemap.mjs update --root /repo
    26|```
    27|
    28|## Outputs
    29|
    30|### .slim/codemap.json
    31|
    32|```json
    33|{
    34|  "file_hashes": {
    35|    "src/index.ts": "abc123..."
    36|  },
    37|  "folder_hashes": {
    38|    "src": "def456..."
    39|  },
    40|  "metadata": {
    41|    "version": "1.0.0",
    42|    "last_run": "2026-01-25T19:00:00Z",
    43|    "include_patterns": ["src/**/*.ts"],
    44|    "exclude_patterns": ["node_modules/**"]
    45|  }
    46|}
    47|```
    48|
    49|### codemap.md (per folder)
    50|
    51|Empty templates created in each folder for fixers to fill with:
    52|
    53|- Responsibility
    54|- Design patterns
    55|- Data/control flow
    56|- Integration points
    57|
    58|## Installation
    59|
    60|Installed automatically via oh-my-opencode-slim installer when custom skills are enabled.
    61|