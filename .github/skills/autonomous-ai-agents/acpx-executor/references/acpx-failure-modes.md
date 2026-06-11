# ACPX Failure Modes — Known Signatures

> Session-specific failure transcripts from May/Jun 2026. Each entry includes
> exact error text and the root cause so future agents can match and bypass
> without retrying a known-dead path.

## 1. Qwen — Deep file scan timeout (60s)

**Trigger**: Agent asked to scan a directory with 1000+ files (e.g., `projects/comicwise/`)

**Observed output**:
```
[tool] Glob: '**/*' in path '.../comicwise' (completed)
  Found 1028 matching file(s)
...
Timed out after 60000ms
hint: increase `--timeout <seconds>` for long-running prompts, or check whether the agent/provider is stalled.
```

**Root cause**: Qwen's ACPX handler globs all files before reading any. On a directory with 1000+ files, glob + first reads exceed the 60s timeout. Even increasing to 120s may not help if the agent proceeds to read dozens of files.

**Bypass**: Don't use ACPX agents for deep codebase analysis. Use `search_files` + `read_file` directly, or write a Python script with `os.walk`.

---

## 1b. Qwen — Architecture/cross-repo reasoning timeout (180s+)

**Trigger**: Agent asked to analyze multiple repositories (3+ projects) and synthesize an architecture plan, migration order, or consolidated directory layout.

**Observed output**:
```
[tool] Glob: '**/*' in path '.../project-a' (completed)
[tool] Glob: '**/*' in path '.../project-b' (completed)
[tool] Glob: '**/*' in path '.../project-c' (completed)
... (architecture reasoning starts) ...
Timed out after 180000ms
hint: increase `--timeout <seconds>` for long-running prompts, or check whether the agent/provider is stalled.
```

**Root cause**: Two issues compound. First, the agent globs all files across multiple projects before reading any content (same as mode 1a). Second, even after files are read, the **reasoning depth** for architecture-level synthesis (comparing 3+ project structures, proposing merge strategies, writing a unified directory tree) exceeds the timeout window. The output is truncated mid-plan — sections after the timeout point are lost silently.

**Bypass**: This is a compound failure — both file globbing AND reasoning depth contribute.
1. Break the prompt into smaller focused sub-prompts: one per source project for analysis, then a final synthesis prompt with the analysis results.
2. Alternatively, do the file analysis yourself with `search_files` + `read_file`, then feed the findings into a focused synthesis prompt.
3. When using ACPX for multi-repo architecture, verify the full output was returned — check for truncation signals like incomplete sentences or abruptly cut sections.

Important: unlike mode 1a (pure file I/O), increasing timeout to 300s+ MAY help for the reasoning component, but the file-globbing overhead per-project still applies. The reliable fix is prompt decomposition.

---

## 2. OpenCode — Cost-guard JSON parse error

**Trigger**: Provider enforce spend limits with non-JSON status lines injected into NDJSON stream

**Observed output**:
```
Failed to parse JSON message: [cost-guard] Active — limit: $20.0000 | warn at: 80% | mode: warn
SyntaxError: Unexpected token 'c', "[cost-guard"...
    at JSON.parse (<anonymous>)
    at enqueueNdJsonLine (file:///.../acpx/dist/live-checkpoint-*.js:3391:24)
```

**Root cause**: The ACPX binary expects clean NDJSON (one JSON object per line). The cost-guard status line `[cost-guard] Active — limit: ...` is not JSON, which breaks the NDJSON parser. This is a protocol-level incompatibility between the `acpx` binary and the specific provider's cost-guard implementation.

**Bypass**: No recovery from agent side. Fall back to another provider (qwen/copilot) or switch to direct implementation. If this happens mid-session, do not retry opencode.

---

## 3. Copilot — Wrong path resolution

**Trigger**: Copilot finds the wrong instance of a project (e.g., a docs copy instead of the real project)

**Observed output**:
```
REPO=C:\Users\Alexa\Desktop\SandBox\docs\project-docs\rhixecompany-comics
---LOCAL_BRANCHES---
master 26819c5
---COMMIT_PRODUCTION---
fatal: Needed a single revision
```

**Root cause**: The Copilot ACPX agent uses `Get-ChildItem -Recurse -Filter` (PowerShell) to locate the project, which returns the first match alphabetically. A docs copy at `SandBox/docs/project-docs/rhixecompany-comics` resolves before the actual project at `Sandbox/projects/rhixecompany-comics`. Drive letter casing (`SandBox` vs `Sandbox`) can also cause mismatches.

**Bypass**: Always specify the exact absolute path in prompts. Don't rely on the agent's auto-discovery. Verify the path the agent resolved before trusting its branch/commit findings.

---

## 4. Copilot — Multi-repo dispatch timeout (60s)

**Trigger**: Copilot CLI given a prompt referencing 3+ repos or projects for analysis

**Observed output**:
```
% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
 38 17804   38  6891    0     0   166k      0 --:--:-- --:--:-- --:--:--  165k
curl: (28) Operation timed out after 60000 milliseconds
```

**Root cause**: Copilot CLI's `-p` mode scans all files matching the prompt context in the background before any reasoning begins. For prompts touching multiple repositories (each with hundreds of files), the cumulative I/O scan time exceeds the 60s curl timeout before a single line of analysis is produced.

**Bypass**: Copilot CLI is unsuitable for multi-repo tasks. Use qwen with 300s+ timeout, or break into single-repo prompts. Skip copilot entirely when the prompt references more than one project directory.

---

## 5. Qwen — Architecture reasoning interrupted (SIGINT/exit 130)

**Trigger**: Qwen Code analyzing multi-project architecture, interrupted before completion

**Observed output**:
```
Timed out after 180000ms
hint: increase `--timeout <seconds>` for long-running prompts
exit code 130
```

**Root cause**: Same as mode 1b (compound file-globbing + reasoning depth), but the agent was manually interrupted (SIGINT) vs hitting the timeout. The output is valid but truncated mid-stream — any sections planned after the interruption point are lost.

**Bypass**: Same as 1b — prompt decomposition. For multi-repo architecture, use separate prompts per repo (120s each) then a final synthesis prompt. Verify the agent's output has a natural conclusion before accepting it.
