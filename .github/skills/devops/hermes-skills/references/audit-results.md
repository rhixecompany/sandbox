# Audit Results Interpretation

## Understanding `hermes skills audit` Output

### Decision Types

**ALLOWED** — Skill passed security scan. Safe to use.

**BLOCKED** — Skill flagged by security scan. Two sub-types:
- `community source + dangerous verdict` — Contains patterns the scanner considers high-risk (env var reads, shell execution, URL fetching, package installs). **These skills are still installed and enabled.** The BLOCKED status is a scan classification, not a functional disablement.
- `community source + caution verdict` — Contains medium-risk patterns. Same: installed and usable.

### Key Insight: Audit Re-scans as "Community" Source

When `hermes skills install` installs from the official registry, the skills are stored locally. When `hermes skills audit` runs, it re-scans them and may classify them as "community" source rather than trusting the original "official" classification. This means:

- Official skills that read API tokens → flagged as "exfiltration" (DANGEROUS)
- Official skills that run shell commands → flagged as "execution" (DANGEROUS)
- Official skills that install packages → flagged as "supply_chain" (DANGEROUS)
- Official skills with low-risk patterns → flagged as "supply_chain" or "network" (CAUTION)

**This is expected behavior.** The audit is conservative by design.

### What `--force` Does

- Works on: CAUTION verdicts (overrides to ALLOWED)
- Does NOT work on: DANGEROUS verdicts (these are always blocked for community source)
- For already-installed official skills: `--force` is irrelevant since the skills are already functional

### When to Worry

Only investigate further if:
1. A skill you just installed doesn't appear in `hermes skills list` at all (install actually failed)
2. A skill shows as "disabled" in `hermes skills list` (not just BLOCKED in audit)
3. `hermes skills audit` reports a skill as missing files or broken SKILL.md

### Example: 94 Official Skills Installed

After installing all 94 official optional skills and running `hermes skills audit --deep`:
- 50 ALLOWED (safe verdict — no risky patterns detected)
- 43 BLOCKED (dangerous/caution verdict — expected for skills that need API tokens, install packages, or run commands)
- 0 actually broken or disabled

All 146 total skills (73 original + 94 new - 21 overlap) were functional.
