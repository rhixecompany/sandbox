#!/usr/bin/env python3
"""
Prompt Library Enhancement Analyzer
Scans all .prompt.md files and reports:
- Frontmatter completeness & consistency
- DRY compliance (inline vs shared refs)
- Best-practice gaps
- Structural issues
- Template reference health
"""
import os, re, json, yaml
from pathlib import Path
from collections import defaultdict

PROMPTS_DIR = Path(r"C:\Users\Alexa\Desktop\SandBox\.github\prompts")
SHARED_DIR = PROMPTS_DIR / "templates" / "_shared"

REQUIRED_FM_FIELDS = ["name", "title", "description", "version"]
RECOMMENDED_FM_FIELDS = ["tags", "dependencies", "skills", "trigger"]
STRUCTURAL_SECTIONS = ["## Goal", "## Context", "## Inputs", "## Outputs", "## Rules", "## Skills Required", "## Phases", "## Steps", "## Workflow", "## Verification"]

def parse_frontmatter(text):
    """Extract YAML frontmatter from .prompt.md text."""
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if not m:
        return None, text
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return "PARSE_ERROR", text
    return fm, text[m.end():]

def check_file(path):
    """Analyze one .prompt.md file. Returns dict of issues found."""
    text = path.read_text(encoding="utf-8")
    issues = defaultdict(list)
    fm, body = parse_frontmatter(text)
    
    # --- Frontmatter ---
    if fm is None:
        issues["critical"].append("NO_FRONTMATTER")
        return dict(issues), fm, text, body
    if fm == "PARSE_ERROR":
        issues["critical"].append("YAML_PARSE_ERROR")
        return dict(issues), fm, text, body
    
    for field in REQUIRED_FM_FIELDS:
        if field not in fm or not fm[field]:
            issues["high"].append(f"MISSING_REQUIRED_FM:{field}")
    
    for field in RECOMMENDED_FM_FIELDS:
        if field not in fm:
            issues["medium"].append(f"MISSING_RECOMMENDED_FM:{field}")
    
    # Trigger check
    name = fm.get("name", "")
    trigger = fm.get("trigger", "")
    if trigger and name and trigger != f"/{name}":
        issues["medium"].append(f"TRIGGER_MISMATCH:trigger={trigger},expected=/{name}")
    elif not trigger:
        issues["medium"].append("MISSING_TRIGGER")
    
    # Tags
    tags = fm.get("tags", [])
    if not tags:
        issues["medium"].append("EMPTY_TAGS")
    elif isinstance(tags, list) and len(tags) <= 1:
        issues["info"].append("TAGS_TOO_FEW:only_1_tag")
    
    # Dependencies format check
    deps = fm.get("dependencies", [])
    for dep in deps:
        if isinstance(dep, str):
            if dep.startswith("skill:"):
                skill_name = dep[6:]
                if skill_name in ["terminal", "search_files", "web_search", "read_file", "write_file", "delegate_task"]:
                    issues["high"].append(f"TOOL_IN_SKILL_PREFIX:{dep}")
    
    # Skills vs dependencies consistency 
    skills_list = fm.get("skills", [])
    for s in skills_list:
        if isinstance(s, str) and " — " in s:
            issues["medium"].append(f"SKILL_WITH_DESCRIPTION:{s}")
    
    # --- Body structure ---
    # Create a normalized searchable body (strip frontmatter)
    body_lower = body.lower()
    
    # Check for structural sections
    found_sections = set()
    for section in STRUCTURAL_SECTIONS:
        # Match heading at start of line
        if re.search(r'^' + re.escape(section), body, re.MULTILINE):
            found_sections.add(section)
    
    # Core must-haves
    if "## Goal" not in found_sections and "## Overview" not in found_sections:
        issues["medium"].append("MISSING_GOAL_OR_OVERVIEW")
    if "## Rules" not in found_sections:
        issues["info"].append("MISSING_RULES_SECTION")
    # Execution sections — check broader patterns
    has_execution = any([
        section in found_sections for section in ["## Phases", "## Steps", "## Workflow", "## Process"]
    ])
    if not has_execution:
        # Also check for inline numbered phases like "### Phase 1" or "# Phase"
        if not re.search(r'^#{2,3}\s+Phase\s+\d', body, re.MULTILINE):
            issues["medium"].append("MISSING_EXECUTION_SECTION:no_Phases/Steps/Workflow")
    
    # DRY compliance — check for inline core rules instead of reference
    if "## Rules" in found_sections:
        # Check if it's a reference to shared or inline
        rules_section_match = re.search(r'^## Rules\s*\n(.*?)(?=^## |\Z)', body, re.MULTILINE | re.DOTALL)
        if rules_section_match:
            rules_text = rules_section_match.group(1)
            if "_shared/rules-core" not in rules_text and "rules-core" not in rules_text:
                # Check if it's just a link to core
                if not re.search(r'`templates/_shared/rules-core', rules_text):
                    issues["info"].append("RULES_INLINE_NOT_SHARED")
    
    # Check for legacy headings
    if re.search(r'#{2,3}\s+Legacy Prompt Details', body):
        issues["medium"].append("LEGACY_PROMPT_DETAILS_SECTION")
    
    # Check for malformed headings (like "## Phase 1# Task1" — hash with no space between)
    if re.search(r'^#{2,3}\s[^#\n]+#{1,2}(?!\s)', body, re.MULTILINE):
        issues["high"].append("MALFORMED_HEADINGS")
    
    # Check description quality
    desc = fm.get("description", "")
    if len(desc) < 30:
        issues["info"].append("DESCRIPTION_TOO_SHORT")
    if desc and (desc.endswith('.') is False):
        issues["info"].append("DESCRIPTION_NO_PERIOD")
    
    return dict(issues), fm, text, body

