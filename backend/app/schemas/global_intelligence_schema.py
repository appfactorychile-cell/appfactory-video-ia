from pydantic import BaseModel, Field


class GlobalOpportunityRequest(BaseModel):
    topic: str = Field(..., examples=["Herramientas de IA para pequenas empresas"])
    country: str = Field(..., examples=["Mexico"])
    language: str = Field(..., examples=["Espanol"])
    niche: str = Field(..., examples=["Tecnologia"])
    daily_budget_usd: float = Field(20.0, ge=0, examples=[20.0])


class BudgetCandidateSchema(BaseModel):
    title: str
    opportunity_score: int
    estimated_cost_usd: float
    expected_roi_percentage: float


class BudgetOptimizationRequest(BaseModel):
    daily_budget_usd: float = Field(20.0, ge=0, examples=[20.0])
    candidates: list[BudgetCandidateSchema] | None = None


class GlobalOpportunityResponse(BaseModel):
    topic: str
    country: str
    language: str
    niche: str
    trend_analysis: dict[str, object]
    competition_analysis: dict[str, object]
    audience_analysis: dict[str, object]
    market_analysis: dict[str, object]
    viral_analysis: dict[str, object]
    roi_dashboard: dict[str, object]
    score_breakdown: dict[str, object]
    opportunity_score: int
    risk_level: int
    recommended_country: str
    recommended_language: str
    executive_decision: dict[str, object]
    country_selection: dict[str, object]
    language_selection: dict[str, object]


class ExecutiveDashboardResponse(BaseModel):
    active_channels: int
    approved_videos: int
    rejected_videos: int
    detected_opportunities: int
    used_budget_usd: float
    ai_cost_usd: float
    estimated_roi_percentage: float
    top_country: str
    recommended_language: str
    fastest_growing_topic: str
    summary: str


class BudgetOptimizationResponse(BaseModel):
    daily_budget_usd: float
    used_budget_usd: float
    remaining_budget_usd: float
    selected_videos: list[dict[str, object]]
    rejected_videos: list[dict[str, object]]
    strategy: str

