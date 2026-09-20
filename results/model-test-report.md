# 📊 Model Test Report

**Date**: 2026-09-14
**Repository**: SandBox (`clean-development` branch)
**Tested via**: `hermes chat --yolo --oneshot`

---

## 🔬 OpenRouter (free model)

| Field        | Value                                         |
| ------------ | --------------------------------------------- |
| **Model**    | `openrouter` (default routing)                |
| **Status**   | ⚠️ Timed out (90s)                            |
| **Warnings** | SOUL.md truncated (31513 chars > 20000 limit) |
| **Errors**   | Auxiliary title generation failed (HTTP 400)  |
| **Result**   | ❌ Not usable — provider timeout              |

**Notes**: OpenRouter model initialization succeeded but timed out during reasoning phase. The SOUL.md file exceeds the context limit, causing truncation warnings. This may affect model routing reliability.

---

## 🔬 OpenCode-Zen (free model)

| Field        | Value                                            |
| ------------ | ------------------------------------------------ |
| **Model**    | `opencode-zen`                                   |
| **Status**   | ✅ Successful                                    |
| **Fallback** | `inclusionai/ling-3.0-flash-fin:free` via `nous` |
| **Duration** | ~55 seconds                                      |
| **Messages** | 2 (1 user, 0 tool calls)                         |
| **Result**   | ✅ Hello response returned correctly             |

**Notes**: OpenCode-Zen model initialized successfully. When openrouter routing failed, it gracefully fell back to `inclusionai/ling-3.0-flash-fin:free` via the `nous` provider. The greeting was returned correctly.

---

## 📋 Summary

| Model        | Status     | Response Time | Notes                     |
| ------------ | ---------- | ------------- | ------------------------- |
| OpenRouter   | ❌ Timeout | >90s          | SOUL.md truncation issue  |
| OpenCode-Zen | ✅ Success | ~55s          | Graceful fallback to nous |

### ⚠️ Known Issues

1. **SOUL.md truncation**: File at 31513 chars exceeds 20000 char limit — trim or increase `context_file_max_chars`
2. **OpenRouter provider instability**: Free models on OpenRouter timed out consistently
3. **Model fallback working**: OpenCode-Zen correctly falls back to alternative providers

### ✅ Recommendations

1. Trim SOUL.md below 20000 chars or set `context_file_max_chars: 35000` in config.yaml
2. Use OpenCode-Zen as primary free model (stable with fallback)
3. Consider pinning a larger-context model if SOUL.md cannot be trimmed
