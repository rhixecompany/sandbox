# Current Model Assessment

> Extracted from `model-recommendation.prompt.md` for DRY templating.

## Current Model Assessment

Specified model: `[Current Model]` (Multiplier: [X]x)

Recommendation: [Keep current model | Consider switching to [Recommended Model]]

Rationale: [Explanation]
```

**Tool Alignment Check**:

Verify model capabilities align with specified tools:

- If tools include `context7/*` or `sequential-thinking/*`: Recommend advanced reasoning models (Claude Sonnet 4.5, GPT-5, Claude Opus 4.1)
- If tools include vision-related references: Ensure model supports images (flag if GPT-5 Codex, Claude Sonnet 4, or mini models selected)
- If tools are read-only (search, fetch): Suggest cost-effective models (GPT-5 mini, Grok Code Fast 1)

### 5. Context7 Integration for Up-to-Date Information

**Leverage Context7 for Model Documentation**:

When uncertainty exists about current model capabilities, use Context7 to fetch latest information:

```markdown
**Verification with Context7**:

Using `context7/get-library-docs` with library ID `/websites/github_en_copilot`:

- Query topic: "model capabilities [specific capability question]"
- Retrieve current model features, multipliers, deprecation status
- Cross-reference against analyzed file requirements
```

**Example Context7 Usage**:

```
If unsure whether Claude Sonnet 4.5 supports image analysis:
→ Use context7 with topic "Claude Sonnet 4.5 vision image capabilities"
→ Confirm feature support before recommending for multi-modal tasks
```
