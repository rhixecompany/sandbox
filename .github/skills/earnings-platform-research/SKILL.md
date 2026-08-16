---
name: earnings-platform-research
title: "Earnings Platform Country Research"
description: "Find earning platforms paying in a target country/currency."
version: 1.0.2
author: "Hermes Agent"
license: MIT
tags: [research, remote-work, earnings, ai-training, data-annotation, currency, verification]
metadata:
  hermes:
    tags: [curator]
---
# Earnings Platform Country Research

## When to Use
- "Find platforms that pay in Nigeria/NGN" or any single-country earning-platform research (AI training, data annotation, surveys, microtasks, transcription, freelancing).
- "Pay better than / baseline platform" comparisons with per-platform pay rates.
- Recurring user project shape: an earnings kit with one report per country/niche (UK kit exists; NGN kit exists; more likely).
- Questions answered: does platform X actually pay workers in country Y, at what rate, via which rails?

## When NOT to Use
- Pure marketing lists without source verification.
- Single-platform quick lookup (use web_extract directly).

## Core rules (user's standing requirements)
1. **Currency rule**: report every pay rate in the user's currency AND its original equivalent (e.g. "$20/hr = NGN 30,000/hr @ $1 = NGN 1,500"). Never use a third currency; never quote only USD for an NGN user.
2. **Trusted source rule**: every pay rate needs a source URL. No source → mark `(unverified)`.
3. **Per-platform flag**: `YES verified` (official supported-countries list / payment page), `unverified/community` (community/third-party only), `NO` (known closed / not recruitable). Marketing copy never counts as verification. Use the literal tokens "NGN verified? YES / WARN / NO" (or emoji variants) in tables so future sessions can grep them.
4. **Report skeleton**: ratings table at top, currency-adjusted table, per-platform sections, tax notes for the jurisdiction (FIRS for NG), sources with URLs, max ~2,500 words.

