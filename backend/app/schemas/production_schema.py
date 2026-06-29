from datetime import datetime

from pydantic import BaseModel, Field


class ProductionCreateRequest(BaseModel):
    topic: str = Field("Herramientas de IA para pequenas empresas", examples=["Herramientas de IA para pequenas empresas"])
    niche: str = Field("Tecnologia", examples=["Tecnologia"])
    language: str = Field("Espanol", examples=["Espanol"])
    country: str = Field("Mexico", examples=["Mexico"])
    approved_idea: str = Field("Explicar una oportunidad util antes de producir")
    executive_decision: str = Field("PRODUCIR", examples=["PRODUCIR"])
    opportunity_score: int = Field(85, ge=0, le=100)


class SceneSchema(BaseModel):
    id: str
    title: str
    visual_description: str
    duration_seconds: int
    camera_direction: str


class AssetSchema(BaseModel):
    id: str
    asset_type: str
    description: str
    status: str


class NarrationSchema(BaseModel):
    voice: str
    tone: str
    script: str
    duration_seconds: int
    status: str


class SubtitleSchema(BaseModel):
    language: str
    lines: list[str]
    status: str


class RenderJobSchema(BaseModel):
    format: str
    resolution: str
    progress: int
    status: str


class QualityReportSchema(BaseModel):
    storyboard_complete: bool
    narration_available: bool
    assets_defined: bool
    subtitles_prepared: bool
    music_selected: bool
    render_ready: bool
    quality_score: int
    approved: bool
    notes: list[str]


class ProductionJobResponse(BaseModel):
    id: str
    topic: str
    niche: str
    language: str
    country: str
    approved_idea: str
    executive_decision: str
    opportunity_score: int
    status: str
    hook: str
    script: str
    storyboard: list[str]
    scenes: list[SceneSchema]
    assets: list[AssetSchema]
    narration: NarrationSchema | None
    subtitles: SubtitleSchema | None
    music: dict[str, object]
    effects: list[str]
    render: RenderJobSchema | None
    quality_report: QualityReportSchema | None
    learning_feedback: dict[str, object]
    created_at: datetime
    updated_at: datetime


class ProductionQueueResponse(BaseModel):
    total: int
    queued: int
    in_production: int
    approved: int
    rejected: int
    jobs: list[ProductionJobResponse]


class HallOfFameItemSchema(BaseModel):
    topic: str
    niche: str
    language: str
    country: str
    duration_seconds: int
    hook: str
    estimated_retention: str
    roi: str
    views: int
    date: str
    success_reason: str

