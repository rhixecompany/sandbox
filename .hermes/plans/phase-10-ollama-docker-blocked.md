# Phase 10: Ollama Cleanup + Docker Model Runner — BLOCKED

## Status: BLOCKED — Hardware Constraints

### Current Hardware
| Resource | Available | Required for target model |
|---|---|---|
| System RAM | 8 GB total, ~950 MB free | 16-32 GB+ for 200K context |
| Docker WSL2 | 2 GB limit, 4 CPUs | 8-16 GB+ |
| GPU | None (integrated only) | NVIDIA 8GB+ for vision/reasoning |
| Storage | Unknown SSD/HDD | 50-100 GB for model weights |

### Ollama Cleanup Status
- [x] Ollama CLI uninstalled (not on PATH)
- [x] `~/.ollama/models/` empty (0 blobs, 0 manifests)
- [x] `~/.ollama/config.json` preserved (348K — just config, no models)
- [x] No ollama containers running in Docker

### Docker Model Runner — Cannot Proceed
Target requirements:
- Context size: >200K
- Vision: Yes
- Reasoning: Yes

These require:
- NVIDIA GPU with 8GB+ VRAM, OR
- 16GB+ system RAM for CPU inference (very slow)

This system has neither. Local Docker model runner with these specs is not feasible.

### Recommended Alternatives

1. **Use cloud providers already configured** (nous, opencode-zen, openrouter) — these offer models with 131K+ context, vision, reasoning
2. **Ollama Cloud** — already configured in `~/.ollama/config.json` with `nemotron-3-ultra`
3. **Upgrade hardware** — NVIDIA GPU + 32GB RAM for local inference

### Next Steps
User to decide:
- A) Accept cloud-based models (already working)
- B) Upgrade hardware for local inference
- C) Reduce requirements (smaller model, no vision, less context)

---
Documented: 2026-08-31
