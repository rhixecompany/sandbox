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
title: Simplify
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

## Pitfalls

- **Windows file locking on `.git/` dirs**: Plugin dirs with `.git/objects/pack/*.idx` files resist `shutil.rmtree()` and `rm -rf` with `[WinError 5] Access is denied`. Fix: `chmod -R +w <dir>` first, then `rm -rf`. Hermes root plugins are NOT affected because they're loaded into agent memory at session start (pack files stay locked).
- **Empty dirs can't always be removed**: Windows may report "Device or resource busy" on directories that are empty but still held open by a shell or explorer handle. The content is gone — just the directory inode is stuck. Not a real failure.
- **Distance check matters**: Always verify the hermes root items are untouched BEFORE deleting from SandBox. The hermes root is the canonical store — SandBox `.github/` is the disposable mirror.
- **Dotfiles/manifests are SandBox metadata, not skills**: In `.github/skills/`, entries like `.hub/`, `.curator_backups/`, `.curator_state`, `.usage.json`, `.bundled_manifest` are Hermes internal state files, not skill directories. Never classify these as duplicates even if a similarly-named dir appears in the hermes root.
- **Dotfiles/manifests in skills dir** — Hermes skills dir contains `.hub/`, `.curator_backups/`, `.curator_state`, `.usage.json`, `.bundled_manifest`. These are NOT skill directories — exclude them from duplicate detection. Filter: skip any entry starting with `.`.
- **Canonical location for Hermes** — `~/AppData/Local/hermes/` is the authoritative location for skills/hooks/plugins. SandBox `.github/` subdirs are community/reference copies that should be deduped against the root, not the other way around.
- **Verify before claiming** — After deletion, always `ls` both the source (to confirm only unique items remain) and the canonical location (to confirm nothing was accidentally deleted there).

## References

- [`references/hermes-artifact-dedup.md`](references/hermes-artifact-dedup.md) — Concrete procedure for deduplicating hermes skills/hooks/plugins between SandBox `.github/` and `~/AppData/Local/hermes/` root. Includes Windows file-locking workaround, preservation rules, and one-shot verification command.

## Verification Checklist

- [ ] All tasks completed
- [ ] Output verified
- [ ] Edge cases handled
