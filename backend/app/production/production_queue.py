from app.models.production import ProductionJob


JOBS: dict[str, ProductionJob] = {}


def add_job(job: ProductionJob) -> ProductionJob:
    JOBS[job.id] = job
    return job


def list_jobs() -> list[ProductionJob]:
    return list(JOBS.values())


def get_job(job_id: str) -> ProductionJob | None:
    return JOBS.get(job_id)


def queue_status() -> dict[str, object]:
    jobs = list_jobs()
    return {
        "total": len(jobs),
        "queued": len([job for job in jobs if job.status == "En cola"]),
        "in_production": len([job for job in jobs if job.status == "En produccion"]),
        "approved": len([job for job in jobs if job.status == "Video aprobado"]),
        "rejected": len([job for job in jobs if job.status == "Rechazado"]),
        "jobs": jobs,
    }

