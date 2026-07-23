# Phases

Extracted from `ai-prompt-engineering-safety-review.prompt.md`.

```
## Phases

### Phase 1: Analyze the prompt

**Goal:** understand what the prompt asks for and where it may fail.

#### Phase 1 Steps

| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Run `/context-map` for prompt sources, references, and related files | Context map |
| 1.2 | Classify the task and domain | Task summary |
| 1.3 | Review safety, bias, and security risks | Risk notes |
| 1.4 | Review clarity and completeness | Quality notes |

#### Phase 1 Tasks
- Identify the prompt's purpose
- Find unsafe or ambiguous instructions
- Capture missing context that affects quality
- If the prompt contains apparent PII, credentials, or secrets, redact them with placeholders (for example, `[API_KEY]`) in the revised prompt and flag this explicitly in the report

### Phase 2: Improve the prompt

**Goal:** rewrite the prompt into a safer, clearer version.

#### Phase 2 Steps

| Step | Action | Output |
| --- | --- | --- |
| 2.1 | Keep the original intent | Rewritten scope |
| 2.2 | Add missing constraints or safeguards | Improved prompt |
| 2.3 | Remove redundant or risky language | Cleaner draft |

#### Phase 2 Tasks
- Make the task easier to execute
- Reduce ambiguity
- Keep the rewrite concise

### Phase 3: Test the revised prompt

**Goal:** compare the revised prompt against the original for reliability and safety.

#### Phase 3 Steps

| Step | Action | Output |
| --- | --- | --- |
| 3.1 | Compare revised vs original on safety (better/equal/worse) | Safety comparison + one-sentence reason |
| 3.2 | Compare revised vs original on clarity (better/equal/worse) | Clarity comparison + one-sentence reason |
| 3.3 | Compare revised vs original on usability (better/equal/worse) | Usability comparison + one-sentence reason |

#### Phase 3 Tasks
- Look for remaining risky instructions
- Confirm the output shape is obvious
- Confirm the prompt still matches the user's goal
- For safety, clarity, and usability, state whether the revised prompt is better than, equal to, or worse
```

---
*Full content in original prompt.*
