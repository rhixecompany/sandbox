---
spec: 2026-09-11-four-goal-execution
title: Four-Goal Execution Specification
version: 1.0
date_created: 2026-09-11
owner: Alexa
status: Approved
plan: .hermes/plans/2026-09-11-four-goal-execution-master-plan.md
---

# Four-Goal Execution Specification

Acceptance criteria for the 4 sequential goals. Each criterion maps to plan tasks. All criteria must be verified with tool evidence before the goal is marked complete.

## G1 — Research artifacts + requirements.txt

| ID | Requirement | Acceptance criteria | Plan ref |
|----|-------------|---------------------|----------|
| G1-R1 | Keep existing reports | node-dependency.md, python-packages.md, technology-stacks.md unchanged | TASK-001 |
| G1-R2 | 11 topic skills | 1 SKILL.md per research topic dir; valid frontmatter; ≤250 lines; topic-accurate | TASK-002 |
| G1-R3 | 11 topic scripts | 1 executable script per skill; lives in scripts/; runs on Windows bash + Python 3.11/3.13 | TASK-003 |
| G1-R4 | 11 tests | 1 test per script; all pass (exit 0) | TASK-004 |
| G1-R5 | 1 research hook | hooks/ entry wiring research/ dir (e.g., stale-md or new-md gate) | TASK-005 |
| G1-R6 | requirements.txt updated | union(pip freeze, python-packages.md packages); `pip check` clean | TASK-007 |

## G2 — Skills dedupe + judge + fix

| ID | Requirement | Acceptance criteria | Plan ref |
|----|-------------|---------------------|----------|
| G2-R1 | initial snapshot | initial-skills.txt exists with real `hermes skills list` output + count | TASK-010 |
| G2-R2 | dedupe | near-exact dupes removed; canonical category copy enhanced; deletion log saved | TASK-012 |
| G2-R3 | judge | skill-judge run on remaining skills; scores recorded | TASK-013 |
| G2-R4 | fix to ≥90 | all judged skills ≥90 or residual documented w/ reason | TASK-014 |
| G2-R5 | count proof | count(initial-skills.txt) > count(updated-skills.txt) | TASK-015 |
| G2-R6 | full debug pass | every updated-skills.txt skill debugged/fixed/verified, ascending by list-modified | TASK-016 |
| G2-R7 | audit subgoal | `hermes skills audit && check && update` findings fixed | TASK-017 |

## G3 — Free-model benchmark

| ID | Requirement | Acceptance criteria | Plan ref |
|----|-------------|---------------------|----------|
| G3-R1 | inventory | free/non-premium model list per provider (opencode-zen, openrouter, nous) recorded | TASK-020/021 |
| G3-R2 | benchmark | per model: latency, accuracy, context, capabilities, tools, vision probed via hermes chat | TASK-022 |
| G3-R3 | observed-only report | every row = observed outcome (success/timeout/error); NO fabricated completions | TASK-023/024 |

## G4 — Profile asset sync

| ID | Requirement | Acceptance criteria | Plan ref |
|----|-------------|---------------------|----------|
| G4-R1 | inventory | 15 profile subdirs inventoried; `profiles/skills` anomaly classified | TASK-030 |
| G4-R2 | delete | skills/hooks/plugins/scripts + config.yaml + .env removed from every profile subdir | TASK-031 |
| G4-R3 | copy | same assets copied from root hermes dir into every profile subdir | TASK-032 |
| G4-R4 | parity | per-profile tree diff vs root empty; config.yaml parses as YAML | TASK-033 |

## Global rules

- **Verification**: every acceptance criterion ends with a tool call (ls, diff, count, test run, exit code).
- **Sequencing**: G1 gate → G2 gate → G3 gate → G4 gate. No phase overlap.
- **Secrets**: .env/config.yaml copied by file operation; contents never echoed to output.