---
author: Hermes Agent (adapted from obra/superpowers)
description: 'TDD: enforce RED-GREEN-REFACTOR, tests before code.'
license: MIT
metadata:
  hermes:
    related_skills:
    - systematic-debugging
    - writing-plans
    - subagent-driven-development
    tags:
    - testing
    - tdd
    - development
    - quality
    - red-green-refactor
name: test-driven-development
platforms:
- linux
- macos
- windows
title: Test Driven Development
version: 1.1.0

---
## Goal
TDD: enforce RED-GREEN-REFACTOR, tests before code.


# Test-Driven Development (TDD)

## Workflow

### Phase 1: Setup

Verify prerequisites are in place and configure the environment.

### Phase 2: Execute

Perform the skills\software development\test driven development\skill.md operations following the skill instructions.

### Phase 3: Verify

Check outputs against expected results and resolve any issues.

### Phase 4: Cleanup

Document outcomes and store any configuration changes.

## Overview

Write the test first. Watch it fail. Write minimal code to pass.

**Core principle:** If you didn't watch the test fail, you don't know if it tests the right thing.

**Violating the letter of the rules is violating the spirit of the rules.**

## When to Use

**Always:**
- New features
- Bug fixes
- Refactoring
- Behavior changes

**Exceptions (ask the user first):**
- Throwaway prototypes
- Generated code
- Configuration files

Thinking "skip TDD just this once"? Stop. That's rationalization.

## The Iron Law

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Write code before the test? Delete it. Start over.

**No exceptions:**
- Don't keep it as "reference"
- Don't "adapt" it while writing tests
- Don't look at it
- Delete means delete

Implement fresh from tests. Period.

## Red-Green-Refactor Cycle

### RED — Write Failing Test

Write one minimal test showing what should happen.

**Good test:**
```python
def test_retries_failed_operations_3_times():
    attempts = 0
    def operation():
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise Exception('fail')
        return 'success'

    result = retry_operation(operation)

    assert result == 'success'
    assert attempts == 3
```
Clear name, tests real behavior, one thing.

**Bad test:**
```python
def test_retry_works():
    mock = MagicMock()
    mock.side_effect = [Exception(), Exception(), 'success']
    result = retry_operation(mock)
    assert result == 'success'  # What about retry count? Timing?
```
Vague name, tests mock not real code.

**Requirements:**
- One behavior per test
- Clear descriptive name ("and" in name? Split it)
- Real code, not mocks (unless truly unavoidable)
- Name describes behavior, not implementation

### Verify RED — Watch It Fail

**MANDATORY. Never skip.**

```bash
# Use terminal tool to run the specific test
pytest tests/test_feature.py::test_specific_behavior -v
```

Confirm:
- Test fails (not errors from typos)
- Failure message is expected
- Fails because the feature is missing

**Test passes immediately?** You're testing existing behavior. Fix the test.

**Test errors?** Fix the error, re-run until it fails correctly.

### GREEN — Minimal Code

Write the simplest code to pass the test. Nothing more.

**Good:**
```python
def add(a, b):
    return a + b  # Nothing extra
```

**Bad:**
```python
def add(a, b):
    result = a + b
    logging.info(f"Adding {a} + {b} = {result}")  # Extra!
    return result
```

Don't add features, refactor other code, or "improve" beyond the test.

**Cheating is OK in GREEN:**
- Hardcode return values
- Copy-paste
- Duplicate code
- Skip edge cases

We'll fix it in REFACTOR.

### Verify GREEN — Watch It Pass

**MANDATORY.**

```bash
# Run the specific test
pytest tests/test_feature.py::test_specific_behavior -v

# Then run ALL tests to check for regressions
pytest tests/ -q
```

Confirm:
- Test passes
- Other tests still pass
- Output pristine (no errors, warnings)

**Test fails?** Fix the code, not the test.

**Other tests fail?** Fix regressions now.

### REFACTOR — Clean Up

After green only:
- Remove duplication
- Improve names
- Extract helpers
- Simplify expressions

Keep tests green throughout. Don't add behavior.

**If tests fail during refactor:** Undo immediately. Take smaller steps.

### Repeat

Next failing test for next behavior. One cycle at a time.

## Why Order Matters

**"I'll write tests after to verify it works"**

Tests written after code pass immediately. Passing immediately proves nothing:
- Might test the wrong thing
- Might test implementation, not behavior
- Might miss edge cases you forgot
- You never saw it catch the bug

Test-first forces you to see the test fail, proving it actually tests something.

**"I already manually tested all the edge cases"**

Manual testing is ad-hoc. You think you tested everything but:
- No record of what you tested
- Can't re-run when code changes
- Easy to forget cases under pressure
- "It worked when I tried it" ≠ comprehensive

Automated tests are systematic. They run the same way every time.

