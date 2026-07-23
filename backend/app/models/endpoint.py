"""Endpoint Model"""

from datetime import datetime
from enum import Enum
from sqlalchemy import Column, String, DateTime, Enum as SQLEnum, Integer, JSON
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database import Base


class EndpointStatus(str, Enum):
    """Endpoint HTTP status categories."""
    ACTIVE = "active"
    REDIRECT = "redirect"
    CLIENT_ERROR = "client_error"
    SERVER_ERROR = "server_error"
    TIMEOUT = "timeout"
    UNKNOWN = "unknown"


class Endpoint(Base):
    """HTTP endpoint discovered during scan."""

    __tablename__ = "endpoints"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    scan_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    
    url = Column(String, nullable=False, index=True)
    method = Column(String, default="GET")
    status_code = Column(Integer, nullable=True)
    
    content_length = Column(Integer, nullable=True)
    content_type = Column(String, nullable=True)
    response_time = Column(Integer, nullable=True)
    status = Column(SQLEnum(EndpointStatus), default=EndpointStatus.UNKNOWN)
    
    is_sensitive = Column(Integer, default=0)
    severity = Column(String)
    
    headers = Column(JSON, nullable=True)
    screenshot_path = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Endpoint {self.url} {self.status_code}>"
