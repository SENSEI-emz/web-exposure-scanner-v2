"""Scan API Endpoints"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc

from app.database import get_db
from app.models.scan import Scan, ScanStatus
from app.schemas.scan import ScanCreate, ScanResponse
from app.services.scan_service import ScanService
from app.utils.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()
scan_service = ScanService()


@router.post("/", response_model=ScanResponse, status_code=status.HTTP_201_CREATED)
async def create_scan(
    scan_data: ScanCreate,
    db: AsyncSession = Depends(get_db),
):
    """Start a new scan."""
    try:
        scan = await scan_service.create_scan(scan_data, db)
        logger.info(f"Scan created: {scan.id} for target {scan.target}")
        return scan
    except Exception as e:
        logger.error(f"Error creating scan: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get("/{scan_id}", response_model=ScanResponse)
async def get_scan(
    scan_id: str,
    db: AsyncSession = Depends(get_db),
):
    """Get scan details."""
    try:
        scan = await scan_service.get_scan(scan_id, db)
        if not scan:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Scan not found",
            )
        return scan
    except Exception as e:
        logger.error(f"Error getting scan: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get("/", response_model=List[ScanResponse])
async def list_scans(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db),
):
    """List all scans."""
    try:
        scans = await scan_service.list_scans(db, skip, limit)
        return scans
    except Exception as e:
        logger.error(f"Error listing scans: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.post("/{scan_id}/stop", status_code=status.HTTP_200_OK)
async def stop_scan(
    scan_id: str,
    db: AsyncSession = Depends(get_db),
):
    """Stop active scan."""
    try:
        scan = await scan_service.stop_scan(scan_id, db)
        logger.info(f"Scan stopped: {scan_id}")
        return {"status": "stopped", "scan_id": scan_id}
    except Exception as e:
        logger.error(f"Error stopping scan: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
