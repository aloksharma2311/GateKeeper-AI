from app.core.supabase import supabase


class ReportRepository:

    @staticmethod
    def create(
        scan_id: str,
        summary: str,
        verdict: str,
        confidence: int,
        risk_level: str,
        attack_vectors,
        recommended_actions
    ):

        result = (
            supabase
            .table("reports")
            .insert(
                {
                    "scan_id": scan_id,
                    "summary": summary,
                    "verdict": verdict,
                    "confidence": confidence,
                    "risk_level": risk_level,
                    "attack_vectors": attack_vectors,
                    "recommended_actions": recommended_actions
                }
            )
            .execute()
        )

        return result.data