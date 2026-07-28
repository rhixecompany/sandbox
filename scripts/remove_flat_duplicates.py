"""Remove flat skill duplicates where canonical categorized versions exist.
Reads from the dedupe report to find all ❌ (non-canonical) paths and deletes them.
"""

import asyncio
import os
import shutil

hermes_skills = os.path.join(
    os.environ.get("HOME", os.environ.get("USERPROFILE", "")), "AppData", "Local", "hermes", "skills"
)


async def main():
    # Read the dedupe report
    dedupe_path = os.path.join(
        os.environ.get("HOME", os.environ.get("USERPROFILE", "")), "Desktop", "SandBox", "docs", "dedupe-report.md"
    )

    with open(dedupe_path) as f:
        content = f.read()

    # Find all ❌ entries - they're the non-canonical flat duplicates
    # Pattern: | Skill | path | NNN | ❌ |
    removed = 0
    errors = 0
    skipped = 0

    for line in content.split("\n"):
        if "|" not in line or "❌" not in line:
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) >= 4:
            # parts[1] = skill name, parts[2] = path
            parts[1]
            path_part = parts[2].strip()

            # Skip entries where the ❌ is on the categorized version
            # (some entries have ❌ on categorized, ✅ on flat - need to check)
            if "\\" in path_part:
                # This is a categorized path - skip unless it's ❌ only
                # The ❌ should be on the flat path
                continue

            # Flat path (no backslash) = non-canonical
            skill_dir = os.path.join(hermes_skills, path_part)
            if os.path.isdir(skill_dir) and os.path.exists(os.path.join(skill_dir, "SKILL.md")):
                try:
                    shutil.rmtree(skill_dir)
                    print(f"REMOVED: {skill_dir}")
                    removed += 1
                except Exception as e:
                    print(f"ERROR: {skill_dir} - {e}")
                    errors += 1
            else:
                print(f"SKIPPED (not found): {skill_dir}")
                skipped += 1

    print("\n---")
    print(f"Removed: {removed}")
    print(f"Errors: {errors}")
    print(f"Skipped: {skipped}")


if __name__ == "__main__":
    asyncio.run(main())
