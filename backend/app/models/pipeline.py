from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(slots=True)
class PipelineStep:
    name: str
    status: str
    estimated_seconds: int
    ai_owner: str


@dataclass(slots=True)
class PipelineRun:
    topic: str
    country: str
    language: str
    niche: str
    steps: list[PipelineStep]
    id: str = field(default_factory=lambda: str(uuid4()))
    status: str = "simulated"
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
