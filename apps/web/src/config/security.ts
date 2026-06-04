export const SECURITY = {
  MAX_UPLOAD_SIZE_MB: 10,

  ALLOWED_IMAGE_TYPES: [
    "image/png",
    "image/jpeg",
    "image/webp",
  ],

  MAX_SCANS_PER_HOUR: 50,
} as const;