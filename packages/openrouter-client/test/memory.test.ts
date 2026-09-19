// Tests for the optional Supermemory memory layer (src/memory.ts).

import { beforeEach, describe, expect, it, mock } from "bun:test";
import { sendChat, SupermemoryMemory, type Message } from "../src/index";

// Keep sendChat's downstream @openrouter/sdk call offline.
beforeEach(() => {
	mock.module("@openrouter/sdk", () => ({
		OpenRouter: class {
			constructor(_options: any) {}
			chat = {
				completions: {
					create: async (params: any) => ({
						id: "chatcmpl-mock",
						object: "chat.completion",
						created: 1234567890,
						model: params.model,
						choices: [
							{
								index: 0,
								message: { role: "assistant", content: "Mock reply" },
								finish_reason: "stop",
								logprobs: null,
							},
						],
						usage: { prompt_tokens: 5, completion_tokens: 3, total_tokens: 8 },
					}),
				},
			};
		},
	}));
});

describe("SupermemoryMemory", () => {
	beforeEach(() => {
		delete process.env.SUPERMEMORY_API_KEY;
	});

	describe("isAvailable", () => {
		it("is false without SUPERMEMORY_API_KEY", () => {
			expect(SupermemoryMemory.isAvailable()).toBe(false);
		});

		it("is true with SUPERMEMORY_API_KEY", () => {
			process.env.SUPERMEMORY_API_KEY = "sm_test";
			expect(SupermemoryMemory.isAvailable()).toBe(true);
		});
	});

	describe("with mocked fetch", () => {
		it("storeExchange POSTs to /v3/documents and returns a customId", async () => {
			process.env.SUPERMEMORY_API_KEY = "sm_test";
			const calls: Array<{ url: string; body: any }> = [];
			const originalFetch = globalThis.fetch;
			globalThis.fetch = (async (url: any, init: any) => {
				calls.push({ url: String(url), body: JSON.parse(init.body) });
				return new Response(JSON.stringify({ id: "doc_1", status: "queued" }), {
					status: 200,
					headers: { "Content-Type": "application/json" },
				});
			}) as typeof fetch;

			try {
				const mem = new SupermemoryMemory("user_123");
				const id = await mem.storeExchange("user", "Hello memory");
				expect(id).toBeTruthy();
				expect(calls).toHaveLength(1);
				expect(calls[0].url).toContain("/v3/documents");
				expect(calls[0].body.containerTag).toBe("user_123");
				expect(calls[0].body.taskType).toBe("memory");
				expect(calls[0].body.content).toContain("user: Hello memory");
			} finally {
				globalThis.fetch = originalFetch;
			}
		});

		it("searchContext normalizes v4/search results", async () => {
			process.env.SUPERMEMORY_API_KEY = "sm_test";
			const originalFetch = globalThis.fetch;
			globalThis.fetch = (async (_url: any, init: any) => {
				const body = JSON.parse(init.body);
				expect(body.q).toBe("dark mode");
				expect(body.containerTag).toBe("user_123");
				expect(body.searchMode).toBe("hybrid");
				return new Response(
					JSON.stringify({
						results: [
							{ id: "mem_1", memory: "user prefers dark mode", similarity: 0.9 },
							{ id: "doc_2", chunk: "settings page dark theme", similarity: 0.71 },
						],
					}),
					{ status: 200, headers: { "Content-Type": "application/json" } },
				);
			}) as typeof fetch;

			try {
				const mem = new SupermemoryMemory("user_123");
				const results = await mem.searchContext("dark mode");
				expect(results).toHaveLength(2);
				expect(results[0].source).toBe("memory");
				expect(results[1].source).toBe("document");
				expect(results[0].content).toContain("dark mode");
			} finally {
				globalThis.fetch = originalFetch;
			}
		});

		it("injectContext adds a system message when none exists", async () => {
			process.env.SUPERMEMORY_API_KEY = "sm_test";
			const originalFetch = globalThis.fetch;
			globalThis.fetch = (async () =>
				new Response(JSON.stringify({ results: [{ memory: "user likes coffee", similarity: 0.8 }] }), {
					status: 200,
					headers: { "Content-Type": "application/json" },
				})) as typeof fetch;

			try {
				const mem = new SupermemoryMemory("user_123");
				const out = await mem.injectContext([{ role: "user", content: "hi" }], "coffee");
				expect(out).toHaveLength(2);
				expect(out[0].role).toBe("system");
				expect(out[0].content).toContain("coffee");
			} finally {
				globalThis.fetch = originalFetch;
			}
		});

		it("returns no-op results when the key is missing", async () => {
			const mem = new SupermemoryMemory("user_123");
			expect(await mem.storeExchange("user", "x")).toBeNull();
			expect(await mem.searchContext("x")).toEqual([]);
		});
	});

	describe("sendChat with memory options", () => {
		it("still returns a completion and does not crash without a key", async () => {
			// No SUPERMEMORY_API_KEY set — memory paths must be transparent.
			const messages: Message[] = [{ role: "user", content: "Hello" }];
			const result = await sendChat("test-api-key", "openai/gpt-4o", messages, {
				memory: { containerTag: "user_123", store: true, inject: true },
			});
			expect(result).toBeDefined();
			expect(result.choices).toHaveLength(1);
		});
	});
});