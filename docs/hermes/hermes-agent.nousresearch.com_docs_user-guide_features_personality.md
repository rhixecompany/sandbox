# Source: <https://hermes-agent.nousresearch.com/docs/user-guide/features/personality>

# Personality & SOUL.md — Hermes Agent (Summary)

Key purpose: SOUL.md is the _primary identity_ of a Hermes instance — the durable, per-user/per-instance system-prompt identity. Edit it to change Hermes' default persona.

---

## Key excerpts (preserved verbatim)

- File/location examples and usage:
  - `SOUL.md`
  - `HERMES_HOME`
  - `/personality`
  - `~/AppData/Local/hermes/SOUL.md`
  - `$HERMES_HOME/SOUL.md`
  - `skip_context_files`
  - `AGENTS.md`
  - `agent.personalities`
  - `~/AppData/Local/hermes/config.yaml`

- Fallback identity (used if SOUL.md is empty/unreadable or `skip_context_files` is set):
  - "You are Hermes Agent, an intelligent AI assistant created by Nous Research..."

- Example SOUL.md content (complete, preserved):

  ```
  # Personality

  You are a pragmatic senior engineer with strong taste.
  You optimize for truth, clarity, and usefulness over politeness theater.

  ## Style
  - Be direct without being cold
  - Prefer substance over filler
  - Push back when something is a bad idea
  - Admit uncertainty plainly
  - Keep explanations compact unless depth is useful

  ## What to avoid
  - Sycophancy
  - Hype language
  - Repeating the user's framing if it's wrong
  - Overexplaining obvious things

  ## Technical posture
  - Prefer simple systems over clever systems
  - Care about operational reality, not idealized architecture
  - Treat edge cases as part of the design, not cleanup
  ```

- Config YAML example for custom personalities:

  ```
  ~/AppData/Local/hermes/config.yaml
  agent.personalities
  agent:
   personalities:
   codereviewer: >
   You are a meticulous code reviewer. Identify bugs, security issues,
   performance concerns, and unclear design choices. Be precise and constructive.
  ```

- Commands (CLI / messaging) to switch personalities:
  - CLI examples:

    ```
    /personality
    /personality concise
    /personality technical
    ```

  - Messaging example:

    ```
    /personality teacher
    ```

---

## Core facts & actionable details

- Location & default seeding
  - Hermes seeds a default `SOUL.md` automatically at:
    - `~/AppData/Local/hermes/SOUL.md` (default)
    - If you run Hermes with a custom home directory: `$HERMES_HOME/SOUL.md`
  - This makes SOUL.md a true _per-user / per-instance_ personality (not per-project).

- Where to edit
  - Most users: edit `~/AppData/Local/hermes/SOUL.md`
  - Custom home: edit `$HERMES_HOME/SOUL.md`

- Purpose & content guidance
  - Use SOUL.md for _durable voice and personality guidance_ (tone, long-lived role, style preferences).
  - Avoid embedding task-specific instructions, step-by-step workflows, or multi-agent orchestration in SOUL.md — those belong in `AGENTS.md`.
  - Keep SOUL.md focused on persona/voice rather than meta-instructions or prompt hacks.

- What Hermes injects into the prompt
  - `SOUL.md` content is inserted directly into _slot #1_ of the system prompt (the agent identity position).
  - _No wrapper language_ is added around the file content.
  - If SOUL.md is empty, whitespace-only, or unreadable, Hermes falls back to the built-in default identity (see quote above). The fallback also applies when `skip_context_files` is set (e.g., subagent/delegation contexts).

- Security scanning
  - `SOUL.md` is scanned like other context-bearing files for prompt-injection patterns before inclusion.
  - Keep SOUL.md focused and avoid trying to smuggle unusual meta-instructions.

- SOUL.md vs AGENTS.md (important distinction)
  - SOUL.md = durable global identity/personality.
  - AGENTS.md = agent definitions and task-specific instructions (per-agent behavior).
  - Useful rule: persona/voice → SOUL.md; task/role/behaviors → AGENTS.md.

- SOUL.md vs /personality
  - `SOUL.md` = persistent default personality.
  - `/personality` = \_session-level overlay_pecific instructions (per-agent behavior).
  - Useful rule: persona/voice → SOUL.md; task/role/behaviors → AGENTS.md.

- SOUL.md vs /personality
  - `SOUL.md` = persistent default personality.
  - `/personality` = _session-level overlay_ that changes or supplements the current system prompt for that session only.
  - Examples: `/personality teacher`, `/personality creative`
  - Session overlays are convenient but the global `SOUL.md` remains the persistent baseline unless the overlay meaningfully replaces it.

- Built-in personalities (switchable with `/personality`)
  - Names and short descriptions:
    - helpful — Friendly, general-purpose assistant
    - concise — Brief, to-the-point responses
    - technical — Detailed, accurate technical expert
    - creative — Innovative, outside-the-box thinking
    - teacher — Patient educator with clear examples
    - kawaii — Cute expressions, sparkles, and enthusiasm ★
    - catgirl — Neko-chan with cat-like expressions, nya~
    - pirate — Captain Hermes, tech-savvy buccaneer
    - shakespeare — Bardic prose with dramatic flair
    - surfer — Totally chill bro vibes
    - noir — Hard-boiled detective narration
    - uwu — Maximum cute with uwu-speak
    - philosopher — Deep contemplation on every query
    - hype — MAXIMUM ENERGY AND ENTHUSIASM!!!

- Custom named personalities in config
  - Define under `agent.personalities` in `~/AppData/Local/hermes/config.yaml`.
  - Switch

[... summary truncated for context management ...]
