# Phase 5: Remediation Planning
# Generates actionable remediation plans for HIGH priority repos

# Load shared modules
$libCore = Join-Path $PSScriptRoot "lib/core"
Import-Module (Join-Path $libCore "logger.psm1") -Force -ErrorAction Stop
Import-Module (Join-Path $libCore "dir-manager.psm1") -Force -ErrorAction Stop

Write-Header "Phase 5: Remediation Planning"

# Load debug report
$debugReportPath = Join-Path (Split-Path $PSScriptRoot -Parent) "REPO_AUDIT/DEBUG_REPORT.json"
$debugReport = Get-Content $debugReportPath | ConvertFrom-Json

# Filter HIGH priority repos
$highPriorityRepos = $debugReport.results | Where-Object { $_.priority -eq "HIGH" }

Write-Phase "Found $($highPriorityRepos.Count) HIGH priority repos"

# Create remediation plans
$remediationPlans = @()

foreach ($repo in $highPriorityRepos) {
    Write-Phase "[REMEDIATION] Planning for: $($repo.name)"
    
    $plan = @{
        repo_name = $repo.name
        repo_path = $repo.path
        priority = $repo.priority
        timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        
        security = @{
            severity = "CRITICAL"
            hardcoded_credentials = $repo.security_analysis.hardcoded_credentials
            exposed_env_vars = $repo.security_analysis.exposed_env_vars
            secrets_found = $repo.security_analysis.secrets_found
            total_issues = $repo.security_analysis.secrets_found + $repo.security_analysis.hardcoded_credentials + $repo.security_analysis.exposed_env_vars
        }
        
        code_quality = @{
            severity = "HIGH"
            broken_imports = $repo.code_quality_analysis.broken_imports
        }
        
        documentation = @{
            severity = "MEDIUM"
            completeness = $repo.documentation_analysis.completeness_percent
            has_readme = $repo.documentation_analysis.has_readme
            has_changelog = $repo.documentation_analysis.has_changelog
        }
        
        dependencies = @{
            total_packages = $repo.dependency_analysis.total_packages
            managers = $repo.dependency_analysis.detected_managers -join ", "
        }
        
        git = @{
            total_commits = $repo.git_analysis.total_commits
            contributors = $repo.git_analysis.contributor_count
            days_since_last = $repo.git_analysis.days_since_last_commit
        }
        
        total_estimated_hours = 22
    }
    
    $remediationPlans += $plan
    Write-Success "  OK: Remediation plan created"
}

Write-Phase "Generating remediation reports..."

# Save JSON report
$jsonPath = "C:\Users\Alexa\Desktop\SandBox\REPO_AUDIT\REMEDIATION_REPORT.json"
$remediationPlans | ConvertTo-Json -Depth 10 | Set-Content $jsonPath
Write-Success "JSON report saved"

# Generate Markdown report
$mdPath = "C:\Users\Alexa\Desktop\SandBox\REPO_AUDIT\REMEDIATION_PLAN.md"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$totalHours = $remediationPlans | Measure-Object -Property total_estimated_hours -Sum | Select-Object -ExpandProperty Sum

$mdContent = "# Phase 5: Remediation Planning`n`n"
$mdContent += "**Generated**: $timestamp`n"
$mdContent += "**Total HIGH Priority Repos**: $($remediationPlans.Count)`n"
$mdContent += "**Total Estimated Hours**: $totalHours`n`n"
$mdContent += "---`n`n"

