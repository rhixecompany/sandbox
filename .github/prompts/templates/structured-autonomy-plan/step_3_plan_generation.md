# Step 3: Plan Generation

> Extracted from `structured-autonomy-plan.prompt.md`.

## Step 3: Plan Generation

1. Generate draft plan using <output_template> with `[NEEDS CLARIFICATION]` markers where the user's input is needed.
2. Save the plan to "plans/{feature-name}/plan.md"
3. Ask clarifying questions for any `[NEEDS CLARIFICATION]` sections
4. MANDATORY: Pause for feedback
5. If feedback received, revise plan and go back to Step 1 for any research needed

</workflow>

<output_template> **File:** `plans/{feature-name}/plan.md`

```markdown
# {Feature Name}

**Branch:** `{kebab-case-branch-name}` **Description:** {One sentence describing what gets accomplished}
