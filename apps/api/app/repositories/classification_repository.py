from app.core.supabase import supabase


class ClassificationRepository:

    @staticmethod
    def create(
        scan_id: str,
        scam_type: str,
        confidence: int,
        explanation: str,
    ):

        response = (
            supabase
            .table(
                "scan_classifications"
            )
            .insert({
                "scan_id": scan_id,
                "scam_type": scam_type,
                "confidence": confidence,
                "explanation": explanation,
            })
            .execute()
        )

        return response.data