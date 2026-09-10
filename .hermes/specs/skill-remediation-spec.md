---
name: skill-remediation-spec
title: "Full Skill Library Remediation — Specification (Phases S1-S7)"
description: |
  Detailed specification for full skill library remediation to 99+ on all judge skills.
  Covers 1,278 active skills across 37 categories.
version: 1.0.0
author: Alexa
license: MIT
tags: [spec, skills, remediation, audit, judge, score-99]
status: approved
linked_plan: master-skill-library-remediation
---

# Full Skill Library Remediation — Specification (Phases S1-S7)

## Scope

| Metric | Value |
|--------|-------|
| Active skills | 1,278 |
| Archived skills | 32 (to be removed) |
| Categories | 37 |
| Root-level skills | 542 |
| Categorized skills | 736 |
| Target judge skills | 7 (skill-judge, plans-judge, specs-judge, prompts-judge, hooks-judge, plugins-judge, scripts-judge) |
| Target score | ≥99 on all |

---

## Phase S1: Archive Cleanup + Dedup

### Requirements
- Remove `.archive/` directory (32 skills)
- Remove `.restore-backups.DISABLED/` if exists
- Identify flat-root vs categorized duplicates
- Remove non-canonical flat copies (keep categorized versions under `<category>/<skill>/`)
- Verify no duplicate skill names across paths

### Acceptance Criteria
| Check | Expected |
|-------|----------|
| .archive removed | Directory gone |
| .restore-backups.DISABLED removed | Directory gone |
| Duplicate skill names | 0 duplicates |
| Canonical paths preserved | All categorized skills intact |
| Skill count after | ~1,200-1,250 |

### Dedup Rules
1. **Canonical location**: `<category>/<skill>/SKILL.md` (e.g., `devops/hermes-skills/`)
2. **Non-canonical**: `<skill>/SKILL.md` at root (e.g., `hermes-skills/`)
3. **Keep**: Canonical (usually richer content, proper category)
4. **Remove**: Non-canonical flat copy
5. **Exception**: If flat has richer content, migrate content then remove flat

---

## Phase S2: Baseline Judge All Skills

### Requirements
- Run `batch_skill_judge.py` on all active skills
- Score 5 dimensions × 20 = 100 max per skill
- Capture baseline distribution
- Generate artifacts: `judge_results/summary.md`, `judge_results/all_results.tsv`, `judge_results/batch_*.md`

### Acceptance Criteria
| Check | Expected |
|-------|----------|
| All skills scored | 100% |
| Distribution captured | PASS/WARN/FAIL counts |
| TSV output | Complete, parseable |
| Top 20 worst identified | List with scores |

### Judge Dimensions (skill-judge)

| Dimension | Weight | Criteria |
|-----------|--------|----------|
| Frontmatter | 20 | name, title, description, version, author, license, tags |
| Structure | 20 | Skills Required table, ≥3 phases, Pitfalls, Verification Checklist, refs exist |
| Content | 20 | Resumability, error handling, platform detection, examples, no placeholders |
| DRY | 20 | No duplicate content, <250 lines, cross-ref consistency |
| References | 20 | 3 ref types, substantive, cited in body, no orphans |

---

## Phase S3: Batch Remediation (Structure)

### Requirements
Run structural fix scripts in sequence:
1. `batch_remediate.py` — Add missing frontmatter, pitfalls, verification checklists
2. `fix_yaml_frontmatter.py` — Fix YAML formatting (inline vs list tags)
3. `patch_fail_structure.py` — Add workflow phases, Skills Required table
4. `patch_all_fail_sections.py` — Inject all 7 critical sections
5. `boost_near_pass_refs.py` — Create domain-specific reference files

### Acceptance Criteria
| Check | Expected |
|-------|----------|
| FAIL skills | 0 |
| Average score | ≥72 |
| WARN skills | Majority |
| PASS skills | Growing |

### Script Details

#### batch_remediate.py
- Adds: `version`, `author`, `license`, `tags` if missing
- Adds: `Pitfalls` section if missing
- Adds: `Verification Checklist` if missing
- Target: FAIL → WARN conversion

