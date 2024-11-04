import structlog
from django.conf import settings

def get_logger(name):
    if name is None:
        name = "subman"
    return structlog.get_logger(f"{settings.SYSTEM_NAME}.{name}")