# Phases

## Phase 1: Discovery

**Purpose:** Inventory all 11 root generator prompts in the repository, classify them by role, and produce a dependency matrix.

**Steps:**

1. Locate all `.prompt.md` files in the `.github/prompts/` directory.
2. Filter to exactly the 11 root generator prompts (listed in the orchestrator prompt's Subagents section).
3. Confirm count = 11; if not, halt with inventory_drift error.
4. Classify each prompt into one of three roles:
   - **Analysis** — produces diagnostic/detection output (stack, folder structure)
   - **Documentation** — produces human-readable specifications, blueprints
   - **Code-generation** — produces compilable/runnable code artifacts
5. Verify each prompt has a valid YAML frontmatter with `name`, `title`, `description`, `tags`, and `trigger`.

**Output:** `inventory.yaml` (or inline inventory section in the manifest)

## Phase 2: Contract Design

**Purpose:** Define the stage graph, dependency edges, and input/output contracts for every generator.

**Steps:**

1. Encode Stage A → Stage B → Stage C linear dependency chain.
2. Encode Stage D as conditional on stack detection + `include-code-generation` flag.
3. Encode Stage E as always-running final consolidation.
4. For each stage, define:
   - Input prerequisites (must exist before stage starts)
   - Expected output artifacts (files + their required sections)
   - Gate criteria (how pass/fail is determined)
5. For each mode (`full`, `quick`, `custom`), map to its stage selection.

**Output:** `contract.yaml` (or inline contract in the runbook)

## Phase 3: Execution

**Purpose:** Run the stages in declared order with gates.

**Sub-phases:**

- 3a: Run Stage A prompts in parallel (technology-stack + folder-structure)
- 3b: Gate A — verify Stage A artifacts exist + pass lint
- 3c: Run Stage B prompts in dependency order (architecture → workflow-analysis → code-exemplars)
- 3d: Gate B — verify Stage B artifacts exist + pass lint + pass dependency trace
- 3e: Run Stage C prompts in parallel (copilot-instructions + readme)
- 3f: Gate C — verify cross-link consistency with Stage A + Stage B outputs
- 3g: Run Stage D prompts (MCP generators) based on detected stack from Stage A
- 3h: Gate D — verify MCP outputs are valid per their language/framework

## Phase 4: Consolidation & Handoff

**Purpose:** Validate all artifacts together, produce the manifest, and decide handoff pass/fail.

**Steps:**

1. Run final consistency gate across ALL generated artifacts.
2. Generate the execution manifest (which stages ran, which prompts, outcomes).
3. Generate the validation report (pass/fail per gate, warnings, remediation items).
4. Decide handoff: PASS (all gates green) or FAIL (any hard failure unresolved).
