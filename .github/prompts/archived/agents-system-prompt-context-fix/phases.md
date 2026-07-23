# Phases

Extracted from `agents-system-prompt-context-fix.prompt.md`.

```
## Phases

### Phase 1: Generate Agent Context Files

**Goal:** Create/update all agent context files using architecture skills.

**Inputs:** Project and subproject directory structures

**Outputs:** Architecture, folder structure, and tech stack documents

**Steps:**

| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Run `architecture-blueprint-generator` | Architecture context files |
| 1.2 | Run `folder-structure-blueprint-generator` | Folder structure documents |
| 1.3 | Run `technology-stack-blueprint-generator` | Tech stack documents |

**Tasks:**

- **Task 1.1 — Architecture Blueprints:** Generate architecture context for project and subprojects
- **Task 1.2 — Folder Structures:** Document folder structure for project and subprojects
- **Task 1.3 — Technology Stacks:** Document tech stack for project and subprojects

---

### Phase 2: Audit VS Code Configuration

**Goal:** List, triage, audit, debug, enhance, and verify all VS Code JSON files.

**Inputs:** All `.vscode/**/*.json` files and folders containing `AGENTS.md`

**Outputs:** Enhanced and verified VS Code configuration

**Steps:**

| Step | Action | Output |
| --- | --- | --- |
| 2.1 | List all JSON files in `.vscode` and subfolders | File inventory |
| 2.2 | Triage all found JSON files | Triage report |
| 2.3 | Audit all configurations | Audit report |
| 2.4 | Debug any issues found | Debug log |
| 2.5 | Enhance configurations | Enhanced configs |
| 2.6 | Verify all configs | Verification report |

**Tasks:**

- **Task 2.1 — Inventory:** List all `.vscode/**/*.json` files across project and subprojects
- **Task 2.2–2.6 — Audit Pipeline:** Triage → Audit → Debug → Enhance → Verify

---

### Phase 3: Verify & Implement

**Goal:** Verify the plan and specs, implement, and confirm completion.

**Inputs:** All previous phase outputs

**Outputs:** Verified and complete plan

**Steps:**

| Step | Action | Output |
| --- | --- | --- |
| 3.1 | Verify the plan and specs | Verification report |
| 3.2 | Imp
```

---
*Full content in original prompt.*
