---
description: "Analyze chatmode or prompt files and recommend optimal AI models based on task complexity, required capabilities, and cost-efficiency"
agent: "agent"
tools:
  - "search/codebase"
  - "fetch"
  - "context7/*"
model: Auto (copilot)
---

## Goal

Analyze chatmode or prompt files and recommend optimal AI models based on task complexity, required capabilities, and cost-efficiency.

## Context

Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.

## Phases

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
- Return the final artifact or findings clearly.
- Stop once the requested result is delivered.

## Legacy Prompt Details
```text
# AI Model Recommendation for Copilot Chat Modes and Prompts

## Mission

Analyze `.agent.md` or `.prompt.md` files to understand their purpose, complexity, and required capabilities, then recommend the most suitable AI model(s) from GitHub Copilot's available options. Provide rationale based on task characteristics, model strengths, cost-efficiency, and performance trade-offs.

## Scope & Preconditions

- **Input**: Path to a `.agent.md` or `.prompt.md` file
- **Available Models**: GPT-4.1, GPT-5, GPT-5 mini, GPT-5 Codex, Claude Sonnet 3.5, Claude Sonnet 4, Claude Sonnet 4.5, Claude Opus 4.1, Gemini 2.5 Pro, Gemini 2.0 Flash, Grok Code Fast 1, o3, o4-mini (with deprecation dates)
- **Model Auto-Selection**: Available in VS Code (Sept 2025+) - selects from GPT-4.1, GPT-5 mini, GPT-5, Claude Sonnet 3.5, Claude Sonnet 4.5 (excludes premium multipliers > 1)
- **Context**: GitHub Copilot subscription tiers (Free: 2K completions + 50 chat/month with 0x models only; Pro: unlimited 0x + 1000 premium/month; Pro+: unlimited 0x + 5000 premium/month)

## Inputs

Required:

- `${input:filePath:Path to .agent.md or .prompt.md file}` - Absolute or workspace-relative path to the file to analyze

Optional:

- `${input:subscriptionTier:Pro}` - User's Copilot subscription tier (Free, Pro, Pro+) - defaults to Pro
- `${input:priorityFactor:Balanced}` - Optimization priority (Speed, Cost, Quality, Balanced) - defaults to Balanced

## Workflow

> ### 1. File Analysis Phase
> **Read and Parse File**:

> **Full content:** `templates/model-recommendation/workflow.md`

## Recommendation: Add Model Specification

Current frontmatter: \`\`\`yaml

---

description: "..." tools: [...]

---

\`\`\`

Recommended frontmatter: \`\`\`yaml

---

description: "..." model: "[Recommended Model Name]" tools: [...]

---

\`\`\`

Rationale: [Explanation of why this model is optimal for this task]
```

If file already specifies a model:

```markdown
## Current Model Assessment

> Specified model: `[Current Model]` (Multiplier: [X]x)
> Recommendation: [Keep current model | Consider switching to [Recommended Model]]

> **Full content:** `templates/model-recommendation/current_model_assessment.md`

## Output Expectations

### Report Structure

Generate a structured markdown report with the following sections:

```markdown
# AI Model Recommendation Report

**File Analyzed**: `[file path]` **File Type**: [chatmode | prompt] **Analysis Date**: [YYYY-MM-DD] **Subscription Tier**: [Free | Pro | Pro+]

---

## File Summary

**Description**: [from frontmatter] **Mode**: [ask | edit | agent] **Tools**: [tool list] **Current Model**: [specified model or "Not specified"]

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

## Model Recommendation

> ### 🏆 Primary Recommendation: [Model Name]
> **Multiplier**: [X]x ([cost implications for subscription tier]) **Strengths**:

> **Full content:** `templates/model-recommendation/model_recommendation.md`

## Auto Model Selection Assessment

**Suitability**: [Recommended | Not Recommended | Situational]

[Explanation of whether auto-selection is appropriate for this task]

**Rationale**:

- [Reason 1]
- [Reason 2]

**Manual Override Scenarios**:

- [Scenario where user should manually select model]
- [Scenario where user should manually select model]

## Implementation Guidance

### Frontmatter Update

[Provide specific code block showing recommended frontmatter change]

### Model Selection in VS Code

**To Use Recommended Model**:

1. Open Copilot Chat
2. Click model dropdown (currently shows "[current model or Auto]")
3. Select **[Recommended Model Name]**
4. [Optional: When to switch back to Auto]

**Keyboard Shortcut**: `Cmd+Shift+P` → "Copilot: Change Model"

### Tool Alignment Verification

[Check results: Are specified tools compatible with recommended model?]

