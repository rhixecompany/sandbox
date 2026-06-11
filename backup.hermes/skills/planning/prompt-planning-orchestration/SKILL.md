---
name: prompt-planning-orchestration
title: Prompt Planning Orchestration
description: Design, specify, and execute complex prompt workflows with safety-first gates, comprehensive documentation, and profile-optimized phase orchestration.
author: Alexa
trigger: /prompt-planning, /orchestrate-prompt-workflow, /design-prompt-system
tags: [planning, prompts, orchestration, specifications, safety, multi-phase]
version: 1.0
status: active
---

# Prompt Planning Orchestration

> Design, specify, and execute complex prompt workflows with safety-first gates, comprehensive documentation, and profile-optimized phase orchestration.

## Overview

When a user requests a prompt workflow system (trigger: `/prompt-*`, `/design-prompt`, `/orchestrate-*`), the task involves multiple interlocking deliverables: template verification, specifications, code samples, implementation guides, and automation. This skill teaches the orchestration pattern and documentation shape for such requests.

## Trigger Conditions

Use this skill when:
- User requests `/prompt-*` workflow design or planning
- User asks to design a multi-stage prompt system or enhancement pipeline
- User wants specifications with code samples AND implementation guide
- User emphasizes "don't stop until complete" + "use best profiles for each task"
- Request includes safety/validation/constraint preservation concerns

## Core Pattern: Four-Phase Orchestration

### Phase 0: Verification (5-10 minutes)
**Profile:** Research analyst (data verification focus)

- Verify all prerequisites exist (templates, input files, directories)
- Create inventory/census of targets (how many files, which workflows)
- Report blocking items or missing dependencies
- Lock in scope before proceeding

**Execution:**
```bash
# Example: verify .github/prompts/ templates exist
ls -la .github/prompts/*.prompt.md
# Verify 7 .txt files in Prompts/
ls Prompts/*.prompts.txt
```

**Deliverable:** Status report (templates ✅, files found, scope locked)

---

### Phase 1: Comprehensive Plan (30-45 minutes)
**Profile:** Architect (specification focus)

Create a complete workflow specification covering:
- Executive summary (objectives, scope, constraints)
- Detailed phase-by-phase specs (what happens, inputs, outputs, success criteria)
- Safety/validation architecture (gates, constraints, rollback)
- Timeline and resource requirements
- Risk mitigation (5+ identified risks)

**Safety-First Design Pattern:**
```
For each phase involving transformation/enhancement:
  1. Pre-transformation audit (extract critical constraints)
  2. Transformation rules (what is allowed, what is not)
  3. Post-transformation verification (constraints still present)
  4. Violation handling (automatic FAIL, logging, rollback trigger)
```

**Deliverable:** 
- Markdown specification (800-1000 lines)
- Cover all phases with explicit success criteria
- Include constraint preservation gates if safety-relevant

---

### Phase 2: Code Samples (20-30 minutes)
**Profile:** Code architect (implementation focus)

Provide production-ready code implementing all phases:
- One class/module per phase
- Full type hints (Python 3.11+)
- Error handling and validation
- Data structures and serialization (JSON, etc.)
- ~700-850 lines total

**Code Structure:**
```python
class Phase1Name:
    @staticmethod
    def do_work(inputs) -> Tuple[output_type, report_dict]:
        """Process inputs through phase logic."""
        # Pre-validation
        # Core logic
        # Post-validation
        # Return structured output + metadata
```

**Deliverable:**
- Single `.py` file with all phase classes
- Ready to import and use
- Examples of invocation at module bottom

---

### Phase 3: Implementation Guide (45-60 minutes)
**Profile:** Patient tutor (step-by-step focus)

Create execution guide covering:
- Quick start (5-minute entry point)
- Step-by-step tutorial for EACH phase
- Shell scripts for automation (one per phase + master orchestrator)
- Pre/during/post execution checklists
- Troubleshooting section (8+ issue/solution pairs)
- Rollback procedures
- Integration with version control

**Script Delivery:**
```bash
scripts/
├─ phase1-name.sh
├─ phase2-name.sh
├─ phase3-name.sh
├─ run-full-pipeline.sh
└─ rollback-safety.sh
```

**Deliverable:**
- 1,200-1,500 line markdown guide
- Repeatable scripts (not hand-typed instructions)
- Checklists for validation at each gate

---

## Multi-Agent Orchestration

When user says "use best profiles for each task", apply:

| Phase | Best Profile | Why | Execution |
|-------|--------------|-----|-----------|
| Verification | research-analyst | inventory, data integrity, blocking items | delegate_task or execute_code |
| Plan | architect | specification design, safety gates, risk analysis | direct implementation or subagent |
| Code | code-architect | implementation samples, type hints, error handling | direct implementation |
| Guide | patient-tutor | step-by-step clarity, troubleshooting, checklists | direct implementation |

