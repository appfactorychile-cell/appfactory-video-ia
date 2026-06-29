from datetime import datetime

from pydantic import BaseModel, Field


class AnimationCreateRequest(BaseModel):
    title: str = Field("Como la IA transforma una pequena empresa")
    topic: str = Field("IA para pequenas empresas")
    video_type: str = Field("Explain 2D")
    template_slug: str = Field("explain-2d")
    language: str = Field("Espanol")
    duration_seconds: int = Field(42, ge=15, le=180)


class AnimationTemplateSchema(BaseModel):
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


class AnimationAssetSchema(BaseModel):
    id: str
    category: str
    name: str
    style: str
    description: str
    status: str


class AnimationSceneSchema(BaseModel):
    id: str
    title: str
    start_seconds: int
    end_seconds: int
    layers: list[str]
    animations: list[str]
    narration: str
    subtitles: list[str]
    music: str


class AnimationTimelineSchema(BaseModel):
    project_id: str
    total_duration_seconds: int
    scenes: list[AnimationSceneSchema]
    music: str
    status: str


class AnimationProjectResponse(BaseModel):
    id: str
    title: str
    video_type: str
    template: AnimationTemplateSchema
    scenes: list[AnimationSceneSchema]
    assets: list[AnimationAssetSchema]
    timeline: AnimationTimelineSchema
    preview: dict[str, object]
    render_pipeline: dict[str, object]
    status: str
    created_at: datetime
    updated_at: datetime


class AnimationLibraryResponse(BaseModel):
    categories: dict[str, list[AnimationAssetSchema]]


class AnimationRenderPlanResponse(BaseModel):
    project_id: str
    status: str
    ffmpeg_ready: bool
    steps: list[str]
    output_format: str
    note: str
