# Phase 1 - Skills Audit

Command run:
`hermes skills audit`

CLI validation:
`hermes skills --help` confirms that `audit` is a supported subcommand.

Captured evidence:
- Audit completed successfully with exit code 0.
- Audited 102 skills.
- Output contained 49 `Decision: BLOCKED` lines.
- Output contained 34 `Decision: ALLOWED` lines.
- Output contained 19 `Warning:` lines.
- Output contained 40 `CRITICAL` findings.

High-risk findings surfaced in the audit:
- `agentmail` — dangerous verdict; persistence issue around
  `~/.hermes/config.yaml`.
- `antigravity-cli` — dangerous verdict; supply-chain download risk.
- `axolotl` — dangerous verdict; supply-chain risk from install/bootstrap
  steps.
- `canvas` — dangerous verdict; API token exfiltration patterns.
- `darwinian-evolver` — dangerous verdict; token exfiltration and
  supply-chain risks.
- `fastmcp` — dangerous verdict; persistence and API token exfiltration.
- `fitness-nutrition` — dangerous verdict; API key handling and exfiltration
  risk.
- `gitnexus-explorer` — dangerous verdict; persistence, network, and
  privilege-escalation patterns.
- `here-now` — dangerous verdict; API key exfiltration.
- `honcho` — dangerous verdict; persistence concerns.
- `accelerate` — caution verdict; exfiltration and supply-chain warnings.
- `whisper` — caution verdict; privilege-escalation and install warnings.

Other notable issues:
- Multiple path-missing warnings were reported for skills such as
  `3-statement-model`, `adversarial-ux-test`, `dcf-model`,
  `docker-management`, `dspy`, `trl-fine-tuning`, `grok`, and
  `hermes-s6-container-supervision`.
- Many findings were classified as supply-chain, exfiltration, persistence,
  network, or privilege-escalation risks.

Review note:
- All evidence needed for review is now contained in this file itself.
