# Phases

> Extracted from `playwright-explore-website.prompt.md`.

## Phases

### Phase 1: Start and orient
**Goal:** load the site and identify the main areas worth exploring.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Open the provided URL | Loaded page |
| 1.2 | Identify the main navigation and primary actions | Flow shortlist |
| 1.3 | Pick 3 to 5 core flows | Exploration plan |

#### Tasks
- Confirm the site is reachable.
- Choose the most important flows.
- Keep the exploration focused.

### Phase 2: Explore flows
**Goal:** interact with the key flows and observe behavior.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 2.1 | Trigger the selected user flows | Interaction notes |
| 2.2 | Record visible UI responses | Outcome log |
| 2.3 | Capture locators for key elements | Locator list |

#### Tasks
- Test the main paths only.
- Note any blocking or confusing behavior.
- Keep the interactions reproducible.

### Phase 3: Document findings
**Goal:** turn the exploration into a clear artifact.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 3.1 | Summarize the flows explored | Flow summary |
| 3.2 | List the key locators and outcomes | Evidence table |
| 3.3 | Note any issues or observations | Findings |

#### Tasks
- Keep notes concise and specific.
- Include element locators when useful.
- Highlight any friction or failure.

### Phase 4: Propose tests and close out
**Goal:** suggest test coverage and finish the session cleanly.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 4.1 | Convert exploration notes into test ideas | Test list |
| 4.2 | Close the browser context | Clean shutdown |
| 4.3 | Deliver the summary | Final report |

#### Tasks
- Propose tests based on real behavior.
- Close the browser when done.
- End with a short, actionable summary.