**Auto-Continue Rule:**
- Do NOT stop between phases asking for approval
- Mark each phase COMPLETE → move to next phase automatically
- Only stop for blocking errors (missing templates, unresolvable dependencies)
- Report progress via todo list updates

---

## Deliverable Shape

### PRIMARY OUTPUTS (4 files, ~3,500 lines)

1. **Comprehensive Plan** (~25 KB, 800-900 lines)
   - Location: `plan/` directory
   - Filename: `{workflow-name}-comprehensive-plan.md`
   - Content: Full specification with 6+ sections

2. **Code Samples** (~25 KB, 700-800 lines)
   - Location: `docs/` directory
   - Filename: `{workflow-name}-code-samples.py`
   - Content: Production-ready implementation

3. **Implementation Guide** (~32 KB, 1,200-1,400 lines)
   - Location: `docs/` directory
   - Filename: `{workflow-name}-implementation-guide.md`
   - Content: Step-by-step execution with scripts

4. **Supporting Docs** (2-3 files)
   - Location: `docs/` directory
   - Examples: execution-summary.md, index.md, navigation.md
   - Content: Quick refs, decision trees, file relationships

### SUPPORT FILES (optional, created during execution)

- `references/{detail}.md` — Phase-specific context, workarounds, pitfalls
- `templates/{scaffold}.md` — Starter files to copy and modify
- `scripts/{name}.sh` — Automation scripts created during guide phase

---

## Safety-First Pattern Deep Dive

### Multi-Gate Constraint Preservation (Phase 4+)

```
GATE 1: PRE-TRANSFORMATION AUDIT
  Extract all critical constraints (CRITICAL, MUST, APPROVAL, BACKUP, etc.)
  Document baseline count and text
  ↓ MUST PASS ↓
  
GATE 2: TRANSFORMATION APPLIED
  Apply enhancements/modifications
  Track all changes
  ↓ MUST PASS ↓
  
GATE 3: POST-TRANSFORMATION VERIFICATION
  Extract all constraints from modified version
  Compare before/after counts
  ↓ IF count decreased: FAIL ↓
  
GATE 4: PATTERN-LEVEL VERIFICATION
  For each critical pattern found in original:
    Check it still exists in modified version
    ↓ IF missing: FAIL with violation log ↓
  
GATE 5: DOCUMENTATION
  Document all changes made
  List any constraint removals (if found, FAIL earlier)
  Create audit trail
  ↓ SUCCESS: Proceed to next phase ↓
```

**Python Implementation Reference:**
```python
class EnhancementPhase:
    @staticmethod
    def validate_enhancement(original: str, enhanced: str, original_audit: Dict) -> Tuple[bool, List[str]]:
        """Validate that enhancements don't violate constraints."""
        errors = []
        
        # Check constraint count
        original_count = original_audit['total_constraints']
        enhanced_audit = SafetyReviewPhase.audit_constraints(enhanced, None)
        enhanced_count = enhanced_audit['total_constraints']
        
        if enhanced_count < original_count:
            errors.append(f"Constraint count decreased: {original_count} → {enhanced_count}")
        
        # Check critical patterns preserved
        for pattern, level in SafetyReviewPhase.CRITICAL_PATTERNS:
            if level == ConstraintLevel.CRITICAL:
                if re.search(pattern, original, re.IGNORECASE):
                    if not re.search(pattern, enhanced, re.IGNORECASE):
                        errors.append(f"Critical constraint pattern lost: {pattern}")
        
        return len(errors) == 0, errors
```

---

## Pitfalls and Anti-Patterns

### ❌ Pitfall 1: Single-File Deliverable
**Problem:** Delivering just a plan, or just code, or just a guide.  
**Solution:** Always deliver 4+ files (plan + code + guide + supporting). They're interdependent and users will ask for the others anyway.

### ❌ Pitfall 2: Skipping Verification Phase
**Problem:** Starting to write plan before confirming templates/targets exist.  
**Solution:** Always verify first (Phase 0). Templates, input files, directory structure. Report what's blocking.

### ❌ Pitfall 3: Weak Safety Specification
**Problem:** Mentioning "safety" vaguely without gates, patterns, or automated checks.  
**Solution:** Define explicit multi-gate pattern. Show constraint extraction, comparison, violation handling. Make it testable.

### ❌ Pitfall 4: Code Samples with No Error Handling
**Problem:** Beautiful code that breaks silently on edge cases.  
**Solution:** Full type hints, validation, try/except, clear error messages. Production-ready from day 1.

### ❌ Pitfall 5: Implementation Guide Without Scripts
**Problem:** Asking users to hand-type complex commands.  
**Solution:** Provide ready-to-run shell scripts for every major step. Users copy/paste, not interpret.

