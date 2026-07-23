# Output Format

> Extracted from `suggest-awesome-github-copilot-instructions.prompt.md`.

## Output Format

Display analysis results in structured table comparing awesome-copilot instructions with existing repository instructions:

| Awesome-Copilot Instruction | Description | Already Installed | Similar Local Instruction | Suggestion Rationale |
| --- | --- | --- | --- | --- |
| [blazor.instructions.md](https://github.com/github/awesome-copilot/blob/main/instructions/blazor.instructions.md) | Blazor development guidelines | ✅ Yes | blazor.instructions.md | Already covered by existing Blazor instructions |
| [reactjs.instructions.md](https://github.com/github/awesome-copilot/blob/main/instructions/reactjs.instructions.md) | ReactJS development standards | ❌ No | None | Would enhance React development with established patterns |
| [java.instructions.md](https://github.com/github/awesome-copilot/blob/main/instructions/java.instructions.md) | Java development best practices | ⚠️ Outdated | java.instructions.md | applyTo pattern differs: remote uses `'**/*.java'` vs local `'*.java'` - Update recommended |
