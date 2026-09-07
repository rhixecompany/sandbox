# Hermes Inventory Capture — 2026-09-05 08:19:35.418671

## hermes auth list

```$hermes auth list
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
  #2  api-key-1            api_key manual exhausted (402) (53m 47s left)
  #3  api-key-3            api_key manual exhausted (402) (53m 48s left)
  #4  api-key-4            api_key manual ←
  #5  api-key-2            api_key manual

openai-codex (2 credentials):
  #1  device_code          oauth   device_code ←
  #2  openai-codex-oauth-2 oauth   device_code rate-limited usage_limit_reached (429) (29d 16h left)

opencode-zen (4 credentials):
  #1  OPENCODE_ZEN_API_KEY api_key env:OPENCODE_ZEN_API_KEY
  #2  api-key-3            api_key manual auth failed (401) (re-auth may be required) ←
  #3  api-key-4            api_key manual auth failed (401) (re-auth may be required)
  #4  api-key-1            api_key manual

openrouter (2 credentials):
  #1  OPENROUTER_API_KEY   api_key env:OPENROUTER_API_KEY rate-limited (429) (16h 40m left)
  #2  api-key-2            api_key manual rate-limited (429) (42m 36s left)

xai (2 credentials):
  #1  api-key-1            api_key manual auth failed (403) (re-auth may be required) ←
  #2  XAI_API_KEY          api_key env:XAI_API_KEY

xai-oauth (1 credentials):
  #1  xai-oauth-oauth-1    oauth   device_code ←

# exit=0

---

## hermes config show

```$hermes config show

┌─────────────────────────────────────────────────────────┐
│              ⚕ Hermes Configuration                    │
└─────────────────────────────────────────────────────────┘

◆ Paths
  Config:       C:\Users\Alexa\AppData\Local\hermes\config.yaml
  Secrets:      C:\Users\Alexa\AppData\Local\hermes\.env
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
  Model:        {'base_url': 'https://api.openai.com/v1', 'default': 'gpt-5.6-luna', 'provider': 'openai-api'}
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

◆ Skill Settings
  hermes.skill.skills.enabled true  [hermes-skills]

────────────────────────────────────────────────────────────
  hermes config edit     # Edit config file
  hermes config set <key> <value>
  hermes setup           # Run setup wizard

# exit=0

---

## hermes status

