#!/usr/bin/env python3
import os
import re

import yaml

with open("slice3.txt") as f:
    files = [l.strip() for l in f if l.strip()]

results = []
for path in files:
    name = os.path.basename(path)
    with open(path, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    # split frontmatter
    fm = {}
    body = text
    if text.startswith("---"):
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
        if m:
            fmb = m.group(1)
            body = m.group(2)
            try:
                fm = yaml.safe_load(fmb) or {}
            except Exception as e:
                fm = {"__parse_error__": str(e)}
    # metrics
    desc = fm.get("description")
    tags = fm.get("tags")
    plan = fm.get("plan")
    formatter = fm.get("formatter")
    has_desc = isinstance(desc, str) and desc.strip() != ""
    has_tags = isinstance(tags, (list,)) and len(tags) > 0
    has_plan = (isinstance(plan, str) and plan.strip() != "") or isinstance(plan, (list, dict))
    has_formatter = (isinstance(formatter, str) and formatter.strip() != "") or isinstance(formatter, (list, dict))
    body_lower = body.lower()
    # instruction clarity
    has_do = bool(re.search(r"\b(do|don\'?t|do not|never|always|must|avoid|ensure)\b", body_lower))
    has_accept = bool(
        re.search(r"acceptance criteria|acceptance\b|definition of done|done when|success criteria", body_lower)
    )
    has_verify = bool(
        re.search(r"verif|check that|confirm that|test that|run .* and confirm|self[- ]?check", body_lower)
    )
    # structural completeness
    headers = re.findall(r"^#{1,3}\s+(.+)$", body, re.MULTILINE)
    htext = " | ".join(headers).lower()
    has_goal = any(k in htext for k in ["goal", "objective", "purpose"])
    has_context = "context" in htext
    has_workflow = any(k in htext for k in ["workflow", "steps", "phase", "process", "procedure", "approach"])
    has_rules = any(k in htext for k in ["rule", "guideline", "constraint", "do", "don't"])
    has_verif_sec = any(k in htext for k in ["verif", "validation", "check", "test"])
    # redundancy / dead references
    tmpl_refs = re.findall(r"(templates?/[^\s\)\]\"\'`]+)", body)
    skill_refs = re.findall(r"(?:skill:)([^\s\)\]\"\'`]+)", body)
    tool_refs = re.findall(r"(?:tool:)([^\s\)\]\"\'`]+)", body)
    # instruction ratio: count lines that look like instructions vs filler
    lines = [l for l in body.splitlines() if l.strip()]
    non_empty = len(lines)
    # references that may be dead (we can't fully resolve, but flag for manual)
    results.append(
        dict(
            name=name,
            size=len(text),
            fm_keys=list(fm.keys()),
            has_desc=has_desc,
            has_tags=has_tags,
            has_plan=has_plan,
            has_formatter=has_formatter,
            has_do=has_do,
            has_accept=has_accept,
            has_verify=has_verify,
            has_goal=has_goal,
            has_context=has_context,
            has_workflow=has_workflow,
            has_rules=has_rules,
            has_verif_sec=has_verif_sec,
            n_headers=len(headers),
            tmpl_refs=tmpl_refs,
            skill_refs=skill_refs,
            tool_refs=tool_refs,
            n_lines=non_empty,
            desc=desc if isinstance(desc, str) else "",
            tags=tags,
        )
    )

# print summary as TSV
print(
    "name\tsize\thas_desc\thas_tags\thas_plan\thas_fmt\thas_do\thas_acc\thas_ver\thas_goal\thas_ctx\thas_wf\thas_rules\thas_versec\tn_hdr\tn_lines\ttag_count"
)
for r in results:
    tc = len(r["tags"]) if isinstance(r["tags"], list) else 0
    print(
        f"{r['name']}\t{r['size']}\t{int(r['has_desc'])}\t{int(r['has_tags'])}\t{int(r['has_plan'])}\t{int(r['has_formatter'])}\t{int(r['has_do'])}\t{int(r['has_accept'])}\t{int(r['has_verify'])}\t{int(r['has_goal'])}\t{int(r['has_context'])}\t{int(r['has_workflow'])}\t{int(r['has_rules'])}\t{int(r['has_verif_sec'])}\t{r['n_headers']}\t{r['n_lines']}\t{tc}"
    )

# dump references for manual inspection
print("\n=== REFERENCES ===")
for r in results:
    refs = []
    if r["tmpl_refs"]:
        refs.append("TMPL:" + ",".join(r["tmpl_refs"]))
    if r["skill_refs"]:
        refs.append("SKILL:" + ",".join(r["skill_refs"]))
    if r["tool_refs"]:
        refs.append("TOOL:" + ",".join(r["tool_refs"]))
    if refs:
        print(r["name"] + " :: " + " | ".join(refs))
