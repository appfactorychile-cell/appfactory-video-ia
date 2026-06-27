from fastapi import APIRouter

from app.schemas.pipeline_schema import PipelineListResponse, PipelineRunResponse, PipelineStartRequest
from app.services import pipeline_service

router = APIRouter(prefix="/pipeline", tags=["Pipeline"])


@router.get("", response_model=PipelineListResponse)
def get_pipeline() -> PipelineListResponse:
    return pipeline_service.list_pipeline_runs()


@router.post("/start", response_model=PipelineRunResponse)
def start_pipeline(payload: PipelineStartRequest) -> PipelineRunResponse:
    return pipeline_service.start_pipeline(payload)
