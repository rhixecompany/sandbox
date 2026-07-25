---
name: prompt-verification
title: Prompt Verification & Integrity Checking
description: Use when verifying that .prompt.md files are internally consistent — DEPS==SKILLS matching, skill resolution, cross-prompt delegation validity, and frontmatter completeness. Run before claiming a prompt is implemented.
version: 1.0.0
author: Alexa
license: MIT
tags:
- prompts
- validation
- quality
- workflow
metadata:
  hermes:
    related_skills:
    - prompt-management
    - prompt-engineering
    tags:
    - prompts
    - validation
    - quality
    - workflow
---

# Prompt Verification & Integrity Checking

Systematic verification workflow for `.prompt.md` files. Run before any prompt is claimed "implemented" — even if it "already exists."

## When to Use

- After creating or updating a `.prompt.md` file
- When asked to "implement" a prompt (re-verify from fresh disk reads every time)
- Before batch execution of a prompt library
- When diagnosing "prompt didn't work" issues
- When auditing skill dependencies in a prompt library

## When NOT to Use

- For prompt content/quality review (use `skill-judge` instead)
- For batch frontmatter fixes (use `prompt-management` Phase 4 instead)
- For single-section edits to a known-good prompt

## Skills Required

| Skill | Purpose |
|-------|---------|
| `prompt-management` | Prompt lifecycle (create, update, execute, batch audit) |
| `prompt-engineering` | Prompt structure and onboarding patterns |

## Workflow

### Phase 1 — Frontmatter Completeness

Verify all required frontmatter fields are present: `name`, `title`, `description`, `version`, `author`, `license`, `tags`, `trigger`. Check optional fields: `mode`, `system`, `dependencies`, `scripts`, `skills`, `formatter`, `plan`, `metadata`, `toolsets`.

