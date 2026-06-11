---
name: prompt-engineering
title: Prompt Engineering
description: "Use when designing, analyzing, or improving prompts for AI systems — including structure optimization, clarity enhancement, and pattern application."
---

# Prompt Engineering

## Description

Design, analyze, structure, and improve prompts for AI systems. Applies Stanford/Anthropic prompt patterns, enforces structural rules (nesting depth, instruction ratio, single source of truth), and produces prompts that are resilient across different AI backends.

## When to Use

- Designing new prompts from scratch
- Improving or refactoring existing prompts
- Applying CRISP, Stanford, or Anthropic prompt patterns
- Validating prompt structure (nesting, instruction ratio, constraint placement)
- Converting raw instructions into structured prompt specifications
- Auditing prompts for consistency and gap analysis

## When NOT to Use

- Executing prompts (use `acpx-executor` or direct delegation)
- Simple one-off questions that don't need structured prompting
- When the prompt already follows established patterns and works

## Goal

Produce well-structured, high-quality prompts that are clear, constrained, and optimized for AI consumption — with explicit rules, phase-based workflows, and verifiable outputs.

## Inputs

- Raw prompt text or instructions
- Target AI backend (Hermes, Copilot, OpenCode)
- Desired output format or schema
- Optional: existing prompt files to refactor

## Outputs

- Structured prompt with YAML frontmatter
- Validation report on prompt quality (structure, completeness, clarity)
- Before/with comparison when refactoring

## Rules

1. **Critical rules in first 15%** — Place MUST/CRITICAL/SAFETY constraints before line 15% of total prompt length
2. **Nesting depth <= 4** — No more than 4 levels of nested lists/sections
3. **Instruction ratio 40-50%** — 40-50% of prompt should be instructions, not context
4. **Single source of truth** — No rule repeated more than 2x
5. **3-tier prioritization** — Safety > Core Workflow > Optimization
6. **Explicit constraints over implied** — Every behavioral boundary is stated, not assumed
7. **Testable acceptance criteria** — Every output has verifiable quality gates

## Workflow

### Phase 1: Analyze

- Read the raw prompt or instructions
- Identify intent, target audience, expected outputs
- Extract implicit constraints and make them explicit
- Measure current prompt metrics (length, nesting, instruction ratio)

### Phase 2: Structure

- Apply the 9-section or 11-section template (per `enhance-markdown`)
- Place critical rules in first 15%
- Normalize heading hierarchy (H1 > H2 > H3)
- Add YAML frontmatter (title, trigger, description, tags, dependencies)

### Phase 3: Enhance

- Apply pattern libraries (CRISP, Stanford, Anthropic)
- Strengthen rules and constraints
- Add verification criteria
- Cross-link dependencies (context-map, skills, subagents)

### Phase 4: Validate

- Count constraint patterns before/after
- Verify no critical rules were removed
- Check instruction ratio (40-50%)
- Confirm nesting depth <= 4

## Skills Required

- `enhance-markdown` — Four-phase markdown auditing and enhancement
- `writing-plans` — Structuring plan documents
- `systematic-debugging` — Finding and fixing prompt issues
- `simplify` — Removing redundancy

## Best Practices

- Keep prompts DRY — no duplicated rules
- Use specific, measurable acceptance criteria
- Tag all dependencies explicitly in frontmatter
- Prefer `## Actions` over `## Actions Summary` (consistent naming)
- Every prompt should have `context-map` in dependencies when part of a pipeline