### ❌ Pitfall 6: Stopping Between Phases
**Problem:** Delivering Phase 1 plan and asking "should I continue?"  
**Solution:** User said "don't stop until complete". Auto-continue through all phases. Stop only on blocking errors.

---

## Quality Checkpoints

### Plan Acceptance Criteria
- ✅ All phases specified (typically 6-8 phases for complex workflows)
- ✅ Each phase has input, process, output explicitly stated
- ✅ Success criteria defined per phase
- ✅ Safety/validation gates documented
- ✅ Rollback procedures for destructive operations
- ✅ Timeline realistic and detailed (2.5 hours typical for 6-phase)
- ✅ 800+ lines (sufficient detail, not hand-wavy)

### Code Acceptance Criteria
- ✅ One class per phase minimum
- ✅ Full type hints (Python 3.11+ syntax)
- ✅ Error handling (try/except, validation, clear messages)
- ✅ Data structures for inputs/outputs (dataclass, Dict, etc.)
- ✅ JSON serialization where relevant
- ✅ ~700-850 lines (substantive, not skeleton)
- ✅ Example invocation at module bottom

### Guide Acceptance Criteria
- ✅ Quick start section (5-15 minute entry point)
- ✅ Step-by-step tutorial for each phase
- ✅ Shell scripts provided and embedded (not just described)
- ✅ Pre/during/post execution checklists
- ✅ Troubleshooting section (6+ issue/solution pairs)
- ✅ Rollback procedures documented
- ✅ 1,200+ lines (comprehensive, not terse)
- ✅ Git integration points noted

---

## When to Load This Skill

Load automatically when:
- User trigger matches `/prompt-*`, `/orchestrate-*`, `/design-prompt-*`
- Request includes "plan", "specification", "guide", "implement"
- User emphasizes "don't stop", "auto-continue", "use best profiles"

When partially relevant (e.g., just want code samples, not full guide):
- Load and adapt — skip the automation scripts phase if not asked for
- Always deliver plan + code + guide core trio
- Reduce supporting docs if scope is smaller

---

## Profile Selection Decision Tree

```
IF user says "use best profiles for each task":
  ├─ Phase 0 (Verification) → research-analyst
  ├─ Phase 1 (Plan) → architect
  ├─ Phase 2 (Code) → code-architect
  ├─ Phase 3 (Guide) → patient-tutor
  └─ → Use delegate_task with profile hints OR direct implementation
  
ELIF workflow is critical/safety-sensitive:
  ├─ Phase 1 (Plan) → architect (deep safety spec)
  ├─ Phase 2 (Code) → code-architect (full error handling)
  └─ → Use direct implementation, not delegation
  
ELSE (routine workflow planning):
  ├─ All phases → direct implementation
  └─ Use execute_code for parallelizable verification/code generation
```

---

## Integration with Other Skills

- **Coordinates with:** brainstorming, plans-and-specs, writing-plans
- **Related:** code-docs, code-samples (external library docs)
- **When these skills load:** plans-and-specs for single-document planning; this skill extends to multi-deliverable systems with code + guides

---

## Example: Dev-Init Workflow (2026-05-27)

Session executed this pattern end-to-end for `/dev-init` prompt workflow:

1. **Phase 0 - Verification** (2 min)
   - Verified all 6 `.github/prompts/` templates exist
   - Found 7 .txt files in `Prompts/` directory
   - Status: ✅ Ready to proceed

2. **Phase 1 - Plan** (30 min)
   - Created `plan/dev-init-comprehensive-plan.md` (867 lines)
   - Specified 6 phases: convert → context-map → safety → boost → plans → validate
   - Documented multi-gate safety constraint gates
   - Defined 7/7 success criteria

3. **Phase 2 - Code** (20 min)
   - Created `docs/dev-init-code-samples.py` (730 lines)
   - 6 phase classes: ConversionPhase, ContextMapPhase, SafetyReviewPhase, EnhancementPhase, PlanUpdatePhase, ValidationPhase
   - Full type hints, error handling, JSON serialization

4. **Phase 3 - Guide** (45 min)
   - Created `docs/dev-init-implementation-guide.md` (1,290 lines)
   - Step-by-step tutorial for all 6 phases
   - 7 shell scripts provided
   - Checklists and troubleshooting

5. **Phase 4 - Support** (10 min)
   - Created `docs/dev-init-execution-summary.md` (381 lines)
   - Created `docs/dev-init-index.md` (426 lines)
   - Navigation guide and decision tree

**Total Delivery:** 5 files, 3,694 lines, 104.2 KB, no interruptions

---

**Version:** 1.0  
**Last Updated:** 2026-05-27  
**Author:** Alexa  
**Status:** Active


## When to Use


- When you need to perform Prompt Planning Orchestration operations or tasks
- When managing Prompt Planning Orchestration infrastructure or configurations
- When automating or debugging Prompt Planning Orchestration workflows
- **Triggers**: "prompt planning orchestration" required for a project


