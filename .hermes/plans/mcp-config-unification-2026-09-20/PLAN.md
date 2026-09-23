# PLAN.md — MCP Configuration Unification & Heavy-to-Lightweight Migration

**Plan ID**: `mcp-config-unification-2026-09-20`
**Goal**: Unify MCP configs across all tools, replace 5 heavy servers, create `.vscode/mcp.json`, delete duplicate `opencode.json`, update Docker prompt.
**Source spec**: `.hermes/specs/mcp-config-unification-2026-09-20/SPEC.md`
**Profile**: default (adminbot for system config changes)
**Status**: Planned → Execution

---

## 1. Rules

- MCP `.github/mcp.json` is the canonical source — all tools reference or sync from it
- Never read/print/commit `.env` contents
- Verify all file operations; preserve `.env` sizes; 0 new `.bak`
- Heavy servers replaced by Hermes native tools, not new MCP servers
- Multi-file-crud-protocol applies (7+ files affected)

---

## 2. Goal

Produce a unified MCP configuration where:

- `.github/mcp.json` is the superset (all servers from both canonical + OpenCode)
- 5 heavy servers removed and replaced with Hermes native tool usage
- `.vscode/mcp.json` created for VS Code parity
- Repo `opencode.json` deleted
- Docker prompt updated to create/verify only + bun+uv

---

## 3. Subgoals

| Subgoal | Description                                                                          |
| ------- | ------------------------------------------------------------------------------------ |
| SG1     | Update `.github/mcp.json` — add 6 OpenCode extras, remove 5 heavy servers            |
| SG2     | Create `.vscode/mcp.json` — copy of updated `.github/mcp.json`                       |
| SG3     | Delete `~/Desktop/SandBox/opencode.json`                                             |
| SG4     | Update `~/.opencode/opencode.json` — align shared servers, remove heavy ones         |
| SG5     | Update `.github/prompts/ci-cd/all-repo-docker-setup/all-repo-docker-setup.prompt.md` |
| SG6     | Update `.hermes.md` and `config.yaml` for MCP changes                                |
| SG7     | Verify all changes pass gates                                                        |

---

## 4. Steps

1. Read current `.github/mcp.json` and `~/.opencode/opencode.json` for exact content
2. Construct updated `.github/mcp.json` with additions + removals
3. Write `.vscode/mcp.json`
4. Delete repo `opencode.json`
5. Update `~/.opencode/opencode.json`
6. Update Docker prompt
7. Update `.hermes.md` and `config.yaml`
8. Verify all gates

---

## 5. Todos

- [ ] SG1: `.github/mcp.json` updated (add 6, remove 5 heavy)
- [ ] SG2: `.vscode/mcp.json` created
- [ ] SG3: Repo `opencode.json` deleted
- [ ] SG4: `~/.opencode/opencode.json` aligned
- [ ] SG5: Docker prompt updated
- [ ] SG6: `.hermes.md` + `config.yaml` updated
- [ ] SG7: All verification gates pass

---

## 6. Phases

### Phase 1: Prepare (Sequential)

**Entry gate**: Spec written and verified
**Tasks**:

- T1: Read current configs (already done — inventory exists)
- T2: Construct new `.github/mcp.json` content

### Phase 2: Apply Changes (Parallel within phase, sequential across)

**Entry gate**: Phase 1 complete
**Tasks**:

- T3: Write updated `.github/mcp.json`
- T4: Write `.vscode/mcp.json`
- T5: Delete repo `opencode.json`
- T6: Update `~/.opencode/opencode.json`
- T7: Update Docker prompt
- T8: Update `.hermes.md` + `config.yaml`

### Phase 3: Verify (Sequential)

**Entry gate**: Phase 2 complete
**Tasks**:

- T9: Verify `.github/mcp.json` JSON validity + server count
- T10: Verify `.vscode/mcp.json` matches `.github/mcp.json`
- T11: Verify repo `opencode.json` deleted
- T12: Verify Docker prompt changes
- T13: Verify `.env` sizes unchanged, 0 `.bak`

---

## 7. Tasks

### TASK-001: Update `.github/mcp.json`

- **Owner**: default
- **Path**: `C:/Users/Alexa/Desktop/SandBox/.github/mcp.json`
- **Action**: Add 6 servers (django, docs, evals, postgres, pytest, time) using `npx.cmd`; remove 5 heavy (playwright, code-sandbox, smithery, mcp-docker, mindstudio)
- **Output**: Updated `.github/mcp.json` with 23 servers (22 - 5 + 6 = 23)
- **Acceptance**: JSON valid; 23 servers; no heavy servers; all 6 extras present
- **Rollback**: Restore from git

### TASK-002: Create `.vscode/mcp.json`

- **Owner**: default
- **Path**: `C:/Users/Alexa/Desktop/SandBox/.vscode/mcp.json`
- **Action**: Write same content as updated `.github/mcp.json`
- **Output**: `.vscode/mcp.json`
- **Acceptance**: File exists; content matches `.github/mcp.json`
- **Rollback**: Delete file

### TASK-003: Delete repo `opencode.json`

- **Owner**: default
- **Path**: `C:/Users/Alexa/Desktop/SandBox/opencode.json`
- **Action**: Delete file
- **Output**: File gone
- **Acceptance**: `os.path.exists` returns False
- **Rollback**: Restore from git

### TASK-004: Update `~/.opencode/opencode.json`

