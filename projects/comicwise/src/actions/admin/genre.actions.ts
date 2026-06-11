"use server";

import { auth } from "@/auth";
import { genreDal } from "@/dal/genre-dal";
import type { ActionResult } from "@/types/actions-types";

type GenreType = Awaited<ReturnType<typeof genreDal.list>>[number];

export async function getGenresAction(): Promise<ActionResult<GenreType[]>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") {
    return { ok: false, error: "Forbidden" };
  }
  try {
    const genres = await genreDal.list({ limit: 100 });
    return { ok: true, data: genres };
  } catch (error) {
    console.error("[getGenresAction]", error);
    return { ok: false, error: "Failed to fetch genres" };
  }
}
