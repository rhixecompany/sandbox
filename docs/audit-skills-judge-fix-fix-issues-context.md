# audit-skills-judge-fix — Fix Issues Context (Progress Log)

> Generated: 2026-06-20T02:00:00Z | Phase: 2-3 (Fix Planning + Execution)
> Tracks: Fix application progress per `thoughts/plans/audit-skills-judge-fix-debug.md`

---

## Fix Progress Tracker

| ID | Issue | Severity | File | Batch | Status | Applied | Verified |
|----|-------|----------|------|-------|--------|---------|----------|
| F1 | Prose in skills: frontmatter | Medium | .prompt.md | 1 | Pending | - | - |
| F2 | Hardcoded Windows paths | Low | .prompt.md | 1 | Pending | - | - |
| F3 | Emoji in technical doc | Low | .prompt.md | 1 | Pending | - | - |
| F4 | .prompt.txt duplicate | Medium | .prompt.txt | 1 | Pending | - | - |
| F5 | Full verification | - | Both | 2 | Pending | - | - |

---

## Batch 1 Execution Log (Proof-of-Concept)

### F1: Prose in skills: Frontmatter
- **Target:** `audit-skills-judge-fix.prompt.md` lines 15-22
- **Action:** Strip descriptions from `skills:` list
- **Command:** TBD
- **Result:** TBD
- **Verification:** Frontmatter `skills:` list contains only identifiers

### F2: Hardcoded Windows Paths
- **Target:** `audit-skills-judge-fix.prompt.md` (multiple lines)
- **Action:** Normalize all `C:\Users\Alexa\AppData\Local\hermes\` → `~/AppData/Local/hermes/`
- **Command:** TBD
- **Result:** TBD
- **Verification:** No `C:\Users\` or `C:/Users/` patterns in content

### F3: Emoji in Technical Doc
- **Target:** `audit-skills-judge-fix.prompt.md` line 265
- **Action:** Replace `🔴` with `[RED]`
- **Command:** TBD
- **Result:** TBD
- **Verification:** No emoji characters in content

### F4: .prompt.txt Duplicate
- **Target:** `audit-skills-judge-fix.prompt.txt`
- **Action:** Remove file (canonical .prompt.md kept)
- **Command:** TBD
- **Result:** TBD
- **Verification:** Single `.prompt.md` file remains

---

## Batch 2 Execution Log

### F5: Full Verification
- **Target:** `audit-skills-judge-fix.prompt.md`
- **Action:** Re-run complete audit suite
- **Command:** TBD
- **Result:** TBD
- **Verification:** All 8 gates pass

---

## Change Summary (Cumulative)

| File | Lines Changed | Issues Fixed | Last Modified |
|------|---------------|--------------|---------------|
| audit-skills-judge-fix.prompt.md | 0 | 0/3 | - |
| audit-skills-judge-fix.prompt.txt | 0 | 0/1 | - |

---

## Next Actions

1. Execute Batch 1 fix F1: Clean `skills:` frontmatter list
2. Execute Batch 1 fix F2: Normalize Windows paths
3. Execute Batch 1 fix F3: Replace emoji
4. Execute Batch 1 fix F4: Remove `.prompt.txt`
5. Verify Batch 1 with audit script
6. Run full verification (F5)
7. Update this log with results