#!/usr/bin/env python3
"""
fix_prompt_library.py -- deterministic prompt frontmatter repair.

Parses ONLY the YAML frontmatter (yaml.safe_load), preserves the body byte-for-byte,
and rewrites frontmatter from the edited dict. Implements rules from the prompt-*
skills. Safe: default audit (no writes); pass --apply to mutate.

Usage:
  python3 fix_prompt_library.py --all [--apply] [--report PATH]
  python3 fix_prompt_library.py --files a.prompt.md,b.prompt.md [--apply]
"""
import argparse, json, os, re, sys

try:
    import yaml
except ImportError:
    sys.stderr.write("PyYAML required\n")
    sys.exit(2)

PROMPTS_DIR = os.path.expanduser("~/Desktop/SandBox/.github/prompts")
SKILLS_DIR = os.path.expanduser("~/AppData/Local/hermes/skills")

UNIVERSAL_REQUIRED = ["name", "title", "description", "version", "author", "license", "tags", "trigger"]
LOCAL_REQUIRED = ["scripts", "skills", "formatter", "plan", "toolsets"]

HERMES_TOOLSETS = {
    "web", "browser", "terminal", "file", "code_execution", "vision", "image_gen",
    "moa", "tts", "skills", "todo", "memory", "context_engine", "session_search",
    "clarify", "delegation", "cronjob", "mcp",
}
VSCODE_MAP = {
    "edit": "file", "editfiles": "file", "createfile": "file",
    "web/fetch": "web", "fetch": "web", "opensimplebrowser": "web",
    "runcommands": "terminal", "terminalcommand": "terminal", "runinterminal": "terminal",
    "execute": "terminal", "execute/runinterminal": "terminal", "runcommands/*": "terminal",
    "search/codebase": "file", "codebase": "file", "search/changes": "file",
    "vscode": None, "vscode.*": None, "extensions": None, "usages": None, "problems": None,
    "todos": None, "changes": None, "testfailure": None, "vscodeapi": None,
    "githubrepo": None, "github": None, "github/*": None, "microsoft.docs.mcp": "web",
    "context7": "web", "nextjs-docs-mcp": "web", "playwright": "browser",
    "io.github.chromedevtools": "browser", "search": "web",
}
KNOWN_TOOLS = {
    "terminal", "file", "web", "browser", "vision", "code_execution", "skills",
    "todo", "memory", "session_search", "clarify", "delegation", "cronjob",
    "search_files", "web_search", "image_gen", "tts", "context_engine",
}
KNOWN_MCP = {
    "mcp-ast-grep", "mcp-code-sandbox", "mcp-codex", "mcp-copilot", "mcp-fetch",
    "mcp-filesystem", "mcp-github", "mcp-linear", "mcp-docker", "mcp-memory",
    "mcp-mindstudio", "mcp-playwright", "mcp-sequential-thinking", "mcp-smithery",
    "ast-grep", "code-sandbox", "codex", "copilot-mcp", "fetch", "filesystem",
    "github", "linear", "mcp-docker", "memory", "mindstudio", "playwright",
    "sequential-thinking", "smithery",
}
TAG_KEYWORDS = [
    ("azure", "azure"), ("aws", "aws"), ("kubernetes", "kubernetes"), ("k8s", "kubernetes"),
    ("docker", "docker"), ("container", "docker"), ("spring", "spring"), ("asp.net", "dotnet"),
    ("aspnet", "dotnet"), (".net", "dotnet"), ("react", "react"), ("next", "nextjs"),
    ("vue", "vue"), ("angular", "angular"), ("python", "python"), ("django", "django"),
    ("fastapi", "python"), ("typescript", "typescript"), ("javascript", "javascript"),
    ("node", "node"), ("github", "github"), ("git", "git"), ("pr", "github"),
    ("pull-request", "github"), ("issue", "github"), ("cosmos", "azure"), ("bigquery", "gcp"),
    ("security", "security"), ("safety", "safety"), ("audit", "audit"), ("review", "review"),
    ("test", "testing"), ("spec", "specification"), ("specification", "specification"),
    ("plan", "planning"), ("planning", "planning"), ("architecture", "architecture"),
    ("blueprint", "architecture"), ("doc", "documentation"), ("documentation", "documentation"),
    ("readme", "documentation"), ("tutorial", "tutorial"), ("comment", "documentation"),
    ("mcp", "mcp"), ("prompt", "prompts"), ("prompts", "prompts"), ("skill", "skills"),
    ("agent", "agents"), ("agents", "agents"), ("orchestrat", "orchestration"),
    ("delegat", "orchestration"), ("linux", "linux"), ("triage", "troubleshooting"),
    ("debug", "debugging"), ("convert", "conversion"), ("migration", "migration"),
    ("cost", "optimization"), ("optimize", "optimization"), ("api", "api"), ("openapi", "api"),
    ("datamodel", "data-modeling"), ("data-model", "data-modeling"), ("comic", "creative"),
    ("creative", "creative"), ("appstore", "mobile"), ("code-review", "review"),
]


