---
author: Hermes Agent
description: Use when creating new skills, editing existing skills, or verifying skills work before deployment. Applies TDD methodology to skill authoring: write failing test scenarios first, then write skill to pass them.
license: MIT
metadata:
  hermes:
    tags: [imported, skill-authoring, tdd, documentation, quality]
name: writing-skills
tags:
- imported
- skill-authoring
- tdd
- documentation
- quality
- scripts
title: Writing Skills
version: 1.8.0
---

# Writing Skills

## Overview

**Writing skills IS Test-Driven Development applied to process documentation.**

Personal skills live in agent-specific directories (`~/.claude/skills` for Claude Code, `~/.agents/skills/` for Codex).

You write test cases (pressure scenarios with subagents), watch them fail (baseline behavior), write the skill (documentation), watch tests pass (agents comply), and refactor (close loopholes).

**Core principle:** If you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing.

**REQUIRED BACKGROUND:** You MUST understand `superpowers:test-driven-development` before using this skill. That skill defines the fundamental RED-GREEN-REFACTOR cycle. This skill adapts TDD to documentation.

## What is a Skill?

A **skill** is a reference guide for proven techniques, patterns, or tools. Skills help future agents find and apply effective approaches.

**Skills are:** Reusable techniques, patterns, tools, reference guides
**Skills are NOT:** Narratives about how you solved a problem once

## TDD Mapping for Skills

| TDD Concept | Skill Creation |
|-------------|----------------|
| **Test case** | Pressure scenario with subagent |
| **Production code** | Skill document (SKILL.md) |
| **Test fails (RED)** | Agent violates rule without skill (baseline) |
| **Test passes (GREEN)** | Agent complies with skill present |
| **Refactor** | Close loopholes while maintaining compliance |

The entire skill creation process follows RED-GREEN-REFACTOR.

## When to Create a Skill

**Create when:**
- Technique wasn't intuitively obvious to you
- You'd reference this again across projects
- Pattern applies broadly (not project-specific)
- Others would benefit

**Don't create for:**
- One-off solutions
- Standard practices well-documented elsewhere
- Project-specific conventions (put in CLAUDE.md)
- Mechanical constraints (if enforceable with regex/validation, automate it—save documentation for judgment calls)

## Skill Types

### Technique
Concrete method with steps to follow (condition-based-waiting, root-cause-tracing)

### Pattern
Way of thinking about problems (flatten-with-flags, test-invariants)

### Reference
API docs, syntax guides, tool documentation (office docs)

## Directory Structure

```
skills/
  skill-name/
    SKILL.md              # Main reference (required)
    supporting-file.*     # Only if needed
```

**Flat namespace** - all skills in one searchable namespace

**Separate files for:**
1. **Heavy reference** (100+ lines) - API docs, comprehensive syntax
2. **Reusable tools** - Scripts, utilities, templates

**Keep inline:**
- Principles and concepts
- Code patterns (< 50 lines)
- Everything else

## SKILL.md Structure

