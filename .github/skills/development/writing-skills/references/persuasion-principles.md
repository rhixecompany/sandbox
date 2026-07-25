# Persuasion Principles for Bulletproofing Skills

Skills that enforce discipline (like TDD) need to resist rationalization. Agents are smart and will find loopholes when under pressure.

Understanding WHY persuasion techniques work helps you apply them systematically.

## Core Principles (Cialdini, 2021; Meincke et al., 2025)

### 1. Authority
Agents defer to explicit rules framed as mandatory, not optional.

**Apply:** Use "MUST", "REQUIRED", "NO EXCEPTIONS" instead of "should" or "recommended".

### 2. Commitment & Consistency
Once an agent commits to a principle (e.g., "I follow TDD"), they resist violating it.

**Apply:** State foundational principles early: "Violating the letter of the rules IS violating the spirit of the rules."

### 3. Scarcity
Limiting exceptions increases perceived value of compliance.

**Apply:** "No exceptions:" followed by explicit list of forbidden workarounds.

### 4. Social Proof
Agents follow patterns they see as standard practice.

**Apply:** "This is the standard pattern used across all production skills."

### 5. Unity
Frame rules as shared identity: "We are agents who write tests first."

**Apply:** Use first-person plural: "We write tests before code. We delete code written before tests."

## Closing Loopholes Explicitly

Don't just state the rule - forbid specific workarounds:

<Bad>
```markdown
Write code before test? Delete it.
```
</Bad>

<Good>
```markdown
Write code before test? Delete it. Start over.

**No exceptions:**
- Don't keep it as "reference"
- Don't "adapt" it while writing tests
- Don't look at it
- Delete means delete
```
</Good>

## Addressing "Spirit vs Letter" Arguments

Add foundational principle early:
```markdown
**Violating the letter of the rules IS violating the spirit of the rules.**
```

## Common Rationalization Patterns

| Excuse | Counter in Skill |
|--------|------------------|
| "I'll just keep it as reference" | Explicitly forbid keeping reference |
| "I'll adapt it while writing tests" | "Don't 'adapt' it while writing tests" |
| "Just one quick fix" | "Delete means delete" |
| "It's a special case" | "No exceptions" |
| "I understand the principle" | "Understanding ≠ compliance" |

## Testing Bulletproofing

Test with pressure scenarios:
- Time pressure: "Do it fast"
- Sunk cost: "You already wrote 50 lines"
- Exhaustion: "It's late, just this once"
- Combined: Time + sunk cost + exhaustion

Document exact rationalizations and add explicit counters for each.

## Psychology Note

Understanding WHY persuasion techniques work helps you apply them systematically. See `references/persuasion-principles.md` for research foundation (Cialdini, 2021; Meincke et al., 2025) on authority, commitment, scarcity, social proof, and unity principles.
