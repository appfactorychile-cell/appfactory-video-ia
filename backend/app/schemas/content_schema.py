from datetime import datetime

from pydantic import BaseModel, Field


class ContentIdeaRequest(BaseModel):
    topic: str
    country: str
    language: str
    niche: str
    tone: str = Field(default="curious, useful and responsible")


class ContentIdeaResponse(BaseModel):
    id: str
    topic: str
    country: str
    language: str
    niche: str
    title: str
    hook: str
    angle: str
    created_at: datetime


class ContentScriptRequest(BaseModel):
    idea_title: str
    language: str = Field(default="Spanish")
    target_duration_seconds: int = Field(default=35, ge=20, le=45)


class ContentScriptResponse(BaseModel):
    id: str
    idea_title: str
    language: str
    estimated_duration_seconds: int
    script: str
    scenes: list[str]
    created_at: datetime