## Verification hierarchy (for country availability)
1. Official supported-countries pages (e.g. mercor.com/supported-countries, talent.docs.mercor.com, CrowdGen payments page).
2. Country job boards and local guides (MyJobMag, eCourseware.ng) — good but over-claim sometimes (e.g., one lists Prolific for NG while Prolific's own country list excludes it; trust official when they conflict).
3. Community reports (Reddit r/<platform>, local YouTube/Facebook creators, payout screenshots, "no VPN needed" claims).
4. Independent journalism for closures (e.g., Rest of World: "Remotasks shut down entirely in Kenya, Nigeria, and Pakistan").
5. Nothing found → `unverified`: say so, never assume.

## Workflow
1. **Preflight path check**: on Windows, task-supplied absolute paths often point at a non-existent user dir (e.g., C:/Users/Admin/...). Run `ls -d /c/Users/*` first; write to the real profile dir (C:/Users/<name>/...) and note the deviation in your summary.
2. **Batch searches** (5-6 per round, 3): general platform lists for the country, per-platform "<Platform> <Country> pay", and per-rail queries ("<Platform> payout mode").
3. **Extract aggregators** (high yield): RemoWork-type top-25 lists, aitrainingjobs.it indexes, country job guides (MyJobMag, eCourseware.ng), remotestack-in country tables — plus each platform's official page.
4. **Settle availability** per verification hierarchy; keep one flag per platform.
5. **Assemble report**; then **verify the deliverable**: `ls` + `wc -w` after writing; grep for suspicious/garbled tokens and repair (below).

## Report skeleton (per platform)
- Ratings / quick-compare table: Platform | NGN Verified? | USD/hr | NGN/hr | Payout | Payout speed | Rating source
- NGN-adjusted realistic outlook (not marketing maximums)
- Per-platform blocks: NGN verified? flag, pay (USD + NGN), entry requirements, payout method + speed, payout minimums/caps, sources
- "Do NOT use" list (closed / not recruitable / unverified)
- Payout rails that work from the country (e.g., for Nigeria: PayPal receive with possible volume caps, Payoneer, AirTM, Wise, direct USD wire; Paystack/Flutterwave appear only on local/scam operations — a global "AI job" asking you to pay via Paystack is a scam tell)
- Tax notes (e.g., Nigeria/FIRS: TIN, Self-Assessment by 30 June, WHT not withheld for NG contractors, don't fake foreign residency for better rates)

## Pitfalls (applied in NGN-kit sessions)
- **Wrong absolute path** → verify user dir before writing; report the real path.
- **File vanishes between calls** → always `ls`/`wc -w` the final file; a scripted write can report success without creating it.
- **Garbled words in long generated markdown** → after writing, grep for known mangled tokens; repair with `patch` using EXACT strings read back from the file. A multi-hunk V4A patch fails atomically if one hunk is even slightly off — copy strings from a fresh read, never from memory.
- **"Global/100+ countries" marketing** → means nothing per-country; follow the hierarchy.
- **Re-running a generator script can DESTROY scored data unless it merges.** A "merge/extend" script that rebuilds the master CSV from an embedded base instead of reading the existing on-disk file truncates the artifact on every re-run (observed: `extend_master_list.py` cut an 83-row scored list back to 56 rows, dropping whole categories). RULE: any script that regenerates a scored artifact must be **union-safe** — read the current CSV, add only rows whose unique key (e.g. platform `name`) is absent, then re-score/sort/write. Verify idempotency by running TWICE: second run must report "added 0" and identical counts.
- **Verifying a script by re-running it can be the trigger that truncates** — don't trust a re-run of an unproven generator as a safe check. `py_compile` + a double-run idempotency assertion (added-count = 0) is the minimal safe verification.
- **Region-porting drift**: sweeping every currency/authority token is mandatory, not just the headline rate. The NGN port had a residual `GBP payout` in the scoring matrix and a stale `NGN960,000` tax figure (correct value under Nigeria Tax Act 2025, in force 1 Jan 2026: **tax-free threshold ₦800,000/year**, then 15%/18%/21%/23%/25% bands). Grep the whole prompt + deliverables for old region tokens before dispatch.

## Multi-category kit build (8× fan-out shape)
When the research covers MANY categories (AI-training, surveys, user-testing, bank referral, cashback/receipts, mystery/field, freelancing, passive apps):
1. Dispatch ≤3 leaf subagents per batch (Hermes concurrency cap), each writing a DISJOINT absolute path under the kit (e.g. `platforms/<cat>/<name>.md`); never two subagents to the same file.
2. Build a scored master CSV with one row per platform: `ngn_ph, reliability, ng_access, entry, scalability, tax, t2n_days` → weighted `total` (weights 30/20/15/10/10/10/5 in the NGN kit; keep them in the script header). Eliminate below pay-floor (e.g. ₦1,500/hr) and geo-locked/blocked rows.
3. Ship CSV + formatted `scoring_matrix.xlsx` (openpyxl; blocked rows shaded), `README.md`, `RESEARCH_REPORT.md`, per-category deep-dives, trackers/templates (earnings csv+xlsx, tax tracker, weekly planner, intake template), scam-warnings, signup-requirements, sample week.
4. Relocate strays if a subagent context path silently dropped a folder segment (see `dispatching-parallel-agents`).
5. Release gate: assert `rows==N`, `KEEP==K`, `len(unique)` no dups, no garbage tokens, xlsx opens.

## References
- `references/ngn-ai-training-platforms.md` — verified NGN AI-training platform bank (pay ranges, flags, rails, sources) from the Aug 2026 NGN-kit session. Reuse for future NGN-kit niches (transcription, surveys, freelancing).
- `references/ngn-earnings-kit-2026.md` — full eight-category NGN kit index: 83 platforms scored / 46 KEEP, per-category top picks, payout-rail map incl. PayPal-NG send-only + Cleva/Grey USD virtual rails, real payer caveats (Honeygain min $20 = 4-8 months, TimeBucks complaint-heavy, Chipper account issues). Reuse for future NGN kit builds.

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] "Earnings Platform Country Research" operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
