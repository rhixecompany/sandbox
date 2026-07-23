# Input Requirements

> Extracted from `devops-rollout-plan.prompt.md`.

## Input Requirements

Gather these details before generating the plan:

### Change Description

- What's changing (infrastructure, application, configuration)
- Version or state transition (from/to)
- Problem solved or feature added

### Environment Details

- Target environment (dev, staging, production, all)
- Infrastructure type (Kubernetes, VMs, serverless, containers)
- Affected services and dependencies
- Current capacity and scale

### Constraints & Requirements

- Acceptable downtime window
- Change window restrictions
- Approval requirements
- Regulatory or compliance considerations

### Risk Assessment

- Blast radius of change
- Data migrations or schema changes
- Rollback complexity and safety
- Known risks
