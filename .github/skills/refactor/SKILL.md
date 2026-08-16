---
author: Alexa
description: 'Three-phase refactoring: understand before moving, move before changing.'
license: MIT
name: refactor
tags:
- refactoring
- code-quality
- best-practices
- tools
title: Refactor
version: 2.0.0
metadata:
  hermes:
    tags: []
---
# Refactor

## Overview

Automated reasoning and workflow tool for `refactor`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## Goal
Three-phase refactoring: understand before moving, move before changing. Never refactor and add behavior in the same pass.

## Core Rules
1. **Understand first** — Read all code you're about to refactor completely before touching it
2. **One concern per pass** — Never mix refactoring with feature work or bug fixes
3. **Tests protect refactoring** — Must have test coverage before and after
4. **Smallest safe step** — Prefer 5 small commits over 1 big one

## When to Use
- Duplicated code extracted to shared function
- Complex conditional simplified to strategy/state pattern
- Large function decomposed into smaller units
- Module reorganized for better cohesion
- Rename for clarity (variables, functions, types)

## When NOT to Use
- Adding features (use TDD instead)
- Bug fixes (use systematic-debugging instead)
- Greenfield code (use writing-plans instead)
- Performance optimization without benchmarks

## Workflow

### Phase 1: Understand
- `git log --oneline -20` — history context
- `read_file` all files in scope — full understanding
- `search_files` — find all callers/usages
- Check tests exist for the code being changed

**Exit:** Can explain every line you're about to change

### Phase 2: Safe Refactoring
1. **Test baseline** — Run full suite: `pytest tests/ -q`
2. **Make ONE structural change** — Extract method, rename, move
3. **Run tests** — Must still pass. If not, revert and try smaller step
4. **Commit** — `refactor: extract validate_email() from signup()`
5. **Repeat** — Until all planned refactors are done

**Preserve behavior:** Input/output contracts unchanged. No new features.

### Phase 3: Verify
- Full test suite passes (same as baseline)
- `git diff --stat` — shows only structural changes
- No TODO/FIXME added
- If CI available: `git push --dry-run` to verify

## Quick Reference: Common Refactors
| Pattern | Before | After |
|---------|--------|-------|
| Extract method | 50-line function | `process() -> _step1() _step2() _step3()` |
| Rename | `x`, `tmp` | `user_count`, `temporary_path` |
| Extract constant | `if x > 7:` | `MIN_PASSWORD_LENGTH = 8` |
| Move to module | `helpers.py` has 40 funcs | `helpers/validation.py`, `helpers/format.py` |
| Inline temp | `result = calc(); return result` | `return calc()` |

## Pitfalls
- **Refactoring and fixing bugs together** — violates single-responsibility. Fix bug first (separate commit), then refactor.
- **No test coverage** — refactoring untested code is guessing. Write characterization tests first.
- **Too large a step** — if reverting hurts, the step was too big. Split finer.
- **Golden-hammer syndrome** — not everything needs the Strategy pattern. Prefer simple over abstract.
- **Scope creep** — "while I'm here" leads to unbounded refactors. List planned changes before starting. Add unplanned ones as separate commits or skip them.
- **Missing imports after extraction** — when moving code between modules, verify all imports carry over. Run the test suite, don't just compile-check.

## Verification Checklist
- [ ] All code read and understood before first edit
- [ ] Test suite runs green before refactoring
- [ ] One structural change per commit
- [ ] Test suite runs green after each change
- [ ] No behavior changes mixed in
- [ ] git log shows clean, atomic refactor commits

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
