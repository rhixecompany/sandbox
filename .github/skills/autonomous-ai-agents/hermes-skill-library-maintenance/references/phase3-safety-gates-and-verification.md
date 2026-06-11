# Phase 3: Safety Gates and Verification Pattern

**Reference Session:** 2026-05-29 Hermes skill library audit and fix workflow

## Problem

Phase 3 (Execute Fix) is high-risk: bulk patches to 100+ files in a live system. A single bad patch can make skills unavailable. Without safety gates, a failure mid-execution leaves the system in an inconsistent state with no easy rollback.

## Solution: 4-Gate Safety Pattern + Verification Checklist

Execute Phase 3 only after establishing these 4 gates and completing verification:

### Gate 1: Active Task Protection

**Before patching any skill, check if it's currently in use.**

```bash
# Query active tasks
hermes tasks list --active

# Expected output (example):
# Task ID     | Status     | Skills Used
# ───────────────────────────────────────
# task-001    | running    | dispatching-parallel-agents
# task-002    | queued     | plans-and-specs
```

**Blocking condition:** If any target skill appears in active tasks, STOP.

**Action:** Schedule maintenance for next quiet window or wait for tasks to complete.

```python
# Programmatically
active_tasks = subprocess.run(['hermes', 'tasks', 'list', '--active'], 
                              capture_output=True, text=True).stdout
target_skills = {
    'dispatching-parallel-agents',
    'plans-and-specs',
    'enhance-markdown',
    'systematic-debugging',
    'hermes-skill-library-maintenance'
}

for skill in target_skills:
    if skill in active_tasks:
        print(f"BLOCKED: {skill} is in active task. Reschedule maintenance.")
        sys.exit(1)
```

### Gate 2: Git Checkpoint

**Before Phase 3, establish clean git state for rollback.**

```bash
# Pre-Phase 3 checklist
git status                          # Must be clean
git commit -am "pre-skills-fix"     # Or stash changes
git tag SKILL-FIX-{DATE}-PRE-PATCH  # Tag snapshot

# Example:
git tag SKILL-FIX-2026-05-29-PRE-PATCH
```

**Rationale:** If patches fail, `git checkout HEAD -- ~/.hermes/skills/{skill}/SKILL.md` restores any skill.

### Gate 3: Dependency Graph

**Map skill-calls-skill relationships before patching.**

Document which skills import/reference others:

```
dispatching-parallel-agents
  ← subagent-driven-development
  ← executing-plans

plans-and-specs
  ← writing-plans
  ← hermes-breakdown-plan

enhance-markdown
  (standalone, no internal references)
```

**Check for circular dependencies:**
```python
# If skill A patches skill B, and B references A, extra caution needed
dependencies = {
    'dispatching-parallel-agents': ['subagent-driven-development'],
    'subagent-driven-development': ['dispatching-parallel-agents', 'executing-plans'],
    'plans-and-specs': ['writing-plans'],
}

# Detect circular
from collections import defaultdict
def has_cycle(graph):
    visited = set()
    rec_stack = set()
    
    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(node)
        return False
    
    return any(dfs(node) for node in graph)

if has_cycle(dependencies):
    print("⚠️ Circular dependency detected. Patch in specific order or document impact.")
```

**Modification impact:** If patching skill A would break skills that depend on it, ensure dependent skills also get patched in same Phase 3 run.

### Gate 4: Rollback Plan

**Document how to recover from each possible failure.**

#### Rollback Strategy 1: Single-Skill Rollback

```bash
# If one skill patch fails/causes regression:
git checkout HEAD -- ~/.hermes/skills/{skill-name}/SKILL.md

# Example:
git checkout HEAD -- ~/.hermes/skills/dispatching-parallel-agents/SKILL.md

# Reload
hermes skills refresh
```

#### Rollback Strategy 2: Batch Rollback

```bash
# If entire batch failed (e.g., batch 3 of 7):
# Revert all patches in that batch
git log --oneline | head -20  # Find commits by batch

# Or, if checkpointed:
# Restore from pre-patch snapshot
git checkout SKILL-FIX-{DATE}-PRE-PATCH -- ~/.hermes/skills/

# Then move forward incrementally
```

#### Rollback Strategy 3: Full Abort

```bash
# If Phase 3 progresses to inconsistent state:
git reset --hard SKILL-FIX-{DATE}-PRE-PATCH
hermes skills refresh
```

