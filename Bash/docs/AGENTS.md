---
title: Agent Configurations — Bash Toolkit
description: Subagent routing rules and configurations for AI-assisted development on the Bash toolkit project.
status: active
tags: [agents, routing, mindmodel, bash, ai-development]
updated: 2026-05-27
---

## Hermes and Copilot

- Use the nearest `AGENTS.md` for files under `Bash/docs/`; this file is the
  local guidance for this folder.
- Follow `../AGENTS.md` and `../../.github/copilot-instructions.md` for the main
  toolkit conventions when writing or updating docs.
- Root Hermes orchestration assets live in `../../.github/agents/hermes.agent.md`
  and `../../.github/prompts/`.
- Keep documentation workflows synchronized with the toolkit source of truth.

     1|# Agent Configurations
     2|
     3|This file defines subagent routing rules and configurations for AI-assisted development on this project.
     4|
     5|## Agent Registry
     6|
     7|### Core Analysis Agents
     8|
     9|| Agent | Purpose | Trigger Keywords |
    10|| --- | --- | --- |
    11|| `mm-stack-detector` | Identify tech stack | general analysis, detect stack |
    12|| `mm-dependency-mapper` | Map library usage | dependencies, imports, packages |
    13|| `mm-convention-extractor` | Extract coding conventions | style, conventions, formatting |
    14|| `mm-domain-extractor` | Extract business terminology | domain, business logic |
    15|| `mm-code-clusterer` | Group similar patterns | patterns, clustering |
    16|| `mm-pattern-discoverer` | Identify pattern categories | architecture, design patterns |
    17|| `mm-anti-pattern-detector` | Find inconsistencies | issues, bugs, anti-patterns |
    18|
    19|### Utility Agents
    20|
    21|| Agent | Purpose | Trigger Keywords |
    22|| --- | --- | --- |
    23|| `mm-constraint-writer` | Assemble mindmodel | write constraints, generate model |
    24|
    25|## Subagent Routing Rules
    26|
    27|### By Task Type
    28|
    29|#### Code Analysis Tasks
    30|
    31|```
    32|Route to: mm-anti-pattern-detector
    33|When: "analyze", "review", "fix", "bug", "issue", "problem"
    34|```
    35|
    36|#### Dependency Tasks
    37|
    38|```
    39|Route to: mm-dependency-mapper
    40|When: "dependencies", "imports", "packages", "requires", "package.json"
    41|```
    42|
    43|#### Pattern Tasks
    44|
    45|```
    46|Route to: mm-pattern-discoverer
    47|When: "pattern", "architecture", "design", "structure"
    48|```
    49|
    50|#### Documentation Tasks
    51|
    52|```
    53|Route to: mm-convention-extractor
    54|When: "document", "comment", "docstring", "readme", "guide"
    55|```
    56|
    57|### By File Type
    58|
    59|| Extension | Primary Agent            | Secondary Agent         |
    60|| --------- | ------------------------ | ----------------------- |
    61|| `.sh`     | mm-stack-detector        | mm-convention-extractor |
    62|| `.ps1`    | mm-stack-detector        | mm-convention-extractor |
    63|| `.bat`    | mm-stack-detector        | mm-convention-extractor |
    64|| `.md`     | mm-convention-extractor  | mm-domain-extractor     |
    65|| `.log`    | mm-anti-pattern-detector | mm-dependency-mapper    |
    66|
    67|## Workflows
    68|
    69|### Phase 1: Analysis (Parallel Execution)
    70|
    71|All 7 analysis agents run concurrently via `spawn_agent`:
    72|
    73|```javascript
    74|spawn_agent({
    75|  agents: [
    76|    { agent: "mm-stack-detector", prompt: "...", description: "..." },
    77|    {
    78|      agent: "mm-dependency-mapper",
    79|      prompt: "...",
    80|      description: "..."
    81|    },
    82|    {
    83|      agent: "mm-convention-extractor",
    84|      prompt: "...",
    85|      description: "..."
    86|    },
    87|    {
    88|      agent: "mm-domain-extractor",
    89|      prompt: "...",
    90|      description: "..."
    91|    },
    92|    { agent: "mm-code-clusterer", prompt: "...", description: "..." },
    93|    {
    94|      agent: "mm-pattern-discoverer",
    95|      prompt: "...",
    96|      description: "..."
    97|    },
    98|    {
    99|      agent: "mm-anti-pattern-detector",

100| prompt: "...", 101| description: "..." 102| } 103| ] 104|}); 105|``    106|    107|### Phase 2: Assembly    108|    109|After Phase 1 completes, route to `mm-constraint-writer`:    110|    111|``javascript 112|spawn_agent({ 113| agents: [ 114| { 115| agent: "mm-constraint-writer", 116| prompt: "Assemble all findings...", 117| description: "Write constraints" 118| } 119| ] 120|}); 121|`    122|    123|## Context Guidelines    124|    125|### What to Include in Prompts    126|    127|1. **Task description** — What the agent should analyze    128|2. **File paths** — Which files to examine    129|3. **Output format** — What structure to return    130|4. **Constraints** — Any limitations or focus areas    131|    132|### Example Prompt Template    133|    134|` 135|Analyze {files} for {purpose}. 136| 137|Focus areas: 138|- {specific requirement 1} 139|- {specific requirement 2} 140| 141|Output format: 142|{ 143| "findings": [...], 144| "summary": "..." 145|} 146|``    147|    148|## Mindmodel Integration    149|    150|The `.mindmodel/` directory contains constraint files generated from analysis. These are Markdown files organized by category (stack, style, patterns) rather than monolithic YAML files.    151|    152|`` 153|.mindmodel/ 154|├── manifest.md # Index of all constraints 155|├── stack/dependencies.md # Tech stack definitions 156|├── style/config.md # Configuration standards 157|├── style/naming.md # Naming conventions 158|├── patterns/\*.md # Design patterns 159|└── examples/ # Code examples 160|`    161|    162|### Lookup Usage    163|    164|`javascript 165|// When implementing features 166|mindmodel_lookup({ query: "create upgrade function" }); 167| 168|// Returns relevant patterns and examples from .mindmodel/ 169|```   170|    171|## Configuration    172|    173|### Agent Behavior Flags    174|    175|| Flag | Default | Purpose |    176|| --- | --- | --- |    177||`parallel_execution`| true | Run independent agents concurrently |    178||`timeout_seconds`| 120 | Maximum time per agent |    179||`retry_on_failure`| true | Retry failed agents once |    180|    181|### Output Preferences    182|    183|| Setting              | Value | Notes                         |    184|| -------------------- | ----- | ----------------------------- |    185||`verbose_logging`   | false | Log all agent interactions    |    186||`cache_results`     | true  | Reuse analysis results        |    187||`incremental_update` | true | Only re-analyze changed files | 188| 189|## Anti-Patterns to Avoid 190| 191|- ❌ Running agents sequentially when parallel is possible 192|- ❌ Skipping Phase 1 before Phase 2 193|- ❌ Ignoring agent error results 194|- ❌ Overwriting .mindmodel without analysis 195|- ❌ Missing progress output during long operations 196|
