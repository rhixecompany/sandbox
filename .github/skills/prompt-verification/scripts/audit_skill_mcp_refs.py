#!/usr/bin/env python3
"""Re-runnable skill-resolution + MCP-reference audit for a Hermes prompt library.

Scans every *.prompt.md, parses ONLY the YAML frontmatter, and checks:
  - skill: deps / skills list resolve to a real skill dir (holds SKILL.md)
  - prompt: deps resolve to an existing <name>.prompt.md
  - tool: entries are MCP servers (mcp-* in KNOWN_GOOD_MCP); non-mcp entries
    are flagged MISLABELED_TOOL (they should be in toolsets: instead)

Read-only: writes nothing except an optional --report markdown file.

Usage:
  python3 audit_skill_mcp_refs.py [--prompts DIR] [--skills DIR] [--report FILE]
"""
import os, re, glob, argparse, sys, yaml

KNOWN_GOOD_MCP = {
    "ast-grep", "code-sandbox", "codex", "copilot-mcp", "fetch", "filesystem",
    "github", "linear", "mcp-docker", "memory", "mindstudio", "playwright",
    "sequential-thinking", "smithery",
}

DEFAULT_PROMPTS = os.path.expanduser(r"~/AppData/Local/hermes/prompts")
DEFAULT_SKILLS = os.path.expanduser(r"~/AppData/Local/hermes/skills")


def real_skill_dirs(skills_root):
    s = set()
    for dp, _, fn in os.walk(skills_root):
        if "SKILL.md" in fn:
            s.add(os.path.basename(dp))
    return s


def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    return m.group(1) if m else None


def audit(prompts_root, skills_root):
    rsd = real_skill_dirs(skills_root)
    files = sorted(glob.glob(os.path.join(prompts_root, "*.prompt.md")))
    existing_prompts = {os.path.basename(f) for f in files}
    failing = []
    for pf in files:
        name = os.path.basename(pf)
        fm_text = parse_frontmatter(open(pf, encoding="utf-8").read())
        if fm_text is None:
            failing.append((name, {"error": "no frontmatter"}, [], [], [], []))
            continue
        try:
            fm = yaml.safe_load(fm_text) or {}
        except Exception as e:
            failing.append((name, {"error": f"yaml: {e}"}, [], [], [], []))
            continue
        deps = fm.get("dependencies")
        if isinstance(deps, str):
            deps = [deps]
        skills, prompts, tools = set(), set(), set()
        for d in (deps or []):
            if not isinstance(d, str):
                continue
            if d.startswith("skill:"): skills.add(d[6:])
            elif d.startswith("prompt:"): prompts.add(d[7:])
            elif d.startswith("tool:"): tools.add(d[5:])
        skills |= {x for x in (fm.get("skills") or []) if isinstance(x, str)}
        tl = fm.get("tools")
        if isinstance(tl, list):
            for t in tl:
                if isinstance(t, str) and t.startswith("tool:"):
                    tools.add(t[5:])
        unres = sorted(s for s in skills if s not in rsd)
        unk = sorted(t for t in tools if t.startswith("mcp-") and t[4:] not in KNOWN_GOOD_MCP)
        mislab = sorted(t for t in tools if not (t.startswith("mcp-") and t[4:] in KNOWN_GOOD_MCP))
        miss_p = sorted(p for p in prompts if p not in existing_prompts)
        if unres or unk or mislab or miss_p:
            failing.append((name, {}, unres, unk, mislab, miss_p))
    return files, rsd, failing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompts", default=DEFAULT_PROMPTS)
    ap.add_argument("--skills", default=DEFAULT_SKILLS)
    ap.add_argument("--report", default=None)
    args = ap.parse_args()
    files, rsd, failing = audit(args.prompts, args.skills)
    print(f"scanned={len(files)} skills={len(rsd)} failing={len(failing)}")
    for f in failing:
        name = f[0]
        if f[1]:
            print(f"  {name}: PARSE_ERROR {f[1]}")
            continue
        _, unres, unk, mislab, miss_p = f
        print(f"  {name}: UNRES={unres} UNKMCP={unk} MISLAB={mislab} MISSPROMPT={miss_p}")
    if args.report:
        with open(args.report, "w", encoding="utf-8") as fh:
            fh.write(f"# Audit ({len(files)} prompts)\n\n")
            if not failing:
                fh.write("All prompts resolve cleanly.\n")
            for f in failing:
                name = f[0]
                if f[1]:
                    fh.write(f"## {name}\n- PARSE_ERROR {f[1]}\n")
                    continue
                _, unres, unk, mislab, miss_p = f
                fh.write(f"## {name}\n- UNRESOLVED: {unres}\n- UNKNOWN_MCP: {unk}\n- MISLABELED_TOOL: {mislab}\n- MISSING_PROMPT_REF: {miss_p}\n")
        print(f"report -> {args.report}")
    sys.exit(1 if failing else 0)


if __name__ == "__main__":
    main()
