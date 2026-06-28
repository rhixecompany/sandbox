---
name: simplify
description: Remove duplicate agent definitions, prompt definitions, and consolidate workspace structure. Use during cleanup phases to deduplicate and compact configuration.
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - deduplication
  - cleanup
  - consolidation
  - simplify
---

# Simplify

Remove duplicate agent/prompt definitions and consolidate workspace structure. Use during cleanup phases to deduplicate and compact configuration.

## Workflow

1. **Detect duplicates** — Compare names, triggers, descriptions across platforms
2. **Choose canonical** — Select the authoritative version
3. **Merge** — Combine any unique properties from duplicates
4. **Remove** — Delete redundant definitions
5. **Verify** — Confirm no broken references remain

## Usage

```bash
# Detect duplicate agent definitions
simplify agents --detect-duplicates

# Consolidate workspace structure
simplify workspace --consolidate

# Dry run
simplify agents --detect-duplicates --dry-run
```

## Verification

- [ ] All duplicates identified and resolved
- [ ] Canonical definitions preserved
- [ ] No broken references after removal
- [ ] Structure compacted without data loss
