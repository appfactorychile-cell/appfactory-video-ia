from fastapi import HTTPException, status

from app.models.production import ProductionJob
from app.production import hall_of_fame, production_engine, production_queue


def create_job(payload: dict[str, object]) -> ProductionJob:
    decision = str(payload.get("executive_decision", "PRODUCIR"))
    if decision != "PRODUCIR":
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="El Director Ejecutivo IA no aprobo producir esta oportunidad.")
    job = ProductionJob(
        topic=str(payload.get("topic", "Herramientas de IA para pequenas empresas")),
        niche=str(payload.get("niche", "Tecnologia")),
        language=str(payload.get("language", "Espanol")),
        country=str(payload.get("country", "Mexico")),
        approved_idea=str(payload.get("approved_idea", "Explicar una oportunidad util antes de producir")),
        executive_decision=decision,
        opportunity_score=int(payload.get("opportunity_score", 85)),
        status="En produccion",
    )
    production_engine.build_production_job(job)
    return production_queue.add_job(job)


def list_jobs() -> list[ProductionJob]:
    jobs = production_queue.list_jobs()
    if jobs:
        return jobs
    return [create_job({})]


def get_job(job_id: str) -> ProductionJob:
    job = production_queue.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Production job not found")
    return job


def approve_job(job_id: str) -> ProductionJob:
    job = get_job(job_id)
    if job.quality_report is None or not job.quality_report.approved:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Quality Control no permite aprobar este video.")
    job.status = "Video aprobado"
    return job


def reject_job(job_id: str) -> ProductionJob:
    job = get_job(job_id)
    job.status = "Rechazado"
    return job


def queue_status() -> dict[str, object]:
    if not production_queue.list_jobs():
        create_job({})
    return production_queue.queue_status()


def list_hall_of_fame() -> list[dict[str, object]]:
    return hall_of_fame.list_hall_of_fame()

