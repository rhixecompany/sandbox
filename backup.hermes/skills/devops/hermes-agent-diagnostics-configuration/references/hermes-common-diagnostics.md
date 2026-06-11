# Hermes Common Diagnostics Commands & Expected Outputs

## Command: hermes status

**Purpose:** Show current model, environment, gateway state, API keys, sessions

**Command:**
```bash
hermes status
```

**Expected Output:**
```
◆ Model
  Model:        qwen3.6-plus-free
  Provider:     OpenCode Zen
  ...

◆ Environment
  Project:      C:\Users\Alexa\AppData\Local\hermes\hermes-agent
  Python:       3.11.14
  .env file:    ✓ exists

◆ API Keys
  OpenRouter    ✓ sk-o...0554
  OpenAI        ✗ (not set)
  Google / Gemini  ✓ AIza...9EfU
  ...

◆ Gateway Service
  Status:       ✓ running
  Manager:      manual process
  PID(s):       16776, 13404
```

**Key Fields to Check:**
- `Model` — what model is active
- `Provider` — which provider is delivering it
- `Python` — environment version
- `API Keys` — which are configured (✓) and which are missing (✗)
- `Gateway Service` — is it running, what's the process ID

---

## Command: hermes insights

**Purpose:** Show usage metrics (sessions, messages, tool calls, token usage)

**Command:**
```bash
hermes insights
```

**Expected Output:**
```
Session count (30 days):      70
Total messages:               4,143
Tool call count:              2,157
Input tokens (approx):        5.3M
Output tokens (approx):       1.1M
...
```

**What It Tells You:**
- How many sessions have run recently
- How active the agent is
- Token consumption trends
- Tool usage patterns

---

## Command: hermes doctor

**Purpose:** Full health check (config, security, environment, dependencies)

**Command:**
```bash
hermes doctor
```

**Expected Output (All Clear):**
```
✓ No active security advisories
✓ Config version up to date
✓ Python environment: 3.11.14
✓ All required directories present
✓ External tools available (git, docker, node)
```

**If Issues Found:**
```
Issues found:
  1. Run hermes setup — config initialization

Fix with: hermes doctor --fix
```

---

## Command: hermes doctor --fix

**Purpose:** Automatically repair issues found by doctor

**Command:**
```bash
hermes doctor --fix
```

**Expected Output:**
```
Fixing identified issues...
✓ Setup completed
✓ Config initialized
```

**When to Use:**
- After hermes doctor reports issues
- After fresh install
- After major config changes

---

## Command: hermes fallback list

**Purpose:** Show primary model and fallback provider chain

**Command:**
```bash
hermes fallback list
```

**Expected Output (With Fallbacks):**
```
Primary:   qwen3.6-plus-free  (via opencode-zen)

  Fallback chain (2 entries):
    1. meta-llama/llama-3.3-70b-instruct:free  (via openrouter)
    2. gemini-3.1-flash  (via google-gemini)

  Tried in order when the primary fails (rate-limit, 5xx, connection errors).
```

**Expected Output (No Fallbacks):**
```
No fallback providers configured.

  Add one with:  hermes fallback add
```

---

## URL Endpoint Validation Pattern

**Test if Provider Endpoint is Accessible:**

```bash
curl -s -I https://opencode.ai/zen/v1/models
```

**Expected:**
```
HTTP/1.1 200 OK
Date: Mon, 25 May 2026 15:07:51 GMT
Content-Type: application/json
Connection: keep-alive
Server: cloudflare
```

**Parsing:**
- First line: HTTP status (200 = accessible, 404 = not found, 503 = down, 403 = auth required)
- `Content-Type: application/json` — endpoint returns JSON (good sign)

**Common Status Codes:**
- `200 OK` — endpoint working
- `403 Forbidden` — endpoint exists but auth required (often fine if API key configured)
- `404 Not Found` — endpoint doesn't exist at that URL
- `503 Service Unavailable` — provider temporarily down
- Connection refused — network blocked or provider down

---

## Troubleshooting Decision Tree

```
Run: hermes status
     |
     ├─ Model is wrong or missing?
     │  └─ Run: hermes model (to pick a different one)
     │
     ├─ API Keys all missing?
     │  └─ Check: cat ~/.env
     │  └─ Add keys if needed
     │
     └─ OK → Next step

Run: hermes doctor
     |
     ├─ Issues found?
     │  └─ Run: hermes doctor --fix
     │  └─ Rerun: hermes doctor (to verify fixed)
     │
     └─ All clear → Next step

Run: hermes fallback list
     |
     ├─ No fallbacks configured?
     │  └─ See: references/fallback-routing-setup.md
     │  └─ Configure via Python script
     │
     └─ Fallbacks present → Done
```

---

## Regular Maintenance

### Weekly
```bash
hermes doctor        # Check for any creeping issues
```

### Monthly
```bash
hermes status        # See current model & API keys
hermes insights      # Check usage trends
hermes fallback list # Verify fallback chain still configured
```

### After System Changes
```bash
hermes doctor --fix  # Repair any broken config
hermes status        # Verify all systems ready
```

---

## Common Issues & Fixes

| Symptom | Check | Fix |
|---------|-------|-----|
| Model queries failing | `hermes status` → API key missing | Set key in .env, restart |
| Fallback not working | `hermes fallback list` → Shows empty | Configure fallbacks (see setup ref) |
| Gateway won't start | `hermes status` → Gateway: ✗ | `hermes doctor --fix` |
| Config corrupted | `hermes doctor` → Multiple errors | Restore from backup, reconfigure |
| Endpoint unreachable | `curl -I https://...` → 503 | Provider down, try fallback or wait |

---

## Related

- Skill: hermes-agent-diagnostics-configuration
- Reference: fallback-routing-setup.md
- Docs: https://hermes-agent.nousresearch.com/docs
