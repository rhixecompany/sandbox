---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Azure Cost Optimize
name: az-cost-optimize
description: "Analyze Azure resources used in the app (IaC files and/or resources in a target rg) and optimize costs - creating GitHub issues for identified optimizations."
---

# Azure Cost Optimize

This workflow analyzes Infrastructure-as-Code (IaC) files and Azure resources to generate cost optimization recommendations. It creates individual GitHub issues for each optimization opportunity plus one EPIC issue to coordinate implementation, enabling efficient tracking and execution of cost savings initiatives.

## Prerequisites

- Azure MCP server configured and authenticated
- GitHub MCP server configured and authenticated
- Target GitHub repository identified
- Azure resources deployed (IaC files optional but helpful)
- Prefer Azure MCP tools (`azmcp-*`) over direct Azure CLI when available

## Workflow Steps

> ### Step 1: Get Azure Best Practices
> **Action**: Retrieve cost optimization best practices before analysis **Tools**:

> **Full content:** `templates/az-cost-optimize/workflow_steps.md`

## 💰 Cost Optimization: [Brief Title]

> **Monthly Savings**: $X | **Risk Level**: [Low/Medium/High] | **Implementation E
> [Clear explanation of the optimization and why it's needed]

> **Full content:** `templates/az-cost-optimize/cost_optimization_brief_title.md`

   ## 📊 Executive Summary

   - **Resources Analyzed**: X
   - **Optimization Opportunities**: Y
   - **Total Monthly Savings Potential**: $X
   - **High Priority Items**: N

   ## 🏗️ Current Architecture Overview

   ```mermaid
   graph TB
       subgraph "Resource Group: [name]"
           [Generated architecture diagram showing current resources and costs]
       end
   ```
   ````

   ## 📋 Implementation Tracking

   ### 🚀 High Priority (Implement First)
   - [ ] # [issue-number]: [Title] - $X/month savings
   - [ ] # [issue-number]: [Title] - $X/month savings

   ### ⚡ Medium Priority
   - [ ] # [issue-number]: [Title] - $X/month savings
   - [ ] # [issue-number]: [Title] - $X/month savings

   ### 🔄 Low Priority (Nice to Have)
   - [ ] # [issue-number]: [Title] - $X/month savings

   ## 📈 Progress Tracking
   - **Completed**: 0 of Y optimizations
   - **Savings Realized**: $0 of $X/month
   - **Implementation Status**: Not Started

   ## 🎯 Success Criteria
   - [ ] All high-priority optimizations implemented
   - [ ] > 80% of estimated savings realized
   - [ ] No performance degradation observed
   - [ ] Cost monitoring dashboard updated

   ## 📝 Notes
   - Review and update this EPIC as issues are completed
   - Monitor actual vs. estimated savings
   - Consider scheduling regular cost optimization reviews

   ```

   ```

## Error Handling

- **Cost Validation**: If savings estimates lack supporting evidence or seem inconsistent with Azure pricing, re-verify configurations and pricing sources before proceeding
- **Azure Authentication Failure**: Provide manual Azure CLI setup steps
- **No Resources Found**: Create informational issue about Azure resource deployment
- **GitHub Creation Failure**: Output formatted recommendations to console
- **Insufficient Usage Data**: Note limitations and provide configuration-based recommendations only

## Success Criteria

- ✅ All cost estimates verified against actual resource configurations and Azure pricing
- ✅ Individual issues created for each optimization (trackable and assignable)
- ✅ EPIC issue provides comprehensive coordination and tracking
- ✅ All recommendations include specific, executable Azure CLI commands
- ✅ Priority scoring enables ROI-focused implementation
- ✅ Architecture diagram accurately represents current state
- ✅ User confirmation prevents unwanted issue creation


## Template References

Detailed templates in `templates/az-cost-optimize/`:
- `cost_optimization_brief_title.md`
- `workflow_steps.md`
