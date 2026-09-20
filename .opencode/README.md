# OpenCode / OpenRouter Sync Reference

# Verified session 2026-09-16

Provider: openrouter (primary), nous (fallback)
Models verified: upstage/solar-pro4:free, deepseek-v4-flash-free, nemotron-3-ultra-free
Auth: vault handles only; .env protected (5274 B workspace / 30269 B hermes home)
MCP sync: .github/mcp.json <-> $HERMES_HOME/mcp.json <-> .vscode/mcp.json (verified)
Config: config.yaml references opencode-zen, openrouter, hermes
Fallback chain: openrouter -> nous -> opencode-zen
Rate limit 403 preserved (future clarification needed)
Identity DRY preserved; .env unchanged; 0 synthetic results
