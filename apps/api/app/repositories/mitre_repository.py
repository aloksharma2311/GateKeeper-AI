from app.core.supabase import supabase


class MitreRepository:

    @staticmethod
    def create(
        scan_id: str,
        technique_id: str,
        technique_name: str
    ):

        return (
            supabase
            .table(
                "mitre_techniques"
            )
            .insert(
                {
                    "scan_id": scan_id,
                    "technique_id": technique_id,
                    "technique_name": technique_name
                }
            )
            .execute()
        )

    @staticmethod
    def get_by_scan_id(
        scan_id: str
    ):

        result = (
            supabase
            .table(
                "mitre_techniques"
            )
            .select("*")
            .eq(
                "scan_id",
                scan_id
            )
            .execute()
        )

        return result.data or []