**Local schema (Alexa's hermetic prompts):** In addition to the universal required fields, every prompt under `~/AppData/Local/hermes/prompts/` must have the following five fields present in frontmatter:

| Field | Type | Default | Purpose |
|-------|------|---------|---------|
| `scripts:` | YAML list | `[]` | Script files this prompt depends on (relative to `hermes/scripts/`) |
| `skills:` | YAML list | `[]` | Skills this prompt loads — inferred from `dependencies:` `skill:` entries, or empty list |
| `toolset` / `toolsets:` | YAML list | N/A | Enabled Hermes toolsets (e.g. `terminal`, `file`, `web`) |
| `formatter:` | string | `default` | Output formatter to apply after execution |
| `plan:` | string | `""` | Reference to a plan file in `hermes/plans/` by path (e.g. `plans/2026-07-16_plan-name.md`) |

These fields must exist even when empty — presence signals schema compliance. Use a Python batch fix script when retrofitting across a large prompt library (see `fix-prompt-frontmatter` skill for the batch pattern).

```bash
python3 -c "
import yaml
with open('prompts/<name>.prompt.md') as f:
    content = f.read()
parts = content.split('---', 2)
if len(parts) < 3:
    print('No valid frontmatter')
else:
    fm = yaml.safe_load(parts[1])
    required = ['name','title','description','version','author','license','tags','trigger']
    missing = [f for f in required if f not in fm]
    if missing:
        print(f'Missing: {missing}')
    else:
        print('All required fields present')
    print(f'Trigger: {fm.get(\"trigger\")}')
    print(f'Tags ({len(fm.get(\"tags\",[]))}): {fm.get(\"tags\",[])}')
"
```

### Phase 2 — DEPS==SKILLS Consistency

Extract `dependencies` items with `skill:` prefix and compare against the `skills` list. Every entry must appear in BOTH lists — a skill in deps but not in skills won't load; a skill in skills but not in deps is a forgotten dependency.

```bash
python3 -c "
import yaml
with open('prompts/<name>.prompt.md') as f:
    parts = f.read().split('---', 2)
fm = yaml.safe_load(parts[1])
deps_skills = set(d.replace('skill:','').strip() for d in fm.get('dependencies',[]) if isinstance(d, str) and d.startswith('skill:'))
skills_set = set(fm.get('skills',[]))
mismatch = deps_skills ^ skills_set
if mismatch:
    print(f'MISMATCH: {sorted(mismatch)}')
    only_deps = deps_skills - skills_set
    only_skills = skills_set - deps_skills
    if only_deps: print(f'  Only in deps: {sorted(only_deps)}')
    if only_skills: print(f'  Only in skills: {sorted(only_skills)}')
else:
    print(f'DEPS==SKILLS: PASS ({len(deps_skills)} skills)')
"
```

### Phase 3 — Skill Resolution

For every skill name in the union of deps+skills, verify a `SKILL.md` exists somewhere under `~/AppData/Local/hermes/skills/`.

```bash
python3 -c "
import yaml, os

skills_root = os.path.expanduser('~/AppData/Local/hermes/skills')
known = set()
for root, dirs, files in os.walk(skills_root):
    if 'SKILL.md' in files:
        known.add(os.path.basename(root))

with open('prompts/<name>.prompt.md') as f:
    parts = f.read().split('---', 2)
fm = yaml.safe_load(parts[1])
deps_skills = set(d.replace('skill:','').strip() for d in fm.get('dependencies',[]) if isinstance(d, str) and d.startswith('skill:'))
all_skills = deps_skills | set(fm.get('skills',[]))
unresolved = [s for s in all_skills if s not in known]
if unresolved:
    print(f'UNRESOLVED: {unresolved}')
else:
    print(f'All {len(all_skills)} skills resolve on disk')
"
```

### Phase 4 — Prompt Dependency Resolution

For every `prompt:` prefixed dependency, verify the target `.prompt.md` file exists.

```bash
python3 -c "
import yaml, os, glob

existing = set(os.path.basename(p).replace('.prompt.md','') for p in glob.glob('prompts/*.prompt.md'))

with open('prompts/<name>.prompt.md') as f:
    parts = f.read().split('---', 2)
fm = yaml.safe_load(parts[1])
prompt_refs = [d.replace('prompt:','').strip() for d in fm.get('dependencies',[]) if isinstance(d, str) and d.startswith('prompt:')]
missing = [p for p in prompt_refs if p not in existing]
if missing:
    print(f'MISSING prompt refs: {missing}')
else:
    print(f'All {len(prompt_refs)} prompt deps resolve')
    for p in prompt_refs:
        print(f'  ✅ prompts/{p}.prompt.md')
"
```

### Phase 5 — Cross-Prompt Delegation Map

Build a directed graph of which prompts delegate to which. Verify downstream capabilities match upstream expectations.

```bash
python3 -c "
import yaml, glob

for pf in sorted(glob.glob('prompts/repo*.prompt.md')):
    with open(pf) as f:
        parts = f.read().split('---', 2)
    if len(parts) < 3: continue
    fm = yaml.safe_load(parts[1])
    trigger = fm.get('trigger', '?')
    deps = fm.get('dependencies', [])
    skill_count = len([d for d in deps if isinstance(d, str) and d.startswith('skill:')])
    prompt_refs = [d.replace('prompt:','').strip() for d in deps if isinstance(d, str) and d.startswith('prompt:')]
    print(f'{trigger:30} {skill_count:2} skills', end='')
    if prompt_refs:
        print(f'  -> {', '.join(prompt_refs)}')
    else:
        print()
"
```

### Phase 6 — Toolsets & Structure Check

Verify `toolsets` match the prompt's domain and the body has all expected sections.

| Prompt Type | Expected Toolsets | Required Sections |
|-------------|------------------|-------------------|
| Research pipeline | `web`, `browser`, `terminal`, `file` | Goal, Context, Workflow/Phases, Verification |
| Repo management | `terminal`, `file`, `browser` | Goal, Prerequisites, Workflow/Phases, Rules |
| Git analysis | `terminal`, `file` | Goal, Workflow, Rules |
| Orchestrator | `web`, `terminal`, `file`, `code_execution` | Goal, Context, Phases, Delegation, Acceptance Criteria |

```bash
grep '^## ' prompts/<name>.prompt.md   # Check section headers present
```

### Phase 7 — MCP-Reference & `tool:` Validation

For every `tool:` prefixed entry in `dependencies:` (and any top-level `tools:` list), it MUST be an MCP server named `mcp-<server>`. Built-in Hermes toolsets (`terminal`, `file`, `search_files`, `web_search`, `browser`, `vision`, `code_execution`, `mcp`) and agent facilities (`delegate_task`, `memory`, `skill_view`) are NOT MCP servers.

**CRITICAL — these are VALID references, NOT mislabels (do NOT flag as `MISLABELED_TOOL`):**
- A `tool:`/`toolsets:` entry naming a built-in Hermes tool (`terminal`, `file`, `search_files`, `web_search`, `browser`, `vision`, `code_execution`, `mcp`, etc.) is a **native tool reference** and is correct as-is.
- A prompt body that instructs "use `delegate_task`" or "call `search_files`" is prose/instruction, not a `tool:` dependency — also not `MISLABELED_TOOL`.
- Only flag as `MISLABELED_TOOL` a `tool:` entry that is neither an `mcp-*` server NOR a known native toolset (e.g. a typo like `tool:termianl`).
- Any `tool:mcp-<x>` whose `<x>` is not in the known-good set is `UNKNOWN_MCP` (typo or uncatalogued server).

**Reusable:** `scripts/audit_skill_mcp_refs.py` scans the whole library frontmatter-only and reports `UNRESOLVED` / `UNKNOWN_MCP` / `MISLABELED_TOOL` / `MISSING_PROMPT_REF` per file. Known-good MCP set and the `mcp-*` rule live in `references/mcp-server-catalog.md`.

```bash
# Run the reusable audit (frontmatter-only; cross-checks skill: + prompt: + tool: refs)
python3 scripts/audit_skill_mcp_refs.py \
  --prompts ~/AppData/Local/hermes/prompts \
  --skills ~/AppData/Local/hermes/skills \
  --report ~/AppData/Local/hermes/prompts/docs/skill-resolution-audit.md
```

Single-file manual check:

```bash
python3 -c "
import yaml
KNOWN_MCP={'fetch','filesystem','github','memory','playwright','sequential-thinking'}
with open('prompts/<name>.prompt.md') as f:
    parts=f.read().split('---',2)
fm=yaml.safe_load(parts[1])
tools=[d[5:] for d in (fm.get('dependencies') or []) if isinstance(d,str) and d.startswith('tool:')]
for t in tools:
    if t.startswith('mcp-'):
        print('OK' if t[4:] in KNOWN_MCP else f'UNKNOWN_MCP: {t}', t)
    else:
        print('MISLABELED_TOOL (move to toolsets:):', t)
"
```

## Fresh-Read Gate (Critical)

`read_file` deduplicates — the tool returns `"unchanged"` when the file hasn't changed since last read. **This does not mean the file is valid.** The dedup cache persists across sessions.

To force a fresh verification:

```bash
# Line count to confirm file exists and has expected size
wc -l prompts/<name>.prompt.md

# Frontmatter via raw python
python3 -c "
import yaml
with open('prompts/<name>.prompt.md') as f:
    c = f.read()
parts = c.split('---', 2)
fm = yaml.safe_load(parts[1])
print(f'trigger={fm.get(\"trigger\")} skills={len(fm.get(\"skills\",[]))} deps={len(fm.get(\"dependencies\",[]))}')
"

# Section structure
grep -n '^## ' prompts/<name>.prompt.md
```

## Pitfalls

- **read_file dedup traps** — Never trust a cached read for verification. The file may have been edited by another agent or the user since your last `read_file`. Always force a fresh read.
- **Skill name collisions** — If two skill dirs have the same name in different categories, `skill_view(name)` returns ambiguous-match errors. Resolve by referencing the full category path or renaming one.
- **Star vs dash in Python YAML** — PyYAML's `safe_load` normalizes list items; don't rely on original formatting.
- **Phase gating** — Don't skip Phase 2 (DEPS==SKILLS) because it "passed last time." Re-run every verification pass.
- **Mismatched toolsets** — A research prompt missing `web` toolset won't be able to `web_search`. A management prompt missing `terminal` won't run git commands.
- **Dead prompt refs** — When a prompt is renamed or deleted, all `prompt:` refs to it become dangling. Verify after every rename.
- **False MISSING on prompt refs** — The Python `glob('prompts/*.prompt.md')` may miss files if the working directory is wrong. Always confirm with `ls` or `find` before reporting a missing ref.
- **`search_files` glob can falsely return 0** — Searching `*.prompt.md` via the `search_files` tool returned 0 results even though 211 files existed; a `terminal` `find`/`ls` confirmed them. When a glob returns nothing unexpected, verify with the terminal before concluding the directory is empty.
- **Dead-template refs are often prose, not links** — A `](...)` link-only scan reported 0 broken template refs, but scanning the body with a `templates/[...]\.md` regex (inline prose mentions, not just Markdown links) found **301 dead refs across 124/211 files** in this library. Always scan BOTH forms; drop any `#anchor` before the `os.path.exists` check. (Working impl: `scripts/verify_prompt_library.py` + `scripts/analyze_prompt_library_v2.py`.)
- **Independent re-verification** — A fix script's own "changed/remaining" self-report is NOT proof of success. Re-run a SEPARATE verifier on a different code path to confirm 0 residual issues.
- **Bundled audit scripts mis-targeted** — `audit_prompts.py`/`fix_prompts.py` are hardcoded to `SandBox/Prompts` and ignore `--workspace` (audit 0 files here); `boost_prompt.py` is absent. Use the custom `scripts/verify_prompt_library.py` / `analyze_prompt_library_v2.py` for this library (see `boost-prompts` Pitfalls).
- **Whole-file regex false positives** — A regex like `re.findall(r"tool:([\w-]+)", txt)` scanned over the *entire* file (not just frontmatter) matches `skill:`/`tool:`/`mcp-` tokens that appear in prompt **bodies** (prose, code samples, `skill_view(name=...)` examples). This produces phantom UNRESOLVED/UNKNOWN entries and makes verification "fail" on a clean library. **Always parse only the YAML frontmatter block** (`^---\n(.*?)\n---\n`) before extracting refs. The reusable `scripts/audit_skill_mcp_refs.py` does this correctly — prefer it over hand-rolled whole-file greps.

## Verification Checklist

- [ ] All required frontmatter fields present (`name`, `title`, `description`, `version`, `author`, `license`, `tags`, `trigger`, `scripts`, `skills`, `formatter`, `plan`)
- [ ] DEPS==SKILLS matches (skill: deps == skills list)
- [ ] Every skill name resolves on disk
- [ ] Every prompt: dep resolves to an existing .prompt.md
- [ ] `tool:` entries are either MCP servers (`mcp-*`) or known native toolsets — native `terminal`/`file`/`search_files`/`web_search`/`delegate_task` refs are VALID, NOT `MISLABELED_TOOL` (Phase 7)
- [ ] Toolsets match the prompt's task domain
- [ ] Body has expected sections (Goal, Workflow/Phases, Rules, Verification)
- [ ] Cross-prompt delegation map is valid (no orphaned refs)
- [ ] Fresh read done (not relying on read_file cache)
- [ ] Refs extracted from **frontmatter only** (no whole-file regex leakage)
- **Native-tool `MISLABELED_TOOL` false positive** — A verification pass (or subagent) that flags `tool:terminal`, `tool:search_files`, `tool:file`, or `delegate_task` as `MISLABELED_TOOL` is WRONG. These are legitimate native-Hermes tool/agent references, not MCP servers and not mislabels. Only flag non-`mcp-*` AND non-native entries (typos). Also: "System Prompt" inside a heading is NOT an injection; a gated `rm -rf` with verify/approval nearby is intentional cleanup, not a defect (see `boost-prompts` Pitfalls).
