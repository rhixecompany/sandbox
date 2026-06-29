# Phases

> Extracted from `tasksync.prompt.md`.

## Phases

### Phase 1: Initialization and Intake

| Field | Details |
| --- | --- |
| Goal | Start TaskSync state machine and obtain first actionable task. |
| Inputs | Session start state and terminal task intake command. |
| Outputs | Active task assignment or waiting-input state. |
| Validation | Initialization phrase and intake command flow are executed correctly. |

### Phase 2: Focused Task Execution

| Field | Details |
| --- | --- |
| Goal | Complete current task fully without non-urgent context switching. |
| Inputs | Current active task, task-specific context, override signals. |
| Outputs | Completed task artifacts and concise progress updates. |
| Validation | Task is completed or explicitly switched only via urgent override. |

### Phase 3: Completion and Continuation Loop

| Field | Details |
| --- | --- |
| Goal | Request and process next task until explicit termination command. |
| Inputs | Completion state, terminal intake responses, failure conditions. |
| Outputs | Next task activation or waiting-input fallback state. |
| Validation | Approved completion phrase used and intake protocol followed exactly. |
