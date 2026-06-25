# Hermes Current State — 2026-06-25

> Profile: alexa | Model: deepseek-v4-flash-free | Provider: opencode-zen

## Hooks

| Hook | Events | Scripts | Status |
|------|--------|---------|--------|
| governance-audit | on_session_start, on_session_end, pre_llm_call | audit-prompt.sh, audit-session-end.sh, audit-session-start.sh, hook.sh | ✅ Active |
| session-auto-commit | on_session_end | auto-commit.sh, hook.sh | ✅ Active |
| session-logger | on_session_start, on_session_end, pre_llm_call | hook.sh, log-prompt.sh, log-session-end.sh, log-session-start.sh | ✅ Active |

All hooks have JSON configs + shell scripts in `~/AppData/Local/hermes/hooks/`.

## Plugins

**15 Enabled:**
basic, copilot-provider, custom-provider, disk-cleanup, huggingface-provider, langfuse, nous, nous-provider, ollama-cloud-provider, openai-codex, openai-codex-provider, opencode-zen-provider, openrouter-provider, security-guidance, web-tavily

**51 Disabled (notable):**
- Provider: anthropic, bedrock, deepseek, gemini, nvidia, qwen-oauth, xai, alibaba, arcee, azure-foundry, copilot-acp, kilocode, kimi-coding, minimax, novita, stepfun, xiaomi, zai
- Platform: discord, teams, google_chat, homeassistant, irc, line, mattermost, ntfy, photon, simplex
- Web search: brave-free, ddgs, exa, firecrawl, parallel, searxng, xai
- Media/other: fal, krea, spotify, openai

## Skills

- Default profile skills: 711 directories
- alexa profile skills: 716 directories
- Unique total (deduped): 535

## Provider Chain

| Priority | Provider | Model |
|----------|----------|-------|
| 1 (primary) | opencode-zen | deepseek-v4-flash-free |
| 2 | nous | stepfun/step-3.7-flash:free |
| 3 | openrouter | qwen/qwen3-coder:free |
