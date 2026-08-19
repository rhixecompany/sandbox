# SPEC: subagent-driven-development Skill Enhancement

**Workstream:** 03-subagent-driven-development
**Priority:** P1 - Core Ask
**Dependencies:** 02-mcp-server-suite (MCP tools for validation)
**Profile:** code-architect

---

## Problem Statement

The existing `subagent-driven-development` skill at `skills/software-development/subagent-driven-development/` needs enhancement per user request: "implement each skills fully using best practices and dry principals". Current skill has good foundation but lacks:
- context-budget-discipline reference (4-tier model)
- gates-taxonomy reference (4 canonical gate types)
- Explicit integration with test-driven-development
- Skill-judge verification target (≥ 90)
- Enhanced red flags and pitfalls

## Current Skill Analysis

**Location:** `~/AppData/Local/hermes/skills/software-development/subagent-driven-development/SKILL.md`
**References:** `references/context-budget-discipline.md`, `references/gates-taxonomy.md` (exist but need verification)
**Structure:** SKILL.md + 2 reference files

## Requirements

### Functional
- [ ] SKILL.md enhanced with:
  - Explicit context-budget-discipline integration (load reference when context degrades)
  - Explicit gates-taxonomy integration (Pre-flight, Revision, Escalation, Abort gates)
  - TDD enforcement in implementer context (test first, verify fail, implement, verify pass)
  - Skill-judge target: ≥ 90 score
  - Verification checklist updated
  - Cross-references to related skills (plan, requesting-code-review, test-driven-development, prompt-library-maintenance)
- [ ] References verified and loadable:
  - `references/context-budget-discipline.md` — PEAK/GOOD/DEGRADING/POOR tiers, read-depth rules
  - `references/gates-taxonomy.md` — Pre-flight, Revision, Escalation, Abort with behavior/recovery
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

## Implementation Approach

```bash
# 1. Read current skill
skill_view subagent-driven-development

# 2. Read references
skill_view subagent-driven-development references/context-budget-discipline.md
skill_view subagent-driven-development references/gates-taxonomy.md

# 3. Enhance SKILL.md with:
#    - Explicit reference loading instructions in workflow
#    - Context budget checks before large subagent batches
#    - Gate vocabulary in verification checkpoints
#    - TDD enforcement in implementer context template
#    - Skill-judge target in verification checklist

# 4. Verify
skill-judge subagent-driven-development
```

## Enhanced Workflow Additions

### Phase 0: Context Budget Check (Before Dispatch)
```python
# Load context-budget-discipline reference
# Check current tier: PEAK/GOOD/DEGRADING/POOR
# If DEGRADING/POOR: reduce batch size, increase verification frequency
# Read-depth rules scale with context window
```

### Phase 1.5: Pre-flight Gate (Per Task)
```python
# Before dispatching implementer:
# - Verify task spec complete
# - Verify dependencies met
# - Verify context budget sufficient
# - If gate fails: ABORT or ESCALATE per gates-taxonomy
```

### Phase 2.5: Revision Gate (After Spec Review)
```python
# After spec compliance review:
# - If PASS: proceed to quality review
# - If gaps: REVISE (loop back to implementer)
# - Revision gate tracks iteration count, max 3
```

### Phase 3.5: Escalation Gate (After Quality Review)
```python
# After quality review:
# - If APPROVED: mark complete
# - If REQUEST_CHANGES: ESCALATE to implementer with specific issues
# - If CRITICAL: ABORT task, require human intervention
```

## Verification Steps

```bash
# 1. Load and verify skill
skill_view subagent-driven-development

# 2. Load and verify references
skill_view subagent-driven-development references/context-budget-discipline.md
skill_view subagent-driven-development references/gates-taxonomy.md

# 3. Run skill judge
# (Use skill-judge skill or equivalent evaluation)

# 4. Check line count
wc -l ~/AppData/Local/hermes/skills/software-development/subagent-driven-development/SKILL.md

# 5. Verify frontmatter
head -30 ~/AppData/Local/hermes/skills/software-development/subagent-driven-development/SKILL.md
```

## Risks

- **Reference files may be thin** — Verify they have substantive content (≥ 50 lines each)
- **Skill-judge criteria may not match** — Ensure skill meets all judge criteria
- **Cross-skill references** — Don't duplicate content from plan, requesting-code-review, test-driven-development

## References

- `skills/software-development/subagent-driven-development/references/context-budget-discipline.md`
- `skills/software-development/subagent-driven-development/references/gates-taxonomy.md`
- `skills/software-development/plan/SKILL.md`
- `skills/software-development/requesting-code-review/SKILL.md`
- `skills/software-development/test-driven-development/SKILL.md`
- `skills/qa/skill-judge/SKILL.md`