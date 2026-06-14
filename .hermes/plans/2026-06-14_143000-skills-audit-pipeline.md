# Plan: Skills Audit, Debug, Fix, Enhance & Judge Pipeline

**Date:** 2026-06-14
**Profile:** code-architect (recommended for this task)
**Mode:** Execution plan — ready to run

---

## Goal

Execute a complete skills quality pipeline on 191 local skills (from `hermes skills list --source local`):
1. **Inventory** — ✅ Done: Saved to `skills_inventory_20260614_143500.log`
2. **Batch Judge** — Run `skill-judge` on all 191 skills in batches of 7 (28 batches)
3. **Remediate** — Patch/fix failures via `skill_manage(action='patch')`
4. **Report** — Document results in `skills_audit_final_report.md`

---

## Inventory Log (Complete)

**File:** `skills_inventory_20260614_143500.log` (191 skills, all enabled)
**Skill names extracted to:** `skill_names_191.txt`

---

## Batch Assignments (28 Batches × 7 Skills = 191)

### Batch 1 (1-7): Core Hermes & Infrastructure
1. Chainlink
2. copilot-cli
3. fine-tuning-with-trl
4. hermes-breakdown
5. hermes-hooks
6. hermes-mcp
7. hermes-skills

### Batch 2 (8-14): Hermes System & AI/ML
8. hermes-system-maintenance
9. huggingface-accelerate
10. ideation
11. inference-sh-cli
12. lambda-labs-gpu-cloud
13. make-repo-contribution
14. modal-serverless-gpu

### Batch 3 (15-21): ML/Profile/Skills
15. peft-fine-tuning
16. profile-maintenance
17. qdrant-vector-search
18. qwen-code
19. simpo-training
20. skill-creator
21. skill-judge

### Batch 4 (22-28): Templates & Architecture
22. stable-diffusion-image-generation
23. template
24. using-git-worktrees
25. validate-memories
26. writing-skills
27. architecture-blueprint-generator
28. folder-structure-blueprint-generator

### Batch 5 (29-35): Architecture & Autonomous Agents
29. technology-stack-blueprint-generator
30. agent-browser
31. agent-governance
32. agentic-eval
33. coding-agents
34. customize-opencode
35. enhance-markdown

### Batch 6 (36-42): Hermes Skills & Creative
36. hermes-skill-library-maintenance
37. template-skill
38. using-superpowers
39. algorithmic-art
40. brand-guidelines
41. canvas-design
42. content-research-writer

### Batch 7 (43-49): Creative & Design
43. excalidraw-diagram-generator
44. frontend-design
45. image-manipulation-image-magick
46. legacy-circuit-mockups
47. marp-slide
48. mermaid-diagrams
49. nano-banana-pro-openrouter

### Batch 8 (50-56): Creative & Development
50. penpot-uiux-design
51. plantuml-ascii
52. theme-factory
53. web-artifacts-builder
54. writing-clearly-and-concisely
55. ai-prompt-engineering-safety-review
56. chrome-devtools

### Batch 9 (57-63): Development Tools
57. context-map
58. convert-plaintext-to-md
59. copilot-cli-quickstart
60. copilot-sdk
61. copilot-usage-metrics
62. create-agentsmd
63. create-implementation-plan

### Batch 10 (64-70): Creation & Generation
64. create-readme
65. create-web-form
66. generate-custom-instructions-from-codebase
67. lsp-setup
68. make-skill-template
69. microsoft-code-reference
70. microsoft-docs

### Batch 11 (71-77): Microsoft & Prompting
71. microsoft-skill-creator
72. prompt-builder
73. prompt-engineering
74. skills
75. suggest-awesome-github-copilot-agents
76. suggest-awesome-github-copilot-instructions
77. update-implementation-plan

### Batch 12 (78-84): VS Code & Workiq
78. vscode-cli
79. vscode-ext-commands
80. vscode-ext-localization
81. vscode-extension-playbook
82. vscode-workspace-configurator
83. workiq-copilot
84. appinsights-instrumentation

### Batch 13 (85-91): DevOps - ASDF to Azure
85. asdf
86. aspire
87. azure-deployment-preflight
88. azure-devops-cli
89. azure-resource-visualizer
90. azure-role-selector
91. azure-static-web-apps

