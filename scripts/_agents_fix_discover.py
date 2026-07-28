#!/usr/bin/env python3
"""agents-fix: discovery + cross-reference + dedup across Hermes, Copilot, Codex.

Parses the three ecosystems present in this repo:
  - Copilot  : .github/agents/*.agent.md   (YAML frontmatter + body)
  - Copilot  : .github/instructions/*.instructions.md
  - Hermes   : prompts/*.prompt.md         (agent-style prompts w/ frontmatter)
  - Codex    : .github/agents/*-codex.agent.md (codex-twin variants)

Produces structured JSON consumed by the report writer.
"""

import asyncio
import json
import os
import re
from collections import defaultdict

ROOT = "C:/Users/Alexa/Desktop/SandBox"


# ---- minimal YAML frontmatter parser (avoids third-party deps) -------------
def parse_frontmatter(text):
    """Return (frontmatter_dict, body). Supports simple YAML: strings, lists,
    block scalars (>-, |), inline lists [..], nested 1-level maps."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    fm_raw, body = m.group(1), m.group(2)
    data = {}
    cur_key = None
    for line in fm_raw.splitlines():
        if not line.strip():
            continue
        # nested list item under a key
        list_match = re.match(r"^(\s+)-\s+(.*)$", line)
        if list_match and cur_key is not None:
            data.setdefault(cur_key, [])
            if isinstance(data[cur_key], list):
                data[cur_key].append(_scalar(list_match.group(2)))
            continue
        kv = re.match(r"^([A-Za-z0-9_\-]+):\s*(.*)$", line)
        if kv:
            key, val = kv.group(1), kv.group(2)
            cur_key = key
            if val == "" or val in (">", ">-", "|", "|-"):
                # possibly block scalar or list follows
                data[key] = None
            else:
                data[key] = _scalar(val)
        elif cur_key is not None and re.match(r"^\s+\S", line):
            # continuation of block scalar
            if isinstance(data.get(cur_key), str) or data.get(cur_key) is None:
                prev = data.get(cur_key) or ""
                data[cur_key] = prev + " " + line.strip() if prev else line.strip()
    return data, body


def _scalar(v):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        if not inner:
            return []
        return [_scalar(x.strip().strip('"').strip("'")) for x in inner.split(",")]
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        return v[1:-1]
    return v


async def read(path):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, _read_sync, path)


def _read_sync(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def slug_from_file(path):
    base = os.path.basename(path)
    return re.sub(r"\.(agent|instructions|prompt)\.md$", "", base)


async def main():
    # ---- discover Copilot agents -----------------------------------------------
    global copilot_agents, copilot_instructions, hermes_prompts
    copilot_agents = []
    agents_dir = os.path.join(ROOT, ".github", "agents")
    if os.path.isdir(agents_dir):
        for fn in sorted(os.listdir(agents_dir)):
            if not fn.endswith(".agent.md"):
                continue
            p = os.path.join(agents_dir, fn)
            fm, body = parse_frontmatter(await read(p))
            slug = slug_from_file(fn)
            copilot_agents.append(
                {
                    "file": f".github/agents/{fn}",
                    "slug": slug,
                    "name": fm.get("name") or slug,
                    "name_in_fm": "name" in fm,
                    "description": (fm.get("description") or "")[:400],
                    "desc_in_fm": "description" in fm,
                    "tools": fm.get("tools") or [],
                    "model": fm.get("model") or "",
                    "body_chars": len(body),
                    "is_codex_twin": slug.endswith("-codex"),
                }
            )

    # ---- discover Copilot instructions ----------------------------------------
    copilot_instructions = []
    instr_dir = os.path.join(ROOT, ".github", "instructions")
    if os.path.isdir(instr_dir):
        for fn in sorted(os.listdir(instr_dir)):
            if not fn.endswith(".instructions.md"):
                continue
            p = os.path.join(instr_dir, fn)
            fm, body = parse_frontmatter(await read(p))
            copilot_instructions.append(
                {
                    "file": f".github/instructions/{fn}",
                    "slug": slug_from_file(fn),
                    "name": fm.get("name") or slug_from_file(fn),
                    "description": (fm.get("description") or "")[:300],
                    "body_chars": len(body),
                }
            )

    # ---- discover Hermes agent-style prompts ----------------------------------
    hermes_prompts = []
    prompts_dir = os.path.join(ROOT, "prompts")
    if os.path.isdir(prompts_dir):
        for fn in sorted(os.listdir(prompts_dir)):
            if not fn.endswith(".prompt.md"):
                continue
            p = os.path.join(prompts_dir, fn)
            fm, body = parse_frontmatter(await read(p))
            slug = slug_from_file(fn)
            hermes_prompts.append(
                {
                    "file": f"prompts/{fn}",
                    "slug": slug,
                    "name": fm.get("name") or slug,
                    "title": fm.get("title") or "",
                    "description": (fm.get("description") or "")[:400],
                    "tags": fm.get("tags") or [],
                    "body_chars": len(body),
                }
            )

    # ---- cross-reference / mapping --------------------------------------------
    # Codex twins: copilot agent slug == "<base>-codex" and a base twin exists
    codex_twins = [a for a in copilot_agents if a["is_codex_twin"]]

    def base_of(s):
        return re.sub(r"-codex$", "", s)

    # Build cross-ref rows keyed by a normalized concept.
    # Strategy: explicit slug match between copilot base and hermes prompt slug.
    copilot_by_slug = {a["slug"]: a for a in copilot_agents}
    hermes_by_slug = {h["slug"]: h for h in hermes_prompts}

    crossref = []
    all_slugs = set(copilot_by_slug) | set(hermes_by_slug)
    for slug in sorted(all_slugs):
        ca = copilot_by_slug.get(slug)
        hp = hermes_by_slug.get(slug)
        # codex twin?
        codex_slug = slug + "-codex" if ca and not slug.endswith("-codex") else None
        codex = (
            copilot_by_slug.get(codex_slug)
            if codex_slug
            else (copilot_by_slug.get(slug) if ca and ca["is_codex_twin"] else None)
        )
        row = {
            "concept": slug,
            "copilot_agent": ca["file"] if ca else "",
            "copilot_name": ca["name"] if ca else "",
            "codex_twin": codex["file"] if codex else "",
            "hermes_prompt": hp["file"] if hp else "",
            "hermes_name": hp["name"] if hp else "",
            "in_copilot": bool(ca),
            "in_codex": bool(codex),
            "in_hermes": bool(hp),
        }
        crossref.append(row)

    # ---- duplicate detection ---------------------------------------------------
    # 1) explicit codex twins (copilot agent + codex twin share base)
    dup_codex_twins = []
    for a in codex_twins:
        base = base_of(a["slug"])
        if base in copilot_by_slug:
            dup_codex_twins.append(
                {
                    "base": base,
                    "copilot": copilot_by_slug[base]["file"],
                    "codex": a["file"],
                    "same_name": copilot_by_slug[base]["name"] == a["name"],
                }
            )

    # 2) identical name fields across distict copilot agent files
    by_name = defaultdict(list)
    for a in copilot_agents:
        by_name[a["name"].strip().lower()].append(a["file"])
    dup_names = {n: fs for n, fs in by_name.items() if len(fs) > 1}

    # 3) near-identical descriptions (first 80 chars) across copilot agents
    by_desc = defaultdict(list)
    for a in copilot_agents:
        d = (a["description"] or "")[:80].strip().lower()
        if d:
            by_desc[d].append(a["file"])
    dup_desc = {d: fs for d, fs in by_desc.items() if len(fs) > 1}

    # ---- gaps ------------------------------------------------------------------
    copilot_only = [a["file"] for a in copilot_agents if a["slug"] not in hermes_by_slug and not a["is_codex_twin"]]
    hermes_only = [h["file"] for h in hermes_prompts if h["slug"] not in copilot_by_slug]

    # ---- schema validation -----------------------------------------------------
    # Copilot agents require `name` + `description` per frontmatter spec.
    schema_issues = []
    for a in copilot_agents:
        if not a["name_in_fm"]:
            schema_issues.append({"file": a["file"], "issue": "missing name (key absent; name inferred from filename)"})
        if not a["desc_in_fm"]:
            schema_issues.append({"file": a["file"], "issue": "missing description"})

    out = {
        "summary": {
            "copilot_agents": len(copilot_agents),
            "copilot_instructions": len(copilot_instructions),
            "hermes_prompts": len(hermes_prompts),
            "codex_twins": len(codex_twins),
            "crossref_rows": len(crossref),
            "copilot_codex_linked": len(dup_codex_twins),
            "dup_names_groups": len(dup_names),
            "dup_desc_groups": len(dup_desc),
            "copilot_only": len(copilot_only),
            "hermes_only": len(hermes_only),
            "schema_issues": len(schema_issues),
        },
        "copilot_agents": copilot_agents,
        "copilot_instructions": copilot_instructions,
        "hermes_prompts": hermes_prompts,
        "crossref": crossref,
        "dup_codex_twins": dup_codex_twins,
        "dup_names": dup_names,
        "dup_desc": dup_desc,
        "gaps": {"copilot_only": copilot_only, "hermes_only": hermes_only},
        "schema_issues": schema_issues,
    }
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, _write_json, os.path.join(ROOT, "results", "_agents_fix_discovery.json"), out)

    print(json.dumps(out["summary"], indent=2))
    print("\n--- codex twins ---")
    for t in dup_codex_twins:
        print(f"  {t['base']}: {t['copilot']}  <->  {t['codex']}  (name-match={t['same_name']})")
    print("\n--- dup names ---")
    for n, fs in dup_names.items():
        print(f"  '{n}': {fs}")
    print("\n--- dup desc (top 5) ---")
    for i, (d, fs) in enumerate(dup_desc.items()):
        if i >= 5:
            break
        print(f"  '{d[:50]}...': {fs}")
    print(f"\n--- schema issues: {len(schema_issues)} ---")
    for s in schema_issues[:10]:
        print(f"  {s}")


def _write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    asyncio.run(main())
