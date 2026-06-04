from app.core.supabase import supabase


class ThreatFindingRepository:

    @staticmethod
    def create(
        scan_id: str,
        finding_type: str,
        finding_value: str,
        confidence: int = 100
    ):

        return (
            supabase.table("threat_findings")
            .insert(
                {
                    "scan_id": scan_id,
                    "finding_type": finding_type,
                    "finding_value": finding_value,
                    "confidence": confidence,
                }
            )
            .execute()
        )