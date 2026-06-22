# Phases

> Extracted from `boost-prompt.prompt.md`.

## Phases

### Phase 1: Interrogate

**Goal:** Understand the task scope, objectives, deliverables, and constraints.

**Steps:**
1. Read the user's draft prompt
2. Ask specific questions using `joyride_request_human_input` to clarify scope, deliverables, and constraints
3. Explore the project workspace using available tools to understand context
4. Run `/context-map` on the target area before producing the refined prompt

### Phase 2: Refine

**Goal:** Produce an improved, well-structured prompt.

**Steps:**
1. Organize the prompt into clear sections or steps
2. Apply markdown formatting for readability
3. Ensure the prompt is easy to understand and follow
4. Define expected deliverables and success criteria

### Phase 3: Deliver

**Goal:** Deliver the prompt to the user and system clipboard.

**Steps:**
1. Copy the prompt to the system clipboard using Joyride:

   ```clojure
   (require '["vscode" :as vscode])
   (vscode/env.clipboard.writeText "your-markdown-text-here")
   ```

2. Announce to the user that the prompt is on the clipboard
3. Type the prompt in chat

**Note**: If Joyride is unavailable (see "Tools Required" -> Fallback), manually select and copy the prompt text from your chat output.

### Phase 4: Iterate

**Goal:** Confirm satisfaction and handle revisions.

**Steps:**
1. Ask the user if they want any changes or additions
2. Repeat Phase 2-4 after any revisions
3. Stop once the user confirms satisfaction
