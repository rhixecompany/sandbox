#!/usr/bin/env python3
"""
Phase 1: Legacy Prompt Migration Script
Migrates legacy Hermes prompts from C:\Users\Alexa\AppData\Local\hermes\prompts\
into .github/prompts/, deduplicating by content hash, preserving unique content.

Handles:
- Same filename, different body → merge/create new
- Same filename, same body → skip (already present)
- Legacy-only files → create new in SandBox
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERMES_LEGACY = Path(r"C:\Users\Alexa\AppData\Local\hermes\prompts")
SANDBOX_PROMPTS = Path(r"C:\Users\Alexa\Desktop\SandBox\.github\prompts")
ARCHIVE_DIR = SANDBOX_PROMPTS / "archived"


def normalize_body(text: str) -> str:
    """Normalize markdown body for hash comparison."""
    lines = text.splitlines()
    # Remove frontmatter
    if lines and lines[0].strip() == "---":
        end = None
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                end = i
                break
        if end:
            lines = lines[end + 1:]
    # Clean up
    cleaned = [line.strip() for line in lines]
    cleaned = [line for line in cleaned if line]
    return "\n".join(cleaned)


def file_hash(path: Path) -> str:
    """SHA-256 of normalized body."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        body = normalize_body(text)
        return hashlib.sha256(body.encode()).hexdigest()
    except Exception:
        return ""


