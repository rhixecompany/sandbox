"use server";

import { auth } from "@/auth";
import { comicDal } from "@/dal/comic-dal";
import type { ActionResult } from "@/types/actions-types";

type ComicType = Awaited<ReturnType<typeof comicDal.list>>[number];

export async function getComicsAction(): Promise<ActionResult<ComicType[]>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") {
    return { ok: false, error: "Forbidden" };
  }
  try {
    const comics = await comicDal.list({ limit: 50 });
    return { ok: true, data: comics };
  } catch (error) {
    console.error("[getComicsAction]", error);
    return { ok: false, error: "Failed to fetch comics" };
  }
}
