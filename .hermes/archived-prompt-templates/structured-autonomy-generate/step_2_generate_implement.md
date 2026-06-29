# Step 2: Generate Implementation File

> Extracted from `structured-autonomy-generate.prompt.md`.

## Step 2: Generate Implementation File

Output the plan as a COMPLETE markdown document using the <plan_template>, ready to be saved as a `.md` file.

The plan MUST include:

- Complete, copy-paste ready code blocks with ZERO modifications needed
- Exact file paths appropriate to the project structure
- Markdown checkboxes for EVERY action item
- Specific, observable, testable verification points
- NO ambiguity - every instruction is concrete
- NO "decide for yourself" moments - all decisions made based on research
- Technology stack and dependencies explicitly stated
- Build/test commands specific to the project type

</workflow>

<research_task> For the entire project described in the master plan, research and gather:

1. **Project-Wide Analysis:**
   - Project type, technology stack, versions
   - Project structure and folder organization
   - Coding conventions and naming patterns
   - Build/test/run commands
   - Dependency management approach

2. **Code Patterns Library:**
   - Collect all existing code patterns
   - Document error handling patterns
   - Record logging/debugging approaches
   - Identify utility/helper patterns
   - Note configuration approaches

3. **Architecture Documentation:**
   - How components interact
   - Data flow patterns
   - API conventions
   - State management (if applicable)
   - Testing strategies

4. **Official Documentation:**
   - Fetch official docs for all major libraries/frameworks
   - Document APIs, syntax, parameters
   - Note version-specific details
   - Record known limitations and gotchas
   - Identify permission/capability requirements

Return a comprehensive research package covering the entire project context. </research_task>

<plan_template>

# {FEATURE_NAME}
