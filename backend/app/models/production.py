from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(slots=True)
class Scene:
    id: str
    title: str
    visual_description: str
    duration_seconds: int
    camera_direction: str


@dataclass(slots=True)
class Asset:
    id: str
    asset_type: str
    description: str
    status: str


@dataclass(slots=True)
class Narration:
    voice: str
    tone: str
    script: str
    duration_seconds: int
    status: str = "Preparada"


@dataclass(slots=True)
class Subtitle:
    language: str
    lines: list[str]
    status: str = "Preparados"


@dataclass(slots=True)
class RenderJob:
    format: str
    resolution: str
    progress: int
    status: str


@dataclass(slots=True)
class QualityReport:
    storyboard_complete: bool
    narration_available: bool
    assets_defined: bool
    subtitles_prepared: bool
    music_selected: bool
    render_ready: bool
    quality_score: int
    approved: bool
    notes: list[str]


@dataclass(slots=True)
class ProductionJob:
    topic: str
    niche: str
    language: str
    country: str
    approved_idea: str
    executive_decision: str
    opportunity_score: int
    id: str = field(default_factory=lambda: str(uuid4()))
    status: str = "En cola"
    hook: str = ""
    script: str = ""
    storyboard: list[str] = field(default_factory=list)
    scenes: list[Scene] = field(default_factory=list)
    assets: list[Asset] = field(default_factory=list)
    narration: Narration | None = None
    subtitles: Subtitle | None = None
    music: dict[str, object] = field(default_factory=dict)
    effects: list[str] = field(default_factory=list)
    render: RenderJob | None = None
    quality_report: QualityReport | None = None
    learning_feedback: dict[str, object] = field(default_factory=dict)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

