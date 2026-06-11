# Profile Orchestration Pattern

**Created:** 2026-05-27  
**Use case:** Multi-phase workflows where different phases require different specialized profiles

## Context

When executing complex workflows (5+ phases, multiple skill domains), orchestrating work across specialized Hermes profiles improves quality and efficiency. Each profile has:
- Specialized SOUL.md with role-specific tone and preferences
- Curated skill library for its domain
- Model/provider configuration tuned for its tasks

## Profile Types

| Profile | Strengths | Use For |
|---------|-----------|---------|
| **code-architect** | Implementation, TypeScript/Python/Go, architecture design | Phase 2 (design), script creation, refactoring |
| **research-analyst** | Analysis, documentation, safety audits, cataloging | Phase 1 (inventory), risk assessment, research |
| **exec-assistant** | Planning, scheduling, coordination, reporting | Project management, status reports, roadmaps |
| **patient-tutor** | Explanations, teaching, onboarding | Documentation, tutorials, knowledge transfer |
| **creative-director** | Design, UX, branding, visual artifacts | UI/UX work, presentations, marketing materials |
| **default** | General-purpose coordination | Phase 5-6 (integration), final verification |

## Orchestration Pattern

### 1. Phase-to-Profile Mapping

Before dispatching, map each phase to the best-suited profile:

**Example: Bash Scripts Modernization (6 phases)**

| Phase | Profile | Rationale |
|-------|---------|-----------|
| Phase 1: Catalog scripts | research-analyst | Analysis, documentation, risk triage |
| Phase 2: TypeScript architecture | code-architect | Design, implementation planning |
| Phase 3: Safety audit | research-analyst | Security review, pattern analysis |
| Phase 4: Implementation | code-architect | Coding, refactoring, tests |
| Phase 5: Verification | default | Integration testing, final checks |
| Phase 6: Documentation | patient-tutor | User-facing docs, onboarding guides |

### 2. Delegation Syntax

Use `delegate_task` with phase-specific context:

```python
delegate_task(tasks=[
    {
        "goal": "Phase 1: Catalog all scripts and identify CRITICAL patterns",
        "context": "You are research-analyst. Scan Bash/, projects/Banking/, projects/comicwise/. Output: docs/bash-scripts-list-context.md with risk triage.",
        "toolsets": ["file", "terminal", "web"],
        # profile parameter not yet supported, but context sets expectations
    },
    {
        "goal": "Phase 2: Design TypeScript architecture with ts-morph AST framework",
        "context": "You are code-architect. Input: docs/bash-scripts-list-context.md. Design: orchestrator pattern, dry-run mode, behavior tests.",
        "toolsets": ["file", "terminal"],
    }
])
```

**Note:** As of 2026-05-27, `profile=` parameter is not yet implemented in `delegate_task`. Use context-based instructions ("You are X profile") as a workaround until profile switching is supported.

### 3. Context Handoff

Each phase must provide complete context for the next:

- **Phase 1 → Phase 2**: Pass `docs/bash-scripts-list-context.md` (script inventory + audit results)
- **Phase 2 → Phase 3**: Pass `plan/bash-scripts-architecture.md` (TypeScript design)
- **Phase 3 → Phase 4**: Pass `docs/bash-scripts-safety-audit.md` (approved safe patterns)
- **Phase 4 → Phase 5**: Pass implementation artifacts + test results
- **Phase 5 → Phase 6**: Pass verification report + final state

### 4. Sequential vs Parallel Dispatch

**Sequential** (phases depend on each other):
```python
# Phase 1 completes, then Phase 2 starts
result1 = delegate_task(goal="Phase 1: Catalog", ...)
result2 = delegate_task(goal="Phase 2: Design", context=f"Input: {result1.output}", ...)
```

**Parallel** (phases are independent):
```python
# Phases 2-4 run concurrently (different skill domains)
results = delegate_task(tasks=[
    {"goal": "Phase 2: Context map", "context": "research-analyst", ...},
    {"goal": "Phase 3: Boost quality", "context": "code-architect", ...},
    {"goal": "Phase 4: Safety review", "context": "research-analyst", ...},
])
```

## Example: Prompt Pipeline (6 phases, 3 profiles)

**User Request:** "Implement the prompt pipeline bootstrap"

**Orchestration:**

| Phase | Profile | Tool |
|-------|---------|------|
| Phase 1: Convert txt→md | code-architect | `delegate_task` |
| Phase 2-4: Map/Boost/Safety | research-analyst | `delegate_task` |
| Phase 5-6: Plan/Normalize | default | Execute directly |

**Code:**
```python
delegate_task(tasks=[
    {
        "goal": "Phase 1: Convert Prompts/*.txt to markdown with YAML frontmatter",
        "context": "You are code-architect. Use .github/prompts/convert-plaintext-to-md.prompt.md. Preserve triggers.",
        "toolsets": ["file", "terminal"],
    },
    {
        "goal": "Phase 2-4: Build context map, boost quality, run safety review",
        "context": "You are research-analyst. Input: Prompts/*.md. Use context-map, boost-prompt, safety-review templates. Output: out/context_map.json, out/safety_report.json.",
        "toolsets": ["file", "terminal", "web"],
    }
])

# Phase 5-6 (coordination) runs directly as default profile
```

## Benefits

1. **Specialized expertise** — Each phase uses the profile best-suited for its domain
2. **Context isolation** — Profiles don't cross-contaminate preferences/workflows
3. **Quality improvement** — code-architect produces better code, research-analyst produces better analysis
4. **Parallel efficiency** — Independent phases run concurrently with specialized tools
5. **Clear handoffs** — Explicit context passing between profiles reduces confusion

## Pitfalls

- **Missing context handoff** — Each profile starts fresh; must pass all relevant state explicitly
- **Sequential dependencies** — Don't parallelize phases that depend on each other's output
- **Wrong profile for phase** — Cataloging with code-architect or coding with research-analyst reduces quality
- **No profile parameter yet** — Use context-based instructions until `delegate_task(profile=...)` is implemented

## Integration with Skills

When a profile loads a skill, that skill's SOUL.md preferences apply:
- code-architect: concise, implementation-first, tests before merge
- research-analyst: thorough analysis, citations, risk assessment
- patient-tutor: step-by-step explanations, no assumed knowledge

Plan phase-to-profile mapping BEFORE dispatching to ensure each phase gets the right expertise.

## Verification Checklist

After profile orchestration:
- [ ] Each phase mapped to appropriate profile
- [ ] Context handoff complete (all inputs passed explicitly)
- [ ] Sequential dependencies respected (no parallel dispatch of dependent phases)
- [ ] Results aggregated correctly (each profile's output captured)
- [ ] Final integration phase uses default profile (neutral coordinator)
