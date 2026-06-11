# Multi-Target Execution Pattern — Worked Example

> From the dev-init prompt library standardization session (2026-05-29).

## Scenario

A `dev-init.prompts.md` file defined scope across 8 targets:
`.github/prompts/convert-plaintext-to-md`, `Prompts/*.txt` (7 files), 5 `.github/prompts/` files, and `Prompts/*.md` (8 files).

The prompt's deliverable was: "Detailed feature specs with code samples, file references, ordered execution plan."

## Execution

### Phase 1: Brainstorm & Plan

Loaded `brainstorming` and `plans-and-specs` skills. Created `docs/dev-init-comprehensive-plan.md` containing:

- Per-target spec with purpose, path, line count, acceptance criteria
- File inventory tables for each target group
- Frontmatter template showing the required YAML fields
- Cross-reference matrix (.txt → .md → .github/prompts/)
- Execution order (Target 1 → Target 2 → ... → Target 8)

```markdown
---
title: Dev-Init Comprehensive Plan
targets:
  - .github/prompts/convert-plaintext-to-md
  - Prompts/*.txt
  - .github/prompts/context-map
  - .github/prompts/boost-prompt
  - .github/prompts/ai-prompt-engineering-safety-review
  - .github/prompts/update-implementation-plan
  - .github/prompts/prompt-builder
  - Prompts/*.md
---
```

### Phase 2: Per-Target Execution

Each target was executed in order. Most (5/8) were already done by prior commits, but execution verified current state.

**Per-target verification code (Python via execute_code):**

```python
from hermes_tools import terminal
scope = ["context-map", "boost-prompt", "ai-prompt-engineering-safety-review",
         "update-implementation-plan", "prompt-builder"]
for s in scope:
    r = terminal(f"head -20 .github/prompts/{s}.prompt.md")
    lines = r["output"].split("\n")
    fm = lines[0].strip() == "---"
    trigger = any("trigger:" in l for l in lines[:20])
    deps = any("dependencies:" in l for l in lines[:20])
    skills = any("skills:" in l for l in lines[:20])
    tags = any("tags:" in l for l in lines[:20])
    desc = any("description:" in l for l in lines[:20])
    # All must pass for the target to be ✅
```

### Phase 3: Sweep Verification

After per-target checks, a cross-reference sweep ran across **all 14 files**:

```python
scope8 = ["agents-fix", "bash-scripts-fix", "commands-fix", "dev-init",
          "general", "repo", "skills-fix", "workspace-consolidate"]
for s in scope8:
    r = terminal(f"head -10 Prompts/{s}.prompts.md", ...)
    # Check: fm=True, trigger=True, desc=True, tags=True
```

**Result:** 12/14 files passed. **2 failures found:**

| File | Field Missing |
|------|---------------|
| `Prompts/bash-scripts-fix.prompts.md` | `description:` (used `title:` instead) |
| `Prompts/workspace-consolidate.prompts.md` | `description:` (used `title:` instead) |

Both used `title:` in frontmatter instead of `description:`. This is a common pattern gap — the `title:` field is technically valid YAML but all peer files use `description:`.

### Phase 4: Fix Gaps

Patched both files to add `description:`:

```yaml
# Before:
title: Bash Scripts Fix — Modernize and Consolidate Scripts
trigger: /bash-scripts-fix
tags: [...]

# After:
title: Bash Scripts Fix — Modernize and Consolidate Scripts
description: Modernize and consolidate all bash, PowerShell, bat, and TypeScript scripts with AST-safe transformations and dry-run support.
trigger: /bash-scripts-fix
tags: [...]
```

### Phase 5: Commit & Report

Single commit `e923268` with message documenting the scope, 3 files changed, 203 insertions.

## Key Takeaways

1. **Plan doc first** prevents scope creep and provides a single source of truth
2. **Sweep verification catches what per-target checks miss** — both missing `description:` fields were only visible when every file was checked against the same template
3. **`title:` vs `description:` is the most common frontmatter gap** — standardize on `description:` for consistency
4. **One commit per execution cycle** keeps the git log clean and atomic
5. **Always re-read files you wrote** — several files had warnings about sibling subagent modifications