#### fix_yaml_frontmatter.py
- Normalizes `tags:` format (accepts both inline `[a,b]` and list `- a\n  - b`)
- Fixes collapsed frontmatter keys
- Fixes CRLF issues

#### patch_fail_structure.py
- Adds `When to Use` / `When NOT to Use` sections
- Adds `Skills Required` table
- Adds phased `Workflow` (≥3 phases)
- Target: Structure dimension 10→16+

#### patch_all_fail_sections.py
Injects all 7 critical sections:
1. `## When to Use`
2. `## When NOT to Use`
3. `## Skills Required` table
4. `## Workflow` with ≥3 phases
5. `## Pitfalls`
6. `## Verification Checklist`
7. `## References` with file pointers

#### boost_near_pass_refs.py
- Creates `references/overview.md` for skills with refs <15
- Domain-specific content (docker, git, api, web, etc.)
- Target: Refs dimension 10→15+

---

## Phase S4: Deep Remediation (Content Depth)

### Requirements
For skills scoring 70-79 after S3:
1. Add platform detection blocks with `get_platform()` function
2. Add error handling blocks with code examples, retry logic, exception tables
3. Create `templates/` and `scripts/` with real runnable content
4. Add explicit reference citations in SKILL.md body (inline + References section)
5. Add ≥3 fenced code blocks per skill
6. Ensure all reference files substantive (>200 chars)

### Acceptance Criteria
| Check | Expected |
|-------|----------|
| Average score | ≥80 |
| Near-PASS (75-79) | ≥85 |
| Platform detection | Present in all |
| Error handling | Present in all |
| 3 ref types | All skills |
| Code blocks | ≥3 per skill |
| Body citations | All reference files cited |

### Proven Technique (60→85+)
From 2026-07-10 remediation run:
1. **Platform detection block** (+4 Structure) — OS-specific guidance function
2. **Error handling block** (+4 Content) — Error codes, retry, exceptions
3. **Templates/scripts dirs** (+10 References) — 3 real reference types
4. **Body citations** (+5 DRY +5 Refs) — Inline + section references
5. **≥3 code blocks** (+4 Content) — Even simple snippets count

---

## Phase S5: Targeted 99+ Push

### Requirements
- Run `skill-judge --threshold 90` on all skills
- For each skill <90: apply targeted fixes per judge feedback
- Add comprehensive examples, edge cases, integration patterns
- Ensure all reference files >200 chars with real content
- Verify all skills ≥90 on skill-judge
- Run all 6 other judges on relevant artifacts

### Acceptance Criteria
| Check | Expected |
|-------|----------|
| All skills skill-judge | ≥90 |
| plans-judge on plans | ≥99 |
| specs-judge on specs | ≥99 |
| prompts-judge on prompts | ≥99 |
| hooks-judge on hooks | ≥99 |
| plugins-judge on plugins | ≥99 |
| scripts-judge on scripts | ≥99 |

### Per-Judge Target Criteria

#### plans-judge (≥99)
- Plan frontmatter complete
- Phases with gates and status
- Specs linked to tasks
- Progress tracking
- Completion verification

#### specs-judge (≥99)
- Requirements traceable to plan
- Acceptance criteria measurable
- Dependencies documented
- Verification methods defined

#### prompts-judge (≥99)
- Frontmatter complete (name, description, version, author, model, skills)
- No placeholder text
- All skills referenced exist
- Structured sections

#### hooks-judge (≥99)
- Hook manifest valid
- Events mapped correctly
- Scripts executable
- No duplicate hooks

#### plugins-judge (≥99)
- Plugin manifest valid
- Tools registered
- Version specified
- Compatibility declared

#### scripts-judge (≥99)
- Shebang present
- Error handling
- Documentation
- Tests exist

---

## Phase S6: All 7 Judge Skills Verification

### Requirements
Run each judge independently and verify ≥99:

