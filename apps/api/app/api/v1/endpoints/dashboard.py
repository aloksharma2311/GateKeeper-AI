from fastapi import (
    APIRouter,
    Header,
)

from app.services.dashboard_service import (
    DashboardService,
)

router = APIRouter()


@router.get("/")
def dashboard(

    organization_id:
    str = Header(...)
):

    return (
        DashboardService
        .get_summary(
            organization_id
        )
    )