from pydantic import BaseModel, Field


class ContentBrainRequest(BaseModel):
    topic: str = Field(..., examples=["AI tools for small businesses"])
    country: str = Field(..., examples=["Mexico"])
    language: str = Field(..., examples=["Spanish"])
    niche: str = Field(..., examples=["Technology"])


class ResearchResultSchema(BaseModel):
    topic: str
    country: str
    language: str
    niche: str
    summary: str
    key_findings: list[str]
    safe_sources_policy: str


class ContentIdeaSchema(BaseModel):
    title: str
    angle: str
    emotion: str
    value_promise: str
    target_duration_seconds: int


class RankedIdeaSchema(BaseModel):
    rank: int
    title: str
    score: int
    curiosity_score: int
    conversation_score: int
    monetization_score: int
    reason: str


class AudienceProfileSchema(BaseModel):
    country: str
    language: str
    niche: str
    target_audience: str
    motivations: list[str]
    objections: list[str]
    preferred_tone: str


class HookProposalSchema(BaseModel):
    hook: str
    score: int
    emotion: str
    expected_retention: str


class StoryStrategySchema(BaseModel):
    selected_idea: str
    emotional_goal: str
    narrative_arc: str
    tone: str
    character: str
    visual_style: str
    recommended_duration_seconds: int


class ProductionPlanSchema(BaseModel):
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


class ContentBrainAnalysisResponse(BaseModel):
    opportunity_score: int
    research_summary: ResearchResultSchema
    ideas: list[ContentIdeaSchema]
    ranking: list[RankedIdeaSchema]
    best_idea: RankedIdeaSchema
    audience_profile: AudienceProfileSchema
    hooks: list[HookProposalSchema]
    story_strategy: StoryStrategySchema
    production_plan: ProductionPlanSchema


class ContentBrainRecommendationResponse(BaseModel):
    best_idea: str
    why_this_idea_is_better: str
    target_emotion: str
    recommended_duration_seconds: int
    recommended_character: str
    recommended_visual_style: str
    recommended_tone: str
    curiosity_level: int
    conversation_potential: int
    monetization_potential: int


class StoryboardSceneSchema(BaseModel):
    scene: str
    visual: str
    narration: str
    subtitles: str


class ContentBrainStoryboardResponse(BaseModel):
    title: str
    hook: str
    scene_1: StoryboardSceneSchema
    scene_2: StoryboardSceneSchema
    scene_3: StoryboardSceneSchema
    narration: str
    subtitles: list[str]
    cta: str
    duration_seconds: int
