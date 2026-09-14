---
name: agent-core-architecture
title: "Agent Core File Architecture — SOUL.md / USER.md / MEMORY.md"
description: "Use when structuring, auditing, or evolving core agent identity files (SOUL.md, USER.md, MEMORY.md) against reference architecture patterns. Covers role separation, incremental enhancement from reference docs, and verification."
version: 1.0.0
author: "Hermes Agent"
tags: [hermes, profiles, soul, user, memory, architecture]
---
# Agent Core File Architecture

## Overview

Automated reasoning and workflow tool for `agent-core-architecture`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## When to Use

- Restructuring SOUL.md, USER.md, or MEMORY.md into canonical format
- Responding to reference architecture documents that describe core file structure
- Auditing existing files for structural completeness
- Creating new profile from scratch with correct architecture
- Aligning profile files after multi-round iterative enhancement

## When NOT to Use

- Generating a single SOUL.md template from profile.yaml → use `devops/soul-enhancer` instead
- General profile maintenance / drift detection → use `devops/profile-maintenance`
- CLI commands for profile lifecycle → use `devops/hermes-profiles`

## Role Separation Principle

Each file owns exactly one concern — no overlap:

| File | Owns | Content Includes |
|------|------|------------------|
| **SOUL.md** | Behavioral invariants | Persona, cognitive style, execution frameworks, architectural invariants, standing rules, memory hierarchy |
| **USER.md** | Operator preferences | Identity, communication, environment stack, planning style, prompting prefs, skill utilization, automation hooks, execution preferences |
| **MEMORY.md** | Learned heuristics | Plan failures, prompt insights, skill cache, hook state — organized by category with dated entries |

## Canonical Section Map

### SOUL.md (6 top-level sections)

```
## Persona                    — 4 bullet-point rules (pragmatist, engineer, honest, direct+opinionated)
## Cognitive Style            — 5 rules (deconstruct, trace, one-variable, surface assumptions, resourceful)
## Execution Frameworks
### Plans                    — 6 rules (linear, breakdown, checkpoint, fallback, state, checkpointing)
### Prompts                  — 8 rules (inheritance, persona lock, constraint, context prio, output typing, no hypothesizing, cot, intent formatting)
### Skills                   — 7 rules (discovery, arg validation, silent, rate limit, credential isolation, combining, mock fallback)
### Hooks                    — 7 rules (pre_flight, pre_exec, on_error, post_process, post_exec, on_user_interrupt, on_idle)
## Architectural Invariants  — 4 subsections × 3 rules each
### Plan Discipline          — validate first, map tool to phase, pause on edge case
### Prompt Construction      — no injection, no reorder, no self-modify
### Skill Execution Bounds   — immutable, 2-error fallback, no precedence bypass
### Hook Lifecycle Guardrails — lightweight, hard stop on failure, append-only logs
## Standing Rules            — 13 numbered operational protocols
## Memory Hierarchy          — Table: SOUL|USER|MEMORY|session_search
```

### USER.md (10 sections)

```
## Identity                  — Name, workspace, profile
## Communication             — Bulleted, lead with result, skip overviews
## Environment Stack         — OS, runtime, tooling, execution mode
## Model                     — Active model name
## Planning Style            — Milestone-based, incremental, approval gates
## Prompting & Gen Prefs     — Direct, light wit, JSDoc Why, MCP+skills
## Custom Skill Utilization  — SKILL.md format, preferred stack, sparse comments
## Automation Hooks          — Ruff pre-commit, test post-exec, .env.local priority
## Execution Preferences     — DRY rules, clarify first, delegate parallel
## Canonical Store           — MEMORY.md as rule store
```

### MEMORY.md (4 categories + 8 sub-sections)

```
|Archival criteria          — Record verified-stable facts only
|Anti-bloat rule            — Purge temporal chatter, 7-day test

## Plan Failures & Adaptations
### Active Milestones        — Track refactor/deployment progress
### Historical Decisions     — Log architectural choices
    (bullet entries)

## Prompt Tuning Insights
### Terminology Glossary      — Domain acronym mappings
### User Feedback Log         — Date-stamped preference notes
    (bullet entries)

## Skill & Tool Cache
### Known Gotchas             — Failure patterns with mitigations
### Function Signatures       — API/param migration tracking
    (bullet entries)

## Active Hook States
### Automated Routines        — Recurring hook triggers
### Failure Edge Cases        — Hook failure thresholds
    (bullet entries)
```

## Workflow: Incorporate Reference Architecture Documents

When the user provides a reference document (blog post, guide, framework docs) describing SOUL.md/USER.md/MEMORY.md structure:

### Phase 1: Map reference to current files

1. Read the reference document — identify the section categories proposed (e.g., "Plan Discipline", "Prompt Construction")
2. Read current SOUL.md, USER.md, MEMORY.md
3. Build a gap matrix: which proposed rules are already covered? Which are new?
4. Note any contradictions (e.g., reference says "neutral tone" but current says "sharp opinions")

### Phase 2: Targeted incorporation

1. **Add new rules** to existing sections — don't restructure unless the reference proposes a fundamentally different section map
2. **Replace outdated rules** when the reference has a better version of the same concept
3. **Add new sections** if the reference proposes structural elements not present (e.g., Architectural Invariants was added as a new top-level section between Execution Frameworks and Standing Rules)
4. Keep the existing structure anchor points — each round builds on the last

### Phase 3: Verify role separation

After the update, verify no DRY violations:
- USER.md should NOT contain SOUL.md rules (execution frameworks, architectural invariants)
- MEMORY.md should NOT contain USER.md preferences
- SOUL.md should NOT contain user-specific preferences

### Phase 4: Multi-round iteration

Reference documents may arrive in sequence. Each round:
1. Only add what's genuinely new this round
2. Don't re-add rules already incorporated from previous rounds
3. If the reference renames existing concepts, prefer the newer canonical name
4. Maintain the standing section count — track it to prevent bloat

## Verification

```bash
# SOUL.md: 5 top-level sections (Persona, Cognitive Style, Execution Frameworks, Architectural Invariants, Standing Rules)
grep -c "^## " SOUL.md    # Expect 5 (Memory Hierarchy doesn't count as separate top-level section for structure check)

# Execution Frameworks: 4 sub-sections
grep -c "^### " SOUL.md   # Expect 8 (4 Execution Frameworks + 4 Architectural Invariants)

# USER.md: 10 sections
grep -c "^## " USER.md    # Expect 10

# MEMORY.md: 4 sections + 8 sub-sections
grep -c "^## " MEMORY.md  # Expect 4
grep -c "^### " MEMORY.md # Expect 8

# No DRY violations
grep -ci "architectural\|cognitive\|standing rule" USER.md  # Should be 0
```

## Pitfalls

| Pitfall | Mitigation |
|---------|------------|
| Reference doc proposes flat rule-list instead of structured sections | Structure into categorized sections — flat lists scale poorly across sessions |
| Multiple reference rounds contradict each other | The latest round's naming wins; older references should be treated as superseded |
| Reference doc written for different framework (e.g., OpenClaw vs Hermes) | Map concepts to equivalent Hermes structures; don't copy verbatim if names differ |
| Section count creeps up every round | Track target: SOUL.md=5 top-level, USER.md=10, MEMORY.md=4. Prune duplicate rules before adding new ones |
| DRY violation creeps in | After each round, grep USER.md for SOUL.md rule keywords; grep MEMORY.md for USER.md preference keywords |

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] "Agent Core File Architecture — SOUL.md / USER.md / MEMORY.md" operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
