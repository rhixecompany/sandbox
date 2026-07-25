# Aggressive Cleanup Patterns

Concrete recipes from a successful 10-phase aggressive cleanup of a workspace with 330 docs files, 44 scripts, 75 judge results, shallow clones, debug logs, and stale plans.

## Inventory Pattern (Broken Symlink Safe)

```python
# SAFE — targeted scans, not rglob("*")
from pathlib import Path

home = os.environ["HOME"]
sandbox = Path(home) / "Desktop" / "SandBox"

# Use shallow iterdir() for top-level
for f in sorted(sandbox.iterdir()):
    if f.is_file():
        print(f"{f.name}  ({f.stat().st_size}B)")

# Use targeted rglob with exclusions for deeper scans
for f in sorted(sandbox.rglob("*")):
    if f.is_file() and '.git' not in f.parts:
        print(f"{f.relative_to(sandbox)}  ({f.stat().st_size}B)")
```

## Duplicate Detection (Different Zero-Padding)

```python
from hashlib import md5

jr = Path.home() / "Desktop/SandBox/judge_results"
hashes = {}
for f in sorted(jr.iterdir()):
    if f.is_file():
        h = md5(f.read_bytes()).hexdigest()
        hashes.setdefault(h, []).append(f.name)

# Show duplicates
for h, names in hashes.items():
    if len(names) > 1:
        print(f"DUPLICATE: {names}")
```

## Batch Deletion by Glob Pattern

```bash
# Delete 35 files with 5-zero-padded naming
rm -f batch_0000{1..9}_results.md batch_000{10..35}_results.md
```

## Windows File Lock Fallback

```bash
# When rm -rf fails with "Device or resource busy":
cmd.exe /c "rd /s /q C:\path\to\stubborn\directory"
```

## Find Empty Dirs (Symlink-Safe)

```bash
# Limited depth + exclusion prevents timeout on broken symlinks
find . -maxdepth 5 -type d -empty \
  -not -path '*/node_modules/*' \
  -not -path '*/.git/*' \
  -not -path '*/.venv/*' \
  2>/dev/null
```

## Post-Cleanup Verification

```bash
# Verify every deleted path
ls tool thoughts .agents architecture.md folder-structure.md 2>&1

# Count remaining files
echo "docs: $(find docs -type f | wc -l) files"
echo "judge: $(ls judge_results | wc -l) files"
echo "root .md: $(ls *.md | wc -l) files"

# Check manifests
cat skills-lock.json
```

## Category Keep/Delete List

| Category | Action |
|----------|--------|
| `*-context.md`, `*-issues-context.md`, `*-fix-issues-context.md`, `*-verify-context.md` | Delete — pipeline intermediates |
| `dev-init-*.md` | Delete — one-time migration artifacts |
| `sandbox-*.md` | Delete — sandbox experiment reports |
| `patch-*.{json,md}` | Delete — patch application records |
| `WORKFLOW_*.txt`, `PHASE-*.txt` | Delete — workflow summaries |
| `dirs_to_delete*.txt` | Delete — generated deletion lists |
| `final-verification.*` | Delete — one-time verification |
| `consolidation-report.md`, `workspace-consolidation-*.md` | Delete — stale consolidation reports |
| `skill-consolidation-report.md`, `skill-dedup-*.md` | Delete — stale dedup docs |
| `skill-library-triage.{json,md}` | Delete — once triage is done |
| `01-*.md` through `07-*.md` | Keep — Hermes reference guides |
| `INDEX.md`, `QUICK_REFERENCE.md` | Keep — entry points |
| `mcp-servers/` | Keep — MCP documentation |
| `Project_Architecture/` | Keep — architecture blueprints |
| `hermes-docs/` | Keep — Hermes docs |
| `categorization-plan.md` | Keep — structural reference |
| `local-skills.md` | Keep — local skill registry |
| `prompt-inventory.md` | Keep — active prompt inventory |