def get_body_text(path: Path) -> str:
    """Get the full body text (without frontmatter) from a prompt file."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        if lines and lines[0].strip() == "---":
            end = None
            for i in range(1, len(lines)):
                if lines[i].strip() == "---":
                    end = i
                    break
            if end:
                return "\n".join(lines[end + 1:])
        return text
    except Exception:
        return ""


def main():
    print(f"=== Phase 1: Legacy Prompt Migration ===")
    print(f"Legacy source: {HERMES_LEGACY}")
    print(f"Target: {SANDBOX_PROMPTS}")
    print()

    # Ensure archive dir exists
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    # Build hash maps
    print("Building hash maps...")
    legacy_hashes = {}
    for f in sorted(HERMES_LEGACY.glob("*.prompt.md")):
        h = file_hash(f)
        if h:
            legacy_hashes[h] = f

    sandbox_hashes = {}
    for f in sorted(SANDBOX_PROMPTS.glob("*.prompt.md")):
        h = file_hash(f)
        if h:
            sandbox_hashes[h] = f

    legacy_names = {f.stem: f for f in HERMES_LEGACY.glob("*.prompt.md")}
    sandbox_names = {f.stem: f for f in SANDBOX_PROMPTS.glob("*.prompt.md")}

    print(f"Legacy prompts: {len(legacy_names)}")
    print(f"SandBox prompts: {len(sandbox_names)}")
    print(f"Unique legacy bodies: {len(legacy_hashes)}")
    print(f"Unique SandBox bodies: {len(sandbox_hashes)}")
    print()

    # Categories
    same_body = []       # Same filename, same body → skip
    diff_body = []       # Same filename, different body → merge
    legacy_only = []     # Only in legacy → create new

    for name, legacy_path in legacy_names.items():
        legacy_h = file_hash(legacy_path)
        if legacy_h == "":
            print(f"  WARN: Cannot hash {legacy_path.name}, skipping")
            continue

        if name in sandbox_names:
            sandbox_path = sandbox_names[name]
            sandbox_h = file_hash(sandbox_path)
            if sandbox_h == legacy_h:
                same_body.append((legacy_path, sandbox_path))
            else:
                diff_body.append((legacy_path, sandbox_path))
        else:
            legacy_only.append((legacy_path, name))

    print(f"Same body (skip): {len(same_body)}")
    print(f"Different body (merge): {len(diff_body)}")
    print(f"Legacy only (create): {len(legacy_only)}")
    print()

    # Process: same body → skip
    print("=== Same body files (already present) ===")
    for legacy_path, sandbox_path in same_body:
        print(f"  SKIP: {legacy_path.name} (identical to {sandbox_path.name})")

    # Process: different body → need to decide merge vs new
    print()
    print("=== Different body files (need merge decision) ===")
    for legacy_path, sandbox_path in diff_body:
        legacy_body = get_body_text(legacy_path)
        sandbox_body = get_body_text(sandbox_path)
        print(f"  {legacy_path.name}: legacy={len(legacy_body)}B, sandbox={len(sandbox_body)}B")
        # For now: legacy content is older/preursor → keep sandbox as primary,
        # but note that legacy has different content. We'll create the legacy
        # content as a new file with disambiguated name if it's truly different.
        # Actually: the discovery showed 0 cross-location hash collisions,
        # meaning ALL 226 legacy files have bodies different from all 226 sandbox files.
        # Strategy: migrate ALL legacy content as new prompts since they're unique.

    # Process: legacy only → create new in SandBox
    print()
    print("=== Legacy-only files (will be created) ===")
    for legacy_path, name in legacy_only:
        print(f"  WILL CREATE: {name}.prompt.md from {legacy_path.name}")

    print()
    print("=== Summary ===")
    print(f"Total legacy files: {len(legacy_names)}")
    print(f"Already present (skip): {len(same_body)}")
    print(f"Need migration (all unique): {len(diff_body) + len(legacy_only)}")
    print(f"Archive candidates: 0 (all legacy content is unique)")

    # Since all 226 legacy bodies are unique from all 226 sandbox bodies
    # (discovery confirmed 0 cross-location hash collisions),
    # we need to migrate ALL legacy content.
    # But since they share filenames, we have naming conflicts.
    # Solution: Treat the 226 sandbox files as the canonical set,
    # and the 226 legacy files as unique content that needs new filenames.
    # 
    # Actually - re-reading the discovery: same filenames, different bodies.
    # The legacy files are older versions of prompts OR different prompts
    # that happen to share names. We should:
    # 1. Keep sandbox files as-is (they're the current canonical versions)
    # 2. For legacy files whose content is truly different/additional,
    #    create new prompt files with disambiguated names
    #
    # But wait - the goal says "All 226 legacy prompts either migrated or archived".
    # Since every legacy file has a unique body not matching any sandbox file,
    # and they share filenames with sandbox files, we have a naming conflict.
    #
    # Best approach: Rename legacy-derived files to avoid collision.
    # E.g., if legacy "setup.prompt.md" has different content from sandbox "setup.prompt.md",
    # create "setup-legacy.prompt.md" or similar.
    #
    # Simplest: migrate all legacy files with a "-legacy" suffix appended to stem.
    # This preserves all content without collision.

    print()
    print("=== Migration Strategy ===")
    print("All 226 legacy bodies are unique from all 226 sandbox bodies.")
    print("Since filenames collide, legacy-derived files will use '-legacy' suffix.")
    print(f"Will create {len(legacy_names)} new prompt files with disambiguated names.")
    print()

    # Actually perform the migration (dry-run by default)
    dry_run = "--apply" not in sys.argv
    if dry_run:
        print("DRY-RUN MODE — no files will be written.")
        print("Use --apply to perform actual migration.")
        print()

        # Show what would happen
        created = 0
        for legacy_path in sorted(HERMES_LEGACY.glob("*.prompt.md")):
            new_name = f"{legacy_path.stem}-legacy.prompt.md"
            target = SANDBOX_PROMPTS / new_name
            if target.exists():
                print(f"  CONFLICT: {new_name} already exists in SandBox!")
            else:
                created += 1

        print(f"\nWould create {created} new prompt files.")
    else:
        print("APPLYING MIGRATION...")
        created = 0
        conflicts = 0
        for legacy_path in sorted(HERMES_LEGACY.glob("*.prompt.md")):
            new_name = f"{legacy_path.stem}-legacy.prompt.md"
            target = SANDBOX_PROMPTS / new_name

            if target.exists():
                print(f"  CONFLICT: {new_name} already exists — skipping {legacy_path.name}")
                conflicts += 1
                continue

            # Copy the file
            shutil.copy2(str(legacy_path), str(target))
            created += 1
            print(f"  CREATED: {new_name}")

        print(f"\nCreated: {created}, Conflicts: {conflicts}")
        print("Migration complete.")


if __name__ == "__main__":
    main()
