from fastapi import APIRouter
from pathlib import Path

from app.motion.motion_engine import motion_plan
from app.render.ffmpeg_manager import detect_ffmpeg
from app.render.video_renderer import render_test_video

router = APIRouter(prefix="/render", tags=["Render Engine"])


@router.get("/status", summary="Render Engine Status")
def render_status() -> dict[str, object]:
    return detect_ffmpeg()


@router.post("/test-video", summary="Generate First Test MP4")
def test_video() -> dict[str, object]:
    return render_test_video()


@router.get("/motion-graphics", summary="Motion Graphics Plan")
def motion_graphics() -> dict[str, object]:
    return motion_plan()


@router.get("/generated-videos", summary="Generated Videos")
def generated_videos() -> list[dict[str, object]]:
    output_dir = Path(__file__).resolve().parents[4] / "output"
    if not output_dir.exists():
        return []
    videos: list[dict[str, object]] = []
    for path in sorted(output_dir.glob("*.mp4"), key=lambda item: item.stat().st_mtime, reverse=True):
        video_type = "Imagen a video" if path.name.startswith("image_") else "Video animado"
        stat = path.stat()
        videos.append(
            {
                "name": path.name,
                "path": str(path),
                "size_bytes": stat.st_size,
                "modified_at": stat.st_mtime,
                "type": video_type,
            }
        )
    return videos
