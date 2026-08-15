import { OpenRouterClient } from "./client";

/**
 * Send a chat completion request using the OpenRouter API.
 *
 * @param apiKey - Your OpenRouter API key
 * @param model - Model identifier (e.g., "openai/gpt-4o", "google/gemma-2-9b-it")
 * @param messages - Array of chat messages
 * @param options - Optional configuration (httpReferer, appTitle, stream, max_tokens, temperature)
 * @returns Promise resolving to a ChatCompletion response
 */
export interface SendChatOptions {
  httpReferer?: string;
  appTitle?: string;
  stream?: boolean;
  max_tokens?: number;
  temperature?: number;
}

export async function sendChat(
  apiKey: string,
  model: string,
  messages: import("./types").Message[],
  options?: SendChatOptions
): Promise<import("./types").ChatCompletion> {
  const client = new OpenRouterClient({
    apiKey,
    httpReferer: options?.httpReferer,
    appTitle: options?.appTitle,
  });

  return client.chatSend({
    model,
    messages,
    stream: options?.stream ?? false,
    max_tokens: options?.max_tokens,
    temperature: options?.temperature,
  });
}

export { OpenRouterClient } from "./client";
export type { ChatCompletion, Message, ModelChoice, OpenRouterClientConfig, SendChatOptions, ToolCall, Usage } from "./types";
