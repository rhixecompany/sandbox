---
category: software-development
title: Caveman Unified
name: caveman-unified
description: "Use when token limits are tight, reducing verbosity in communication, commits, reviews, or code. Triggers: caveman mode, less tokens, be brief, /caveman."
---

## caveman-unified

Unified ultra-compressed communication skill consolidating caveman, caveman-commit, caveman-compress, and caveman-review into a single modular system.

## Verification Checklist

- [ ] Prerequisites verified and available
- [ ] Caveman Unified operations completed successfully
- [ ] Configuration or output verified against requirements
- [ ] No errors or warnings during execution
- [ ] Changes documented and committed if applicable

## Description

Ultra-compressed communication mode cutting token usage ~75% while maintaining technical accuracy. Provides specialized compression for code, commits, reviews, and general communication with multiple intensity levels (lite, full, ultra, wenyan variants).

## When to Use

Use this skill when:

- Token limits are tight or context optimization needed
- Need to reduce verbosity in any communication
- Compressing explanations, commits, reviews, or code
- Saving context space for active work
- User says "caveman mode", "talk like caveman", "less tokens", "be brief", "/caveman"
- Writing commit messages with minimal noise
- Reviewing code with terse, focused feedback
- Compressing memory files or session archives

**Triggers**: "Caveman mode", "Talk like caveman", "Less tokens", "Be brief", "/caveman", "write a commit", "code review", "compress this", "token-optimization"

## When NOT to Use

- For formal documentation or client-facing communication
- For detailed explanations where clarity is paramount
- For code comments requiring full context
- For user-facing content or marketing copy
- When technical precision cannot be sacrificed
- For accessibility-critical content

## Workflow

### Phase 1: Understand Context & Intent

- Identify key information to preserve
- Determine compression intensity needed (lite/full/ultra)
- Plan compression strategy based on domain (code/commit/review/general)
- Remove unnecessary details while preserving meaning

### Phase 2: Apply Compression Rules

- Remove filler words and redundant phrases
- Shorten sentences to essential clauses
- Use abbreviations and symbols where clear
- Apply domain-specific compression (commit: subject ≤50 chars; review: one-line per issue)
- Eliminate promotional adjectives and AI puffery

### Phase 3: Verify Technical Accuracy

- Check that meaning is preserved
- Ensure clarity despite brevity
- Verify completeness of critical information
- Test understanding by re-reading

## Compression Levels

### Lite

- Remove obvious redundancy
- Keep full sentences
- Preserve all technical terms
- ~30% token reduction

### Full

- Aggressive abbreviation
- Short phrases instead of sentences
- Domain-specific shorthand
- ~75% token reduction

### Ultra

- Minimal punctuation
- Single words/symbols
- Extreme abbreviation
- ~85% token reduction

### Wenyan Variants

- wenyan-lite: Lite compression with classical Chinese style
- wenyan-full: Full compression with classical Chinese style
- wenyan-ultra: Ultra compression with classical Chinese style

## Specialized Domains

### Caveman-Commit

- Subject: ≤50 chars, conventional commits format
- Body: Only when "why" isn't obvious
- Remove noise, preserve intent and reasoning
- Example: "fix: auth token expiry handling in session manager"

### Caveman-Compress

- Compress memory files into caveman-speak
- ~75% token reduction for session archives
- Preserve decision rationale and key findings
- Ideal for CLAUDE.md optimization

### Caveman-Review

- One-line per issue: location, problem, fix
- Terse, focused feedback
- No verbose explanations
- Example: "src/auth.ts:42 - missing null check on user.id, add guard clause"

## Tools & References

- **Related Skills**: writing-clearly-and-concisely (humanization), caveman-compress (memory optimization)
- **Compression Principles**: Remove filler, preserve meaning, abbreviate aggressively
- **Token Savings**: Typical 75% reduction across all domains
- **Best Practices**: Always verify technical accuracy after compression

## Best Practices

1. **Preserve Critical Information**: Never sacrifice technical accuracy for brevity
2. **Domain Awareness**: Use appropriate compression level for context (commit vs. review vs. general)
3. **Verify Clarity**: Re-read compressed output to ensure meaning is clear
4. **Test Understanding**: Have someone else read it to confirm comprehension
5. **Use Abbreviations Consistently**: Define once, then use throughout
6. **Avoid Ambiguity**: Compress structure, not critical details
7. **Combine with Other Skills**: Use with writing-clearly-and-concisely for maximum clarity

## Examples

### General Caveman (Full)

- Before: "The system encountered a critical issue where the authentication token expired unexpectedly, causing all active user sessions to be terminated abruptly."
- After: "Auth token expired → all sessions killed"
