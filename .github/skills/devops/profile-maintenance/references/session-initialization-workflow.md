# Session Initialization Workflow

**Purpose:** Standardized session start procedure for Hermes Agent. Embedded in SOUL.md as Strict Rule #1.

---

## Rule Definition (from SOUL.md)

> **Rule 1: Session Start Rule**
> At the beginning of every session, you MUST:
> 1. Search the current working directory (`C:\\Users\\Alexa\\Desktop\\SandBox`) for `SESSION_REPORT.md`
> 2. Read and understand it completely
> 3. Explain it back to the user before proceeding with any other work

---

## Implementation Steps

### Step 1: Locate SESSION_REPORT.md
```bash
# Primary location
ls C:/Users/Alexa/Desktop/SandBox/SESSION_REPORT.md

# Fallback: search workspace
find /c/Users/Alexa/Desktop/SandBox -iname "session_report*" -type f 2>/dev/null
```

### Step 2: Read & Understand
```bash
cat C:/Users/Alexa/Desktop/SandBox/SESSION_REPORT.md
```
Extract:
- **Current session**: ID, timestamp, profile, model, work completed, tools/skills, state, result
- **Recent sessions** (rolling 5): IDs, titles, work summaries
- **Pattern**: Note any recurring tasks, errors, or context

### Step 3: Explain Back to User
**Format:**
```
## SESSION_REPORT.md Summary (Rolling 5 Sessions)

**Current Session:** <ID>
- Timestamp: <time>
- Profile: <profile>
- Model: <model>
- Work: <summary>
- State: <current state>
- Result: <outcome>

**Recent Sessions:**
1. <ID> — <title>
2. ...
```

---

## Why This Matters

1. **Context Restoration**: SESSION_REPORT.md is the durable log across sessions (especially after compaction)
2. **Continuity**: Prevents repeating work or losing track of multi-session tasks
3. **Accountability**: Verifies hooks (`session-logger`, `session-auto-commit`) are working
4. **User Trust**: Demonstrates the agent "reads the room" before acting

---

## Integration with Profile Maintenance

When updating SOUL.md (via `profile-maintenance` skill), verify:
- [ ] All 7 profiles have Session Start Rule in SOUL.md
- [ ] Rule text is identical across profiles
- [ ] No profile has conflicting session workflow instructions
- [ ] `.hermes.md` and `AGENTS.md` reference the rule

---

## Anti-Patterns to Avoid

| Anti-Pattern | Fix |
|--------------|-----|
| Skipping read, jumping to work | Mandatory: read → explain → then work |
| Reading only current session | Read rolling 5 — context needs history |
| Paraphrasing instead of explaining | Explain back verbatim key facts |
| Assuming SESSION_REPORT.md exists | Search first; if missing, note and create |

---

## Verification at Session End

Before ending session, update SESSION_REPORT.md:
```bash
# Append current session to rolling summary
# Prepend to recent sessions (shift older out)
# Update: session ID, date, profile, model, work, tools, skills, state, result
```

See `hermes-hooks` skill → `session-auto-commit` hook → should auto-commit this update.