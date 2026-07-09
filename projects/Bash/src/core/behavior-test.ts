#!/usr/bin/env bun
/**
 * Behavior Test Framework
 * Version: 1.0.0
 *
 * Validates behavior preservation during script migration
 *
 * Features:
 * - Input→output test cases
 * - Semantic equivalence verification
 * - Regression detection
 * - Test suite management
 */

import { deepEqual } from "assert";

// ─── Types ───────────────────────────────────────────────────────────

export interface BehaviorTest<I = any, O = any> {
  name: string;
  description?: string;
  input: I;
  expectedOutput: O;
  timeout?: number;
}

export interface TestResult {
  name: string;
  passed: boolean;
  error?: string;
  actualOutput?: any;
  expectedOutput?: any;
  duration: number;
}

export interface TestSuiteResult {
  total: number;
  passed: number;
  failed: number;
  duration: number;
  results: TestResult[];
}

export type Implementation<I = any, O = any> = (input: I) => Promise<O> | O;

// ─── Behavior Validator Class ────────────────────────────────────────

export class BehaviorValidator<I = any, O = any> {
  private tests: BehaviorTest<I, O>[] = [];
  private verbose: boolean;

  constructor(opts?: { verbose?: boolean }) {
    this.verbose = opts?.verbose || false;
  }

  /**
   * Add a test case
   */
  addTest(test: BehaviorTest<I, O>): void {
    this.tests.push(test);
  }

  /**
   * Add multiple test cases
   */
  addTests(tests: BehaviorTest<I, O>[]): void {
    this.tests.push(...tests);
  }

  /**
   * Clear all test cases
   */
  clearTests(): void {
    this.tests = [];
  }

  /**
   * Get all test cases
   */
  getTests(): BehaviorTest<I, O>[] {
    return [...this.tests];
  }

  /**
   * Run a single test
   */
  private async runTest(
    test: BehaviorTest<I, O>,
    implementation: Implementation<I, O>,
  ): Promise<TestResult> {
    const startTime = Date.now();
    const result: TestResult = {
      name: test.name,
      passed: false,
      duration: 0,
      expectedOutput: test.expectedOutput,
    };

    try {
      // Execute implementation with timeout
      const timeoutMs = test.timeout || 30000;
      const timeoutPromise = new Promise<never>((_, reject) =>
        setTimeout(() => reject(new Error("Test timeout")), timeoutMs),
      );

      const executionPromise = Promise.resolve(implementation(test.input));
      const actualOutput = await Promise.race([
        executionPromise,
        timeoutPromise,
      ]);

      result.actualOutput = actualOutput;

      // Compare outputs
      try {
        deepEqual(actualOutput, test.expectedOutput);
        result.passed = true;
      } catch (error) {
        result.passed = false;
        result.error = `Output mismatch: ${error}`;
      }
    } catch (error) {
      result.passed = false;
      result.error = `Execution error: ${error}`;
    }

    result.duration = Date.now() - startTime;

    if (this.verbose) {
      this.logTestResult(result);
    }

    return result;
  }

  /**
   * Log test result to console
   */
  private logTestResult(result: TestResult): void {
    const status = result.passed ? "✓" : "✗";
    const color = result.passed ? "\x1b[32m" : "\x1b[31m";
    const reset = "\x1b[0m";

    console.log(
      `${color}${status}${reset} ${result.name} (${result.duration}ms)`,
    );

    if (!result.passed && result.error) {
      console.log(`  Error: ${result.error}`);
      console.log(`  Expected:`, JSON.stringify(result.expectedOutput));
      console.log(`  Got:`, JSON.stringify(result.actualOutput));
    }
  }

  /**
   * Run all tests against an implementation
   */
  async validate(implementation: Implementation<I, O>): Promise<boolean> {
    const suiteResult = await this.runSuite(implementation);
    return suiteResult.failed === 0;
  }

  /**
   * Run full test suite
   */
  async runSuite(
    implementation: Implementation<I, O>,
  ): Promise<TestSuiteResult> {
    const startTime = Date.now();
    const results: TestResult[] = [];

    console.log(`\nRunning ${this.tests.length} test(s)...\n`);

    for (const test of this.tests) {
      const result = await this.runTest(test, implementation);
      results.push(result);
    }

    const duration = Date.now() - startTime;
    const passed = results.filter((r) => r.passed).length;
    const failed = results.filter((r) => !r.passed).length;

    const suiteResult: TestSuiteResult = {
      total: this.tests.length,
      passed,
      failed,
      duration,
      results,
    };

    this.logSuiteResult(suiteResult);

    return suiteResult;
  }

