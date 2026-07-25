# Bulletproofing Skills Against Rationalization

Skills that enforce discipline (like TDD) need to resist rationalization. Agents are smart and will find loopholes when under pressure.

Understanding WHY persuasion techniques work helps you apply them systematically. See `references/persuasion-principles.md` for research foundation (Cialdini, 2021; Meincke et al., 2025) on authority, commitment, scarcity, social proof, and unity principles.

## Close Every Loophole Explicitly

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

## Address "Spirit vs Letter" Arguments

Add foundational principle early:
```markdown
**Violating the letter of the rules is violating the spirit of the rules.**
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
- Exhaustion: "It's 2am, just this once"
- Combined: Time + sunk cost + exhaustion

Document exact rationalizations and add explicit counters for each.
