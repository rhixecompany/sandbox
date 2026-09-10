# Hermes Log Analysis Report

Generated: 2026-09-10T21:00:25.124228+00:00
Logs dir: C:\Users\Alexa\AppData\Local\hermes\logs
Files: 96 | Lines: 450472 | Errors: 15733

## By Category (top 10)

- `other`: 373956
- `hook`: 29163
- `network`: 26088
- `plugin`: 8301
- `mcp`: 3943
- `chat`: 3603
- `provider`: 2864
- `session`: 1623
- `rate_limit`: 520
- `subagent`: 242

## By Level
- `NONE`: 312502
- `DEBUG`: 50313
- `WARNING`: 49714
- `INFO`: 22155
- `ERROR`: 15597
- `CRITICAL`: 136
- `TRACE`: 55

## Per-file
| File | Lines | Errors | Top category |
|---|---|---|---|
| mcp-stderr.log | 224122 | 12366 | other |
| gateway.log | 27814 | 567 | other |
| agent.log.1 | 33699 | 388 | other |
| errors.log | 6600 | 378 | other |
| agent.log | 10413 | 363 | other |
| desktop.log | 4861 | 297 | other |
| gateway-stdio.log | 21933 | 296 | other |
| web_tools_debug_158e6182-ac16-431c-b170-3e2204fd8fd7.json | 2742 | 209 | other |
| web_tools_debug_369c0aa7-c32b-437c-819d-549890d696e0.json | 1925 | 134 | other |
| agent.log.2 | 31957 | 126 | other |
| errors.log.2 | 17600 | 113 | other |
| action-skills-update.log | 3139 | 100 | other |
| errors.log.1 | 17488 | 74 | other |
| rate-limit-bypass.jsonl | 51 | 46 | rate_limit |
| web_tools_debug_0404a025-c034-455c-bee5-5d91324bbc68.json | 844 | 40 | other |
| update.log | 5500 | 32 | other |
| agent.log.3 | 24558 | 30 | other |
| action-skills-install-agent-hooks-21d3eec4.log | 147 | 25 | other |
| web_tools_debug_21807d2a-46c3-485f-b20f-b4b88dd81401.json | 213 | 17 | other |
| web_tools_debug_1f78cd24-dee5-4257-b1ff-977a39a776be.json | 225 | 9 | other |
| web_tools_debug_369bba39-604a-4140-b71b-503b191e1c38.json | 190 | 8 | other |
| action-doctor.log | 483 | 7 | other |
| vision_tools_debug_7b2d14c9-e1e7-40a8-9a23-a7752aeff1dc.json | 93 | 6 | other |
| web_tools_debug_14d1e2bc-9292-4273-884f-41d14a6d3fd7.json | 81 | 6 | other |
| web_tools_debug_728a9190-de1a-42b5-90fe-de0158ea659d.json | 81 | 6 | other |
| web_tools_debug_8398453b-6e47-47be-974c-f366d98b802b.json | 81 | 6 | other |
| web_tools_debug_d54f353a-081b-45c5-944c-f02a990bcbf5.json | 81 | 6 | other |
| web_tools_debug_065d3dd5-dd7d-4893-98fb-7c2ee39d8c12.json | 135 | 5 | other |
| web_tools_debug_a623bf91-feac-4576-b37f-4317d680c935.json | 69 | 5 | other |
| web_tools_debug_421bbdfe-f5ac-4c38-8dfb-57a10901c396.json | 133 | 4 | other |
| web_tools_debug_a1517a7d-aeee-4f0a-86a1-78c84a1b79bf.json | 57 | 4 | other |
| web_tools_debug_d7314bfe-036b-444a-a26a-033b77567657.json | 66 | 4 | other |
| web_tools_debug_e46e7b3a-eeea-4320-a48f-db78ccf4dfc8.json | 57 | 4 | other |
| web_tools_debug_88e6925e-3d6e-4185-a57b-7691948ddc2f.json | 45 | 3 | other |
| web_tools_debug_8a3e7bbd-6e1b-43f6-aeac-ebcf99969eaa.json | 45 | 3 | other |
| web_tools_debug_a4da6304-a074-4fa3-8d12-b0ea1e076a19.json | 45 | 3 | other |
| web_tools_debug_b526f1e4-8887-421f-bf44-87ab8cf82b42.json | 45 | 3 | other |
| web_tools_debug_dee6fbb5-586d-4607-bafe-1b9dcce61fec.json | 45 | 3 | other |
| web_tools_debug_e73330c6-8645-447f-83b8-55d2d57fc0b4.json | 66 | 3 | other |
| action-security-audit.log | 78 | 2 | other |
| tui_gateway_crash.log | 3011 | 2 | other |
| web_tools_debug_0d15d3a5-aef5-48d3-b400-769b61b40027.json | 44 | 2 | other |
| web_tools_debug_14bed752-4e0e-432f-8d57-23a9c25cd29e.json | 65 | 2 | other |
| web_tools_debug_35b66d71-e510-4981-9b1e-d9f864d34a5f.json | 49 | 2 | other |
| web_tools_debug_43300a95-96cb-4737-8872-55b11a45d50f.json | 33 | 2 | other |
| web_tools_debug_5a46d6d1-647b-42df-bfd9-14d8b7eec415.json | 33 | 2 | other |
| web_tools_debug_6f842f5a-4e23-4fc2-9306-410d62fa304c.json | 33 | 2 | other |
| web_tools_debug_7fd8ed1a-4730-4791-89ca-d61211bb4f99.json | 64 | 2 | other |
| web_tools_debug_831a3c9c-69ac-4abe-b0c8-be8c576772f8.json | 48 | 2 | other |
| web_tools_debug_97a800a2-3f98-41c9-be79-a22767f9dff4.json | 57 | 2 | other |
| web_tools_debug_a685efca-914a-4c1d-8dbe-e2f227704f4b.json | 33 | 2 | other |
| action-skills-install-browse-sh-agent-email-get-email-inbox-5e963107.log | 6 | 1 | other |
| action-skills-install-prompt-9c7e05e5.log | 8 | 1 | other |
| action-skills-install-skills-sh-ruvnet-ruflo-hooks-automation-48b1a537.log | 33 | 1 | other |
| vision_tools_debug_fad158d1-ffcb-4d15-911c-09838dcb9e21.json | 23 | 1 | other |
| web_tools_debug_78cc725a-58e5-46b1-b680-b442f4399f98.json | 36 | 1 | other |
| web_tools_debug_94fe9bac-c11e-43ff-8ef9-43aac1c67931.json | 31 | 1 | other |
| web_tools_debug_9f092cd8-5a72-4272-8f9b-bcf4c8b0f3c3.json | 21 | 1 | other |
| web_tools_debug_f032d6fb-379c-495d-8c57-062244f88f56.json | 60 | 1 | other |
| web_tools_debug_f9119bf5-eb29-4935-bf65-e1f4ee034cf2.json | 21 | 1 | other |
| web_tools_debug_fa7fe07a-d96c-490c-93c8-97256f1649b5.json | 21 | 1 | other |
| ? | 0 | 0 | — |
| ? | 0 | 0 | — |
| ? | 0 | 0 | — |
| ? | 0 | 0 | — |
| ? | 0 | 0 | — |
| ? | 0 | 0 | — |
| ? | 0 | 0 | — |
| action-curator-run.log | 16 | 0 | other |
| action-skills-install-agentmemory-hooks-1da657c2.log | 24 | 0 | other |
| action-skills-install-automation-scripts-87f17be5.log | 9 | 0 | other |
| action-skills-install-browse-sh-agentpowers-ai-search-skills-plugins-s-422cdd19.log | 24 | 0 | other |
| action-skills-install-bun-scripts-0188e601.log | 6 | 0 | other |
| action-skills-install-devops-scripts-224aaa27.log | 6 | 0 | other |
| action-skills-install-git-hooks-generator-d3ed007b.log | 6 | 0 | other |
| action-skills-install-git-hooks-manager-1acaec54.log | 6 | 0 | other |
| action-skills-install-git-hooks-toolkit-d1a18d38.log | 6 | 0 | other |
| action-skills-install-init-hooks-33601839.log | 6 | 0 | other |
| action-skills-install-live-qa-scripts-bef61c17.log | 6 | 0 | other |
| action-skills-install-milaex-crypto-api-61c38fe7.log | 7 | 0 | other |
| action-skills-install-official-autonomous-ai-agents-antigravity-cli-c50527af.log | 8 | 0 | other |
| action-skills-install-react-game-loop-a621caf2.log | 6 | 0 | other |
| action-skills-install-realtime-react-hooks-3ca811ed.log | 6 | 0 | other |
| action-skills-install-senpub-124ab220.log | 6 | 0 | other |
| action-skills-install-skills-sh-aj-geddes-useful-ai-prompts-data-migra-5420a3a5.log | 28 | 0 | other |
| action-skills-install-skills-sh-parcadei-continuous-claude-v3-hooks-01054015.log | 22 | 0 | other |
| action-skills-install-skills-sh-patternsdev-skills-hooks-pattern-04b883cf.log | 25 | 0 | other |
| action-skills-install-skills-sh-sickn33-antigravity-awesome-skills-pro-f1b9ea0e.log | 24 | 0 | other |
| action-skills-install-solo-plan-14e77242.log | 6 | 0 | other |
| action-skills-install-trpg-data-context-hooks-24858dd4.log | 6 | 0 | other |
| bootstrap-installer.log | 2657 | 0 | other |
| capture_common.log | 716 | 0 | other |
| gateway-exit-diag.log | 127 | 0 | other |
| gateway-restart.log | 4 | 0 | other |
| gui.log | 146 | 0 | other |
| hooks.log | 5026 | 0 | other |

