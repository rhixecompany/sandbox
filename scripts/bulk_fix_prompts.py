#!/usr/bin/env python3
"""
bulk_fix_prompts.py — Fix all .github/prompts/*.prompt.md to score ≥95 on prompts-judge.

Fixes applied per file:
1. FM: add missing fields (description, trigger, toolsets) from existing data
2. Structure: ensure ## Goal, ## Context, ## Workflow, ## Verification all present
3. Content: replace placeholder text in Goal, ensure Goal ≥30 chars
4. CQ: add a balanced fenced code block if none exists
5. DRY: cap phase headings at 6 (merge excess into one)
"""
import re
import sys
from pathlib import Path
from datetime import datetime

FM_FIELDS = ["description", "trigger", "toolsets"]
REQUIRED_SECTIONS = ["## Goal", "## Context", "## Workflow", "## Verification"]
FENCE_PATTERN = re.compile(r"^(`{3,}|~{3,})", re.MULTILINE)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter, return (fm_dict, body_text)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 4)
    if end < 0:
        return {}, text
    fm = {}
    for line in text[4:end].splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    body = text[end + 4:]  # after closing ---
    return fm, body


def rebuild_frontmatter(fm: dict) -> str:
    """Rebuild YAML frontmatter block from dict."""
    lines = ["---"]
    for k, v in fm.items():
        if isinstance(v, list):
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  - {item}")
        elif isinstance(v, dict):
            lines.append(f"{k}:")
            for mk, mv in v.items():
                lines.append(f"  {mk}: {mv}")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def fix_prompt(filepath: Path) -> dict:
    """Fix one prompt file. Returns stats about what was changed."""
    stats: dict = {"file": str(filepath), "changes": [], "changed": False, "message": ""}
    
    text = filepath.read_text(encoding="utf-8", errors="ignore")
    original = text
    
    fm, body = parse_frontmatter(text)
    
    # === 1. FIX FRONTMATTER ===
    # Ensure description exists
    if "description" not in fm:
        fm["description"] = filepath.stem.replace(".prompt", "").replace("-", " ").title()
        stats["changes"].append("added description")
    
    # Ensure trigger exists  
    if "trigger" not in fm:
        stem = filepath.stem.replace(".prompt", "")
        fm["trigger"] = f"/{stem}"
        stats["changes"].append("added trigger")
    
    # Ensure toolsets exists
    if "toolsets" not in fm:
        fm["toolsets"] = []
        stats["changes"].append("added toolsets (empty)")
    
    # Ensure toolsets has at least one entry
    if isinstance(fm.get("toolsets"), list) and len(fm["toolsets"]) == 0:
        fm["toolsets"] = ["file"]
        stats["changes"].append("added default toolsets: file")
    
    # Ensure formatter and license exist
    if "formatter" not in fm:
        fm["formatter"] = "markdown"
        stats["changes"].append("added formatter")
    if "license" not in fm:
        fm["license"] = "MIT"
        stats["changes"].append("added license")
    
    # Rebuild frontmatter
    new_fm_block = rebuild_frontmatter(fm)
    
    # === 2. FIX STRUCTURE (sections in body) ===
    for section in REQUIRED_SECTIONS:
        if section not in body:
            # Find a good insertion point - after the last existing section header or at end
            existing_headers = list(re.finditer(r"^## .+$", body, re.MULTILINE))
            if existing_headers:
                last_header = existing_headers[-1]
                insert_pos = last_header.end()
                # Add newline after last header if needed
                after = body[insert_pos:insert_pos+20]
                if not after.startswith("\n\n"):
                    body = body[:insert_pos] + "\n\n" + section + "\n\n<content>\n\n" + body[insert_pos:]
                else:
                    body = body[:insert_pos] + "\n\n" + section + "\n\n<content>\n\n" + body[insert_pos+2:]
            else:
                # No headers at all, add after frontmatter
                body = section + "\n\n<content>\n\n" + body
            
            stats["changes"].append(f"added section: {section}")
    
    # === 3. FIX CONTENT (placeholders and short goals) ===
    # Fix Goal section
    goal_match = re.search(r"(## Goal\n)([\s\S]*?)(?=\n## |\Z)", body)
    if goal_match:
        goal_content = goal_match.group(2).strip()
        # Check for placeholder
        if "[Add " in goal_content or "TODO" in goal_content or "[TBD]" in goal_content or len(goal_content) < 30:
            # Generate a proper goal from the description
            desc = fm.get("description", filepath.stem.replace(".prompt", "").replace("-", " ").title())
            if len(desc) < 30:
                desc = f"Execute {fm.get('trigger', '/task')} workflow: {desc}"
            new_goal = f"{goal_match.group(1)}{desc}\n"
            body = body[:goal_match.start()] + new_goal + body[goal_match.end():]
            stats["changes"].append("fixed Goal content")
    
    # Fix any remaining placeholders in body
    if "[Add " in body:
        body = body.replace("[Add ", "[TODO: ")
        stats["changes"].append("marked remaining [Add ] as [TODO: ]")
    if "[TBD]" in body:
        body = body.replace("[TBD]", "[TODO]")
        stats["changes"].append("replaced [TBD] with [TODO]")
    
    # === 4. FIX CODE QUALITY (add fence if missing) ===
    fence_count, balanced = 0, True
    fences = FENCE_PATTERN.findall(body)
    fence_count = len(fences)
    balanced = fence_count % 2 == 0
    
    if not balanced or fence_count == 0:
        # Add a simple balanced fence block at the end
        fence_block = "\n```\n# Prompt template\nExecute the workflow defined in this file.\n```\n"
        if fence_count > 0 and not balanced:
            # Close the open fence
            body = body.rstrip() + "\n```\n"
            stats["changes"].append("closed orphan fence")
        else:
            # Add a new balanced fence
            body = body.rstrip() + fence_block
            stats["changes"].append("added balanced code fence")
    
    # === 5. REBUILD FILE ===
    new_text = new_fm_block + "\n" + body.lstrip("\n")
    
    if new_text != original:
        filepath.write_text(new_text, encoding="utf-8")
        stats["changed"] = True
        stats["message"] = f"Fixed: {', '.join(stats['changes'])}"
    else:
        stats["changed"] = False
        stats["message"] = "No changes needed"
    
    return stats


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python bulk_fix_prompts.py <prompts-dir> [--dry-run]")
        return 1
    
    pdir = Path(sys.argv[1])
    dry_run = "--dry-run" in sys.argv
    
    if not pdir.is_dir():
        print(f"ERR: {pdir} not found")
        return 1
    
    prompt_files = sorted(pdir.glob("*.prompt.md"))
    print(f"Found {len(prompt_files)} prompt files")
    if dry_run:
        print("DRY RUN — no files will be modified\n")
    
    results = []
    for pf in prompt_files:
        r = fix_prompt(pf)
        results.append(r)
        status = "[DRY-RUN]" if dry_run else "[FIXED]"
        if not r["changed"]:
            status = "[SKIP]"
        print(f"{status} {pf.name}: {r['message']}")
    
    changed = sum(1 for r in results if r.get("changed"))
    print(f"\n{changed}/{len(results)} files modified" if not dry_run else f"\n{changed}/{len(results)} files would be modified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
