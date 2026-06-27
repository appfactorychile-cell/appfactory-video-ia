from fastapi import APIRouter

from app.schemas.opportunity_schema import (
    EditorialRecommendationRequest,
    EditorialRecommendationResponse,
)
from app.services import editorial_service

router = APIRouter(prefix="/editorial", tags=["Editorial"])


@router.post("/recommend", response_model=EditorialRecommendationResponse)
def recommend_content(payload: EditorialRecommendationRequest) -> EditorialRecommendationResponse:
    return editorial_service.recommend_content(payload)
