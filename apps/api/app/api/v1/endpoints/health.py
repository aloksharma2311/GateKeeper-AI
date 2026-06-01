from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def health():
    return {
        "status": "healthy",
        "service": "gatekeeper-api",
        "version": "1.0.0",
    }