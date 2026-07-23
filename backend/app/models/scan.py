"""Scan Model"""

from datetime import datetime
from enum import Enum
from sqlalchemy import Column, String, DateTime, Enum as SQLEnum, JSON, Integer, Float
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database import Base


class ScanStatus(str, Enum):
    """Scan status enumeration."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    STOPPED = "stopped"


class Scan(Base):
    """Scan model representing a complete scanning operation."""

    __tablename__ = "scans"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    target = Column(String, nullable=False, index=True)
    status = Column(SQLEnum(ScanStatus), default=ScanStatus.PENDING)
    
    scan_type = Column(String, default="full")
    include_port_scan = Column(Integer, default=1)
    include_screenshots = Column(Integer, default=1)
    include_misconfiguration = Column(Integer, default=1)
    
    total_endpoints = Column(Integer, default=0)
    critical_issues = Column(Integer, default=0)
    high_issues = Column(Integer, default=0)
    medium_issues = Column(Integer, default=0)
    low_issues = Column(Integer, default=0)
    
    severity_score = Column(Float, default=0.0)
    
    started_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    error_message = Column(String, nullable=True)
    
    config = Column(JSON, nullable=True)
    results = Column(JSON, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Scan {self.id} target={self.target} status={self.status}>"


class ScanResult(Base):
    """Detailed scan results."""

    __tablename__ = "scan_results"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    scan_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    
    result_type = Column(String)
    data = Column(JSON, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ScanResult {self.id} scan_id={self.scan_id}>"
