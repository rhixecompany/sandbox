"use server";

import { auth } from "@/auth";
import { chapterDal } from "@/dal/chapter-dal";
import type { ActionResult } from "@/types/actions-types";

type ChapterType = Awaited<ReturnType<typeof chapterDal.list>>[number];

export async function getChaptersAction(): Promise<ActionResult<ChapterType[]>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") {
    return { ok: false, error: "Forbidden" };
  }
  try {
    const chapters = await chapterDal.list({ limit: 50 });
    return { ok: true, data: chapters };
  } catch (error) {
    console.error("[getChaptersAction]", error);
    return { ok: false, error: "Failed to fetch chapters" };
  }
}
