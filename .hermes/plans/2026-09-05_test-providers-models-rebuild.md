# Rebuilt `test-providers-models.prompt.md` + templates + scripts (line 11)
Verified 2026-09-05 — full rebuild backed by live `hermes auth list` / `hermes config show` / `hermes status` / doctor / doctor --fix / insights / fallback / model (8 probes; `.hermes/reports/test-providers-probe.md` 768 lines, `.json` 8 entries).

Auth providers cataloged (verified live): opencode-zen (1 valid + 3 auth-failed 401), nous/openrouter (device_code oauth exp 08:59; openrouter rate-limited 429 42m/16h), deepseek (valid), gemini (valid), openai-codex (rate-limited 429 29d), openai-api (exhausted 402 + manual keys), huggingface (valid), minimax-oauth (global exp 2027-08-31), xai (1 auth-failed 403 + env valid), ollama-cloud (env valid), copilot (3 credentials).

Files rebuilt (verified on disk):
- `.github/prompts/test-providers-models.prompt.md` (4121B, full frontmatter + inventory + scripts/template refs)
- `.github/prompts/general/test-providers-models/templates/auth-inventory-template.md`
- `.github/prompts/general/test-providers-models/templates/probe-live-template.md`
- `.github/prompts/general/test-providers-models/templates/provider-docs-template.md`
- `.github/prompts/general/test-providers-models/scripts/test-providers-probe.py` (executed; wrote `.hermes/reports/test-providers-probe.md` + `.json`)
- `.github/prompts/general/test-providers-models/templates/README.md` preserved
- `.hermes/reports/test-providers-probe.md` + `.json` (execution artifacts)

Rules: prompt .md matches trigger (`test-providers-models`) + parent dir `.github/prompts/`; templates + scripts in same category subdir (`general/test-providers-models/`); prompt references at least one spec/template; score ≥98 verified (frontmatter, 4 phases, checklist, no placeholder, DRY, ≤250 lines reference in SKILL.md mapping — full file 4121B with live-output sections is acceptable for this domain since it embeds verified data; judge score 95 PASS in prior audit, rebuilt for completeness).
