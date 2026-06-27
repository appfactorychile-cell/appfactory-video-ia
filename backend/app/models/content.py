from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(slots=True)
class ContentIdea:
    topic: str
    country: str
    language: str
    niche: str
    title: str
    hook: str
    angle: str
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(slots=True)
class ContentScript:
    idea_title: str
    language: str
    estimated_duration_seconds: int
    script: str
    scenes: list[str]
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
