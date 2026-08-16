---
name: research-actionable-kit
title: "Research to Actionable Kit"
description: "Turn research findings into organized, actionable deliverable kits with templates, trackers, and references. Use when user asks for research + 'create all needed files/samples' or 'give me everything I need to start'."
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: [research, deliverable, templates, trackers, actionable-output]
metadata:
  hermes:
    tags: [imported]
---
# Research to Actionable Kit

## Overview

Automated reasoning and workflow tool for `research-actionable-kit`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## Goal
Transform raw research into a self-contained, immediately usable kit that the user can start executing from Day 1 — not just a report they have to figure out how to apply.

## When to Use
- User asks for research AND "create all needed files/samples/templates"
- User wants "everything I need to start earning/doing X"
- Research output must be actionable, not just informational
- Deliverable should include: main guide, templates, trackers, references, index

## When NOT to Use
- Pure research synthesis without actionable output
- One-off answers or summaries
- When user only wants a report/analysis

## Trigger Phrases
- "research X and create all files I need"
- "give me everything to start Y"
- "create templates, trackers, and references for Z"
- "make it actionable / give me a kit"

---

## Workflow

### Phase 1: Research & Synthesis
1. **Load previous session data** — Use `session_search` for prior research on same topic
2. **Conduct new research** — Use MCP tools (Tavily, web_search, web_extract) + community sources (Reddit, forums)
3. **Cross-validate** — Verify each finding against 2+ independent sources
4. **Structure findings** — Organize by priority tiers, £/hr, effort, prerequisites

### Phase 2: Kit Architecture
Design the kit structure before writing:

```
<topic>-kit/
├── <TOPIC>_MASTER.md           # Main guide: rankings, comparisons, strategy
├── templates/                  # Copy-and-use starter files
│   ├── <routine>_planner.md    # Printable routines/checklists
│   ├── <daily>_tracker.csv     # Importable logs (Sheets/Excel)
│   └── <onboarding>_checklist.md # Step-by-step setup
├── trackers/                   # Ongoing monitoring
│   ├── tax_<topic>.md          # Tax/compliance records
│   ├── monthly_summary.csv     # Month-end rollups
│   └── <specific>_log.md       # Domain-specific logs
├── references/                 # Supporting knowledge
│   ├── platform_links.md       # Direct URLs, dashboard bookmarks
│   ├── <regulatory>_guidance.md # Legal/tax rules
│   └── scam_warnings.md        # Red flags, verification
└── README.md                   # Index + quick start
```

### Phase 3: Content Creation Rules

#### Main Guide (`*_MASTER.md`)
- Executive summary table (priority, £/hr, monthly potential, effort)
- Detailed breakdown by tier/category
- Real user data (community reports, not theoretical maxes)
- Strategy synthesis (optimal stack by user level)
- Tax/legal reality check
- Confidence assessment + methodology

#### Templates (`templates/`)
- **Planners**: Printable, tick-box routines with time estimates
- **Trackers**: CSV format for Sheets/Excel import, minimal columns
- **Checklists**: Priority-ordered, verification columns, week-by-week

#### Trackers (`trackers/`)
- Tax-compliant (HMRC/IRS/local rules)
- Separate trading vs non-trading income
- Allowance tracking (trading allowance, PSA, etc.)
- Month-end rollup template

#### References (`references/`)
- Direct signup URLs (no search required)
- Regulatory guidance in plain language
- Scam red flags + verification checklist
- Community sources for ongoing updates

#### README.md
- 5-minute quick start
- Directory structure map
- Optimal stack summary table
- Real earnings data
- Tool stack recommendations
- Maintenance schedule

### Phase 4: Quality Gates
Before delivering, verify:
- [ ] Every platform has direct signup link in `references/platform_links.md`
- [ ] All CSV templates import cleanly (no trailing commas, consistent headers)
- [ ] Tax guidance matches current tax year rules
- [ ] Real community data cited (not marketing claims)
- [ ] Scam warnings include verification steps
- [ ] README quick-start works end-to-end

---

## Pitfalls

| Pitfall | Prevention |
|---------|------------|
| **Report, not kit** | Always include templates/, trackers/, references/ — not just a .md file |
| **Theoretical earnings** | Use only real user reports (Reddit, forums) with dates; mark theoretical maxes explicitly |
| **Missing tax context** | Always include tax tracker + guidance for user's jurisdiction |
| **Dead links** | Verify every URL in platform_links.md; use official domains only |
| **No priority order** | Tier platforms: High £/hr → Medium → Fillers → Passive; number them |
| **Over-engineering** | Keep templates minimal — user modifies, doesn't admire |
| **Jurisdiction blindness** | Tax guidance must match user's country (UK in this session) |

---

## Skill Integration

### With `web-research-pipeline`
- This skill CONSUMES research from web-research-pipeline
- web-research-pipeline = gather; research-actionable-kit = package + deliver

### With `plans-and-specs`
- If kit is complex (>10 files), write a plan first using plans-and-specs
- Then execute kit creation per plan

### With `writing-skills`
- Follow SKILL.md structure for any new skill created from kit pattern

---

## Templates Provided

This skill includes templates in `templates/`:
- `kit_structure.yaml` — folder/file scaffold for new kits
- `master_guide_template.md` — starter structure for main guide
- `csv_tracker_template.csv` — minimal daily log columns
- `checklist_template.md` — priority-ordered onboarding

## Scripts Provided

Scripts in `scripts/`:
- `verify_kit.py` — validates kit completeness (links, CSV, required files)
- `generate_readme.py` — auto-generates README.md from kit manifest

---

## Verification Checklist

- [ ] Kit has all 5 directories: templates/, trackers/, references/, (optional scripts/), root
- [ ] Main guide has executive summary table + tiered detail
- [ ] At least 3 template types: planner, tracker, checklist
- [ ] Tax tracker matches user's jurisdiction
- [ ] Platform links verified (no 404s)
- [ ] Scam warnings have decision tree
- [ ] README has 5-min quick start + directory map
- [ ] Real earnings data cited with sources/dates

---

## Example: This Session's Output

**Input:** "research UK earning sites better than Outlier/Attapoll, create all files I need"

**Output:** `uk-earnings-kit/` with 11 files:
- `UK_EARNING_SITES_MASTER.md` (330 lines, 6 tiers, real user data)
- `templates/weekly_planner.md` (printable 7-day routine)
- `templates/earnings_tracker.csv` (Sheets-ready daily log)
- `templates/signup_checklist.md` (priority-ordered, verification columns)
- `trackers/tax_tracker.md` (UK trading allowance, PSA, matched betting exempt)
- `trackers/monthly_summary_template.csv` (month-end rollup)
- `trackers/bank_switch_log.md` (current 2026 offers, CASS process)
- `references/platform_links.md` (25+ direct signup URLs)
- `references/tax_guidance_uk.md` (HMRC rules, allowances, decision tree)
- `references/scam_warnings.md` (red flags, verification, avoid list)
- `README.md` (5-min start, structure map, optimal stack table)

---

*Created from session: UK earnings kit delivery (2026-07-25). Pattern: research → synthesize → structured actionable kit.*

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
