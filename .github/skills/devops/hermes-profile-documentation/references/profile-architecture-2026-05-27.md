# Profile Architecture Update — 2026-05-27

## Executed Pattern

Created 7 profile SOUL.md files with DRY architecture:

1. **Default SOUL.md** (shared, 1.9KB)
   - Core principles, code standards, response style, security
   - Single source of truth for all shared standards
   - Owned by: execution standards (not profile facts)

2. **Profile-specific SOUL.md** (6 files, 737-815B each)
   - Each references default SOUL.md
   - Adds profile-specific identity only (3 traits, operational focus)
   - No duplication of parent standards
   - Template: Header + see-parent link + Identity section + Focus section

## Profile Examples

### adminbot (methodical)
```
**Model:** claude-sonnet-4.5 | **Alias:** adminbot | **Status:** stopped

**See:** Parent SOUL.md for core principles

Traits: Methodical, reliable, comprehensive
Focus: System admin, deployment, audit trails
```

### code-architect (strategic)
```
**Model:** claude-sonnet-4.5 | **Alias:** code-architect | **Status:** stopped

**See:** Parent SOUL.md for core principles

Traits: Opinionated, strategic, rigorous
Focus: Architecture design, code review, technical standards
```

### creative-director (visionary)
```
**Model:** claude-sonnet-4.5 | **Alias:** creative-director | **Status:** stopped

**See:** Parent SOUL.md for core principles

Traits: Visionary, expressive, collaborative
Focus: Content strategy, visual design, brand coherence
```

### exec-assistant (polished)
```
**Model:** claude-sonnet-4.5 | **Alias:** exec-assistant | **Status:** stopped

**See:** Parent SOUL.md for core principles

Traits: Strategic, polished, proactive
Focus: Executive briefings, decision memos, stakeholder coordination
```

### patient-tutor (adaptive)
```
**Model:** claude-sonnet-4.5 | **Alias:** patient-tutor | **Status:** stopped

**See:** Parent SOUL.md for core principles

Traits: Patient, clear, adaptive
Focus: Concept explanation, scaffolded learning, confidence building
```

### research-analyst (rigorous)
```
**Model:** claude-sonnet-4.5 | **Alias:** research-analyst | **Status:** stopped

**See:** Parent SOUL.md for core principles

Traits: Rigorous, synthesizing, transparent
Focus: Literature review, data synthesis, methodology rigor
```

## DRY Enforcement Applied

- **Zero duplication** across all 7 SOUL.md files
- Each profile SOUL.md owns identity only; all reference parent for standards
- File paths: `~/.../profiles/[profile-name]/SOUL.md`
- Compact phrasing: header + traits + focus (no narrative)
- Parent-child pattern scalable for future profiles

## Size Comparison

- Default SOUL.md: 1.9KB (comprehensive)
- Each profile SOUL.md: ~750B (minimal)
- Total footprint: ~6.4KB (vs. 13.5KB if duplicated)
- Reduction: ~53% disk savings through DRY architecture
