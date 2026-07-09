import { describe, expect, it } from "vitest";
import { performTask } from "../templates/ts-module-template.js";

describe("performTask", () => {
  it("returns dry-run note when dryRun=true", async () => {
    const r = await performTask(" test ", { dryRun: true });
    expect(r.note).toBe("dry-run: no side effects");
  });

  it("executes when dryRun=false", async () => {
    const r = await performTask(" hello ", { dryRun: false });
    expect(r.note).toBe("executed");
  });
});
