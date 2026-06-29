from dataclasses import asdict

from fastapi import APIRouter

from app.production import production_manager
from app.schemas.production_schema import (
    HallOfFameItemSchema,
    ProductionCreateRequest,
    ProductionJobResponse,
    ProductionQueueResponse,
)

router = APIRouter(prefix="/production", tags=["AI Production Engine"])


def _job_response(job) -> dict[str, object]:
    return asdict(job)


@router.get("/jobs", response_model=list[ProductionJobResponse], summary="Production Jobs")
def list_production_jobs() -> list[dict[str, object]]:
    return [_job_response(job) for job in production_manager.list_jobs()]


@router.post("/create", response_model=ProductionJobResponse, summary="Create Production Job")
def create_production_job(payload: ProductionCreateRequest) -> dict[str, object]:
    return _job_response(production_manager.create_job(payload.model_dump()))


@router.get("/queue", response_model=ProductionQueueResponse, summary="Production Queue")
def production_queue() -> dict[str, object]:
    queue = production_manager.queue_status()
    queue["jobs"] = [_job_response(job) for job in queue["jobs"]]
    return queue


@router.get("/hall-of-fame", response_model=list[HallOfFameItemSchema], summary="Hall of Fame")
def hall_of_fame() -> list[dict[str, object]]:
    return production_manager.list_hall_of_fame()


@router.get("/{job_id}", response_model=ProductionJobResponse, summary="Production Job Detail")
def get_production_job(job_id: str) -> dict[str, object]:
    return _job_response(production_manager.get_job(job_id))


@router.post("/{job_id}/approve", response_model=ProductionJobResponse, summary="Approve Production Job")
def approve_production_job(job_id: str) -> dict[str, object]:
    return _job_response(production_manager.approve_job(job_id))


@router.post("/{job_id}/reject", response_model=ProductionJobResponse, summary="Reject Production Job")
def reject_production_job(job_id: str) -> dict[str, object]:
    return _job_response(production_manager.reject_job(job_id))

