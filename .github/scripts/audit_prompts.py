"""
Phase 1 Audit: Scan all .md files in Prompts/ and .github/prompts/
for formatting, structural, and content issues.
"""
import os, re, json, yaml
from pathlib import Path

SANDBOX = Path("C:/Users/Alexa/Desktop/SandBox")
PROMPTS_DIR = SANDBOX / "Prompts"
GITHUB_PROMPTS_DIR = SANDBOX / ".github/prompts"

all_files = []
for d in [PROMPTS_DIR, GITHUB_PROMPTS_DIR]:
    for f in sorted(d.glob("*.md")):
        all_files.append(f)

print(f"Total files to audit: {len(all_files)}")

issues = []
file_reports = {}

for fpath in all_files:
    rel = str(fpath.relative_to(SANDBOX))
    content = fpath.read_text(encoding="utf-8", errors="replace")
    lines = content.splitlines()
    file_issues = []
    
    # --- FRONTMATTER CHECK ---
    has_frontmatter = content.startswith("---")
    fm_end = -1
    fm_text = ""
    if has_frontmatter:
        # Find closing ---
        for i in range(1, min(60, len(lines))):
            if lines[i].strip() == "---":
                fm_end = i
                fm_text = "\n".join(lines[1:i])
                break
    
    if fm_end == -1 and has_frontmatter:
        file_issues.append({"severity": "HIGH", "type": "frontmatter", "detail": "Unclosed frontmatter fence (no closing --- in first 60 lines)"})
    elif fm_end == -1 and not has_frontmatter:
        file_issues.append({"severity": "HIGH", "type": "frontmatter", "detail": "No YAML frontmatter at all"})
    
    # Double frontmatter fence check (3+ --- in first 60 lines)
    if has_frontmatter:
        fence_count = sum(1 for l in lines[:60] if l.strip() == "---")
        if fence_count >= 3:
            file_issues.append({"severity": "HIGH", "type": "frontmatter", "detail": f"Double frontmatter fences ({fence_count} --- markers in first 60 lines)"})
    
    # Parse YAML frontmatter
    fm_valid = False
    fm_data = None
    if fm_text:
        try:
            fm_data = yaml.safe_load(fm_text)
            if isinstance(fm_data, dict):
                fm_valid = True
            else:
                file_issues.append({"severity": "HIGH", "type": "frontmatter", "detail": "Frontmatter YAML does not parse as a mapping"})
        except yaml.YAMLError as e:
            file_issues.append({"severity": "HIGH", "type": "frontmatter", "detail": f"Frontmatter YAML parse error: {e}"})
    
    # Check required fields
    if fm_valid and isinstance(fm_data, dict):
        required = ["description"]
        for field in required:
            if field not in fm_data:
                file_issues.append({"severity": "MEDIUM", "type": "frontmatter", "detail": f"Missing required frontmatter field: {field}"})
    
    # --- SKILLS: DEPENDENCY-STYLE PROSE ---
    for i, line in enumerate(lines[:60], 1):
        if re.match(r'^skills:\s*$', line.strip()):
            # Check next few lines for prose-style entries
            for j in range(i, min(i+10, len(lines))):
                next_line = lines[j].strip()
                if next_line and not next_line.startswith('#') and not next_line.startswith('-') and next_line != 'skills:':
                    if ':' in next_line and not next_line.startswith('-'):
                        file_issues.append({"severity": "MEDIUM", "type": "skills-prose", "detail": f"Line {j+1}: skills: section has dependency-style prose instead of list: '{next_line[:80]}'"})
                    break
    
    # --- FORMATTING ---
    # Trailing whitespace
    trailing_ws = [i+1 for i, l in enumerate(lines) if l != l.rstrip() and l.strip()]
    if trailing_ws:
        file_issues.append({"severity": "LOW", "type": "formatting", "detail": f"Trailing whitespace on {len(trailing_ws)} lines (first: {trailing_ws[:3]})"})
    
    # Mixed line endings
    if '\r\n' in content and '\n' in content.replace('\r\n', ''):
        file_issues.append({"severity": "LOW", "type": "formatting", "detail": "Mixed line endings (CRLF + LF)"})
    
    # Tab characters
    tab_lines = [i+1 for i, l in enumerate(lines) if '\t' in l]
    if tab_lines:
        file_issues.append({"severity": "LOW", "type": "formatting", "detail": f"Tab characters on {len(tab_lines)} lines"})
    
    # --- STRUCTURAL ---
    # Empty file
    if len(lines) == 0 or all(l.strip() == '' for l in lines):
        file_issues.append({"severity": "HIGH", "type": "structural", "detail": "File is empty or all whitespace"})
    
    # Heading hierarchy (check for skipped levels)
    headings = [(i+1, l) for i, l in enumerate(lines) if re.match(r'^#{1,6}\s', l)]
    prev_level = 0
    for hline, htext in headings:
        level = len(re.match(r'^(#+)', htext).group(1))
        if prev_level > 0 and level > prev_level + 1:
            file_issues.append({"severity": "MEDIUM", "type": "structure", "detail": f"Line {hline}: Heading level skip (h{prev_level} -> h{level}): '{htext[:60]}'"})
        prev_level = level
    
    # Duplicate headings
    heading_texts = [re.sub(r'^#+\s*', '', h[1]).strip() for h in headings]
    seen = set()
    for ht in heading_texts:
        if ht.lower() in seen:
            file_issues.append({"severity": "MEDIUM", "type": "structure", "detail": f"Duplicate heading: '{ht}'"})
        seen.add(ht.lower())
    
    # --- CONTENT ---
    # TODO/FIXME markers
    todo_lines = [(i+1, l) for i, l in enumerate(lines) if re.search(r'\b(TODO|FIXME|HACK|XXX)\b', l) and not l.strip().startswith('#')]
    if todo_lines:
        file_issues.append({"severity": "LOW", "type": "content", "detail": f"TODO/FIXME markers on {len(todo_lines)} lines"})
    
    # Broken markdown links
    broken_links = []
    for i, line in enumerate(lines):
        for m in re.finditer(r'\[([^\]]*)\]\(([^)]*)\)', line):
            url = m.group(2)
            if url.startswith("http") and not url.startswith(("http://", "https://")):
                broken_links.append((i+1, url))
            elif url == "":
                broken_links.append((i+1, "(empty)"))
    if broken_links:
        file_issues.append({"severity": "MEDIUM", "type": "content", "detail": f"Potentially broken links: {broken_links[:3]}"})
    
    # --- EXTENSION CHECK ---
    fname = fpath.name
    if fpath.parent == PROMPTS_DIR and not fname.endswith(".prompts.md"):
        file_issues.append({"severity": "LOW", "type": "naming", "detail": f"File in Prompts/ doesn't use .prompts.md extension"})
    if fpath.parent == GITHUB_PROMPTS_DIR and not fname.endswith(".prompt.md"):
        file_issues.append({"severity": "LOW", "type": "naming", "detail": f"File in .github/prompts/ doesn't use .prompt.md extension"})
    
    # --- ZOD EMPTY FILE ---
    if fname == "zod-schema-generation.prompt.md" and len(content.strip()) == 0:
        file_issues.append({"severity": "HIGH", "type": "content", "detail": "File is completely empty (0 bytes)"})
    
    file_reports[rel] = {
        "lines": len(lines),
        "size": fpath.stat().st_size,
        "has_frontmatter": has_frontmatter,
        "fm_valid": fm_valid,
        "fm_fields": list(fm_data.keys()) if isinstance(fm_data, dict) else [],
        "headings": len(headings),
        "issues": file_issues,
        "issue_count": len(file_issues),
        "high": sum(1 for i in file_issues if i["severity"] == "HIGH"),
        "medium": sum(1 for i in file_issues if i["severity"] == "MEDIUM"),
        "low": sum(1 for i in file_issues if i["severity"] == "LOW"),
    }
    issues.extend([(rel, i) for i in file_issues])

