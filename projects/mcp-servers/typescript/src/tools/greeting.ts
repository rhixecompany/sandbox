import { z } from "zod";

/**
 * Schema for the greeting tool input parameters.
 */
export const GreetingInputSchema = z.object({
  name: z
    .string()
    .min(1, "Name is required")
    .max(100, "Name must be 100 characters or fewer"),
  title: z
    .string()
    .optional()
    .default("")
    .describe("Optional title (e.g., Dr., Prof., Esq.)"),
  tone: z
    .enum(["friendly", "formal", "enthusiastic"])
    .optional()
    .default("friendly")
    .describe("The tone of the greeting"),
});

export type GreetingInput = z.infer<typeof GreetingInputSchema>;

/**
 * Generates a personalized greeting based on the provided input parameters.
 * Supported tones: friendly, formal, enthusiastic.
 */
export function generateGreeting(input: GreetingInput): string {
  const { name, title, tone } = input;
  const prefix = title ? `${title} ` : "";

  switch (tone) {
    case "formal":
      return `Greetings, ${prefix}${name}. It is a pleasure to make your acquaintance.`;
    case "enthusiastic":
      return `Hey ${prefix}${name}! So great to see you — let's get things done! 🚀`;
    case "friendly":
    default:
      return `Hello, ${prefix}${name}! Welcome to the MCP server. How can I help you today?`;
  }
}
