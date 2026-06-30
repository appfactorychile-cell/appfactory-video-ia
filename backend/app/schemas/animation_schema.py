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


class SceneComposeRequest(BaseModel):
    scene_id: str | None = None
    title: str = Field("Hook visual")
    main_text: str = Field("Esto parece simple, pero cambia como se crea contenido.")
    subtitle: str = Field("La oportunidad aparece antes que el video.")
    duration_seconds: int = Field(10, ge=3, le=30)
    character: str = Field("Narrador 2D")
    character_id: str = Field("narrador-hombre")
    expression: str = Field("Feliz")
    character_animation: str = Field("Hablar")
    tone: str = Field("premium")


class VideoScenesComposeRequest(BaseModel):
    video_id: str | None = None
    storyboard: list[dict[str, object]] | None = None


class SceneCompositionResponse(BaseModel):
    scene_id: str
    title: str
    main_text: str
    subtitle: str
    duration_seconds: float
    narration: dict[str, object]
    subtitle_plan: dict[str, object]
    speech_track: dict[str, object]
    background: dict[str, object]
    character: dict[str, object]
    icons: list[dict[str, object]]
    layers: list[dict[str, object]]
    suggested_animation: str
    aspect_ratio: str
    status: str


class VideoScenesCompositionResponse(BaseModel):
    video_id: str
    status: str
    scene_count: int
    scenes: list[SceneCompositionResponse]
    narration_plan: dict[str, object] | None = None


class AnimationTimelineBuildRequest(BaseModel):
    timeline_id: str | None = None
    scenes: list[dict[str, object]] | None = None


class AnimationTimelineSceneResponse(BaseModel):
    scene_id: str
    title: str
    start_time: float
    end_time: float
    duration_seconds: float
    layers: list[dict[str, object]]
    keyframes: list[dict[str, object]]
    entry_animation: str
    exit_animation: str
    zoom: dict[str, object]
    pan: dict[str, object]
    transition: dict[str, object]
    subtitles: list[dict[str, object]]
    narration: dict[str, object]
    subtitle_plan: dict[str, object]
    speech_track: dict[str, object]
    camera_events: list[dict[str, object]]
    text_events: list[dict[str, object]]
    character_track: dict[str, object]


class AnimationTimelineBuildResponse(BaseModel):
    timeline_id: str
    status: str
    total_duration_seconds: float
    scene_count: int
    scenes: list[AnimationTimelineSceneResponse]
    global_transitions: list[dict[str, object]]
    preview: dict[str, object]


class AnimationTimelinePreviewResponse(BaseModel):
    timeline_id: str
    status: str
    total_duration_seconds: int
    frames: list[dict[str, object]]
