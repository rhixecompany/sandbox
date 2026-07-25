# Cross-Prompt Delegation Map & Domain Registry (read-only analysis)

Technique for auditing a prompt library WITHOUT editing any `*.prompt.md` — produces a
delegation graph and a per-domain member registry. Invented/validated on a 211-file
Copilot/agent prompt library. All steps are read-only; only a report file is written.

## 1. Extract cross-prompt delegation edges

A delegation edge is a `prompt:`-prefixed entry inside the frontmatter `dependencies:` list:

```yaml
dependencies:
- skill:writing-plans
- prompt:context-map.prompt.md      # <- delegation edge (cross-prompt)
- prompt:update-implementation-plan  # .prompt.md suffix optional
```

Extraction (frontmatter only — never the body):

```python
import re, yaml, glob, os
files = sorted(glob.glob(os.path.join(P, "*.prompt.md")))
all_b = {os.path.basename(f) for f in files}
def fm(t):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", t, re.DOTALL)
    return (m.group(1), m.group(2)) if m else (None, t)
def norm(x):
    return x if x.endswith(".prompt.md") else x + ".prompt.md"
edges = {}; dangling = []
for f in files:
    b = os.path.basename(f)
    ft, _ = fm(open(f, encoding="utf-8").read())
    refs = set()
    if ft:
        d = yaml.safe_load(ft) or {}
        for dep in (d.get("dependencies") or []):
            if isinstance(dep, str):
                m = re.match(r"^prompt:([A-Za-z0-9._-]+)$", dep.strip())
                if m:
                    t = norm(m.group(1))
                    if t not in all_b: dangling.append((b, t))
                    refs.add(t)
    if refs: edges[b] = refs
```

**Pitfall — body-level `prompt:` keys are NOT edges.** Some prompts (e.g. dotnet-upgrade)
define task steps in the body as `- name: "X" prompt: "..."`. Those `prompt:` keys are
step descriptors, not delegation. The `^prompt:...$` regex on `dependencies:` list items
only matches frontmatter delegation refs. Keep extraction strictly inside frontmatter.

**Pitfall — `skill:`/`tool:` deps are NOT delegation edges.** Only `prompt:` prefix means
"delegate to another prompt." `skill:`/`tool:` mean skill or MCP-tool dependencies.

## 2. Categorize into domains — USE STEM, NOT TAGS

**The trap:** library-wide meta-tags (`prompts`, `typescript`, `ml`, `specification`,
`frontend`) are affixed to 80–200 of the files. Tag-based domain classification
(`if "ml" in tags`) floods the largest domains with false members. Filenames (stems) are
far more discriminative — they encode the actual subject (e.g. `power-bi-*-` vs
`csharp-*-`).

**Fix:** a priority-ordered stem-substring classifier (specific rules first, general
last). Each file gets ONE primary domain. Iterate until `unmatched == 0`.

