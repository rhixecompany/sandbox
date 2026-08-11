#!/usr/bin/env python3
"""Independent verification of the prompt library (no mutation).

Separate code path from the fixer so a fixer's self-report can never be
trusted as proof of validity. Run after every batch fix.

Usage:  python3 verify_prompt_library.py
"""
import glob, os, re, sys
try:
    import yaml
except ImportError:
    sys.stderr.write("PyYAML required\n")
    sys.exit(2)

PROMPTS_DIR = os.path.expanduser("~/Desktop/SandBox/.github/prompts")
SKILLS_DIR = os.path.expanduser("~/AppData/Local/hermes/skills")

HERMES_TOOLSETS = {"web","browser","terminal","file","code_execution","vision","image_gen",
    "moa","tts","skills","todo","memory","context_engine","session_search","clarify",
    "delegation","cronjob","mcp"}

def known_skills():
    s = set()
    for root, dirs, files in os.walk(SKILLS_DIR):
        if "SKILL.md" in files:
            s.add(os.path.basename(root))
    return s

KS = known_skills()

def split_fm(text):
    if not text.startswith("---"):
        return None, text, False
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.DOTALL)
    if not m:
        return None, text, False
    try:
        fm = yaml.safe_load(m.group(1))
    except Exception:
        return None, text, False
    if not isinstance(fm, dict):
        return None, text, False
    return fm, text[m.end():], True

def verify(path):
    slug = os.path.basename(path).replace(".prompt.md","")
    raw = open(path, "r", encoding="utf-8", errors="replace").read()
    issues = []
    if "\r\n" in raw:
        issues.append("CRLF")
    fm, body, had = split_fm(raw)
    if not had or fm is None:
        return [f"NO_VALID_FRONTMATTER({slug})"]
    if len(re.findall(r"^metadata:", raw, re.MULTILINE)) > 1:
        issues.append("DUPLICATE_METADATA")
    req = ["name","title","description","version","author","license","tags","trigger"]
    for f in req:
        if f not in fm or fm.get(f) in (None, "", []):
            issues.append(f"MISSING:{f}")
    local = ["scripts","skills","formatter","plan","toolsets"]
    for f in local:
        if f not in fm:
            issues.append(f"MISSING_LOCAL:{f}")
    if fm.get("name") != slug:
        issues.append(f"NAME≠SLUG({fm.get('name')})")
    if str(fm.get("trigger","")).strip() != "/"+slug:
        issues.append(f"TRIGGER≠/{slug}")
    deps = fm.get("dependencies", []) or []
    dep_skills = set()
    for d in deps:
        if isinstance(d,str) and d.lower().startswith("skill:"):
            dep_skills.add(d[6:].strip())
    skills = set(fm.get("skills", []) or [])
    if dep_skills != skills:
        only_deps = dep_skills - skills
        only_skills = skills - dep_skills
        if only_deps: issues.append(f"SKILL_DEP_ONLY:{sorted(only_deps)}")
        if only_skills: issues.append(f"SKILL_LIST_ONLY:{sorted(only_skills)}")
    for d in deps:
        if isinstance(d,str) and d.lower().startswith("skill:mcp-"):
            issues.append("MCP_AS_SKILL_DEP")
    for s in skills:
        if str(s).lower().startswith("mcp-"):
            issues.append("MCP_IN_SKILLS")
    ts = fm.get("toolsets", fm.get("toolset", [])) or []
    if isinstance(ts, str): ts = [ts]
    bad = [t for t in ts if str(t).lower() not in HERMES_TOOLSETS]
    if bad: issues.append(f"BAD_TOOLSET:{bad}")
    if any(isinstance(d,str) and d.lower().startswith("tool:mcp-") for d in deps):
        if "mcp" not in [str(t).lower() for t in ts]:
            issues.append("MCP_DEP_NO_TOOLSET")
    for s in skills:
        if s not in KS:
            issues.append(f"UNRESOLVED_SKILL:{s}")
    if re.search(r"^#{2,3}\s+Legacy Prompt Details", body, re.MULTILINE):
        issues.append("LEGACY_SECTION")
    return issues

def main():
    files = sorted(glob.glob(os.path.join(PROMPTS_DIR, "*.prompt.md")))
    all_issues = {}
    clean = 0
    for fp in files:
        iss = verify(fp)
        if iss:
            all_issues[os.path.basename(fp)] = iss
        else:
            clean += 1
    print(f"TOTAL={len(files)} CLEAN={clean} WITH_ISSUES={len(all_issues)}")
    from collections import Counter
    c = Counter()
    for iss in all_issues.values():
        for i in iss:
            key = i.split("(")[0].split(":")[0]
            c[key]+=1
    print("ISSUE TYPE COUNTS:", dict(c))
    for fn, iss in sorted(all_issues.items()):
        print(f"  {fn}: {iss}")

if __name__=="__main__":
    main()
