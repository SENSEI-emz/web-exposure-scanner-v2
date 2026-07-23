"""Application Configuration"""

from typing import List
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings from environment variables."""

    DEBUG: bool = False
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_WORKERS: int = 4

    DATABASE_URL: str = "postgresql://scanner:scanner_pass@localhost:5432/web_scanner"
    DATABASE_ECHO: bool = False
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 10

    REDIS_URL: str = "redis://localhost:6379"

    FRONTEND_URL: str = "http://localhost:3000"
    FRONTEND_API_URL: str = "http://localhost:8000"

    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]

    MAX_CONCURRENT_TASKS: int = 10
    SCAN_TIMEOUT: int = 3600
    DNS_TIMEOUT: int = 5
    HTTP_TIMEOUT: int = 10
    PORT_SCAN_TIMEOUT: int = 30

    CHROMIUM_PATH: str = "/usr/bin/chromium-browser"
    SCREENSHOT_RESOLUTION: str = "1280x720"
    SCREENSHOT_TIMEOUT: int = 10
    SCREENSHOT_DIR: str = "screenshots"

    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"

    JWT_SECRET_KEY: str = "your-super-secret-key-change-this"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


settings = get_settings()
