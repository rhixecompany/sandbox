/**
 * calculator — Arithmetic operations tool
 *
 * Handles add, subtract, multiply, divide, power, and modulo.
 * Includes edge-case handling for division by zero and overflow.
 */

import { z } from "zod";

export const CalculatorArgsSchema = z.object({
  a: z.number(),
  b: z.number(),
  operation: z.enum(["add", "subtract", "multiply", "divide", "power", "modulo"]),
});

type CalculatorArgs = z.infer<typeof CalculatorArgsSchema>;

/**
 * Execute an arithmetic operation with error handling.
 */
export async function calculatorTool(
  args: Record<string, unknown>,
): Promise<{ content: Array<{ type: string; text: string }>; isError?: boolean }> {
  const { a, b, operation } = args as CalculatorArgs;

  let result: number;
  let symbol: string;

  switch (operation) {
    case "add":
      result = a + b;
      symbol = "+";
      break;
    case "subtract":
      result = a - b;
      symbol = "−";
      break;
    case "multiply":
      result = a * b;
      symbol = "×";
      break;
    case "divide":
      if (b === 0) {
        return {
          content: [{ type: "text", text: "Error: Division by zero is not allowed." }],
          isError: true,
        };
      }
      result = a / b;
      symbol = "÷";
      break;
    case "power":
      if (a === 0 && b < 0) {
        return {
          content: [{ type: "text", text: "Error: Cannot raise zero to a negative power." }],
          isError: true,
        };
      }
      result = Math.pow(a, b);
      symbol = "^";
      break;
    case "modulo":
      if (b === 0) {
        return {
          content: [{ type: "text", text: "Error: Modulo by zero is not allowed." }],
          isError: true,
        };
      }
      result = a % b;
      symbol = "%";
      break;
  }

  if (!Number.isFinite(result)) {
    return {
      content: [{ type: "text", text: "Error: Result is not finite (overflow or undefined)." }],
      isError: true,
    };
  }

  return {
    content: [
      {
        type: "text",
        text: JSON.stringify({ expression: `${a} ${symbol} ${b}`, result, operation }, null, 2),
      },
    ],
  };
}