### Batch 14 (92-98): DevOps - Customization to Fabric
92. customization-audit
93. datadog
94. dependabot
95. entra-agent-user
96. fabric-lakehouse
97. git-history-preserving-migration
98. github-actions-efficiency

### Batch 15 (99-105): DevOps - GitHub to Work
99. glab
100. hermes-profiles
101. hermes-setup
102. jira
103. log-analysis-and-triage
104. multi-stage-dockerfile
105. powerbi-modeling

### Batch 16 (106-112): DevOps - Projects to Workspace
106. projects-multi-repo-init-normalize
107. provider-reliability-diagnostics
108. rbac-audit-logging
109. secret-scanning
110. service-integrations
111. session-audit-report
112. snowflake-semanticview

### Batch 17 (113-119): DevOps - Terraform to GitHub
113. terraform-azurerm-set-diff-analyzer
114. webhook-subscriptions
115. windows-maintenance-operations
116. work-on-ticket
117. workspace-audit
118. finishing-a-development-branch
119. gh-cli

### Batch 18 (120-126): GitHub Core
120. git-commit
121. git-helper
122. git-submodule-workflow
123. github
124. github-workflow
125. sponsor-finder
126. mcp-builder

### Batch 19 (127-133): MCP & Media
127. mcp-cli
128. mcp-security-audit
129. native-mcp
130. slack-gif-creator
131. spotify
132. transloadit-media-processing
133. brainstorming

### Batch 20 (134-140): Planning & Productivity
134. plans-and-specs
135. prompt-planning-orchestration
136. prd
137. doc-coauthoring
138. documentation-extraction-and-indexing
139. documentation-writer
140. docx

### Batch 21 (141-147): Productivity - Files to Linear
141. file-organizer
142. finnish-humanizer
143. internal-comms
144. linear
145. markdown-to-html
146. meeting-insights-analyzer
147. meeting-minutes

### Batch 22 (148-154): Productivity - PDF to QA
148. pdf
149. pdftk-server
150. pptx
151. task-management
152. user-communication-preferences
153. xlsx
154. boilerplate-stripper

### Batch 23 (155-161): QA - Playwright
155. playwright-automation-fill-in-form
156. playwright-generate-e2e-test
157. playwright-generate-test
158. polyglot-test-agent
159. postgresql-code-review
160. scoutqa-test
161. test-skill

### Batch 24 (162-168): QA - Verification to Web
162. verification-before-completion
163. web-design-reviewer
164. webapp-testing
165. godmode
166. repo-research-pipeline
167. web-research-pipeline
168. banking

### Batch 25 (169-175): Software Dev - Bash to Code
169. bash-scripts-audit-remediation
170. caveman-unified
171. claude-api
172. clonedeps
173. code-docs
174. codemap
175. context7

### Batch 26 (176-182): Software Dev - Debug to Mindstudio
176. debugging-hermes-tui-commands
177. executing-plans
178. fluentui-blazor
179. httpie
180. mindstudio-wrapper
181. nuget-manager
182. project-docs

### Batch 27 (183-189): Software Dev - Quasi to Script
183. quasi-coder
184. receiving-code-review
185. refactor
186. sandbox
187. script-orchestration
188. shadcn
189. winapp-cli

### Batch 28 (190-191): Software Dev - Worktrunk to Writing
190. worktrunk
191. writing-plans

---

## Execution Workflow (Per Batch)

### For Each Batch (7 skills):

```markdown
### Step A: Judge Batch
1. Load skill-judge skill: `skill_view('skill-judge')`
2. For each skill in batch:
   - `skill_view('<skill-name>')` — read full SKILL.md + references
   - Run skill-judge evaluation against criteria:
     - Accuracy & correctness
     - Completeness (all sections present)
     - Usability (clear triggers, examples, verification)
     - Maintainability (DRY, no hardcoded paths)
   - Record: score, pass/fail, specific failures

### Step B: Remediate Failures
3. For each failed skill:
   - Diagnose root cause (missing sections, broken commands, stale examples, no verification gates)
   - `skill_manage(action='patch', name='<skill>', old_string='...', new_string='...')`
   - Re-judge patched skill
   - Confirm pass

### Step C: Document
4. Save batch results to `judge_batch_N_results.md`
5. Log patches applied
```

