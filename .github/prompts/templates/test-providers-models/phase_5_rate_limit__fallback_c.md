# Phase 5: Rate Limit & Fallback Chain Analysis (Optional ◇)

> Extracted from `test-providers-models.prompt.md` for DRY templating.

## Phase 5: Rate Limit & Fallback Chain Analysis (Optional ◇)

**Profile:** `adminbot` | **Persona:** DevOps Engineer

**Goal:** Analyze provider rate limits, cooldown periods, and optimal fallback
chain configuration.

**Tools:** `terminal`, `provider-reliability-diagnostics` skill

**Skills:** `plans-and-specs`

**Inputs:** Rate limit data from Phase 3

**Outputs:** Fallback chain recommendation

### Steps

| Step | Action                                   | Output                |
| ---- | ---------------------------------------- | --------------------- |
| 5.1  | Analyze rate-limit patterns per provider | Rate limit report     |
| 5.2  | Test fallback chain switching            | Fallback test results |
| 5.3  | Recommend optimal provider order         | Config recommendation |
| 5.4  | Document cooldown periods per provider   | Cooldown reference    |

### Verification

- [ ] Provider failover works end-to-end
- [ ] Cooldown periods are empirically measured
- [ ] Fallback chain config is documented

---
