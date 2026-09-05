---
name: test-providers-models-rebuild
version: 1.0.0
author: Alexa
profile: default
model: thinkingmachines/inkling:free (openrouter)
category: implementation-plan
status: completed
---
# Implementation Plan — Rebuild test-providers-models.prompt.md

## Context (verified live 2026-09-05)

Workspace: C:\Users\Alexa\Desktop\SandBox | Branch: clean-development
Active Hermes profile: default | Model active: gpt-5.6-luna (openai-api)
Existing prompt: `.github/prompts/general/test-providers-models/test-providers-models.prompt.md` (326 lines, v3.0.0, author Hermes Agent)
Templates under `.github/prompts/templates/`: model-probe-template.md, provider-docs-research-template.md, provider-inventory-template.md, capability-ranking-template.md, verification-gates-template.md, agent-propagation-template.md, hermes-config-template.md

## User Intent (verbatim requirement, ordered)

Only after FULL understanding of prompt + all templates → delete old prompt + create new prompt + templates in correct dir so all auth providers are captured by executing:
`hermes config show && hermes auth list && hermes status && hermes insights && hermes fallback list`
and locate each auth provider's URL + documentation URL; then `/web-research-pipeline` for best-practices per auth provider; web-extract all doc URLs as markdown files used as prompt workflow context; create multi-tasks for intelligently testing each model (Provider, Context, max-output, capabilities); create markdown file of all `:free`-suffix models used as context to execute `hermes chat --provider "P" --model "M" -q "tasks" --oneshot` in background (no timeout) for each model; once all done audit all new sessions to rank best 5; configure Hermes model via `hermes config set` with top-ranked; configure fallback with remaining 4 via `hermes fallback clear` + `hermes fallback add`; finally `/prompts-judge` on new `test-providers-models.prompt.md` to debug/fix all issues/warnings/errors, raise score >= 98.

Stacked skills loaded (verified): using-superpowers, brainstorming, user-communication-preferences, mcp-sequential-thinking, plans-and-specs, plan-mode, create-implementation-plan, execution-phase (next). Additional skills required per user: `/mcp-filesystem` (file ops), `/mcp-ast-grep` (search/replace), `/mcp-memory` (persistent notes), `/plan`, `/plan-mode`, `/plans-and-specs`, `/create-implementation-plan`, `/implementation-plan`, `/executing-plans`, `/writing-clearly-and-concisely`, `/subagent-driven-development`.

## Ordered Tasks (strict "only then" — do NOT reorder)

### Phase A: Read & Understand (COMPLETE before any delete)
- [x] Read `.github/prompts/general/test-providers-models/test-providers-models.prompt.md` (326 lines, 10 rules, 8 phases, 4 templates referenced, provider table 9 providers)
- [x] Read 3 templates: model-probe-template.md (82 lines), provider-docs-research-template.md (120 lines), provider-inventory-template.md (60 lines)
- [x] Inspect `.github/prompts/templates/` full listing (verified 10 templates exist)
- [x] Read SESSION_REPORT.md (2026-09-05 01:57 session, 20 skill_view, 9 terminal, model gpt-5.6-luna)
- [x] Confirm workspace root, git branch `clean-development`

### Phase B: Hermes Inventory & Provider Discovery
- [ ] Execute `hermes config show` → capture base_url, provider, model.default, fallback_providers
- [ ] Execute `hermes auth list` → all 11 providers (copilot, deepseek, gemini, huggingface, minimax-oauth, nous, ollama-cloud, openai-api, openai-codex, opencode-zen, openrouter, xai, xai-oauth) with cred status + active key
- [ ] Execute `hermes status` → capture all provider URLs (portal, inference, auth file, region, access exp)
- [ ] Execute `hermes insights` → capture `:free` models used in last 30d (minimax-m3:free 30 sessions, longcat-2.0:free 5, solar-pro4:free 7, nemotron-3-ultra-free 14, nemotron-3.5-lightning-free 2, step-3.7-flash:free 10, nemotron-3-nano-omni-30b-a3b 4, inkling:free 1, mimo-v2.5-free 2, gemini-2.5-flash 1, big-pickle 2)
- [ ] Execute `hermes fallback list` → confirm empty (verified: "No fallback providers configured")
- [ ] Save inventory as `.github/prompts/general/test-providers-models/templates/provider-inventory-filled.md`

