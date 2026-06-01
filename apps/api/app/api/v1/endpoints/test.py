from fastapi import APIRouter

from app.services.storage_service import StorageService

router = APIRouter()


@router.get("/download-test")
async def download_test():

    path = (
        "53c6b31b-7665-4a48-952d-b959c031c02b/"
        "4926afd0-ccd1-4455-bb25-20962893b500/"
        "original.jpg"
    )

    file_path = StorageService.download_scan(path)

    return {
        "downloaded_to": file_path
    }