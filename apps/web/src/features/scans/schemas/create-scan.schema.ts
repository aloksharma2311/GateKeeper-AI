import { z } from "zod";

export const CreateScanSchema = z.object({
  scanType: z.enum([
    "screenshot",
    "url",
    "message",
    "job_offer",
  ]),
});

export type CreateScanInput =
  z.infer<typeof CreateScanSchema>;