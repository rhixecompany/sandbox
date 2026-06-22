# Phases

> Extracted from `prompt-builder.prompt.md`.

## Phases

### Phase 1: Discovery

**Goal:** Gather all requirements through systematic questioning.

Preflight requirement:
- Run `/context-map` first to identify relevant prompt files, references, and dependencies.

**Steps:**

These 9 topic areas guide the discovery process. The actual interactive questions are phrased during execution.

| Topic # | Area | Details |
| --- | --- | --- |
| 1 | Prompt Identity & Purpose | Filename, one-sentence description, category |
| 2 | Persona Definition | Role, expertise level, domain knowledge, qualifications |
| 3 | Task Specification | Primary task, secondary tasks, inputs, constraints |
| 4 | Context & Variable Requirements | Selection, file references, input variables, workspace vars |
| 5 | Detailed Instructions & Standards | Step-by-step process, coding standards, patterns, things to avoid |
| 6 | Output Requirements | Format, new files, modifications, examples |
| 7 | Tool & Capability Requirements | File ops, execution, external, specialized, analysis tools |
| 8 | Technical Configuration | Mode (agent/ask/edit), model requirements, special constraints |
| 9 | Quality & Validation Criteria | Success measurement, validation steps, error handling |

### Phase 2: Generate

**Goal:** Produce the complete `.prompt.md` file using gathered requirements.

**Steps:**
1. Compile all answers into a prompt structure
2. Select appropriate frontmatter (description, agent mode, tools, model) and write the generated file to `.github/prompts/<filename>.prompt.md` unless the user specifies a different path during discovery (Topic 1)
3. Write persona section with specific role and expertise
4. Write task section with clear, measurable requirements
5. Write instructions section with step-by-step process
6. Write context/input section with variable usage
7. Write output section with expected format and structure
8. Write quality/validation section with success criteria

### Phase 3: Verify

**Goal:** Confirm the generated prompt follows repository patterns and is production-ready.

**Steps:**
1. Verify all required sections are present (frontmatter, persona, task, instructions, input, output, quality)
2. Check against high-quality pattern references (blueprints, specifications, guides)
3. Confirm the prompt is token-efficient and well-structured
4. Validate all tool references match available tools in the system
5. Review generated prompt for clarity, ambiguity, and logical flow
6. Confirm file is written to correct location and readable by user
