---
name: shared-managed-agents-onboarding
description: "Managed Agents — Onboarding Flow"
version: 1.0.0
author: Alexa
---
     1|# Managed Agents — Onboarding Flow
     2|
     3|> **Invoked via `/claude-api managed-agents-onboard`?** You're in the right place. Run the interview below — don't summarize it back to the user, ask the questions.
     4|
     5|Use this when a user wants to set up a Managed Agent from scratch. Three steps: **branch on know-vs-explore → configure the template → set up the session**. End by emitting working code.
     6|
     7|> Read `shared/managed-agents-core.md` alongside this — it has full detail for each knob. This doc is the interview script, not the reference.
     8|
     9|---
    10|
    11|Claude Managed Agents is a hosted agent: Anthropic runs the agent loop on its orchestration layer and provisions a sandboxed container per session where the agent's tools execute. You supply the agent config and the environment config; the harness — event stream, sandbox orchestration, prompt caching, context compaction, and extended thinking — is handled for you.
    12|
    13|**What you supply:**
    14|
    15|- **An agent config** — tools, skills, model, system prompt. Reusable and versioned.
    16|- **An environment config** — the sandbox your agent's tools execute in (networking, packages). Reusable across agents.
    17|
    18|Each run of the agent is a **session**.
    19|
    20|---
    21|
    22|## 1. Know or explore?
    23|
    24|Ask the user:
    25|
    26|> Do you already know the agent you want to build, or would you like to explore some common patterns first?
    27|
    28|### Explore path — show the patterns
    29|
    30|Four shapes, same runtime code path (`sessions.create()` → `sessions.events.send()` → stream). Only the trigger and sink differ.
    31|
    32|| Pattern | Trigger | Example |
    33|| --- | --- | --- | --- |
    34|| Event-triggered | Webhook | GitHub PR push → CMA (GitHub tool) → Slack | # <------ MC maybe delete? |
    35|| Scheduled | Cron | Daily brief: browser + GitHub + Jira → CMA → Slack | # <------ MC maybe delete? |
    36|| Fire-and-forget PR | Human | Slack slash-command → CMA (GitHub tool) → PR passing CI |
    37|| Research + dashboard | Human | Topic → CMA (web search + `frontend-design` skill) → HTML dashboard |
    38|
    39|Ask which shape fits, then continue with the Know path using it as the reference.
    40|
    41|### Know path — configure template
    42|
    43|Three rounds. Batch the questions in each round; don't ask them one at a time.
    44|
    45|**Round A — Tools.** Start here; it's the most concrete part. Three types; ask which the user wants (any combination):
    46|
    47|| Type | What it is | How to guide |
    48|| --- | --- | --- |
    49|| **Prebuilt Claude Agent tools** (`agent_toolset_20260401`) | Ready-to-use: `bash`, `read`, `write`, `edit`, `glob`, `grep`, `web_fetch`, `web_search`. Enable all at once, or individually via `enabled: true/false`. | Recommend enabling the full toolset. List the 8 tools so the user knows what they're getting. Full detail: `shared/managed-agents-tools.md` → Agent Toolset. |
    50|| **MCP tools** | Third-party integrations (GitHub, Linear, Asana, etc.) via `mcp_toolset`. Credentials live in a vault, not inline. | Ask which services. For each, walk through MCP server URL + vault credentials. Full detail: `shared/managed-agents-tools.md` → MCP Servers + Vaults. |
    51|| **Custom tools** | The user's own app handles these tool calls — agent fires `agent.custom_tool_use`, the app sends a result message back. | Ask for each tool: name, description, input schema. The app code that handles the event is _their_ code — don't generate it. Full detail: `shared/managed-agents-tools.md` → Custom Tools. |
    52|
    53|**Round B — Skills, files, and repos.** What the agent has on hand when it starts.
    54|
    55|_Skills_ — two types; both work the same way — Claude auto-uses them when relevant. Max 20 per agent.
    56|
    57|- [ ] **Pre-built Agent Skills**: `xlsx`, `docx`, `pptx`, `pdf`. Reference by name.
    58|- [ ] **Custom Skills**: skills uploaded to the user's org via the Skills API. Reference by `skill_id` + optional `version`. If the skill doesn't exist yet, walk the user through `POST /v1/skills` + `POST /v1/skills/{id}/versions` (beta header `skills-2025-10-02`). Full detail: `shared/managed-agents-tools.md` → Skills + Skills API.
    59|
    60|_GitHub repositories_ — any repos the agent needs on-disk? For each:
    61|
    62|- [ ] Repo URL (`https://github.com/org/repo`)
    63|- [ ] `authorization_token` (PAT or GitHub App token scoped to the repo)
    64|- [ ] Optional `mount_path` (defaults to `/workspace/<repo-name>`) and `checkout` (branch or SHA)
    65|
    66|Emit as `resources: [{type: "github_repository", url, authorization_token, ...}]`. Full detail: `shared/managed-agents-environments.md` → GitHub Repositories.
    67|
    68|> ‼️ **PR creation needs the GitHub MCP server too.** `github_repository` gives filesystem access only — to open PRs, also attach the GitHub MCP server in Round A and credential it via a vault. The workflow is: edit files in the mounted repo → push branch via `bash` → create PR via the MCP `create_pull_request` tool.
    69|
    70|_Files_ — any local files to seed the session with? For each:
    71|
    72|- [ ] Upload via the Files API → persist `file_id`
    73|- [ ] Choose a `mount_path` — absolute, e.g. `/workspace/data.csv` (parents auto-created; files mount read-only)
    74|
    75|Emit as `resources: [{type: "file", file_id, mount_path}]`. Max 999 file resources. Agent working directory defaults to `/workspace`. Full detail: `shared/managed-agents-environments.md` → Files API.
    76|
    77|**Round C — Environment + identity:**
    78|
    79|- [ ] Networking: unrestricted internet from the container, or lock egress to specific hosts? (If locked, MCP server domains must be in `allowed_hosts` or tools silently fail.)
    80|- [ ] Name?
    81|- [ ] Job (one or two sentences — becomes the system prompt)?
    82|- [ ] Model? (default `claude-opus-4-7`)
    83|
    84|---
    85|
    86|## 2. Set up the session
    87|
    88|Per-run. Points at the agent + environment, attaches credentials, kicks off.
    89|
    90|**Vault credentials** (if the agent declared MCP servers):
    91|
    92|- [ ] Existing vault, or create one? (`client.beta.vaults.create()` + `vaults.credentials.create()`)
    93|
    94|Credentials are write-only, matched to MCP servers by URL, auto-refreshed. See `shared/managed-agents-tools.md` → Vaults.
    95|
    96|**Kickoff:**
    97|
    98|- [ ] First message to the agent?
    99|
   100|Session creation blocks until all resources mount. Open the event stream before sending the kickoff. Stream is SSE; break on `session.status_terminated`, or on `session.status_idle` with a terminal `stop_reason` — i.e. anything except `requires_action`, which fires transiently while the session waits on a tool confirmation or custom-tool result (see `shared/managed-agents-client-patterns.md` Pattern 5). Usage lands on `span.model_request_end`. Agent-written artifacts end up in `/mnt/session/outputs/` — download via `files.list({scope_id: session.id, betas: ["managed-agents-2026-04-01"]})`.
   101|
   102|---
   103|
   104|## 3. Emit the code
   105|
   106|Go straight from the last interview answer to the code — no preamble about the setup-vs-runtime split, no "the critical thing to internalize…", no lecture about `agents.create()` being one-time. The two-block structure below already shows that; don't narrate it. Generate **two clearly-separated blocks** per language detected (Python/TS/cURL — see SKILL.md → Language Detection):
   107|
   108|**Block 1 — Setup (run once, store the IDs):**
   109|
   110|1. `environments.create()` → persist `env_id`
   111|2. `agents.create()` with everything from §Round A–C → persist `agent_id` and `agent_version`
   112|
   113|Label: `# ONE-TIME SETUP — run once, save the IDs to config/.env`
   114|
   115|**Block 2 — Runtime (run on every invocation):**
   116|
   117|1. Load `env_id` + `agent_id` from config/env
   118|2. `sessions.create(agent=AGENT_ID, environment_id=ENV_ID, resources=[...], vault_ids=[...])`
   119|3. Open stream, `events.send()` the kickoff, loop until `session.status_terminated` or `session.status_idle && stop_reason.type !== 'requires_action'` (see `shared/managed-agents-client-patterns.md` Pattern 5 for the full gate — do not break on bare `session.status_idle`)
   120|
   121|> ⚠️ **Never emit `agents.create()` and `sessions.create()` in the same unguarded block.** That teaches the user to create a new agent on every run — the #1 anti-pattern. If they need a single script, wrap agent creation in `if not os.getenv("AGENT_ID"):`.
   122|
   123|Pull exact syntax from `python/managed-agents/README.md`, `typescript/managed-agents/README.md`, or `curl/managed-agents.md`. Don't invent field names.
   124|