---
author: Alexa
description: 'Use when interacting with the Claude API: client patterns, managed agents,
  and examples.'
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: claude-api
tags:
- imported
title: Claude Api
version: 1.0.0

---
# Claude Api

## Description

Use when interacting with the Claude API: client patterns, tool use, streaming, and configuration.

## When to Use

- Building applications with Claude API or Anthropic SDK
- Implementing prompt caching for cost/latency optimization
- Migrating between Claude model versions (4.5 → 4.6 → 4.7)
- Adding/modifying Claude features (thinking, tool use, batch, files, citations, memory)
- Debugging cache hit rates or token usage
- Questions about Managed Agents or SDK best practices

## When NOT to Use

- Code imports `openai` or other provider SDKs
- Provider-neutral code or general programming questions
- Built-in language features or standard library usage
- Projects using OpenAI, Gemini, or other non-Anthropic APIs

## Workflow

### Phase 1: Understand Requirements

- Identify Claude model version and feature needs
- Determine if prompt caching applies (cost/latency sensitive?)
- Check for existing SDK code to migrate

### Phase 2: Design Solution

- Choose appropriate Claude model (Opus/Sonnet/Haiku)
- Plan prompt caching strategy if applicable
- Design tool use or batch processing if needed

### Phase 3: Implement & Optimize

- Write SDK code with proper error handling
- Enable prompt caching with cache_control blocks
- Test cache hit rates and token usage
- Migrate code between model versions if needed

### Phase 4: Verify & Document

- Confirm cache hits are working
- Validate token counts and costs
- Document model-specific behavior

## Tools & References

- **Anthropic SDK**: https://github.com/anthropic-ai/anthropic-sdk-python
- **Prompt Caching**: Reduces latency and cost for repeated context
- **Model Versions**: Track deprecations and new features

## Skills Required

| Skill | Purpose |
|-------|---------|
| `context7` | Look up current Anthropic SDK documentation |
| `systematic-debugging` | Diagnose SDK integration issues |

## Best Practices

- Always include error handling for API calls
- Use prompt caching for large, repeated context
- Test cache hit rates in development
- Monitor token usage and costs
- Keep SDK dependencies up to date
- Document model-specific behavior in code comments

## Verification Checklist

- [ ] Client is configured with proper error handling and retries
- [ ] Prompt caching is enabled where appropriate for repeated context
- [ ] Cache hit rates are verified in development
- [ ] Model version and feature requirements are clearly identified
- [ ] Token usage and costs are monitored

## Pitfalls

- Not enabling prompt caching for large system prompts wastes tokens and latency
- Hardcoding model versions without migration planning breaks on deprecation
- Missing error handling on API calls causes silent failures in production
- Ignoring rate limits leads to intermittent 429 errors under load
