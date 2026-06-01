from app.core.supabase import supabase


class ScanRepository:

    @staticmethod
    def get_by_id(scan_id: str):
        response = (
            supabase
            .table("scans")
            .select("*")
            .eq("id", scan_id)
            .single()
            .execute()
        )

        return response.data

    @staticmethod
    def update_status(
        scan_id: str,
        status: str
    ):
        response = (
            supabase
            .table("scans")
            .update({
                "status": status
            })
            .eq("id", scan_id)
            .execute()
        )

        return response.data