---

## Files to Create/Update

| File | Purpose |
|------|---------|
| `skills_inventory_20260614_143500.log` | ✅ Raw inventory (done) |
| `skill_names_191.txt` | ✅ Parsed skill names (done) |
| `judge_batch_1_results.md` ... `judge_batch_28_results.md` | Per-batch judgment results |
| `skills_audit_final_report.md` | Final aggregate report |
| `profiles/code-architect/skills/*/SKILL.md` | Patched skills (as needed) |

---

## Validation Criteria (from skill-judge)

Each skill evaluated on:
- [ ] **Accuracy** — Commands work, APIs current, examples executable
- [ ] **Completeness** — All required sections: trigger, steps, pitfalls, verification
- [ ] **Usability** — Clear prerequisites, copy-paste runnable examples
- [ ] **Maintainability** — No hardcoded paths, DRY, version-agnostic where possible
- [ ] **Safety** — No destructive ops without confirmation, secrets handling

---

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Token overflow per batch | Batch size 7; summarize results, don't retain full skill text |
| Truncated skill names in log | Map to actual directory names (see mapping below) |
| Skill-judge criteria too strict | First batch calibrates; adjust threshold if needed |
| Unfixable skills | Mark `deprecated` in manifest; exclude from future |
| Time: 28 batches × ~10 min | ~4-5 hours total; can parallelize across sessions |

---

## Truncated Name → Directory Mapping

| Log Name (Truncated) | Actual Directory |
|---------------------|------------------|
| stable-diffusion-image-g… | stable-diffusion-image-generation |
| architecture-blueprint-g… | architecture-blueprint-generator |
| folder-structure-bluepri… | folder-structure-blueprint-generator |
| technology-stack-bluepri… | technology-stack-blueprint-generator |
| hermes-skill-library-mai… | hermes-skill-library-maintenance |
| excalidraw-diagram-gener… | excalidraw-diagram-generator |
| image-manipulation-image… | image-manipulation-image-magick |
| nano-banana-pro-openrout… | nano-banana-pro-openrouter |
| writing-clearly-and-conc… | writing-clearly-and-concisely |
| ai-prompt-engineering-sa… | ai-prompt-engineering-safety-review |
| create-implementation-pl… | create-implementation-plan |
| generate-custom-instruct… | generate-custom-instructions-from-codebase |
| suggest-awesome-github-c… | suggest-awesome-github-copilot-agents |
| suggest-awesome-github-c… | suggest-awesome-github-copilot-instructions |
| update-implementation-pl… | update-implementation-plan |
| vscode-workspace-configu… | vscode-workspace-configurator |
| appinsights-instrumentat… | appinsights-instrumentation |
| azure-deployment-preflig… | azure-deployment-preflight |
| git-history-preserving-m… | git-history-preserving-migration |
| projects-multi-repo-init… | projects-multi-repo-init-normalize |
| provider-reliability-dia… | provider-reliability-diagnostics |
| terraform-azurerm-set-di… | terraform-azurerm-set-diff-analyzer |
| windows-maintenance-oper… | windows-maintenance-operations |
| finishing-a-development-… | finishing-a-development-branch |
| documentation-extraction… | documentation-extraction-and-indexing |
| user-communication-prefe… | user-communication-preferences |
| playwright-automation-fi… | playwright-automation-fill-in-form |
| playwright-generate-e2e-… | playwright-generate-e2e-test |
| verification-before-comp… | verification-before-completion |
| bash-scripts-audit-remed… | bash-scripts-audit-remediation |
| debugging-hermes-tui-com… | debugging-hermes-tui-commands |
| prompt-planning-orchestr… | prompt-planning-orchestration |
| transloadit-media-proces… | transloadit-media-processing |

---

## Execution Order

1. **Batch 1** → Judge → Patch → Re-judge → Document
2. **Batch 2** → Judge → Patch → Re-judge → Document
3. ... continue through Batch 28
4. **Final Report** → Aggregate all results

---

## Saved Plan Location

`.hermes/plans/2026-06-14_143000-skills-audit-pipeline.md` (this file, updated)

---

## Next Action

**Ready to execute Batch 1.** Want me to:
1. Run Batch 1 judgment now?
2. Adjust batch size or criteria?
3. Skip any skills/categories?