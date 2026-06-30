from fastapi import APIRouter
from pydantic import BaseModel

from app.image_video.image_video_engine import create_image_video, get_job, list_jobs, upload_image


router = APIRouter(prefix="/image-video", tags=["Image To Animated Video Engine"])


class ImageUploadRequest(BaseModel):
    filename: str
    data_url: str


class ImageVideoCreateRequest(BaseModel):
    upload_id: str | None = None
    title: str = "Una imagen puede contar una historia"
    subtitle: str = "Video vertical generado localmente."
    style: str = "Curiosidad"


@router.post("/upload", summary="Upload Image For Animated Video")
def upload(payload: ImageUploadRequest) -> dict[str, object]:
    return upload_image(payload.model_dump())


@router.post("/create", summary="Create Animated Video From Image")
def create(payload: ImageVideoCreateRequest) -> dict[str, object]:
    return create_image_video(payload.model_dump())


@router.get("/jobs", summary="Image Video Jobs")
def jobs() -> list[dict[str, object]]:
    return list_jobs()


@router.get("/{job_id}", summary="Image Video Job Detail")
def job_detail(job_id: str) -> dict[str, object]:
    return get_job(job_id)
