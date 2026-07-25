---
name: sandbox-opencode-config
description: "OpenCode Configuration"
version: 1.0.0
author: Alexa
---
     1|# OpenCode Configuration
     2|
     3|## Main Config: `.opencode/opencode.json`
     4|
     5|### Model
     6|
     7|- `opencode/qwen3.6-plus-free`
     8|
     9|### MCP Servers
    10|
    11|| Server | Type | Purpose |
    12|| --- | --- | --- |
    13|| context7 | remote | Library documentation lookup |
    14|| exa | remote | Web search |
    15|| filesystem | local | File system access (C:/Users/Alexa) |
    16|| gh_grep | remote | GitHub code search |
    17|| MCP_DOCKER | local | GitHub automation (docker mcp gateway) |
    18|| memory | local | Knowledge graph |
    19|| next-devtools | local | Next.js dev tools |
    20|| playwright | local | Browser automation |
    21|| sequential-thinking | local | Step-by-step reasoning |
    22|
    23|### Plugins (17 active)
    24|
    25|- opencode-handoff, @tarquinen/opencode-dcp, @spoons-and-mirrors/subtask2
    26|- @tarquinen/opencode-smart-title, opencode-optimal-model-temps
    27|- @nick-vi/opencode-type-inject, octto, @howaboua/opencode-planning-toolkit
    28|- @zenobius/opencode-background, superpowers (local)
    29|- smart-codebase, opencode-mystatus, @slkiser/opencode-quota
    30|- opencode-gemini-auth, micode, opencode-copilot-usage-detector
    31|- opencode-rate-limit, opencode-cost-guard, oh-my-opencode-slim
    32|
    33|### Rules (22 files)
    34|
    35|All loaded from `.opencode/rules/`: building, code-review, commit-messages, context7, custom-instructions, debugging, documentation, github-automation, github-session-limits, memory-bank, nextjs-tailwind, performance, planning, playwright-typescript, process-workflows, security, sequential-thinking, system-control, task-implementation, tasksync, testing, typescript
    36|
    37|### Hooks
    38|
    39|- `.opencode/hooks/session-start` - Runs at session start
    40|- `.opencode/hooks/hooks.json` - Hook configuration
    41|
    42|### Projects (26 configs)
    43|
    44|YAML files in `.opencode/projects/` defining project-specific settings.
    45|
    46|### Skills (60+)
    47|
    48|Located in `.opencode/skills/`. Key skills: brainstorming, banking, frontend-design, context7, test-driven-development, systematic-debugging, shadcn, webapp-testing.
    49|
    50|## Plugin Archive
    51|
    52|40+ archived plugins in `.opencode/plugins-archive/` - don't modify these.
    53|
    54|## Superpowers Plugin
    55|
    56|- Location: `file:///C:/Users/Alexa/.config/opencode/plugin-src/superpowers`
    57|- Injects `using-superpowers` skill at session start via `.opencode/plugin/superpowers.ts`
    58|- Provides skills, agents, commands for enhanced workflow
    59|