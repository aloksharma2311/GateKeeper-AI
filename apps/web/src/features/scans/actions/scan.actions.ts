"use server";

import { createClient } from "@/lib/supabase/server";
import { ScanService } from "../services/scans.service";

export async function createTestScan() {
  const supabase = await createClient();

  const {
    data: { user },
  } = await supabase.auth.getUser();

  if (!user) {
    throw new Error("Unauthorized");
  }

  const { data: workspace } =
    await supabase
      .from("organizations")
      .select("*")
      .eq("owner_id", user.id)
      .single();

  return ScanService.createScan(
    workspace.id,
    user.id,
    "screenshot"
  );
}