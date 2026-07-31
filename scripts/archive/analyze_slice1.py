#!/usr/bin/env python3
"""Read-only prompt-quality enhancement analysis for slice 1."""

import json
import os
import re

import yaml

PROMPTS_DIR = "C:/Users/Alexa/AppData/Local/hermes/prompts"

FILES = [
    "Initial.prompt.md",
    "agents-fix.prompt.md",
    "agents-generator.prompt.md",
    "agents-system-prompt-context-fix.prompt.md",
    "ai-prompt-engineering-safety-review.prompt.md",
    "apple-appstore-reviewer.prompt.md",
    "architecture-blueprint-generator.prompt.md",
    "arch-linux-triage.prompt.md",
    "aspnet-minimal-api-openapi.prompt.md",
    "az-cost-optimize.prompt.md",
    "azure-resource-health-diagnose.prompt.md",
    "bash-scripts-fix.prompt.md",
    "bigquery-pipeline-audit.prompt.md",
    "boost-prompt.prompt.md",
    "breakdown-epic-arch.prompt.md",
    "breakdown-epic-pm.prompt.md",
    "breakdown-feature-implementation.prompt.md",
    "breakdown-feature-prd.prompt.md",
    "breakdown-plan.prompt.md",
    "breakdown-test.prompt.md",
    "centos-linux-triage.prompt.md",
    "code-exemplars-blueprint-generator.prompt.md",
    "code-review.prompt.md",
    "comicwise-development.prompt.md",
    "comment-code-generate-a-tutorial.prompt.md",
    "containerize-aspnetcore.prompt.md",
    "containerize-aspnet-framework.prompt.md",
    "context-map.prompt.md",
    "conventional-commit.prompt.md",
    "convert-plaintext-to-md.prompt.md",
    "copilot-instructions-blueprint-generator.prompt.md",
    "cosmosdb-datamodeling.prompt.md",
    "create-agentsmd.prompt.md",
    "create-architectural-decision-record.prompt.md",
    "create-github-action-workflow-specification.prompt.md",
    "create-github-issue-feature-from-specification.prompt.md",
    "create-github-issues-feature-from-implementation-plan.prompt.md",
    "create-github-issues-for-unmet-specification-requirements.prompt.md",
    "create-github-pull-request-from-specification.prompt.md",
    "create-implementation-plan.prompt.md",
    "create-llms.prompt.md",
    "create-oo-component-documentation.prompt.md",
    "create-readme.prompt.md",
    "create-specification.prompt.md",
    "create-spring-boot-java-project.prompt.md",
    "create-spring-boot-kotlin-project.prompt.md",
    "csharp-async.prompt.md",
    "csharp-docs.prompt.md",
    "csharp-mcp-server-generator.prompt.md",
    "csharp-nunit.prompt.md",
    "csharp-tunit.prompt.md",
    "csharp-xunit.prompt.md",
    "database.prompt.md",
    "dataverse-python-advanced-patterns.prompt.md",
    "dataverse-python-production-code.prompt.md",
    "dataverse-python-quickstart.prompt.md",
    "dataverse-python-usecase-builder.prompt.md",
    "debugger-prompt.prompt.md",
    "debian-linux-triage.prompt.md",
    "development.prompt.md",
]

# Known skills from registry (subset relevant for resolution checks)
KNOWN_SKILLS = set(
    [
        "brainstorming",
        "plans-and-specs",
        "dispatching-parallel-agents",
        "subagent-driven-development",
        "systematic-debugging",
        "simplify",
        "acpx-executor",
        "copilot-cli-quickstart",
        "introspection-only-general",
        "no-git-delete",
        "no-net-fetch",
        "using-superpowers",
        "boost-prompt",
        "boost-prompts",
        "prompt-engineering-patterns",
        "skill-creator",
        "writing-skills",
        "hermes-agent",
    ]
)

SECTION_PAT = re.compile(
    r"^\s*#{1,3}\s+(Goal|Context|Workflow|Phase|Phases|Steps|Process|Rules?|Do|Don.?t|Acceptance|Verify|Verification|Checklist|Output|Format|Requirements?)\b",
    re.I,
)
RULE_PAT = re.compile(r"^\s*[-*]\s+", re.M)
DO_DONT_PAT = re.compile(r"\b(do(n\'t| not)?|don\'t|never|always|must|should|avoid|forbid|require)\b", re.I)
ACCEPT_PAT = re.compile(
    r"\b(acceptance criteria|acceptance|criterion|done when|definition of done|success criteria)\b", re.I
)
VERIFY_PAT = re.compile(r"\b(verify|verification|checklist|self[- ]?check|before (you )?finish|confirm)\b", re.I)
FILLER_PAT = re.compile(
    r"\b(hi|hello|hey|sure|great|let me know|feel free|as an ai|i can help|please note that|just a|okay|ok)\b", re.I
)


