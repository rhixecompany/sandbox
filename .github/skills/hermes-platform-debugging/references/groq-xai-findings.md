# Groq and xAI Auth Findings

## Groq

- **Live models endpoint:** 200 with valid key
- **Hermes chat routing:** Not supported for chat; STT/TTS only
- **Conclusion:** Store `GROQ_API_KEY` in `.env` if voice features are needed. Do not set `model.provider: groq`.

## xAI / Grok

- **Live models endpoint:** 403 with valid key format
- **Error (confirmed 2026-08-11):** `permission-denied` — team has used all
  available credits or reached monthly spending limit. Distinct from a dead
  key: probe `/v1/models` with the stored key; a 403 naming the team/limit =
  billing exhaustion, 401 = key problem.
- **Hermes chat routing:** Supported via `xai` or `xai-oauth`
- **Conclusion:** Key is syntactically valid but unusable until xAI
  account/credits issue is resolved. Store `XAI_API_KEY` in `.env` for future
  use. Do NOT rotate/delete the key on 403 — top up credits instead.

## Pattern

Always validate API keys against live endpoints before configuring Hermes model routing. A 200 from `/v1/models` is necessary but not sufficient; also verify chat completions work.