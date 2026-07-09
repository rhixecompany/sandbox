---
title: "ADR-0001: Use Bun as the Primary JavaScript/TypeScript Runtime and Package Manager"
status: "Accepted"
date: "2026-07-09"
authors: "Contributors, Automation Engine (projects/Bash), Hermes Agent"
supersedes: ""
superseded_by: ""
---

# ADR-0001: Use Bun as the Primary JavaScript/TypeScript Runtime and Package Manager

## Status

**Accepted** | Proposed | Rejected | Superseded | Deprecated

## Context

The SandBox workspace is a monorepo-style repository hosting 29 subprojects plus root
automation tooling (29 subprojects per `docs/agents-context/architecture.md`), mixing
TypeScript/Bun tooling, Python data scripts, Django web apps, and a multi-language
MCP-server collection. A consistent, fast JS/TS runtime and package manager is required
at the root and for the TypeScript automation toolkit (`projects/Bash/`, which audits,
triages, remediates, and cross-references agent/skill/prompt assets).

A generated prompt body elsewhere in the asset set instructed agents to "always use
pnpm." This conflicted with the repository's actual declarations: `package.json` pins
`"packageManager": "bun@1.3.14"` and the repo ships `bun.lock`. `pnpm` exists on PATH only
incidentally (via nvm4w) and is not referenced by any script. To eliminate toolchain drift
and agent confusion, an explicit, authoritative decision was needed and was encoded in
`AGENTS.md §3` ("Toolchain & Commands (REAL — bun, not pnpm)").

## Decision

Adopt **Bun 1.3.14+** as the single JavaScript/TypeScript runtime, package manager, and
test runner for the root workspace and all TypeScript tooling (notably `projects/Bash/`).
Installation uses `bun install --frozen-lockfile || bun install`; quality gates run via
`bun run typecheck` (`tsc --noEmit`), `bun run lint:strict` (ESLint flat config,
`--max-warnings=0`), `bun run format` (Prettier), and `bun run test` (Vitest). Discourage
and do not introduce `pnpm`, `npm`, or `yarn` for these scopes.

## Consequences

### Positive

- **POS-001**: Single, fast runtime covers install + run + test, cutting toolchain surface and CI setup time.
- **POS-002**: `bun.lock` is committed and `--frozen-lockfile` is enforced, giving reproducible installs across contributors and CI.
- **POS-003**: Alignment with declared repo metadata (`"packageManager": "bun@1.3.14"`), preventing agent/LLM confusion about which package manager to invoke.
- **POS-004**: Native TypeScript execution and built-in test runner (Vitest via Bun) reduce config and dependency overhead for the automation toolkit.

### Negative

- **NEG-001**: Bun's smaller ecosystem and occasional incompatibility with Node-only packages add risk for subprojects that depend on deep Node/npm tooling.
- **NEG-002**: Contributors must have Bun 1.3.14+ installed locally; onboarding diverges from the more common npm/pnpm mental model.
- **NEG-003**: The decision is documented only via `AGENTS.md` prose plus repo metadata, not a prior ADR, so this record retroactively formalizes an already-effective convention.

## Alternatives Considered

### pnpm

- **ALT-001**: **Description**: Fast, disk-efficient npm-compatible package manager with strict node-linker semantics; suggested by a generated prompt body.
- **ALT-002**: **Rejection Reason**: Present on PATH only incidentally (via nvm4w) and referenced by no script or `package.json` field; adopting it would contradict the repo's pinned `packageManager` and `bun.lock`, fracturing the toolchain.

### npm

- **ALT-003**: **Description**: Default Node.js package manager, universally available.
- **ALT-004**: **Rejection Reason**: Slower installs, no bundled runtime/test runner, and inconsistent lockfile behavior versus the already-committed `bun.lock`; does not match the repo's Bun-first setup.

### Yarn (Classic / Berry)

- **ALT-005**: **Description**: Feature-rich package manager with workspaces and Plug'n'Play support.
- **ALT-006**: **Rejection Reason**: Additional config surface (`yarn.lock`, `.yarnrc`) and no runtime benefit over Bun for the automation toolkit; not used anywhere in the workspace.

## Implementation Notes

- **IMP-001**: Root `package.json` already declares `"packageManager": "bun@1.3.14"` and ships `bun.lock`; keep these as the source of truth for the Bun version.
- **IMP-002**: Enforce in CI and agent guidance: run `bun install --frozen-lockfile` then the `typecheck` / `lint:strict` / `test` gates before merge; escalate any pnpm/npm/yarn invocation as a toolchain violation.
- **IMP-003**: Success criteria — every TypeScript subproject in scope installs and passes gates exclusively via Bun, with zero `pnpm-lock.yaml` / `package-lock.json` / `yarn.lock` artifacts at root.

## References

- **REF-001**: `AGENTS.md` §3 "Toolchain & Commands (REAL — bun, not pnpm)" — authoritative toolchain statement.
- **REF-002**: `package.json` — `"packageManager": "bun@1.3.14"`, `@types/bun`, no root scripts.
- **REF-003**: `docs/agents-context/tech-stack.md` and `docs/agents-context/architecture.md` — root runtime and subproject stack inventory.
