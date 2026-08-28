---
name: model-recommendation
title: Model Recommendation
description: Analyzes chatmode or prompt files and recommends optimal AI models based on task complexity, capabilities, and cost-efficiency.
version: 1.0.0
author: Hermes Agent
date: '2026-08-25'
tags:
  - model
  - recommendation
  - analysis
  - routing
  - ai
  - cost
  - capabilities
  - planning
metadata:
  hermes:
    profile: code-architect
    priority: medium
  copilot:
    model_required: sonnet
  opencode:
    enabled: true
  codex:
    enabled: true
---
## Table of Contents

## Goal

## Context

## Phases



# Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand off](#phase-4:-hand-off)
- [Mission](#mission)
- [Scope & Preconditions](#scope-&-preconditions)
- [Prompt Variables](#prompt-variables)
- [Workflow](#workflow)
  - [1. File Analysis Phase](#1-file-analysis-phase)
- [Recommendation: Add Model Specification](#recommendation:-add-model-specification)
- [Current Model Assessment](#current-model-assessment)
- [Output Expectations](#output-expectations)
  - [Report Structure](#report-structure)
- [File Summary**Description**: [from frontmatter] **Mode**: [ask](#file-summary**description**:-[from-frontmatter]-**mode**:-[ask)
- [Task Analysis](#task-analysis)
  - [Task Complexity](#task-complexity)
  - [Task Category](#task-category)
  - [Key Characteristics](#key-characteristics)
- [Model Recommendation>](#model-recommendation>)
  - [🏆 Primary Recommendation: [Model Name]](#🏆-primary-recommendation:-[model-name])
- [Auto Model Selection Assessment](#auto-model-selection-assessment)
- [Implementation Guidance](#implementation-guidance)
  - [Frontmatter Update](#frontmatter-update)
  - [Model Selection in VS Code**To Use Recommended Model**:](#model-selection-in-vs-code**to-use-recommended-model**:)
  - [Tool Alignment Verification](#tool-alignment-verification)
- [Deprecation Notices](#deprecation-notices)
- [Additional Considerations](#additional-considerations)
  - [Subscription Tier Recommendations](#subscription-tier-recommendations)
  - [Priority Factor Adjustments](#priority-factor-adjustments)
  - [Long-Term Model Strategy](#long-term-model-strategy)
- [Quick Reference](#quick-reference)
  - [Output Quality Standards](#output-quality-standards)
- [Quality Assurance](#quality-assurance)
- [Advanced Use Cases](#advanced-use-cases)
  - [Analyzing Multiple Files](#analyzing-multiple-files)
  - [Comparative Analysis](#comparative-analysis)
  - [Migration Planning](#migration-planning)
- [Examples](#examples)
  - [Example 1: Simple Formatting Task](#example-1:-simple-formatting-task)
  - [Example 2: Complex Architecture Review](#example-2:-complex-architecture-review)
  - [Example 3: Django Expert Mode](#example-3:-django-expert-mode)
  - [Example 4: Free Tier User with Planning Mode](#example-4:-free-tier-user-with-planning-mode)
- [Knowledge Base](#knowledge-base)
  - [Model Multiplier Cost Reference](#model-multiplier-cost-reference)
  - [Model Changelog & Deprecations (October 2025)](#model-changelog-&-deprecations-october-2025)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)



- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Intake](#phase-1:-intake)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Hand off](#phase-4:-hand-off)
- [Mission](#mission)
- [Scope & Preconditions](#scope-&-preconditions)
- [Prompt Variables](#prompt-variables)
- [Workflow](#workflow)
- [1. File Analysis Phase](#1-file-analysis-phase)
- [Recommendation: Add Model Specification](#recommendation:-add-model-specification)
- [Current Model Assessment](#current-model-assessment)
- [Output Expectations](#output-expectations)
- [Report Structure](#report-structure)
- [File Summary**Description**: [from frontmatter] **Mode**: [ask](#file-summary**description**:-[from-frontmatter]-**mode**:-[ask)
- [Task Analysis](#task-analysis)
- [Task Complexity](#task-complexity)
- [Task Category](#task-category)
- [Key Characteristics](#key-characteristics)
- [Model Recommendation>](#model-recommendation>)
- [🏆 Primary Recommendation: [Model Name]](#🏆-primary-recommendation:-[model-name])
- [Auto Model Selection Assessment](#auto-model-selection-assessment)
- [Implementation Guidance](#implementation-guidance)
- [Frontmatter Update](#frontmatter-update)
- [Model Selection in VS Code**To Use Recommended Model**:](#model-selection-in-vs-code**to-use-recommended-model**:)
- [Tool Alignment Verification](#tool-alignment-verification)
- [Deprecation Notices](#deprecation-notices)
- [Additional Considerations](#additional-considerations)
- [Subscription Tier Recommendations](#subscription-tier-recommendations)
- [Priority Factor Adjustments](#priority-factor-adjustments)
- [Long-Term Model Strategy](#long-term-model-strategy)
- [Quick Reference](#quick-reference)
- [Output Quality Standards](#output-quality-standards)
- [Quality Assurance](#quality-assurance)
- [Advanced Use Cases](#advanced-use-cases)
- [Analyzing Multiple Files](#analyzing-multiple-files)
- [Comparative Analysis](#comparative-analysis)
- [Migration Planning](#migration-planning)
- [Examples](#examples)
- [Example 1: Simple Formatting Task](#example-1:-simple-formatting-task)
- [Example 2: Complex Architecture Review](#example-2:-complex-architecture-review)
- [Example 3: Django Expert Mode](#example-3:-django-expert-mode)
- [Example 4: Free Tier User with Planning Mode](#example-4:-free-tier-user-with-planning-mode)
- [Knowledge Base](#knowledge-base)
- [Model Multiplier Cost Reference](#model-multiplier-cost-reference)
- [Model Changelog & Deprecations (October 2025)](#model-changelog-&-deprecations-october-2025)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)





Analyze chatmode or prompt files and recommend optimal AI models based on task complexity, required capabilities, and cost-efficiency.


Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.


### Phase 1: Intake

- Read the request and identify the exact scope.
- Locate the relevant files, diffs, or references.

### Phase 2: Execute

- Perform the requested work with the smallest safe change set.
- Keep the steps explicit and reproducible.

### Phase 3: Verify

- Check the result against the goal, rules, and inputs.
- Confirm the output is usable and complete.

### Phase 4: Hand off

- Return the final artifact or findings .
- Stop once the requested result is delivered.

## Mission

Analyze `.agent.md` or `.prompt.md` files to understand their purpose, complexity, and required capabilities, then recommend the most suitable AI model(s) from GitHub Copilot's available options. Provide rationale based on task characteristics, model strengths, cost-efficiency, and performance trade-offs.

## Scope & Preconditions

- **Input**: Path to a `.agent.md` or `.prompt.md` file- **Available Models**: GPT-4.1, GPT-5, GPT-5 mini, GPT-5 Codex, Claude Sonnet 3.5, Claude Sonnet 4, Claude Sonnet 4.5, Claude Opus 4.1, Gemini 2.5 Pro, Gemini 2.0 Flash, Grok Code Fast 1, o3, o4-mini (with deprecation dates)- **Model Auto-Selection**: Available in VS Code (Sept 2025+) - selects from GPT-4.1, GPT-5 mini, GPT-5, Claude Sonnet 3.5, Claude Sonnet 4.5 (excludes premium multipliers

> 1)- **Context**: GitHub Copilot subscription tiers (Free: 2K completions + 50 chat/month with 0x models only; Pro: unlimited 0x + 1000 premium/month; Pro+: unlimited 0x + 5000 premium/month)

## Prompt Variables

Required:- `${input:filePath:Path to .agent.md or .prompt.md file}` - Absolute or workspace-relative path to the file to analyzeOptional:- `${input:subscriptionTier:Pro}` - User's Copilot subscription tier (Free, Pro, Pro+) - defaults to Pro- `${input:priorityFactor:Balanced}` - Optimization priority (Speed, Cost, Quality, Balanced) - defaults to Balanced

## Workflow

### 1. File Analysis Phase

>
> **Read and Parse File**:
> **Full content:**

## Recommendation: Add Model Specification

Current frontmatter: \`\`\`yaml---description: "..." tools: [...]---\`\`\`Recommended frontmatter: \`\`\`yaml---description: "..." model: "[Recommended Model Name]" tools: [...]---\`\`\`Rationale: [Explanation of why this model is optimal for this task]```If file already specifies a model:```markdown

## Current Model Assessment

> Specified model: `[Current Model]` (Multiplier: [X]x)
> Recommendation: [Keep current model | Consider switching to [Recommended Model]]
> **Full content:**

## Output Expectations

### Report Structure

Generate a structured markdown report with the following sections:```markdown# AI Model Recommendation Report**File Analyzed**: `[file path]` **File Type**: [chatmode | prompt] **Analysis Date**: [YYYY-MM-DD] **Subscription Tier**: [Free | Pro | Pro+]---

## File Summary**Description**: [from frontmatter] **Mode**: [ask

| edit | agent] **Tools**: [tool list] **Current Model**: [specified model or "Not specified"]

## Task Analysis

### Task Complexity

- **Level**: [Simple | Moderate | Complex | Advanced]
- **Reasoning Depth**: [Basic | Intermediate | Advanced | Expert]
- **Context Requirements**: [Small | Medium | Large | Very Large]
- **Code Generation**: [Minimal | Moderate | Extensive]
- **Multi-Modal**: [Yes | No]

### Task Category

[Primary category from 8 categories listed in Workflow Phase 1]

### Key Characteristics

- Characteristic 1: [explanation]
- Characteristic 2: [explanation]
- Characteristic 3: [explanation]

## Model Recommendation>

### 🏆 Primary Recommendation: [Model Name]

> **Multiplier**: [X]x ([cost implications for subscription tier]) **Strengths**:
> **Full content:**

## Auto Model Selection Assessment

**Suitability**: [Recommended | Not Recommended | Situational]

*Explanation of whether auto-selection is appropriate for this task*

**Rationale**:

- [Reason 1]
- [Reason 2]

**Manual Override Scenarios**:

- [Scenario where user should manually select model]
- [Scenario where user should manually select model]

## Implementation Guidance

### Frontmatter Update

[Provide specific code block showing recommended frontmatter change]

### Model Selection in VS Code**To Use Recommended Model**:

1. Open Copilot Chat
2. Click model dropdown (currently shows "[current model or Auto]")
3. Select **[Recommended Model Name]**
4. [Optional: When to switch back to Auto]**Keyboard Shortcut**: `Cmd+Shift+P` → "Copilot: Change Model"

### Tool Alignment Verification

[Check results: Are specified tools compatible with recommended model?]✅ **Compatible Tools**: [list] ⚠️ **Potential Limitations**: [list if any]

## Deprecation Notices

[If applicable, list any deprecated models in current configuration]⚠️ **Deprecated Model in Use**: [Model Name] (Deprecation date: [YYYY-MM-DD])**Migration Path**:- **Current**: [Deprecated Model]- **Replacement**: [Recommended Model]- **Action Required**: Update `model:` field in frontmatter by [date]- **Behavioral Changes**: [any expected differences]

## Additional Considerations

### Subscription Tier Recommendations

[Specific advice based on Free/Pro/Pro+ tier]

### Priority Factor Adjustments

[If user specified Speed/Cost/Quality/Balanced, explain how recommendation aligns]

### Long-Term Model Strategy

[Advice for when to re-evaluate model selection as file evolves]---

## Quick Reference

**TL;DR**: Use **[Primary Model]** for this task due to [one-sentence rationale]. Cost: [X]x multiplier. Use **[Primary Model]** for this task due to [one-sentence rationale]. Cost: [X]x multiplier.**One-Line Update**: \`\`\`yaml model: "[Recommended Model Name]" \`\`\````

### Output Quality Standards

- **Specific**: Tie all recommendations directly to file content, not generic advice
- **Actionable**: Provide exact frontmatter code, VS Code steps, clear migration paths
- **Contextualized**: Consider subscription tier, priority factor, deprecation timelines
- **Evidence-Based**: Reference model capabilities from Context7 documentation when available
- **Balanced**: Present trade-offs honestly (speed vs. quality vs. cost)
- **Up-to-Date**: Flag deprecated models, suggest current alternatives

## Quality Assurance

> - [ ] File successfully read and parsed
> - [ ] Frontmatter extracted correctly (or noted if missing)

## Advanced Use Cases

### Analyzing Multiple Files

If user provides multiple files:1. Analyze each file individually2. Generate separate recommendations per file3. Provide summary table comparing recommendations4. Note any patterns (e.g., "All debug-related modes benefit from Claude Sonnet 4.5")

### Comparative Analysis

If user asks "Which model is better between X and Y for this file?":1. Focus comparison on those two models only2. Use side-by-side table format3. Declare a winner with specific reasoning4. Include cost comparison for subscription tier

### Migration Planning

If file specifies a deprecated model:

## Examples

### Example 1: Simple Formatting Task

**File**: `format-code.prompt.md` **Content**: "Format Python code with Black style, add type hints" **Recommendation**: GPT-5 mini (0x multiplier, fastest, sufficient for repetitive formatting) **Alternative**: Grok Code Fast 1 (0.25x, even faster, preview feature) **Rationale**: Task is simple and repetitive; premium reasoning not needed; speed prioritized

### Example 2: Complex Architecture Review

**File**: `architect.agent.md` **Content**: "Review system design for scalability, security, maintainability; analyze trade-offs; provide ADR-level recommendations" **Recommendation**: Claude Sonnet 4.5 (1x multiplier, expert reasoning, excellent for architecture) **Alternative**: Claude Opus 4.1 (10x, use for very large codebases

> 500K tokens) **Rationale**: Requires deep reasoning, architectural expertise, design pattern knowledge; Sonnet 4.5 excels at this

### Example 3: Django Expert Mode

**File**: `django.agent.md` **Content**: "Django 5.x expert with ORM optimization, async views, REST API design; uses context7 for up-to-date Django docs" **Recommendation**: GPT-5 (1x multiplier, advanced reasoning, excellent code quality) **Alternative**: Claude Sonnet 4.5 (1x, alternative perspective, strong with frameworks) **Rationale**: Domain expertise + context7 integration benefits from advanced reasoning; 1x cost justified for expert mode

### Example 4: Free Tier User with Planning Mode

**File**: `plan.agent.md` **Content**: "Research and planning mode with read-only tools (search, fetch, githubRepo)" **Subscription**: Free (2K completions + 50 chat requests/month, 0x models only) **Recommendation**: GPT-4.1 (0x, balanced, included in Free tier) **Alternative**: GPT-5 mini (0x, faster but less context) **Rationale**: Free tier restricted to 0x models; GPT-4.1 provides best balance of quality and context for planning tasks

## Knowledge Base

### Model Multiplier Cost Reference

### Model Changelog & Deprecations (October 2025)

## Template References

Detailed section templates in `templates/model-recommendation/`:- `context7_query_templates.md`- `current_model_assessment.md`- `knowledge_base.md`- `model_recommendation.md`- `quality_assurance.md`- `workflow.md`

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section