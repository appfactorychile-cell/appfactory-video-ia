from datetime import datetime, timezone

from app.core.config import get_settings


def build_health_response() -> dict[str, object]:
    settings = get_settings()
    return {
        "status": "ok",
        "service": settings.app_name,
        "version": settings.version,
        "environment": settings.environment,
        "mock_mode": settings.mock_mode,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
