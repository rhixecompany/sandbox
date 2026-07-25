# Skill Testing Patterns by Type

All skills MUST pass a failing test first (TDD). The test approach varies by skill type.

## Discipline-Enforcing Skills (rules/requirements)

**Examples:** TDD, verification-before-completion, designing-before-coding

### Test Approach

**Baseline scenario:** Run without skill, document exact violations
```bash
# Pressure scenario
"You're under deadline. You've written 100 lines. Just run it once to verify."
# Observe: Does agent skip tests? Rationalizations?
```

**Pressure scenarios (combine for max effect):**
- Time pressure: "Do it fast, production is down"
- Sunk cost: "You already wrote 500 lines, don't throw them away"
- Exhaustion: "It's 2am, just make it work"
- Authority: "My manager says ship it now"
- Combined: Time + sunk cost + exhaustion

**Success criteria:** Agent follows rule under maximum pressure

**Document rationalizations and add explicit counters:**
```markdown
**Rationalization:** "I'll just run it once to verify"
**Counter:** "One run IS writing code before tests. Delete. Start over."
```

## Technique Skills (how-to guides)

**Examples:** condition-based-waiting, root-cause-tracing, defensive-programming

### Test Approach

**Application scenarios:** Can they apply the technique correctly?
```bash
"Apply condition-based waiting to this flaky test"
"Trace the root cause of this memory leak"
```

**Variation scenarios:** Do they handle edge cases?
```bash
"Condition appears then disappears"
"Multiple async operations in sequence"
"Condition never becomes true (timeout)"
```

**Missing information tests:** Do instructions have gaps?
```bash
"Apply technique to Go codebase" (if examples only in TS)
```

**Success criteria:** Agent successfully applies technique to new scenario

## Pattern Skills (mental models)

**Examples:** reducing-complexity, information-hiding concepts

### Test Approach

**Recognition scenarios:** Do they recognize when pattern applies?
```bash
"Should I use the flatten-with-flags pattern here?"
```

**Application scenarios:** Can they use the mental model?
```bash
"Refactor this nested if-else using information-hiding"
```

**Counter-examples:** Do they know when NOT to apply?
```bash
"This is a simple 3-line function. Does pattern apply?"
```

**Success criteria:** Agent correctly identifies when/how to apply pattern

## Reference Skills (documentation/APIs)

**Examples:** API documentation, command references, library guides

### Test Approach

**Retrieval scenarios:** Can they find the right information?
```bash
"Find the flag for disabling telemetry in CLI"
```

**Application scenarios:** Can they use what they found correctly?
```bash
"Use the CLI to export report with no telemetry"
```

**Gap testing:** Are common use cases covered?
```bash
"Common task: authenticate then query. Covered?"
```

**Success criteria:** Agent finds and correctly applies reference information

## Testing Workflow (All Types)

```bash
# 1. BASELINE - Run WITHOUT skill, document failures
# 2. WRITE SKILL - Address specific failures from baseline
# 3. VERIFY - Run WITH skill, confirm compliance
# 4. PRESSURE TEST - Run under combined pressure, confirm no regression
# 5. DOCUMENT - Record rationalizations and counters added
```

## Common Testing Mistakes

| Mistake | Fix |
|---------|-----|
| Testing only happy path | Always test violations under pressure |
| Testing once | Re-test after every edit (TDD) |
| No rationalization documentation | Record every excuse, add explicit counter |
| Skipping combined pressure | Combine time + sunk cost + exhaustion |
| Assuming "obvious" clarity | If not tested, it's broken |