- **Owner**: default
- **Path**: `C:/Users/Alexa/.opencode/opencode.json`
- **Action**: Remove 5 heavy servers; align shared servers with `.github/mcp.json`; keep OpenCode-specific entries that are NOT heavy and NOT in `.github/mcp.json`
- **Output**: Updated `~/.opencode/opencode.json`
- **Acceptance**: No heavy servers; shared servers match `.github/mcp.json`
- **Rollback**: Restore from git (if tracked) or manual restore

### TASK-005: Update Docker prompt

- **Owner**: default
- **Path**: `C:/Users/Alexa/Desktop/SandBox/.github/prompts/ci-cd/all-repo-docker-setup/all-repo-docker-setup.prompt.md`
- **Action**: Remove clone/build/scan/prune subgoals; keep only Dockerfile create/verify; add bun+uv setup subgoal
- **Output**: Updated prompt
- **Acceptance**: No clone/build/scan/prune instructions; bun+uv subgoal present
- **Rollback**: Restore from git

### TASK-006: Update `.hermes.md` + `config.yaml`

- **Owner**: default
- **Path**: `C:/Users/Alexa/Desktop/SandBox/.hermes.md` + `C:/Users/Alexa/Desktop/SandBox/config.yaml`
- **Action**: Update MCP server references to reflect new state
- **Output**: Updated files
- **Acceptance**: References match new MCP state
- **Rollback**: Restore from git

### TASK-007: Verification

- **Owner**: default
- **Action**: Run all gate checks
- **Output**: Verification evidence
- **Acceptance**: All gates pass

---

## 8. Subtasks

### TASK-001 Subtasks

- 001a: Construct JSON with additions
- 001b: Remove heavy server entries
- 001c: Write file

### TASK-005 Subtasks

- 005a: Remove clone subgoal
- 005b: Remove build subgoal
- 005c: Remove secure subgoal
- 005d: Remove cleanup plan subgoal
- 005e: Remove prune subgoal
- 005f: Add bun+uv setup subgoal
- 005g: Update verification section

---

## 9. Gates

| Gate | Condition                               | Verification                                                                    |
| ---- | --------------------------------------- | ------------------------------------------------------------------------------- |
| G1   | `.github/mcp.json` is valid JSON        | `python -c "import json; json.load(open('.github/mcp.json'))"` exit 0           |
| G2   | 23 servers in `.github/mcp.json`        | Count `mcpServers` keys = 23                                                    |
| G3   | No heavy servers in `.github/mcp.json`  | grep for playwright, code-sandbox, smithery, mcp-docker, mindstudio → 0 matches |
| G4   | All 6 extras in `.github/mcp.json`      | grep for django, docs, evals, postgres, pytest, time → all present              |
| G5   | `.vscode/mcp.json` exists and matches   | `diff .github/mcp.json .vscode/mcp.json` → no differences                       |
| G6   | Repo `opencode.json` deleted            | `test -f opencode.json` → exit 1                                                |
| G7   | Docker prompt no clone/build/scan/prune | grep → 0 matches for those terms                                                |
| G8   | Docker prompt has bun+uv subgoal        | grep → matches for bun and uv                                                   |
| G9   | `.env` sizes unchanged                  | `os.path.getsize` matches: CWD 5274 B, Hermes 30269 B                           |
| G10  | 0 new `.bak` files                      | Find `.bak` → 0 new since session start                                         |

---

## 10. Checklists

### Pre-execution

- [ ] Spec created and verified
- [ ] All clarifying questions answered
- [ ] `.env` sizes recorded (CWD: 5274 B, Hermes: 30269 B)
- [ ] Git clean state verified

### Post-execution

- [ ] All gates pass
- [ ] `.env` sizes unchanged
- [ ] 0 new `.bak` files
- [ ] No `.env` contents exposed
- [ ] Identity/routing rules preserved

---

## 11. Actions

| Action                             | Task     | Command/Tool                                      |
| ---------------------------------- | -------- | ------------------------------------------------- |
| Write `.github/mcp.json`           | TASK-001 | `write_file`                                      |
| Write `.vscode/mcp.json`           | TASK-002 | `write_file`                                      |
| Delete `opencode.json`             | TASK-003 | `terminal rm` or `write_file` with empty + delete |
| Write `~/.opencode/opencode.json`  | TASK-004 | `write_file`                                      |
| Patch Docker prompt                | TASK-005 | `patch`                                           |
| Patch `.hermes.md` + `config.yaml` | TASK-006 | `patch`                                           |
| Verify gates                       | TASK-007 | `terminal` + `read_file`                          |

---

## 12. Needed Specs

- `.hermes/specs/mcp-config-unification-2026-09-20/SPEC.md` (created)

---

## 13. Dependencies and Risks

| Dependency                                     | Risk                          | Mitigation                                         |
| ---------------------------------------------- | ----------------------------- | -------------------------------------------------- |
| `.github/mcp.json` syntax                      | Invalid JSON breaks all tools | Validate with `json.load` before writing           |
| `~/.opencode/opencode.json` not tracked by git | Can't git-restore             | Back up before writing                             |
| Docker prompt frontmatter                      | Breaking YAML structure       | Read full file first; use `patch` not `write_file` |
| `.hermes.md` large file (6463 B)               | Patch context mismatch        | Read exact lines before patching                   |

---

## 14. Verification Evidence

To be populated during Phase 3 execution.

---

## 15. Rollback and Completion

- **Rollback**: All changes are git-restorable except `~/.opencode/opencode.json` (not in repo). Back it up before modifying.
- **Completion**: All 10 gates pass + `.env` sizes verified + 0 `.bak` + verification evidence recorded.
