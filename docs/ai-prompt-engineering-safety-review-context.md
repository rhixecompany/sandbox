# ai-prompt-engineering-safety-review — Context Catalog

Generated: 2026-05-25 | Source file: .github/prompts/ai-prompt-engineering-safety-review.prompt.md

## Purpose & Trigger

- **Trigger**: `/ai-prompt-engineering-safety-review`
- **Purpose Slug**: `ai-prompt-engineering-safety-review`
- **Description**: Review a prompt for safety, bias, security, clarity, and effectiveness, then produce a safer improved version.
- **Tags**: hermes, copilot, opencode, safety, security, bias, optimization
- **Domain**: Prompt engineering, safety, bias detection, security review

## File Inventory

| # | Path | Type | Status | Size |
| --- | ---- | ---- | ------ | ---- |
| 1 | .github/prompts/ai-prompt-engineering-safety-review.prompt.md | Markdown (Hermes Prompt) | Active | 3.8 KB |

## Frontmatter Summary

```yaml
trigger: /ai-prompt-engineering-safety-review
description: >-
  Review a prompt for safety, bias, security, clarity, and effectiveness, 
  then produce a safer improved version.
tags: [hermes, copilot, opencode, safety, security, bias, optimization]
dependencies:
  - skill:prompt-engineering
  - skill:systematic-debugging
skills:
  - prompt-engineering — Apply safety and quality patterns
  - systematic-debugging — Systematic issue detection
```

**Validation**: ✓ All required fields present

## Dependencies Declared

### Direct Dependencies

| Type | Name | Purpose | Status |
| --- | ---- | ---- | ------ |
| Skill | `prompt-engineering` | Apply safety, bias, and security review patterns | External (not verified) |
| Skill | `systematic-debugging` | Systematic detection of prompt issues | External (not verified) |

### Reference Sources

- No @agent references
- No /trigger references to other prompts
- No external URLs or links
- Self-contained workflow

## Reverse Dependencies & Cross-File References

### Forward References TO This Prompt

