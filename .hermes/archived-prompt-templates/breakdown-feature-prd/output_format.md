# Output Format

> Extracted from `breakdown-feature-prd.prompt.md`.

## Output Format

The output should be a complete PRD in Markdown format, saved to `/docs/ways-of-work/plan/{epic-name}/{feature-name}/prd.md`.

### PRD Structure

#### 1. Feature Name

- A clear, concise, and descriptive name for the feature.

#### 2. Epic

- Link to the parent Epic PRD and Architecture documents.

#### 3. Goal

- **Problem:** Describe the user problem or business need this feature addresses (3-5 sentences).
- **Solution:** Explain how this feature solves the problem.
- **Impact:** What are the expected outcomes or metrics to be improved (e.g., user engagement, conversion rate, etc.)?

#### 4. User Personas

- Describe the target user(s) for this feature.

#### 5. User Stories

- Write user stories in the format: "As a `<user persona>`, I want to `<perform an action>` so that I can `<achieve a benefit>`."
- Cover the primary paths and edge cases.

#### 6. Requirements

- **Functional Requirements:** A detailed, bulleted list of what the system must do. Be specific and unambiguous.
- **Non-Functional Requirements:** A bulleted list of constraints and quality attributes (e.g., performance, security, accessibility, data privacy).

#### 7. Acceptance Criteria

- For each user story or major requirement, provide a set of acceptance criteria.
- Use a clear format, such as a checklist or Given/When/Then. This will be used to validate that the feature is complete and correct.

#### 8. Out of Scope

- Clearly list what is _not_ included in this feature to avoid scope creep.
