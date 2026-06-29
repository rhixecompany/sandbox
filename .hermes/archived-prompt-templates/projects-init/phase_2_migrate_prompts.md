# Phase 2: Migrate Prompts

> Extracted from `projects-init.prompt.md`.

## Phase 2: Migrate Prompts

**Goal:** Discover all markdown prompt files, migrate them to `.github/prompts/`, consolidate, delete duplicates.

**Inputs:** `pwd`, `.github/prompts/` (if exists)

**Outputs:** Prompt files consolidated in `.github/prompts/`

**Steps:**

| Step | Action                                               | Output                    |
| ---- | ---------------------------------------------------- | ------------------------- |
| 2.1  | Run `ls pwd` to list root-level prompt files         | Root prompt list          |
| 2.2  | Run `ls .github/prompts/**` to list existing prompts | Existing prompt inventory |
| 2.3  | Migrate root prompt files to `.github/prompts/`      | Migrated prompts          |
| 2.4  | Identify and delete duplicate prompts                | Deduplicated prompts      |
| 2.5  | Report before/after counts                           | Phase summary             |

**Tasks:**

- **Task 2.1 — List root prompts:** Find all `.prompt.md` / `.prompt.txt` files at workspace root
- **Task 2.2 — List existing:** Inventory `.github/prompts/` contents
- **Task 2.3 — Migrate:** Move each root prompt file to `.github/prompts/` (create dir if needed)
- **Task 2.4 — Deduplicate:** Compare for same-name prompts across old/new locations; delete originals
- **Task 2.5 — Report:** Log migration counts and deletions

---
