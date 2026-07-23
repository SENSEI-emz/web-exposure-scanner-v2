"""Scan Service"""

from typing import Optional, List
from uuid import UUID
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.scan import Scan, ScanStatus
from app.schemas.scan import ScanCreate
from app.utils.logger import get_logger

logger = get_logger(__name__)


class ScanService:
    """Service for scan operations."""

    async def create_scan(
        self,
        scan_data: ScanCreate,
        db: AsyncSession,
    ) -> Scan:
        """Create new scan."""
        scan = Scan(
            target=scan_data.target,
            status=ScanStatus.PENDING,
            scan_type=scan_data.scan_type,
            include_port_scan=scan_data.include_port_scan,
            include_screenshots=scan_data.include_screenshots,
            include_misconfiguration=scan_data.include_misconfiguration,
            config=scan_data.config,
        )
        db.add(scan)
        await db.commit()
        await db.refresh(scan)
        return scan

    async def get_scan(
        self,
        scan_id: str,
        db: AsyncSession,
    ) -> Optional[Scan]:
        """Get scan by ID."""
        result = await db.execute(
            select(Scan).where(Scan.id == UUID(scan_id))
        )
        return result.scalar_one_or_none()

    async def list_scans(
        self,
        db: AsyncSession,
        skip: int = 0,
        limit: int = 10,
    ) -> List[Scan]:
        """List scans with pagination."""
        result = await db.execute(
            select(Scan)
            .order_by(desc(Scan.created_at))
            .offset(skip)
            .limit(limit)
        )
        return result.scalars().all()

    async def stop_scan(
        self,
        scan_id: str,
        db: AsyncSession,
    ) -> Scan:
        """Stop running scan."""
        scan = await self.get_scan(scan_id, db)
        if not scan:
            raise ValueError("Scan not found")

        scan.status = ScanStatus.STOPPED
        await db.commit()
        await db.refresh(scan)
        return scan
