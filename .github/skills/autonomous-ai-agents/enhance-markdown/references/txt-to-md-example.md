# TXT→MD Conversion Example

This file documents a worked conversion example using the 9-section template.
Source: `Prompts/generalprompts.txt` → `Prompts/generalprompts.md`

## Raw Input (before)

```
/brainstorming /plans-and-specs  /dispatching-parallel-agents
/subagent-driven-development  /systematic-debugging  /simplify
/plan /prompt-engineering for
- Write code faster with Context7 for codebase awareness and
  Sequential Thinking for structured problem-solving.
- Automate your development cycle: open issues, write code,
  and update tickets with GitHub and Atlassian.
- Run commands and scripts, manage files and control your
  system directly from your AI client.
```

## Enhanced & Templated Output (after)

### Skills Section
Derived from the `/command-name` references at the top. Each command maps to a skill:
- `brainstorming` → Ideation for dev workflow automation
- `plans-and-specs` → Plan automation workflows
- `dispatching-parallel-agents` → Parallel task execution

### Personas Section
Built from the task description's role framing:
> AI-Native Developer — writes code faster with Context7...

### Rules Section
Extracted guardrails from the input's imperative instructions:
- Always use Context7 for codebase awareness before making code changes
- Apply Sequential Thinking for structured problem-solving on complex issues
- Automate the development cycle end-to-end when possible

### Steps Section
Numbered high-level sequence derived from the bullet points:
1. Load Context7 skill for codebase awareness before any code work
2. Apply Sequential Thinking for structured problem-solving
3. Automate the development cycle: open issues, write code, update tickets
4. Run commands and scripts directly from the AI client
5. Manage files and control the system via CLI

### Tasks Section
Checklist items decomposed from each step's sub-actions:
- [ ] Load Context7 skill for codebase awareness
- [ ] Apply Sequential Thinking for structured problem-solving
- [ ] Automate opening issues with GitHub
- [ ] Automate writing code changes

### Actions Section
Tool-to-task mapping inferred from the described capabilities:
- `skill_view` — Load Context7 for codebase awareness
- `web_search` — Research API patterns and documentation
- `delegate_task` — Deploy automation subagents
- `terminal` — Run commands, scripts, manage files directly

## Template Application Rules (from the worked example)

1. **Optional section detection**: Skills → matched (tool references exist), Subagents → matched (delegation implied), Personas → matched (role definition present), Phases → NOT matched (0 stages defined), Subtasks → NOT matched (tasks are flat)
2. **Core 4 always present**: Rules, Steps, Tasks, Actions were always included
3. **Content provenance**: Every populated section traced back to the enhanced text — no invented content
4. **Absent sections omitted**: Phases and Subtasks were dropped cleanly

## Common Pitfalls Avoided

- Don't invent content for optional sections that don't have detectible source material
- Don't leave core sections empty — use `- N/A` if genuinely no applicable content
- The same-stem rule (`foo.txt` → `foo.md`) must preserve directory location
- Overwrite is acceptable for existing `.md` targets (output always regenerates from source `.txt`)
