# Probe results — test-providers-models

## auth_list
exit=0
```
copilot (3 credentials):
  #1  GITHUB_TOKEN         api_key env:GITHUB_TOKEN
  #2  COPILOT_GITHUB_TOKEN api_key env:COPILOT_GITHUB_TOKEN ←
  #3  api-key-3            api_key manual

deepseek (1 credentials):
  #1  DEEPSEEK_API_KEY     api_key env:DEEPSEEK_API_KEY ←

gemini (1 credentials):
  #1  GOOGLE_API_KEY       api_key env:GOOGLE_API_KEY ←

huggingface (1 credentials):
  #1  HF_TOKEN             api_key env:HF_TOKEN ←

minimax-oauth (1 credentials):
  #1  oauth                oauth   oauth ←

nous (1 credentials):
  #1  device_code          oauth   device_code ←

ollama-cloud (1 credentials):
  #1  OLLAMA_API_KEY       api_key env:OLLAMA_API_KEY ←

openai-api (5 credentials):
  #1  OPENAI_API_KEY       api_key env:OPENAI_API_KEY exhausted (402) (ready to retry)
  #2  api-key-1            api_key manual exhausted (402) (ready to retry) ←
  #3  api-key-3            api_key manual exhausted (402) (ready to retry)
  #4  api-key-4            api_key manual
  #5  api-key-2            api_key manual

openai-codex (3 credentials):
  #1  device_code          oauth   device_code ←
  #2  openai-codex-oauth-2 oauth   device_code rate-limited usage_limit_reached (429) (29d 12h left)
  #3  alexanderrhixe30@gmail.com oauth   device_code

opencode-zen (2 credentials):
  #1  OPENCODE_ZEN_API_KEY api_key env:OPENCODE_ZEN_API_KEY ←
  #2  zen-backup           api_key manual

openrouter (1 credentials):
  #1  OPENROUTER_API_KEY   api_key env:OPENROUTER_API_KEY ←

xai (2 credentials):
  #1  api-key-1            api_key manual auth failed (403) (re-auth may be required) ←
  #2  XAI_API_KEY          api_key env:XAI_API_KEY

xai-oauth (1 credentials):
  #1  xai-oauth-oauth-1    oauth   device_code ←


```
## config_show
exit=0
```

┌─────────────────────────────────────────────────────────┐
│              ⚕ Hermes Configuration                    │
└─────────────────────────────────────────────────────────┘

◆ Paths
  Config:       C:\Users\Alexa\AppData\Local\hermes\profiles\ops\config.yaml
  Secrets:      C:\Users\Alexa\AppData\Local\hermes\profiles\ops\.env
  Install:      C:\Users\Alexa\AppData\Local\hermes\hermes-agent

◆ API Keys
  OpenRouter     sk-o...0554
  OpenAI (STT/TTS) (not set)
  Exa            (not set)
  Parallel       (not set)
  Firecrawl      (not set)
  Tavily         tvly...V8Eu
  Perplexity     (not set)
  Browserbase    (not set)
  Browser Use    (not set)
  FAL            (not set)
  Anthropic      (not set)

◆ Model
  Model:        {'base_url': 'https://opencode.ai/zen/v1', 'default': 'nemotron-3-ultra-free', 'provider': 'opencode-zen', 'api_mode': 'chat_completions'}
  Max turns:    150

◆ Display
  Personality:  concise
  Reasoning:    on
  Bell:         complete=on, prompt=off
  User preview: first 2 line(s), last 2 line(s)

◆ Terminal
  Backend:      local
  Working dir:  
  Timeout:      360s

◆ Timezone
  Timezone:     (server-local)

◆ Context Compression
  Enabled:      yes
  Threshold:    90%
  Target ratio: 20% of threshold preserved
  Protect last: 40 messages
  Protect first: 6 non-system head messages
  Model:        (auto)

◆ Auxiliary Models (overrides)
  Vision        provider=openrouter, model=nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free

◆ Messaging Platforms
  Telegram:     configured
  Discord:      not configured

────────────────────────────────────────────────────────────
  hermes config edit     # Edit config file
  hermes config set <key> <value>
  hermes setup           # Run setup wizard


```
## status
exit=0
```

┌─────────────────────────────────────────────────────────┐
│                 ⚕ Hermes Agent Status                  │
└─────────────────────────────────────────────────────────┘

◆ Environment
  Project:      C:\Users\Alexa\AppData\Local\hermes\hermes-agent
  Python:       3.13.14
  .env file:    ✓ exists
  Model:        nemotron-3-ultra-free
  Provider:     OpenCode Zen

◆ API Keys
  OpenRouter    ✓ sk-o...0554
  OpenAI        ✗ (not set)
  Google / Gemini  ✓ AIza...9EfU
  DeepSeek      ✓ sk-a...9f84
  xAI / Grok    ✓ xai-...l0iu
  NVIDIA NIM    ✗ (not set)
  Z.AI / GLM    ✗ (not set)
  Kimi          ✗ (not set)
  StepFun Step Plan  ✗ (not set)
  MiniMax       ✗ (not set)
  MiniMax-CN    ✗ (not set)
  DeepInfra     ✗ (not set)
  Firecrawl     ✗ (not set)
  Tavily        ✓ tvly...V8Eu
  Perplexity    ✗ (not set)
  Keenable      ✗ (not set)
  Browser Use   ✗ (not set)
  Browserbase   ✗ (not set)
  FAL           ✗ (not set)
  ElevenLabs    ✗ (not set)
  GitHub        ✓ gho_...5pZk
  Anthropic     ✗ (not set)

◆ Auth Providers
  Nous Portal   ✓ logged in
    Portal URL: https://portal.nousresearch.com
    Inference:  https://inference-api.nousresearch.com/v1
    Access exp: 2026-09-05 12:58:27 W. Central Africa Standard Time
    Key exp:    2026-09-05 12:58:27 W. Central Africa Standard Time
    Refresh:    yes
  OpenAI Codex  ✓ logged in
    Auth file:  C:\Users\Alexa\AppData\Local\hermes\profiles\ops\auth.json
    Refreshed:  2026-09-05 09:10:57 W. Central Africa Standard Time
  Qwen OAuth    ✗ not logged in (run: qwen auth qwen-oauth)
    Auth file:  C:\Users\Alexa\.qwen\oauth_creds.json
    Error:      Qwen CLI credentials not found. Run 'qwen auth qwen-oauth' first.
  MiniMax OAuth  ✓ logged in
    Region:     global
    Access exp: 2027-08-31T16:20:05.475000+00:00
  xAI OAuth     ✓ logged in
    Auth file:  C:\Users\Alexa\AppData\Local\hermes\profiles\ops\auth.json
    Refreshed:  2026-09-05 10:33:23 W. Central Africa Standard Time

◆ Nous Tool Gateway
  Your Nous Portal account has no usable paid credits, so managed web, image, TTS, STT, browser, and Modal tools is unavailable. Add credits or update billing at https://portal.nousresearch.com/billing. If you recently bought credits, run `hermes model` to refresh Hermes.

◆ API-Key Providers
  Z.AI / GLM       ✗ not configured (run: hermes model)
  Kimi / Moonshot  ✗ not configured (run: hermes model)
  StepFun Step Plan ✗ not configured (run: hermes model)
  MiniMax          ✗ not configured (run: hermes model)
  MiniMax (China)  ✗ not configured (run: hermes model)
  DeepInfra        ✗ not configured (run: hermes model)

◆ Terminal Backend
  Backend:      local
  Sudo:         ✓ enabled

◆ Messaging Platforms
  Telegram      ✓ configured (home: 7043401427)
  Discord       ✗ not configured
  WhatsApp      ✗ not configured
  Signal        ✗ not configured
  Slack         ✗ not configured
  Email         ✗ not configured
  SMS           ✗ not configured
  DingTalk      ✗ not configured
  Feishu        ✗ not configured
  WeCom         ✗ not configured
  WeCom Callback  ✗ not configured
  Weixin        ✗ not configured
  BlueBubbles   ✗ not configured
  QQBot         ✗ not configured
  Yuanbao       ✗ not configured
  A2A           ✓ configured (plugin)
  Buzz          ✗ not configured (plugin)
  DingTalk      ✗ not configured (plugin)
  Email         ✗ not configured (plugin)
  Feishu / Lark  ✗ not configured (plugin)
  Matrix        ✗ not configured (plugin)
  ntfy          ✗ not configured (plugin)
  Raft          ✗ not configured (plugin)
  Slack         ✓ configured (plugin)
  SMS (Twilio)  ✗ not configured (plugin)
  Telegram      ✓ configured (plugin)
  WeCom (Enterprise WeChat)  ✓ configured (plugin)
  WeCom Callback (self-built apps)  ✓ configured (plugin)
  WhatsApp      ✓ configured (plugin)

◆ Gateway Service
  Status:       ✗ stopped
  Manager:      manual process

◆ Scheduled Jobs
  Jobs:         0

◆ Sessions
  Active:       0
  Slots:        1/10 in use
                desktop           20260905_115455_ac280c   14m

────────────────────────────────────────────────────────────
  Run 'hermes doctor' for detailed diagnostics
  Run 'hermes setup' to configure


```
## doctor
exit=0
```

┌─────────────────────────────────────────────────────────┐
│                 🩺 Hermes Doctor                        │
└─────────────────────────────────────────────────────────┘

◆ Security Advisories
  ✓ No active security advisories

◆ MCP Server Security
  ✓ No suspicious MCP stdio commands

◆ Python Environment
  ✓ Python 3.13.14
  ✓ SQLite 3.53.1
    → SQLite source id: 2026-05-05 10:34:17 c88b22011a54b4f6fbd149e9f8e4…
    → state.db: WAL journal mode (1.3 MB)
    → cron/executions.db: WAL journal mode (20.0 KB)
    → projects.db: WAL journal mode (44.0 KB)
    → verification_evidence.db: WAL journal mode (32.0 KB)
  ✓ Virtual environment active
  ✓ Version files consistent (0.21.0)

◆ SSL / CA Certificates
  ✓ SSL CA certificate bundle is valid

◆ Required Packages
  ✓ OpenAI SDK
  ✓ Rich (terminal UI)
  ✓ python-dotenv
  ✓ PyYAML
  ✓ HTTPX
  ✓ Croniter (cron expressions) (optional)
  ✓ python-telegram-bot (optional)
  ✓ discord.py (optional)

◆ Configuration Files
  ✓ ~/AppData/Local/hermes/profiles/ops/.env file exists
  ✓ API key or custom endpoint configured
  ✓ ~/AppData/Local/hermes/profiles/ops/config.yaml exists
  ✓ Config version up to date (v40)
  ✓ No deprecated config keys or env vars

◆ xAI Model Retirement (May 15, 2026)
  ✓ No retired xAI models in config

◆ Plugin import paths (removed Sep 14, 2026)
  ✓ No enabled plugin imports paths removed on 2026-09-14

◆ Auth Providers
  ✓ Nous Portal auth (logged in)
  ✓ OpenAI Codex auth (logged in)
  ✓ MiniMax OAuth (logged in, region=global)
  ✓ xAI OAuth (logged in)

◆ Directory Structure
  ✓ ~/AppData/Local/hermes/profiles/ops directory exists
  ✓ ~/AppData/Local/hermes/profiles/ops/cron/ exists
  ✓ ~/AppData/Local/hermes/profiles/ops/sessions/ exists
  ✓ ~/AppData/Local/hermes/profiles/ops/logs/ exists
  ✓ ~/AppData/Local/hermes/profiles/ops/skills/ exists
  ✓ ~/AppData/Local/hermes/profiles/ops/memories/ exists
  ✓ ~/AppData/Local/hermes/profiles/ops/SOUL.md exists (persona configured)
  ✓ ~/AppData/Local/hermes/profiles/ops/memories/ directory exists
  ✓ MEMORY.md exists (4161 chars)
  ✓ USER.md exists (1237 chars)
  ✓ ~/AppData/Local/hermes/profiles/ops/state.db exists (1 sessions)
    → state.db logical size 1.3 MB, 328 pages, 71 free, WAL 2.7 MB
    → 148 messages, 1 sessions, journal_mode=wal
    → FTS tables: messages_fts, messages_fts_trigram

◆ External Tools
  ✓ git
  ✓ ripgrep (rg) (faster file search)
  ✓ docker (optional)
  ✓ Node.js
  ✓ agent-browser (browser automation)
  ✓ Playwright Chromium (browser engine)
  ⚠ Browser tools (agent-browser) deps (0 critical, 1 high, 0 moderate — run: cd C:\Users\Alexa\AppData\Local\hermes\hermes-agent && npm audit fix --workspaces=false)
  ⚠ web workspace deps (0 critical, 1 high, 1 moderate — build-tool advisory; clears via lockfile bump)
    →   ^ build-time tooling (not runtime); if manual npm remediation errors with an arborist crash it's a known npm bug — clears via a lockfile bump
  ✓ ui-tui workspace deps (no known vulnerabilities)

◆ API Connectivity
  Running 40 connectivity checks in parallel…
                                                                      
  ✓ OpenRouter API
  ✓ DeepSeek            
  ✓ Hugging Face        
  ✓ OpenCode Zen        
  ✓ gemini              
  ✓ ollama-cloud        
  ⚠ xai                  (HTTP 403)

◆ Tool Availability
  ✓ browser-use
  ✓ clarify
  ✓ code_execution
  ✓ computer_use
  ✓ cronjob
  ✓ delegation
  ✓ desktop_ui
  ✓ file
  ✓ memory
  ✓ project
  ✓ session_search
  ✓ skills
  ✓ terminal
  ✓ todo
  ✓ tts
  ✓ video
  ✓ video_gen
  ✓ vision
  ✓ x_search
  ✓ kanban (runtime-gated; loaded only for dispatcher-spawned workers)
  ✓ web search (tavily)
  ✓ web extract (tavily)
  ⚠ a2a (system dependency not met)
  ⚠ browser (system dependency not met)
  ⚠ browser-cdp (system dependency not met)
  ⚠ discord (missing DISCORD_BOT_TOKEN)
  ⚠ discord_admin (missing DISCORD_BOT_TOKEN)
  ⚠ feishu_doc (system dependency not met)
  ⚠ feishu_drive (system dependency not met)
  ⚠ hermes-yuanbao (system dependency not met)
  ⚠ homeassistant (system dependency not met)
  ⚠ image_gen (system dependency not met)

◆ Skills Hub
  ✓ Skills Hub directory exists
  ✓ Lock file OK (13 hub-installed skill(s))
  ✓ GitHub token configured (authenticated API access)

◆ Memory Provider
  ✓ Built-in memory active (no external provider configured — this is fine)

◆ Profiles
  ✓ 13 profile(s) found
  ✓   alexa: nemotron-3-ultra-free, no alias
  ✓   code-architect: nemotron-3-ultra-free, no alias
  ✓   creative-director: nemotron-3-ultra-free, no alias
  ✓   cto: nemotron-3-ultra-free, no alias
  ✓   designer: nemotron-3-ultra-free, no alias
  ✓   dev: nemotron-3-ultra-free, no alias
  ✓   exec-assistant: nemotron-3-ultra-free, no alias
  ✓   ops: nemotron-3-ultra-free, no alias
  ✓   patient-tutor: nemotron-3-ultra-free, no alias
  ✓   pm: nemotron-3-ultra-free, no alias
  ✓   qa: nemotron-3-ultra-free, no alias
  ✓   research-analyst: nemotron-3-ultra-free, no alias
  ✓   security: nemotron-3-ultra-free, no alias

────────────────────────────────────────────────────────────
  Found 2 issue(s) to address:

  1. Browser tools (agent-browser) has 1 npm vulnerability
  2. web workspace has 2 npm vulnerabilities

  Tip: run 'hermes doctor --fix' to auto-fix what's possible.


```
## doctor_fix
exit=0
```

┌─────────────────────────────────────────────────────────┐
│                 🩺 Hermes Doctor                        │
└─────────────────────────────────────────────────────────┘

◆ Security Advisories
  ✓ No active security advisories

◆ MCP Server Security
  ✓ No suspicious MCP stdio commands

◆ Python Environment
  ✓ Python 3.13.14
  ✓ SQLite 3.53.1
    → SQLite source id: 2026-05-05 10:34:17 c88b22011a54b4f6fbd149e9f8e4…
    → state.db: WAL journal mode (1.3 MB)
    → cron/executions.db: WAL journal mode (20.0 KB)
    → projects.db: WAL journal mode (44.0 KB)
    → verification_evidence.db: WAL journal mode (32.0 KB)
  ✓ Virtual environment active
  ✓ Version files consistent (0.21.0)

◆ SSL / CA Certificates
  ✓ SSL CA certificate bundle is valid

◆ Required Packages
  ✓ OpenAI SDK
  ✓ Rich (terminal UI)
  ✓ python-dotenv
  ✓ PyYAML
  ✓ HTTPX
  ✓ Croniter (cron expressions) (optional)
  ✓ python-telegram-bot (optional)
  ✓ discord.py (optional)

◆ Configuration Files
  ✓ ~/AppData/Local/hermes/profiles/ops/.env file exists
  ✓ API key or custom endpoint configured
  ✓ ~/AppData/Local/hermes/profiles/ops/config.yaml exists
  ✓ Config version up to date (v40)
  ✓ No deprecated config keys or env vars

◆ xAI Model Retirement (May 15, 2026)
  ✓ No retired xAI models in config

◆ Plugin import paths (removed Sep 14, 2026)
  ✓ No enabled plugin imports paths removed on 2026-09-14

◆ Auth Providers
  ✓ Nous Portal auth (logged in)
  ✓ OpenAI Codex auth (logged in)
  ✓ MiniMax OAuth (logged in, region=global)
  ✓ xAI OAuth (logged in)

◆ Directory Structure
  ✓ ~/AppData/Local/hermes/profiles/ops directory exists
  ✓ ~/AppData/Local/hermes/profiles/ops/cron/ exists
  ✓ ~/AppData/Local/hermes/profiles/ops/sessions/ exists
  ✓ ~/AppData/Local/hermes/profiles/ops/logs/ exists
  ✓ ~/AppData/Local/hermes/profiles/ops/skills/ exists
  ✓ ~/AppData/Local/hermes/profiles/ops/memories/ exists
  ✓ ~/AppData/Local/hermes/profiles/ops/SOUL.md exists (persona configured)
  ✓ ~/AppData/Local/hermes/profiles/ops/memories/ directory exists
  ✓ MEMORY.md exists (4161 chars)
  ✓ USER.md exists (1237 chars)
  ✓ ~/AppData/Local/hermes/profiles/ops/state.db exists (1 sessions)
    → state.db logical size 1.3 MB, 328 pages, 71 free, WAL 2.7 MB
    → 148 messages, 1 sessions, journal_mode=wal
    → FTS tables: messages_fts, messages_fts_trigram

◆ External Tools
  ✓ git
  ✓ ripgrep (rg) (faster file search)
  ✓ docker (optional)
  ✓ Node.js
  ✓ agent-browser (browser automation)
  ✓ Playwright Chromium (browser engine)
  ⚠ Browser tools (agent-browser) deps (0 critical, 1 high, 0 moderate — run: cd C:\Users\Alexa\AppData\Local\hermes\hermes-agent && npm audit fix --workspaces=false)
  ⚠ web workspace deps (0 critical, 1 high, 1 moderate — build-tool advisory; clears via lockfile bump)
    →   ^ build-time tooling (not runtime); if manual npm remediation errors with an arborist crash it's a known npm bug — clears via a lockfile bump
  ✓ ui-tui workspace deps (no known vulnerabilities)

◆ API Connectivity
  Running 40 connectivity checks in parallel…
                                                                      
  ✓ OpenRouter API
  ✓ DeepSeek            
  ✓ Hugging Face        
  ✓ OpenCode Zen        
  ✓ gemini              
  ✓ ollama-cloud        
  ⚠ xai                  (HTTP 403)

◆ Tool Availability
  ✓ browser-use
  ✓ clarify
  ✓ code_execution
  ✓ computer_use
  ✓ cronjob
  ✓ delegation
  ✓ desktop_ui
  ✓ file
  ✓ memory
  ✓ project
  ✓ session_search
  ✓ skills
  ✓ terminal
  ✓ todo
  ✓ tts
  ✓ video
  ✓ video_gen
  ✓ vision
  ✓ x_search
  ✓ kanban (runtime-gated; loaded only for dispatcher-spawned workers)
  ✓ web search (tavily)
  ✓ web extract (tavily)
  ⚠ a2a (system dependency not met)
  ⚠ browser (system dependency not met)
  ⚠ browser-cdp (system dependency not met)
  ⚠ discord (missing DISCORD_BOT_TOKEN)
  ⚠ discord_admin (missing DISCORD_BOT_TOKEN)
  ⚠ feishu_doc (system dependency not met)
  ⚠ feishu_drive (system dependency not met)
  ⚠ hermes-yuanbao (system dependency not met)
  ⚠ homeassistant (system dependency not met)
  ⚠ image_gen (system dependency not met)

◆ Skills Hub
  ✓ Skills Hub directory exists
  ✓ Lock file OK (13 hub-installed skill(s))
  ✓ GitHub token configured (authenticated API access)

◆ Memory Provider
  ✓ Built-in memory active (no external provider configured — this is fine)

◆ Profiles
  ✓ 13 profile(s) found
  ✓   alexa: nemotron-3-ultra-free, no alias
  ✓   code-architect: nemotron-3-ultra-free, no alias
  ✓   creative-director: nemotron-3-ultra-free, no alias
  ✓   cto: nemotron-3-ultra-free, no alias
  ✓   designer: nemotron-3-ultra-free, no alias
  ✓   dev: nemotron-3-ultra-free, no alias
  ✓   exec-assistant: nemotron-3-ultra-free, no alias
  ✓   ops: nemotron-3-ultra-free, no alias
  ✓   patient-tutor: nemotron-3-ultra-free, no alias
  ✓   pm: nemotron-3-ultra-free, no alias
  ✓   qa: nemotron-3-ultra-free, no alias
  ✓   research-analyst: nemotron-3-ultra-free, no alias
  ✓   security: nemotron-3-ultra-free, no alias

────────────────────────────────────────────────────────────
  Found 2 issue(s) to address:

  1. Browser tools (agent-browser) has 1 npm vulnerability
  2. web workspace has 2 npm vulnerabilities



```
## insights
exit=0
```

  ╔══════════════════════════════════════════════════════════╗
  ║                    📊 Hermes Insights                    ║
  ║                       Last 30 days                       ║
  ╚══════════════════════════════════════════════════════════╝

  Period: Sep 05, 2026 — Sep 05, 2026

  📋 Overview
  ────────────────────────────────────────────────────────
  Sessions:          1             Messages:        148
  Tool calls:        71            User messages:   4
  Input tokens:      199,414       Output tokens:   20,424
  Total tokens:      5,968,958
  Avg msgs/session:  148.0

  💰 Cost
  ────────────────────────────────────────────────────────
  Unknown:            1 session(s) (no pricing data)

  🤖 Models Used
  ────────────────────────────────────────────────────────
  Model                          Sessions       Tokens
  inkling:free                          1    5,968,958

  📱 Platforms
  ────────────────────────────────────────────────────────
  Platform       Sessions   Messages         Tokens
  desktop               1        148      5,035,952

  🔧 Top Tools
  ────────────────────────────────────────────────────────
  Tool                            Calls        %
  terminal                           24    33.8%
  read_file                          14    19.7%
  write_file                          8    11.3%
  execute_code                        7     9.9%
  search_files                        7     9.9%
  skill_view                          4     5.6%
  memory                              2     2.8%
  clarify                             2     2.8%
  grep                                1     1.4%
  patch                               1     1.4%
  skills_list                         1     1.4%

  🧠 Top Skills
  ────────────────────────────────────────────────────────
  Skill                          Loads   Edits   Last used
  mcp-sequential-thinking            1       0      Sep 05
  plan                               1       0      Sep 05
  brainstorming                      1       0      Sep 05
  using-superpowers                  1       0      Sep 05
  Distinct skills: 4  Loads: 4  Edits: 0

  📅 Activity Patterns
  ────────────────────────────────────────────────────────
  Mon                  0
  Tue                  0
  Wed                  0
  Thu                  0
  Fri                  0
  Sat  ███████████████ 1
  Sun                  0

  Peak hours: 11AM (1)
  Active days: 1

  🏆 Notable Sessions
  ────────────────────────────────────────────────────────
  Most messages        148 msgs           (Sep 05, 20260905_115455_)
  Most tokens          200,624 tokens     (Sep 05, 20260905_115455_)
  Most tool calls      71 calls           (Sep 05, 20260905_115455_)


```
## fallback
exit=0
```

  No fallback providers configured.

  Add one with:  hermes fallback add


```
## model
exit=0
```

  Current model:    nemotron-3-ultra-free
  Active provider:  OpenCode Zen


  Select provider:
  Select by number, Enter to confirm.

  (○)  1. Nous Portal (Everything your agent needs, 300+ models with bundled tool use)
  (○)  2. Fireworks AI (OpenAI-compatible direct model API)
  (○)  3. OpenRouter (Pay-per-use API aggregator)
  (○)  4. Mixture of Agents (named presets; aggregator acts after reference models)
  (○)  5. NovitaAI (Cloud: Model API, Agent Sandbox, GPU Cloud)
  (○)  6. LM Studio (Local desktop app with built-in model server)
  (○)  7. Anthropic (Claude models via API key or Claude Code)
  (○)  8. OpenAI ▸ (ChatGPT/Codex subscription or direct OpenAI API)
  (○)  9. Qwen ▸ (Qwen Cloud / DashScope, Coding Plan, Token Plan & Qwen CLI OAuth)
  (○) 10. xAI Grok ▸ (Direct API or SuperGrok / Premium+ OAuth)
  (○) 11. Xiaomi MiMo (MiMo-V2.5 and V2 models: pro, omni, flash)
  (○) 12. Tencent Hy ▸ (Hy4 / Hy3 via TokenHub & TokenPlan)
  (○) 13. NVIDIA NIM (Nemotron models via build.nvidia.com or local NIM)
  (○) 14. GitHub Copilot ▸ (GitHub token API or copilot --acp process)
  (○) 15. Hugging Face Inference Providers
  (○) 16. Google AI Studio (Native Gemini API)
  (○) 17. Google Vertex AI (Gemini via GCP; OAuth2 service account or ADC, GCP billing/quotas)
  (○) 18. DeepSeek (V3, R1, coder, direct API)
  (○) 19. Z.AI / GLM (Zhipu direct API)
  (○) 20. Kimi / Moonshot ▸ (Coding Plan, Moonshot global & China endpoints)
  (○) 21. StepFun Step Plan (Agent / coding models via Step Plan API)
  (○) 22. MiniMax ▸ (Global, OAuth Coding Plan & China endpoints)
  (○) 23. Ollama Cloud (Cloud-hosted open models, ollama.com)
  (○) 24. Arcee AI (Trinity models, direct API)
  (○) 25. GMI Cloud (Multi-model direct API)
  (○) 26. Kilo Code (Kilo Gateway API)
  (●) 27. OpenCode ▸ (Zen pay-as-you-go, Go subscription, or free tier)  ← currently active
  (○) 28. AWS Bedrock (Claude, Nova, Llama, DeepSeek; IAM or API key)
  (○) 29. Azure Foundry (OpenAI-style or Anthropic-style endpoint, your Azure AI deployment)
  (○) 30. Vercel AI Gateway (Multi-model aggregator)
  (○) 31. Actual Computer - hosted inference via api.actual.inc, or local offline inference via ACTUAL_BASE_URL
  (○) 32. CommandCode — 20+ models via OpenAI-compatible API
  (○) 33. CommandCode — Claude models via Anthropic Messages API
  (○) 34. custom (direct API)
  (○) 35. DeepInfra — 100+ open models, pay-per-use
  (○) 36. Meta Muse Spark family (Meta Superintelligence Labs)
  (○) 37. Nebius Token Factory — OpenAI-compatible inference
  (○) 38. Ramp Router (router.com) — routes each request to the cheapest model that clears your quality bar
  (○) 39. Upstage (Solar API)
  (○) 40. Api.groq.com (api.groq.com/openai/v1/chat/completions) — openai/gpt-oss-120b
  (○) 41. Ollama (127.0.0.1:11434/v1) — gemma4:12b
  (○) 42. Custom endpoint (enter URL manually)
  (○) 43. Remove a saved custom provider
  (○) 44. Configure auxiliary models...
  (○) 45. Leave unchanged

Select provider:
    1. Nous Portal (Everything your agent needs, 300+ models with bundled tool use)
    2. Fireworks AI (OpenAI-compatible direct model API)
    3. OpenRouter (Pay-per-use API aggregator)
    4. Mixture of Agents (named presets; aggregator acts after reference models)
    5. NovitaAI (Cloud: Model API, Agent Sandbox, GPU Cloud)
    6. LM Studio (Local desktop app with built-in model server)
    7. Anthropic (Claude models via API key or Claude Code)
    8. OpenAI ▸ (ChatGPT/Codex subscription or direct OpenAI API)
    9. Qwen ▸ (Qwen Cloud / DashScope, Coding Plan, Token Plan & Qwen CLI OAuth)
    10. xAI Grok ▸ (Direct API or SuperGrok / Premium+ OAuth)
    11. Xiaomi MiMo (MiMo-V2.5 and V2 models: pro, omni, flash)
    12. Tencent Hy ▸ (Hy4 / Hy3 via TokenHub & TokenPlan)
    13. NVIDIA NIM (Nemotron models via build.nvidia.com or local NIM)
    14. GitHub Copilot ▸ (GitHub token API or copilot --acp process)
    15. Hugging Face Inference Providers
    16. Google AI Studio (Native Gemini API)
    17. Google Vertex AI (Gemini via GCP; OAuth2 service account or ADC, GCP billing/quotas)
    18. DeepSeek (V3, R1, coder, direct API)
    19. Z.AI / GLM (Zhipu direct API)
    20. Kimi / Moonshot ▸ (Coding Plan, Moonshot global & China endpoints)
    21. StepFun Step Plan (Agent / coding models via Step Plan API)
    22. MiniMax ▸ (Global, OAuth Coding Plan & China endpoints)
    23. Ollama Cloud (Cloud-hosted open models, ollama.com)
    24. Arcee AI (Trinity models, direct API)
    25. GMI Cloud (Multi-model direct API)
    26. Kilo Code (Kilo Gateway API)
  → 27. OpenCode ▸ (Zen pay-as-you-go, Go subscription, or free tier)  ← currently active
    28. AWS Bedrock (Claude, Nova, Llama, DeepSeek; IAM or API key)
    29. Azure Foundry (OpenAI-style or Anthropic-style endpoint, your Azure AI deployment)
    30. Vercel AI Gateway (Multi-model aggregator)
    31. Actual Computer - hosted inference via api.actual.inc, or local offline inference via ACTUAL_BASE_URL
    32. CommandCode — 20+ models via OpenAI-compatible API
    33. CommandCode — Claude models via Anthropic Messages API
    34. custom (direct API)
    35. DeepInfra — 100+ open models, pay-per-use
    36. Meta Muse Spark family (Meta Superintelligence Labs)
    37. Nebius Token Factory — OpenAI-compatible inference
    38. Ramp Router (router.com) — routes each request to the cheapest model that clears your quality bar
    39. Upstage (Solar API)
    40. Api.groq.com (api.groq.com/openai/v1/chat/completions) — openai/gpt-oss-120b
    41. Ollama (127.0.0.1:11434/v1) — gemma4:12b
    42. Custom endpoint (enter URL manually)
    43. Remove a saved custom provider
    44. Configure auxiliary models...
    45. Leave unchanged

Choice [1-45] (27): 
No change.

```