**"Deleting X hours of work is wasteful"**

Sunk cost fallacy. The time is already gone. Your choice now:
- Delete and rewrite with TDD (high confidence)
- Keep it and add tests after (low confidence, likely bugs)

The "waste" is keeping code you can't trust.

**"TDD is dogmatic, being pragmatic means adapting"**

TDD IS pragmatic:
- Finds bugs before commit (faster than debugging after)
- Prevents regressions (tests catch breaks immediately)
- Documents behavior (tests show how to use code)
- Enables refactoring (change freely, tests catch breaks)

"Pragmatic" shortcuts = debugging in production = slower.

**"Tests after achieve the same goals — it's spirit not ritual"**

No. Tests-after answer "What does this do?" Tests-first answer "What should this do?"

Tests-after are biased by your implementation. You test what you built, not what's required. Tests-first force edge case discovery before implementing.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30 seconds. |
| "I'll test after" | Tests passing immediately prove nothing. |
| "Tests after achieve same goals" | Tests-after = "what does this do?" Tests-first = "what should this do?" |
| "Already manually tested" | Ad-hoc ≠ systematic. No record, can't re-run. |
| "Deleting X hours is wasteful" | Sunk cost fallacy. Keeping unverified code is technical debt. |
| "Keep as reference, write tests first" | You'll adapt it. That's testing after. Delete means delete. |
| "Need to explore first" | Fine. Throw away exploration, start with TDD. |
| "Test hard = design unclear" | Listen to the test. Hard to test = hard to use. |
| "TDD will slow me down" | TDD faster than debugging. Pragmatic = test-first. |
| "Manual test faster" | Manual doesn't prove edge cases. You'll re-test every change. |
| "Existing code has no tests" | You're improving it. Add tests for the code you touch. |

## Red Flags — STOP and Start Over

If you catch yourself doing any of these, delete the code and restart with TDD:

- Code before test
- Test after implementation
- Test passes immediately on first run
- Can't explain why test failed
- Tests added "later"
- Rationalizing "just this once"
- "I already manually tested it"
- "Tests after achieve the same purpose"
- "Keep as reference" or "adapt existing code"
- "Already spent X hours, deleting is wasteful"
- "TDD is dogmatic, I'm being pragmatic"
- "This is different because..."

**All of these mean: Delete code. Start over with TDD.**


## Pitfalls

- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context
- **Context limits:** Process in batches; write results after each batch
## Verification Checklist

Before marking work complete:

- [ ] Every new function/method has a test
- [ ] Watched each test fail before implementing
- [ ] Each test failed for expected reason (feature missing, not typo)
- [ ] Wrote minimal code to pass each test
- [ ] All tests pass
- [ ] Output pristine (no errors, warnings)
- [ ] Tests use real code (mocks only if unavoidable)
- [ ] Edge cases and errors covered

Can't check all boxes? You skipped TDD. Start over.

## When Stuck

| Problem | Solution |
|---------|----------|
| Don't know how to test | Write the wished-for API. Write the assertion first. Ask the user. |
| Test too complicated | Design too complicated. Simplify the interface. |
| Must mock everything | Code too coupled. Use dependency injection. |
| Test setup huge | Extract helpers. Still complex? Simplify the design. |

## Hermes Agent Integration

### Running Tests

Use the `terminal` tool to run tests at each step:

```python
# RED — verify failure
terminal("pytest tests/test_feature.py::test_name -v")

# GREEN — verify pass
terminal("pytest tests/test_feature.py::test_name -v")

# Full suite — verify no regressions
terminal("pytest tests/ -q")
```

### With delegate_task

When dispatching subagents for implementation, enforce TDD in the goal:

```python
delegate_task(
    goal="Implement [feature] using strict TDD",
    context="""
    Follow test-driven-development skill:
    1. Write failing test FIRST
    2. Run test to verify it fails
    3. Write minimal code to pass
    4. Run test to verify it passes
    5. Refactor if needed
    6. Commit

    Project test command: pytest tests/ -q
    Project structure: [describe relevant files]
    """,
    toolsets=['terminal', 'file']
)
```

### With systematic-debugging

Bug found? Write failing test reproducing it. Follow TDD cycle. The test proves the fix and prevents regression.

Never fix bugs without a test.

## Testing Anti-Patterns

- **Testing mock behavior instead of real behavior** — mocks should verify interactions, not replace the system under test
- **Testing implementation details** — test behavior/results, not internal method calls
- **Happy path only** — always test edge cases, errors, and boundaries
- **Brittle tests** — tests should verify behavior, not structure; refactoring shouldn't break them

## Phase 5.2: Real-World Operation Validation

**After unit tests pass (GREEN), before deployment:**

TDD validates code works. **Real-world operation tests** validate that code works *correctly in actual use*, producing correct output, metrics, and side effects.

