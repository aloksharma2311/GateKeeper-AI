from fastapi import APIRouter

from app.services.scan_service import ScanService
from app.services.scan_processor_service import (
    ScanProcessorService,
)

router = APIRouter()


@router.get("/")
async def get_scans():

    return ScanService.get_scans()


@router.post(
    "/process/{scan_id}"
)
async def process_scan(
    scan_id: str
):

    return (
        ScanProcessorService.process(
            scan_id
        )
    )