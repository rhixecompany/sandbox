"use server";

import { auth } from "@/auth";
import { typeDal } from "@/dal/type-dal";
import type { ActionResult } from "@/types/actions-types";

type ComicTypeType = Awaited<ReturnType<typeof typeDal.list>>[number];

export async function getTypesAction(): Promise<ActionResult<ComicTypeType[]>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") {
    return { ok: false, error: "Forbidden" };
  }
  try {
    const types = await typeDal.list({ limit: 50 });
    return { ok: true, data: types };
  } catch (error) {
    console.error("[getTypesAction]", error);
    return { ok: false, error: "Failed to fetch types" };
  }
}