**See**: `references/phase-5-2-real-world-operations.md` for full pattern, safety verdicts, and example from Sandbox/Bash project.

### When to Use Phase 5.2

- Scripts with real operational effects (disk cleanup, package upgrade, cache clearing)
- Multi-step workflows combining multiple scripts
- Code that interacts with external systems (package managers, filesystems)
- Any tool where dry-run mode reveals what will happen, but you need to verify actual execution matches

### Pattern: Dry-Run → Real Execution

**Step 1: Dry-Run Test (Preview)**
```bash
# Script with --dry-run flag shows what would happen, without doing it
bash clean_dependency_folders.sh --dry-run
# Output: "Found 301.1 MB, would clean [list], (dry-run — no changes made)"
```

**Step 2: Metrics Capture Test (Safe, Read-Only)**
```bash
# Before execution, capture baseline metrics
pwsh -NoProfile -Command '. ./disk-analysis.ps1'
# Output: "394.40 MB dependencies, 5 folders"
```

**Step 3: Real Execution Test (Conditional)**
```bash
# Run with actual operations (destructive only if --dry-run removed)
bash cache-clean.sh --all
# Output: actual results, logs created
```

**Step 4: Verification Test (Read-Only)**
```bash
# Verify results match expected output
pwsh -NoProfile -Command '. ./verify_cleanup.ps1'
# Output: "FOUND: N remaining folders"
```

### Structure (Reusable Template)

```bash
#!/bin/bash
# execute-real.sh — Real-world operation validation suite

# For each operation:
# 1. Dry-run: preview what would happen
# 2. Metrics: capture before/after data
# 3. Actual: run with real operations
# 4. Verify: confirm results match expected behavior

test_1_dry_run() {
    echo "=== TEST 1: DRY-RUN (Safe, Preview) ==="
    bash script.sh --dry-run
    echo "Status: ✓ PASS (no actual changes)"
}

test_2_real_execution() {
    echo "=== TEST 2: REAL EXECUTION ==="
    bash script.sh --all
    echo "Status: ✓ PASS (actual results captured)"
}

test_3_verification() {
    echo "=== TEST 3: VERIFICATION (Safe, Read-Only) ==="
    pwsh -NoProfile -Command '. ./verify.ps1'
    echo "Status: ✓ PASS (results verified)"
}

# Run all tests
test_1_dry_run
test_2_real_execution
test_3_verification
```

### Key Metrics to Capture

For cleanup/removal operations:
- Space identified before
- Items removed (count + size)
- Space freed after
- Log files created with timestamps

For upgrade/install operations:
- Packages available/checked
- Installed/upgraded count
- Success rate (N/total)
- Error details logged

For analysis operations:
- Scan time
- Items found
- Categories and breakdown
- Anomalies or critical findings

### Pitfall: Skipping Dry-Run

**❌ WRONG:** Jump straight to real execution without --dry-run
```bash
bash clean_dependency_folders.sh  # Deletes immediately!
```

**✓ RIGHT:** Dry-run first, verify output, then real execution
```bash
bash clean_dependency_folders.sh --dry-run    # Preview
bash clean_dependency_folders.sh                # Real
```

Why: Dry-run proves the operation targets the right things before actually deleting.

### Pitfall: No Before/After Metrics

**❌ WRONG:** Run cleanup without capturing space freed
```bash
bash cache-clean.sh --all
# No way to verify it worked or how much space was freed
```

**✓ RIGHT:** Capture metrics at each stage
```bash
pwsh '. ./disk-analysis.ps1'          # Before
bash cache-clean.sh --all              # Execute
pwsh '. ./disk-analysis.ps1'          # After
# Comparison shows: "Freed 394.40 MB"
```

### Safety Verdict Convention

Label each test with its risk level:

```
TEST 1: Disk Analysis (Safe, Read-Only)
  - No files modified
  - No side effects
  - Safe to run anytime

TEST 2: Dependency Cleanup (Conditional: Dry-Run)
  - Dry-run: safe (no changes)
  - Real: destructive (deletes files)
  - Status: Dry-run verified

TEST 3: Package Upgrade (Conditional: Admin Required)
  - Requires elevated privileges
  - May require network
  - Status: Skipped (insufficient privileges)
```

### Integration with Unit Tests

```
Unit Tests (Phase 1-4: RED-GREEN-REFACTOR)
  ↓ Verify code logic
  ↓ All passing

Real-World Operation Tests (Phase 5.2: Dry-Run → Real)
  ↓ Verify operations produce correct real-world effects
  ↓ Metrics captured and documented

Production Deployment
  ↓ Safe and verified
```

## Final Rule

```
Production code → test exists and failed first
Otherwise → not TDD

Operational code → dry-run verified, metrics captured, real execution logged
Otherwise → not ready for deployment
```

No exceptions without the user's explicit permission.

