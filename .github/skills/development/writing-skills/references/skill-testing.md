# Skill Testing Methodology by Type

All skills MUST pass a failing test first (TDD). The test approach varies by skill type.

## Discipline-Enforcing Skills (rules/requirements)

**Examples:** TDD, verification-before-completion, designing-before-coding

**Test with:**
- Academic questions: Do they understand the rules?
- Pressure scenarios: Do they comply under stress?
- Multiple pressures combined: time + sunk cost + exhaustion
- Identify rationalizations and add explicit counters

**Success criteria:** Agent follows rule under maximum pressure

## Technique Skills (how-to guides)

**Examples:** condition-based-waiting, root-cause-tracing, defensive-programming

**Test with:**
- Application scenarios: Can they apply the technique correctly?
- Variation scenarios: Do they handle edge cases?
- Missing information tests: Do instructions have gaps?

**Success criteria:** Agent successfully applies technique to new scenario

## Pattern Skills (mental models)

**Examples:** reducing-complexity, information-hiding concepts

**Test with:**
- Recognition scenarios: Do they recognize when pattern applies?
- Application scenarios: Can they use the mental model?
- Counter-examples: Do they know when NOT to apply?

**Success criteria:** Agent correctly identifies when/how to apply pattern

## Reference Skills (documentation/APIs)

**Examples:** API documentation, command references, library guides

**Test with:**
- Retrieval scenarios: Can they find the right information?
- Application scenarios: Can they use what they found correctly?
- Gap testing: Are common use cases covered?

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
| Skipping "too tedious" | Testing is less tedious than debugging bad skill in production |
| "Academic review is enough" | Reading ≠ using. Test application scenarios. |
| "No time to test" | Deploying untested skill wastes more time fixing it later. |

**All of these mean: Test before deploying. No exceptions.**
