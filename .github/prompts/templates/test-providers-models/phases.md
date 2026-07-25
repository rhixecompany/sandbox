# Test Providers & Models — Phases

> Full operational phases for `prompts/test-providers-models.prompt.md`.
> Each phase should use web research tools (`web_search`, `web_extract`, `firecrawl-search`, `web-research-pipeline`) alongside local Hermes commands.

## Phase 0: Auth & Provider Inventory

- Enumerate authorized providers using live Hermes auth/config as source of truth.
- **Web research:** for each provider, search their docs page for API reference, model list endpoint, and pricing. Save findings under `docs/research/<provider>/`.
  - OpenRouter: scrape `https://openrouter.ai/models` for full catalog
  - Nous: check `https://docs.nousresearch.com/`
  - Other providers: find their model listing pages via `web_search`
- Gate: all authorized providers captured and documented, with at least one web-research artifact per provider.

## Phase 1: Model Catalog Discovery

- Catalog available models per provider.
- **Web research:** use `firecrawl-search` or `web_extract` on provider model pages to get the full model list (beyond what `hermes auth` shows). Cross-reference against local config.
  - For OpenRouter: `firecrawl-scrape` the models page to extract all model IDs, pricing tiers, and context windows.
  - For HuggingFace: search `https://huggingface.co/models` for inference-enabled models.
  - For GitHub Copilot: check Microsoft docs for available models and switching.
- Gate: catalog entries documented per provider, enriched with web-extracted metadata (pricing, context, capabilities).

## Phase 2: Free Model Extraction

- Extract free-tier or otherwise accessible models into a table.
- **Web research:** search for each provider's free tier offerings — many have free credits, free models, or trial tiers not visible in local config.
  - Search "openrouter free models 2026", "nous free tier", "huggingface inference free tier".
  - Use `web-research-pipeline` to batch-search all providers and consolidate results.
- Gate: free-tier model table complete with web-research cross-reference annotations.

## Phase 3: Provider-by-Provider Benchmarking

- Run lightweight benchmarks/availability checks.
- **Web research:** search for community benchmarks (OpenRouter leaderboard, Artificial Analysis, Chatbot Arena) to contextualize local findings.
  - Pull LMSYS Chatbot Arena results via `web_extract`.
  - Compare local latency/pricing against published community data.
- Gate: benchmark outputs saved per provider/model; web-sourced community context appended to each result.

## Phase 4: Cross-Provider Comparison & Report

- Compare findings across providers/models.
- **Web research:** search for comparison articles, pricing analysis, and performance reviews. Use `research-toolkit` for structured synthesis.
  - Generate a comparison table that blends local benchmarks with web-published data.
  - Note discrepancies between local availability and published documentation.
- Gate: comparison report generated and reviewed.

## Phase 5: Rate Limit & Fallback Chain Analysis

- Document rate-limit behavior and fallback recommendations.
- **Web research:** search for provider status pages, known rate-limit thresholds, and fallback best-practices.
  - Check OpenRouter status page, provider SLA docs.
  - Search "hermes fallback provider configuration best practices" for config guidance.
- Gate: fallback recommendation completed with web-sourced SLA/limit data.

## Phase 6: Script Creation & Automation

- Create or update scripts that capture the above for reruns.
- **Script must include web research calls** — `web_search` / `web_extract` for refreshing provider info before each run, not just local `hermes` commands.
- Document the web research sources used so the script can re-fetch on next run.
- Gate: scripts runnable and preserved; web research sources documented in script header.

## Completion

- Append progress after each phase.
- Append evidence to `docs/orchestrator-verification.md` after each phase.
- All web research artifacts live in `docs/research/` with `SOURCE.md` attribution files.
