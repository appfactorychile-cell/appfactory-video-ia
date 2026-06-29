from fastapi import APIRouter

from app.render.ffmpeg_manager import detect_ffmpeg
from app.render.video_renderer import render_test_video

router = APIRouter(prefix="/render", tags=["Render Engine"])


@router.get("/status", summary="Render Engine Status")
def render_status() -> dict[str, object]:
    return detect_ffmpeg()


@router.post("/test-video", summary="Generate First Test MP4")
def test_video() -> dict[str, object]:
    return render_test_video()
