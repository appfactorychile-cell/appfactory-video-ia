from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class WorkflowChannelCreate(BaseModel):
    name: str = Field(..., examples=["Futuro Latino IA"])
    country: str = Field(..., examples=["Mexico"])
    language: str = Field(..., examples=["Spanish"])
    niche: str = Field(..., examples=["Technology"])
    description: str = Field(..., examples=["Canal de videos cortos sobre tecnologia util para pymes."])
    daily_video_count: int = Field(default=8, ge=1, le=50)
    platforms: list[str] = Field(default_factory=lambda: ["YouTube Shorts", "Instagram Reels", "TikTok"])
    mode: Literal["automatic", "manual"] = "manual"


class WorkflowChannelResponse(WorkflowChannelCreate):
    pass


class WorkflowBaseResponse(BaseModel):
    workflow_id: str
    current_step: str
    progress: dict[str, bool]


class WorkflowCreateChannelResponse(WorkflowBaseResponse):
    channel: WorkflowChannelResponse
    created_at: datetime


class WorkflowStepRequest(BaseModel):
    workflow_id: str


class WorkflowChooseIdeaRequest(WorkflowStepRequest):
    idea_id: str


class WorkflowChooseHookRequest(WorkflowStepRequest):
    hook_id: str


class WorkflowOpportunityResponse(WorkflowBaseResponse):
    executive_decision: dict[str, object]
    opportunity_score: int
    competition: str
    potential: str
    trend: str
    monetization: str
    ideal_time: str
    notes: list[str]


class WorkflowIdeaSchema(BaseModel):
    id: str
    title: str
    curiosity: int
    emotion: str
    value: str
    viral_level: int
    monetization: int
    retention: int


class WorkflowIdeasResponse(WorkflowBaseResponse):
    ideas: list[WorkflowIdeaSchema]


class WorkflowSelectedIdeaResponse(WorkflowBaseResponse):
    selected_idea: WorkflowIdeaSchema
    message: str


class WorkflowHookSchema(BaseModel):
    id: str
    hook: str
    score: int
    emotion: str
    retention: str


class WorkflowHooksResponse(WorkflowBaseResponse):
    hooks: list[WorkflowHookSchema]


class WorkflowSelectedHookResponse(WorkflowBaseResponse):
    selected_hook: WorkflowHookSchema
    message: str


class WorkflowSceneSchema(BaseModel):
    scene: str
    visual: str
    narration: str
    subtitles: str


class WorkflowStoryResponse(WorkflowBaseResponse):
    objective: str
    narrator: str
    character: str
    scenario: str
    tone: str
    duration_seconds: int
    style: str
    scenes: list[WorkflowSceneSchema]
    narration: str
    subtitles: list[str]
    cta: str


class WorkflowProductionPlanResponse(WorkflowBaseResponse):
    narrator: str
    voice_type: str
    format: str
    platforms: list[str]
    music: str
    lighting: str
    camera_movement: str
    color: str
    rhythm: str
    duration_seconds: int
    language: str


class WorkflowReadyResponse(WorkflowBaseResponse):
    ready: bool
    message: str
    next_locked_steps: list[str]


class WorkflowStateResponse(WorkflowBaseResponse):
    channel: WorkflowChannelResponse
    opportunity: dict[str, object] | None = None
    executive_audit: dict[str, object] | None = None
    ideas: list[WorkflowIdeaSchema] = Field(default_factory=list)
    selected_idea: WorkflowIdeaSchema | None = None
    hooks: list[WorkflowHookSchema] = Field(default_factory=list)
    selected_hook: WorkflowHookSchema | None = None
    story_strategy: dict[str, object] | None = None
    storyboard: dict[str, object] | None = None
    production_plan: dict[str, object] | None = None
    ready: bool = False
