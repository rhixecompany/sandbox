#!/usr/bin/env python3
"""Phase 6 — Enhancement pass: add standard reference-only sections.

For every prompt missing them, appends (at EOF, in order):
  ## MCP Servers & Tools   — only the 4 files lacking it (family-specific, real servers)
  ## Hooks                 — compact reference to shared .github/hooks assets
  ## Scripts               — reference to .enhance/ tooling + hooks scripts
  ## Related Prompts       — same-family prompt links, computed + verified to exist

Reference-only: every path/link below resolves to a real file. No new facts.
Files already carrying a section are skipped. Dry-run by default.

Usage:
    python enhance_sections.py          # dry-run report
    python enhance_sections.py --apply  # write changes
"""
import sys
from collections import defaultdict
from pathlib import Path

root = Path.home() / "Desktop/SandBox/.github/prompts"
APPLY = "--apply" in sys.argv

HOOKS_BLOCK = (
    "## Hooks\n\n"
    "Shared workspace hooks run around this prompt's execution — see "
    "[`.github/hooks/README.md`](../hooks/README.md): `session-logger`, "
    "`session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, "
    "`post-exec-state-log.py`.\n"
)

SCRIPTS_BLOCK = (
    "## Scripts\n\n"
    "Prompt-library tooling (see `.enhance/`):\n\n"
    "- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)\n"
    "- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, "
    "`.enhance/fix_frontmatter_plan.py` — Class C-E repair/verify tooling\n"
    "- `.github/hooks/*` — hook implementations referenced in the Hooks section\n"
)

MCP_BLOCKS = {
    "setup-bun-bunx.prompt.md": (
        "## MCP Servers & Tools\n\n"
        "- **Terminal** — `bun`/`bunx` execution for migration and verification.\n"
        "- **File tools** — read/patch manifests (`package.json`, `tsconfig.json`).\n"
        "- **Tooling-lint MCP** — eslint/prettier checks across touched repos.\n"
        "- **Tooling-config MCP** — pre-commit/.gitignore validation.\n"
    ),
    "smithery-setup.prompt.md": (
        "## MCP Servers & Tools\n\n"
        "- **Smithery MCP** — registry/search/toolbox management (this prompt's subject).\n"
        "- **Terminal** — `smithery` CLI install/configure calls.\n"
        "- **Web tools** — `web_search`, `web_extract` for registry documentation.\n"
    ),
    "all-repo-docker-setup.prompt.md": (
        "## MCP Servers & Tools\n\n"
        "- **Docker MCP** — container/image/compose management across repos.\n"
        "- **Terminal** — docker CLI builds, scans, and logs.\n"
        "- **File tools** — Dockerfile/docker-compose.yml inspection and patches.\n"
        "- **GitHub MCP** — repo discovery and clone workflows.\n"
    ),
    "test-providers-models.prompt.md": (
        "## MCP Servers & Tools\n\n"
        "- **Terminal** — `hermes auth list` and provider/model configuration.\n"
        "- **Delegation** — `delegate_task` parallel capability probes.\n"
        "- **Web tools** — provider documentation lookups.\n"
        "- **Skills** — `test-providers-models` skill (this prompt's engine).\n"
    ),
}

# ---- family computation (first token; fall back to second token) ----
files = sorted(root.glob("*.prompt.md"))
names = [f.name for f in files]
by_first = defaultdict(list)
by_second = defaultdict(list)
for n in names:
    parts = n[:-len(".prompt.md")].split("-")
    by_first[parts[0]].append(n)
    if len(parts) > 1:
        by_second[parts[1]].append(n)

def family_of(n):
    parts = n[:-len(".prompt.md")].split("-")
    if len(by_first[parts[0]]) >= 2:
        return parts[0], sorted(by_first[parts[0]])
    if len(parts) > 1 and len(by_second[parts[1]]) >= 2:
        return parts[1], sorted(by_second[parts[1]])
    return None, []

def related_block(n):
    fam, members = family_of(n)
    if not fam:
        return None
    others = [m for m in members if m != n]
    lines = ["## Related Prompts\n", "\n", "Same-family prompts:\n", "\n"]
    for m in others:
        lines.append(f"- [`{m}`]({m})\n")
    return "".join(lines)

# ---- main pass ----
changed = []  # (name, section)
for f in files:
    text = f.read_text(encoding="utf-8")
    additions = []
    if "## MCP Servers & Tools" not in text and f.name in MCP_BLOCKS:
        additions.append(MCP_BLOCKS[f.name])
        changed.append((f.name, "MCP Servers & Tools"))
    if "## Hooks" not in text:
        additions.append(HOOKS_BLOCK)
        changed.append((f.name, "Hooks"))
    if "## Scripts" not in text:
        additions.append(SCRIPTS_BLOCK)
        changed.append((f.name, "Scripts"))
    if "## Related Prompts" not in text:
        rb = related_block(f.name)
        if rb:
            additions.append(rb)
            changed.append((f.name, "Related Prompts"))
    if not additions:
        continue
    if not text.endswith("\n"):
        text += "\n"
    text = text.rstrip("\n") + "\n\n" + "\n\n".join(additions).rstrip("\n") + "\n"
    if APPLY:
        f.write_text(text, encoding="utf-8", newline="\n")

by_section = defaultdict(int)
for _, s in changed:
    by_section[s] += 1
print(f"SUMMARY: {len(changed)} section addition(s)"
      + ("" if APPLY else " (dry-run — re-run with --apply)"))
for s, c in sorted(by_section.items()):
    print(f"  {s}: {c}")
if not APPLY:
    fams = defaultdict(int)
    for f in files:
        fam, members = family_of(f.name)
        if fam and "## Related Prompts" not in f.read_text(encoding="utf-8"):
            fams[fam] += 1
    print("  families with >=2 members:", len(fams))
