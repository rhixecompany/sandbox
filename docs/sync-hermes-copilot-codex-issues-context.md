# sync-hermes-copilot-codex — Audit Issues Context

> Generated: 2026-06-21T10:00:00Z | Source: `sync-hermes-copilot-codex.prompt.md`
> Audit: Fresh re-run (Phase 1)

---

## Issues Summary

| Severity | Count | Category |
|----------|-------|----------|
| Medium | 1 | Dead reference to removed `.prompt.txt` file |
| Low | 3 | Missing recommended frontmatter fields |
| Low | 1 | Missing `metadata.hermes` section |
| Low | 1 | No verification checklist |
| Info | 1 | Inconsistent YAML style (`tags:` flow sequence vs block lists) |
| Info | 1 | Redundant `dependencies:` section alongside `skills:` |

---

## Detailed Findings

### sync-hermes-copilot-codex.prompt.md

---

#### MEDIUM: Stale Reference to Removed .prompt.txt

- **Location:** Line 45
- **Current:**
  ```
  - **Source reference:** `./sync-hermes-copilot-codex.prompt.txt`
  ```
- **Problem:** `sync-hermes-copilot-codex.prompt.txt` was removed in the previous enhancement run (canonical `.prompt.md` was kept). The reference is now a dead link.
- **Fix:** Update to reference only the canonical `.prompt.md` file, or add a note that legacy `.txt` was consolidated.

---

#### LOW: Missing Recommended Frontmatter Fields

- **Location:** Frontmatter (lines 1-26)
- **Current fields:** `trigger`, `description`, `tags`, `dependencies`, `skills`
- **Missing fields of value:**
  - `name` — Identifier for cross-system resolution (e.g., `sync-hermes-copilot-codex`)
  - `title` — Human-readable display name
  - `version` — Version tracking (e.g., `1.0.0`)
  - `author` — Ownership attribution
  - `license` — Usage terms
- **Fix:** Add relevant fields. Minimum suggested: `name`, `title`, `version` for a prompt file.

---

#### LOW: Missing metadata.hermes Section

- **Location:** Frontmatter, after `skills:`
- **Current:** No `metadata` block at all
- **Problem:** Without `metadata.hermes.related_skills`, Hermes has no structured way to map this prompt's skill dependencies.
- **Fix:** Add:
  ```yaml
  metadata:
    hermes:
      related_skills:
        - using-superpowers
        - user-communication-preferences
        - plans-and-specs
  ```

---

#### LOW: No Verification Checklist

- **Location:** End of file (after `## Actions Summary`)
- **Problem:** The prompt instructs execution but has no self-checking mechanism. Per Hermes normalization best practices, a verification checklist makes the prompt self-validating.
- **Fix:** Add a `## Verification Checklist` section with checkboxes for post-execution verification.

---

#### INFO: Inconsistent YAML Style (tags: Flow Sequence)

- **Location:** Frontmatter `tags:` field (lines 8-17)
- **Current:**
  ```yaml
  tags:
    [
      hermes,
      copilot,
      ...
    ]
  ```
- **Problem:** Valid YAML (flow sequence) but inconsistent with the block-style lists used for `skills:` and `dependencies:`. Not a functional issue, but style inconsistency.
- **Fix:** Convert to block-style list:
  ```yaml
  tags:
    - hermes
    - copilot
    ...
  ```

---

#### INFO: Redundant dependencies: Section

- **Location:** Frontmatter `dependencies:` (lines 18-21)
- **Current:**
  ```yaml
  dependencies:
    - skill:using-superpowers
    - skill:user-communication-preferences
    - skill:plans-and-specs
  ```
- **Context:** The `skills:` list (lines 22-25) already references the same three skills with clean identifiers. The `dependencies:` section with `skill:` prefix is a Copilot convention that duplicates the Hermes-style `skills:` list.
- **Fix:** Either:
  - A. Remove `dependencies:` (if Hermes-only target)
  - B. Keep both if cross-system compatibility is needed (add a clarifying comment)

---

## False Positives / Warnings Resolved

| Check | Lines | Result |
|-------|-------|--------|
| Table pipe balance | 50-63 | ✅ All tables balanced (3 pipes = 2 columns, correct) |
| Double frontmatter fences | 1-60 | ✅ 2 fences (correct) |
| Code fence balance | — | ✅ 0 fences (none needed) |
| Heading hierarchy | — | ✅ 1 H1, 6 H2, 4 H3 — no jumps |
| Trigger vs filename | 2 | ✅ Match: `/sync-hermes-copilot-codex` |
| `.prompt.txt` file exists? | — | ✅ File correctly removed (not needed) |
