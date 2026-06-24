# Phases

> Extracted from `playwright-automation-fill-in-form.prompt.md`.

## Phases

### Phase 1: Intake
**Goal:** confirm the form details before touching the page.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Read the requested URL and values | Input summary |
| 1.2 | Confirm any missing values or file paths | Clarification list |
| 1.3 | Decide whether the upload path is valid | Ready/not-ready status |

#### Tasks
- Validate the form inputs.
- Identify any missing detail early.
- Avoid guessing on ambiguous fields.

### Phase 2: Fill the form
**Goal:** enter the data into the form without submitting it.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 2.1 | Open the form URL | Loaded form |
| 2.2 | Fill each field in order | Completed inputs |
| 2.3 | Upload the image if valid | Uploaded attachment |

#### Tasks
- Enter the values exactly as provided.
- Keep the browser on the form page.
- Do not click submit.

### Phase 3: Verify state
**Goal:** confirm the form is ready for human review.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 3.1 | Re-check filled fields | Verification notes |
| 3.2 | Verify the upload state | Attachment status |
| 3.3 | Pause before submission | Review-ready state |

#### Tasks
- Confirm the form is filled correctly.
- Highlight any remaining issue.
- Stop before any submission action.

### Phase 4: Hand off
**Goal:** ask for review and wait for direction.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 4.1 | Summarize what was completed | Handoff note |
| 4.2 | State that the form was not submitted | Safety confirmation |
| 4.3 | Ask for review or next step | User response |

#### Tasks
- Report the filled fields.
- Confirm submission did not happen.
- Ask for approval before any further action.
