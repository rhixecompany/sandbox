"use server";

import { auth } from "@/auth";
import { artistDal } from "@/dal/artist-dal";
import type { ActionResult } from "@/types/actions-types";

type ArtistType = Awaited<ReturnType<typeof artistDal.list>>[number];

export async function getArtistsAction(): Promise<ActionResult<ArtistType[]>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") {
    return { ok: false, error: "Forbidden" };
  }
  try {
    const artists = await artistDal.list({ limit: 50 });
    return { ok: true, data: artists };
  } catch (error) {
    console.error("[getArtistsAction]", error);
    return { ok: false, error: "Failed to fetch artists" };
  }
}
