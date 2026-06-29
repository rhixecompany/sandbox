# Phase 1: Triage Documentation

> Extracted from `projects-init.prompt.md`.

## Phase 1: Triage Documentation

**Goal:** Inventory all markdown documentation files, identify duplicates, consolidate, delete duplicates.

**Inputs:** `pwd`, `docs/**` (and subdirectories)

**Outputs:** Consolidated markdown documentation with no duplicates

**Steps:**

| Step | Action                                                         | Output             |
| ---- | -------------------------------------------------------------- | ------------------ |
| 1.1  | Run `ls pwd && ls pwd` to list workspace root files            | File list          |
| 1.2  | Run `ls docs/**` recursively to list all documentation files   | Doc file inventory |
| 1.3  | Identify duplicate markdown files (same name, similar content) | Duplicate list     |
| 1.4  | Consolidate: keep canonical version, delete duplicates         | Clean doc set      |
| 1.5  | Report before/after counts                                     | Phase summary      |

**Tasks:**

- **Task 1.1 — List root:** Run `ls` in workspace root, capture all markdown files
- **Task 1.2 — List docs:** Run recursive `ls docs/`, capture all `.md` files
- **Task 1.3 — Find duplicates:** Compare filenames across directories; flag same-name files
- **Task 1.4 — Consolidate:** For each duplicate pair, keep the version with more complete content, delete the other
- **Task 1.5 — Report:** Log file count before → after; document what was deleted

---
