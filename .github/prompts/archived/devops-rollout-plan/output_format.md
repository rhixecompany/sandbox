# Output Format

> Extracted from `devops-rollout-plan.prompt.md`.

## Output Format

Generate a structured rollout plan with these sections:

### 1. Executive Summary

- What, why, when, duration
- Risk level and rollback time
- Affected systems and user impact
- Expected downtime

### 2. Prerequisites & Approvals

- Required approvals (technical lead, security, compliance, business)
- Required resources (capacity, backups, monitoring, rollback automation)
- Pre-deployment backups

### 3. Preflight Checks

- Infrastructure health validation
- Application health baseline
- Dependency availability
- Monitoring baseline metrics
- Go/no-go decision checklist

### 4. Step-by-Step Rollout Procedure

**Phases**: Pre-deployment, deployment, progressive verification

- Specific commands for each step
- Validation after each step
- Duration estimates

### 5. Verification Signals

**Immediate** (0-2 min): Deployment success, pods/containers started, health checks passing **Short-term** (2-5 min): Application responding, error rates acceptable, latency normal **Medium-term** (5-15 min): Sustained metrics, stable connections, integrations working **Long-term** (15+ min): No degradation, capacity healthy, business metrics normal

### 6. Rollback Procedure

**Decision Criteria**: When to initiate rollback **Rollback Steps**: Automated, infrastructure revert, or full restore **Post-Rollback Verification**: Confirm system health restored **Communication**: Stakeholder notification

### 7. Communication Plan

- Pre-deployment (T-24h): Schedule and impact notice
- Deployment start: Commencement notice
- Progress updates: Status every X minutes
- Completion: Success confirmation
- Rollback (if needed): Issue notification

**Stakeholder Matrix**: Who to notify, when, via what method, with what content

### 8. Post-Deployment Tasks

- Immediate (1h): Verify criteria met, review logs
- Short-term (24h): Monitor metrics, review errors
- Medium-term (1 week): Post-deployment review, lessons learned

### 9. Contingency Plans

Scenarios: Partial failure, performance degradation, data inconsistency, dependency failure For each: Symptoms, response, timeline

### 10. Contact Information

- Primary and secondary on-call
- Escalation path
- Emergency contacts (infrastructure, security, database, networking)