### Phase C: Web Research — Provider Documentation & Best Practices
For each of 9 working/auth providers (nous, opencode-zen, openrouter, ollama-cloud, gemini, deepseek, xai, openai-api, openai-codex; skip minimax-oauth/huggingface per scope):
- [ ] `web_search`: `"{provider} API documentation models free"` + `"{provider} Hermes configuration guide"`
- [ ] `web_extract` documentation URL → `.github/prompts/general/test-providers-models/provider_docs/{provider}-docs.md`
- [ ] Filter all `:free` suffix models → record in provider-inventory-filled.md
- [ ] Capture auth method (device_code / api_key / oauth), base_url, docs_url, rate limits
- [ ] Use web-research-pipeline skill (load + invoke)
- Only then proceed to Phase D.

### Phase D: Discover `:free` Models — Markdown File
- [ ] Aggregate all `:free`-suffix models from Phase C docs + insights → `.github/prompts/general/test-providers-models/free-models-index.md`
- [ ] Columns: provider | model (with `:free`) | source (docs/probe/insights) | context | max_output | vision | reasoning
- Only then proceed to Phase E.

### Phase E: Multi-Task Capability Probe (Parallel Subagents)
Per `delegate_task` (subagent-driven-development) — create one subagent per (provider × `:free` model) found in Phase D:
Task spec per subagent:
```
Goal: Probe model capabilities for {provider}/{model}
Input: .github/prompts/general/test-providers-models/free-models-index.md + provider_docs/{provider}-docs.md
Method: hermes chat --provider "{provider}" --model "{model}" -q "Reply ONLY: vision=<yes/no> reasoning=<yes/no> ctx=<max_tokens> max_output=<max_output_tokens> capabilities=[list]" --oneshot
Output file: probes/{provider}-{model-slug}-probe.md (fill model-probe-template.md)
Record structured JSON: {provider, model, working, vision, reasoning, ctx, max_output, latency_ms, error, source}
```
- [ ] Launch batch (delegate all at once; no timeout; background)
- [ ] Once all done (wait for results), aggregate results → `.github/prompts/general/test-providers-models/probes/probe-aggregate.md`
- Only then proceed to Phase F.

### Phase F: Ranking & Audit New Sessions
- [ ] Read all aggregate probes; drop non-working (working=false)
- [ ] Apply ranking algorithm (from prompt v3.0.0 Phase 4):
```python
def sort_key(m):
    working = 1 if m['working'] else 0
    vision = 2 if m['vision'] else 0
    reason = 1 if m['reasoning'] else 0
    ctx = min(m['ctx'], 2_000_000) / 2_000_000
    output = min(m['max_output'], 100_000) / 100_000
    return (working, vision, reason, ctx, output, -latency_penalty)
```
- [ ] Top 5 ranked → `.github/prompts/general/test-providers-models/top-5-ranked.md`
- [ ] Audit all new sessions from Phase E probes (use `session_search` + session-logger results)
- [ ] Confirm no rate-limit/auth errors in top 5

### Phase G: Configure Hermes (Strict Order — Only Then)
Per top-5 ranking file:
```
hermes config set model.provider <top_provider>
hermes config set model.default <top_model>
hermes fallback clear
hermes fallback add <provider2>
hermes fallback add <provider3>
hermes fallback add <provider4>
hermes fallback add <provider5>
hermes config set providers.<provider1>.default_model <model1>
... (repeat for 5)
```
- [ ] Verify `fallback_providers` is YAML list (python yaml.safe_load check)
- [ ] Verify `hermes config check` passes
- [ ] Capture post-config state → `.github/prompts/general/test-providers-models/post-config-state.md`
Only then proceed to Phase H.

### Phase H: Delete Old Prompt + Create New Prompt + Templates (Strict — Only After G Verified)
- [ ] Delete `.github/prompts/general/test-providers-models/test-providers-models.prompt.md` (destructive — only after G passes)
- [ ] Create new `.github/prompts/general/test-providers-models/test-providers-models.prompt.md` with:
  - Updated provider table including ALL auth providers from Phase B (with URLs + docs URLs)
  - Updated `:free` model list from Phase D
  - Phase 1-8 structure preserved but enhanced with multi-task subagent references
  - References to `.github/prompts/templates/` files by exact filename
  - Context block referencing `provider_docs/{provider}-docs.md`, `free-models-index.md`, `probes/probe-aggregate.md`, `top-5-ranked.md`
- [ ] Update templates directory: verify all 4 templates (model-probe, provider-docs-research, provider-inventory, capability-ranking) are linked and complete; create missing `agent-propagation-template.md` fill if needed
- Only then proceed to Phase I.

