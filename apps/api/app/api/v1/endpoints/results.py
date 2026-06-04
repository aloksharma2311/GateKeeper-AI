from fastapi import APIRouter

from app.repositories.scan_repository import (
    ScanRepository
)

router = APIRouter()


@router.get("/{scan_id}")
async def get_scan_results(
    scan_id: str
):
    return ScanRepository.get_full_scan(
        scan_id
    )