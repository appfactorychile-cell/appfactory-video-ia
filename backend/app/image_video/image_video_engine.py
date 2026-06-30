from uuid import uuid4

from app.image_video.image_analyzer import analyze_image
from app.image_video.image_motion_planner import create_motion_plan
from app.image_video.image_upload_manager import get_upload, save_uploaded_image
from app.image_video.image_video_renderer import render_image_video


IMAGE_VIDEO_JOBS: dict[str, dict[str, object]] = {}


def upload_image(payload: dict[str, object]) -> dict[str, object]:
    upload = save_uploaded_image(payload)
    analysis = analyze_image(str(upload["path"]))
    upload["analysis"] = analysis
    return upload


def create_image_video(payload: dict[str, object]) -> dict[str, object]:
    upload = get_upload(str(payload.get("upload_id") or "") or None)
    analysis = analyze_image(str(upload["path"]))
    style = str(payload.get("style") or "Curiosidad")
    title = str(payload.get("title") or "Una imagen puede contar una historia")
    subtitle = str(payload.get("subtitle") or "Video vertical generado localmente.")
    plan = create_motion_plan(analysis, style)
    render = render_image_video(str(upload["path"]), title, subtitle, style, plan)
    job_id = str(uuid4())
    job = {
        "job_id": job_id,
        "status": render.get("status"),
        "upload": upload,
        "analysis": analysis,
        "motion_plan": plan,
        "render": render,
        "title": title,
        "subtitle": subtitle,
        "style": style,
    }
    IMAGE_VIDEO_JOBS[job_id] = job
    return job


def get_job(job_id: str) -> dict[str, object]:
    if job_id not in IMAGE_VIDEO_JOBS:
        return {"job_id": job_id, "status": "not_found", "message": "Trabajo no encontrado"}
    return IMAGE_VIDEO_JOBS[job_id]


def list_jobs() -> list[dict[str, object]]:
    return list(IMAGE_VIDEO_JOBS.values())
