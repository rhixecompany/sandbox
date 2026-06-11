import { vi } from "vitest";

// Mock comic data for SearchDAL tests
const mockComics = [
  {
    id: 1,
    title: "Test Comic",
    description: "A test comic with searchable content",
    slug: "test-comic",
    synopsis: "Test synopsis",
    coverImage: "cover.jpg",
    rating: 4.5,
    status: "Ongoing" as const,
    createdAt: new Date(),
    updatedAt: new Date(),
    deletedAt: null,
    authorId: 1,
    artistId: 1,
    typeId: 1,
    author: { id: 1, name: "Test Author" },
    artist: { id: 1, name: "Test Artist" },
    genres: [{ genre: { id: 1, name: "Action" } }],
    type: { id: 1, name: "Manga" },
  },
  {
    id: 2,
    title: "Another Comic",
    description: "Another test comic for pagination testing",
    slug: "another-comic",
    synopsis: "Another test synopsis",
    coverImage: "cover2.jpg",
    rating: 3.8,
    status: "Completed" as const,
    createdAt: new Date(),
    updatedAt: new Date(),
    deletedAt: null,
    authorId: 2,
    artistId: 2,
    typeId: 1,
    author: { id: 2, name: "Test Author 2" },
    artist: { id: 2, name: "Test Artist 2" },
    genres: [{ genre: { id: 2, name: "Drama" } }],
    type: { id: 1, name: "Manga" },
  },
];

// Helper type for mock filter conditions
interface MockCondition {
  __mockType: string;
  columnName?: string;
  conditions?: MockCondition[];
  pattern?: string;
  value?: unknown;
}

// Filter mockComics by traversing mock condition objects
function applyMockFilter(items: typeof mockComics, where: MockCondition | undefined): typeof mockComics {
  if (!where || !where.__mockType) return items;

  if (where.__mockType === "ilike") {
    const pattern = (where.pattern ?? "").replaceAll("%", "").toLowerCase();
    const col = where.columnName;
    if (!col) return items;
    return items.filter((item) => {
      const val = item[col as keyof typeof item];
      // eslint-disable-next-line @typescript-eslint/no-base-to-string
      return val !== null && val !== undefined && String(val).toLowerCase().includes(pattern);
    });
  }

  if (where.__mockType === "eq") {
    const col = where.columnName;
    if (!col) return items;
    return items.filter((item) => item[col as keyof typeof item] === where.value);
  }

  if (where.__mockType === "and") {
    let result = items;
    for (const condition of where.conditions ?? []) {
      result = applyMockFilter(result, condition);
    }
    return result;
  }

  if (where.__mockType === "or") {
    const sets = (where.conditions ?? []).map((c) => applyMockFilter(items, c));
    const union = new Set<(typeof mockComics)[number]>();
    for (const set of sets) {
      for (const item of set) union.add(item);
    }
    return [...union];
  }

  return items;
}

// Mock drizzle-orm operators to return parseable condition objects
vi.mock("drizzle-orm", async () => {
  const actual = await vi.importActual<typeof import("drizzle-orm")>("drizzle-orm");
  return {
    ...actual,
    count: vi.fn().mockReturnValue({ _: "mock" }),
    ilike: vi.fn(
      (column: { name?: string }, pattern: string): MockCondition => ({
        __mockType: "ilike",
        // eslint-disable-next-line @typescript-eslint/no-base-to-string
        columnName: column?.name ?? String(column),
        pattern,
      })
    ),
    eq: vi.fn(
      (column: { name?: string }, value: unknown): MockCondition => ({
        __mockType: "eq",
        // eslint-disable-next-line @typescript-eslint/no-base-to-string
        columnName: column?.name ?? String(column),
        value,
      })
    ),
    and: vi.fn(
      (...conditions: (MockCondition | undefined)[]): MockCondition => ({
        __mockType: "and",
        conditions: conditions.filter(Boolean) as MockCondition[],
      })
    ),
    or: vi.fn(
      (...conditions: (MockCondition | undefined)[]): MockCondition => ({
        __mockType: "or",
        conditions: conditions.filter(Boolean) as MockCondition[],
      })
    ),
  };
});

// Mock database with proper implementations
vi.mock("@/database/db", () => {
  const createMockDb = () => {
    const mockDb: Record<string, unknown> = {};

    mockDb.select = vi.fn(() => ({
      from: vi.fn(() => ({
        where: vi.fn((condition: MockCondition) => {
          const filtered = applyMockFilter(mockComics, condition);
          return Promise.resolve([{ count: filtered.length }]);
        }),
      })),
    }));
    mockDb.from = vi.fn(() => ({
      where: vi.fn(() => mockDb),
    }));
    mockDb.where = vi.fn(() => mockDb);
    mockDb.limit = vi.fn(() => mockDb);
    mockDb.offset = vi.fn(() => mockDb);
    mockDb.insert = vi.fn(() => ({
      values: vi.fn(() => ({
        returning: vi.fn().mockResolvedValue([]),
      })),
    }));
    mockDb.update = vi.fn(() => ({
      set: vi.fn(() => ({
        where: vi.fn(() => ({
          returning: vi.fn().mockResolvedValue([]),
        })),
      })),
    }));
    mockDb.delete = vi.fn(() => ({
      where: vi.fn(() => ({
        returning: vi.fn().mockResolvedValue([]),
      })),
    }));
    mockDb.query = {
      comic: {
        findMany: vi.fn((options?: Record<string, unknown>) => {
          let results = applyMockFilter(mockComics, options?.where as MockCondition | undefined);

          // Apply offset pagination
          if (options?.offset && typeof options.offset === "number") {
            results = results.slice(options.offset);
          }

          // Apply limit
          if (options?.limit && typeof options.limit === "number") {
            results = results.slice(0, options.limit);
          }

          return results;
        }),
        findFirst: vi.fn().mockResolvedValue(mockComics[0]),
      },
      chapter: {
        findMany: vi.fn().mockResolvedValue([]),
        findFirst: vi.fn().mockResolvedValue(null),
      },
      bookmark: {
        findMany: vi.fn().mockResolvedValue([]),
        findFirst: vi.fn().mockResolvedValue(null),
      },
    };

    return mockDb;
  };

  return { db: createMockDb() };
});

// Mock next/cache
vi.mock("next/cache", () => ({
  revalidatePath: vi.fn(),
  revalidateTag: vi.fn(),
}));

// Mock next/server
vi.mock("next/server", () => ({
  redirect: vi.fn(),
  notFound: vi.fn(),
}));

// Mock next/navigation
vi.mock("next/navigation", () => ({
  useRouter: vi.fn(),
  useSearchParams: vi.fn(),
  usePathname: vi.fn(),
  redirect: vi.fn(),
  notFound: vi.fn(),
}));

// Mock auth
vi.mock("@/auth", () => ({
  auth: vi.fn().mockResolvedValue({
    user: { id: "test-user-id", email: "test@example.com", role: "user" },
  }),
}));
