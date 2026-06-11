#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

/**
 * Phase 3: Consolidation
 * Merge all findings from Phase 1 & 2, assign IDs, group into batches
 */

class FindingsConsolidator {
  constructor(auditDir, batchDir) {
    this.auditDir = auditDir;
    this.batchDir = batchDir;
    this.findings = [];
    this.findingId = 0;
  }

  /**
   * Load all findings from audit directory
   */
  loadAllFindings() {
    const files = fs.readdirSync(this.auditDir);
    const diagnosticFiles = files.filter((f) => f.includes("diagnostic_"));

    for (const file of diagnosticFiles) {
      try {
        const content = fs.readFileSync(
          path.join(this.auditDir, file),
          "utf-8",
        );
        const data = JSON.parse(content);
        // Parse findings from diagnostic output
        console.log(`Loaded: ${file}`);
      } catch (e) {
        console.error(`Error loading ${file}: ${e.message}`);
      }
    }
  }

  /**
   * Consolidate and assign unique IDs
   */
  consolidateFindings(allRawFindings) {
    const consolidated = [];

    allRawFindings.forEach((finding, idx) => {
      consolidated.push({
        ...finding,
        consolidatedId: `FIND-${String(++this.findingId).padStart(4, "0")}`,
      });
    });

    return consolidated;
  }

  /**
   * Group findings into batches (max 7 files per batch)
   */
  groupIntoBatches(findings) {
    const batches = [];
    let currentBatch = {
      id: `BATCH-001`,
      findings: [],
      fileCount: 0,
    };

    // Sort by severity (CRITICAL first)
    const severityOrder = { critical: 0, high: 1, medium: 2, low: 3 };
    findings.sort(
      (a, b) =>
        (severityOrder[a.severity] || 99) - (severityOrder[b.severity] || 99),
    );

    for (const finding of findings) {
      // Estimate files affected (conservatively, 1 per finding)
      const filesNeeded = 1;

      if (currentBatch.fileCount + filesNeeded > 7) {
        // Finalize current batch and start new
        batches.push(currentBatch);
        currentBatch = {
          id: `BATCH-${String(batches.length + 1).padStart(3, "0")}`,
          findings: [],
          fileCount: 0,
        };
      }

      currentBatch.findings.push(finding);
      currentBatch.fileCount += filesNeeded;
    }

    if (currentBatch.findings.length > 0) {
      batches.push(currentBatch);
    }

    return batches;
  }

  /**
   * Generate consolidated report
   */
  generateConsolidatedReport(findings, batches) {
    const summary = {
      timestamp: new Date().toISOString(),
      totalFindings: findings.length,
      byCritical: findings.filter((f) => f.severity === "critical").length,
      byHigh: findings.filter((f) => f.severity === "high").length,
      byMedium: findings.filter((f) => f.severity === "medium").length,
      byLow: findings.filter((f) => f.severity === "low").length,
      totalBatches: batches.length,
      maxFilesPerBatch: 7,
    };

    let reportContent = `# Consolidated Proposed Fixes Report

Generated: ${summary.timestamp}

## Summary

- **Total Findings**: ${summary.totalFindings}
  - Critical: ${summary.byCritical}
  - High: ${summary.byHigh}
  - Medium: ${summary.byMedium}
  - Low: ${summary.byLow}
- **Total Batches**: ${summary.totalBatches}
- **Max Files per Batch**: ${summary.maxFilesPerBatch}

## Batch Breakdown

`;

    batches.forEach((batch) => {
      reportContent += `### ${batch.id} (${batch.findings.length} findings, ${batch.fileCount} files)\n\n`;
      batch.findings.forEach((finding) => {
        const severity = (finding.severity || "unknown").toUpperCase();
        const type = finding.type || "UNKNOWN";
        const repoId = finding.repoId || "unknown";
        const rootCause =
          finding.rootCause || finding.description || "Unknown issue";
        const proposedFix = finding.proposedFix || "No fix proposed";
        const complexity = finding.complexity || "UNKNOWN";
        const risk = finding.risk || "UNKNOWN";

        reportContent += `- **${finding.consolidatedId}** [${severity}] ${type}\n`;
        reportContent += `  - Repo: ${repoId}\n`;
        reportContent += `  - Issue: ${rootCause}\n`;
        reportContent += `  - Fix: ${proposedFix}\n`;
        reportContent += `  - Complexity: ${complexity}\n`;
        reportContent += `  - Risk: ${risk}\n\n`;
      });
    });

    return reportContent;
  }

  /**
   * Execute Phase 3: Consolidate, batch, and report
   */
  execute(allFindings) {
    console.log("\n==========================================");
    console.log("Phase 3: Consolidation");
    console.log("==========================================\n");

    // Consolidate
    const consolidated = this.consolidateFindings(allFindings);
    console.log(`Consolidated ${consolidated.length} findings`);

    // Group into batches
    const batches = this.groupIntoBatches(consolidated);
    console.log(`Grouped into ${batches.length} batches`);

    // Generate report
    const reportContent = this.generateConsolidatedReport(
      consolidated,
      batches,
    );
    const reportPath = "./CONSOLIDATED_PROPOSED_FIXES.md";
    fs.writeFileSync(reportPath, reportContent);
    console.log(`\nReport generated: ${reportPath}`);

    // Save batches
    const batchesPath = "./BATCHES.json";
    fs.writeFileSync(batchesPath, JSON.stringify(batches, null, 2));
    console.log(`Batches saved: ${batchesPath}`);

    console.log("\n==========================================");
    console.log("Phase 3 Complete");
    console.log("==========================================\n");

    return { consolidated, batches, reportPath, batchesPath };
  }
}

// Main execution
if (require.main === module) {
  const auditDir = path.join(__dirname, "../docs/audits");
  const batchDir = path.join(__dirname, "../BATCH_LOGS");

  // Ensure batch directory exists
  if (!fs.existsSync(batchDir)) {
    fs.mkdirSync(batchDir, { recursive: true });
  }

  const consolidator = new FindingsConsolidator(auditDir, batchDir);

  // Load all findings from diagnostic files
  const files = fs.readdirSync(auditDir);
  const diagnosticFiles = files.filter((f) => f.includes("diagnostic_"));

  const allFindings = [];
  for (const file of diagnosticFiles) {
    try {
      const content = fs.readFileSync(path.join(auditDir, file), "utf-8");
      const data = JSON.parse(content);

      // Extract repoId from filename (e.g., "comicwise_diagnostic_2026-05-15_12-25-17.json")
      const repoId = file.split("_diagnostic_")[0];

      // Handle both array and single object formats
      const findings = Array.isArray(data) ? data : [data];

      // Add repoId to each finding
      findings.forEach((finding) => {
        allFindings.push({
          ...finding,
          repoId: repoId,
        });
      });
    } catch (e) {
      console.error(`Error loading ${file}: ${e.message}`);
    }
  }

  // Execute consolidation
  consolidator.execute(allFindings);
}

module.exports = FindingsConsolidator;
