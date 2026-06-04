import { createClient } from "@/lib/supabase/server";

export class ScanRepository {
  static async create(data: {
    organizationId: string;
    createdBy: string;
    scanType: string;
    filePath?: string;
    fileName?: string;
    fileSize?: number;
    mimeType?: string;
  }) {
    const supabase = await createClient();

    const { data: scan, error } = await supabase
      .from("scans")
      .insert({
        organization_id: data.organizationId,

        created_by: data.createdBy,

        scan_type: data.scanType,

        status: "uploaded",

        threat_score: 0,

        file_path: data.filePath,

        file_name: data.fileName,

        file_size: data.fileSize,

        mime_type: data.mimeType,
      })
      .select()
      .single();

    if (error) {
      throw error;
    }

    return scan;
  }

  static async getByUser(userId: string) {
    const supabase = await createClient();

    const { data, error } = await supabase
      .from("scans")
      .select("*")
      .eq("created_by", userId)
      .order("created_at", {
        ascending: false,
      });

    if (error) {
      throw error;
    }

    return data;
  }

  static async getByOrganization(organizationId: string) {
    const supabase = await createClient();

    const { data, error } = await supabase
      .from("scans")
      .select("*")
      .eq("organization_id", organizationId)
      .order("created_at", {
        ascending: false,
      });

    if (error) {
      throw error;
    }

    return data;
  }
}
