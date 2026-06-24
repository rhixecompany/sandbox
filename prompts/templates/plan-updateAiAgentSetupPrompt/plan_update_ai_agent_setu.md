# Plan: Update AI Agent Setup Prompt for Comicbook Project

> Extracted from `plan-updateAiAgentSetupPrompt.prompt.md`.

## Plan: Update AI Agent Setup Prompt for Comicbook Project

**TL;DR:**  
This plan will produce a comprehensive `.github/prompts/setup.prompt.md` for AI agents, merging all critical knowledge from project markdowns and documentation. It will include actionable instructions, deeper code samples, and workflow explanations, focusing on architecture, developer workflows, unique conventions, integration points, and real code patterns.

---

**Steps**

1. **Documentation Collection**
   - List and read all files in `.references/comicwise/**/*`, `.references/comicr/**/*`,`.references/bookwise/**/*`, `.references/comicwise-master/**/*`, `.github/prompts/*.md`, `docs/*.md`, `.github/copilot-instructions.md`, and `README.md`.
   - Summarize key patterns, workflows, conventions, steps, phase, task, subtask.

2. **Architecture Analysis**
   - Map major components: Next.js App Router, Drizzle ORM, modular auth, UI primitives.
   - Document service boundaries, data flows, and rationale for structure (e.g., why modular auth, why Drizzle).

3. **Developer Workflow Extraction**
   - Detail build, lint, and debugging commands (`pnpm lint:fix`, `pnpm build`).
   - Document VSCode optimization, batch fix documentation, error triage, and commit practices.

4. **Project-Specific Patterns**
   - Highlight unique conventions: React Suspense import, error handling with `cause`, strict JSON for VSCode, modular auth callbacks.
   - Reference key files and directories for each pattern.

5. **Integration Points & Dependencies**
   - Map external dependencies (NextAuth, Drizzle, Tailwind, ESLint plugins).
   - Document cross-component communication (auth provider integration, DB access).

6. **Deeper Code Samples**
   - Provide full code samples for:
     - Credentials provider `authorize` function.
     - DB fetch and password verification functions.
     - Auth API route handler.
     - VSCode settings and extensions.
   - Ensure samples are copy-paste ready and reference real project files.

7. **Merge & Update Setup Prompt**
   - Show me the updated prompt and output the updated prompt to `.github/prompts/setup.prompt.md` only after user confirmation.
   - If `.github/prompts/setup.prompt.md` exists, merge new content intelligently, preserving valuable sections key patterns, workflows, conventions, steps, phase, task, subtask and updating outdated ones.
   - Structure the prompt with clear markdown sections, actionable steps, and feedback requests.

8. **Feedback & Iteration**
   - Ask the user for feedback on unclear or incomplete sections, key patterns, workflows, conventions, steps, phase, task, subtask.
   - Iterate and expand sections, key patterns, workflows, conventions, steps, phase, task, subtask as requested, focusing on deeper workflow explanations and code samples.

---

**Verification**

- Ensure the updated prompt covers all critical knowledge for immediate agent productivity.
- Confirm all referenced code samples, workflows, key patterns, conventions, steps, phase, task, subtask are accurate and project-specific.
- Validate that the prompt is actionable, scannable, and free of generic advice.

---

**Decisions**

- All code samples will be real, not aspirational.
- Only discoverable patterns and workflows will be documented.
- Feedback will drive further expansion and clarification.

---

**Next Steps:**  
Proceed to execute each step, starting with documentation collection and analysis, then drafting and merging the expanded setup prompt. Request user feedback after initial delivery.
