"""Scan History API Endpoints"""

from fastapi import APIRouter, HTTPException, status

from app.services.history_service import HistoryService
from app.utils.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()
history_service = HistoryService()


@router.get("/")
async def get_scan_history(
    skip: int = 0,
    limit: int = 20,
):
    """Get scan history."""
    try:
        history = await history_service.get_history(skip, limit)
        return history
    except Exception as e:
        logger.error(f"History retrieval error: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get("/{domain}/comparison")
async def compare_scans(domain: str):
    """Compare exposure changes over time."""
    try:
        logger.info(f"Comparing scans for domain {domain}")
        comparison = await history_service.compare_domain_scans(domain)
        return comparison
    except Exception as e:
        logger.error(f"Comparison error: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
