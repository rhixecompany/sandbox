---
trigger: /boost-prompt
description: >-
  Interactive prompt refinement workflow: interrogates scope, deliverables, and constraints, then copies final markdown to clipboard using Joyride.
tags: [hermes, copilot, writing-skills, refinement, joyride]
dependencies:
  - skill:writing-skills
  - skill:writing-plans
  - tool:joyride
  - command:/context-map
  - command:/prompt-engineering
skills:
  - writing-skills — Crafting and optimizing prompts and instructions
  - writing-plans — Structured prompt authoring
---

# boost-prompt

> Interactive prompt refinement workflow: interrogates scope, deliverables, constraints; copies final markdown to clipboard; never writes code.

## Goal

Iteratively refine a user's task prompt into a high-quality, detailed prompt through interrogation, exploration, and structured formatting.

## Context

Use when you need to improve a draft prompt before submitting it to an AI system. Requires the Joyride VS Code extension for clipboard operations. This prompt does NOT write code - it only refines prompts.

**Critical rules (must appear within the first 15% of execution):**
- DO NOT WRITE ANY CODE - this is a prompt refinement workflow only
- Always ask clarifying questions before finalizing the prompt
- Copy the final markdown to clipboard using Joyride after each revision

## Inputs

- A draft prompt from the user
- The current workspace context (for project exploration)
- Optional constraints or specific requirements

## Outputs

- An improved, structured prompt in markdown format
- Prompt copied to system clipboard via Joyride
- Verification that the user is satisfied with the result

## Rules

1. **No code** - DO NOT write any code; this workflow is for prompt refinement only
2. **Interrogate first** - Ask specific questions to understand scope, objectives, deliverables, and constraints before refining
3. **Explore the project** - Use available tools to understand the codebase and task context
4. **Map context first** - Run `/context-map` before deep prompt refinement so file and dependency context is explicit
5. **Structured output** - Organize the prompt into clear sections or steps
6. **Clipboard delivery** - Use Joyride to copy the final markdown to the system clipboard
7. **Iterate** - After delivering, ask the user if they want changes or additions

## Skills Required

| Skill | Purpose |
| --- | --- |
| `context-map` | Preflight map of relevant files and references before refinement |
| `writing-skills` | Crafting and optimizing prompts and instructions |
| `writing-plans` | Structured prompt authoring and organization (section layout, phase flow) |

## Tools Required

| Tool | Purpose |
| --- | --- |
| `joyride_request_human_input` | Interactive user input via VS Code Joyride extension |
| `vscode.env.clipboard.writeText` | Copy text to system clipboard via Joyride (ClojureScript API) |

### Joyride Setup

**Requirement**: VS Code Joyride extension installed and active

**Installation**:
- Install from VS Code Extensions marketplace: search "Joyride"
- Verify in command palette: `Joyride: Open Prompt Library`

**API Reference**:
- `joyride_request_human_input` - Prompts user for multi-line input via VS Code dialog
- `vscode.env.clipboard.writeText(text)` - Copies text to system clipboard (requires active Joyride context)

**Fallback**: If Joyride is unavailable, manually copy the final prompt from Phase 3 output to your clipboard

## Phases

### Phase 1: Interrogate

**Goal:** Understand the task scope, objectives, deliverables, and constraints.

**Steps:**
1. Read the user's draft prompt
2. Ask specific questions using `joyride_request_human_input` to clarify scope, deliverables, and constraints
3. Explore the project workspace using available tools to understand context
4. Run `/context-map` on the target area before producing the refined prompt

### Phase 2: Refine

**Goal:** Produce an improved, well-structured prompt.

**Steps:**
1. Organize the prompt into clear sections or steps
2. Apply markdown formatting for readability
3. Ensure the prompt is easy to understand and follow
4. Define expected deliverables and success criteria

### Phase 3: Deliver

**Goal:** Deliver the prompt to the user and system clipboard.

**Steps:**
1. Copy the prompt to the system clipboard using Joyride:

   ```clojure
   (require '["vscode" :as vscode])
   (vscode/env.clipboard.writeText "your-markdown-text-here")
   ```

2. Announce to the user that the prompt is on the clipboard
3. Type the prompt in chat

**Note**: If Joyride is unavailable (see "Tools Required" -> Fallback), manually select and copy the prompt text from your chat output.

### Phase 4: Iterate

**Goal:** Confirm satisfaction and handle revisions.

**Steps:**
1. Ask the user if they want any changes or additions
2. Repeat Phase 2-4 after any revisions
3. Stop once the user confirms satisfaction

## Actions Summary

1. Interrogate the user about scope, deliverables, and constraints
2. Explore the project workspace for context
3. Refine the prompt into structured markdown
4. Copy to clipboard via Joyride
5. Present in chat
6. Ask for feedback and iterate if needed
