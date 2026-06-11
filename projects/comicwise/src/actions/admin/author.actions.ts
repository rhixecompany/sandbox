"use server";

import { auth } from "@/auth";
import { authorDal } from "@/dal/author-dal";
import type { ActionResult } from "@/types/actions-types";

type AuthorType = Awaited<ReturnType<typeof authorDal.list>>[number];

export async function getAuthorsAction(): Promise<ActionResult<AuthorType[]>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") {
    return { ok: false, error: "Forbidden" };
  }
  try {
    const authors = await authorDal.list({ limit: 50 });
    return { ok: true, data: authors };
  } catch (error) {
    console.error("[getAuthorsAction]", error);
    return { ok: false, error: "Failed to fetch authors" };
  }
}
