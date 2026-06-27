from fastapi import APIRouter

from app.core.health import build_health_response

router = APIRouter(tags=["Health"])


@router.get("/health")
def health() -> dict[str, object]:
    return build_health_response()
