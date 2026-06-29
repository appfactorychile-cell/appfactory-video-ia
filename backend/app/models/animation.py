from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class AnimationTemplate:
    slug: str
    name: str
    video_type: str
    duration_seconds: int
    scene_count: int
    transitions: list[str]
    camera_motion: str
    animations: list[str]
    seconds_per_scene: int
    narration: str
    subtitles: str


@dataclass
class AnimationAsset:
    id: str
    category: str
    name: str
    style: str
    description: str
    status: str = "Disponible"


@dataclass
class AnimationScene:
    id: str
    title: str
    start_seconds: int
    end_seconds: int
    layers: list[str]
    animations: list[str]
    narration: str
    subtitles: list[str]
    music: str


@dataclass
class AnimationTimeline:
    project_id: str
    total_duration_seconds: int
    scenes: list[AnimationScene]
    music: str
    status: str


@dataclass
class AnimationProject:
    id: str
    title: str
    video_type: str
    template: AnimationTemplate
    scenes: list[AnimationScene]
    assets: list[AnimationAsset]
    timeline: AnimationTimeline
    preview: dict[str, object]
    render_pipeline: dict[str, object]
    status: str = "Pipeline preparado"
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
