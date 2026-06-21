# audit-skills-judge-fix — Dependency Context Catalog

> Generated: 2026-06-20T02:00:00Z | Source: `audit-skills-judge-fix.prompt.md`

## Purpose Resolution

- **Purpose slug:** `audit-skills-judge-fix`
- **Trigger:** `/audit-skills-judge-fix`
- **Source file:** `audit-skills-judge-fix.prompt.md`
- **Source reference:** `audit-skills-judge-fix.prompt.txt`

---

## Forward Dependencies (from this file)

### External Paths Referenced
| Path | Line | Context |
|------|------|---------|
| `C:\Users\Alexa\AppData\Local\hermes\skills\` | 44 | Target scope for skills audit |
| `C:\Users\Alexa\AppData\Local\hermes\scripts\` | 39, 215-219, 301-306, 389-402 | Python scripts location |
| `docs/local-skills.md` | 45, 84, 92, 100 | Phase 1 output |
| `docs/skill-inventory.json` | 84 | Phase 1 output |
| `docs/categorization-plan.md` | 46, 117 | Phase 2 output |
| `docs/dedupe-report.md` | 47, 169 | Phase 3 output |
| `docs/consolidation-report.md` | 50, 169 | Phase 3/6 output |
| `judge_results/all_results.tsv` | 48, 229 | Phase 4 output |
| `judge_results/summary.md` | 48, 237 | Phase 4 output |
| `judge_results/batch_NNNN_results.md` | 235 | Phase 4 output |
| `judge_results/needs_work_list.txt` | 238 | Phase 4 output |
| `judge_results/rewrite_list.txt` | 239 | Phase 4 output |
| `judge_results/remediation_report.md` | 49 | Phase 5 output |
| `judge_results/final_results.tsv` | 290 | Phase 5 output |
| `docs/final-verification.md` | 51, 349 | Phase 7 output |
| `SESSION_REPORT.md` | 362 | Phase 7 output |
| `skill_inventory.json` | 401 | Generated mapping |
| `skill_name_to_path.json` | 402, 227 | Generated mapping |

### Skill Dependencies (from frontmatter `skills:` and `dependencies:`)
| Skill | Type | Purpose |
|-------|------|---------|
| `using-superpowers` | workflow | Establishes workflow foundation |
| `user-communication-preferences` | config | Loads user prefs for execution style |
| `plans-and-specs` | planning | Creates implementation plan from goal |
| `skill-judge` | qa | Evaluates skill quality against criteria (v1.1.0) |
| `hermes-skills` | devops | Skills discovery, install, management |
| `skill-creator` | development | Author in-repo SKILL.md |
| `writing-skills` | development | Write clear skill prose and structure |

### Referenced Python Scripts (all in `C:\Users\Alexa\AppData\Local\hermes\scripts\`)
| Script | Purpose | Phase |
|--------|---------|-------|
| `batch_skill_judge.py` | Batch score all skills on 5 dimensions | 4, 7 |
| `batch_remediate.py` | Patch skills scoring 60-79 | 5 |
| `batch_remediate_42_59.py` | Patch skills scoring 42-59 | 5 |
| `batch_rewrite_worst.py` | Full rebuild of skills scoring <60 | 5 |
| `dedupe_skills.py` | Find duplicate SKILL.md files | 3 |
| `consolidate_skills.py` | Identify overlapping skills for merge | 3, 6 |
| `merge_skill.py` | Merge thin skill into umbrella skill | 3, 6 |
| `audit_prompts.py` | Audit prompt files for issues | 1 |

### Commands / Triggers
| Command | Line | Context |
|---------|------|---------|
| `/audit-skills-judge-fix` | 2 | This prompt's trigger |
| `/using-superpowers` | 12, 16 | Skill trigger |
| `/user-communication-preferences` | 13, 17 | Skill trigger |
| `/plans-and-specs` | 14, 18, 97 | Skill trigger |
| `/skill-judge` | 19, 73 | Skill trigger |
| `/hermes skills audit` | 90 | Hermes CLI command |
| `/hermes skills check` | 90 | Hermes CLI command |
| `/hermes skills update` | 90 | Hermes CLI command |
| `/hermes skills list` | 91, 120, 181, 356 | Hermes CLI command |

---

## Reverse Dependencies (files referencing this file/trigger)

| File | Line | Reference Type |
|------|------|----------------|
| `audit-skills-judge-fix.prompt.txt` | 1 | Source TXT version with skill triggers |
| `docs/test-providers-models-context.md` | 53 | Related prompt family entry |
| `docs/sync-hermes-copilot-codex-context.md` | 54 | Related prompt family entry |

---

## Related Prompt Family (same skill pattern)

| File | Shared Skills |
|------|---------------|
| `test-providers-models.prompt.md` | using-superpowers, user-communication-preferences, plans-and-specs |
| `sync-hermes-copilot-codex.prompt.md` | using-superpowers, user-communication-preferences, plans-and-specs |
| `agents-system-prompt-context-fix.prompt.md` | using-superpowers, user-communication-preferences, plans-and-specs |

---

## Target Environment Inventory

### Skills Directory (`C:\Users\Alexa\AppData\Local\hermes\skills\`)
- **Total skills:** 373 (post-dedup 2026-06-15)
- **Categories:** 16+ (autonomous-ai-agents, architecture, blockchain, creative, data-science, devops, development, github, mlops, productivity, qa, research, etc.)
- **Profile-specific:** code-architect has 368 local skill directories

### Scripts Directory (`C:\Users\Alexa\AppData\Local\hermes\scripts\`)
- **All 8 referenced scripts present** (see table above)
- Additional supporting scripts: `audit_prompts.py`, `apply_vscode_customizations.py`, etc.

---

## File Structure Summary

| File | Lines | Size | Frontmatter | Tables | Code Blocks |
|------|-------|------|-------------|--------|-------------|
| `audit-skills-judge-fix.prompt.md` | 424 | 20.3 KB | ✅ Valid YAML | 13 tables | 0 |
| `audit-skills-judge-fix.prompt.txt` | 2 | 804 B | ❌ No frontmatter | 0 | 0 |

---

## Audit Target Files (for batch processing)

1. `audit-skills-judge-fix.prompt.md` — Primary audit target
2. `audit-skills-judge-fix.prompt.txt` — Source reference, potential TXT→MD conversion