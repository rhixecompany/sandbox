Session notes: 2026-05-26

- Active model switch observed: claude-sonnet-4.5 -> gpt-5-mini via GitHub Copilot. Update USER.md and MEMORY.md to reflect model change.
- Tool-limit workaround: disabled selected MCP servers (docker, docker-gateway, next-devtools) to keep total tools under 128 when using big-pickle. Alternative recommended: prefer execute_code over delegate_task when handling multi-file analysis to avoid loading many subagent tools.
- Created Hermes profiles: code-architect, research-analyst, exec-assistant, patient-tutor, creative-director. Each includes SOUL.md (local profiles). Documented in MEMORY.md.
- Recent skills created: hermes-complete-setup (umbrella), hermes-configuration-verification (fast-path).
- Files updated in session:
  - C:\Users\Alexa\AppData\Local\hermes\memories\USER.md (normalized fields, added active model)
  - C:\Users\Alexa\AppData\Local\hermes\memories\MEMORY.md (summarized environment & tooling notes)

Notes to future agents:
- When editing memory files, prefer explicit field-format (Name:, OS:, Editor/IDE:, Shell preference:, Active model:). Do not leave model names stale.
- When the user expresses a preference about local commands (PowerShell vs git-bash), add a one-line PowerShell equivalent under the Quick Commands section of reports.
