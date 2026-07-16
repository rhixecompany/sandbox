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

# Priority-ordered. Each entry: (domain, "substring-in-stem" or exact set)
# Order matters: specific before general.
RULES = [
 ("linux-triage", ["arch-linux-triage","centos-linux-triage","debian-linux-triage","fedora-linux-triage","linux-triage"]),
 ("azure-cloud", ["az-cost-optimize","azure-resource-health-diagnose","update-avm-modules-in-bicep","avm","bicep"]),
 ("power-platform-dataverse", ["power-apps","power-bi","dataverse","power-platform"]),
 ("mcp-server-dev", ["mcp-server-generator","mcp-copilot-studio","mcp-create-adaptive","mcp-create-declarative","mcp-deploy-manage","typespec-create-agent","typespec-create-api-plugin","typespec-api-operations"]),
 ("dotnet-csharp", ["dotnet","csharp","aspnet","ef-core","containerize-aspnet"]),
 ("java-kotlin", ["java-","kotlin","spring-boot","java-springboot","kotlin-springboot","graalvm"]),
 ("swift-apple", ["apple-appstore","swift-mcp"]),
 ("data-sql-database", ["cosmosdb","bigquery","sql-code-review","sql-optimization","postgresql","database","db-"]),
 ("frontend-web", ["migrate-to-next","next-intl","nextjs","tailwind","typescript","zod-schema","openapi-to-application","javascript-typescript","setup-nextjs"]),
 ("github-pr-issue", ["create-github","my-issues","my-pull-requests","git-flow","repo-management","suggest-awesome-github","conventional-commit","github-copilot"]),
 ("planning-specs", ["create-specification","create-implementation-plan","update-specification","update-implementation-plan","breakdown-","hermes-breakdown","context-map","plan-","create-technical-spike","create-architectural-decision-record","devops-rollout","gen-specs-as-issues"]),
 ("blueprint-generators", ["architecture-blueprint-generator","folder-structure-blueprint-generator","technology-stack-blueprint-generator","project-workflow-analysis-blueprint-generator","generator-orchestrator"]),
 ("testing-qa", ["testing","write-tests","pytest","playwright","jest","junit","mstest","nunit","tunit","xunit","coverage","quality-gate","review-and-refactor","refactor-code","refactor-method","refactor-plan","code-review"]),
 ("devops-cicd", ["multi-stage-dockerfile","docker","containerize","deployment","devops"]),
 ("documentation", ["documentation","docs","mkdocs","tldr","readme","create-llms","update-llms","markdown","oo-component","update-docs","update-markdown","write-coding-standards","comment-code-generate","add-educational-comments","csharp-docs","java-docs","code-exemplars","refactor-mardown","create-readme","readme-blueprint","generate-docs"]),
 ("agents-agentic", ["multi-agent","structured-autonomy","agent","agents","autonomy","remember","session-agentsmd","run-session","task-implementation","tasksync","seed-review","workspace-consolidate","model-recommendation","declarative-agents","copilot-instructions","sync-hermes-copilot","features"]),
 ("research", ["web-research-pipeline","repo-research-pipeline","repo-story-time","comicwise"]),
 ("security", ["security","safety-review"]),
 ("prompts-library-maintenance", ["prompt-builder","prompt-management","prompts-fix","prompts-strict-template","boost-prompt","convert-plaintext-to-md","agents-fix","bash-scripts-fix","skills-fix","skills-debug","audit-skills","create-agentsmd","optimize-agents","generate-custom-instructions","refresh-agent-inventory","finalize-agent-prompt","execute-all-prompts","what-context-needed","dev-init","dev-imp","projects-init","setup","dev","development","pl","memory-merger","test-providers-models"]),
 ("general-meta", ["initial","general","first-ask","editorconfig","shuffle-json","debugger-prompt","debug-issue","performance","repo"]),
]

def classify(name):
    n = name.lower()
    for dom, subs in RULES:
        for s in subs:
            if s in n:
                return dom
    return None

domain_map = OrderedDict()
unmatched = []
for base, m in meta.items():
    dom = classify(m["name"])
    if dom is None:
        unmatched.append(base)
    domain_map[base] = dom

print("=== UNMATCHED ===")
for u in unmatched:
    print("  ", u)
print(f"\nUnmatched: {len(unmatched)}")

counts = Counter(domain_map.values())
print("\n=== DOMAIN COUNTS ===")
for dom,c in sorted(counts.items(), key=lambda x:-x[1]):
    print(f"  {dom}: {c}")
print(f"  TOTAL: {sum(counts.values())} (files={len(files)})")

# Dump for registry writer
os.makedirs(DOCS_DIR, exist_ok=True)
json.dump(domain_map, open(os.path.join(DOCS_DIR,"_domains.json"),"w"), indent=2)
