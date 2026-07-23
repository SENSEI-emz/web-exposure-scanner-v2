"""Report Schemas"""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from datetime import datetime


class ReportResponse(BaseModel):
    """Schema for report response."""
    scan_id: str
    target: str
    scan_date: datetime
    status: str
    
    total_endpoints: int
    total_vulnerabilities: int
    critical_count: int
    high_count: int
    medium_count: int
    low_count: int
    info_count: int
    
    endpoints: List[Dict[str, Any]]
    vulnerabilities: List[Dict[str, Any]]
    recommendations: List[str]
    
    severity_score: float
    execution_time: float
