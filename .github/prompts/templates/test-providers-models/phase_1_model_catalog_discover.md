# Phase 1: Model Catalog Discovery (Needed ✓)

> Extracted from `test-providers-models.prompt.md` for DRY templating.

## Phase 1: Model Catalog Discovery (Needed ✓)

**Profile:** `research-analyst` | **Persona:** Research Analyst

**Goal:** For each provider, discover available models through their
respective model discovery mechanisms.

**Tools:** `fetch`/`web_extract`, `terminal`, `execute_code`

**Skills:** `plans-and-specs`

**Inputs:** Provider inventory from Phase 0

**Outputs:** Per-provider model catalog table

### Provider Discovery Methods — Results (2026-06-21)

| Provider     | Discovery Method     | Models Found | Free Models | Status                       |
| ------------ | -------------------- | ------------ | ----------- | ---------------------------- |
| openrouter   | OpenRouter Live API  | 340 total    | 27 free     | ✅ Live data                 |
| openai-api   | OpenAI models API    | N/A          | N/A         | ❌ Key not in subprocess env |
| huggingface  | HF Inference API     | 10+ warm     | Varies      | ✅ API query worked          |
| nous         | Hermes model catalog | 24 curated   | TBD live    | ✅ From catalog JSON         |
| ollama-cloud | Ollama tags API      | TBD          | TBD         | ◇ Not queried                |
| copilot      | GitHub Copilot API   | TBD          | TBD         | ⚠️ Rate-limited              |

**Key Discovery:** The Hermes Model Catalog (v1, updated 2026-06-16) contains only **33 curated OpenRouter models** and **24 Nous models**. The live OpenRouter API has **340 models** — 10× more. Always prefer the live API over the curated catalog for discovery.

### Steps

| Step | Action                             | Tools    | Output                |
| ---- | ---------------------------------- | -------- | --------------------- |
| 1.1  | Fetch OpenRouter model catalog     | fetch    | OpenRouter model list |
| 1.2  | Fetch OpenAI model catalog         | fetch    | OpenAI model list     |
| 1.3  | Fetch HuggingFace inference models | fetch    | HF model list         |
| 1.4  | Fetch Nous Hermes catalog          | fetch    | Nous model list       |
| 1.5  | Fetch Ollama cloud catalog         | fetch    | Ollama model list     |
| 1.6  | Fetch Copilot available models     | terminal | Copilot model list    |
| 1.7  | Compile per-provider model tables  | terminal | Catalog summary       |

### Verification

- [ ] All 6 providers queried for models
- [ ] Results captured in structured format
- [ ] Failed/disconnected providers noted
- [ ] Models with context window sizes recorded

---
