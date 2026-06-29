def log_step(job_id: str, step: str, status: str) -> dict[str, str]:
    return {"job_id": job_id, "step": step, "status": status}

