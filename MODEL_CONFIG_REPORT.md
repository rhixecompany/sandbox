# 📊 Hermes Model Configuration Report

**Workspace:** `C:\Users\Alexa\Desktop\SandBox`  
**Generated:** 2026-09-10 01:37:59  
**Status:** ✅ Complete

## 📋 Current Configuration

### Model Settings

- **Default Model:** `nemotron-3.5-lightning-free`
- **Provider:** `opencode-zen`
- **API Mode:** `chat_completions`
- **Max Turns:** `150`
- **Context Compression:** `Enabled` (Threshold: 90%, Target: 20%)

### API Keys Status

- **OpenRouter:** `sk-o...0554` (set)
- **OpenAI:** (not set for STT/TTS)
- **Exa, Firecrawl, Tavily, Perplexity, Browserbase, Browser Use, FAL, Anthropic:** (not set)

### Fallback Configuration

- **Current Fallback Providers:** `[]` (empty - not actively configured via hermes CLI)
- **Config File Fallback Models** (from config.yaml):
  - `opencode-zen` (primary)
  - `deepseek`
  - `nous`

### Model Testing Results

| Model                         | Status       | Notes                          |
| ----------------------------- | ------------ | ------------------------------ |
| `nemotron-3.5-lightning-free` | ✅ **WORKS** | Primary model via opencode-zen |
| `deepseek-v4-flash-free`      | ✅ **WORKS** | Available as fallback          |
| `nemotron-3-ultra-free`       | ✅ **WORKS** | Available in config            |

### Configuration Commands Used

```bash
# Set the default model
hermes config set model nemotron-3.5-lightning-free

# Fallback models are configured in config.yaml:
# fallback_providers:
#   - opencode-zen
#   - deepseek
#   - nous

# Verify configuration
hermes config show
hermes model list
hermes fallback list
```
