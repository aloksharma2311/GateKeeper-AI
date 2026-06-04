"use server";

import { createClient } from "@/lib/supabase/server";
import { ScansService } from "../services/scans.service";

export async function createTestScan() {
  const supabase = await createClient();

  const {
    data: { user },
  } = await supabase.auth.getUser();

  if (!user) {
    throw new Error("Unauthorized");
  }

  const { data: workspace, error } =
    await supabase
      .from("organizations")
      .select("*")
      .eq("owner_id", user.id)
      .single();

  if (error || !workspace) {
    throw new Error("Workspace not found");
  }

  return await ScansService.createScan({
  organizationId: workspace.id,
  userId: user.id,
  scanType: "screenshot",
  filePath: "test.png",
  fileName: "test.png",
  fileSize: 0,
  mimeType: "image/png",
});
}