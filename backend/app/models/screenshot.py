"""Screenshot Model"""

from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database import Base


class Screenshot(Base):
    """Screenshot of discovered endpoint."""

    __tablename__ = "screenshots"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    scan_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    endpoint_id = Column(UUID(as_uuid=True), nullable=True)
    
    url = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    
    width = Column(Integer)
    height = Column(Integer)
    size_bytes = Column(Integer)
    
    status_code = Column(Integer, nullable=True)
    capture_time = Column(Integer, nullable=True)
    error = Column(String, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Screenshot {self.url}>"
