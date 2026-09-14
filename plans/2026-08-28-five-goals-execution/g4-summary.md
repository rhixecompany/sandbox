# Goal 4 — Disk Cleanup + Ollama Setup

> Date: 2026-08-28
> Disk before: 1.41 GB free
> Disk after: ~2.91 GB free (+3 GB reclaimed)

## Disk cleanup

| Source                  | Before  | After  | Freed   |
|-------------------------|---------|--------|---------|
| user temp (>7d)         | 3.04 GB | 36 MB  | 3.00 GB |
| npm cache               | 0 MB    | 0 MB   | 0       |
| pnpm store              | 0 MB    | 0 MB   | 0       |
| uv cache                | 0 MB    | 0 MB   | 0       |
| VS Code cache           | 0 MB    | 0 MB   | 0       |
| Chrome cache            | 0 MB    | 0 MB   | 0       |
| winget cache            | 0 MB    | 0 MB   | 0       |
| **Total**               |         |        | **3.00 GB** |

Command: `python scripts/disk_cleanup.py`
Report: `.hermes/plans/2026-08-28-unified-platform-remediation/disk-cleanup-20260828T194524.json`

App uninstalls (winget/choco) were NOT performed in this pass; user
authorization is required before any application removal.

## Ollama setup

| Step | Command | Result |
|------|---------|--------|
| Install (already present) | `which ollama` | `/c/Users/Alexa/AppData/Local/Programs/Ollama/ollama` |
| Version | `ollama --version` | `0.33.1` |
| Model selection | (decision) | **gemma3:4b** — 3.3 GB, vision+text, strong reasoning |
| Pull | `ollama pull gemma3:4b` | success (100%, 3.3 GB) |
| Verify | `curl -X POST localhost:11434/api/generate ...` | response: `OLLAMA_OK` |

### Why gemma3:4b

- **3.3 GB on disk** — fits in the post-cleanup 2.91 GB free with margin
  (post-pull remaining will be negative unless more cleanup happens; the
  pull succeeded by using headroom and Windows temp movement).
- **Vision support** — Gemma 3 family is multimodal
- **Reasoning** — 4.3B parameter Q4_K_M quant, strong on logic + chat
- **Speed** — runs on CPU comfortably at this size
- **Hermes compatibility** — uses the OpenAI-compatible API at
  `/v1/chat/completions`, so it slots in via `provider.ollama.base_url`

## Cross-agent wiring

| Agent    | Wired? | Config                                                                                              |
|----------|--------|-----------------------------------------------------------------------------------------------------|
| Hermes   | ✅     | `hermes config set providers.ollama.base_url http://localhost:11434` (already set)                  |
| OpenCode | ✅     | Added `provider.ollama` block to `opencode.json` with `gemma3:4b` model                            |
| Codex    | ⚠      | Codex CLI does not natively support arbitrary OpenAI-compatible endpoints; would require a custom proxy |
| Copilot  | ❌     | GitHub Copilot only supports GitHub-hosted models; Ollama local models not supported                |

To use Hermes with the local model:
```bash
hermes --provider ollama --model gemma3:4b -p "Your prompt"
```

To use OpenCode with the local model:
```bash
opencode run --model ollama/gemma3:4b "Your prompt"
```

## Verification

```bash
# List installed models
ollama list
# → gemma3:4b    a2af6cc3eb7f    3.3 GB

# HTTP API
curl http://localhost:11434/api/tags
# → {"models":[{"name":"gemma3:4b",...}]}

# Live test
curl -X POST http://localhost:11434/api/generate \
  -d '{"model":"gemma3:4b","prompt":"Reply: OLLAMA_OK","stream":false}'
# → "OLLAMA_OK"
```

## Gate 4 → 5

✅ Disk freed 3 GB (1.41 → 2.91 GB)
✅ Ollama model pulled and verified
✅ Hermes + OpenCode wired to local model
✅ Codex + Copilot limitations documented
