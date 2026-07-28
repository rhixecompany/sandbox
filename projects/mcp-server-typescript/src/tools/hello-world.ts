/**
 * greet — A friendly greeting tool
 *
 * Demonstrates string manipulation, optional parameters, and
 * enum-based style selection on the MCP tool interface.
 */

import { z } from "zod";

export const GreetArgsSchema = z.object({
  name: z.string().min(1, "Name is required").max(100, "Name too long"),
  title: z.string().max(50, "Title too long").optional(),
  style: z.enum(["casual", "formal", "enthusiastic"]).default("casual"),
});

type GreetArgs = z.infer<typeof GreetArgsSchema>;

/**
 * Build a greeting string based on style and optional title.
 */
export async function greetTool(
  args: Record<string, unknown>,
): Promise<{ content: Array<{ type: string; text: string }>; isError?: boolean }> {
  const parsed = args as GreetArgs;
  const displayName = parsed.title ? `${parsed.title} ${parsed.name}` : parsed.name;

  let greeting: string;
  switch (parsed.style) {
    case "formal":
      greeting = `Good day, ${displayName}. It is a pleasure to make your acquaintance.`;
      break;
    case "enthusiastic":
      greeting = `Hey there ${displayName}! 🌟 So great to see you today!`;
      break;
    case "casual":
    default:
      greeting = `Hello, ${displayName}! Welcome to the MCP server.`;
      break;
  }

  return {
    content: [
      {
        type: "text",
        text: JSON.stringify({ greeting, style: parsed.style, recipient: displayName }, null, 2),
      },
    ],
  };
}
