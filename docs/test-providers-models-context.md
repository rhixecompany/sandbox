# test-providers-models — Dependency Context Catalog

> Generated: 2026-06-20T00:00:00Z | Source: `test-providers-models.prompt.md`

## Purpose Resolution

- **Purpose slug:** `test-providers-models`
- **Trigger:** `/test-providers-models`
- **Source file:** `test-providers-models.prompt.md`
- **Source reference:** `test-providers-models.prompt.txt`

---

## Forward Dependencies (from this file)

### External Links
| URL | Line | Context |
|-----|------|---------|
| `https://hermes-agent.nousresearch.com/docs/api/model-catalog.json` | 33 | Model catalog URL for fetching provider/model data |

### Skill Dependencies (from frontmatter `skills:` and `dependencies:`)
| Skill | Type | Purpose |
|-------|------|---------|
| `using-superpowers` | workflow | Establishes workflow foundation |
| `user-communication-preferences` | config | Loads user prefs for execution style |
| `plans-and-specs` | planning | Creates implementation plan from goal |

### Referenced Files
| Path | Line | Type |
|------|------|------|
| `./test-providers-models.prompt.txt` | 32 | Source reference (TXT version) |
| `C:\Users\Alexa\AppData\Local\hermes\scripts\test_models.py` | 128 | Test harness script (NOT FOUND) |

### Commands / Triggers
| Command | Line | Context |
|---------|------|---------|
| `/test-providers-models` | 2 | This prompt's trigger |

---

## Reverse Dependencies (files referencing this file/trigger)

| File | Line | Reference Type |
|------|------|----------------|
| `test-providers-models.prompt.txt` | 1 | Source TXT version with skill triggers |

---

## Related Prompt Family (same skill pattern)

| File | Shared Skills |
|------|---------------|
| `audit-skills-judge-fix.prompt.md` | using-superpowers, user-communication-preferences, plans-and-specs |
| `agents-system-prompt-context-fix.prompt.md` | using-superpowers, user-communication-preferences, plans-and-specs |
| `sync-hermes-copilot-codex.prompt.md` | using-superpowers, user-communication-preferences, plans-and-specs |

---

## File Structure Summary

| File | Lines | Size | Frontmatter | Tables | Code Blocks |
|------|-------|------|-------------|--------|-------------|
| `test-providers-models.prompt.md` | 152 | 5.4 KB | ✅ Valid YAML | 6 tables | 0 |
| `test-providers-models.prompt.txt` | 15 | 1.4 KB | ❌ No frontmatter | 0 | 0 |

---

## Missing/Referenced-but-Absent Artifacts

| Artifact | Referenced At | Status |
|----------|---------------|--------|
| `C:\Users\Alexa\AppData\Local\hermes\scripts\test_models.py` | Line 128 | ❌ NOT FOUND |
| Model catalog JSON | Line 33 | 🌐 External URL |

---

## Audit Target Files (for batch processing)

1. `test-providers-models.prompt.md` — Primary audit target
2. `test-providers-models.prompt.txt` — Source reference, potential TXT→MD conversion