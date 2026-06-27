from fastapi import APIRouter

from app.schemas.opportunity_schema import OpportunityAnalyzeRequest, OpportunityResponse
from app.services import opportunity_service

router = APIRouter(prefix="/opportunities", tags=["Opportunities"])


@router.get("", response_model=list[OpportunityResponse])
def get_opportunities() -> list[OpportunityResponse]:
    return opportunity_service.list_opportunities()


@router.post("/analyze", response_model=OpportunityResponse)
def analyze_opportunity(payload: OpportunityAnalyzeRequest) -> OpportunityResponse:
    return opportunity_service.analyze_opportunity(payload)
