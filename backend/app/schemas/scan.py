"""Scan Schemas"""

from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime


class ScanCreate(BaseModel):
    """Schema for creating a new scan."""
    target: str = Field(..., description="Target domain or URL")
    scan_type: Optional[str] = Field("full", description="Scan type: full, quick, custom")
    include_port_scan: bool = Field(True)
    include_screenshots: bool = Field(True)
    include_misconfiguration: bool = Field(True)
    config: Optional[Dict[str, Any]] = None


class ScanUpdate(BaseModel):
    """Schema for updating a scan."""
    status: Optional[str] = None
    error_message: Optional[str] = None


class ScanResponse(BaseModel):
    """Schema for scan response."""
    id: str
    target: str
    status: str
    scan_type: str
    total_endpoints: int
    critical_issues: int
    high_issues: int
    medium_issues: int
    low_issues: int
    severity_score: float
    started_at: datetime
    completed_at: Optional[datetime]
    error_message: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
