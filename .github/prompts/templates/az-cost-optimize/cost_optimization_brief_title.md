# 💰 Cost Optimization: [Brief Title]

> Extracted from `az-cost-optimize.prompt.md`.

   ## 💰 Cost Optimization: [Brief Title]

   **Monthly Savings**: $X | **Risk Level**: [Low/Medium/High] | **Implementation Effort**: X days

   ### 📋 Description

   [Clear explanation of the optimization and why it's needed]

   ### 🔧 Implementation

   **IaC Files Detected**: [Yes/No - based on file_search results]

   ```bash
   # If IaC files found: Show IaC modifications + deployment
   # File: infrastructure/bicep/modules/app-service.bicep
   # Change: sku.name: 'S3' → 'B2'
   az deployment group create --resource-group [rg] --template-file infrastructure/bicep/main.bicep

   # If no IaC files: Direct Azure CLI commands + warning
   # ⚠️ No IaC files found. If they exist elsewhere, modify those instead.
   az appservice plan update --name [plan] --sku B2
   ```
   ````

   ### 📊 Evidence
   - Current Configuration: [details]
   - Usage Pattern: [evidence from monitoring data]
   - Cost Impact: $X/month → $Y/month
   - Best Practice Alignment: [reference to Azure best practices if applicable]

   ### ✅ Validation Steps
   - [ ] Test in non-production environment
   - [ ] Verify no performance degradation
   - [ ] Confirm cost reduction in Azure Cost Management
   - [ ] Update monitoring and alerts if needed

   ### ⚠️ Risks & Considerations
   - [Risk 1 and mitigation]
   - [Risk 2 and mitigation]

   **Priority Score**: X | **Value**: X/10 | **Risk**: X/10

   ```

   ```

### Step 7: Create EPIC Coordinating Issue

**Action**: Create master issue to track all optimization work. Label it with "cost-optimization" (green color), "azure" (blue color), and "epic" (purple color). **MCP Tools Required**: `create_issue` for EPIC **Note about mermaid diagrams**: Ensure you verify mermaid syntax is correct and create the diagrams taking accessibility guidelines into account (styling, colors, etc.). **Process**:

1. **Create EPIC Issue**:

   **Title**: `[EPIC] Azure Cost Optimization Initiative - $X/month potential savings`

   **Body Template**:

   ````markdown
   # 🎯 Azure Cost Optimization EPIC

   **Total Potential Savings**: $X/month | **Implementation Timeline**: X weeks
