---
status: completed
---

# Oh My OpenAgent / Oh My Hermes — Specification

**Version** 1.0 | **Date** 2026-08-05 | **Owner** OWL

## 1. Purpose

Provision and verify the oh-my-openagent (OMO) multi-agent orchestration framework and the Oh My Hermes workflow layer on top of OpenCode CLI + Hermes Agent, following the official 2026 installation guide.

## 2. Scope

**In scope:** OpenCode CLI prereq, OMO install, agent model mapping (sisyphus/hephaestus/oracle/librarian/explore/atlas/prometheus), provider auth, non-interactive env flags, Hermes plugin wiring, doctor + smoke verification.

**Out of scope:** purchasing/resolving LLM subscriptions; CI deployment; detailed per-agent permission tuning beyond defaults.

## 3. Functional Requirements

| ID   | Requirement                                                                                                |
| ---- | ---------------------------------------------------------------------------------------------------------- |
| FR-1 | OpenCode CLI present and ≥ 1.4.0.                                                                          |
| FR-2 | `oh-my-openagent` resolvable via `bunx` (package 4.x).                                                     |
| FR-3 | Config file `~/.config/opencode/oh-my-openagent.jsonc` present; agents map to models.                      |
| FR-4 | At least one provider authed in `opencode auth list`.                                                      |
| FR-5 | Non-interactive flags `OPENCODE_DISABLE_EMBEDDED_WEB_UI/SHARE/AUTOUPDATE=true` set for Hermes-driven runs. |
| FR-6 | Hermes opensource plugin dir present (or documented fallback to built-in agent).                           |
| FR-7 | `opencode agents` lists ≥ 1 agent; `omo_doctor.py` reports PASS.                                           |
| FR-8 | No secrets printed by any artifact.                                                                        |

## 4. Non-Functional

- NFR-1: Read-only doctor; no destructive side effects.
- NFR-2: Windows/MSYS safe (uses `opencode.cmd` path).
- NFR-3: Reusable across OpenCode/Claude Code/Codex platforms (OMO is provider-agnostic).

## 5. Acceptance Criteria

- AC-1: `python scripts/omo_doctor.py` exits 0 (no blocking failures).
- AC-2: `bunx oh-my-openagent doctor` reports System OK.
- AC-3: `opencode agents` lists agents.
- AC-4: All artifacts (script/skill/plan/spec/prompt) present and validated on disk.

## 6. Result (Executed)

OMO 4.19.4 already installed; opencode 1.18.13; config present; auth providers present; env flags set. `omo_doctor.py` + `bunx doctor` pass. Codex (openai.chatgpt) + opencode ext + hermes-chat installed in VS Code.
