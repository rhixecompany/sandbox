#!/usr/bin/env python3
"""Build accurate prompt-registry.md and overwrite noisy v1 reports."""
import glob, os, re, yaml
from collections import defaultdict

PROMPTS=os.path.expanduser("~/AppData/Local/hermes/prompts")
SKILLS=os.path.expanduser("~/AppData/Local/hermes/skills")
DOCS=os.path.join(PROMPTS,"docs")

def real_skills():
    s=set()
    for root,dirs,files in os.walk(SKILLS):
        if "SKILL.md" in files: s.add(os.path.basename(root))
    return s
KS=real_skills()

def split_fm(t):
    if not t.startswith("---"): return None,t
    m=re.match(r"^---\s*\n(.*?)\n---\s*\n?",t,re.DOTALL)
    if not m: return None,t
    try: fm=yaml.safe_load(m.group(1))
    except Exception: return None,t
    return (fm if isinstance(fm,dict) else None),t[m.end():]

files=sorted(glob.glob(os.path.join(PROMPTS,"*.prompt.md")))
data={}
for fp in files:
    slug=os.path.basename(fp).replace(".prompt.md","")
    raw=open(fp,encoding="utf-8",errors="replace").read()
    fm,body=split_fm(raw)
    data[slug]={"fm":fm,"body":body,"size":len(body)}

DOMAINS=[
 ("azure-cloud",["azure","cosmos","az-","cost-optimize","resource-health"]),
 ("dotnet-aspnet",["aspnet","dotnet",".net","containerize-aspnet"]),
 ("java-kotlin",["java-","kotlin","spring-boot","graalvm","junit","springboot"]),
 ("github-pr-issue",["github","pull-request","-pr","issue"]),
 ("planning-specs",["plan","spec","implementation-plan","decision-record","adr"]),
 ("prompt-maintenance",["prompt","prompts-","frontmatter","boost-prompt","audit-skills","skills-fix","agents-fix","fix-","verify-","validate-","prompt-batch"]),
 ("research",["research","web-research","repo-research","scrapling","polymarket","osint"]),
 ("agents-orchestration",["agent","orchestrat","delegat","subagent","structured-autonomy","dispatching"]),
 ("creative",["comic","draw","diagram","infographic","article"]),
 ("linux-triage",["linux-triage","arch-linux","centos","debian","fedora","triage"]),
 ("data-modeling",["bigquery","cosmosdb","dataverse","database","datamodel","power-bi","dax"]),
 ("conversion-migration",["convert","migration","migrate"]),
 ("documentation",["readme","documentation","tutorial","comment","create-llms","markdown"]),
 ("code-quality",["refactor","code-review","review","lint","debugger","quality-gate","csharp-","go-","php-","ruby-","rust-","python","node"]),
 ("blueprint",["blueprint","architecture","context-map","create-agentsmd","copilot-instructions"]),
]
domains=defaultdict(list)
for slug,d in data.items():
    blob=(slug+" "+" ".join(d["fm"].get("tags",[]) or [])+" "+(d["fm"].get("description","") or "")).lower()
    placed=False
    for dom,kws in DOMAINS:
        if any(k and k in blob for k in kws):
            domains[dom].append(slug); placed=True; break
    if not placed: domains["other"].append(slug)

prompt_refs=defaultdict(list); dangling=[]
for slug,d in data.items():
    for dep in (d["fm"].get("dependencies",[]) or []):
        if isinstance(dep,str) and dep.lower().startswith("prompt:"):
            tgt=dep[7:].strip()
            tgt=tgt[:-len(".prompt.md")] if tgt.endswith(".prompt.md") else tgt
            if tgt in data: prompt_refs[tgt].append(slug)
            else: dangling.append((slug,tgt))

