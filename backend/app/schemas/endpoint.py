"""Endpoint Schemas"""

from typing import Optional, Dict, Any
from pydantic import BaseModel
from datetime import datetime


class EndpointResponse(BaseModel):
    """Schema for endpoint response."""
    id: str
    scan_id: str
    url: str
    method: str
    status_code: Optional[int]
    content_type: Optional[str]
    response_time: Optional[int]
    is_sensitive: bool
    severity: Optional[str]
    headers: Optional[Dict[str, Any]]
    screenshot_path: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
