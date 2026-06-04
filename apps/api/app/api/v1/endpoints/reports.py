from fastapi import APIRouter
from app.core.supabase import supabase

router = APIRouter()


@router.get("/{scan_id}")
def get_report(
    scan_id: str
):

    result = (
        supabase
        .table("reports")
        .select("*")
        .eq(
            "scan_id",
            scan_id
        )
        .execute()
    )

    if not result.data:
        return {
            "message":
            "Report not found"
        }

    return result.data[0]