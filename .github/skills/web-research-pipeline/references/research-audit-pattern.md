# Research Audit Pattern — Discover, Gap-Analyse, Patch

> **Origin:** UK Earnings Kit update session (2026-07-25) — found existing 11-file kit, identified gaps via 5 Tavily searches, patched 2 files + added 1 new reference.

## When to Use

- You have existing research/knowledge base artifacts and need to bring them current
- Before doing a fresh greenfield research pass — check if re-use is possible
- User asks to "research extensively" on a topic you've already researched

## Anti-Pattern: Greenfield Every Time

**Don't:** Run searches, extract pages, save as markdown — recreating everything from scratch.

**Do:** 
1. Discover what exists
2. Diff it against current needs
3. Research only the gaps
4. Patch existing + add new references

## The Pattern

### Step 1: Discover Existing Artifacts

```python
# Scan the workspace for research artifacts
from hermes_tools import search_files

# Check for knowledge kits, research reports, reference dirs
results = search_files(pattern="*EARNING*", target="files", path=".")
results = search_files(pattern="references/", target="files", path=".")
results = search_files(pattern="RESEARCH_REPORT*", target="files", path="./projects")
```

**What to look for:** `uk-earnings-kit/`, `references/` dirs under active skills, `projects/*/RESEARCH_REPORT.md`, any `kit/` or `guide/` directories.

### Step 2: Assess Coverage vs Staleness

Read the existing files to answer:
- What platforms/categories are covered?
- What's dated? (old offers, closed platforms, stale £/hr estimates)
- What's missing entirely? (new platforms, new categories, new trends)

**Output:** A structured gap list like:
```
Existing: 10 survey sites, 3 AI training platforms, 8 mystery shopping apps
Gaps:     Mercor, Alignerr, Invisible Technologies (new AI platforms)
          Opiday, PaidViewpoint, Sproutful (new survey sites)
          Barclays £200 bank offer (July 2026 deadline)
          Reselling, AI Implementation services (new categories)
```

### Step 3: Targeted Gap Research

For each gap area, run 1 specific Tavily search:

```python
from hermes_tools import mcp_call
# One search per gap area
search1 = mcp_call("tavily_search", query="UK AI training platforms 2026 Mercor Alignerr alternatives")
search2 = mcp_call("tavily_search", query="best UK survey sites 2026 new platforms")
search3 = mcp_call("tavily_search", query="UK bank switching offers July 2026")
```

**Rule:** 3-5 targeted searches > 1 broad search. Each query should target exactly one gap.

### Step 4: Diff & Patch

Compare search findings against existing content:

| Finding | Existing Coverage | Action |
|---------|------------------|--------|
| Mercor $40-150/hr | Not in kit | Add to Tier 1 + new reference file |
| Barclays £200 | Not in kit | Update bank switching section |
| BeMyEye 3M shoppers | Not in kit | Add to mystery shopping list |

**Actions:**
- **Patch existing files** — update sections, add rows to tables
- **Add new reference files** — for deep-dive topics (e.g., `references/ai_training_platforms.md`)
- **Update index/README** — reflect new files in the table of contents

### Step 5: Verify

- Re-read patched files to confirm no structural damage
- Count: new platforms added, sections updated, references created
- Confirm the plan document reflects all changes

## Worked Example

Session: UK Earnings Kit update (2026-07-25)
- **Existing:** 11 files (master guide, 3 refs, 3 templates, 3 trackers, README)
- **Gap analysis:** AI training covered only 2 platforms (DataAnnotation, Outlier) while actual 2026 market has 10+ active platforms
- **Searches:** 5 Tavily searches — AI training, survey alternatives, mystery shopping, bank switching, general side hustles
- **Output:** 12 files now (patched master guide + platform links, new AI training reference + plan)
- **Time saved vs greenfield:** ~60% — didn't recreate templates, trackers, or tax guidance from scratch

## Tools Used

| Tool | Phase | Purpose |
|------|-------|---------|
| Tavily MCP search | Step 3 | Parallel targeted searches |
| read_file | Step 1-2 | Read existing artifacts |
| patch | Step 4 | Update existing files |
| write_file | Step 4 | Create new reference files |
| directory_tree | Step 1 | Map existing structure |

## Pitfalls

- **Don't assume existing research is complete.** Even comprehensive kits get stale fast (platforms launch/close quarterly).
- **Don't skip the gap analysis.** Patching without knowing what's missing leaves the same gaps.
- **Don't over-search.** 5 targeted searches are enough for a knowledge kit. 10+ becomes diminishing returns.
- **Respect existing structure.** Patch into the same file structure and table format rather than reformatting. Consistency makes the kit easier to maintain next time.