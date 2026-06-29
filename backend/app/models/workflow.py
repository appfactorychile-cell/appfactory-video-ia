from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(slots=True)
class WorkflowChannel:
    name: str
    country: str
    language: str
    niche: str
    description: str
    daily_video_count: int
    platforms: list[str]
    mode: str


@dataclass(slots=True)
class WorkflowState:
    channel: WorkflowChannel
    id: str = field(default_factory=lambda: str(uuid4()))
    current_step: str = "channel_created"
    opportunity: dict[str, object] | None = None
    executive_audit: dict[str, object] | None = None
    ideas: list[dict[str, object]] = field(default_factory=list)
    selected_idea: dict[str, object] | None = None
    hooks: list[dict[str, object]] = field(default_factory=list)
    selected_hook: dict[str, object] | None = None
    story_strategy: dict[str, object] | None = None
    storyboard: dict[str, object] | None = None
    production_plan: dict[str, object] | None = None
    ready: bool = False
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