**In docs/**:
- `docs/ai-prompt-engineering-safety-review-context.md` — (this file)
- `docs/ai-prompt-engineering-safety-review-issues-context.md` — Issues catalog
- `docs/ai-prompt-engineering-safety-review-verify-context.md` — Verification report

**In .opencode/**:
- No direct references in `.opencode/` configuration files

**In backups/**:
- `docs/prompt-backups/20260525-162517Z/Prompts/bash-scripts-fix.prompts.md` — Listed as available prompt
- `docs/prompt-backups/20260525-162517Z/Prompts/general.prompts.md` — Listed as available prompt
- `docs/prompt-backups/20260525-162517Z/Prompts/repo.prompts.md` — Listed as available prompt

## Content Structure Audit

### Sections Present

| Section | Lines | Status |
| --- | ---- | ------ |
| YAML Frontmatter | 12 | ✓ Complete |
| Goal | 2 | ✓ Present |
| Context | 5 | ✓ Present (with domain focus) |
| Inputs | 3 | ✓ Present |
| Outputs | 3 | ✓ Present (includes checklist) |
| Rules | 6 | ✓ Present (safety-focused) |
| Skills Required | 4 | ✓ Present |
| Phases (4 phases) | 78 | ✓ Complete |
| Actions Summary | 6 | ✓ Present |

### Phase Breakdown

- **Phase 1: Analyze the prompt** (lines 59-75) — Classify task, review risks, assess clarity
- **Phase 2: Improve the prompt** (lines 76-92) — Rewrite into safer, clearer version
- **Phase 3: Test the revised prompt** (lines 93-109) — Check safety, clarity, usability
- **Phase 4: Verify and report** (lines 110-126) — Return final review for reuse

## Unique Characteristics

### Safety-First Focus

The prompt emphasizes safety at multiple levels:

**Rules Section (lines 41-49)**:
1. Check harmful content, misinformation, and illegal activity risk **first**
2. Check bias, privacy, and prompt-injection risk
3. Assess clarity, specificity, constraints, output format
4. Preserve task intent when rewriting
5. Add only safeguards that support the task
6. Keep improved prompt shorter and clearer

**Key Principle** (line 48): "Add only safeguards that support the task" — prevents over-constraining

### Risk Assessment Framework

**Phase 1 focuses on three risk categories**:
1. **Safety risks** — harmful content, misinformation, illegal activity
2. **Security risks** — bias, privacy, prompt injection
3. **Quality risks** — clarity, completeness, ambiguity

**Phase 3 validates these**:
1. Review revised prompt for safety
2. Review revised prompt for clarity
3. Review revised prompt for usability

### Output Quality

**Outputs** (lines 35-39):
- Prompt analysis report (findings)
- Revised prompt (actionable deliverable)
- Checklist of improvements (quick reference)

## Content Quality Notes

- **Consistency**: High — follows template patterns
- **Completeness**: All outputs described in phases
- **Clarity**: Clear analysis → improvement → testing flow
- **Safety Emphasis**: Explicit focus on harmful content, bias, injection risks
- **Practical Focus**: Avoids theory; emphasizes concrete recommendations (line 25)
- **Markdown**: Proper tables and structured lists
- **Line count**: 132 lines total (compact, focused)

## Cross-File Consistency

### Comparison with Related Prompts

Similar structured prompts in directory:
- `context-map.prompt.md` — Follows same 4-phase pattern ✓
- `boost-prompt.prompt.md` — Follows same pattern ✓

**Consistency Score**: Excellent — matches established template

## External Dependencies Check

| Dependency | Type | Verified | Status |
| --- | --- | --- | --- |
| skill:prompt-engineering | Skill | No | Not found in audit |
| skill:systematic-debugging | Skill | No | Not found in audit |

## Dependency Map

```
ai-prompt-engineering-safety-review.prompt.md
├── skill:prompt-engineering (external)
│   └── Safety and quality review patterns
└── skill:systematic-debugging (external)
    └── Issue detection methodology
```

## Related Prompt Ecosystem

This prompt is complementary to:
- **context-map.prompt.md** — /context-map — Used to map dependencies before changes
- **boost-prompt.prompt.md** — /boost-prompt — Used to refine prompts interactively
- **update-implementation-plan.prompt.md** — /update-implementation-plan — Used to structure plans

**Workflow Position**: Can be used BEFORE `/boost-prompt` to identify safety issues, or independently to audit existing prompts.

## Threat Model & Risk Categories Addressed

The prompt systematically addresses:

| Risk Category | Examples | Mitigation in Prompt |
| --- | --- | --- |
| Harmful Content | Violence, abuse, illegal activities | Phase 1.1: Classify and identify |
| Misinformation | False claims, unverified facts | Phase 1.2: Review safety risks |
| Prompt Injection | Malicious instructions, manipulation | Phase 1.2: Security risk review |
| Bias | Discrimination, unfair treatment | Phase 1.2: Bias check |
| Privacy | Exposure of sensitive data | Phase 1.2: Privacy check |
| Clarity Risks | Ambiguous instructions, unclear outputs | Phase 1.3: Quality assessment |
| Usability Issues | Missing context, unclear flow | Phase 3.3: Usability check |

## Historical References

Prompt is referenced in:
- Historical prompts inventory (prompt-backups dated 2026-05-25)
- Described as: "Use when reviewing prompts for safety, bias, security, and clarity."

## Status Summary

| Aspect | Finding |
| --- | --- |
| Frontmatter | ✓ Valid |
| Structure | ✓ Complete |
| Dependencies | ✓ Declared (2 skills) |
| Risk Framework | ✓ Comprehensive |
| Safety Focus | ✓ Strong |
| Internal References | ✓ Self-contained |
| Cross-file Refs | ✓ Appears in 3 backup indexes |
| Markdown Format | ✓ Proper |
| Content Flow | ✓ Clear, logical |

## Recommendations for Next Phase

1. Verify that `skill:prompt-engineering` and `skill:systematic-debugging` exist
2. Create a checklist template for Phase 1 risk assessment
3. Develop a library of common safety issues and remediation patterns
4. Add examples of before/after prompt revisions
5. Document the threat model more explicitly
6. Create a quick-start guide for safety review workflow
7. Consider adding a severity/priority rating system for identified issues