foreach ($plan in $remediationPlans) {
    $mdContent += "## $($plan.repo_name)`n`n"
    $mdContent += "**Path**: ``$($plan.repo_path)``  `n"
    $mdContent += "**Priority**: $($plan.priority)  `n"
    $mdContent += "**Total Estimated Hours**: $($plan.total_estimated_hours)`n`n"
    
    $mdContent += "### Security Issues (CRITICAL - $($plan.security.total_issues) issues)`n`n"
    $mdContent += "- **Hardcoded Credentials**: $($plan.security.hardcoded_credentials) found`n"
    $mdContent += "  - Action: Remove all hardcoded credentials and use environment variables`n`n"
    $mdContent += "- **Exposed Environment Variables**: $($plan.security.exposed_env_vars) found`n"
    $mdContent += "  - Action: Move sensitive env vars to .env.example and add .env to .gitignore`n`n"
    $mdContent += "- **Potential Secrets**: $($plan.security.secrets_found) found`n"
    $mdContent += "  - Action: Scan with git-secrets or truffleHog and remove from history`n`n"
    
    $mdContent += "### Code Quality Issues (HIGH)`n`n"
    $mdContent += "- **Broken Imports**: $($plan.code_quality.broken_imports) found`n"
    $mdContent += "  - Action: Fix import paths and verify all dependencies are installed`n`n"
    
    $mdContent += "### Documentation Issues (MEDIUM)`n`n"
    $mdContent += "- **Completeness**: $($plan.documentation.completeness)%`n"
    $mdContent += "- **Has README**: $($plan.documentation.has_readme)`n"
    $mdContent += "- **Has CHANGELOG**: $($plan.documentation.has_changelog)`n"
    $mdContent += "- **Action**: Increase documentation coverage to 80% and add CHANGELOG.md`n`n"
    
    $mdContent += "### Dependencies`n`n"
    $mdContent += "- **Total Packages**: $($plan.dependencies.total_packages)`n"
    $mdContent += "- **Package Managers**: $($plan.dependencies.managers)`n"
    $mdContent += "- **Action**: Run npm audit / pip audit and update outdated packages`n`n"
    
    $mdContent += "### Git History`n`n"
    $mdContent += "- **Total Commits**: $($plan.git.total_commits)`n"
    $mdContent += "- **Contributors**: $($plan.git.contributors)`n"
    $mdContent += "- **Days Since Last Commit**: $($plan.git.days_since_last)`n"
    $mdContent += "- **Action**: Clean git history of exposed secrets using git-filter-branch or BFG`n`n"
    
    $mdContent += "### Remediation Steps`n`n"
    $mdContent += "1. **IMMEDIATE (Security)** - ~4 hours`n"
    $mdContent += "   - Remove hardcoded credentials from codebase`n"
    $mdContent += "   - Move sensitive env vars to .env.example`n"
    $mdContent += "   - Add .env and .secrets to .gitignore`n"
    $mdContent += "   - Clean git history of exposed secrets`n`n"
    
    $mdContent += "2. **SHORT-TERM (Code Quality)** - ~6 hours`n"
    $mdContent += "   - Fix broken imports ($($plan.code_quality.broken_imports) issues)`n"
    $mdContent += "   - Run linter and fix style issues`n"
    $mdContent += "   - Add missing type definitions`n"
    $mdContent += "   - Audit and update dependencies`n`n"
    
    $mdContent += "3. **MEDIUM-TERM (Documentation)** - ~8 hours`n"
    $mdContent += "   - Create CHANGELOG.md`n"
    $mdContent += "   - Add API documentation`n"
    $mdContent += "   - Write setup and deployment guides`n"
    $mdContent += "   - Document architecture and design decisions`n`n"
    
    $mdContent += "4. **ONGOING (Maintenance)** - ~4 hours`n"
    $mdContent += "   - Set up automated security scanning`n"
    $mdContent += "   - Enable dependabot for dependency updates`n"
    $mdContent += "   - Implement pre-commit hooks for secret detection`n"
    $mdContent += "   - Establish code review process`n`n"
    
    $mdContent += "---`n`n"
}

$mdContent | Set-Content $mdPath
Write-Success "Markdown report saved"

Write-Success "Phase 5 Complete!"
Write-Phase "Summary:"
Write-Info "  - $($remediationPlans.Count) HIGH priority repos analyzed"
Write-Info "  - $totalHours total estimated hours for remediation"
Write-Info "  - Reports saved to REPO_AUDIT directory"
Set-StrictMode -Version Latest
