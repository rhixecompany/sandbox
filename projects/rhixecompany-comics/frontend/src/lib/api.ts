const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api";

export class ApiError extends Error {
  constructor(
    public status: number,
    message: string,
  ) {
    super(message);
    this.name = "ApiError";
  }
}

interface ApiOptions extends RequestInit {
  params?: Record<string, string | number | boolean | undefined>;
  signal?: AbortSignal;
}

async function request<T>(endpoint: string, options: ApiOptions = {}): Promise<T> {
  const { params, ...fetchOptions } = options;

  const url = new URL(`${API_BASE}${endpoint}`);
  if (params) {
    Object.entries(params).forEach(([key, value]) => {
      if (value !== undefined) {
        url.searchParams.append(key, String(value));
      }
    });
  }

  const headers: Record<string, string> = {
    "Content-Type": "application/json",
    ...(fetchOptions.headers as Record<string, string>),
  };

  const res = await fetch(url.toString(), {
    ...fetchOptions,
    headers,
  });

  if (!res.ok) {
    const text = await res.text().catch(() => "Unknown error");
    throw new ApiError(res.status, text);
  }

  return res.json();
}

export const api = {
  get<T>(endpoint: string, options?: ApiOptions) {
    return request<T>(endpoint, { ...options, method: "GET" });
  },
  post<T>(endpoint: string, body?: unknown, options?: ApiOptions) {
    return request<T>(endpoint, {
      ...options,
      method: "POST",
      body: body ? JSON.stringify(body) : undefined,
    });
  },
  put<T>(endpoint: string, body?: unknown, options?: ApiOptions) {
    return request<T>(endpoint, {
      ...options,
      method: "PUT",
      body: body ? JSON.stringify(body) : undefined,
    });
  },
  patch<T>(endpoint: string, body?: unknown, options?: ApiOptions) {
    return request<T>(endpoint, {
      ...options,
      method: "PATCH",
      body: body ? JSON.stringify(body) : undefined,
    });
  },
  delete<T>(endpoint: string, options?: ApiOptions) {
    return request<T>(endpoint, { ...options, method: "DELETE" });
  },
};

