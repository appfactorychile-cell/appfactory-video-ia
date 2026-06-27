from fastapi import APIRouter

from app.schemas.content_schema import (
    ContentIdeaRequest,
    ContentIdeaResponse,
    ContentScriptRequest,
    ContentScriptResponse,
)
from app.services import content_service

router = APIRouter(prefix="/content", tags=["Content"])


@router.post("/idea", response_model=ContentIdeaResponse)
def create_content_idea(payload: ContentIdeaRequest) -> ContentIdeaResponse:
    return content_service.generate_idea(payload)


@router.post("/script", response_model=ContentScriptResponse)
def create_content_script(payload: ContentScriptRequest) -> ContentScriptResponse:
    return content_service.generate_script(payload)
