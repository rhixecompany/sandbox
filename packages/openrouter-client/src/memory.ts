/**
 * Supermemory memory layer for openrouter-client.
 *
 * Optional, dependency-free (uses global fetch). Store exchanges with
 * taskType "memory" (POST /v3/documents) and retrieve context before the
 * model answers (POST /v4/search). Scoped to ONE singular containerTag —
 * format ^[a-zA-Z0-9_:-]+$, first write creates the tag, never cross-tag.
 *
 * The API key is read from process.env.SUPERMEMORY_API_KEY only. When it is
 * absent, every method is a no-op returning null/[] so the host app never
 * crashes and behavior stays backward compatible.
 */

export interface SupermemoryMemoryOptions {
	/** API base URL (default https://api.supermemory.ai) */
	apiBase?: string;
	/** Custom key provider; defaults to process.env.SUPERMEMORY_API_KEY */
	apiKey?: () => string | undefined;
	/** Per-request timeout in ms (default 15000) */
	timeoutMs?: number;
}

export interface MemorySearchResult {
	id?: string;
	content: string;
	score: number;
	source: "memory" | "document";
}

interface MessageLike {
	role: string;
	content: string;
}

const DEFAULT_API_BASE = "https://api.supermemory.ai";

function stableHash(input: string): string {
	let h1 = 0xdeadbeef ^ 0;
	let h2 = 0x41c6ce57 ^ 0;
	for (let i = 0; i < input.length; i++) {
		const ch = input.charCodeAt(i);
		h1 = Math.imul(h1 ^ ch, 2654435761);
		h2 = Math.imul(h2 ^ ch, 1597334677);
	}
	h1 = Math.imul(h1 ^ (h1 >>> 16), 2246822507) ^ Math.imul(h2 ^ (h2 >>> 13), 3266489909);
	h2 = Math.imul(h2 ^ (h2 >>> 16), 2246822507) ^ Math.imul(h1 ^ (h1 >>> 13), 3266489909);
	return (4294967296 * (2097151 & h2) + (h1 >>> 0)).toString(36).slice(0, 24);
}

export class SupermemoryMemory {
	private containerTag: string;
	private apiBase: string;
	private apiKey: () => string | undefined;
	private timeoutMs: number;

	constructor(containerTag: string, options: SupermemoryMemoryOptions = {}) {
		this.containerTag = containerTag;
		this.apiBase = options.apiBase ?? process.env.SUPERMEMORY_API_BASE ?? DEFAULT_API_BASE;
		this.apiKey = options.apiKey ?? (() => process.env.SUPERMEMORY_API_KEY);
		this.timeoutMs = options.timeoutMs ?? 15000;
	}

	/** True when SUPERMEMORY_API_KEY is present in the environment. */
	static isAvailable(): boolean {
		return Boolean(process.env.SUPERMEMORY_API_KEY);
	}

	/**
	 * Store one exchange (taskType "memory", full extraction pipeline).
	 * Returns the created document id, or null when the key is missing or the
	 * request fails (errors are swallowed — memory must never break chat).
	 */
	async storeExchange(
		role: "system" | "user" | "assistant" | "tool",
		content: string,
		metadata: Record<string, string> = {},
	): Promise<string | null> {
		const key = this.apiKey();
		if (!key || !content.trim()) return null;
		try {
			const customId = stableHash(`${this.containerTag}|${role}|${content}`);
			const body = {
				content: `${role}: ${content}`.slice(0, 100_000),
				containerTag: this.containerTag,
				taskType: "memory",
				customId,
				metadata: { role, ...metadata },
			};
			await this._post("/v3/documents", body, key);
			return customId;
		} catch {
			return null;
		}
	}

	/**
	 * Search prior context for a query (memories + documents).
	 * Returns normalized results, or [] when unavailable/failed.
	 */
	async searchContext(
		query: string,
		options: { limit?: number; searchMode?: "memories" | "documents" | "hybrid" } = {},
	): Promise<MemorySearchResult[]> {
		const key = this.apiKey();
		if (!key || !query.trim()) return [];
		try {
			const data = await this._post(
				"/v4/search",
				{
					q: query,
					containerTag: this.containerTag,
					searchMode: options.searchMode ?? "hybrid",
					limit: options.limit ?? 5,
				},
				key,
			);
			const results: MemorySearchResult[] = (data.results ?? []).map((r: any) => {
				const chunk = r.chunk ?? r.memory ?? r.content;
				return {
					id: r.id ?? r.memoryId ?? undefined,
					content: typeof chunk === "string" ? chunk : JSON.stringify(chunk),
					score: Number(r.similarity ?? r.score ?? 0),
					source: r.chunk ? "document" : "memory",
				};
			});
			return results.slice(0, options.limit ?? 5);
		} catch {
			return [];
		}
	}

	/** Turn search results into a compact system-context block. */
	static buildSystemContext(results: MemorySearchResult[], maxChars = 2000): string {
		if (results.length === 0) return "";
		let out = "Relevant prior context from memory:\n";
		let used = out.length;
		for (const r of results) {
			const line = `- [${r.source}·${r.score.toFixed(2)}] ${r.content}\n`;
			if (used + line.length > maxChars) break;
			out += line;
			used += line.length;
		}
		return out;
	}

	/**
	 * Inject retrieved context into a message list as (or merged into) the
	 * system message. Returns a NEW array; the input is not mutated.
	 */
	injectContext(
		messages: MessageLike[],
		query: string,
		options: { limit?: number; searchMode?: "memories" | "documents" | "hybrid" } = {},
	): Promise<MessageLike[]> {
		return (async () => {
			const results = await this.searchContext(query, options);
			const block = SupermemoryMemory.buildSystemContext(results);
			if (!block) return messages;
			const copy: MessageLike[] = [...messages];
			const sysIdx = copy.findIndex((m) => m.role === "system");
			if (sysIdx === -1) {
				copy.unshift({ role: "system", content: block });
			} else {
				copy[sysIdx] = { ...copy[sysIdx], content: `${copy[sysIdx].content}\n\n${block}` };
			}
			return copy;
		})();
	}

	private async _post(path: string, body: unknown, key: string): Promise<any> {
		const controller = new AbortController();
		const timer = setTimeout(() => controller.abort(), this.timeoutMs);
		try {
			const res = await fetch(`${this.apiBase}${path}`, {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
					Authorization: `Bearer ${key}`,
				},
				body: JSON.stringify(body),
				signal: controller.signal,
			});
			if (!res.ok) {
				throw new Error(`supermemory ${path} -> HTTP ${res.status}`);
			}
			return await res.json();
		} finally {
			clearTimeout(timer);
		}
	}
}

export default SupermemoryMemory;