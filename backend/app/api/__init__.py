"""API Routes"""

from fastapi import APIRouter

from app.api.v1 import scans, scanners, reports, history

router = APIRouter()

router.include_router(scans.router, prefix="/scans", tags=["scans"])
router.include_router(scanners.router, prefix="/scanners", tags=["scanners"])
router.include_router(reports.router, prefix="/reports", tags=["reports"])
router.include_router(history.router, prefix="/history", tags=["history"])
