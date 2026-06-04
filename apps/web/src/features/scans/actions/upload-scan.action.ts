"use server";

import { randomUUID } from "crypto";

import { createClient } from "@/lib/supabase/server";
import { ScansService } from "../services/scans.service";
import { StorageService } from "../services/storage.service";

import { revalidatePath } from "next/cache";

const MAX_FILE_SIZE = 10 * 1024 * 1024;

const ALLOWED_TYPES = ["image/png", "image/jpeg", "image/jpg", "image/webp"];

export async function uploadScreenshot(formData: FormData) {
  const file = formData.get("file") as File;

  if (!file) {
    throw new Error("No file provided");
  }

  if (file.size > MAX_FILE_SIZE) {
    throw new Error("File too large");
  }

  if (!ALLOWED_TYPES.includes(file.type)) {
    throw new Error("Invalid file type");
  }

  const supabase = await createClient();

  const {
    data: { user },
  } = await supabase.auth.getUser();

  if (!user) {
    throw new Error("Unauthorized");
  }

  const { data: workspace } = await supabase
    .from("organizations")
    .select("*")
    .eq("owner_id", user.id)
    .single();

  const scanId = randomUUID();

  const extension = file.name.split(".").pop();

  const filePath = `${workspace.id}/${scanId}/original.${extension}`;

  await StorageService.uploadScreenshot(filePath, file);

  const scan = await ScansService.createScan({
    organizationId: workspace.id,
    userId: user.id,
    scanType: "screenshot",
    filePath,
    fileName: file.name,
    fileSize: file.size,
    mimeType: file.type,
  });

  await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/api/v1/scans/process/${scan.id}`,
    {
      method: "POST",
    },
  );

  revalidatePath("/scans");

  return scan;
}
