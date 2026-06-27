from datetime import datetime

from pydantic import BaseModel, Field


class OpportunityAnalyzeRequest(BaseModel):
    topic: str = Field(..., examples=["New battery technology"])
    country: str = Field(..., examples=["Mexico"])
    language: str = Field(..., examples=["Spanish"])
    niche: str = Field(..., examples=["Technology"])


class OpportunityResponse(BaseModel):
    id: str
    topic: str
    country: str
    language: str
    niche: str
    opportunity_score: int
    demand_level: str
    competition_level: str
    recommended_window: str
    rationale: list[str]
    created_at: datetime


class EditorialRecommendationRequest(BaseModel):
    topic: str
    country: str
    language: str
    niche: str
    opportunity_score: int = Field(default=78, ge=0, le=100)


class EditorialRecommendationResponse(BaseModel):
    topic: str
    recommendation: str
    ai_confidence_score: int
    reasons: list[str]
    risks: list[str]
    final_decision: str
