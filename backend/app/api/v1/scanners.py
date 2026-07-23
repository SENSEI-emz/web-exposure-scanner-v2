"""Scanner Module API Endpoints"""

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Dict, Any

from app.services.scanner_service import ScannerService
from app.utils.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()
scanner_service = ScannerService()


class ScannerRequest(BaseModel):
    """Scanner request payload."""
    target: str
    options: Dict[str, Any] = {}


@router.post("/subdomain")
async def run_subdomain_scanner(request: ScannerRequest):
    """Run subdomain enumeration."""
    try:
        logger.info(f"Starting subdomain scan for {request.target}")
        results = await scanner_service.run_subdomain_scanner(request.target, request.options)
        return {"status": "success", "results": results}
    except Exception as e:
        logger.error(f"Subdomain scanner error: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.post("/directory")
async def run_directory_scanner(request: ScannerRequest):
    """Run directory brute-forcing."""
    try:
        logger.info(f"Starting directory scan for {request.target}")
        results = await scanner_service.run_directory_scanner(request.target, request.options)
        return {"status": "success", "results": results}
    except Exception as e:
        logger.error(f"Directory scanner error: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.post("/port")
async def run_port_scanner(request: ScannerRequest):
    """Run port scanning."""
    try:
        logger.info(f"Starting port scan for {request.target}")
        results = await scanner_service.run_port_scanner(request.target, request.options)
        return {"status": "success", "results": results}
    except Exception as e:
        logger.error(f"Port scanner error: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.post("/misconfiguration")
async def run_misconfiguration_check(request: ScannerRequest):
    """Check for misconfigurations."""
    try:
        logger.info(f"Starting misconfiguration check for {request.target}")
        results = await scanner_service.run_misconfiguration_check(request.target, request.options)
        return {"status": "success", "results": results}
    except Exception as e:
        logger.error(f"Misconfiguration check error: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
