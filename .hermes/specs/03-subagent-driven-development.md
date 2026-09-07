---
name: 03-subagent-driven-development
title: Subagent-Driven Development Skill Enhancement
status: in_progress
owner: Alexa
version: 1.0.0
---

## Goal

Enhance the existing `subagent-driven-development` skill with explicit context-budget-discipline integration, gates-taxonomy integration, TDD enforcement, and a skill-judge target score of ≥ 90. Ensure all references are loadable and the skill passes skill-judge verification.

## Requirements

### Functional
- [ ] SKILL.md enhanced with explicit context-budget-discipline integration (load reference when context degrades)
- [ ] SKILL.md enhanced with explicit gates-taxonomy integration (Pre-flight, Revision, Escalation, Abort gates)
- [ ] TDD enforcement in implementer context (test first, verify fail, implement, verify pass)
- [ ] Skill-judge target: ≥ 90 score
- [ ] Verification checklist updated
- [ ] Cross-references to related skills (plan, requesting-code-review, test-driven-development, prompt-library-maintenance)
- [ ] References verified and loadable: `references/context-budget-discipline.md` and `references/gates-taxonomy.md`
- [ ] Skill passes `skill-judge` with score ≥ 90
- [ ] Skill loads without error via `skill_view`

### Non-Functional
- [ ] DRY: No duplication with other skills (reference instead)
- [ ] Line count < 250 (move detail to references)
- [ ] All references cited in SKILL.md body
- [ ] Frontmatter complete (name, title, description, version, author, license, tags)

## Acceptance Criteria

| Check | Command | Expected |
|-------|---------|----------|
| Skill loads | `skill_view subagent-driven-development` | Returns full content, no error |
| References load | `skill_view subagent-driven-development references/context-budget-discipline.md` | Returns content |
| References load | `skill_view subagent-driven-development references/gates-taxonomy.md` | Returns content |
| Skill judge | `skill-judge subagent-driven-development` | Score ≥ 90 |
| Frontmatter valid | Check SKILL.md | All required fields present |
| Line count | `wc -l SKILL.md` | < 250 lines |
| TDD mentioned | grep -i "tdd\|test.driven" SKILL.md | Found |
| Gates mentioned | grep -i "gate\|pre.flight\|revision\|escalation\|abort" SKILL.md | Found |

## Non-Functional Requirements

DRY compliance: no duplication with other skills — use references instead. SKILL.md must be under 250 lines with detailed content moved to reference files. All references must be cited in the SKILL.md body. Frontmatter must include name, title, description, version, author, license, and tags fields.

## Verification

```bash
# 1. Load and verify skill
skill_view subagent-driven-development
# Expected: Returns full content, no error

# 2. Load and verify references
skill_view subagent-driven-development references/context-budget-discipline.md
skill_view subagent-driven-development references/gates-taxonomy.md
# Expected: Both return content

# 3. Run skill judge
# (Use skill-judge skill or equivalent evaluation)
# Expected: Score ≥ 90

# 4. Check line count
wc -l ~/AppData/Local/hermes/skills/software-development/subagent-driven-development/SKILL.md
# Expected: < 250 lines

# 5. Verify frontmatter
head -30 ~/AppData/Local/hermes/skills/software-development/subagent-driven-development/SKILL.md
# Expected: All required frontmatter fields present
```

## Linked Specs
- 03-subagent-driven-development.md

## Linked Plan
- ../skill-implementation-master-plan.md
- ../2026-08-15_202608_four-agent-prompt-audit-plan.md
