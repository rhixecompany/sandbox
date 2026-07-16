#!/usr/bin/env python3
import os, re, yaml, glob, json
from collections import Counter, OrderedDict

PROMPTS_DIR = r"C:/Users/Alexa/AppData/Local/hermes/prompts"
DOCS_DIR = os.path.join(PROMPTS_DIR, "docs")
files = sorted(glob.glob(os.path.join(PROMPTS_DIR, "*.prompt.md")))

def extract_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    return (m.group(1), m.group(2)) if m else (None, text)

meta = {}
for f in files:
    base = os.path.basename(f)
    name = base.replace(".prompt.md","")
    with open(f, encoding="utf-8") as fh:
        text = fh.read()
    fm_text, body = extract_frontmatter(text)
    tags, desc = [], ""
    if fm_text is not None:
        try:
            fm = yaml.safe_load(fm_text) or {}
            tags = fm.get("tags") or []
            desc = fm.get("description") or ""
            if not isinstance(tags, list): tags=[str(tags)]
        except: pass
    meta[base] = {"name": name, "tags":[str(t).lower() for t in tags], "desc":str(desc).lower()}

# ---- Priority-ordered domain rules (first match wins) ----
# Each rule: (domain, [stem-substrings], [discriminative tags])
RULES = [
 ("prompts-library-maintenance",
   ["prompt-builder","prompt-management","prompts-fix","prompts-strict-template","boost-prompt",
    "convert-plaintext-to-md","ai-prompt-engineering-safety-review","audit-skills-judge-fix",
    "skills-debug-prompt","skills-fix","create-agentsmd","optimize-agentsmd","optimize-agentsMd",
    "generate-custom-instructions-from-codebase","copilot-instructions-blueprint-generator",
    "github-copilot-starter","declarative-agents","mcp-create-declarative-agent","typespec-create-agent",
    "suggest-awesome-github-copilot","sync-hermes-copilot-codex","refresh-agent-inventory",
    "run-session-agentsmd-workflow","session-agentsmd-full-workflow","finalize-agent-prompt",
    "agents-system-prompt-context-fix","memory-merger","agents-fix","bash-scripts-fix","pl",
    "execute-all-prompts","what-context-needed"],
   ["prompts-library","prompt-maintenance","skill-maintenance"]),

 ("power-platform-dataverse",
   ["power-apps","power-bi","dataverse","power-platform"],
   ["power-platform","power-bi","dataverse"]),

 ("azure-cloud",
   ["az-","azure","avm","bicep","entra","fabric"],
   ["azure","bicep","entra","fabric","avm"]),

 ("dotnet-csharp",
   ["dotnet","csharp","aspnet","ef-core","containerize-aspnet","mstest","nunit","xunit","tunit",
    ".net","net-"],
   ["dotnet","csharp","aspnet","ef-core"]),

 ("java-kotlin",
   ["java-","kotlin","spring","graalvm"],
   ["java","kotlin","spring"]),

 ("go", ["go-mcp"], ["go","golang"]),
 ("rust", ["rust"], ["rust"]),
 ("php", ["php"], ["php"]),
 ("ruby", ["ruby"], ["ruby"]),
 ("swift-apple",
   ["swift","apple-appstore","ios"],
   ["swift","apple","ios"]),

 ("data-sql-database",
   ["sql","postgres","cosmos","bigquery","database","db-"],
   ["sql","postgresql","cosmos","bigquery","database"]),

 ("frontend-web",
   ["nextjs","next-","react","vue","tailwind","typescript","typespec","zod","frontend","javascript-typescript",
    "openapi-to-application","web-","setup-nextjs","migrate-to-next","next-intl"],
   ["frontend","react","nextjs","tailwind","vue","typescript","typespec","zod"]),

 ("github-pr-issue",
   ["create-github","my-issues","my-pull-requests","git-flow","github-copilot","gen-specs-as-issues",
    "repo-management","suggest-awesome-github","conventional-commit","git-"],
   ["github","git","pull-request","issue","copilot"]),

 ("planning-specs",
   ["create-specification","create-implementation-plan","update-specification","update-implementation-plan",
    "breakdown","context-map","plan-","create-technical-spike","create-architectural-decision-record",
    "devops-rollout-plan","create-readme","readme-","dev-imp","dev-init","dev","development","projects-init",
    "setup","project-workflow"],
   ["specification","planning","architecture-decision"]),

 ("testing-qa",
   ["test","pytest","playwright","jest","junit","xunit","mstest","nunit","tunit","coverage","qa","quality-gate",
    "write-tests"],
   ["testing","playwright","jest","pytest","junit","xunit","mstest","nunit","tunit","qa"]),

 ("mcp-server-dev",
   ["mcp-server-generator","mcp-","typespec-create-api-plugin"],
   ["mcp"]),

 ("linux-triage",
   ["linux-triage","arch-linux","centos","debian","fedora","ubuntu"],
   ["linux","arch-linux"]),

 ("devops-cicd",
   ["docker","containerize","bicep","ci-cd","cicd","deployment","deploy","rollout","devops",
    "update-avm-modules","multi-stage-dockerfile"],
   ["docker","kubernetes","devops","deployment","ci-cd"]),

 ("documentation",
   ["documentation","docs","mkdocs","tldr","readme","llms","markdown","create-oo-component",
    "update-oo-component","update-docs-on-code-change","update-markdown","write-coding-standards",
    "comment-code-generate","add-educational-comments","csharp-docs","java-docs","refactor-mardown",
    "code-review","postgresql-code-review","sql-code-review","code-exemplars"],
   ["documentation","markdown","readme","docs","mkdocs"]),

 ("agents-agentic",
   ["multi-agent","structured-autonomy","agent","agents","autonomy","remember","session-agentsmd",
    "run-session","task-implementation","features","tasksync","seed-review","workspace-consolidate",
    "model-recommendation","test-providers-models"],
   ["agents","multi-agent","agentic"]),

 ("blueprint-generators",
   ["blueprint-generator","technology-stack","folder-structure","architecture-blueprint",
    "project-workflow-analysis"],
   ["blueprint"]),

 ("research",
   ["web-research-pipeline","repo-research-pipeline","repo-story-time","comicwise"],
   ["research","arxiv","web-research"]),

 ("security",
   ["security","sql-optimization","postgresql-optimization","performance","debug","debugger",
    "review-and-refactor","refactor","code-review","quality"],
   ["security","performance","debugging"]),

 ("general-meta",
   ["general","initial","first-ask","setup","editorconfig","shuffle-json","structured-autonomy",
    "my-issues","my-pull-requests"],
   []),
]

def classify(name, tags, desc):
    n = name.lower(); t = set(tags); d = desc
    for dom, stems, dtags in RULES:
        for s in stems:
            if s in n:
                return dom
        for tg in dtags:
            if tg in t:
                return dom
    return None

domain_map = OrderedDict()
unmatched = []
for base, m in meta.items():
    dom = classify(m["name"], m["tags"], m["desc"])
    if dom is None:
        unmatched.append(base)
    domain_map[base] = dom

print("=== UNMATCHED ===")
for u in unmatched:
    print("  ", u, "| tags:", meta[u]["tags"])
print(f"\nUnmatched count: {len(unmatched)}")

counts = Counter(domain_map.values())
print("\n=== DOMAIN COUNTS ===")
total=0
for dom,c in sorted(counts.items(), key=lambda x:-x[1]):
    print(f"  {dom}: {c}")
    total+=c
print(f"  TOTAL: {total} (files={len(files)})")
