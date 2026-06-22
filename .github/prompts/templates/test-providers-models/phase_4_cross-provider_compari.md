# Phase 4: Cross-Provider Comparison & Report (Recommended ☆)

> Extracted from `test-providers-models.prompt.md` for DRY templating.

## Phase 4: Cross-Provider Comparison & Report (Recommended ☆)

**Profile:** `research-analyst` | **Persona:** Data Analyst

**Goal:** Compile benchmark results into a cross-provider comparison report
with recommendations.

**Tools:** `terminal`, `memory`, `skills`

**Skills:** `plans-and-specs`, `verification-before-completion`

**Inputs:** Benchmark results from Phase 3

**Outputs:** Final comparison report with recommendations

### Steps

| Step | Action                                     | Output                 |
| ---- | ------------------------------------------ | ---------------------- |
| 4.1  | Aggregate results by provider              | Provider summary table |
| 4.2  | Score each provider on reliability + speed | Provider scores        |
| 4.3  | Rank providers by task type suitability    | Ranked comparisons     |
| 4.4  | Write final report with recommendations    | Comparison report      |
| 4.5  | Save report to memory                      | `memory target=memory` |

### Report Sections

1. **Provider Overview** — Which providers have usable free models
2. **Benchmark Ranking** — Models ranked by task performance
3. **Reliability Score** — Rate limits, uptime, error rates per provider
4. **Recommendations** — Best provider per task type (reasoning, tools, knowledge)
5. **Fallback Chain** — Optimal provider fallback order

### Verification

- [ ] All providers from Phase 0 included in comparison
- [ ] Pass/fail status clear per model per task
- [ ] Rate-limit issues documented
- [ ] Recommendations are actionable and prioritized

---