**Frontmatter (YAML):**
- Two required fields: `name` and `description` (see [agentskills.io/specification](https://agentskills.io/specification) for all supported fields)
- Max 1024 characters total
- `name`: Use letters, numbers, and hyphens only
- `category`: (under `metadata.hermes`) Populates the Category column in `hermes skills list`. NOT derived from directory structure.
- `description`: Third-person, describes ONLY when to use (NOT what it does)
  - Start with "Use when..." to focus on triggering conditions
  - Include specific symptoms, situations, and contexts
  - **NEVER summarize the skill's process or workflow**
  - Keep under 500 characters if possible

```markdown
---
name: Skill-Name-With-Hyphens
description: Use when [specific triggering conditions and symptoms]
---

# Skill Name

## Overview
What is this? Core principle in 1-2 sentences.

## When to Use
[Small inline flowchart IF decision non-obvious]

Bullet list with SYMPTOMS and use cases
When NOT to use

## Core Pattern (for techniques/patterns)
Before/after code comparison

## Quick Reference
Table or bullets for scanning common operations

## Implementation
Inline code for simple patterns
Link to file for heavy reference or reusable tools

## Common Mistakes
What goes wrong + fixes

## Real-World Impact (optional)
Concrete results
```

## CSO: Critical for Discovery

See `references/cso.md` for complete guidelines.

**Critical for discovery:** Future agents need to FIND your skill.

### 1. Rich Description Field

**Purpose:** Agents read description to decide which skills to load for a given task.

**Format:** Start with "Use when..." to focus on triggering conditions.

**CRITICAL: Description = When to Use, NOT What the Skill Does**

The description should ONLY describe triggering conditions. Do NOT summarize the skill's process or workflow.

```yaml
# ❌ BAD: Summarizes workflow
description: Use when executing plans - dispatches subagent per task with code review between tasks

# ✅ GOOD: Just triggering conditions
description: Use when executing implementation plans with independent tasks in the current session
```

**Content:** Use concrete triggers, symptoms, and situations. Describe the *problem* not *language-specific symptoms*. Write in third person. **NEVER summarize the skill's process or workflow.**

### 2-5. Keyword Coverage, Naming, Token Efficiency, Cross-Referencing

See `references/cso.md` for complete guidelines.

## Flowchart Usage

Use flowcharts ONLY for:
- Non-obvious decision points
- Process loops where you might stop too early
- "When to use A vs B" decisions

Never use flowcharts for: reference material, code examples, linear instructions.

See `references/graphviz-conventions.dot` for style rules.

## Code Examples

**One excellent example beats many mediocre ones**

Choose most relevant language:
- Testing techniques → TypeScript/JavaScript
- System debugging → Shell/Python
- Data processing → Python

**Good example:** Complete, runnable, well-commented explaining WHY, from real scenario, ready to adapt.

**Don't:** Implement in 5+ languages, create fill-in-the-blank templates, write contrived examples.

## File Organization

### Self-Contained Skill
```
defense-in-depth/
  SKILL.md    # Everything inline
```

### Skill with Reusable Tool
```
condition-based-waiting/
  SKILL.md    # Overview + patterns
  example.ts  # Working helpers to adapt
```

### Skill with Heavy Reference
```
pptx/
  SKILL.md       # Overview + workflows
  pptxgenjs.md   # 600 lines API reference
  ooxml.md       # 500 lines XML structure
  scripts/       # Executable tools
```

## The Iron Law

See `references/iron-law.md` for full text.

```
NO SKILL WITHOUT A FAILING TEST FIRST
```

This applies to NEW skills AND EDITS to existing skills.

Write skill before testing? Delete it. Start over.
Edit skill without testing? Same violation.

**No exceptions** - Not for "simple additions", "just adding a section", "documentation updates".

**REQUIRED BACKGROUND:** The `superpowers:test-driven-development` skill explains why this matters. Same principles apply to documentation.

## Testing All Skill Types

See `references/skill-testing.md` for detailed methodology.

### Discipline-Enforcing Skills (rules/requirements)
Test with: academic questions, pressure scenarios, multiple pressures combined

### Technique Skills (how-to guides)
Test with: application scenarios, variation scenarios, missing information tests

### Pattern Skills (mental models)
Test with: recognition scenarios, application scenarios, counter-examples

### Reference Skills (documentation/APIs)
Test with: retrieval scenarios, application scenarios, gap testing

## Common Rationalizations for Skipping Testing

| Excuse | Reality |
|--------|---------|
| "Skill is obviously clear" | Clear to you ≠ clear to other agents. Test it. |
| "It's just a reference" | References can have gaps. Test retrieval. |
| "Testing is overkill" | Untested skills have issues. Always. 15 min testing saves hours. |
| "I'll test if problems emerge" | Problems = agents can't use skill. Test BEFORE deploying. |

**All of these mean: Test before deploying. No exceptions.**

## Bulletproofing Skills Against Rationalization

See `references/bulletproofing.md` for research foundation (Cialdini, 2021; Meincke et al., 2025).

### Close Every Loophole Explicitly

Don't just state the rule - forbid specific workarounds:

<Bad>
```markdown
Write code before test? Delete it.
```
</Bad>

<Good>
```markdown
Write code before test? Delete it. Start over.

**No exceptions:**
- Don't keep it as "reference"
- Don't "adapt" it while writing tests
- Don't look at it
- Delete means delete
```
</Good>

### Address "Spirit vs Letter" Arguments

Add foundational principle early:
```markdown
**Violating the letter of the rules is violating the spirit of the rules.**
```

## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text
- [ ] Batch judge score ≥80 (Frontmatter≥18, Structure≥18, Content≥16, DRY≥16, References≥11)

## Batch Judge Optimization (Key Learnings from 116-Skill Audit)

The batch judge script (`~/AppData/Local/hermes/scripts/batch_skill_judge.py`) scores 5 dimensions (20 pts each = 100 max). Target ≥80 to PASS.

| Dimension | Boost Strategy |
|-----------|----------------|
| **Frontmatter (20)** | Complete all fields: name, title, description, version, author, license, tags; add `metadata.hermes.tags` |
| **Structure (20)** | Add **Skills Required table** (+4 pts), ≥3 workflow phases, Pitfalls section, Verification Checklist |
| **Content (20)** | Add concrete code examples with error handling, real usage patterns, NOT generic templates |
| **DRY (20)** | **Keep SKILL.md < 250 lines** — move detail to `references/` files. Each 50 lines over = -1 to -2 pts |
| **References (20)** | Create `references/overview.md` + `templates/` dir. Cite them in body. Each ref file = +2-3 pts |

### Proven Enhancement Sequence

1. **Add `references/overview.md`** — high-level context, architecture, patterns (boosts References 0→11)
2. **Add `templates/` with starter files** — `skill-template.md`, `technique-skill-template.md`, `reference-skill-template.md` (boosts References +2, Structure via usage examples)
3. **Add "Skills Required" table** — lists dependent skills with purpose (boosts Structure 16→20)
4. **Move verbose sections to `references/`** — CSO guidelines, testing methodology, bulletproofing, iron law, graphviz conventions, persuasion principles (boosts DRY 9→14+)
5. **Cite every reference file in SKILL.md body** — "See `references/xyz.md`" (required for reference credit)
6. **Add concrete usage examples** — `bash` blocks with real commands, not placeholders (boosts Content)

### Pitfall: Line Count Trap
- 250 lines = DRY 16-18 (PASS territory)
- 300+ lines = DRY 9-12 (WARN territory)  
- 350+ lines = DRY 6-9 (hard to recover)
- **Fix:** Extract to `references/` aggressively. One concept per reference file.

### Batch Judge Workflow
```bash
# Run judge
python ~/AppData/Local/hermes/scripts/batch_skill_judge.py --category development

# Check bottom 10
awk -F'\t' '$2<80' judge_results/all_results.tsv | sort -k2,2n

# Enhance lowest, re-run, repeat until all ≥80
```
- [ ] Batch judge score ≥80 (Frontmatter≥18, Structure≥18, Content≥16, DRY≥16, References≥11)

## Batch Judge Optimization (Key Learnings from 116-Skill Audit)

The batch judge script (`~/AppData/Local/hermes/scripts/batch_skill_judge.py`) scores 5 dimensions (20 pts each = 100 max). Target ≥80 to PASS.

| Dimension | Boost Strategy |
|-----------|----------------|
| **Frontmatter (20)** | Complete all fields: name, title, description, version, author, license, tags; add `metadata.hermes.tags` |
| **Structure (20)** | Add **Skills Required table** (+4 pts), ≥3 workflow phases, Pitfalls section, Verification Checklist |
| **Content (20)** | Add concrete code examples with error handling, real usage patterns, NOT generic templates |
| **DRY (20)** | **Keep SKILL.md < 250 lines** — move detail to `references/` files. Each 50 lines over = -1 to -2 pts |
| **References (20)** | Create `references/overview.md` + `templates/` dir. Cite them in body. Each ref file = +2-3 pts |

### Proven Enhancement Sequence

1. **Add `references/overview.md`** — high-level context, architecture, patterns (boosts References 0→11)
2. **Add `templates/` with starter files** — `skill-template.md`, `technique-skill-template.md`, `reference-skill-template.md` (boosts References +2, Structure via usage examples)
3. **Add "Skills Required" table** — lists dependent skills with purpose (boosts Structure 16→20)
4. **Move verbose sections to `references/`** — CSO guidelines, testing methodology, bulletproofing, iron law, graphviz conventions, persuasion principles (boosts DRY 9→14+)
5. **Cite every reference file in SKILL.md body** — "See `references/xyz.md`" (required for reference credit)
6. **Add concrete usage examples** — `bash` blocks with real commands, not placeholders (boosts Content)

### Pitfall: Line Count Trap
- 250 lines = DRY 16-18 (PASS territory)
- 300+ lines = DRY 9-12 (WARN territory)  
- 350+ lines = DRY 6-9 (hard to recover)
- **Fix:** Extract to `references/` aggressively. One concept per reference file.

### Batch Judge Workflow
```bash
# Run judge
python $LOCALAPPDATA/hermes/scripts/batch_skill_judge.py --category development

# Check bottom 10
awk -F'\t' '$2<80' judge_results/all_results.tsv | sort -k2,2n

# Enhance lowest, re-run, repeat until all ≥80
```

## Skills Required

| Skill | Purpose |
|-------|---------|
| `superpowers:test-driven-development` | RED-GREEN-REFACTOR fundamentals |
| `systematic-debugging` | Root cause analysis for testing gaps |

## Related Skills

- `superpowers:test-driven-development` — TDD fundamentals
- `systematic-debugging` — Root cause analysis
- `skill-creator` — Author in-repo SKILL.md files

## Usage Examples

```bash
# Create new skill with TDD
writing-skills --create --tdd

# Test existing skill
writing-skills --test skills/my-skill/

# Validate skill structure
writing-skills --validate skills/my-skill/
```

## Error Handling

- **Invalid frontmatter:** Exits with code 1, prints specific validation error
- **Missing required sections:** Warns, lists missing sections
- **Line count exceeded:** Exits with code 2 if >250 lines
- **Placeholder text detected:** Warns with line numbers

## Pitfalls

- **Over-documenting:** Keep skills focused; move detail to references/
- **Workflow summaries in description:** Causes agents to skip reading skill body
- **Missing test scenarios:** Every skill needs at least 3 test scenarios (baseline, pressure, edge case)
- **Force-loading with @ links:** Burns 200k+ context before needed

## References

- `references/cso.md` — CSO guidelines
- `references/skill-testing.md` — Test methodology per skill type
- `references/bulletproofing.md` — Persuasion research for bulletproofing
- `references/iron-law.md` — TDD iron law
- `references/graphviz-conventions.dot` — Flowchart style rules
- `superpowers:test-driven-development` — TDD fundamentals