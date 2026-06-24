# 3. Prioritization Phase

> Extracted from `gen-specs-as-issues.prompt.md`.

## 3. Prioritization Phase

- Apply a score to each identified gap:

**Scoring Matrix (1-5 scale):**

- User Impact: How many users benefit?
- Strategic Alignment: Fits core mission?
- Implementation Feasibility: Technical complexity?
- Resource Requirements: Development effort needed?
- Risk Level: Potential negative impacts?

**Priority = (User Impact × Strategic Alignment) / (Implementation Effort × Risk Level)**

**Output Creation:**

- Present the top 3 highest-priority missing features based on the scoring
- For each, provide:
  - Feature name
  - Current status
  - Impact if not implemented
  - Dependencies on other features
