from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.narration.narration_engine import analyze_script, generate_narration, get_job, list_jobs, plan_narration


router = APIRouter(prefix="/narration", tags=["Narration Engine"])


class NarrationRequest(BaseModel):
    script: str = Field(
        "La inteligencia artificial no debe crear videos sin pensar. Primero analiza una oportunidad. Luego prepara escenas, voz, subtitulos y ritmo. Finalmente deja todo listo para producir un video animado claro.",
    )
    voice: str = "Narrador Local Mock"
    job_id: str | None = None


@router.post("/script", summary="Segment Narration Script")
def script(payload: NarrationRequest) -> dict[str, object]:
    return analyze_script(payload.model_dump())


@router.post("/plan", summary="Plan Narration")
def plan(payload: NarrationRequest) -> dict[str, object]:
    return plan_narration(payload.model_dump())


@router.post("/generate", summary="Generate Mock Narration")
def generate(payload: NarrationRequest) -> dict[str, object]:
    return generate_narration(payload.model_dump())


@router.get("/jobs", summary="Narration Jobs")
def jobs() -> list[dict[str, object]]:
    return list_jobs()


@router.get("/{job_id}", summary="Narration Job Detail")
def job(job_id: str) -> dict[str, object]:
    return get_job(job_id)
