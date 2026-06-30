from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.audio.audio_engine import audio_job, audio_jobs, effects_library, mix_audio, music_library, plan_audio


router = APIRouter(prefix="/audio", tags=["Audio Engine"])


class AudioRequest(BaseModel):
    duration_seconds: float = 12
    scene_count: int = 4
    music_style: str = "educativa"
    effects: list[str] = Field(default_factory=lambda: ["whoosh", "pop", "transition", "soft-hit"])
    job_id: str | None = None
    audio_timeline: dict[str, object] | None = None


@router.get("/music-library", summary="Audio Music Library")
def music() -> list[dict[str, object]]:
    return music_library()


@router.get("/effects-library", summary="Audio Effects Library")
def effects() -> list[dict[str, object]]:
    return effects_library()


@router.post("/plan", summary="Plan Audio Timeline")
def plan(payload: AudioRequest) -> dict[str, object]:
    return plan_audio(payload.model_dump())


@router.post("/mix", summary="Prepare Mock Audio Mix")
def mix(payload: AudioRequest) -> dict[str, object]:
    return mix_audio(payload.model_dump())


@router.get("/jobs", summary="Audio Jobs")
def jobs() -> list[dict[str, object]]:
    return audio_jobs()


@router.get("/{job_id}", summary="Audio Job Detail")
def job(job_id: str) -> dict[str, object]:
    return audio_job(job_id)
