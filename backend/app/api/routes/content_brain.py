from fastapi import APIRouter

from app.schemas.content_brain_schema import (
    ContentBrainAnalysisResponse,
    ContentBrainRecommendationResponse,
    ContentBrainRequest,
    ContentBrainStoryboardResponse,
    ProductionPlanSchema,
)
from app.services import content_brain_service

router = APIRouter(prefix="/content-brain", tags=["Content Brain"])


@router.post("/analyze", response_model=ContentBrainAnalysisResponse)
def analyze_content_brain(payload: ContentBrainRequest) -> ContentBrainAnalysisResponse:
    return content_brain_service.analyze(payload)


@router.post("/recommend", response_model=ContentBrainRecommendationResponse)
def recommend_content_strategy(payload: ContentBrainRequest) -> ContentBrainRecommendationResponse:
    return content_brain_service.recommend(payload)


@router.post("/storyboard", response_model=ContentBrainStoryboardResponse)
def create_storyboard(payload: ContentBrainRequest) -> ContentBrainStoryboardResponse:
    return content_brain_service.storyboard(payload)


@router.post("/production-plan", response_model=ProductionPlanSchema)
def create_production_plan(payload: ContentBrainRequest) -> ProductionPlanSchema:
    return content_brain_service.production_plan(payload)
