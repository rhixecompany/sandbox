from pathlib import Path
import re

files = [
    "Prompts/agents-fix.prompts.md",
    "Prompts/bash-scripts-fix.prompts.md",
    "Prompts/dev-init.prompts.md",
    "Prompts/general.prompts.md",
    "Prompts/prompts-fix.prompts.md",
    "Prompts/repo-management.prompts.md",
    "Prompts/repo.prompts.md",
    "Prompts/skills-fix.prompts.md",
    "Prompts/workspace-consolidate.prompts.md",
]

HEADER_SKILLS = {
    "introspection-only-general",
    "no-git-delete",
    "no-net-fetch",
    "skills-tools-preflight-check",
}

for p in files:
    path = Path(p)
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        print(f"MALFORMED\t{p}")
        continue
    fm = parts[1]
    body = parts[2]
    lines = fm.splitlines()
    skills = []
    skills_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("skills:"):
            skills_idx = i
            skills.append(line)
            continue
        if skills_idx is not None and line.startswith("    - "):
            items = line[6:].strip()
            if items:
                skills.append(items)
            continue
        if skills_idx is not None and (not line.startswith("    ") or line.strip() == "---"):
            skills_idx = None
            continue
    seen = []
    for item in skills[1:]:
        if item not in seen:
            seen.append(item)
    ordered = list(HEADER_SKILLS) + [item for item in seen if item not in HEADER_SKILLS]
    new_lines = []
    if skills:
        new_lines.append(skills[0])
        new_lines.extend(f"    - {item}" for item in ordered)
    else:
        new_lines.append("skills:")
        new_lines.extend(f"    - {item}" for item in ordered)
    # replace old skills block
    start = None
    end = None
    for i, line in enumerate(lines):
        if line.strip().startswith("skills:"):
            start = i
        if start is not None and i > start and line.strip() in {"tags:", "dependencies:", "mode:", "system:", "description:", "trigger:"}:
            end = i
            break
    if start is None:
        lines[0:0] = new_lines
    else:
        if end is None:
            end = len(lines)
        lines[start:end] = new_lines
    new_fm = "\n".join(lines)
    new_text = f"---{new_fm}---{body}"
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        print(f"UPDATED\t{p}")
    else:
        print(f"NOOP\t{p}")