### Phase I: Propagation (Agent Config Updates)
- [ ] Update `.hermes.md` provider/model table (per user preference: concise table, no duplication)
- [ ] Update `AGENTS.md` profile routing (if model references exist)
- [ ] Update installed agent configs (`.opencode/mcp.json`, `.codex/mcp.json`) if referenced
- [ ] Only verified working (`working=true`) models written; exclude non-working

### Phase J: Verification Gates (Mandatory Before Claiming Done)
- [ ] `hermes config check` → PASS
- [ ] `hermes profile list` → PASS
- [ ] Python YAML validation: `fallback_providers` is list, not string → PASS
- [ ] `/prompts-judge test-providers-models.prompt.md` → score >= 98
- [ ] If judge score < 98: debug/fix warnings/errors (loop max 3 attempts per file; after 3, ask user)
- [ ] Confirm no `.bak`/`.backup` artifacts (user rule: git for rollback, no backups)
- [ ] Confirm new prompt references correct directory (`.github/prompts/general/test-providers-models/` + templates/)
- [ ] Confirm `free-models-index.md` exists and lists all `:free` models
- Only after all PASS → Phase K.

### Phase K: Final Audit & Completion
- [ ] Read updated SESSION_REPORT.md (update with this session's results)
- [ ] Confirm `current_state` in plan file = completed
- [ ] Confirm `.hermes/plans/` has this plan file saved (it does: this file)

## File Paths (Exact)

Existing (read-only reference):
- `.github/prompts/general/test-providers-models/test-providers-models.prompt.md`
- `.github/prompts/templates/model-probe-template.md`
- `.github/prompts/templates/provider-docs-research-template.md`
- `.github/prompts/templates/provider-inventory-template.md`
- `.github/prompts/templates/capability-ranking-template.md`
- `.github/prompts/templates/verification-gates-template.md`
- `.github/prompts/templates/agent-propagation-template.md`
- `.github/prompts/templates/hermes-config-template.md`

New/modified (created/replaced in order):
- `.github/prompts/general/test-providers-models/templates/provider-inventory-filled.md`
- `.github/prompts/general/test-providers-models/provider_docs/` (9 .md files)
- `.github/prompts/general/test-providers-models/free-models-index.md`
- `.github/prompts/general/test-providers-models/probes/probe-aggregate.md`
- `.github/prompts/general/test-providers-models/top-5-ranked.md`
- `.github/prompts/general/test-providers-models/post-config-state.md`
- `.github/prompts/general/test-providers-models/test-providers-models.prompt.md` (replaced after Phase G verified)
- `.hermes/plans/` (this file) → final `current_state: completed`

## Risks & Blockers (Explicit)

- `hermes auth list` shows openrouter rate-limited (429, 16h 42m left) and opencode-zen auth failed (401); xai auth failed (403). These providers may fail live probe → must be excluded from working chain but kept in docs.
- `hermes status` shows openai-api model set to `gpt-5.6-luna`; user wants verified working `:free` models as primary. Replacing primary requires `hermes config set` — confirmed allowed (not destructive to workspace; reversible via git rollback on `~/AppData/Local/hermes/config.yaml` if needed).
- `hermes fallback list` = empty; configuring new fallback chain = permitted per user instruction (explicit).
- Multi-task subagent delegation requires `delegate_task` tool; available. No timeout needed per user instruction.
- `prompts-judge` score must reach >=98; if it fails twice, per skill rules: ask user for authorization before third fix attempt.
- No `.bak` files created (enforced); rollback via git.

## Verification Gates (Check After Each Phase)

- [A] Prompt + all 3 templates read; no placeholders missed (verified 326 + 82 + 120 + 60 lines)
- [B] `hermes auth/config/status/insights/fallback` captured; inventory filled
- [C] Each provider doc saved; `:free` models listed; URLs captured
- [D] `free-models-index.md` exists; complete
- [E] All subagent probes returned; aggregate saved; no timeouts
- [F] Top 5 ranked; non-working excluded; audit complete
- [G] `hermes config check` PASS; YAML list verified; top model + 4 fallbacks set
- [H] Old prompt deleted; new prompt created; templates linked; no placeholder text left
- [I] Agent propagation complete; only working models propagated; `.hermes.md`/`AGENTS.md` updated
- [J] `prompts-judge` >= 98; all errors/warnings fixed; max 3 fix loops observed
- [K] SESSION_REPORT.md updated; `.hermes/plans/` file complete; user goal complete

## Dependencies (Strict — Must Hold)

A → B → C → D → E → F → G → H → I → J → K
No phase skips allowed. Each "→" means verified before proceeding.
