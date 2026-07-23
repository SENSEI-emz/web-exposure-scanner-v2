"""Logger Configuration"""

import logging
import json
from pythonjsonlogger import jsonlogger
from app.config import settings


def get_logger(name: str) -> logging.Logger:
    """Get configured logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(settings.LOG_LEVEL)

    if not logger.handlers:
        if settings.LOG_FORMAT == "json":
            handler = logging.StreamHandler()
            formatter = jsonlogger.JsonFormatter()
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        else:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)

    return logger
