import json
import subprocess
from pathlib import Path

from app.render.ffmpeg_manager import detect_ffmpeg


def _orientation(width: int, height: int) -> str:
    if height > width:
        return "vertical"
    if width > height:
        return "horizontal"
    return "cuadrada"


def analyze_image(path: str) -> dict[str, object]:
    image_path = Path(path)
    ffmpeg = detect_ffmpeg()
    ffprobe = Path(str(ffmpeg.get("path") or "")).with_name("ffprobe.exe")
    width = 0
    height = 0
    if ffprobe.exists():
        result = subprocess.run(
            [
                str(ffprobe),
                "-v",
                "error",
                "-select_streams",
                "v:0",
                "-show_entries",
                "stream=width,height",
                "-of",
                "json",
                str(image_path),
            ],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
        if result.returncode == 0:
            payload = json.loads(result.stdout or "{}")
            stream = (payload.get("streams") or [{}])[0]
            width = int(stream.get("width") or 0)
            height = int(stream.get("height") or 0)
    ratio = round(width / height, 4) if width and height else 0
    return {
        "width": width,
        "height": height,
        "format": image_path.suffix.replace(".", "").upper() or "UNKNOWN",
        "orientation": _orientation(width, height) if width and height else "desconocida",
        "aspect_ratio": ratio,
        "size_bytes": image_path.stat().st_size,
    }

