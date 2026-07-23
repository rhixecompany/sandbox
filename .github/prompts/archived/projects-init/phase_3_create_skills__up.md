# Phase 3: Create Skills & Update

> Extracted from `projects-init.prompt.md`.

## Phase 3: Create Skills & Update

**Goal:** Scan `.github/prompts/`, identify needed skills and scripts, create them, update prompt frontmatter with correct skill dependencies.

**Inputs:** `.github/prompts/**`

**Outputs:** New skills in `~/AppData/Local/hermes/skills/`, prompts updated with skill references

**Steps:**

| Step | Action                                                                      | Output                 |
| ---- | --------------------------------------------------------------------------- | ---------------------- |
| 3.1  | List all prompts in `.github/prompts/`                                      | Prompt inventory       |
| 3.2  | For each prompt, extract referenced skills/tools from `skills:` frontmatter | Skill requirement list |
| 3.3  | Create any missing skills using `skill-manage`                              | Skills created         |
| 3.4  | Create supporting scripts in `~/AppData/Local/hermes/scripts/`              | Scripts created        |
| 3.5  | Update prompt frontmatter with correct skill dependency references          | Updated prompts        |

**Tasks:**

- **Task 3.1 — Inventory:** List all `.prompt.md` files in `.github/prompts/`
- **Task 3.2 — Extract skills:** Parse each prompt's YAML frontmatter `skills:` field; aggregate unique skill names
- **Task 3.3 — Create skills:** For each referenced skill that doesn't exist, run `skill_manage(action='create')` with minimal scaffold
- **Task 3.4 — Create scripts:** Write helper scripts to `~/AppData/Local/hermes/scripts/` as needed
- **Task 3.5 — Update prompts:** Ensure each prompt's `dependencies:` and `skills:` lists are accurate and reference real skills
