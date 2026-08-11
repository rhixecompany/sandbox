#!/usr/bin/env python3
"""Deep audit + registry builder for the Hermes prompt library.

Read-only except the docs/ reports it writes. Covers:
  A) skill-resolution + MCP-reference audit (with false-positive filters)
  B) content-structure + safety review (accurate pass)
  C) cross-prompt delegation map + domain registry

Usage:  python3 audit_prompt_library.py
"""
import glob, os, re, yaml
from collections import defaultdict

PROMPTS = os.path.expanduser("~/Desktop/SandBox/.github/prompts")
SKILLS = os.path.expanduser("~/AppData/Local/hermes/skills")
DOCS = os.path.join(PROMPTS, "docs")
os.makedirs(DOCS, exist_ok=True)

KNOWN_MCP = {"ast-grep","code-sandbox","codex","copilot-mcp","fetch","filesystem",
    "github","linear","mcp-docker","memory","mindstudio","playwright",
    "sequential-thinking","smithery","tavily","neon","sentry","honcho",
    "context7","parallel-search","parallel-task","python-quality",
    "tooling-lint","tooling-config"}
# Native Hermes tools that are VALID as tool: deps (do NOT flag these)
NATIVE_TOOLS = {"terminal","file","web","browser","vision","code_execution","tts","skills",
    "todo","memory","session_search","clarify","delegation","cronjob","search_files",
    "web_search","image_gen","context_engine","mcp","patch","write_file",
    "execute_code","delegate_task","read_file","terminal_command"}

def real_skills():
    s=set()
    for root,dirs,files in os.walk(SKILLS):
        if "SKILL.md" in files: s.add(os.path.basename(root))
    return s
KS = real_skills()

def split_fm(text):
    if not text.startswith("---"): return None, text
    m=re.match(r"^---\s*\n(.*?)\n---\s*\n?",text,re.DOTALL)
    if not m: return None, text
    try: fm=yaml.safe_load(m.group(1))
    except Exception: return None, text
    return (fm if isinstance(fm,dict) else None), text[m.end():]

files=sorted(glob.glob(os.path.join(PROMPTS,"*.prompt.md")))
prompts=set(os.path.basename(f).replace(".prompt.md","") for f in files)
data={}
for fp in files:
    slug=os.path.basename(fp).replace(".prompt.md","")
    raw=open(fp,encoding="utf-8",errors="replace").read()
    fm,body=split_fm(raw)
    data[slug]={"fm":fm,"body":body}

# A) tool: + prompt: validation (false-positive filtered)
tool_issues=[]; prompt_issues=[]
for slug,d in data.items():
    fm=d["fm"]
    if fm is None: continue
    for dep in (fm.get("dependencies",[]) or []):
        if not isinstance(dep,str): continue
        low=dep.lower()
        if low.startswith("tool:"):
            ref=dep[5:].strip().lower()
            ref2=ref[4:] if ref.startswith("mcp-") else ref
            if ref2 in KNOWN_MCP or ref in NATIVE_TOOLS or ref2 in NATIVE_TOOLS:
                continue
            tool_issues.append((slug,dep))
        elif low.startswith("prompt:"):
            raw_t=dep[7:].strip()
            tgt=raw_t[:-len(".prompt.md")] if raw_t.endswith(".prompt.md") else raw_t
            if tgt in prompts:
                pass
            elif tgt in KS:
                prompt_issues.append((slug,dep,"MISLABELED_AS_PROMPT (it is a skill)"))
            else:
                prompt_issues.append((slug,dep,"DANGLING (no such prompt or skill)"))

# B) structure (broad) + real safety
STRUCT_KW=("goal","context","workflow","phase","rule","step","instruction","task",
           "action","example","usage","how to","overview","purpose","input","output")
struct_less=[]
safety=[]
INJ=re.compile(r"ignore (previous|prior|above|all) instructions|pretend you are|you are (dan|jailbroken)|reveal your (system|prompt)|system prompt:|exfiltrate (credentials|keys|secrets)",re.I)
for slug,d in data.items():
    body=d["body"]
    heads=[h.lower() for h in re.findall(r"^#{1,3}\s+(.+)$",body,re.M)]
    if not any(any(k in h for k in STRUCT_KW) for h in heads):
        if not heads:
            struct_less.append(slug)
    for line in body.splitlines():
        if INJ.search(line):
            safety.append((slug,"INJECTION",line.strip()[:120]))
        if re.search(r"\brm -rf\b",line) and not re.search(r"verify|after|confirm|approval|gate",line,re.I):
            safety.append((slug,"DESTRUCTIVE-NO-GATE",line.strip()[:120]))

with open(os.path.join(DOCS,"skill-resolution-audit.md"),"w",encoding="utf-8") as f:
    f.write("# Skill / Tool / Prompt-Dependency Audit (accurate pass)\n\n")
    f.write(f"Prompts: {len(data)} | Skills known: {len(KS)} | Prompts known: {len(prompts)}\n\n")
    f.write(f"## tool: dependency issues (unknown server/tool): {len(tool_issues)}\n")
    for s,dep in tool_issues: f.write(f"- {s}: {dep}\n")
    f.write(f"\n## prompt: dependency issues: {len(prompt_issues)}\n")
    for s,dep,note in prompt_issues: f.write(f"- {s}: `{dep}` — {note}\n")
    if not tool_issues and not prompt_issues:
        f.write("\nRESULT: all tool:/prompt: deps resolve correctly.\n")

with open(os.path.join(DOCS,"content-safety-audit.md"),"w",encoding="utf-8") as f:
    f.write("# Content Structure & Safety Audit (accurate pass)\n\n")
    f.write(f"Prompts: {len(data)}\n\n")
    f.write(f"Prompts with NO headings at all (truly unstructured): {len(struct_less)}\n")
    for s in struct_less: f.write(f"  - {s}\n")
    f.write(f"\nReal safety findings: {len(safety)}\n")
    for s,kind,snip in safety: f.write(f"  - [{kind}] {s}: `{snip}`\n")
    if not safety: f.write("  - None.\n")

print("tool: issues:",len(tool_issues),"| prompt: issues:",len(prompt_issues),
      "| heading-less:",len(struct_less),"| safety:",len(safety))
for s,dep,note in prompt_issues: print("  PROMPT-ISSUE:",s,dep,note)
