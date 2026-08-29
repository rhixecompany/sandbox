---
name: uk-earnings-research-pipeline
title: UK Earnings Research Pipeline
description: Comprehensive stacked-skills pipeline to discover, filter, validate, and rank superior UK earning platforms, leveraging prior session data and MCP tools.
trigger: /uk-earnings-research-pipeline
version: 1.0.0
author: Hermes Agent
tags:
  - research
  - uk
  - earnings
  - pipeline
  - skills
  - income-generation
metadata:
  hermes:
    profile: code-architect
    priority: medium
  copilot:
    model_required: sonnet
  opencode:
    enabled: true
  codex:
    enabled: true
toolsets:
  - file
  - terminal
skills:
  - skill:using-superpowers
dependencies: []
formatter: markdown
license: MIT
---
## Table of Contents

## Goal

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Personas](#personas)
- [Personality](#personality)
- [Rules](#rules)
  - [Domain Rules](#domain-rules)
  - [Standing Rules](#standing-rules)
- [Phases](#phases)
  - [Phase 0: Context Recovery & Inventory (MANDATORY FIRST)](#phase-0:-context-recovery-&-inventory-mandatory-first)
  - [Phase 1: Systematic Platform Discovery](#phase-1:-systematic-platform-discovery)
  - [Phase 2: Rigorous Filtering & Scoring](#phase-2:-rigorous-filtering-&-scoring)
  - [Phase 3: Deep Validation (Top 20 Platforms)](#phase-3:-deep-validation-top-20-platforms)
  - [Phase 4: Output Generation — Complete Execution Kit](#phase-4:-output-generation-—-complete-execution-kit)
  - [Phase 5: Verification & Handoff](#phase-5:-verification-&-handoff)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Subgoals](#subgoals)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)



- [Goal](#goal)
- [Context](#context)
- [Personas](#personas)
- [Personality](#personality)
- [Rules](#rules)
- [Domain Rules](#domain-rules)
- [Standing Rules](#standing-rules)
- [Phases](#phases)
- [Phase 0: Context Recovery & Inventory (MANDATORY FIRST)](#phase-0:-context-recovery-&-inventory-mandatory-first)
- [Phase 1: Systematic Platform Discovery](#phase-1:-systematic-platform-discovery)
- [Phase 2: Rigorous Filtering & Scoring](#phase-2:-rigorous-filtering-&-scoring)
- [Phase 3: Deep Validation (Top 20 Platforms)](#phase-3:-deep-validation-top-20-platforms)
- [Phase 4: Output Generation — Complete Execution Kit](#phase-4:-output-generation-—-complete-execution-kit)
- [Phase 5: Verification & Handoff](#phase-5:-verification-&-handoff)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Subgoals](#subgoals)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)





**Identify and validate UK earning platforms that are genuinely better than Outlier and Attapoll** — higher pay, better reliability, UK-specific opportunities, lower barrier to entry, faster payouts. Create all necessary files, trackers, and samples for immediate execution.


- **User**: Alexa (UK-based, Site Supervisor/Manager background, Rexos Properties May 2025–June 2026)
- **Workspace**: `C:\Users\Alexa\Desktop\SandBox\`
- **Prior Work**: UK Earnings Kit created 2026-07-24 at `uk-earnings-kit/` (11 files, 4 folders, 3 Tavily searches, 25+ platforms documented)
- **Standing Goal**: "Better than Outlier/Attapoll" — declared complete 2026-07-25 but needs continuous validation

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Research Analyst** | Platform discovery, data extraction, scoring |
| **UK Tax Advisor** | HMRC compliance, trading allowance, expense tracking |
| **QA Engineer** | Signup flow testing, validation gates, quality checks |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep, fabricated data
- **Encourage**: Evidence-based decisions, MCP-first tooling, parallel execution

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- **No fabricated pay rates** — mark "unverified" if no independent source
- **UK tax compliance first** — trading allowance (£1,000) is a shield, not a loophole
- **Scam elimination criteria are mandatory** — auto-reject platforms failing thresholds
- **Affiliate disclosure required** — flag any referral links
- **Minimum 3 independent sources per platform** — Reddit, Trustpilot, official, user reports

### Standing Rules

1. **Map before touch** — Inventory all prior session data before new research
2. **Parallel first** — Dispatch subagents for independent categories simultaneously
3. **Smallest safe change** — Update files incrementally, verify each write
4. **Verify before claim** — Test trackers open in Excel, validate links resolve
5. **Report blockers** — State when a platform lacks verifiable data


### Phase 0: Context Recovery & Inventory (MANDATORY FIRST)

- `session_search(query="uk earnings kit OR outlier OR attapoll OR UK earning platforms", limit=5)`
- `search_files(target="files", path="C:/Users/Alexa/Desktop/SandBox", file_glob="**/*.md")`
- `honcho_search(query="UK earning platforms OR Outlier OR Attapoll OR survey sites OR AI training UK")`
- `honcho_context(peer="user")`

### Phase 1: Systematic Platform Discovery

**1.1 Category Mapping** — Use `/brainstorming` for 10 platform categories
**1.2 Parallel Web Research** — Dispatch 8 leaf subagents via `/subagent-driven-development`:

- AI Training / Data Annotation (Outlier alternatives)
- Survey & Micro-tasks (Attapoll alternatives)
- User Testing / UX Research
- Market Research Panels
- Bank Switching / Financial Incentives
- Cashback / Receipt Scanning
- Mystery Shopping / Field Tasks
- Freelance / Gig Platforms (UK construction/property/facilities)
**1.3 MCP Tool Enrichment** — Tavily (search/extract/research) + Firecrawl (scrape/crawl) for each platform

### Phase 2: Rigorous Filtering & Scoring

**2.1 Scoring Matrix** (weighted):

- Effective £/hour: 30%
- Reliability: 20%
- UK Accessibility: 15%
- Entry Barrier: 10%
- Scalability: 10%
- Tax Efficiency: 10%
- Time to First £: 5%

**2.2 Elimination Criteria** (auto-reject):

- Pay < £5/hr effective
- No UK payout method (PayPal UK, UK bank transfer, Wise GBP)
- >30% disqualification rate on surveys
- Trustpilot < 3.5 or < 100 reviews
- Invitation-only with no public waitlist
- Known payment delays > 14 days
- Requires US SSN/ITIN/W-8BEN without UK alternative

### Phase 3: Deep Validation (Top 20 Platforms)

**3.1 Sign-up Flow Testing** — Browser automation for each top candidate
**3.2 Sentiment Mining** — Reddit/Trustpilot/Forum searches via Tavily
**3.3 Tax & Legal Compliance** — HMRC trading allowance, SA thresholds, expense tracking

### Phase 4: Output Generation — Complete Execution Kit

Create folder structure at `uk-earnings-kit/` with:

- `platforms/` — per-category deep-dives
- `references/` — master CSV, scoring XLSX, links, tax guidance, scam warnings
- `trackers/` — earnings XLSX, tax tracker, bank switch log, weekly planner, referral tracker
- `templates/` — platform evaluation, weekly routine, expense log, signup checklist
- `samples/` — sample earnings week, tax return snippet, referral messages
- `RESEARCH_REPORT.md` — executive summary, top 5 recommendations, 30-day action plan

### Phase 5: Verification & Handoff

- All platforms ≥3 independent sources
- Pay rates verified via recent (≤3 months) UK user reports
- Tax guidance cites HMRC.gov.uk pages
- No affiliate links without disclosure
- All trackers open in Excel/Google Sheets without errors
- Weekly planner fits A4 printable
- Update `SESSION_REPORT.md`

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content
2. **Structured output** — Use clear sections with consistent heading levels
3. **Verification gates** — Always verify before claiming completion
4. **Minimal changes** — Fix root cause, not symptoms
5. **Parallel execution** — Batch independent MCP calls and subagent tasks
6. **Evidence-based** — Cite URLs and timestamps for every claim

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Inventory | All prior session data loaded and referenced |
| 2 | Discovery | 8 categories researched, ≥50 platforms found |
| 3 | Scoring | All platforms scored, elimination criteria applied |
| 4 | Validation | Top 20 deep-validated with browser + sentiment |
| 5 | Outputs | All folders/files created, trackers functional |
| 6 | Quality | Gates passed, session report updated |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow |
| `user-communication-preferences` | Concise, action-first, DRY output |
| `brainstorming` | Structured idea generation for categories |
| `subagent-driven-development` | Parallel leaf subagents for research |
| `plan` | Markdown plan to `.hermes/plans/` |
| `plans-and-specs` | Implementation plans, specs, decomposition |
| `web-research-pipeline` | Web search → extract → scrape → save workflow |

## MCP Servers & Tools

The following MCP servers and tools are available. Use them in preference to native equivalents per MCP-first tooling policy.

| MCP Server | Tools Used |
| ------------ | ------------ |
| `tavily` | `tavily_search`, `tavily_extract`, `tavily_research`, `tavily_crawl`, `tavily_map` |
| `firecrawl` | `firecrawl_scrape`, `firecrawl_crawl`, `firecrawl_map`, `firecrawl_search`, `firecrawl_extract` |
| `playwright` | `browser_navigate`, `browser_snapshot`, `browser_click`, `browser_type`, `browser_wait_for` |
| `github` | Repository operations if needed |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex scoring |

## Tasks

- [ ] Phase 0: Load all prior session data and existing files
- [ ] Phase 1: Brainstorm categories → dispatch 8 parallel subagents → MCP enrich
- [ ] Phase 2: Apply scoring matrix → filter with elimination criteria
- [ ] Phase 3: Deep validate top 20 (browser + sentiment + tax)
- [ ] Phase 4: Generate complete `uk-earnings-kit/` folder structure
- [ ] Phase 5: Verify quality gates → update session report

## Subgoals

1. **Prepare** — Understand requirements, load context, inventory prior work
2. **Discover** — Systematic platform discovery across 8 categories
3. **Evaluate** — Score, filter, validate with evidence
4. **Generate** — Create all execution files, trackers, templates
5. **Verify** — Quality gates, functional testing, handoff documentation

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section

## Related Prompts

Same-family prompts:

- [`uk-earnings-research.prompt.md`](uk-earnings-research.prompt.md)