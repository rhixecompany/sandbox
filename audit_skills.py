#!/usr/bin/env python3
"""Read-only skill-resolution + MCP-reference audit for prompt library."""
import os, re, glob, json
import yaml

SKILLS_ROOT = r"C:/Users/Alexa/AppData/Local/hermes/skills"
PROMPTS_ROOT = r"C:/Users/Alexa/AppData/Local/hermes/prompts"
REPORT_PATH = os.path.join(PROMPTS_ROOT, "docs", "skill-resolution-audit.md")

KNOWN_GOOD_MCP = {
    "ast-grep", "code-sandbox", "codex", "copilot-mcp", "fetch", "filesystem",
    "github", "linear", "mcp-docker", "memory", "mindstudio", "playwright",
    "sequential-thinking", "smithery",
}

# Hermes built-in toolsets (these are toolSETS, not MCP servers -> mislabeled if under tool:)
KNOWN_TOOLSETS = {
    "terminal", "file", "search_files", "browser", "computer_use", "vision",
    "web_search", "web_extract", "notes", "memory", "shell", "fs",
    # common aliases seen in frontmatter
    "code_execution", "chromium", "scrape", "search", "read", "write",
}

# Build the set of real skill dir names: every directory that contains a SKILL.md
real_skill_dirs = set()
for dirpath, dirnames, filenames in os.walk(SKILLS_ROOT):
    if "SKILL.md" in filenames:
        # the skill dir is the directory holding SKILL.md
        real_skill_dirs.add(os.path.basename(dirpath))

def split_deps(deps):
    """Return (skills set, prompts set, tools set, raw list)."""
    skills, prompts, tools, raw = set(), set(), set(), []
    if not deps:
        return skills, prompts, tools, raw
    if isinstance(deps, str):
        deps = [deps]
    for d in deps:
        if not isinstance(d, str):
            continue
        raw.append(d)
        if d.startswith("skill:"):
            skills.add(d[len("skill:"):])
        elif d.startswith("prompt:"):
            prompts.add(d[len("prompt:"):])
        elif d.startswith("tool:"):
            tools.add(d[len("tool:"):])
    return skills, prompts, tools, raw

# Collect all prompt names referenced so we can resolve prompt: deps too
prompt_files = sorted(glob.glob(os.path.join(PROMPTS_ROOT, "*.prompt.md")))
all_prompt_names = {os.path.basename(p) for p in prompt_files}

results = []
total_unresolved = 0
total_unknown_mcp = 0
total_mislabeled = 0

for pf in prompt_files:
    fname = os.path.basename(pf)
    try:
        with open(pf, encoding="utf-8") as fh:
            text = fh.read()
    except Exception as e:
        results.append({"file": fname, "error": f"read error: {e}", "fail": True})
        continue
    # parse frontmatter between first --- and second ---
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        results.append({"file": fname, "error": "no frontmatter", "fail": True})
        continue
    fm_text = m.group(1)
    try:
        fm = yaml.safe_load(fm_text) or {}
    except Exception as e:
        results.append({"file": fname, "error": f"yaml parse error: {e}", "fail": True})
        continue

    deps_skills, deps_prompts, deps_tools, _ = split_deps(fm.get("dependencies"))
    skills_list = set(fm.get("skills") or []) if isinstance(fm.get("skills"), (list,)) else set()
    # also some prompts may have a 'tools' top-level list of tool: entries
    extra_tools = set()
    tv = fm.get("tools")
    if isinstance(tv, list):
        for t in tv:
            if isinstance(t, str) and t.startswith("tool:"):
                extra_tools.add(t[len("tool:"):])

    # Normalize skill references: combine deps skills + skills list
    skill_refs = deps_skills | skills_list
    # Normalize tool refs
    tool_refs = deps_tools | extra_tools

    issues = {"UNRESOLVED": [], "UNKNOWN_MCP": [], "MISLABELED_TOOL": []}

    for s in sorted(skill_refs):
        if s not in real_skill_dirs:
            issues["UNRESOLVED"].append(s)
    for t in sorted(tool_refs):
        if t.startswith("mcp-"):
            server = t[len("mcp-"):]
            if server not in KNOWN_GOOD_MCP:
                issues["UNKNOWN_MCP"].append(t)
        else:
            # a tool: entry that is not an mcp-* server
            # is it a known Hermes toolset name? then it's mislabeled (should be toolsets:)
            # even if not in our known set, tool: must be an MCP server per spec
            issues["MISLABELED_TOOL"].append(t)

    fail = any(issues[k] for k in issues)
    if fail:
        total_unresolved += len(issues["UNRESOLVED"])
        total_unknown_mcp += len(issues["UNKNOWN_MCP"])
        total_mislabeled += len(issues["MISLABELED_TOOL"])
    results.append({
        "file": fname,
        "fail": fail,
        "unresolved": issues["UNRESOLVED"],
        "unknown_mcp": issues["UNKNOWN_MCP"],
        "mislabeled": issues["MISLABELED_TOOL"],
        "skill_refs": sorted(skill_refs),
        "tool_refs": sorted(tool_refs),
    })

failing = [r for r in results if r.get("fail")]
print(f"Total prompt files scanned: {len(prompt_files)}")
print(f"Real skill dirs (SKILL.md holders): {len(real_skill_dirs)}")
print(f"Failing files: {len(failing)}")
print(f"  UNRESOLVED skill refs total: {total_unresolved}")
print(f"  UNKNOWN_MCP total: {total_unknown_mcp}")
print(f"  MISLABELED_TOOL total: {total_mislabeled}")
print()
for r in failing:
    print(f"  {r['file']}: UNRES={r['unresolved']} UNKMCP={r['unknown_mcp']} MISLAB={r['mislabeled']}")

# dump for report generation
summary = {
    "total": len(prompt_files),
    "failing": failing,
    "real_skill_count": len(real_skill_dirs),
    "totals": {"UNRESOLVED": total_unresolved, "UNKNOWN_MCP": total_unknown_mcp, "MISLABELED_TOOL": total_mislabeled},
}
with open(r"C:/Users/Alexa/Desktop/SandBox/audit_summary.json", "w") as fh:
    json.dump(summary, fh, indent=2)
print("\nWrote audit_summary.json")
