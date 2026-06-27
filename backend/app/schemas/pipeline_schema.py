from datetime import datetime

from pydantic import BaseModel, Field


class PipelineStartRequest(BaseModel):
    topic: str
    country: str
    language: str
    niche: str


class PipelineStepSchema(BaseModel):
    name: str
    status: str
    estimated_seconds: int
    ai_owner: str


class PipelineRunResponse(BaseModel):
    id: str
    topic: str
    country: str
    language: str
    niche: str
    status: str
    steps: list[PipelineStepSchema]
    created_at: datetime


class PipelineListResponse(BaseModel):
    runs: list[PipelineRunResponse] = Field(default_factory=list)
