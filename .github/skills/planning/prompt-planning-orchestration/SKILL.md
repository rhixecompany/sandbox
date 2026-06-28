---
name: prompt-planning-orchestration
title: "Prompt Planning Orchestration"
description: "Design, specify, and execute complex prompt workflows with safety-first gates, comprehensive documentation, and profile-optimized phase orchestration. Don't stop until complete."
version: 1.1.0
author: Alexa
license: MIT
tags: [imported]
metadata:
  hermes:
    tags: [imported]
---
# Prompt Planning Orchestration

## Goal
Design, specify, and execute complex prompt workflows with safety-first gates, comprehensive documentation, and profile-optimized phase orchestration. Deliver 4 primary files: plan, code samples, implementation guide, supporting docs.

## Subgoals
1. **Verify** — Confirm prerequisites, templates, scope
2. **Plan** — Create comprehensive workflow specification
3. **Code** — Provide production-ready implementation samples
4. **Guide** — Create step-by-step execution guide with scripts
5. **Support** — Create navigation docs, summaries, indexes

## Personas
| Persona | When to Use |
|---------|-------------|
| **Architect** | Full workflow design with safety gates |
| **Developer** | Code samples and implementation |
| **Tech Writer** | Documentation and guides |
| **Operator** | Execution and troubleshooting |

## Personality & Tone
- **Tone**: Thorough, safety-conscious, production-ready
- **Style**: Auto-continue through all phases; never stop between phases for approval
- **Avoid**: Single-file deliverables, skipping verification, weak safety specs, hand-wavy plans
- **Encourage**: Complete delivery (plan + code + guide + supporting), concrete examples, ready-to-run scripts

## Profile Selection
| Task Type | Recommended Profile |
|-----------|---------------------|
| Full orchestration | `exec-assistant` + `code-architect` |
| Plan only | `exec-assistant` |
| Code samples | `code-architect` |
| Guide/tutorial | `patient-tutor` |
| Safety review | `research-analyst` |
| General purpose | `default` |

### Multi-Agent Profile Assignment
| Phase | Best Profile | Why |
|-------|--------------|-----|
| Verification | `research-analyst` | Inventory, data integrity |
| Plan | `exec-assistant` | Specification, safety gates |
| Code | `code-architect` | Implementation, type hints |
| Guide | `patient-tutor` | Step-by-step clarity |

## When to Use
- User requests `/prompt-*` workflow design or planning
- User asks to design a multi-stage prompt system
- User wants specifications with code samples AND implementation guide
- User emphasizes "don't stop until complete" + "use best profiles"
- Request includes safety/validation/constraint preservation

**Triggers**: `/prompt-planning`, `/orchestrate-prompt-workflow`, `/design-prompt-system`

## When NOT to Use
- Simple single-document planning (use `plans-and-specs` instead)
- Code-only requests (use `code-architect` profile directly)
- When user only wants a plan, not full deliverables

## Skills Required
| Skill | Purpose |
|-------|---------|
| `brainstorming` | Explore workflow approaches before planning |
| `plans-and-specs` | Structure the comprehensive plan |
| `executing-plans` | Execute the workflow after design |
| `verification-before-completion` | Cross-reference plan vs execution |
| `systematic-debugging` | Debug workflow issues |

## Workflow

### Phase 0: Verification
**Profile**: `research-analyst`
- Verify all prerequisites exist (templates, input files, directories)
- Create inventory/census of targets
- Report blocking items or missing dependencies
- Lock in scope before proceeding

### Phase 1: Comprehensive Plan
**Profile**: `exec-assistant`
- Executive summary (objectives, scope, constraints)
- Detailed phase-by-phase specs
- Safety/validation architecture (gates, constraints, rollback)
- Timeline and resource requirements
- Risk mitigation (5+ identified risks)
- **Deliverable**: 800-900 line markdown specification

### Phase 2: Code Samples
**Profile**: `code-architect`
- One class/module per phase
- Full type hints (Python 3.11+)
- Error handling and validation
- Data structures and serialization
- **Deliverable**: 700-800 line `.py` file

### Phase 3: Implementation Guide
**Profile**: `patient-tutor`
- Quick start (5-minute entry point)
- Step-by-step tutorial for each phase
- Shell scripts for automation
- Pre/during/post execution checklists
- Troubleshooting (8+ issue/solution pairs)
- **Deliverable**: 1,200-1,500 line markdown guide

### Phase 4: Support Docs
- Execution summary
- Index/navigation
- Decision trees

## Deliverable Shape
See `references/deliverable-shapes.md` for detailed output structure, quality checkpoints, and acceptance criteria.

## Safety-First Pattern
For each phase involving transformation:
1. **Pre-transformation audit** — Extract critical constraints
2. **Transformation rules** — What is allowed, what is not
3. **Post-transformation verification** — Constraints still present
4. **Violation handling** — Automatic FAIL, logging, rollback trigger

## Pitfalls
- **Single-file deliverable**: Always deliver 4+ files (plan + code + guide + supporting)
- **Skipping verification**: Always verify prerequisites first
- **Weak safety spec**: Define explicit multi-gate pattern with constraint extraction
- **Code without error handling**: Full type hints, validation, try/except
- **Guide without scripts**: Provide ready-to-run shell scripts for every major step
- **Stopping between phases**: Auto-continue; only stop for blocking errors
- **Non-standard file extensions**: When planning batch prompt operations, check for both `.prompt.md` and `.prompts.md` extensions. Run `ls *.prompt*.md 2>/dev/null` during Phase 0 to discover all targets. Files with plural `.prompts.md` are easily missed and silently excluded from batch operations.

## Auto-Continue Rule
- Do NOT stop between phases asking for approval
- Mark each phase COMPLETE → move to next automatically
- Only stop for blocking errors
- Report progress via todo list updates

## Verification Checklist
- [ ] All prerequisites verified (Phase 0)
- [ ] Comprehensive plan delivered with safety gates (Phase 1)
- [ ] Code samples delivered with full type hints (Phase 2)
- [ ] Implementation guide delivered with scripts (Phase 3)
- [ ] Supporting docs created (Phase 4)
- [ ] All deliverables meet acceptance criteria
- [ ] No phases were skipped
