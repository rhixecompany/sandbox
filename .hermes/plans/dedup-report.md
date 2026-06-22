# Dedup Report — Docs & Research Consolidation

## Exact Duplicates Found

| Group | Files | Type | Action |
|-------|-------|------|--------|
| skills-reports/ (all) | 284 | Auto-generated judge reports — templated, 169 identical, 115 with minor issues | DELETE all (regeneratable via batch_skill_judge.py) |
| skills-audit/ (individual) | 176 | Auto-generated per-skill audits — aggregate exists in index.md | DELETE 176 individual, KEEP index.md |

## Consolidation Candidates

| Group | Files → | Target | Action |
|-------|---------|--------|--------|
| Project_Architecture/ | 51 → 17 | Merge per-project triples into single doc | CONSOLIDATE (subagent dispatched) |
| multi-agent-research/ | 12 → 3 | Merge phase summaries | CONSOLIDATE |
| skills-reports/ | 284 → 0 | Delete all (regeneratable) | DELETE |
| skills-audit/ | 177 → 1 | Keep only index.md | DELETE 176 |

## Unique Content to Preserve (No Dedup)

| Category | Files | Rationale |
|----------|-------|-----------|
| mcp-research/ | 34 | Unique MCP server evaluations |
| research/*/ | 25 | Unique tutorial/research content per API |
| hermes/ | 13 | Official Hermes docs |
| user-guide/ + guides/ + getting-started/ | 11 | Hermes guidance |
| plans/ + specs/ + misc | 9 | Implementation plans |
| multi-agent-research/ | 12 | Phase summaries (consolidating, not deleting) |

## Summary

| Metric | Value |
|--------|-------|
| Files before dedup | 616 |
| Files to delete | 460 (skills-reports: 284 + skills-audit-individual: 176) |
| Files to consolidate | 51 (Project_Architecture triples) |
| Files to keep | 97 (all hand-authored + index.md) |
| Files after dedup | ~112 |
| Space savings | ~1.2MB (450K + 788K) |