✅ **Compatible Tools**: [list] ⚠️ **Potential Limitations**: [list if any]

## Deprecation Notices

[If applicable, list any deprecated models in current configuration]

⚠️ **Deprecated Model in Use**: [Model Name] (Deprecation date: [YYYY-MM-DD])

**Migration Path**:

- **Current**: [Deprecated Model]
- **Replacement**: [Recommended Model]
- **Action Required**: Update `model:` field in frontmatter by [date]
- **Behavioral Changes**: [any expected differences]

## Context7 Verification

[If Context7 was used for verification]

**Queries Executed**:

- Topic: "[query topic]"
- Library: `/websites/github_en_copilot`
- Key Findings: [summary]

## Additional Considerations

### Subscription Tier Recommendations

[Specific advice based on Free/Pro/Pro+ tier]

### Priority Factor Adjustments

[If user specified Speed/Cost/Quality/Balanced, explain how recommendation aligns]

### Long-Term Model Strategy

[Advice for when to re-evaluate model selection as file evolves]

---

## Quick Reference

**TL;DR**: Use **[Primary Model]** for this task due to [one-sentence rationale]. Cost: [X]x multiplier.

**One-Line Update**: \`\`\`yaml model: "[Recommended Model Name]" \`\`\`
```

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

> **Full content:** `templates/model-recommendation/quality_assurance.md`

## Advanced Use Cases

### Analyzing Multiple Files

If user provides multiple files:

1. Analyze each file individually
2. Generate separate recommendations per file
3. Provide summary table comparing recommendations
4. Note any patterns (e.g., "All debug-related modes benefit from Claude Sonnet 4.5")

### Comparative Analysis

If user asks "Which model is better between X and Y for this file?":

1. Focus comparison on those two models only
2. Use side-by-side table format
3. Declare a winner with specific reasoning
4. Include cost comparison for subscription tier

### Migration Planning

If file specifies a deprecated model:

1. Prioritize migration guidance in report
2. Test current behavior expectations vs. replacement model capabilities
3. Provide phased migration if breaking changes expected
4. Include rollback plan if needed

## Examples

### Example 1: Simple Formatting Task

**File**: `format-code.prompt.md` **Content**: "Format Python code with Black style, add type hints" **Recommendation**: GPT-5 mini (0x multiplier, fastest, sufficient for repetitive formatting) **Alternative**: Grok Code Fast 1 (0.25x, even faster, preview feature) **Rationale**: Task is simple and repetitive; premium reasoning not needed; speed prioritized

### Example 2: Complex Architecture Review

**File**: `architect.agent.md` **Content**: "Review system design for scalability, security, maintainability; analyze trade-offs; provide ADR-level recommendations" **Recommendation**: Claude Sonnet 4.5 (1x multiplier, expert reasoning, excellent for architecture) **Alternative**: Claude Opus 4.1 (10x, use for very large codebases >500K tokens) **Rationale**: Requires deep reasoning, architectural expertise, design pattern knowledge; Sonnet 4.5 excels at this

### Example 3: Django Expert Mode

**File**: `django.agent.md` **Content**: "Django 5.x expert with ORM optimization, async views, REST API design; uses context7 for up-to-date Django docs" **Recommendation**: GPT-5 (1x multiplier, advanced reasoning, excellent code quality) **Alternative**: Claude Sonnet 4.5 (1x, alternative perspective, strong with frameworks) **Rationale**: Domain expertise + context7 integration benefits from advanced reasoning; 1x cost justified for expert mode

### Example 4: Free Tier User with Planning Mode

**File**: `plan.agent.md` **Content**: "Research and planning mode with read-only tools (search, fetch, githubRepo)" **Subscription**: Free (2K completions + 50 chat requests/month, 0x models only) **Recommendation**: GPT-4.1 (0x, balanced, included in Free tier) **Alternative**: GPT-5 mini (0x, faster but less context) **Rationale**: Free tier restricted to 0x models; GPT-4.1 provides best balance of quality and context for planning tasks

## Knowledge Base

> ### Model Multiplier Cost Reference
> ### Model Changelog & Deprecations (October 2025)

> **Full content:** `templates/model-recommendation/knowledge_base.md`

## Context7 Query Templates

> Use these query patterns when verification needed:
> **Model Capabilities**:

> **Full content:** `templates/model-recommendation/context7_query_templates.md`

## Template References

Detailed section templates in `templates/model-recommendation/`:
- `context7_query_templates.md`
- `current_model_assessment.md`
- `knowledge_base.md`
- `model_recommendation.md`
- `quality_assurance.md`
- `workflow.md`