```bash
# Skill judge (all skills)
python scripts/batch_skill_judge.py --threshold 99

# Plans judge
hermes judge plans --threshold 99

# Specs judge
hermes judge specs --threshold 99

# Prompts judge
hermes judge prompts --threshold 99

# Hooks judge
hermes judge hooks --threshold 99

# Plugins judge
hermes judge plugins --threshold 99

# Scripts judge
hermes judge scripts --threshold 99
```

### Acceptance Criteria
| Judge | Score ≥ 99? |
|-------|-------------|
| skill-judge | Yes |
| plans-judge | Yes |
| specs-judge | Yes |
| prompts-judge | Yes |
| hooks-judge | Yes |
| plugins-judge | Yes |
| scripts-judge | Yes |

---

## Phase S7: Final Verification + Git Commit

### Requirements
- Run `test_run_all_goals.py` — all tests pass
- Run `verify_run_all_goals.py` — all 5 checks pass
- Commit all changes with conventional messages
- Push to `clean-development`, `development`, `production`
- Tag release
- Generate final `SESSION_REPORT.md`

### Acceptance Criteria
| Check | Expected |
|-------|----------|
| test_run_all_goals.py | All PASS |
| verify_run_all_goals.py | 5/5 PASS |
| Git commit | Clean, conventional |
| 3 branches pushed | Yes |
| Tag | Created |
| SESSION_REPORT.md | Complete |

---

## Scripts Required

| Script | Purpose | Phase |
|--------|---------|-------|
| `scripts/batch_skill_judge.py` | Parallel skill scoring | S2, S3, S4, S5, S6 |
| `scripts/batch_remediate.py` | Structural frontmatter fixes | S3 |
| `scripts/fix_yaml_frontmatter.py` | YAML normalization | S3 |
| `scripts/patch_fail_structure.py` | Workflow phases injection | S3 |
| `scripts/patch_all_fail_sections.py` | 7 critical sections | S3 |
| `scripts/boost_near_pass_refs.py` | Domain reference files | S3 |
| `scripts/deep_remediate.py` | Content depth (platform, errors, templates) | S4 |
| `scripts/push_to_99.py` | Targeted 90→99 fixes | S5 |
| `scripts/verify_all_judges.py` | Run all 7 judges | S6, 11 |
| `scripts/verify_phaseS1.py` through `verify_phaseS7.py` | Phase verification | S1-S7 |

---

## Cross-Phase Dependencies

| Phase | Depends On |
|-------|------------|
| S2 | S1 (clean inventory) |
| S3 | S2 (baseline scores) |
| S4 | S3 (structure fixed) |
| S5 | S4 (content depth) |
| S6 | S5 (skills ≥90) |
| S7 | S6 (all judges ≥99) |
| S7 | 11 (run-all-goals judges ≥99) |

---

## Verification Artifacts

All artifacts saved to:
- `judge_results/` — batch scores, summaries, TSV
- `docs/skill-audit-report.md` — audit output
- `docs/skills-audit.md` — hermes skills audit
- `docs/dedupe-report.md` — dedup results
- `docs/skills-modified.md` — modified skills list
- `docs/local-skills.md` — final skill inventory
- `SESSION_REPORT.md` — session summary

---

## Rollback Plan

If any phase causes regression:
1. `git checkout HEAD -- <affected-paths>`
2. Re-run verification for that phase
3. Document issue in SESSION_REPORT.md
4. Apply targeted fix instead of batch script

---

## Quality Gates

| Gate | Command | Threshold |
|------|---------|-----------|
| S1 Dedup | `grep -rh "^name:" skills/ | sort | uniq -d` | 0 duplicates |
| S2 Baseline | `batch_skill_judge.py` | All scored |
| S3 Structure | `batch_skill_judge.py --threshold 70` | 0 FAIL |
| S4 Content | `batch_skill_judge.py --threshold 80` | Avg ≥80 |
| S5 90+ | `batch_skill_judge.py --threshold 90` | All ≥90 |
| S6 All Judges | `verify_all_judges.py` | All ≥99 |
| S7 Final | `verify_run_all_goals.py` | 5/5 PASS |