"""Report Generation API Endpoints"""

from fastapi import APIRouter, HTTPException, status, Query
from typing import Literal

from app.services.report_service import ReportService
from app.utils.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()
report_service = ReportService()


@router.get("/{scan_id}")
async def get_report(scan_id: str):
    """Get scan report."""
    try:
        logger.info(f"Generating report for scan {scan_id}")
        report = await report_service.generate_report(scan_id)
        return report
    except Exception as e:
        logger.error(f"Report generation error: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get("/{scan_id}/export")
async def export_report(
    scan_id: str,
    format: Literal["json", "html", "pdf"] = Query("json"),
):
    """Export report in specified format."""
    try:
        logger.info(f"Exporting report for scan {scan_id} as {format}")
        report_data = await report_service.export_report(scan_id, format)
        return report_data
    except Exception as e:
        logger.error(f"Report export error: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