```python
RULES = [   # (domain, [stem-substrings])  — order: specific before general
  ("linux-triage", ["arch-linux-triage","centos-linux-triage","debian-linux-triage","fedora-linux-triage","linux-triage"]),
  ("azure-cloud",  ["az-cost-optimize","azure-resource-health-diagnose","update-avm-modules-in-bicep","avm","bicep"]),
  ("power-platform-dataverse", ["power-apps","power-bi","dataverse","power-platform"]),
  ("mcp-server-dev", ["mcp-server-generator","mcp-copilot-studio","mcp-create-adaptive","mcp-create-declarative","mcp-deploy-manage","typespec-create-agent","typespec-create-api-plugin","typespec-api-operations"]),
  ("dotnet-csharp", ["dotnet","csharp","aspnet","ef-core","containerize-aspnet"]),
  ("java-kotlin",   ["java-","kotlin","spring-boot","java-springboot","kotlin-springboot","graalvm"]),
  ("swift-apple",   ["apple-appstore","swift-mcp"]),
  ("data-sql-database", ["cosmosdb","bigquery","sql-code-review","sql-optimization","postgresql","database","db-"]),
  ("frontend-web",  ["migrate-to-next","next-intl","nextjs","tailwind","typescript","zod-schema","openapi-to-application","javascript-typescript","setup-nextjs"]),
  ("github-pr-issue", ["create-github","my-issues","my-pull-requests","git-flow","repo-management","suggest-awesome-github","conventional-commit","github-copilot"]),
  ("planning-specs", ["create-specification","create-implementation-plan","update-specification","update-implementation-plan","breakdown-","hermes-breakdown","context-map","plan-","create-technical-spike","create-architectural-decision-record","devops-rollout","gen-specs-as-issues"]),
  ("blueprint-generators", ["architecture-blueprint-generator","folder-structure-blueprint-generator","technology-stack-blueprint-generator","project-workflow-analysis-blueprint-generator","generator-orchestrator"]),
  ("testing-qa",    ["testing","write-tests","pytest","playwright","jest","junit","mstest","nunit","tunit","xunit","coverage","quality-gate","review-and-refactor","refactor-code","refactor-method","refactor-plan","code-review"]),
  ("devops-cicd",   ["multi-stage-dockerfile","docker","containerize","deployment","devops"]),
  ("documentation", ["documentation","docs","mkdocs","tldr","readme","create-llms","update-llms","markdown","oo-component","update-docs","update-markdown","write-coding-standards","comment-code-generate","add-educational-comments","csharp-docs","java-docs","code-exemplars","refactor-mardown","create-readme","readme-blueprint","generate-docs"]),
  ("agents-agentic", ["multi-agent","structured-autonomy","agent","agents","autonomy","remember","session-agentsmd","run-session","task-implementation","tasksync","seed-review","workspace-consolidate","model-recommendation","declarative-agents","copilot-instructions","sync-hermes-copilot","features"]),
  ("research",      ["web-research-pipeline","repo-research-pipeline","repo-story-time","comicwise"]),
  ("security",      ["security","safety-review"]),
  ("prompts-library-maintenance", ["prompt-builder","prompt-management","prompts-fix","prompts-strict-template","boost-prompt","convert-plaintext-to-md","agents-fix","bash-scripts-fix","skills-fix","skills-debug","audit-skills","create-agentsmd","optimize-agents","generate-custom-instructions","refresh-agent-inventory","finalize-agent-prompt","execute-all-prompts","what-context-needed","dev-init","dev-imp","projects-init","setup","dev","development","pl","memory-merger","test-providers-models"]),
  ("general-meta",  ["initial","general","first-ask","editorconfig","shuffle-json","debugger-prompt","debug-issue","performance","repo"]),
]
def classify(name):
    n = name.lower()
    for dom, subs in RULES:
        for s in subs:
            if s in n: return dom
    return "uncategorized"
domain_map = {os.path.basename(f): classify(os.path.basename(f).replace(".prompt.md","")) for f in files}
unmatched = [b for b in domain_map if domain_map[b] == "uncategorized"]
```

Re-run until `len(unmatched) == 0`. Then emit a per-domain table + member lists.

## 3. Read-only verification before delivering the report

Independently re-derive edges/domains in a SEPARATE script (different code path) and
cross-check the report's claims (counts, source list). Write it to `%TEMP%` with a
`hermes-verify-` prefix, run, confirm, delete. Never trust the generator's own counts.

## 4. Report layout (prompt-registry.md)

- Overview: library size, nature, maintenance-pass summary table.
- Delegation & dependency model: N delegating prompts, M edges, K dangling, format notes.
- Domain grouping table (domain / count / %).
- Cross-prompt delegation map: one `### file` subsection per delegating prompt, bullet edges.
- Per-domain explanation: description + full member list per domain.
- Methodology: read-only caveat, parsing approach, classifier coverage proof.
