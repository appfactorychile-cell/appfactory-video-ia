from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(slots=True)
class ResearchResult:
    topic: str
    country: str
    language: str
    niche: str
    summary: str
    key_findings: list[str]
    safe_sources_policy: str
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(slots=True)
class ContentIdea:
    title: str
    angle: str
    emotion: str
    value_promise: str
    target_duration_seconds: int


@dataclass(slots=True)
class RankedIdea:
    rank: int
    title: str
    score: int
    curiosity_score: int
    conversation_score: int
    monetization_score: int
    reason: str


@dataclass(slots=True)
class AudienceProfile:
    country: str
    language: str
    niche: str
    target_audience: str
    motivations: list[str]
    objections: list[str]
    preferred_tone: str


@dataclass(slots=True)
class HookProposal:
    hook: str
    score: int
    emotion: str
    expected_retention: str


@dataclass(slots=True)
class StoryStrategy:
    selected_idea: str
    emotional_goal: str
    narrative_arc: str
    tone: str
    character: str
    visual_style: str
    recommended_duration_seconds: int


@dataclass(slots=True)
class ProductionPlan:
    narrator: str
    visual_style: str
    camera_type: str
    lighting: str
    music: str
    transitions: str
    format: str
    platforms: list[str]
    duration_seconds: int
    language: str