def parse(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    fm = {}
    body = text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
    if m:
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except Exception:
            fm = {}
        body = m.group(2)
    return fm, body, text


def check_refs(body, text):
    dead = []
    # templates/... references are real file paths; check existence.
    # templates/_shared/* DOES exist, so exclude those (valid references).
    seen = set()
    for ref in re.findall(r"templates/[A-Za-z0-9_\-./]+", text):
        ref_clean = ref.rstrip(").,")
        if ref_clean.startswith("templates/_shared"):
            continue  # known-good shared templates
        if ref_clean in seen:
            continue
        seen.add(ref_clean)
        p = os.path.join(PROMPTS_DIR, ref_clean)
        if not os.path.exists(p):
            dead.append(("template", ref_clean))
    # skill:/tool: are namespace identifiers (real skills/tools), NOT file paths; skip.
    return dead


results = []
for fn in FILES:
    path = os.path.join(PROMPTS_DIR, fn)
    if not os.path.exists(path):
        results.append((fn, None, {"missing": True}))
        continue
    fm, body, text = parse(path)
    lines = [l for l in body.splitlines() if l.strip()]
    n_lines = len(lines)
    # frontmatter
    desc = fm.get("description")
    tags = fm.get("tags")
    plan = fm.get("plan")
    formatter = fm.get("formatter")
    fm_rich = bool(desc and str(desc).strip()) and bool(tags) and bool(plan) and bool(formatter)
    tags_empty = (
        (tags is None) or (isinstance(tags, list) and len(tags) == 0) or (isinstance(tags, str) and not tags.strip())
    )
    # structure (match on section headers, case-insensitive, plural-tolerant)
    headers = [l for l in body.splitlines() if re.match(r"^\s*#{1,4}\s", l)]

    def hdr_has(pat, hdrs):
        return any(re.search(pat, h, re.I) for h in hdrs)

    has_goal = hdr_has(r"goal", headers)
    has_context = hdr_has(r"context", headers)
    has_phases = hdr_has(r"phase|workflow|step|process|procedure", headers)
    has_rules = hdr_has(r"rule|constraint|requirement|do(?:n.?t)?|guideline|policy", headers)
    has_verify = hdr_has(r"verif|checklist|check|acceptance|done|validat", headers)
    # acceptance/verification also detectable in body prose
    accept = len(ACCEPT_PAT.findall(body))
    verify_kw = len(VERIFY_PAT.findall(body))
    has_acc_or_verify = bool(has_verify or accept or verify_kw)
    # rule indicators
    bullets = len(RULE_PAT.findall(body))
    do_dont = len(DO_DONT_PAT.findall(body))
    accept = len(ACCEPT_PAT.findall(body))
    verify_kw = len(VERIFY_PAT.findall(body))
    # filler
    filler = len(FILLER_PAT.findall(body))
    instruction_ratio = max(0.0, 1.0 - (filler / max(1, n_lines)))
    # redundancy: length of inline 'core rules' style blocks that duplicate _shared
    inline_rules = bool(re.search(r"rules?[:\s].*?(must|always|never|do not|don\'t)", body, re.I))
    refs = check_refs(body, text)
    # scoring of enhancement value
    issues = []
    if not (desc and str(desc).strip()):
        issues.append("missing description")
    if tags_empty:
        issues.append("empty/missing tags")
    if not plan:
        issues.append("missing plan")
    if not formatter:
        issues.append("missing formatter")
    if not has_acc_or_verify:
        issues.append("no acceptance/verification criteria")
    if not has_rules:
        issues.append("no explicit rules section")
    if not has_phases:
        issues.append("no workflow/phases section")
    if refs:
        issues.append("dead references")
    # candidate value: more issues = higher value
    value = len(issues)
    results.append(
        (
            fn,
            fm,
            {
                "n_lines": n_lines,
                "n_headers": len(headers),
                "desc": bool(desc and str(desc).strip()),
                "tags_empty": tags_empty,
                "tags": tags,
                "plan": bool(plan),
                "formatter": bool(formatter),
                "has_goal": has_goal,
                "has_context": has_context,
                "has_phases": has_phases,
                "has_rules": has_rules,
                "has_verify": has_verify,
                "has_acc_or_verify": has_acc_or_verify,
                "bullets": bullets,
                "do_dont": do_dont,
                "accept": accept,
                "verify_kw": verify_kw,
                "filler": filler,
                "instruction_ratio": round(instruction_ratio, 2),
                "refs": refs,
                "issues": issues,
                "value": value,
                "size": len(text),
            },
        )
    )

# Save JSON for inspection
with open("C:/Users/Alexa/Desktop/SandBox/analysis_slice1.json", "w") as f:
    json.dump([{"file": r[0], "fm": (r[1] if r[1] else {}), "meta": r[2]} for r in results], f, indent=2, default=str)

# Print summary table
print(
    f"{'FILE':45} {'val':>3} {'desc':>4} {'tags':>4} {'plan':>4} {'fmt':>3} {'acc/v':>5} {'phs':>3} {'rul':>3} {'refs':>4} issues"
)
for fn, fm, m in sorted(results, key=lambda x: -x[2].get("value", 0)):
    if m.get("missing"):
        print(f"{fn:45} MISSING")
        continue
    print(
        f"{fn[:44]:45} {m['value']:>3} {str(m['desc'])[0]:>4} {('E' if m['tags_empty'] else '+'):>4} {str(m['plan'])[0]:>4} {str(m['formatter'])[0]:>3} {(m['accept'] or m['has_verify']):>5} {m['has_phases']:>3} {m['has_rules']:>3} {len(m['refs']):>4}  {','.join(m['issues'])}"
    )
print("\nTotal files:", len(results))
