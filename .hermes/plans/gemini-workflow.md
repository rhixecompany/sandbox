# Gemini Provider Workflow Implementation Plan

**Date:** 2026-08-16  
**Provider:** gemini  
**Status:** pending  

---

## Goal

Implement the complete gemini provider workflow: credential verification (GOOGLE_API_KEY / GEMINI_API_KEY), model selection, free tier quota awareness, MCP compatibility, known bug workarounds, and auxiliary model offload.

## Architecture

Use the Hermes CLI to validate gemini as the 3rd fallback. Key concerns: free tier quota exhaustion (critical for agent workloads), doctor false positive bug (#26623), and tier detection bug (#21399).

## Tech Stack

- Hermes CLI
- GOOGLE_API_KEY or GEMINI_API_KEY
- gemini-2.5-flash model

---

## Tasks

### Task 1: Verify Credentials

**Step 1: Check env var**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes config env-path 2>&1'
cat "$(hermes config env-path 2>&1 | tail -1)" 2>&1 | grep -i gemini
```

**Step 2: List pooled credentials**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes auth list gemini 2>&1'
```

**Step 3: Check doctor (note known false positive)**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes doctor 2>&1 | grep -A2 gemini'
```

**Step 4: Document findings** → `.hermes/plans/results/gemini-auth.txt`

---

### Task 2: Verify Model Selection

**Step 1: List models**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes model 2>&1 | grep -A20 "gemini"'
```

**Step 2: Test model responsiveness**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes chat -q "What is machine learning?" -m gemini-2.5-flash 2>&1'
```

**Step 3: Test tool calling (function calling)**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes chat -q "Use the filesystem tool to list files in the current directory" 2>&1'
```

**Step 4: Document findings** → `.hermes/plans/results/gemini-model.txt`

---

### Task 3: Document Free Tier Quotas

**Objective:** Assess free tier limitations and expected consumption.

**Step 1: Research free tier limits**
- Document known Gemini free tier quotas
- Estimate per-session consumption (tool calls, retries, compression, auxiliary tasks)

**Step 2: Check for quota exhaustion in recent sessions**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes sessions list 2>&1 | head -10'
```

**Step 3: Document findings** → `.hermes/plans/results/gemini-quotas.txt`

---

### Task 4: MCP Compatibility (Sample)

**Objective:** Test MCP servers with gemini backing model.

**Step 1: Test sequential-thinking**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes mcp test sequential-thinking 2>&1'
```

**Step 2: Test github**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes mcp test github 2>&1'
```

**Step 3: Document findings** → `.hermes/plans/results/gemini-mcp.txt`

---

### Task 5: Compile Workflow Report

**Objective:** Produce complete gemini workflow report.

**Step 1: Aggregate all results**
Read all `.hermes/plans/results/gemini-*.txt` files.

**Step 2: Write final report**
Create `.hermes/plans/results/gemini-workflow-report.md` with all findings, recommendations, and open questions.

---

## Dependencies

- Task 1 → Task 2 → Tasks 3-4 (parallel) → Task 5

## Known Issues

- **hermes doctor false positive:** GitHub issue #26623 — doctor may report invalid API key even when it works. Don't block on doctor errors; test actual chat instead.
- **Free tier exhaustion risk:** Free tier quotas are low for agentic workloads. A single complex session can exhaust quota.
- **Tier detection bug:** GitHub issue #21399 — probe_gemini_tier() may report "paid" for free-tier keys when rate-limit headers are absent.

## Verification

- [ ] All CLI commands executed
- [ ] Results files written
- [ ] Free tier quota analysis included
- [ ] Doctor false positive documented

## Approval Gate

Review this plan and results before proceeding to the next provider.
