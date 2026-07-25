---
name: prompt-library-canonicalization
title: "Prompt Library Canonicalization"
description: "Use when auditing, migrating, deduplicating, or canonicalizing prompt/instruction/agent libraries across Hermes, Copilot, or local AI tooling stores."
version: 0.1.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags:
      - prompts
      - migration
      - dedupe
      - canonicalization
---
# Prompt Library Canonicalization

## Goal
Make one authoritative prompt/instruction/agent library on disk, migrate legacy stores into it, dedupe exact bodies, fix stale cross-references, and verify the result before claiming completion.

## When to Use
- Consolidating scattered prompt libraries into `.github/prompts` or another canonical root
- Migrating legacy Hermes/Copilot prompts from `%LOCALAPPDATA%`, `.hermes/prompts/`, `.github/agents/`, etc.
- Deduplicating exact instruction/agent bodies across multiple roots
- Fixing broken path references, folders, or migration artifacts in `.github/`
- Validating prompt library health after bulk edits or migration passes

## When NOT to Use
- Writing new prompt content from scratch (use domain-specific skills)
- Editing prompt content semantically (use review/refactor skills)
- Running automated bulk content rewrites that risk YAML frontmatter corruption without parser validation

## Workflow

### Phase 1: Inventory
1. Enumerate canonical root files: count, size, MD5 hashes
2. Enumerate legacy roots: same metrics
3. Diff by filename and by body hash
4. Record findings in `references/inventory-template.md`

### Phase 2: Migration
1. Copy missing legacy prompts into canonical root
2. Skip exact-body duplicates; record them in manifest
3. Resolve filename collisions deterministically (`-legacy-<md5prefix>`)
4. Update index/count metadata files

### Phase 3: Dedupe
1. Group exact-body duplicates by MD5 across canonical root and legacy roots
2. Keep one copy, delete or archive rest
3. Update cross-references to canonical path
4. Re-verify counts

### Phase 4: Path/Catalog Fixes
1. Audit `.github/**/*.md|yml|yaml` for stale paths
2. Fix broken relative links
3. Confirm every referenced path exists on disk
4. Re-check migration indicators/markers

### Phase 5: Verify
1. Print final file counts, duplicate groups, missing paths
2. Confirm manifest/audit JSONs exist on disk
3. Only then mark complete

## Rules
- Prefer targeted `patch`/`write_file`; no `.bak`/`.backup`/`.old` files.
- Use copy, not move, for migration unless user explicitly authorizes deletion.
- Validate after bulk edits; never assume structured text survived modification.
- Verify on disk; never fabricate counts or file existence.

## Pitfalls
- **Duplicate workflow markers stacking:** Before adding `status: not_started`, frontmatter, or migration markers, check whether the file was already marked. Re-read recent edits to avoid stacking duplicate headers/metadata.
- **Filename vs body collisions:** Two prompts with the same filename may differ in body; same body may live under different filenames. Hash bodies for exact dedupe; use filenames for collision resolution only.
- **Frontmatter corruption from bulk edits:** Regex/line-based replacements on YAML frontmatter often collapse arrays or duplicate keys. After any bulk operation, parse frontmatter with a YAML parser. If corruption is detected, restore from the last clean commit rather than hand-repairing.
- **Verification before claim:** Before reporting success, stat or read back the declared outputs. Subagent summaries are self-reports; confirm files exist and counts match before advancing.
- **Validate the validator before bulk edits:** A large “missing reference” count can come from the audit script, not the repo. Reproduce one reported missing ref directly on disk before creating or rewriting files. Especially watch for path-normalization, backtick stripping, fragment splitting, and empty-line handling bugs in audit tooling.

## Reference

See `references/` for:
- `inventory-template.md` — prompt library inventory schema
- `migration-manifest-template.md` — migration record format