```$hermes status

┌─────────────────────────────────────────────────────────┐
│                 ⚕ Hermes Agent Status                  │
└─────────────────────────────────────────────────────────┘

◆ Environment
  Project:      C:\Users\Alexa\AppData\Local\hermes\hermes-agent
  Python:       3.13.14
  .env file:    ✓ exists
  Model:        gpt-5.6-luna
  Provider:     OpenAI API

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
    Access exp: 2026-09-05 08:59:41 W. Central Africa Standard Time
    Key exp:    2026-09-05 08:59:41 W. Central Africa Standard Time
    Refresh:    yes
  OpenAI Codex  ✓ logged in
    Auth file:  C:\Users\Alexa\AppData\Local\hermes\auth.json
    Refreshed:  2026-09-04 22:30:54 W. Central Africa Standard Time
  Qwen OAuth    ✗ not logged in (run: qwen auth qwen-oauth)
    Auth file:  C:\Users\Alexa\.qwen\oauth_creds.json
    Error:      Qwen CLI credentials not found. Run 'qwen auth qwen-oauth' first.
  MiniMax OAuth  ✓ logged in
    Region:     global
    Access exp: 2027-08-31T16:20:05.475000+00:00
  xAI OAuth     ✓ logged in
    Auth file:  C:\Users\Alexa\AppData\Local\hermes\auth.json
    Refreshed:  2026-09-05 05:24:53 W. Central Africa Standard Time

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
  Jobs:         0 active, 2 total

◆ Sessions
  Active:       1 session(s)
  Last activity:   2026-08-24
  Slots:        1/10 in use
                cli               20260905_081227_b159fe   7m

────────────────────────────────────────────────────────────
  Run 'hermes doctor' for detailed diagnostics
  Run 'hermes setup' to configure

# exit=0

---

## hermes insights

```$hermes insights

  ╔══════════════════════════════════════════════════════════╗
  ║                    📊 Hermes Insights                    ║
  ║                       Last 30 days                       ║
  ╚══════════════════════════════════════════════════════════╝

  Period: Aug 19, 2026 — Sep 05, 2026

  📋 Overview
  ────────────────────────────────────────────────────────
  Sessions:          135           Messages:        8,179
  Tool calls:        4,849         User messages:   300
  Input tokens:      28,808,316    Output tokens:   1,800,784
  Total tokens:      459,164,627
  Active time:       ~25.1d        Avg session:     ~5h 5m
  Avg msgs/session:  60.6

  💰 Cost
  ────────────────────────────────────────────────────────
  Estimated:          ~$0.0053
  Included:           13 session(s) (subscription — no provider invoice)
  Unknown:            105 session(s) (no pricing data)

  🤖 Models Used
  ────────────────────────────────────────────────────────
  Model                          Sessions       Tokens
  minimax-m3:free                      30  169,317,064
  gpt-5.6-luna                         15  104,504,329
  nemotron-3-ultra-free                14   74,583,849
  longcat-2.0:free                      5   53,427,495
  solar-pro4:free                       7   23,055,224
  nemotron-3.5-lightning-free           2   14,502,007
  step-3.7-flash:free                  10   10,697,379
  nemotron-3-nano-omni-30b-a3b          4    5,129,752
  minimax-m3                            1    1,593,528
  inkling:free                          1    1,305,555
  mimo-v2.5-free                        2      313,261
  MiniMax-M3                            1      308,152
  big-pickle                            2      256,734
  gpt-5.4-mini                          1       52,719
  free                                  2       51,046
  gemini-2.5-flash                      1       35,442
  nemotron-3-ultra-550b-a55b:f          7       31,091
  gpt-5-mini                            0            0

  📱 Platforms
  ────────────────────────────────────────────────────────
  Platform       Sessions   Messages         Tokens
  tui                  87      4,688    224,363,536
  cli                  36      2,707    202,120,374
  subagent              7        395     10,263,935
  desktop               4        386     18,133,315
  telegram              1          3         49,807

  🔧 Top Tools
  ────────────────────────────────────────────────────────
  Tool                            Calls        %
  terminal                        2,165    33.5%
  read_file                       1,271    19.7%
  skill_view                        874    13.5%
  search_files                      463     7.2%
  tool_call                         311     4.8%
  execute_code                      267     4.1%
  patch                             244     3.8%
  write_file                        215     3.3%
  todo                              106     1.6%
  mcp__filesystem__read_text_file       95     1.5%
  mcp__filesystem__list_directory       90     1.4%
  delegate_task                      56     0.9%
  process                            51     0.8%
  mcp__filesystem__search_files       51     0.8%
  session_search                     42     0.7%
  ... and 21 more tools

  🧠 Top Skills
  ────────────────────────────────────────────────────────
  Skill                          Loads   Edits   Last used
  using-superpowers                 31       0      Sep 05
  user-communication-preferenc      30       0      Sep 05
  hermes-agent                      24       0      Sep 05
  create-implementation-plan        22       0      Sep 05
  plans-and-specs                   22       0      Sep 05
  mcp-filesystem                    22       0      Sep 05
  subagent-driven-development       21       0      Sep 05
  writing-clearly-and-concisel      20       0      Sep 05
  executing-plans                   20       0      Sep 05
  implementation-plan               20       0      Sep 05
  Distinct skills: 143  Loads: 874  Edits: 0

  📅 Activity Patterns
  ────────────────────────────────────────────────────────
  Mon  ███████         38
  Tue                  0
  Wed  █               1
  Thu                  0
  Fri  ███             18
  Sat  ███████████████ 78
  Sun                  0

  Peak hours: 5AM (27), 4AM (16), 1AM (15), 5PM (10), 6PM (9)
  Active days: 7
  Best streak: 2 consecutive days

  🏆 Notable Sessions
  ────────────────────────────────────────────────────────
  Longest session      4.2d               (Aug 31, 20260831_150617_)
  Most messages        759 msgs           (Aug 29, 20260829_004155_)
  Most tokens          6,163,869 tokens   (Aug 28, 20260828_225006_)
  Most tool calls      381 calls          (Aug 29, 20260829_004155_)

# exit=0

---

## hermes fallback list

```$hermes fallback list

  No fallback providers configured.

  Add one with:  hermes fallback add

# exit=0

---

