import { z } from "zod";

/**
 * Schema for the calculator tool input parameters.
 * Supports basic arithmetic: add, subtract, multiply, divide, power, modulo.
 */
export const CalculatorInputSchema = z.object({
  operation: z.enum(["add", "subtract", "multiply", "divide", "power", "modulo"], {
    description: "The arithmetic operation to perform",
  }),
  a: z.number({ description: "First operand" }),
  b: z.number({ description: "Second operand" }),
});

export type CalculatorInput = z.infer<typeof CalculatorInputSchema>;

/**
 * Result type returned by the calculator.
 */
export interface CalculatorResult {
  operation: string;
  a: number;
  b: number;
  result: number | string;
}

/**
 * Performs the requested arithmetic operation on two operands.
 * Returns the numeric result on success, or an error message string for
 * division-by-zero and similar edge cases.
 */
export function calculate(input: CalculatorInput): CalculatorResult {
  const { operation, a, b } = input;

  let result: number | string;

  switch (operation) {
    case "add":
      result = a + b;
      break;
    case "subtract":
      result = a - b;
      break;
    case "multiply":
      result = a * b;
      break;
    case "divide":
      if (b === 0) {
        result = "Error: Division by zero is not allowed";
      } else {
        result = a / b;
      }
      break;
    case "power":
      result = Math.pow(a, b);
      break;
    case "modulo":
      if (b === 0) {
        result = "Error: Modulo by zero is not allowed";
      } else {
        result = a % b;
      }
      break;
    default:
      result = `Error: Unknown operation '${operation}'`;
  }

  return { operation, a, b, result };
}