## Sample errors (top 10 per file with errors)
### action-doctor.log
- `  ⚠ Browser tools (agent-browser) deps (0 critical, 2 high, 0 moderate — run: cd C:\Users\Alexa\AppData\Local\hermes\hermes-agent && npm audit fix --workspaces=false)`
- `  ⚠ web workspace deps (0 critical, 4 high, 0 moderate — build-tool advisory; clears via lockfile bump)`
- `  ⚠ ui-tui workspace deps (0 critical, 2 high, 0 moderate — build-tool advisory; clears via lockfile bump)`
- `  ⚠ web workspace deps (0 critical, 4 high, 0 moderate — build-tool advisory; clears via lockfile bump)`
- `  ⚠ ui-tui workspace deps (0 critical, 3 high, 0 moderate — build-tool advisory; clears via lockfile bump)`
### action-security-audit.log
- `           AIOHTTP: Out-of-bounds heap read in C HTTP response parser error path (malformed chunked response)`
- `           AIOHTTP: Out-of-bounds heap read in C HTTP response parser error path (malformed chunked response)`
### action-skills-install-agent-hooks-21d3eec4.log
- `  CRITICAL exfiltration   SKILL.md:450                   "| `pre_tool_call` `
- `  CRITICAL destructive    SKILL.md:195                   "| `This command is `
- `  CRITICAL destructive    SKILL.md:327                   "echo `
- `  CRITICAL destructive    SKILL.md:450                   "| `pre_tool_call` `
- `  CRITICAL destructive    SKILL.md:218                   ""reason": " Blocked `
### action-skills-install-browse-sh-agent-email-get-email-inbox-5e963107.log
- `Error: Could not fetch 'browse-sh/agent.email/get-email-inbox' from any source.`
### action-skills-install-prompt-9c7e05e5.log
- `Error: Could not fetch 'prompt' from any source.`
### action-skills-install-skills-sh-ruvnet-ruflo-hooks-automation-48b1a537.log
- `  CRITICAL destructive    SKILL.md:106                   "npx claude-flow hook `
### action-skills-update.log
- `  CRITICAL supply_chain   references\cli-docs.md:9       "- macOS/Linux: `curl `
- `  CRITICAL exfiltration   scripts\watch_github.py:118    "token = `
- `  CRITICAL exfiltration   scripts\stocks_client.py:247   "key = `
- `  CRITICAL exfiltration   scripts\stocks_client.py:381   "av_key = `
- `  CRITICAL exfiltration   SKILL.md:173                   "curl -s `
### agent.log
- `2026-09-10 21:26:40,262 ERROR agent.chat_completion_helpers: Streaming failed before delivery: Error code: 503 - {'error': {'type': 'server_error', 'message': 'Error from provider (Console): Upstream `
- `openai.InternalServerError: Error code: 503 - {'error': {'type': 'server_error', 'message': 'Error from provider (Console): Upstream request failed: Endpoint is unavailable.'}}`
- `2026-09-10 21:26:44,555 ERROR agent.chat_completion_helpers: Streaming failed before delivery: Error code: 503 - {'error': {'type': 'server_error', 'message': 'Error from provider (Console): Upstream `
- `openai.InternalServerError: Error code: 503 - {'error': {'type': 'server_error', 'message': 'Error from provider (Console): Upstream request failed: Endpoint is unavailable.'}}`
- `[ERROR] Traceback (most recent call last):`
### agent.log.1
- `httpx2.HTTPStatusError: Client error '405 Method Not Allowed' for url 'https://search.parallel.ai/mcp'`
- `2026-09-10 20:17:31,299 ERROR agent.chat_completion_helpers: Streaming failed before delivery: Error code: 429 - {'type': 'error', 'error': {'type': 'FreeUsageLimitError', 'message': 'Error from provi`
- `openai.RateLimitError: Error code: 429 - {'type': 'error', 'error': {'type': 'FreeUsageLimitError', 'message': 'Error from provider (Console): Rate limit exceeded. Please try again later.'}}`
- `2026-09-10 20:17:32,870 ERROR agent.chat_completion_helpers: Streaming failed before delivery: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'pool`
- `openai.RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'poolside/laguna-s-2.1:free is temporarily rate-limited upstream. Please retr`
### agent.log.2
- `pywintypes.error: (5, 'AssignProcessToJobObject', 'Access is denied.')`
- `pywintypes.error: (5, 'AssignProcessToJobObject', 'Access is denied.')`
- `httpx2.HTTPStatusError: Client error '405 Method Not Allowed' for url 'https://search.parallel.ai/mcp'`
- `httpx2.HTTPStatusError: Client error '405 Method Not Allowed' for url 'https://search.parallel.ai/mcp'`
- `2026-09-10 19:48:34,017 ERROR [20260910_194621_d64612] agent.chat_completion_helpers: Streaming failed before delivery: Error code: 429 - {'status': 429, 'message': "The requested model is temporarily`
### agent.log.3
- `2026-09-10 18:34:54,321 ERROR [20260910_175132_d8685f] agent.conversation_loop: Error during OpenAI-compatible API call #1: BLOCKED_MISSING_PREREQUISITE: required pre-compress checkpoint unavailable: `
- `2026-09-10 18:34:54,323 ERROR [20260910_175132_d8685f] agent.conversation_loop: Outer loop error in API call #1`
- `httpx2.HTTPStatusError: Client error '405 Method Not Allowed' for url 'https://search.parallel.ai/mcp'`
- `httpx2.HTTPStatusError: Client error '405 Method Not Allowed' for url 'https://search.parallel.ai/mcp'`
- `httpx2.HTTPStatusError: Client error '405 Method Not Allowed' for url 'https://search.parallel.ai/mcp'`
### desktop.log
- `[hermes] [boot] could not read served dashboard token (Hermes backend): 404: {"error":"Headless backend (hermes serve): web UI disabled — use `hermes dashboard` for the browser UI."}`
- `[hermes] [boot] could not read served dashboard token (Hermes backend for profile "cto"): 404: {"error":"Headless backend (hermes serve): web UI disabled — use `hermes dashboard` for the browser UI."}`
- `[hermes] [boot] could not read served dashboard token (Hermes backend for profile "creative-director"): 404: {"error":"Headless backend (hermes serve): web UI disabled — use `hermes dashboard` for the`
- `[hermes] [boot] could not read served dashboard token (Hermes backend for profile "pm"): 404: {"error":"Headless backend (hermes serve): web UI disabled — use `hermes dashboard` for the browser UI."}`
- `[hermes]    📝 Error: Connection error.`
### errors.log
- `2026-09-10 20:49:40,870 ERROR agent.chat_completion_helpers: Streaming failed before delivery: Error code: 503 - {'error': {'type': 'server_error', 'message': 'Error from provider (Console): Upstream `
- `openai.InternalServerError: Error code: 503 - {'error': {'type': 'server_error', 'message': 'Error from provider (Console): Upstream request failed: Endpoint is unavailable.'}}`
- `2026-09-10 20:51:30,890 ERROR agent.chat_completion_helpers: Streaming failed before delivery: Error code: 503 - {'error': {'type': 'server_error', 'message': 'Error from provider (Console): Upstream `
- `openai.InternalServerError: Error code: 503 - {'error': {'type': 'server_error', 'message': 'Error from provider (Console): Upstream request failed: Endpoint is unavailable.'}}`
- `2026-09-10 20:51:34,879 ERROR agent.chat_completion_helpers: Streaming failed before delivery: Error code: 503 - {'error': {'type': 'server_error', 'message': 'Error from provider (Console): Upstream `
### errors.log.1
- `2026-09-10 19:27:08,371 ERROR gateway.run: ✗ telegram error: telegram connect timed out after 45s`
- `2026-09-10 19:37:37,329 ERROR agent.chat_completion_helpers: Streaming failed before delivery: Error code: 429 - {'type': 'error', 'error': {'type': 'FreeUsageLimitError', 'message': 'Error from provi`
- `openai.RateLimitError: Error code: 429 - {'type': 'error', 'error': {'type': 'FreeUsageLimitError', 'message': 'Error from provider (Console): Rate limit exceeded. Please try again later.'}}`
- `2026-09-10 19:37:40,417 ERROR agent.chat_completion_helpers: Streaming failed before delivery: Error code: 429 - {'type': 'error', 'error': {'type': 'FreeUsageLimitError', 'message': 'Error from provi`
- `openai.RateLimitError: Error code: 429 - {'type': 'error', 'error': {'type': 'FreeUsageLimitError', 'message': 'Error from provider (Console): Rate limit exceeded. Please try again later.'}}`
### errors.log.2
- `2026-09-10 16:36:30,420 ERROR agent.chat_completion_helpers: Streaming failed before delivery: Error code: 429 - {'status': 429, 'message': "The requested model is temporarily at capacity upstream. Th`
- `openai.RateLimitError: Error code: 429 - {'status': 429, 'message': "The requested model is temporarily at capacity upstream. This is not your API key's rate limit — please retry shortly."}`
- `2026-09-10 16:41:38,689 ERROR agent.chat_completion_helpers: Streaming failed before delivery: Error code: 429 - {'status': 429, 'message': "The requested model is temporarily at capacity upstream. Th`
- `openai.RateLimitError: Error code: 429 - {'status': 429, 'message': "The requested model is temporarily at capacity upstream. This is not your API key's rate limit — please retry shortly."}`
- `2026-09-10 16:43:45,247 ERROR agent.chat_completion_helpers: Streaming failed before delivery: Error code: 401 - {'type': 'error', 'error': {'type': 'ModelError', 'message': 'Model minimax-m3-free is `
### gateway-stdio.log
- `ERROR asyncio: Task exception was never retrieved`
- `ERROR telegram.ext.Updater: Error while calling `get_updates` one more time to mark all fetched updates. Suppressing error to ensure graceful shutdown. When polling for updates is restarted, updates m`
- `telegram.error.NetworkError: httpx.ConnectError: All connection attempts failed`
- `ERROR telegram.ext: Network Retry Loop (Bootstrap delete Webhook): Failed run number 0 of 0. Aborting.`
- `telegram.error.NetworkError: httpx.ConnectError: All connection attempts failed`
### gateway.log
- `telegram.error.TimedOut: Timed out`
- `telegram.error.NetworkError: httpx.ConnectError: All connection attempts failed`
- `2026-08-09 07:11:25,386 ERROR hermes_plugins.telegram_platform.adapter: [Telegram] Failed to connect to Telegram: httpx.ConnectError: All connection attempts failed`
- `2026-08-09 07:12:57,901 ERROR hermes_plugins.telegram_platform.adapter: [Telegram] Failed to connect to Telegram: httpx.ConnectError: All connection attempts failed`
- `2026-08-09 07:14:59,666 ERROR hermes_plugins.telegram_platform.adapter: [Telegram] Failed to connect to Telegram: httpx.ConnectError: All connection attempts failed`
### mcp-stderr.log
- `verifying docker images: Get "https://auth.docker.io/token?scope=repository%3Amcp%2Fsignatures%3Apull&service=registry.docker.io": remote error: tls: bad record MAC`
- `      throw er; // Unhandled 'error' event`
- `Error: EPIPE: broken pipe, write`
- `Emitted 'error' event on Socket instance at:`
- `      throw er; // Unhandled 'error' event`
### rate-limit-bypass.jsonl
- `{"ts": "2026-09-05T03:36:11+0100", "event": "retry", "model": "primary", "attempt": 1, "sleep_s": 0.5, "error": "429 rate limit exceeded"}`
- `{"ts": "2026-09-05T03:36:12+0100", "event": "retry", "model": "primary", "attempt": 2, "sleep_s": 0.5, "error": "429 rate limit exceeded"}`
- `{"ts": "2026-09-05T03:36:12+0100", "event": "retry", "model": "primary", "attempt": 1, "sleep_s": 0.5, "error": "429 too many requests"}`
- `{"ts": "2026-09-05T03:36:13+0100", "event": "retry", "model": "primary", "attempt": 2, "sleep_s": 0.5, "error": "429 too many requests"}`
- `{"ts": "2026-09-05T03:36:13+0100", "event": "retry", "model": "primary", "attempt": 3, "sleep_s": 0.5, "error": "429 too many requests"}`
### tui_gateway_crash.log
- `[tui-parent] 2026-08-24T23:14:34.511Z uncaughtException: Error: write EPIPE`
- `[tui-parent] 2026-08-31T15:40:11.431Z uncaughtException: Error: write EPIPE`
### update.log
- `dist/assets/error-state-D-dzDtJy.js                        1.35 kB │ gzip:     0.64 kB`
- `dist/assets/error-boundary-CJVQAT8r.js                     2.68 kB │ gzip:     1.08 kB`
- `dist/assets/error-state-DbQn86jw.js                        1.35 kB │ gzip:     0.64 kB`
- `dist/assets/error-boundary-BcLStJ3n.js                     2.88 kB │ gzip:     1.17 kB`
- `dist/assets/error-state-DI7tkfOo.js                        1.35 kB │ gzip:     0.64 kB`
### vision_tools_debug_7b2d14c9-e1e7-40a8-9a23-a7752aeff1dc.json
- `      "error": "Error analyzing image: Error code: 400 - {'error': {'message': 'Error from provider (DeepSeek): Failed to deserialize the JSON body into the target type: messages[0]: unknown variant ``
- `      "error": "Error analyzing image: Error code: 400 - {'error': {'message': 'Error from provider (DeepSeek): Failed to deserialize the JSON body into the target type: messages[0]: unknown variant ``
- `      "error": "Error analyzing image: Error code: 400 - {'error': {'message': 'Error from provider (DeepSeek): Failed to deserialize the JSON body into the target type: messages[0]: unknown variant ``
- `      "error": "Error analyzing image: Error code: 400 - {'error': {'message': 'Error from provider (DeepSeek): Failed to deserialize the JSON body into the target type: messages[0]: unknown variant ``
- `      "error": "Error analyzing image: Error code: 400 - {'error': {'message': 'Error from provider (DeepSeek): Failed to deserialize the JSON body into the target type: messages[0]: unknown variant ``
### vision_tools_debug_fad158d1-ffcb-4d15-911c-09838dcb9e21.json
- `      "error": "Error analyzing image: Error code: 400 - {'error': {'message': 'Error from provider (DeepSeek): Failed to deserialize the JSON body into the target type: messages[0]: unknown variant ``
### web_tools_debug_0404a025-c034-455c-bee5-5d91324bbc68.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_065d3dd5-dd7d-4893-98fb-7c2ee39d8c12.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_0d15d3a5-aef5-48d3-b400-769b61b40027.json
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_14bed752-4e0e-432f-8d57-23a9c25cd29e.json
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_14d1e2bc-9292-4273-884f-41d14a6d3fd7.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_158e6182-ac16-431c-b170-3e2204fd8fd7.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_1f78cd24-dee5-4257-b1ff-977a39a776be.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_21807d2a-46c3-485f-b20f-b4b88dd81401.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_35b66d71-e510-4981-9b1e-d9f864d34a5f.json
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_369bba39-604a-4140-b71b-503b191e1c38.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_369c0aa7-c32b-437c-819d-549890d696e0.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_421bbdfe-f5ac-4c38-8dfb-57a10901c396.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_43300a95-96cb-4737-8872-55b11a45d50f.json
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_5a46d6d1-647b-42df-bfd9-14d8b7eec415.json
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_6f842f5a-4e23-4fc2-9306-410d62fa304c.json
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_728a9190-de1a-42b5-90fe-de0158ea659d.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_78cc725a-58e5-46b1-b680-b442f4399f98.json
- `      "error": null,`
### web_tools_debug_7fd8ed1a-4730-4791-89ca-d61211bb4f99.json
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_831a3c9c-69ac-4abe-b0c8-be8c576772f8.json
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_8398453b-6e47-47be-974c-f366d98b802b.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_88e6925e-3d6e-4185-a57b-7691948ddc2f.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_8a3e7bbd-6e1b-43f6-aeac-ebcf99969eaa.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_94fe9bac-c11e-43ff-8ef9-43aac1c67931.json
- `      "error": null,`
### web_tools_debug_97a800a2-3f98-41c9-be79-a22767f9dff4.json
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_9f092cd8-5a72-4272-8f9b-bcf4c8b0f3c3.json
- `      "error": null,`
### web_tools_debug_a1517a7d-aeee-4f0a-86a1-78c84a1b79bf.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_a4da6304-a074-4fa3-8d12-b0ea1e076a19.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_a623bf91-feac-4576-b37f-4317d680c935.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_a685efca-914a-4c1d-8dbe-e2f227704f4b.json
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_b526f1e4-8887-421f-bf44-87ab8cf82b42.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_d54f353a-081b-45c5-944c-f02a990bcbf5.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_d7314bfe-036b-444a-a26a-033b77567657.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_dee6fbb5-586d-4607-bafe-1b9dcce61fec.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_e46e7b3a-eeea-4320-a48f-db78ccf4dfc8.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_e73330c6-8645-447f-83b8-55d2d57fc0b4.json
- `      "error": null,`
- `      "error": null,`
- `      "error": null,`
### web_tools_debug_f032d6fb-379c-495d-8c57-062244f88f56.json
- `      "error": null,`
### web_tools_debug_f9119bf5-eb29-4935-bf65-e1f4ee034cf2.json
- `      "error": null,`
### web_tools_debug_fa7fe07a-d96c-490c-93c8-97256f1649b5.json
- `      "error": "web is configured to use 'tavily' (set via hermes tools), but no registered web search provider has that name. Run 'hermes tools' to change it.",`