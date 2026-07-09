#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

/**
 * Phase 5: Final Summary
 * Generate final audit report and summary
 */

class FinalSummaryGenerator {
  constructor(batchLogsDir) {
    this.batchLogsDir = batchLogsDir;
    this.logs = [];
  }

  /**
   * Load all batch logs
   */
  loadBatchLogs() {
    const files = fs.readdirSync(this.batchLogsDir);
    const logFiles = files.filter((f) => f.includes("_log.json"));

    for (const file of logFiles) {
      try {
        const content = fs.readFileSync(
          path.join(this.batchLogsDir, file),
          "utf-8",
        );
        this.logs.push(JSON.parse(content));
      } catch (e) {
        console.error(`Error loading ${file}: ${e.message}`);
      }
    }
  }

  /**
   * Generate final summary
   */
  generateSummary() {
    const summary = {
      timestamp: new Date().toISOString(),
      totalBatches: this.logs.length,
      totalFindings: this.logs.reduce(
        (sum, log) => sum + log.results.length,
        0,
      ),
      successful: this.logs.filter((log) => log.status === "success").length,
      partial: this.logs.filter((log) => log.status === "partial").length,
      failed: this.logs.filter((log) => log.status === "failed").length,
      verificationPassed: this.logs.filter(
        (log) =>
          log.verification && log.verification.overallStatus === "passed",
      ).length,
      verificationSkipped: this.logs.filter(
        (log) =>
          log.verification && log.verification.overallStatus === "skipped",
      ).length,
    };

    let reportContent = `# Final Audit Summary

Generated: ${summary.timestamp}

## Execution Summary

- **Total Batches**: ${summary.totalBatches}
- **Total Findings Applied**: ${summary.totalFindings}
- **Successful Batches**: ${summary.successful}
- **Partial Success**: ${summary.partial}
- **Failed Batches**: ${summary.failed}

## Verification Results

- **Verification Passed**: ${summary.verificationPassed}
- **Verification Skipped**: ${summary.verificationSkipped}

## Batch Details

`;

    this.logs.forEach((log) => {
      reportContent += `### ${log.id}\n`;
      reportContent += `- Status: ${log.status}\n`;
      reportContent += `- Findings Applied: ${log.results.length}\n`;
      reportContent += `- Verification: ${log.verification?.overallStatus || "N/A"}\n\n`;
    });

    reportContent += `## Recommendations

1. Review batch results in BATCH_LOGS/ directory
2. Check CONSOLIDATED_PROPOSED_FIXES.md for details
3. Verify all changes with full test suite
4. Address any failed batches manually
5. Deploy changes following normal procedures

---
*End of Report*
`;

    return reportContent;
  }

  /**
   * Execute Phase 5: Final summary generation
   */
  execute() {
    console.log("\n==========================================");
    console.log("Phase 5: Final Summary");
    console.log("==========================================\n");

    this.loadBatchLogs();
    console.log(`Loaded ${this.logs.length} batch logs`);

    const summary = this.generateSummary();
    const summaryPath = "./FINAL_AUDIT_SUMMARY.md";
    fs.writeFileSync(summaryPath, summary);
    console.log(`\nFinal summary generated: ${summaryPath}`);

    console.log("\n==========================================");
    console.log("Phase 5 Complete");
    console.log("==========================================\n");

    return summaryPath;
  }
}

// Main execution
if (require.main === module) {
  const batchLogsDir = path.join(__dirname, "BATCH_LOGS");

  // Check if BATCH_LOGS directory exists
  if (!fs.existsSync(batchLogsDir)) {
    console.error(`Error: BATCH_LOGS directory not found at ${batchLogsDir}`);
    console.log("Please run Phase 4 (batch executor) before Phase 5");
    process.exit(1);
  }

  try {
    const generator = new FinalSummaryGenerator(batchLogsDir);
    const summaryPath = generator.execute();

    console.log(`✓ Summary generated successfully`);
    console.log(`✓ Output: ${summaryPath}`);
    console.log("\n==========================================");
    console.log("Audit Complete!");
    console.log("==========================================");
    console.log("\nNext steps:");
    console.log("1. Review CONSOLIDATED_PROPOSED_FIXES.md");
    console.log("2. Check BATCH_LOGS/ for execution details");
    console.log("3. Review FINAL_AUDIT_SUMMARY.md for overview");
    console.log("==========================================\n");

    process.exit(0);
  } catch (error) {
    console.error("Fatal error:", error.message);
    process.exit(1);
  }
}

module.exports = FinalSummaryGenerator;
