// Tests for openrouter-client (TypeScript package).

import { sendChat, OpenRouterClient, type Message } from "../src/index";

describe("openrouter-client", () => {
	describe("sendChat", () => {
		it("should return a ChatCompletion with a single user message", async () => {
			const messages: Message[] = [{ role: "user", content: "Hello, world!" }];

			const result = await sendChat("test-api-key", "openai/gpt-4o", messages);

			expect(result).toBeDefined();
			expect(result.id).toBeTruthy();
			expect(result.object).toBe("chat.completion");
			expect(result.choices).toHaveLength(1);
			expect(result.choices[0].message.role).toBe("assistant");
			expect(result.choices[0].finish_reason).toBe("stop");
			expect(result.usage).toBeDefined();
			expect(result.usage.total_tokens).toBeGreaterThan(0);
		});

		it("should pass httpReferer and appTitle to the client", async () => {
			const messages: Message[] = [{ role: "user", content: "Test message" }];

			const result = await sendChat("test-api-key", "google/gemma-2-9b-it", messages, {
				httpReferer: "https://example.com",
				appTitle: "My App",
			});

			expect(result).toBeDefined();
			expect(result.model).toBe("google/gemma-2-9b-it");
		});

		it("should handle empty messages array gracefully", async () => {
			const messages: Message[] = [];

			const result = await sendChat("test-api-key", "openai/gpt-4o", messages);

			expect(result).toBeDefined();
			expect(result.choices).toBeDefined();
		});
	});

	describe("OpenRouterClient", () => {
		it("should instantiate with config", () => {
			const config = {
				apiKey: "test-key",
				httpReferer: "https://example.com",
				appTitle: "Test App",
			};

			const client = new OpenRouterClient(config);
			expect(client).toBeDefined();
		});

		it("should have chatSend method", () => {
			const client = new OpenRouterClient({ apiKey: "test-key" });
			expect(typeof client.chatSend).toBe("function");
		});
	});
});
