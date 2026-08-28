---
name: us-earnings-research
title: US Earnings Research
description: Identify and validate US earning platforms that are genuinely better than Outlier and Attapoll across pay, reliability, barrier to entry, and payout speed.
version: 1.0.0
author: Hermes Agent
tags:
  - research
  - us
  - earnings
  - income-generation
  - platforms
  - web-research
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
---
## Table of Contents

## Goal

## Context

## Phases


# Table of Contents

- [us Earnings Research Pipeline](#us-earnings-research-pipeline)
- [Goal](#goal)
- [Context](#context)
- [Skill Stack (Load in Order)](#skill-stack-load-in-order)
- [Phase 0: Context Recovery & Inventory (MANDATORY FIRST)](#phase-0:-context-recovery-&-inventory-mandatory-first)
  - [0.1 Load Prior Session Data](#01-load-prior-session-data)
  - [0.2 Read All Existing Files](#02-read-all-existing-files)
  - [0.3 Honcho Memory Recall](#03-honcho-memory-recall)
- [Phase 1: Systematic Platform Discovery](#phase-1:-systematic-platform-discovery)
  - [1.1 Category Mapping (Brainstorming)](#11-category-mapping-brainstorming)
  - [1.2 Parallel Web Research (Web Research Pipeline)](#12-parallel-web-research-web-research-pipeline)
  - [1.3 MCP Tool Enrichment](#13-mcp-tool-enrichment)
- [Phase 2: Rigorous Filtering & Scoring](#phase-2:-rigorous-filtering-&-scoring)
  - [2.1 Scoring Matrix (Apply to Every Platform)](#21-scoring-matrix-apply-to-every-platform)
  - [2.2 Elimination Criteria (Auto-real Filters](#22-elimination-criteria-auto-real-filters)
- [Phase 3: Deep Validation (Top 20 Platforms)](#phase-3:-deep-validation-top-20-platforms)
  - [3.1 Sign-up Flow Testing (Browser Automation)](#31-sign-up-flow-testing-browser-automation)
  - [3.2 Reddit/Trustpilot/Forum Sentiment Mining](#32-reddit/trustpilot/forum-sentiment-mining)
  - [3.3 Tax & Legal Compliance Check](#33-tax-&-legal-compliance-check)
- [Phase 4: Output Generation — Complete Execution Kit](#phase-4:-output-generation-—-complete-execution-kit)
  - [4.1 Create/Update Folder Structure](#41-create/update-folder-structure)
  - [4.2 Required Output Files](#42-required-output-files)
- [Phase 5: Verification & Handoff](#phase-5:-verification-&-handoff)
  - [5.1 Quality Gates](#51-quality-gates)
  - [5.2 Session Report](#52-session-report)
- [Execution Instructions for Subagents](#execution-instructions-for-subagents)
  - [Orchestrator (You)](#orchestrator-you)
  - [Leaf Subagents](#leaf-subagents)
- [Communication Preferences (from USER.md)](#communication-preferences-from-usermd)
- [Safety & Ethics](#safety-&-ethics)
- [Trigger Phrase](#trigger-phrase)


- [Goal](#goal)
- [Context](#context)
- [Skill Stack (Load in Order)](#skill-stack-load-in-order)
- [Phase 0: Context Recovery & Inventory (MANDATORY FIRST)](#phase-0:-context-recovery-&-inventory-mandatory-first)
  - [0.1 Load Prior Session Data](#01-load-prior-session-data)
  - [0.2 Read All Existing Files](#02-read-all-existing-files)
  - [0.3 Honcho Memory Recall](#03-honcho-memory-recall)
- [Phase 1: Systematic Platform Discovery](#phase-1:-systematic-platform-discovery)
  - [1.1 Category Mapping (Brainstorming)](#11-category-mapping-brainstorming)
  - [1.2 Parallel Web Research (Web Research Pipeline)](#12-parallel-web-research-web-research-pipeline)
  - [1.3 MCP Tool Enrichment](#13-mcp-tool-enrichment)
- [Phase 2: Rigorous Filtering & Scoring](#phase-2:-rigorous-filtering-&-scoring)
  - [2.1 Scoring Matrix (Apply to Every Platform)](#21-scoring-matrix-apply-to-every-platform)
  - [2.2 Elimination Criteria (Auto-real Filters](#22-elimination-criteria-auto-real-filters)
- [Phase 3: Deep Validation (Top 20 Platforms)](#phase-3:-deep-validation-top-20-platforms)
  - [3.1 Sign-up Flow Testing (Browser Automation)](#31-sign-up-flow-testing-browser-automation)
  - [3.2 Reddit/Trustpilot/Forum Sentiment Mining](#32-reddit/trustpilot/forum-sentiment-mining)
  - [3.3 Tax & Legal Compliance Check](#33-tax-&-legal-compliance-check)
- [Phase 4: Output Generation — Complete Execution Kit](#phase-4:-output-generation-—-complete-execution-kit)
  - [4.1 Create/Update Folder Structure](#41-create/update-folder-structure)
  - [4.2 Required Output Files](#42-required-output-files)
- [Phase 5: Verification & Handoff](#phase-5:-verification-&-handoff)
  - [5.1 Quality Gates](#51-quality-gates)
  - [5.2 Session Report](#52-session-report)
- [Execution Instructions for Subagents](#execution-instructions-for-subagents)
  - [Orchestrator (You)](#orchestrator-you)
  - [Leaf Subagents](#leaf-subagents)
- [Communication Preferences (from USER.md)](#communication-preferences-from-usermd)
- [Safety & Ethics](#safety-&-ethics)
- [Trigger Phrase](#trigger-phrase)



## us Earnings Research Pipeline


**Identify and validate us earning platforms that are genuinely better than Outlier and Attapoll** — higher pay, better reliability, us-specific opportunities, lower barrier to entry, faster payouts. Create all necessary files, trackers, and samples for immediate execution.


- **User**: Alexa (us-based, Site Supervisor/Manager background, Rexos Properties May 2025–June 2026)
- **Workspace**: `C:\Users\Alexa\Desktop\SandBox\`
- **Prior Work**: us Earnings Kit created 2026-07-24 at `us-earnings-kit/` (11 files, 4 folders, 3 Tavily searches, 25+ platforms documented)
- **Standing Goal**: "Better than Outlier/Attapoll" — declared complete 2026-07-25 but needs continuous validation

---

## Skill Stack (Load in Order)

```
/using-superpowers
/user-communication-preferences
/brainstorming
/subagent-driven-development
/plan
/plans-and-specs
/web-research-pipeline
```

---

## Phase 0: Context Recovery & Inventory (MANDATORY FIRST)

### 0.1 Load Prior Session Data

```
session_search(query="us earnings kit OR outlier OR attapoll OR us earning platforms", limit=5)
```

- Retrieve all prior research sessions
- Extract platform lists, pay rates, verification status, user feedback
- Identify gaps in previous coverage

### 0.2 Read All Existing Files

```
search_files(target="files", path="C:/Users/Alexa/Desktop/SandBox", file_glob="**/*.md")
search_files(target="files", path="C:/Users/Alexa/Desktop/SandBox", file_glob="**/*.txt")
search_files(target="files", path="C:/Users/Alexa/Desktop/SandBox", file_glob="**/*.json")
```

- Load `us-earnings-kit/` completely
- Load any `references/*.md`, `trackers/*.md`, `templates/*.md`
- Load session reports, memory files, skill outputs

### 0.3 Honcho Memory Recall

```
honcho_search(query="us earning platforms OR Outlier OR Attapoll OR survey sites OR AI training us")
honcho_search(query="bank switching us OR side hustle us 2026")
honcho_context(peer="user")
```

---

## Phase 1: Systematic Platform Discovery

### 1.1 Category Mapping (Brainstorming)

Use `/brainstorming` to generate platform categories:

- AI Training / Data Annotation (Outlier competitors)
- Survey & Micro-tasks (Attapoll competitors)
- User Testing / UX Research
- Market Research Panels
- Bank Switching / Financial Incentives
- Cashback / Receipt Scanning
- Mystery Shopping / Field Tasks
- Freelance / Gig Platforms (us-specific)
- Content / Creator Monetization
- Affiliate / Referral Programs
- Passive Income Apps
- Skill-based Platforms

### 1.2 Parallel Web Research (Web Research Pipeline)

Dispatch **parallel subagents** via `/subagent-driven-development` — one per category:

```python
delegate_task(tasks=[
```json
{"goal": "Find top 10 us AI training/data annotation platforms (Outlier alternatives). For each: pay rate £/hr, entry requirements, payout speed, Trustpilot score, us tax treatment, referral link", "role": "leaf"},
{"goal": "Find top 10 us survey/micro-task apps (Attapoll alternatives). For each: £/hour effective, minimum payout, survey availability us, disqualification rate, app store rating", "role": "leaf"},
{"goal": "Find top 10 us user testing/UX research platforms. For each: £/test, test frequency us, device requirements, payment terms, screener pass rate", "role": "leaf"},
{"goal": "Find all current us bank switching offers (Jul 2026). For each: bonus £, eligibility, direct debit reqs, credit check type, switch service used, referral bonus", "role": "leaf"},
{"goal": "Find us cashback/receipt apps ranked by actual annual return. Include: TopCashback, Quidco, Airtime Rewards, Shopmium, GreenJinn, ZipZero, loyalty cards", "role": "leaf"},
{"goal": "Find us mystery shopping/field task platforms. For each: pay per task, geographic coverage, reimbursement policy, schedule flexibility", "role": "leaf"},
{"goal": "Find us freelance/gig platforms for site supervisor/management background. Include: construction, property, facilities management, health & safety", "role": "leaf"},
{"goal": "Find us passive income apps (bandwidth sharing, data donation, lockscreen). Measure: £/month actual, battery/data impact, privacy score", "role": "leaf"},
```

], role="orchestrator")
```

### 1.3 MCP Tool Enrichment

For each platform discovered, use **Tavily MCP** for deep extraction:

```
mcp__tavily__tavily_search(query="[platform name] us review 2026 pay rate Trustpilot")
mcp__tavily__tavily_extract(urls=["[platform URL]", "[Trustpilot URL]", "[Reddit us thread]"])
mcp__tavily__tavily_research(topic="[platform name] us tax implications HMRC trading allowance")
```

Use **Firecrawl MCP** for full-site extraction:

```
mcp__firecrawl_scrape__firecrawl_scrape(url="[platform dashboard/help center]")
mcp__firecrawl_crawl__firecrawl_crawl(url="[platform site]", limit=50)
```

---

## Phase 2: Rigorous Filtering & Scoring

### 2.1 Scoring Matrix (Apply to Every Platform)

| Dimension | Weight | Measurement |
| -------------------- | ------ | --------------------------------------------------- |
| **Effective £/hour** | 30% | Realistic after disqualifications, wait times |
| **Reliability** | 20% | Payout consistency, platform age, company stability |
| **us Accessibility** | 15% | us sign-up, GBP payout, us support, no VPN needed |
| **Entry Barrier** | 10% | Skills, equipment, approval time, invitation-only |
| **Scalability** | 10% | Hourly cap, task availability, referral multiplier |
| **Tax Efficiency** | 10% | Trading allowance eligible, expense deductibility |
| **Time to First £** | 5% | Days from sign-up to withdrawable balance |

### 2.2 Elimination Criteria (Auto-real Filters

- ❌ Pay < £5/hr effective
- ❌ No us payout method (PayPal us, us bank transfer, Wise GBP)
- ❌ >30% disqualification rate on surveys
- ❌ Trustpilot < 3.5 or < 100 reviews
- ❌ Invitation-only with no public waitlist
- ❌ Known payment delays > 14 days
- ❌ Requires US SSN / ITIN / W-8BEN without us alternative

---

## Phase 3: Deep Validation (Top 20 Platforms)

### 3.1 Sign-up Flow Testing (Browser Automation)

For each top candidate:

```
browser_navigate(url="[signup URL]")
browser_snapshot(full=true)
# Document: steps, ID verification, phone verification, bank link, time to first task

```

### 3.2 Reddit/Trustpilot/Forum Sentiment Mining

```
mcp__tavily__tavily_search(query="[platform] us Reddit 2026 payment proof")
mcp__tavily__tavily_search(query="[platform] us banned account review")
mcp__tavily__tavily_search(query="[platform] vs Outlier vs Attapoll us")
```

### 3.3 Tax & Legal Compliance Check

- HMRC trading allowance (£1,000) applicability
- Self-assessment threshold
- Expense tracking requirements
- Platform provides tax documents?

---

## Phase 4: Output Generation — Complete Execution Kit

### 4.1 Create/Update Folder Structure

```
C:\Users\Alexa\Desktop\SandBox\us-earnings-kit\
├── platforms/
│ ├── ai-training/
│ ├── surveys-microtasks/
│ ├── user-testing/
│ ├── bank-switching/
│ ├── cashback-receipts/
│ ├── mystery-shopping/
│ ├── freelance-gigs/
│ └── passive-apps/
├── references/
│ ├── platform_master_list.csv
│ ├── scoring_matrix.xlsx
│ ├── signup_requirements.md
│ ├── tax_guidance_us_2026.md
│ ├── scam_warnings.md
│ └── platform_links.md
├── trackers/
│ ├── earnings_tracker.xlsx
│ ├── tax_tracker.md
│ ├── bank_switch_log.md
│ ├── weekly_planner.md
│ └── referral_tracker.md
├── templates/
│ ├── platform_evaluation.md
│ ├── weekly_routine.md
│ ├── expense_log.csv
│ └── signup_checklist.md
├── samples/
│ ├── sample_earnings_week.xlsx
│ ├── sample_tax_return_snippet.md
│ └── sample_referral_messages.md
└── RESEARCH_REPORT.md
```

### 4.2 Required Output Files

| File | Purpose |
| ------------------------------------- | ------------------------------------------------------------------- |
| `platforms/*/platform_name.md` | Deep-dive per platform (signup, pay, tasks, pros/cons, screenshots) |
| `references/platform_master_list.csv` | All platforms with scores, filterable |
| `references/scoring_matrix.xlsx` | Weighted scores, ranked, conditional formatting |
| `references/platform_links.md` | Direct signup/referral links (affiliate where beneficial) |
| `references/tax_guidance_us_2026.md` | HMRC rules, trading allowance, allowable expenses, record-keeping |
| `references/scam_warnings.md` | Red flags, known scams, verification checklist |
| `trackers/earnings_tracker.xlsx` | Multi-platform, auto-sum, tax-year tabs |
| `trackers/tax_tracker.md` | Running total vs £1,000 allowance, SA trigger alert |
| `trackers/weekly_planner.md` | Time-blocked routine, platform rotation, KPI targets |
| `templates/platform_evaluation.md` | Reusable for new platforms |
| `templates/weekly_routine.md` | Printable, checkbox-driven |
| `samples/sample_earnings_week.xlsx` | Realistic example |
| `RESEARCH_REPORT.md` | Executive summary, top 5 recommendations, 30-day action plan |

---

## Phase 5: Verification & Handoff

### 5.1 Quality Gates

- [ ] All platforms have ≥3 independent sources
- [ ] Pay rates verified via recent (≤3 months) us user reports
- [ ] Tax guidance cites HMRC.gov.us pages
- [ ] No affiliate links without disclosure
- [ ] All trackers open in Excel/Google Sheets without errors
- [ ] Weekly planner fits A4 printable

### 5.2 Session Report

```
session_search() → capture this session's work
Update SESSION_REPORT.md with: platforms found, files created, gaps, next actions
```

---

## Execution Instructions for Subagents

### Orchestrator (You)

1. Load all 7 skills in order
2. Execute Phase 0 — report inventory
3. Dispatch 8 parallel leaf subagents (Phase 1.2)
4. Collect results → deduplicate → score (Phase 2)
5. Dispatch validation subagents for top 20 (Phase 3)
6. Generate all output files (Phase 4)
7. Verify quality gates (Phase 5)

### Leaf Subagents

- **MUST** use Tavily MCP + Firecrawl MCP + web_search + web_extract
- **MUST** cite sources with URLs and timestamps
- **MUST** output structured JSON + markdown per platform
- **MUST NOT** fabricate pay rates — mark "unverified" if no source
- **REPORT** blockers immediately via clarify if needed

---

## Communication Preferences (from USER.md)

- **Concise bullets**, lead with result, skip fluff
- **Action-first**: command then explanation
- **Batch independent calls** — parallelize everything
- **Honest blockers**: report directly, never fabricate
- **Verify before claim**: test, check, confirm before reporting

---

## Safety & Ethics

- No referral fraud, no multi-accounting, no VPN spoofing
- Disclose affiliate relationships
- Respect platform ToS
- us tax compliance first — trading allowance is a shield, not a loophole
- Flag any platform requiring upfront payment

---

## Trigger Phrase

> **"/us-earnings-research-pipeline"** — loads this entire prompt as the task instruction

---

_Generated by Hermes Agent using stacked skill bundles. This prompt is idempotent — re-running updates existing files without duplication._