---

## Phase 3 Execution: Step-by-Step

### Before Starting

- [ ] All 4 gates checked and documented
- [ ] No active tasks using target skills
- [ ] Git HEAD is clean, pre-patch snapshot tagged
- [ ] Dependency graph reviewed (no surprise circular deps)
- [ ] Rollback procedure understood by operator

### During Execution

**Use `skill_manage(action='patch')` for each fix, in order:**

```python
# Tier 1: Critical Fixes (highest risk, execute first)
skill_manage(action='patch', name='systematic-debugging', ...)
skill_manage(action='patch', name='dispatching-parallel-agents', ...)
skill_manage(action='patch', name='enhance-markdown', ...)

# After Tier 1, verify before proceeding
for skill in ['systematic-debugging', 'dispatching-parallel-agents', 'enhance-markdown']:
    result = subprocess.run(['hermes', 'skill', 'view', skill], 
                           capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR: {skill} is unavailable after patch. ROLLBACK.")
        # Execute Gate 4 recovery
        break

# Tier 2: Documentation Fixes (lower risk)
skill_manage(action='patch', name='plans-and-specs', ...)
# ... (repeat for all Tier 2)

# Tier 3: Content Updates (lowest risk)
skill_manage(action='patch', name='subagent-driven-development', ...)
# ... (repeat for all Tier 3)
```

### After Each Patch

```bash
# Verify skill is still loadable
hermes skill view {skill-name} | head -5
echo "✓ {skill-name} loaded"

# Check for broken cross-references
grep "skill_view()" ~/.hermes/skills/{skill-name}/SKILL.md | grep -v "name="
# Expected: 0 results (no broken calls)
```

### After All Patches

Run comprehensive verification suite:

```bash
# 1. Skill count unchanged
BEFORE=162
AFTER=$(hermes skills list | wc -l)
echo "Skill count: $BEFORE → $AFTER (expected: same)"

# 2. All patched skills loadable
for skill in {all 8 patched}; do
  hermes skill view "$skill" > /tmp/check.txt || {
    echo "ERROR: $skill failed to load"
    exit 1
  }
done
echo "✓ All skills loadable"

# 3. No broken cross-references
grep -r "skill_view()" ~/.hermes/skills/*/SKILL.md | grep -v "name=" | wc -l
# Expected: 0

# 4. Examples are current
grep -i "sandbox\|bash/" ~/.hermes/skills/*/SKILL.md | head -5
# Expected: added references visible
```

---

## Verification Checklist

Mark these complete before declaring Phase 3 successful:

- [ ] All 4 safety gates were checked before execution
- [ ] No active tasks were using target skills
- [ ] Pre-patch snapshot tagged (git)
- [ ] All patches applied without errors
- [ ] All patched skills load successfully (`hermes skill view` works)
- [ ] Skill count unchanged (162+ before and after)
- [ ] No broken cross-references in patched skills
- [ ] Examples reference current project (SandBox/Bash where applicable)
- [ ] Commit tagged: `git tag SKILL-FIX-{DATE}-POST-PATCH`

---

## Session Example: 2026-05-29 Skill Library Fix

**Execution:**
- 162+ skills in system
- 8 skills to patch (Tier 1-3)
- Phase 3 prepared (not yet executed in session)

**Safety Gates Established:**
1. ✓ Active Task Protection — will check before user approval
2. ✓ Git Checkpoint — pre-patch tag documented
3. ✓ Dependency Graph — mapped in audit report
4. ✓ Rollback Plan — git-based recovery documented

**Artifacts Generated:**
- Phase 1: `docs/skills-debug-context.md` (audit)
- Phase 2: `docs/plan/skills-debug-plan.md` (fix strategy)
- Phase 3 (prepared): `.github/prompts/skills-debug-prompt.md` (execution steps)

**Key Learning:** Separating Phase 3 preparation from execution enables review checkpoint. User can review prompt, confirm gates, and approve execution when safe.

---

## Related Patterns

- **Batch Processing:** See `references/batch-processing-pattern.md` for handling 100+ files efficiently
- **Title Derivation:** See `references/title-derivation-algorithm.md` for auto-generating skill metadata
- **Multi-Phase Artifact Pattern:** Phase outputs (markdown reports, JSON mappings, execution prompts) enable traceability and rollback
