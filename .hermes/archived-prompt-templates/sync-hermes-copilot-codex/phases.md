# Phases

> Extracted from `sync-hermes-copilot-codex.prompt.md`.

## Phases

### Phase 1: Inventory Instructions & Agents

**Goal:** List and triage all instructions and agents, creating personalities and profiles.

**Inputs:** `.github/agents/` and `.github/instructions/` directories

**Outputs:** Personalities and profiles created for each instruction/agent

**Steps:**

| Step | Action                                                   | Output                |
| ---- | -------------------------------------------------------- | --------------------- |
| 1.1  | List all files in `.github/instructions/`                | Instruction inventory |
| 1.2  | For each instruction, create a corresponding personality | Personalities created |
| 1.3  | List all files in `.github/agents/`                      | Agent inventory       |
| 1.4  | For each agent, create a corresponding profile           | Profiles created      |

**Tasks:**

- **Task 1.1–1.2 — Instructions → Personalities:** Scan instructions, create matching personalities
- **Task 1.3–1.4 → Agents → Profiles:** Scan agents, create matching profiles

---

### Phase 2: Identify Root Folders

**Goal:** Locate all three AI agent root directories.

**Inputs:** Filesystem scan

**Outputs:** Identified root paths for Hermes, Copilot, and Codex

**Steps:**

| Step | Action                                                  | Output       |
| ---- | ------------------------------------------------------- | ------------ |
| 2.1  | Identify Hermes root folder (`~/AppData/Local/hermes/`) | Hermes path  |
| 2.2  | Identify Copilot root folder (`~/.copilot/`)            | Copilot path |
| 2.3  | Identify Codex root folder (`~/.codex/`)                | Codex path   |

---

### Phase 3: Sync Assets

**Goal:** Synchronize skills, plugins, and hooks across all three agents.

**Inputs:** Identified root paths from Phase 2

**Outputs:** Synced skills, plugins, and hooks

**Steps:**

| Step | Action                               | Output         |
| ---- | ------------------------------------ | -------------- |
| 3.1  | Sync skills across all three agents  | Skills synced  |
| 3.2  | Sync plugins across all three agents | Plugins synced |
| 3.3  | Sync hooks across all three agents   | Hooks synced   |

**Tasks:**

- **Task 3.1 — Skills Sync:** Bidirectional sync of skill directories
- **Task 3.2 — Plugins Sync:** Bidirectional sync of plugin directories
- **Task 3.3 — Hooks Sync:** Bidirectional sync of hook directories

---

### Phase 4: Verify & Implement

**Goal:** Verify the plan and specs, implement, and confirm completion.

**Inputs:** All previous phase outputs

**Outputs:** Verified and complete plan

**Steps:**

| Step | Action                              | Output                  |
| ---- | ----------------------------------- | ----------------------- |
| 4.1  | Verify the plan and specs           | Verification report     |
| 4.2  | Implement the plan and specs        | Implementation complete |
| 4.3  | Verify plan and specs are completed | Completion confirmation |
