import { describe, expect, it } from "vitest";

import { createComicSchema } from "@/schemas/comic.schema";

describe("CreateComicSchema", () => {
  it("accepts valid comic data", () => {
    const result = createComicSchema.safeParse({
      title: "My Comic",
      slug: "my-comic",
      status: "Ongoing",
      description: "A great comic that is long enough",
      type: "manga",
    });
    expect(result.success).toBe(true);
  });

  it("rejects empty title", () => {
    const result = createComicSchema.safeParse({
      title: "",
      slug: "my-comic",
      status: "Ongoing",
      description: "A great comic that is long enough",
      type: "manga",
    });
    expect(result.success).toBe(false);
  });

  it("rejects invalid status", () => {
    const result = createComicSchema.safeParse({
      title: "Test",
      slug: "test",
      status: "Invalid",
      description: "A great comic that is long enough",
      type: "manga",
    });
    expect(result.success).toBe(false);
  });
});
