from fastapi import APIRouter

from app.services.scan_service import ScanService

router = APIRouter()


@router.get("/")
async def get_scans():

    scans = ScanService.get_scans()

    return scans


@router.post("/process")
async def process_scan():

    return {
        "message": "scan processing placeholder"
    }