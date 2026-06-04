import { createClient } from "@/lib/supabase/server";

interface CreateScanInput {
  organizationId: string;
  userId: string;
  scanType: string;
  filePath: string;
  fileName: string;
  fileSize: number;
  mimeType: string;
}

export class ScansService {
  static async createScan(
    input: CreateScanInput
  ) {
    const supabase =
      await createClient();

    const { data, error } =
      await supabase
        .from("scans")
        .insert({
          organization_id:
            input.organizationId,

          created_by:
            input.userId,

          scan_type:
            input.scanType,

          status:
            "uploaded",

          threat_score:
            0,

          file_path:
            input.filePath,

          file_name:
            input.fileName,

          file_size:
            input.fileSize,

          mime_type:
            input.mimeType,
        })
        .select()
        .single();

    if (error) {
      throw error;
    }

    return data;
  }

  static async getScans() {
    const supabase =
      await createClient();

    const { data, error } =
      await supabase
        .from("scans")
        .select("*")
        .order(
          "created_at",
          {
            ascending: false,
          }
        );

    if (error) {
      throw error;
    }

    return data ?? [];
  }
}