def split_frontmatter(text):
    if not text.startswith("---"):
        return None, text, False, None
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.DOTALL)
    if not m:
        return None, text, False, None
    raw_fm = m.group(1)
    body = text[m.end():]
    try:
        fm = yaml.safe_load(raw_fm)
    except Exception:
        return None, text, False, None
    if not isinstance(fm, dict):
        return None, text, False, None
    return fm, body, True, raw_fm


def infer_tags(bundle, existing):
    if existing:
        return existing
    low = bundle.lower()
    return sorted({tag for kw, tag in TAG_KEYWORDS if kw in low})


def normalize_toolset_entry(t):
    t = str(t).strip().lower()
    if t in HERMES_TOOLSETS:
        return t
    if t in VSCODE_MAP:
        return VSCODE_MAP[t]
    return None


def process_file(path, apply):
    slug = os.path.basename(path).replace(".prompt.md", "")
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    fm, body, had_fm, _ = split_frontmatter(raw)
    actions = []
    if fm is None:
        fm = {}
        actions.append("added missing frontmatter block")
        had_fm = False

    if fm.get("name") != slug:
        fm["name"] = slug
        actions.append(f"set name -> {slug}")
    if not fm.get("title"):
        fm["title"] = slug.replace("-", " ").replace("_", " ").title()
        actions.append("added title")

    if not fm.get("description"):
        seed = ""
        for line in body.splitlines():
            s = line.strip()
            if s and not s.startswith("#") and not s.startswith("---"):
                seed = s[:200]
                break
        fm["description"] = seed or f"Prompt for {slug}"
        actions.append("added description")

    if not fm.get("version"):
        fm["version"] = "1.0.0"
        actions.append("set version -> 1.0.0")
    else:
        fm["version"] = str(fm["version"])

    if not fm.get("author"):
        fm["author"] = "Hermes Agent"
        actions.append("set author")
    if not fm.get("license"):
        fm["license"] = "MIT"
        actions.append("set license -> MIT")

    tags = fm.get("tags")
    if tags is None:
        fm["tags"] = []
        tags = []
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.strip("[]").split(",") if t.strip()]
        fm["tags"] = tags
        actions.append("normalized tags from string")
    if isinstance(tags, list):
        fm["tags"] = [str(t) for t in tags]
    inferred = infer_tags((fm.get("description", "") + " " + body[:400]), fm.get("tags", []))
    if not fm.get("tags"):
        fm["tags"] = inferred
        if inferred:
            actions.append(f"inferred tags -> {inferred}")
    else:
        seen = set()
        ded = [t for t in fm["tags"] if not (t in seen or seen.add(t))]
        if len(ded) != len(fm["tags"]):
            actions.append("deduped tags")
        fm["tags"] = ded

    if "triggers" in fm and "trigger" not in fm:
        fm["trigger"] = fm.pop("triggers")
        actions.append("renamed triggers: -> trigger:")
    expected = "/" + slug
    if not fm.get("trigger") or str(fm["trigger"]).strip() != expected:
        fm["trigger"] = expected
        actions.append(f"set trigger -> {expected}")

    deps = fm.get("dependencies")
    if deps is None:
        deps = []
        fm["dependencies"] = []
    if isinstance(deps, str):
        deps = [deps]
        fm["dependencies"] = deps
    new_deps = []
    for d in deps:
        if not isinstance(d, str):
            new_deps.append(d)
            continue
        d = d.strip()
        low = d.lower()
        if low.startswith("skill:"):
            ref = d[6:].strip()
            refl = ref.lower()
            if refl.startswith("mcp-") or refl in KNOWN_MCP:
                new_deps.append("tool:mcp-" + refl)
                actions.append("dep %s -> tool: (mcp)" % d)
            elif refl in KNOWN_TOOLS:
                new_deps.append("tool:" + refl)
                actions.append("dep %s -> tool:%s" % (d, refl))
            else:
                new_deps.append("skill:" + ref)
        elif low.startswith("command:"):
            new_deps.append("tool:" + d[8:].strip())
            actions.append("dep %s -> tool:" % d)
        elif low.startswith("tool:") or low.startswith("prompt:"):
            new_deps.append(d)
        else:
            new_deps.append("skill:" + d)
    fm["dependencies"] = new_deps

    skill_deps = [d[6:].strip() for d in new_deps if d.lower().startswith("skill:")]
    existing_skills = fm.get("skills")
    if existing_skills is None:
        existing_skills = []
        fm["skills"] = []
    if isinstance(existing_skills, str):
        existing_skills = [s.strip() for s in existing_skills.strip("[]").split(",") if s.strip()]
    merged = list(existing_skills) + [s for s in skill_deps if s not in existing_skills]
    cleaned = []
    for s in merged:
        sl = s.lower()
        if sl.startswith("mcp-") or sl in KNOWN_MCP:
            actions.append("removed mcp entry from skills: %s" % s)
            continue
        if sl == slug:
            actions.append("removed self-ref from skills: %s" % s)
            continue
        cleaned.append(s)
    if cleaned != list(existing_skills):
        fm["skills"] = cleaned
        actions.append("synced skills: with skill: deps (DEPS==SKILLS)")
    for s in cleaned:
        if s not in skill_deps:
            new_deps.append("skill:" + s)
            actions.append("added skill: dep %s (DEPS==SKILLS)" % s)
    fm["dependencies"] = new_deps

    if "scripts" not in fm:
        fm["scripts"] = []
        actions.append("added scripts: []")
    elif fm.get("scripts") is None:
        fm["scripts"] = []
    if "formatter" not in fm:
        fm["formatter"] = "default"
        actions.append("added formatter: default")
    if "plan" not in fm:
        fm["plan"] = ""
        actions.append('added plan: ""')

    ts = fm.get("toolsets")
    if ts is None:
        ts = fm.get("toolset")
        if ts is not None:
            actions.append("renamed toolset: -> toolsets:")
        else:
            ts = []
    if isinstance(ts, str):
        ts = [ts]
    norm = []
    for t in ts:
        n = normalize_toolset_entry(t)
        if n and n not in norm:
            norm.append(n)
    has_mcp_dep = any(d.lower().startswith("tool:mcp-") for d in new_deps)
    if has_mcp_dep and "mcp" not in norm:
        norm.append("mcp")
        actions.append("added mcp to toolsets (mcp dep present)")
    norm = [t for t in norm if not t.startswith("mcp-")]
    if not norm:
        norm = ["terminal", "file"]
        actions.append("defaulted toolsets -> [terminal, file]")
    seen = set()
    final_ts = []
    for t in norm:
        if t not in seen:
            seen.add(t)
            final_ts.append(t)
    if final_ts != (fm.get("toolsets") or fm.get("toolset")):
        if "toolset" in fm:
            del fm["toolset"]
        fm["toolsets"] = final_ts
        actions.append("normalized toolsets")

    if re.search(r"^#{2,3}\s+Legacy Prompt Details", body, re.MULTILINE):
        body = re.sub(r"\n#{2,3}\s+Legacy Prompt Details.*?(?=\n#{1,3}\s|\Z)", "", body, flags=re.DOTALL)
        actions.append("stripped Legacy Prompt Details section")

    if apply and actions:
        new_fm_text = yaml.dump(fm, sort_keys=False, default_flow_style=False, allow_unicode=True, width=4096)
        out = "---\n" + new_fm_text + "---\n" + body
        with open(path, "w", encoding="utf-8") as f:
            f.write(out)

    return {
        "file": os.path.basename(path), "slug": slug, "changed": bool(actions),
        "actions": actions,
        "name": fm.get("name"), "title": fm.get("title"), "trigger": fm.get("trigger"),
        "tags": fm.get("tags"), "skills": fm.get("skills"), "toolsets": fm.get("toolsets"),
        "dep_count": len(fm.get("dependencies", [])),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--files", help="comma-separated file paths")
    ap.add_argument("--apply", action="store_true", help="mutate files")
    ap.add_argument("--report", help="write JSON report to this path")
    args = ap.parse_args()

    files = []
    if args.files:
        for p in args.files.split(","):
            p = p.strip()
            if not os.path.isabs(p):
                p = os.path.join(PROMPTS_DIR, p)
            files.append(p)
    elif args.all:
        for fn in sorted(os.listdir(PROMPTS_DIR)):
            if fn.endswith(".prompt.md"):
                files.append(os.path.join(PROMPTS_DIR, fn))
    else:
        sys.stderr.write("Specify --all or --files\n")
        sys.exit(1)

    results = []
    changed = 0
    for fp in files:
        if not os.path.exists(fp):
            results.append({"file": fp, "error": "not found"})
            continue
        try:
            r = process_file(fp, args.apply)
            if r["changed"]:
                changed += 1
            results.append(r)
        except Exception as e:
            results.append({"file": os.path.basename(fp), "error": str(e)})

    summary = {"total": len(results), "changed": changed, "mode": "apply" if args.apply else "audit", "results": results}
    if args.report:
        with open(args.report, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)
    else:
        print("MODE=%s TOTAL=%s CHANGED=%s" % (summary["mode"], summary["total"], changed))
        for r in results:
            if r.get("error"):
                print("  ERR %s: %s" % (r["file"], r["error"]))
            elif r["changed"]:
                print("  ~ %s: %s" % (r["file"], "; ".join(r["actions"])))


if __name__ == "__main__":
    main()
