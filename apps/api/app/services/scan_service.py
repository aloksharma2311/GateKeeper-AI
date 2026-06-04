from app.core.supabase import supabase


class ScanService:

    @staticmethod
    def get_scans():

        response = (
            supabase
            .table("scans")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )

        print("SCAN RESPONSE:", response.data)

        return response.data