def main():
    prompt_files = sorted(PROMPTS_DIR.glob("*.prompt.md"))
    print(f"=== Prompt Library Enhancement Analyzer ===\n")
    print(f"Scanning: {len(prompt_files)} .prompt.md files\n")
    
    all_issues = defaultdict(lambda: defaultdict(list))
    per_file = []
    summary_counts = {"critical": 0, "high": 0, "medium": 0, "info": 0}
    
    for pf in prompt_files:
        # Handle double extension .prompt.md properly
        name = pf.name.replace('.prompt.md', '')
        issues, fm, full_text, body = check_file(pf)
        per_file.append({"name": name, "issues": issues, "has_fm": fm not in (None, "PARSE_ERROR")})
        
        for severity, issuelist in issues.items():
            summary_counts[severity] += len(issuelist)
            for iss in issuelist:
                all_issues[severity][iss].append(name)
    
    # Print summary
    print(f"Issues by severity:")
    for sev in ["critical", "high", "medium", "info"]:
        count = summary_counts[sev]
        print(f"  {sev.upper():10s}: {count}")
    print()
    
    print(f"Files with no frontmatter:")
    no_fm = [p["name"] for p in per_file if not p["has_fm"]]
    for n in no_fm:
        print(f"  - {n}.prompt.md")
    
    print(f"\n=== Detailed Issue Breakdown ===\n")
    for sev in ["critical", "high", "medium", "info"]:
        if not all_issues[sev]:
            continue
        print(f"\n--- {sev.upper()} ---")
        for issue, files in sorted(all_issues[sev].items()):
            print(f"\n  {issue}")
            print(f"    Files: {len(files)}")
            # Show first 5 files
            for f in files[:5]:
                print(f"      - {f}.prompt.md")
            if len(files) > 5:
                print(f"      ... and {len(files)-5} more")
    
    # Write JSON report
    report = {
        "total_files": len(prompt_files),
        "issue_counts": dict(summary_counts),
        "files_no_frontmatter": no_fm,
        "all_issues": {sev: dict(items) for sev, items in all_issues.items()},
        "per_file": [{"name": p["name"], "issue_count": sum(len(v) for v in p["issues"].values())} for p in per_file]
    }
    
    report_path = PROMPTS_DIR / ".enhance" / "analysis_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    
    print(f"\n\nFull report written to: {report_path}")
    
    # Identify top worst/best files
    ranked = sorted(report["per_file"], key=lambda x: x["issue_count"], reverse=True)
    print(f"\n=== Top 10 Most Issues ===")
    for p in ranked[:10]:
        print(f"  {p['name']}: {p['issue_count']} issues")
    print(f"\n=== Cleanest (0 issues) ===")
    clean = [p for p in ranked if p["issue_count"] == 0]
    for p in clean[:10]:
        print(f"  {p['name']}")

if __name__ == "__main__":
    main()
