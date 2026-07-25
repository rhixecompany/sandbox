---
name: prompt-library-consolidation
title: Prompt Library Consolidation
description: Canonicalize prompt/template libraries, migrate legacy template trees, deduplicate conflicts, and validate references across prompts, docs, scripts, and tool declarations.
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - prompts
  - templates
  - consolidation
  - validation
  - refactoring
---

# Prompt Library Consolidation

Use this skill when cleaning up a prompt library at scale: migrating template trees, deduplicating conflicting files, normalizing filenames, rewriting references, and validating the resulting ecosystem.

## When to Use

- Migrating legacy template assets into a canonical `prompts/templates/` tree
- Consolidating duplicate or conflicting prompt/template files
- Normalizing filenames, especially after copy/migration work
- Updating prompt references in prompts, docs, results, or supporting artifacts
- Running validation after large prompt-library edits

## Core Workflow

1. **Inventory first**
   - Identify the canonical source tree and any legacy trees that still exist.
   - Search for reference patterns before editing, not after.

2. **Canonicalize the file layout**
   - Move template bodies into the canonical `prompts/templates/` tree.
   - Prefer one stable file path per concept.
   - Normalize filenames to plain ASCII when legacy copies introduce Unicode punctuation or ambiguous separators.

3. **Update references next**
   - Rewrite prompt/doc/result references to canonical template paths.
   - Replace legacy root-template references only after the canonical tree is in place.

4. **Retire the legacy tree only after references are clean**
   - Remove the old tree only after searches confirm no active references remain.
   - If old paths still appear, fix the references before deleting anything else.

5. **Validate with targeted checks**
   - Use repo-wide validators, but do not trust them alone when the repository already contains many pre-existing failures.
   - Combine validators with direct searches for legacy path patterns and spot-check the migrated family.

## Verification Checklist

- [ ] Canonical template files exist under `prompts/templates/`
- [ ] Legacy root template paths are gone from active prompts/docs/results
- [ ] Filenames are normalized and stable
- [ ] Any Unicode-dash or copy-artifact filenames are removed or renamed
- [ ] Validation runs are supplemented with targeted search checks
- [ ] The legacy tree is deleted only after references are clean

## Pitfalls

- Repo-wide validation can be noisy because unrelated prompt or skill issues may already exist.
- Do not treat validator failures as migration failures until you confirm the exact file set involved.
- Canonicalization often exposes filename drift from copied artifacts; check for Unicode dash variants and similar lookalikes.
- Retiring the legacy tree too early makes reference repair harder.

## References

- `references/prompt-migration-notes.md` — session-specific migration notes, verification patterns, and common false-positive patterns from repo-wide validation