# --- SUMMARY ---
print(f"\n{'='*60}")
print(f"AUDIT SUMMARY")
print(f"{'='*60}")
print(f"Files audited: {len(all_files)}")
print(f"Total issues: {len(issues)}")
print(f"  HIGH:   {sum(1 for _,i in issues if i['severity']=='HIGH')}")
print(f"  MEDIUM: {sum(1 for _,i in issues if i['severity']=='MEDIUM')}")
print(f"  LOW:    {sum(1 for _,i in issues if i['severity']=='LOW')}")

print(f"\n--- Files with HIGH issues ---")
for rel, fr in sorted(file_reports.items()):
    if fr["high"] > 0:
        print(f"  {rel}: {fr['high']} HIGH")
        for i in fr["issues"]:
            if i["severity"] == "HIGH":
                print(f"    - [{i['type']}] {i['detail']}")

print(f"\n--- Files with MEDIUM issues ---")
for rel, fr in sorted(file_reports.items()):
    if fr["medium"] > 0:
        print(f"  {rel}: {fr['medium']} MEDIUM")
        for i in fr["issues"]:
            if i["severity"] == "MEDIUM":
                print(f"    - [{i['type']}] {i['detail']}")

print(f"\n--- Files with LOW issues (first 10) ---")
count = 0
for rel, fr in sorted(file_reports.items()):
    if fr["low"] > 0 and count < 10:
        print(f"  {rel}: {fr['low']} LOW")
        for i in fr["issues"]:
            if i["severity"] == "LOW":
                print(f"    - [{i['type']}] {i['detail']}")
        count += 1

# Write JSON for later phases
output = {
    "summary": {
        "total_files": len(all_files),
        "total_issues": len(issues),
        "high": sum(1 for _,i in issues if i["severity"]=="HIGH"),
        "medium": sum(1 for _,i in issues if i["severity"]=="MEDIUM"),
        "low": sum(1 for _,i in issues if i["severity"]=="LOW"),
    },
    "files": file_reports
}
with open(SANDBOX / "docs" / "audit_results.json", "w") as f:
    json.dump(output, f, indent=2)
print(f"\nFull results written to docs/audit_results.json")
