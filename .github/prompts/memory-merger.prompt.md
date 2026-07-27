---
name: memory-merger
title: Memory Merger
description: 'Merges mature lessons from a domain memory file into its instruction file. Syntax:
  `/memory-merger >domain [scope]` where scope is `global` (default), `user`, `workspace`,
  or `ws`.'
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills: []
formatter: default
plan: ''
tags:
  - ml
  - prompts
  - specification
  - typescript
trigger: /memory-merger
---

## GoalMerges mature lessons from a domain memory file into its instruction file. Syntax: `/memory-merger >domain [scope]` where scope is `global` (default), `user`, `workspace`, or `ws`.## ContextUse when you need to memory merger for the current workspace or task.## Inputs- The current workspace, repo, or document state.- The specific request, diff, spec, or files provided by the user.- Any prompt variables, paths, or constraints named in the original instructions.## Outputs- A complete result that matches the prompt's purpose.- A concise verification note when the task benefits from one.## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Follow the prompt literally and prefer evidence from the current workspace.- Keep the response structured, deterministic, and easy to act on.- Avoid changing unrelated files or adding unnecessary scope.- If something is unclear, state the assumption instead of guessing.## Phases### Phase 1: Intake- Read the request and identify the exact scope.- Locate the relevant files, diffs, or references.### Phase 2: Execute- Perform the requested work with the smallest safe change set.- Keep the steps explicit and reproducible.### Phase 3: Verify- Check the result against the goal, rules, and inputs.- Confirm the output is usable and complete.### Phase 4: Hand off- Return the final artifact or findings clearly.- Stop once the requested result is delivered.## ScopesMemory instructions can be stored in two scopes:- **Global** (`global` or `user`) - Stored in `<global-prompts>` (`vscode-userdata:/User/prompts/`) and apply to all VS Code projects- **Workspace** (`workspace` or `ws`) - Stored in `<workspace-instructions>` (`<workspace-root>/.github/instructions/`) and apply only to the current projectDefault scope is **global**.Throughout this prompt, `<global-prompts>` and `<workspace-instructions>` refer to these directories.## Syntax```/memory-merger >domain-name [scope]```- `>domain-name` - Required. The domain to merge (e.g., `>clojure`, `>git-workflow`, `>prompt-engineering`)- `[scope]` - Optional. One of: `global`, `user` (both mean global), `workspace`, or `ws`. Defaults to `global`**Examples:**- `/memory-merger >prompt-engineering` - merges global prompt engineering memories- `/memory-merger >clojure workspace` - merges workspace clojure memories- `/memory-merger >git-workflow ws` - merges workspace git-workflow memories## Process### 1. Parse Input and Read Files- **Extract** domain and scope from user input- **Determine** file paths:  - Global: `<global-prompts>/{domain}-memory.instructions.md` → `<global-prompts>/{domain}.instructions.md`  - Workspace: `<workspace-instructions>/{domain}-memory.instructions.md` → `<workspace-instructions>/{domain}.instructions.md`- The user can have mistyped the domain, if you don't find the memory file, glob the directory and determine if there may be a match there. Ask the user for input if in doubt.- **Read** both files (memory file must exist; instruction file may not)### 2. Analyze and ProposeReview all memory sections and present them for merger consideration:```## Proposed Memories for Merger> ### Memory: [Headline]> **Content:** [Key points]> **Full content:** `templates/memory-merger/proposed_memories_for_mer.md`## Example```User: "/memory-merger >clojure"Agent:1. Reads clojure-memory.instructions.md and clojure.instructions.md2. Proposes 3 memories for merger3. [STOPS]User: "go"Agent:4. Defines quality bar for 10/105. Merges new instructions candidate, iterates to 10/106. Updates clojure.instructions.md7. Cleans clojure-memory.instructions.md```## Template ReferencesTemplates in `templates/memory-merger/`:- `example.md`- `phases.md`- `process.md`- `proposed_memories_for_mer.md`