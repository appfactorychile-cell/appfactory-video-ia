from datetime import datetime

from pydantic import BaseModel, Field


class ChannelCreate(BaseModel):
    name: str = Field(..., examples=["Canal Ciencia Global"])
    target_country: str = Field(..., examples=["Chile"])
    language: str = Field(..., examples=["Spanish"])
    timezone: str = Field(..., examples=["America/Santiago"])
    niche: str = Field(..., examples=["Science"])
    visual_style: str = Field(..., examples=["Cinematic documentary"])
    ai_voice: str = Field(..., examples=["Natural narrator"])
    daily_video_count: int = Field(default=8, ge=1, le=50)
    publishing_times: list[str] = Field(default_factory=lambda: ["08:00", "13:00", "17:00", "21:00"])
    connected_platforms: list[str] = Field(default_factory=list)
    content_rules: list[str] = Field(default_factory=list)


class ChannelResponse(ChannelCreate):
    id: str
    status: str
    created_at: datetime
