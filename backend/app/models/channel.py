from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(slots=True)
class Channel:
    name: str
    target_country: str
    language: str
    timezone: str
    niche: str
    visual_style: str
    ai_voice: str
    daily_video_count: int
    publishing_times: list[str]
    connected_platforms: list[str]
    content_rules: list[str]
    id: str = field(default_factory=lambda: str(uuid4()))
    status: str = "active"
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
