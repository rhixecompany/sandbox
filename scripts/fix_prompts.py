#!/usr/bin/env python3
"""
Batch fix script for prompt files.
Fixes: missing triggers, frontmatter issues, tags format, legacy sections, dependency prefixes.
"""

import re
from pathlib import Path

import yaml

PROMPTS_DIR = Path("C:/Users/Alexa/Desktop/SandBox/prompts")
SHARED_TEMPLATES_DIR = PROMPTS_DIR / "templates" / "_shared"


# Load shared templates
def load_shared_template(name):
    path = SHARED_TEMPLATES_DIR / name
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""


FRONTMATTER_TEMPLATE = load_shared_template("frontmatter.md")
RULES_CORE = load_shared_template("rules-core.md")
DEPS_CORE = load_shared_template("deps-core.md")
SKILLS_TABLE_CORE = load_shared_template("skills-table-core.md")


def parse_frontmatter(content):
    """Parse YAML frontmatter from content."""
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None, content
    fm_text = match.group(1)
    body = content[match.end() :].lstrip("\n")
    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError:
        fm = {}
    return fm, body


def format_frontmatter(fm):
    """Format frontmatter as YAML string."""
    return yaml.dump(fm, sort_keys=False, default_flow_style=False, allow_unicode=True)


def fix_tags_format(tags):
    """Convert tags to proper YAML list format."""
    if not tags:
        return ["hermes"]
    if isinstance(tags, str):
        # Try to parse as Python list or comma-separated
        if tags.startswith("[") and tags.endswith("]"):
            try:
                import ast

                return ast.literal_eval(tags)
            except Exception:
                pass
        return [t.strip() for t in tags.split(",") if t.strip()]
    if isinstance(tags, list):
        return [str(t) for t in tags if t]
    return ["hermes"]


def standardize_dep_prefixes(deps):
    """Convert command:/tool: prefixes to skill: in dependencies."""
    if not deps:
        return []
    standardized = []
    for dep in deps:
        if isinstance(dep, str):
            if dep.startswith("command:") or dep.startswith("tool:"):
                # Extract the skill name
                name = dep.split(":", 1)[1]
                standardized.append(f"skill:{name}")
            elif dep.startswith("prompt:") or dep.startswith("skill:"):
                standardized.append(dep)
            else:
                standardized.append(f"skill:{dep}")
        else:
            standardized.append(dep)
    return standardized


def generate_trigger(name):
    """Generate trigger from name."""
    if not name:
        return ""
    # Ensure it starts with /
    if not name.startswith("/"):
        return f"/{name}"
    return name


def fix_prompt_file(filepath, dry_run=False):
    """Fix a single prompt file."""
    content = filepath.read_text(encoding="utf-8")
    original = content

    fm, body = parse_frontmatter(content)
    if fm is None:
        return {"path": str(filepath), "status": "error", "reason": "No frontmatter"}

    changes = []

    # 1. Fix name - derive from filename if missing
    if not fm.get("name"):
        name = filepath.stem.replace(".prompt", "")
        fm["name"] = name
        changes.append(f"Added name: {name}")

    # 2. Fix trigger - derive from name if missing
    if not fm.get("trigger"):
        trigger = generate_trigger(fm["name"])
        fm["trigger"] = trigger
        changes.append(f"Added trigger: {trigger}")

    # 3. Fix version
    if not fm.get("version"):
        fm["version"] = "1.0.0"
        changes.append("Added version: 1.0.0")

    # 4. Fix title - use name as fallback
    if not fm.get("title"):
        title = fm["name"].replace("-", " ").title()
        fm["title"] = title
        changes.append(f"Added title: {title}")

    # 5. Fix description
    if not fm.get("description"):
        fm["description"] = f"Prompt for {fm['title'].lower()}"
        changes.append("Added description")

    # 6. Fix tags
    old_tags = fm.get("tags", [])
    new_tags = fix_tags_format(old_tags)
    if "hermes" not in new_tags:
        new_tags.append("hermes")
    if set(old_tags) != set(new_tags):
        fm["tags"] = new_tags
        changes.append(f"Fixed tags: {old_tags} -> {new_tags}")

    # 7. Fix author/license
    if not fm.get("author"):
        fm["author"] = "Hermes Agent"
        changes.append("Added author: Hermes Agent")
    if not fm.get("license"):
        fm["license"] = "MIT"
        changes.append("Added license: MIT")

    # 8. Fix dependencies - standardize prefixes
    old_deps = fm.get("dependencies", [])
    new_deps = standardize_dep_prefixes(old_deps)
    if old_deps != new_deps:
        fm["dependencies"] = new_deps
        changes.append("Standardized dependencies")

    # 9. Fix skills - ensure it's a list
    if "skills" in fm and not isinstance(fm["skills"], list):
        fm["skills"] = [fm["skills"]]
        changes.append("Fixed skills to be list")

    # 10. Remove legacy section from body
    legacy_pattern = r"\n##\s*Legacy Prompt Details.*?(?=\n##|\n###|\Z)"
    if re.search(legacy_pattern, body, re.DOTALL | re.IGNORECASE):
        body = re.sub(legacy_pattern, "", body, flags=re.DOTALL | re.IGNORECASE)
        changes.append("Removed legacy section")

    # Also check for ### Legacy
    legacy_pattern_h3 = r"\n###\s*Legacy Prompt Details.*?(?=\n##|\n###|\Z)"
    if re.search(legacy_pattern_h3, body, re.DOTALL | re.IGNORECASE):
        body = re.sub(legacy_pattern_h3, "", body, flags=re.DOTALL | re.IGNORECASE)
        changes.append("Removed legacy H3 section")

    # 11. Add reference to shared rules if not present
    if "rules-core.md" not in body and "Core Rules" not in body:
        # Add after first major section or at end
        pass  # Skip for now, let user decide

    # Rebuild content
    new_content = "---\n" + format_frontmatter(fm) + "---\n" + body

    # Normalize line endings
    new_content = new_content.replace("\r\n", "\n")

    if new_content != original:
        if not dry_run:
            filepath.write_text(new_content, encoding="utf-8")
        return {"path": str(filepath), "status": "fixed", "changes": changes}

    return {"path": str(filepath), "status": "ok", "changes": []}


def main():
    import sys

    dry_run = "--dry-run" in sys.argv

    # Find all .prompt.md files
    files = list(PROMPTS_DIR.rglob("*.prompt.md"))
    print(f"Found {len(files)} prompt files")

    results = []
    for f in files:
        result = fix_prompt_file(f, dry_run=dry_run)
        results.append(result)
        if result["status"] == "fixed":
            print(f"  FIXED: {result['path']} - {', '.join(result['changes'])}")
        elif result["status"] == "error":
            print(f"  ERROR: {result['path']} - {result['reason']}")

    fixed = sum(1 for r in results if r["status"] == "fixed")
    errors = sum(1 for r in results if r["status"] == "error")
    ok = sum(1 for r in results if r["status"] == "ok")

    print(f"\nSummary: {fixed} fixed, {ok} ok, {errors} errors")

    if dry_run:
        print("\nDRY RUN - no files modified. Run without --dry-run to apply.")


if __name__ == "__main__":
    main()
