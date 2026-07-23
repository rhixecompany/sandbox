# Phase 0: Auth & Provider Inventory (Needed ✓)

> Extracted from `test-providers-models.prompt.md` for DRY templating.

## Phase 0: Auth & Provider Inventory (Needed ✓)

**Profile:** `default` | **Persona:** OWL (System Admin)

**Goal:** Run `hermes auth list` to inventory all authorized LLM providers,
their credential status, and auth methods.

**Tools:** `terminal`, `hermes auth list`, `hermes config show`

**Skills:** `using-superpowers`

**Inputs:** Hermes CLI

**Outputs:** Provider inventory table (as shown above)

### Steps

| Step | Action                                    | Tools    | Output                |
| ---- | ----------------------------------------- | -------- | --------------------- |
| 0.1  | Run `hermes auth list`                    | terminal | Raw auth list         |
| 0.2  | Run `hermes config show \| grep provider` | terminal | Provider config chain |
| 0.3  | Check rate-limit status for each provider | terminal | Rate limit report     |
| 0.4  | Compile into provider inventory table     | terminal | Markdown table        |
| 0.5  | Log results to memory                     | memory   | Saved findings        |

### Verification

- [ ] All 6 providers from auth list are captured
- [ ] Credential status documented per provider
- [ ] Rate-limit cooldowns noted where applicable
- [ ] Provider config chain matches auth list

---
