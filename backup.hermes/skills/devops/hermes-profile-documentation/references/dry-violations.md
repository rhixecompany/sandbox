# Common DRY Violations & Fixes

## Violation 1: Duplicating Standards Across Files

**Pattern:**
```
# USER.md
## Code Quality Standards
- TypeScript / JavaScript (Bun)
- Bash (POSIX)
- Python 3.11+
- Go (perf-critical)

# SOUL.md
## Code Quality Standards
### Preferred Languages
- TypeScript / JavaScript (Bun package manager)
- Bash / Shell (POSIX-compliant for git-bash/MSYS)
- Python 3.11+
- Go (performance-critical)
```

**Problem:** Same content appears in both files. If standards change, both must be updated. Risk of desync.

**Fix:** Keep standards ONLY in SOUL.md. USER.md references it:
```
# USER.md
## Development Standards

See SOUL.md for: code quality, commit style, formatting, linting, verification order.

# SOUL.md
## Code Quality Standards

**Languages:** TypeScript/JS (Bun), Bash (POSIX), Python 3.11+, Go (perf-critical)
```

---

## Violation 2: Repeating Profile State Across Sessions

**Pattern:**
```
Memory (2026-05-27):
> Profile consolidation: USER.md + SOUL.md updated...

Memory (2026-05-28):
> Profile consolidation: USER.md + SOUL.md updated...
```

**Problem:** Session notes about the same update exist in multiple memory entries. When state changes, old notes become stale.

**Fix:** Store only CURRENT state in memory. Reference session transcripts for history:
```
Memory:
> Hermes state (2026-05-27): 7 profiles, claude-haiku-4.5 active, Gateway manual/stopped...

(Don't record "consolidated on X date" — that's session history, not durable state)
```

---

## Violation 3: Redundant Explanations in Docs

**Pattern:**
```
# USER.md
User prefers concise, action-first responses and PowerShell for local Windows commands;
requires explicit approval before destructive operations and file commits.

# SOUL.md
## Response Style

### ✅ DO
- Start with action summary
- Skip "I can help with that"
- Show commands first, explanation after
- Use git for safety, not backups
- Run full end-to-end when phases are clear
- Pause only on blocking errors or explicit checkpoints
```

**Problem:** User preferences explained redundantly in USER.md, then detailed in SOUL.md. If preferences change, both need updating.

**Fix:** USER.md lists preferences as bullets; SOUL.md details ONLY the execution standards that implement them:
```
# USER.md
## Execution Preferences
- Concise, action-first; no pleasantries
- Full end-to-end when phases/tasks provided; pause on blocking errors or checkpoints
- Explicit approval: git commits, destructive operations
- File ops: Direct update/patch only (no .bak/.backup/.old); git for rollback

# SOUL.md
(Details HOW those preferences are enforced in response style, file operations, security)
```

---

## Violation 4: Multiple Sources of Truth for Active Model

**Pattern:**
```
Memory:
> Active model: gpt-5-mini (switched from claude-sonnet-4.5) via GitHub Copilot

USER.md:
> Active model: gpt-5-mini (GitHub Copilot)

SOUL.md:
> Profile-Specific Notes
> Active model: gpt-5-mini (GitHub Copilot)
```

**Problem:** Same fact in three places. After `hermes profile list` returns a new model, three places need updates.

**Fix:** Source of truth is HERMES STATUS. USER.md pulls from that. Memory references it; SOUL.md doesn't mention it:
```
# Command (run first)
hermes status

# USER.md (single source)
- **Default Model:** claude-haiku-4.5 (GitHub Copilot)

# Memory (optional reference only)
> Hermes state: claude-haiku-4.5 active...

# SOUL.md (no mention of model name; focuses on standards)
(Identity & Tone section describes the agent's role, not its model)
```

---

## Violation 5: Unclear Ownership of Metadata

**Pattern:**
```
# USER.md
## Notes

- Hermes home: C:\Users\Alexa\AppData\Local\hermes
- Skill library context: 194 fixed, 185 patched
- Known tool quirks: Cron script field is relative to...

# Memory
- Hermes installation folder is at C:\Users\Alexa\AppData\Local\hermes
- Skill library: 194 fixed, 185 patched (May 2026)
- Cron job script field is relative to...
```

**Problem:** Same facts in both USER.md and memory. Unclear which is authoritative.

**Fix:** Memory = durable personal facts (paths, quirks, learned lessons). USER.md = current profile state only:
```
# USER.md
- (No repetition of memory facts; focus on CURRENT profile state)

# Memory (single source for durable facts)
- Hermes home: C:\Users\Alexa\AppData\Local\hermes
- Cron script path: relative to ~/AppData/Local/hermes/scripts/ (no double-path prefix)
- Skill library workflow: 4-phase audit/plan/execute/verify
```

---

## Fix Checklist When Consolidating Docs

- [ ] **USER.md:** Identity + current state only. No standards or examples.
- [ ] **SOUL.md:** Standards + execution rules only. No profile state or model names.
- [ ] **Memory:** Durable facts only (paths, quirks, conventions). No session notes or transient state.
- [ ] **Remove all cross-file duplication.** Each fact lives in ONE place.
- [ ] **Add cross-references.** USER.md → "See SOUL.md for standards". SOUL.md → "See USER.md for profile".
- [ ] **Test:** Read USER.md + SOUL.md together; verify they're complementary, not redundant.
- [ ] **Run hermes status** before updating USER.md to ensure facts are current.
