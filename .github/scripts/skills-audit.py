"""Audit all skills for remaining issues - Windows path."""
import os, re, sys

# Use the actual Hermes install path
home = os.environ.get("USERPROFILE", "C:\\Users\\Alexa")
skill_dir = os.path.join(home, "AppData", "Local", "hermes", "skills")
print(f"Scanning: {skill_dir}")

if not os.path.isdir(skill_dir):
    print(f"ERROR: {skill_dir} does not exist")
    sys.exit(1)

counts = {"total": 0, "fm": 0, "when": 0, "workflow": 0, "checklist": 0, "bp": 0, "h1_code": 0}
details = {"missing_when": [], "missing_wf": [], "missing_vc": [], "missing_bp": [], "h1_code": []}

for root, dirs, files in os.walk(skill_dir):
    parts = root.replace("\\", "/").split("/")
    if "templates" in parts:
        continue
    if "SKILL.md" in files:
        path = os.path.join(root, "SKILL.md")
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {path}: {e}", file=sys.stderr)
            continue

        counts["total"] += 1
        rel = path.replace(skill_dir, "").lstrip("/\\").replace("\\", "/")

        # Frontmatter
        if content.startswith("---"):
            counts["fm"] += 1

        # When to Use
        if re.search(r"^## When to (Use|use)\b", content, re.MULTILINE):
            counts["when"] += 1
        else:
            details["missing_when"].append(rel)

        # Workflow / Process / Pipeline / Phases / Decision Flow / The Process
        wf_pattern = r"^## (Workflow|Process|Pipeline|Phases|The Process|Decision Flow)\b"
        if re.search(wf_pattern, content, re.MULTILINE):
            counts["workflow"] += 1
        else:
            details["missing_wf"].append(rel)

        # Verification Checklist
        if "## Verification Checklist" in content or "## Checklist" in content:
            counts["checklist"] += 1
        else:
            details["missing_vc"].append(rel)

        # Best Practices
        if re.search(r"^## Best Practices", content, re.MULTILINE):
            counts["bp"] += 1
        else:
            details["missing_bp"].append(rel)

        # H1 inside code blocks
        code_blocks = re.findall(r"```[\s\S]*?```", content)
        for cb in code_blocks:
            if re.search(r"^# ", cb, re.MULTILINE):
                counts["h1_code"] += 1
                details["h1_code"].append(rel)
                break

# Print results
print(f"\nTotal: {counts['total']}")
print(f"Frontmatter: {counts['fm']}/176")
print(f"When to Use: {counts['when']}/176 | missing: {len(details['missing_when'])}")
print(f"Workflow: {counts['workflow']}/176 | missing: {len(details['missing_wf'])}")
print(f"Verification Checklist: {counts['checklist']}/176 | missing: {len(details['missing_vc'])}")
print(f"Best Practices: {counts['bp']}/176 | missing: {len(details['missing_bp'])}")
print(f"H1 in code blocks: {counts['h1_code']}")

if details["missing_when"]:
    print(f"\n=== MISSING When to Use ({len(details['missing_when'])}) ===")
    for s in details["missing_when"]:
        print(f"  {s}")

if details["missing_wf"]:
    print(f"\n=== MISSING Workflow ({len(details['missing_wf'])}) ===")
    for s in details["missing_wf"][:30]:
        print(f"  {s}")
    if len(details["missing_wf"]) > 30:
        print(f"  ... and {len(details['missing_wf']) - 30} more")

if details["missing_vc"]:
    print(f"\n=== MISSING Verification Checklist ({len(details['missing_vc'])}) ===")
    for s in details["missing_vc"][:30]:
        print(f"  {s}")
    if len(details["missing_vc"]) > 30:
        print(f"  ... and {len(details['missing_vc']) - 30} more")

if details["missing_bp"]:
    print(f"\n=== MISSING Best Practices ({len(details['missing_bp'])}) ===")
    for s in details["missing_bp"][:15]:
        print(f"  {s}")
    if len(details["missing_bp"]) > 15:
        print(f"  ... and {len(details['missing_bp']) - 15} more")

if details["h1_code"]:
    print(f"\n=== H1 inside code blocks ({len(details['h1_code'])}) ===")
    for s in details["h1_code"]:
        print(f"  {s}")
