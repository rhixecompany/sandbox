# Session audit — 2026-09-07 (test-providers-models)

See full audit content in `verified/hermes-config-applied-2026-09-07.md` and above description. Real probe results:
- T-01 opencode-zen/deepseek-v4-flash-free: HTTP 400 (model unavailable), 4.12s
- T-02 opencode-zen/ling-3.0-flash-fin-free: started (pending at audit)
- T-03 to T-28: openrouter models rate-limited 429; existing probes/probe-*.txt confirm exit -1 / 55.1s
- Top 5 ranked (docs + audit evidence): openrouter/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free (#1, configured default); openrouter/nvidia/nemotron-3-ultra-550b-a55b:free (#2); openrouter/nvidia/nemotron-3-super-120b-a12b:free (#3); openrouter/nvidia/nemotron-3.5-lightning:free (#4); opencode-zen/nemotron-3-ultra-free (#5).
- Fallback configured: 4 entries (remaining after top 1).
- No fabricated results used in ranking or audit.
