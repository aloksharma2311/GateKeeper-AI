from fastapi import APIRouter

from app.api.v1.endpoints.health import router as health_router
from app.api.v1.endpoints.scans import router as scans_router
from app.api.v1.endpoints.test import router as test_router
from app.api.v1.endpoints.results import (
    router as results_router
)
from app.api.v1.endpoints.dashboard import (
    router as dashboard_router
)

from app.api.v1.endpoints import reports
router = APIRouter()

router.include_router(
    health_router,
    prefix="/health",
    tags=["Health"],
)

router.include_router(
    scans_router,
    prefix="/scans",
    tags=["Scans"],
)

router.include_router(
    test_router,
    prefix="/test",
    tags=["Test"],
)

router.include_router(
    results_router,
    prefix="/results",
    tags=["Results"]
)

router.include_router(
    dashboard_router,
    prefix="/dashboard",
    tags=["dashboard"]
)

router.include_router(
    reports.router,
    prefix="/reports",
    tags=["Reports"]
)