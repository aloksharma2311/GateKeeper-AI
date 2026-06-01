from app.core.supabase import supabase


class OCRResultRepository:

    @staticmethod
    def create(
        scan_id: str,
        extracted_text: str
    ):
        response = (
            supabase
            .table("ocr_results")
            .insert({
                "scan_id": scan_id,
                "extracted_text": extracted_text
            })
            .execute()
        )

        return response.data