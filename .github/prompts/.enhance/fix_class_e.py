#!/usr/bin/env python3
"""Phase 5 (Class E) — analyzer findings.

Fixes:
1. RULES_INLINE_NOT_SHARED (7 files): the `## Rules` section now references
   `templates/_shared/rules-core.md` and wraps the inline rules under a
   `### Domain Rules` heading (DRY pattern used by compliant prompts).
2. test-providers-models.prompt.md: adds `## Rules` (rules-core reference +
   domain rules) and a `## Phases` section (5 phases mapped from existing
   sections — no new facts).

Usage:
    python fix_class_e.py          # dry-run report
    python fix_class_e.py --apply  # write changes
"""
import re
import sys
from pathlib import Path

root = Path.home() / "Desktop/SandBox/.github/prompts"
APPLY = "--apply" in sys.argv

REF_LINES = (
    "> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)\n"
    "> Domain-specific additions below.\n"
)

INLINE_FILES = [
    "all-repo-docker-setup.prompt.md",
    "ngn-earnings-research.prompt.md",
    "setup-bun-bunx.prompt.md",
    "setup-groq-cloud.prompt.md",
    "smithery-setup.prompt.md",
    "uk-earnings-research.prompt.md",
    "us-earnings-research.prompt.md",
]

TPM_RULES = (
    "## Rules\n\n"
    + REF_LINES
    + "\n### Domain Rules\n\n"
    + "1. **Inventory from authority** — Enumerate providers/models from `hermes auth list`; never invent a provider or model ID.\n"
    + "2. **Probe, don't assume** — A model counts as working only after a live capability probe succeeds; no fabricated results.\n"
    + "3. **Deterministic ordering** — Rank by the fixed rule: vision → reasoning → context size; document every override.\n"
    + "4. **Free-tier only** — Only models usable on the free tier are candidates for the fallback chain.\n"
    + "5. **Verify before claiming** — Run the Verification section gates before reporting the chain complete.\n"
)

TPM_PHASES = (
    "## Phases\n\n"
    + "1. **Phase 1 — Inventory** — `hermes auth list` all authorized providers; collect each provider's working free `default_model` and capabilities.\n"
    + "2. **Phase 2 — Probe** — Delegate live capability probes to subagents with the full Context Block; each probe returns actual availability, vision/reasoning support, and context size.\n"
    + "3. **Phase 3 — Rank** — Merge probe results and apply the Ranking Algorithm (vision → reasoning → context size) to produce the ordered candidate list.\n"
    + "4. **Phase 4 — Configure** — Set the primary model and fallback chain in Hermes config per the Configure section.\n"
    + "5. **Phase 5 — Verify** — Confirm `fallback_providers` is a real YAML list and every entry resolves to a working free model; fix and re-verify if not.\n"
)

changed = []

for name in INLINE_FILES:
    f = root / name
    text = f.read_text(encoding="utf-8")
    m = re.search(r"^## Rules\s*\n", text, re.M)
    if not m:
        print(f"SKIP {name}: no ## Rules heading")
        continue
    if "templates/_shared/rules-core" in text:
        print(f"SKIP {name}: already references rules-core")
        continue
    # insert reference + ### Domain Rules after the "## Rules" line
    head = text[: m.end()]
    tail = text[m.end() :]
    new = head + "\n" + REF_LINES + "\n### Domain Rules\n\n" + tail
    changed.append((name, "rules-core reference + ### Domain Rules"))
    if APPLY:
        f.write_text(new, encoding="utf-8", newline="\n")

# test-providers-models
tpm = root / "test-providers-models.prompt.md"
tpm_text = tpm.read_text(encoding="utf-8")
if "## Rules" not in tpm_text:
    # insert ## Rules after the ## Goal section (before ## Subgoals)
    m = re.search(r"^## Subgoals\s*\n", tpm_text, re.M)
    if m:
        tpm_text = tpm_text[: m.start()] + TPM_RULES + "\n" + tpm_text[m.start() :]
        changed.append(("test-providers-models.prompt.md", "added ## Rules"))
if "## Phases" not in tpm_text:
    m = re.search(r"^## Verification\s*\n", tpm_text, re.M)
    if m:
        tpm_text = tpm_text[: m.start()] + TPM_PHASES + "\n" + tpm_text[m.start() :]
        changed.append(("test-providers-models.prompt.md", "added ## Phases (5)"))
if APPLY:
    tpm.write_text(tpm_text, encoding="utf-8", newline="\n")

print(f"SUMMARY: {len(changed)} fix(es)" + ("" if APPLY else " (dry-run — re-run with --apply)"))
for name, what in changed:
    print(f"  {name}: {what}")
