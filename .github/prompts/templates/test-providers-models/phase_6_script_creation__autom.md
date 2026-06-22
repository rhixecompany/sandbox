# Phase 6: Script Creation & Automation (Recommended ☆)

> Extracted from `test-providers-models.prompt.md` for DRY templating.

## Phase 6: Script Creation & Automation (Recommended ☆)

**Profile:** `code-architect` | **Persona:** Developer

**Goal:** Create or update the `test_models.py` test harness to support all
6 providers with a unified CLI interface.

**Tools:** `terminal`, `execute_code`, `write_file`

**Skills:** `user-communication-preferences`

**Script target:** `~/AppData/Local/hermes/scripts/test_models.py`

**Inputs:** Provider discovery methods from Phase 1

**Outputs:** Working multi-provider test harness

### Script Requirements

| Requirement            | Priority      | Description                                    |
| ---------------------- | ------------- | ---------------------------------------------- |
| `--list-providers`     | ✓ Needed      | List all configured providers with auth status |
| `--list-free`          | ✓ Needed      | List free models from all providers            |
| `--all-free`           | ✓ Needed      | Benchmark all free models across all providers |
| `--provider NAME`      | ✓ Needed      | Test specific provider only                    |
| `--model MODEL`        | ☆ Recommended | Test specific model only                       |
| `--output FORMAT`      | ◇ Optional    | Output format (table/json/markdown)            |
| Multi-provider support | ✓ Needed      | Handle all 6 auth methods                      |
| Rate-limit handling    | ✓ Needed      | Retry, backoff, and error logging              |

### Steps

| Step | Action                                                 | Output              |
| ---- | ------------------------------------------------------ | ------------------- |
| 6.1  | Read existing `test_models.py` if present              | Current script      |
| 6.2  | Design unified multi-provider interface                | Script spec         |
| 6.3  | Implement provider modules per auth type               | Provider modules    |
| 6.4  | Implement benchmark tasks (reasoning, tool, knowledge) | Benchmark engine    |
| 6.5  | Add CLI argument parsing                               | CLI interface       |
| 6.6  | Add rate-limit handling and retry logic                | Resilient execution |
| 6.7  | Test with `--list-free` and `--provider openrouter`    | Verified script     |

### Verification

- [ ] Script runs without errors
- [ ] All 6 providers discoverable via `--list-providers`
- [ ] Free models listed for at least authenticated providers
- [ ] Benchmark runs produce markdown output
- [ ] Rate-limit errors are caught and logged, not fatal

---
