# Rationale for Hermes diagnostics and profile consistency

## Context

Feature 9 in `docs/scope/scope.md` asks for a full repository and Hermes diagnostic sweep, evidence based debugging, supported repairs, and consistency checks for every profile returned by `hermes profile list`. The current run is architecture only. It must not execute repair commands or mutate Hermes profile configuration.

The workspace is a Windows repository using Git Bash through Hermes. The repository has a root `package.json` with a `check` script. The repository already has many GitHub Actions workflows and shared agent guidance, so the future implementation must remain narrow and must not rewrite unrelated CI or context files.

## Evidence collected

| Evidence | Result |
|---|---|
| `git fetch --quiet` | Exit 0 |
| Base branch preflight | `main` was not available locally, so `master` was selected. The remote comparison returned `behind=unknown`, so freshness is unresolved rather than guessed |
| Working tree | `docs/scope/scope.md` was already modified before this specification was written. The current repository path is `C:\Users\Alexa\playgrounds\SandBox` |
| Hermes home | The resolved runtime home for this session is `C:\Users\Alexa\AppData\Local\hermes`. Only path and command metadata are retained |
| `hermes profile list` | Exit 0. It listed `default` as running, many stopped profiles, alias values for most named profiles, and warnings that many profiles share the default Telegram credential |
| Credential evidence | No credential value was copied into this rationale. The warning text names the conflict only |
| Scope | Feature 9 is planned, GA, and now receives this proposed specification |
| Architect support files | `internal/design-conversation.md`, `agent-prompt.md`, and `spec-template.md` were present and read. `agent-modes/cross-cutting.md` and `internal/after-subagent.md` were not present in the installed architect skill directory. Their absence is recorded, not filled with invented content |

The live profile output showed shared Telegram credential warnings for `adminbot`, `analyst`, `architect`, `code-architect`, `creative`, `creative-director`, `cto`, `designer`, `dev`, `exec-assistant`, `ops`, `patient-tutor`, `pm`, `research-analyst`, `security`, `skills`, and `tutor`. The specification intentionally treats those warnings as approval gates and does not propose automatic credential removal or creation.

The current process working directory is `C:\Users\Alexa\playgrounds\SandBox`, while `AGENTS.md` contains older references to `C:\Users\Alexa\Desktop\SandBox` and a malformed integration table. This is recorded as a context prerequisite rather than silently repaired during architecture. The future implementation must reconcile repository context through the repository synchronization workflow before starting `HERMES-001`; the live process path remains authoritative for this specification pass.

The source contract follows the installed Hermes profile guidance. `hermes profile list` is the inventory and primary alias authority, `hermes profile show <name>` is the optional detail source, and read only wrapper directory metadata supplements aliases when the live list is incomplete. The implementation must not invoke `hermes profile alias <name>` during diagnosis because that command creates a wrapper. `hermes config check` plus an allowlisted projection of `hermes config show` provide non secret routing and configuration evidence. The default profile maps to the Hermes home root. Non default profiles map to `profiles/<name>`, with documented identity and memory files checked by metadata only. Unsupported commands or missing fields produce an explicit unavailable or not collected finding rather than an inferred empty result.

## Options considered

### Parallel command runner

This would reduce wall time, but concurrent commands could interleave log output, compete for shared Hermes state, and make a repair cause difficult to attribute. It was rejected for the first tracer bullet.

### Stop on first failure

This would simplify control flow, but it would hide independent failures and would not satisfy the requested full diagnostic sweep. It was rejected.

### Sequential durable runner

This records each command in a fixed order, continues after failures, preserves per command exit status, and makes the report useful even when Hermes is partially unhealthy. It was selected.

### Automatic shared credential repair

Removing a credential reference or assigning a new bot can disconnect a profile or change message routing. It also requires credential ownership and external setup that this run does not have. It was rejected.

### Hermes CLI first repair

The existing user preference and configuration guidance require `hermes config set` for configuration changes when supported. A dry run and explicit apply boundary reduce accidental mutation. This was selected. Direct file edits are not part of the automated repair path; an emergency manual edit remains outside this runner and cannot bypass its hard deny policy.

## Design answers

The design conversation confirmed these decisions:

1. The current run creates the Hermes specification only.
2. Future execution uses a durable sequential diagnostic runner.
3. The command runner continues after failures and records platform limits.
4. Profile consistency covers live inventory, directories, aliases, routing, and non secret configuration references.
5. Shared Telegram credential warnings are reported and require approval, with no automatic credential mutation.
6. Repair uses Hermes CLI commands with a dry run and explicit apply boundary.

## Documentation sources

* Hermes Agent documentation, `https://hermes-agent.nousresearch.com/docs`
* Installed `hermes-diagnostic-repair` skill, which defines the command sweep and JSON plus Markdown reporting pattern
* Installed `hermes-system-maintenance` skill and `references/diagnostic-commands.md`, which define resource, configuration, and repair caution patterns
* Installed `log-analysis-and-triage` skill, which defines log categories and redaction review needs
* Installed `hermes-profiles` skill, which defines profile inventory and `hermes config check` verification
* Installed `systematic-debugging` skill, which requires evidence and root cause investigation before fixes

## Verification boundary

This architecture pass verified specification files and recorded current read only evidence. The formal report schema and acceptance matrix are in `verify.md`, with golden canonicalization vectors and a test mapping for AC-1 through AC-20. It did not run `bun run check`, `hermes doctor`, `hermes doctor --fix`, Hermes log commands, or profile repair commands because the user selected specification only for Hermes in this run. The future implementation must record `hermes doctor --fix` as `approval_required` and `not_run` during diagnosis, with a null exit code, and may execute it only through an explicit approved apply plan.
