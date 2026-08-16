export interface OpenRouterClientConfig {
	apiKey: string;
	httpReferer?: string;
	appTitle?: string;
}

export interface Message {
	role: "system" | "user" | "assistant" | "tool";
	content: string;
	name?: string;
	tool_calls?: ToolCall[];
	tool_call_id?: string;
}

export interface ToolCall {
	id: string;
	type: "function";
	function: { name: string; arguments: string };
}

export interface ModelChoice {
	index: number;
	message: Message;
	logprobs?: number[];
	finish_reason: "stop" | "length" | "tool_calls" | "content_filter" | "null";
}

export interface Usage {
	prompt_tokens: number;
	completion_tokens: number;
	total_tokens: number;
}

export interface ChatCompletion {
	id: string;
	object: "chat.completion";
	created: number;
	model: string;
	choices: ModelChoice[];
	usage: Usage;
}

export class OpenRouterClient {
	private apiKey: string;
	private httpReferer?: string;
	private appTitle?: string;

	constructor(config: OpenRouterClientConfig) {
		this.apiKey = config.apiKey;
		this.httpReferer = config.httpReferer;
		this.appTitle = config.appTitle;
	}

	/**
	 * Send a chat completion request.
	 */
	async chatSend(params: {
		model: string;
		messages: Message[];
		stream?: boolean;
		max_tokens?: number;
		temperature?: number;
	}): Promise<ChatCompletion> {
		// Delegate to @openrouter/sdk
		const sdk = await import("@openrouter/sdk");
		const client = new sdk.OpenRouterClient(this.apiKey);

		const headers: Record<string, string> = {};
		if (this.httpReferer) headers["HTTP-Referer"] = this.httpReferer;
		if (this.appTitle) headers["X-Title"] = this.appTitle;

		const response = await client.chat.completions.create({
			model: params.model,
			messages: params.messages.map((m) => ({
				role: m.role,
				content: m.content,
				name: m.name,
				tool_calls: m.tool_calls,
				tool_call_id: m.tool_call_id,
			})),
			stream: params.stream ?? false,
			max_tokens: params.max_tokens,
			temperature: params.temperature,
			headers,
		});

		// Map SDK response to our ChatCompletion type
		const choices = response.choices.map((c) => ({
			index: c.index,
			message: c.message as Message,
			logprobs: c.logprobs,
			finish_reason: c.finish_reason as ChatCompletion["choices"][0]["finish_reason"],
		})) as ModelChoice[];

		const usage = response.usage as Usage;

		return {
			id: response.id,
			object: response.object,
			created: response.created,
			model: response.model,
			choices,
			usage,
		};
	}
}
