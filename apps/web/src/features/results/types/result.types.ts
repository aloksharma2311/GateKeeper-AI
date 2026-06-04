export interface Finding {
  id: string;
  finding_type: string;
  finding_value: string;
  confidence: number;
}

export interface OCRResult {
  extracted_text: string;
}

export interface ScanResult {
  scan: {
    id: string;
    status: string;
    threat_score: number;
  };

  ocr: OCRResult | null;

  findings: Finding[];
}