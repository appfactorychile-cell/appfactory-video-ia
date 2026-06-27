from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(slots=True)
class OpportunityAnalysis:
    topic: str
    country: str
    language: str
    niche: str
    opportunity_score: int
    demand_level: str
    competition_level: str
    recommended_window: str
    rationale: list[str]
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
