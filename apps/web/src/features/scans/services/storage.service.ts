import { createClient } from "@/lib/supabase/server";

export class StorageService {
  static async uploadScreenshot(
    path: string,
    file: File
  ) {
    const supabase = await createClient();

    const { error } =
      await supabase.storage
        .from(
          process.env.NEXT_PUBLIC_SCAN_BUCKET!
        )
        .upload(path, file, {
          upsert: false,
          contentType: file.type,
        });

    if (error) {
      throw error;
    }

    return path;
  }
}