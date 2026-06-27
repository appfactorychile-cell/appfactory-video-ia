from dataclasses import asdict

from app.data.mock_store import STORE
from app.models.opportunity import OpportunityAnalysis
from app.schemas.opportunity_schema import OpportunityAnalyzeRequest, OpportunityResponse


def list_opportunities() -> list[OpportunityResponse]:
    return [OpportunityResponse(**asdict(opportunity)) for opportunity in STORE.opportunities]


def analyze_opportunity(payload: OpportunityAnalyzeRequest) -> OpportunityResponse:
    base = len(payload.topic) + len(payload.country) + len(payload.language) + len(payload.niche)
    score = 62 + (base % 31)
    opportunity = OpportunityAnalysis(
        topic=payload.topic,
        country=payload.country,
        language=payload.language,
        niche=payload.niche,
        opportunity_score=score,
        demand_level="high" if score >= 80 else "medium",
        competition_level="low" if score >= 82 else "moderate",
        recommended_window="08:00-13:00 local time" if score >= 80 else "17:00-21:00 local time",
        rationale=[
            "Simulated audience demand is strong for this niche and region.",
            "The topic can be adapted culturally without copying existing content.",
            "Estimated competition leaves room for original editorial positioning.",
        ],
    )
    STORE.opportunities.append(opportunity)
    return OpportunityResponse(**asdict(opportunity))
