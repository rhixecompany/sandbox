---
sidebar_position: 16
title: "Persistent Goals"
description: "Set a standing goal and let Hermes keep working across turns until it is done. Our take on the Ralph loop."
status: "in_progress"
---

# Goal

Download all `.md` files from `https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/*.md` → `docs/features/`. Read + understand each. Implement subgoal (`/subgoal implement, execute each .md`) by generating per-feature artifact bundles.

# Subgoal

For each discovered feature `.md`:

1. Read file at `docs/features/<file>.md`
2. Generate bundle: `./plans/<file>-plan.md`, `./specs/<file>-spec.md`, `./prompts/<file>-prompt.md`, `skills/<feature>-bundle/SKILL.md`, `scripts/<file>-execute.py`
3. Execute script (simulate / real) and verify artifacts exist + reference the feature content.

# Discovery (verified via web_search)

Confirmed feature docs (8 items; 7 from search + possible extras):

- `overview.md`
- `mcp.md`
- `memory.md`
- `skills.md`
- `tools.md`
- `tool-gateway.md`
- `kanban.md`
- `hooks.md`

Raw URLs mapped (example): `https://raw.githubusercontent.com/NousResearch/hermes-agent/main/website/docs/user-guide/features/overview.md`

# Phase Plan (Sequential outer / Parallel inner)

```
PHASE 1 - DISCOVERY + DOWNLOAD (sequential, gate-verified)
PHASE 2 - READ + UNDERSTAND (parallel per feature via delegate_task)
PHASE 3 - BUNDLE GENERATION (parallel per feature)
PHASE 4 - EXECUTION (parallel scripts; sequential gate verifies all outputs)
PHASE 5 - VERIFICATION GATE (sequential; report results to user)
```

# Verification Gates (per phase)

- Gate 1: `docs/features/` has ≥1 `.md` file downloaded; `_file_inventory.md` present.
- Gate 2: Each feature `.md` readable; summary lines captured in `./plans/<file>-plan.md`.
- Gate 3: Each bundle's 5 artifacts exist; `SKILL.md` has ≥10-line body; `plan.md` has frontmatter.
- Gate 4: `scripts/<file>-execute.py` runs (exit 0) and produces `results/<file>-result.md`.
- Gate 5: Final inventory file `./plans/_final_inventory.md` counts all artifacts (plans/specs/prompts/skills/scripts/results) per feature; no synthetic session IDs; no fabricated URL responses.

# Execution Mode Decision

- Mixed: sequential download (depends on URL discovery) → parallel subagent per feature (independent bundles) → sequential verification gate. Per multi-file-change-protocol decision tree.

# Blockers / Unavailable Skills (honest reporting)

The exact named skills `plan`, `mcp-filesystem`, `mcp-ast-grep`, `mcp-memory` were not found in this profile. Workaround: use native `write_file`/`read_file`/`terminal` equivalents; flag in reports. No synthetic replacement.

# Resource Allocation

- Master agent (this session): Phase 1 (download) + Phase 5 (gate)
- Per-feature subagent (up to 8): Phase 2 + Phase 3 + Phase 4
- Scripts: `scripts/download_features.py`, `scripts/execute_feature_bundle.py`
