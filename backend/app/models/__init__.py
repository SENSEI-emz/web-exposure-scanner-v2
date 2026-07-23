"""Database Models"""

from app.models.scan import Scan, ScanResult
from app.models.endpoint import Endpoint
from app.models.vulnerability import Vulnerability
from app.models.screenshot import Screenshot

__all__ = ["Scan", "ScanResult", "Endpoint", "Vulnerability", "Screenshot"]
