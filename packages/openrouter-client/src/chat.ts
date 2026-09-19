import { OpenRouterClient } from "./client";
import { SupermemoryMemory } from "./memory";

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
	/**
	 * Optional Supermemory integration (items 1+2 of the SandBox onboarding):
	 * - inject: search prior context (POST /v4/search) and prepend it to the
	 *   system message before the model answers (search-then-answer).
	 * - store: persist each user/assistant exchange (POST /v3/documents,
	 *   taskType "memory") so future sessions have memory.
	 * Requires SUPERMEMORY_API_KEY in the environment; absent key or any
	 * failure degrades to current behavior (no memory, no error).
	 */
	memory?: {
		containerTag: string;
		store?: boolean;
		inject?: boolean;
		searchQuery?: string;
		limit?: number;
		searchMode?: "memories" | "documents" | "hybrid";
	};
}

export async function sendChat(
	apiKey: string,
	model: string,
	messages: import("./types").Message[],
	options?: SendChatOptions,
): Promise<import("./types").ChatCompletion> {
	const client = new OpenRouterClient({
		apiKey,
		httpReferer: options?.httpReferer,
		appTitle: options?.appTitle,
	});

	// Search-then-answer: retrieve prior context and inject into the system turn.
	let chatMessages: import("./types").Message[] = messages;
	if (options?.memory?.inject) {
		try {
			const mem = new SupermemoryMemory(options.memory.containerTag);
			const lastUser =
				[...messages].reverse().find((m) => m.role === "user")?.content ?? "";
			const q = options.memory.searchQuery ?? lastUser;
			if (q) {
				chatMessages = (await mem.injectContext(chatMessages, q, {
					limit: options.memory.limit ?? 5,
					searchMode: options.memory.searchMode,
				})) as import("./types").Message[];
			}
		} catch {
			// Memory must never break chat — degrade silently.
		}
	}

	const response = await client.chatSend({
		model,
		messages: chatMessages,
		stream: options?.stream ?? false,
		max_tokens: options?.max_tokens,
		temperature: options?.temperature,
	});

	// Store the exchange for future sessions (best effort, non-blocking).
	if (options?.memory?.store) {
		try {
			const mem = new SupermemoryMemory(options.memory.containerTag);
			for (const m of messages) {
				if (m.role === "user" || m.role === "assistant") {
					await mem.storeExchange(m.role, m.content);
				}
			}
		} catch {
			// Best effort only.
		}
	}

	return response;
}

export { OpenRouterClient } from "./client";
export type {
	ChatCompletion,
	Message,
	ModelChoice,
	OpenRouterClientConfig,
	SendChatOptions,
	ToolCall,
	Usage,
} from "./types";