  /**
   * Log test suite summary
   */
  private logSuiteResult(result: TestSuiteResult): void {
    const color = result.failed === 0 ? "\x1b[32m" : "\x1b[31m";
    const reset = "\x1b[0m";

    console.log("\n" + "=".repeat(60));
    console.log("Test Suite Results:");
    console.log("=".repeat(60));
    console.log(`Total:    ${result.total}`);
    console.log(`${color}Passed:   ${result.passed}${reset}`);
    if (result.failed > 0) {
      console.log(`${color}Failed:   ${result.failed}${reset}`);
    }
    console.log(`Duration: ${result.duration}ms`);
    console.log("=".repeat(60) + "\n");
  }

  /**
   * Compare two implementations for behavior parity
   */
  async compareBehavior(
    originalImpl: Implementation<I, O>,
    newImpl: Implementation<I, O>,
  ): Promise<boolean> {
    console.log("\nComparing behavior between implementations...\n");

    let allMatched = true;

    for (const test of this.tests) {
      try {
        const originalOutput = await Promise.resolve(originalImpl(test.input));
        const newOutput = await Promise.resolve(newImpl(test.input));

        try {
          deepEqual(originalOutput, newOutput);
          if (this.verbose) {
            console.log(`✓ ${test.name}: Outputs match`);
          }
        } catch {
          console.error(`✗ ${test.name}: Output mismatch`);
          console.error(`  Original:`, JSON.stringify(originalOutput));
          console.error(`  New:`, JSON.stringify(newOutput));
          allMatched = false;
        }
      } catch (error) {
        console.error(`✗ ${test.name}: Execution error`);
        console.error(`  Error:`, error);
        allMatched = false;
      }
    }

    if (allMatched) {
      console.log("\n✓ All tests passed: Behavior parity confirmed\n");
    } else {
      console.log("\n✗ Some tests failed: Behavior divergence detected\n");
    }

    return allMatched;
  }
}

// ─── Test Suite Builder ──────────────────────────────────────────────

export class TestSuiteBuilder<I = any, O = any> {
  private validator: BehaviorValidator<I, O>;

  constructor() {
    this.validator = new BehaviorValidator<I, O>({ verbose: true });
  }

  /**
   * Add test case with fluent API
   */
  test(name: string, input: I, expectedOutput: O): this {
    this.validator.addTest({ name, input, expectedOutput });
    return this;
  }

  /**
   * Add test case with description
   */
  testWithDescription(
    name: string,
    description: string,
    input: I,
    expectedOutput: O,
  ): this {
    this.validator.addTest({ name, description, input, expectedOutput });
    return this;
  }

  /**
   * Build the validator
   */
  build(): BehaviorValidator<I, O> {
    return this.validator;
  }
}

// ─── Common Test Patterns ────────────────────────────────────────────

/**
 * Create test cases from input-output pairs
 */
export function createTestsFromPairs<I, O>(
  pairs: Array<[I, O]>,
  namePrefix = "test",
): BehaviorTest<I, O>[] {
  return pairs.map(([input, expectedOutput], index) => ({
    name: `${namePrefix}-${index + 1}`,
    input,
    expectedOutput,
  }));
}

/**
 * Capture behavior from existing implementation
 */
export async function captureBehavior<I, O>(
  implementation: Implementation<I, O>,
  inputs: I[],
): Promise<BehaviorTest<I, O>[]> {
  const tests: BehaviorTest<I, O>[] = [];

  for (let i = 0; i < inputs.length; i++) {
    const input = inputs[i]!;
    const output = await Promise.resolve(implementation(input));

    tests.push({
      name: `captured-test-${i + 1}`,
      input: input,
      expectedOutput: output,
    });
  }

  return tests;
}

/**
 * Validate migration with automatic test capture
 */
export async function validateMigration<I, O>(
  originalImpl: Implementation<I, O>,
  newImpl: Implementation<I, O>,
  testInputs: I[],
): Promise<boolean> {
  console.log("Step 1: Capturing original behavior...");
  const tests = await captureBehavior(originalImpl, testInputs);

  console.log(
    `Step 2: Validating new implementation (${tests.length} tests)...`,
  );
  const validator = new BehaviorValidator<I, O>({ verbose: true });
  validator.addTests(tests);

  return await validator.validate(newImpl);
}
