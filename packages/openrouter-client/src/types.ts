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
  function: { name: string; arguments: string; };
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
