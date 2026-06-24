# Phases

> Extracted from `context-map.prompt.md`.

## Phases

### Phase 1: Discover the scope

**Goal:** find the files and relationships that matter.

#### Steps

| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Search for task-related files | File shortlist |
| 1.2 | Map direct dependencies | Dependency list |
| 1.3 | Identify related tests and patterns | Reference list |

#### Tasks
- Start from the target area
- Follow imports and exports
- Include tests that may change

### Phase 2: Build the context map

**Goal:** turn the findings into a usable planning artifact.

#### Steps

| Step | Action | Output |
| --- | --- | --- |
| 2.1 | Organize files to modify | Modify list |
| 2.2 | Organize dependent files and tests | Dependency and test lists |
| 2.3 | Add reference patterns and risks | Context map |

#### Tasks
- Keep the table output concise
- Make the map easy to scan
- Highlight anything that may block the change

### Phase 3: Review the context map

**Goal:** confirm the map is complete enough to start work.

#### Steps

| Step | Action | Output |
| --- | --- | --- |
| 3.1 | Check for missing files or dependencies | Gap list |
| 3.2 | Check for unclear risk items | Risk notes |
| 3.3 | Prepare the final map | Review-ready map |

#### Tasks
- Remove unnecessary detail
- Keep the map current and specific
- Make sure the affected tests are visible

### Phase 4: Verify and hand off

**Goal:** hand off a usable pre-implementation map.

#### Steps

| Step | Action | Output |
| --- | --- | --- |
| 4.1 | Summarize the scope | Summary |
| 4.2 | Present the map | Context map |
| 4.3 | State the main risks | Risk assessment |

#### Tasks
- Keep the handoff short
- Make the next step obvious
- Do not implement the change here
