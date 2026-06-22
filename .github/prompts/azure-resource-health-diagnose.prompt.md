---
agent: "agent"
description: "Analyze Azure resource health, diagnose issues from logs and telemetry, and create a remediation plan for identified problems."
---

## Goal

Analyze Azure resource health, diagnose issues from logs and telemetry, and create a remediation plan for identified problems.

## Context

Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.

## Phases

### Phase 1: Intake
- Read the request and identify the exact scope.
- Locate the relevant files, diffs, or references.

### Phase 2: Execute
- Perform the requested work with the smallest safe change set.
- Keep the steps explicit and reproducible.

### Phase 3: Verify
- Check the result against the goal, rules, and inputs.
- Confirm the output is usable and complete.

### Phase 4: Hand off
- Return the final artifact or findings clearly.
- Stop once the requested result is delivered.

## Legacy Prompt Details
# Azure Resource Health & Issue Diagnosis

This workflow analyzes a specific Azure resource to assess its health status, diagnose potential issues using logs and telemetry data, and develop a comprehensive remediation plan for any problems discovered.

## Prerequisites

- Azure MCP server configured and authenticated
- Target Azure resource identified (name and optionally resource group/subscription)
- Resource must be deployed and running to generate logs/telemetry
- Prefer Azure MCP tools (`azmcp-*`) over direct Azure CLI when available

## Workflow Steps

> ### Step 1: Get Azure Best Practices
> **Action**: Retrieve diagnostic and troubleshooting best practices **Tools**: Az

> **Full content:** `templates/azure-resource-health-diagnose/workflow_steps.md`

   ## 🔍 Executive Summary

   [Brief overview of health status and key findings]

   ## 📊 Health Metrics

   - **Availability**: X% over last 24h
   - **Performance**: [Average response time/throughput]
   - **Error Rate**: X% over last 24h
   - **Resource Utilization**: [CPU/Memory/Storage percentages]

   ## 🚨 Issues Identified

   ### Critical Issues

   - **[Issue 1]**: [Description]
     - **Root Cause**: [Analysis]
     - **Impact**: [Business impact]
     - **Immediate Action**: [Required steps]

   ### High Priority Issues

   - **[Issue 2]**: [Description]
     - **Root Cause**: [Analysis]
     - **Impact**: [Performance/reliability impact]
     - **Recommended Fix**: [Solution steps]

   ## 🛠️ Remediation Plan

   ### Phase 1: Immediate Actions (0-2 hours)

   ```bash
   # Critical fixes to restore service
   [Azure CLI commands with explanations]
   ```
   ````

   ### Phase 2: Short-term Fixes (2-24 hours)

   ```bash
   # Performance and reliability improvements
   [Azure CLI commands with explanations]
   ```

   ### Phase 3: Long-term Improvements (1-4 weeks)

   ```bash
   # Architectural and preventive measures
   [Azure CLI commands and configuration changes]
   ```

   ## 📈 Monitoring Recommendations
   - **Alerts to Configure**: [List of recommended alerts]
   - **Dashboards to Create**: [Monitoring dashboard suggestions]
   - **Regular Health Checks**: [Recommended frequency and scope]

   ## ✅ Validation Steps
   - [ ] Verify issue resolution through logs
   - [ ] Confirm performance improvements
   - [ ] Test application functionality
   - [ ] Update monitoring and alerting
   - [ ] Document lessons learned

   ## 📝 Prevention Measures
   - [Recommendations to prevent similar issues]
   - [Process improvements]
   - [Monitoring enhancements]

   ```

   ```

## Error Handling

- **Resource Not Found**: Provide guidance on resource name/location specification
- **Authentication Issues**: Guide user through Azure authentication setup
- **Insufficient Permissions**: List required RBAC roles for resource access
- **No Logs Available**: Suggest enabling diagnostic settings and waiting for data
- **Query Timeouts**: Break down analysis into smaller time windows
- **Service-Specific Issues**: Provide generic health assessment with limitations noted

## Success Criteria

- ✅ Resource health status accurately assessed
- ✅ All significant issues identified and categorized
- ✅ Root cause analysis completed for major problems
- ✅ Actionable remediation plan with specific steps provided
- ✅ Monitoring and prevention recommendations included
- ✅ Clear prioritization of issues by business impact
- ✅ Implementation steps include validation and rollback procedures


## Template References

Detailed templates in `templates/azure-resource-health-diagnose/`:
- `workflow_steps.md`