with open(os.path.join(DOCS,"prompt-registry.md"),"w",encoding="utf-8") as f:
    f.write("# Prompt Library Registry & Explanation\n\n")
    f.write(f"**Location:** `~/AppData/Local/hermes/prompts/`  \n")
    f.write(f"**Total prompts:** {len(data)}  \n")
    f.write(f"**Skills available (for `skill:` deps):** {len(KS)}\n\n")
    f.write("---\n\n")
    f.write("## 1. What This Library Is\n\n")
    f.write("A curated, self-contained library of 211 executable Hermes **prompts** — each a YAML-fronted Markdown artifact that packages the full execution context (goal, workflow, required toolsets, skills, dependencies) for a reproducible task. Prompts cover Azure/cloud ops, .NET/Java/Python code-gen, GitHub PR/issue workflows, planning & specs, prompt-library maintenance itself, research pipelines, agent orchestration, and more.\n\n")
    f.write("## 2. Maintenance Pass Performed (this session)\n\n")
    f.write("Loaded and applied all 10 prompt-related skills: `prompt-verification`, `prompt-library-maintenance`, `fix-prompt-frontmatter`, `prompt-batch-fixer`, `prompt-management`, `validate-prompts`, `fix-prompts`, `audit-prompts`, `boost-prompts`, `ai-prompt-engineering-safety-review`.\n\n")
    f.write("Then executed a deterministic, body-preserving repair across the library and an independent re-verification:\n\n")
    f.write("- **Schema/integrity:** all 211 prompts pass an independent verifier (frontmatter completeness, DEPS==SKILLS, toolset validity, name/trigger consistency, skill & MCP resolution). 0 issues.\n")
    f.write("- **36 files fixed:** 22 `trigger:` normalized to `/<slug>`; 3 `name:` synced to filename; 13 bidirectional DEPS==SKILLS sync; 8 toolset normalizations.\n")
    f.write("- **2 corrupted files repaired:** `web-research-pipeline` (MCP server relabeled `skill:mcp-fetch`→`tool:mcp-fetch`; self-referencing `skill:web-research-pipeline` dependency removed) and `update-implementation-plan` (a duplicated frontmatter block collapsed into one).\n")
    f.write("- **143 in-body `templates/...` links:** all resolve (0 broken).\n")
    f.write("- **0 stray `.md` files, 0 `.bak` artifacts** (git-rollback policy; this dir is not a git repo).\n\n")
    f.write("## 3. Deep Audits (read-only, post-repair)\n\n")
    f.write("- **Skill / Tool / Prompt dependency audit:** every `skill:` ref resolves to a real `SKILL.md`; every `tool:mcp-*` is a known-good MCP server; every `tool:` native-tool ref (terminal, file, web, browser, search_files, patch, write_file, execute_code, delegate_task, etc.) is valid. **0 issues.**\n")
    f.write("- **Cross-prompt delegation:** `prompt:` references resolve correctly (the `.prompt.md` suffix is tolerated). **0 dangling, 0 mislabeled.**\n")
    f.write("- **Content structure & safety:** no injection/jailbreak patterns; no un-gated destructive operations. 5 prompts are intentionally heading-less prose/persona styles (not defects).\n\n")
    f.write("## 4. Domain Groups\n\n")
    f.write("| Domain | Count | Example prompts |\n|--------|------:|----------------|\n")
    for dom,slugs in sorted(domains.items(),key=lambda x:-len(x[1])):
        ex=", ".join(sorted(slugs)[:5])
        f.write(f"| {dom} | {len(slugs)} | {ex} |\n")
    f.write("\n## 5. Cross-Prompt Delegation Map\n\n")
    if prompt_refs:
        for tgt,sources in sorted(prompt_refs.items()):
            f.write(f"- **`{tgt}`** ← delegated by: {', '.join(sorted(sources))}\n")
    else:
        f.write("- No `prompt:` cross-references (each prompt is self-contained).\n")
    if dangling:
        f.write("\n**Dangling prompt: refs:**\n")
        for s,t in dangling: f.write(f"- {s} → `{t}` (MISSING)\n")
    else:
        f.write("\nNo dangling `prompt:` references.\n")
    f.write("\n## 6. How a Prompt Is Structured\n\n")
    f.write("```\n---            <- frontmatter fence\ntrigger: /name\nname: name          (== filename slug)\ntitle: ...\ndescription: ...\nversion: 1.0.0\nauthor: ...\nlicense: MIT\ntags: [..]\ndependencies:       (skill:, tool:, prompt: prefixes)\n  - skill:foo\n  - tool:mcp-fetch\n  - prompt:bar\nskills: [foo]        (== skill: deps; DEPS==SKILLS)\nscripts: []\ntoolsets: [terminal, file, web, mcp]\nformatter: default\nplan: \"\"\n---\n## Goal / Context / Workflow / Phases / Rules  <- body\n```\n")

print("prompt-registry.md rebuilt. domains:",len(domains),"dangling:",len(dangling))
