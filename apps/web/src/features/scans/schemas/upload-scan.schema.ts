import { z } from "zod";

export const UploadScanSchema =
  z.object({
    scanType: z.enum([
      "screenshot",
      "url",
      "message",
      "job_offer",
    ]),
  });

export type UploadScanInput =
  z.infer<typeof UploadScanSchema>;