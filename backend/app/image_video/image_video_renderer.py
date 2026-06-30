import json
import subprocess
from pathlib import Path

from app.render.ffmpeg_manager import detect_ffmpeg


PROJECT_ROOT = Path(__file__).resolve().parents[3]
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_FILE = OUTPUT_DIR / "image_video_0001.mp4"
FONT_FILE = Path("C:/Windows/Fonts/arial.ttf")


def _escape_drawtext(value: object) -> str:
    text = str(value or "")
    return (
        text.replace("\\", "\\\\")
        .replace(":", "\\:")
        .replace("'", "\\'")
        .replace(",", "\\,")
        .replace("%", "\\%")
        .replace("\n", " ")
    )


def _probe_duration(ffmpeg_path: str, video_path: Path) -> float:
    ffprobe = Path(ffmpeg_path).with_name("ffprobe.exe")
    if not ffprobe.exists():
        return 0.0
    result = subprocess.run(
        [str(ffprobe), "-v", "error", "-show_entries", "format=duration", "-of", "json", str(video_path)],
        capture_output=True,
        text=True,
        timeout=12,
        check=False,
    )
    if result.returncode != 0:
        return 0.0
    try:
        return round(float(json.loads(result.stdout).get("format", {}).get("duration", 0)), 2)
    except (TypeError, ValueError, json.JSONDecodeError):
        return 0.0


def render_image_video(image_path: str, title: str, subtitle: str, style: str, plan: dict[str, object]) -> dict[str, object]:
    ffmpeg = detect_ffmpeg()
    if not ffmpeg.get("available"):
        return {"status": "error", "message": "FFmpeg no encontrado", "path": "", "duration_seconds": 0, "size_bytes": 0}

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ffmpeg_path = str(ffmpeg["path"])
    font = str(FONT_FILE).replace("\\", "/").replace(":", "\\:")
    safe_title = _escape_drawtext(title or "Imagen convertida en video")
    safe_subtitle = _escape_drawtext(subtitle or "Subtitulo animado generado localmente")
    safe_style = _escape_drawtext(style or "Curiosidad")
    accent = str(plan.get("accent") or "0x38bdf8")
    duration = int(plan.get("duration_seconds") or 12)
    filter_complex = (
        "[0:v]scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,"
        "boxblur=24:2,eq=brightness=-0.24:saturation=1.15,setsar=1[bg];"
        "[0:v]scale=620:840:force_original_aspect_ratio=decrease,setsar=1[fg];"
        "[bg][fg]overlay=x='(W-w)/2+18*sin(t*0.55)':y='252+20*cos(t*0.45)',"
        "drawgrid=width=64:height=64:thickness=1:color=white@0.045,"
        f"drawbox=x='mod(t*90,780)-60':y=110:w=160:h=160:color={accent}@0.22:t=fill,"
        f"drawbox=x=54:y=86:w=612:h=178:color=black@0.42:t=fill,"
        f"drawbox=x=70:y=226:w='560*min(1\\,t*0.85)':h=8:color={accent}@0.88:t=fill,"
        f"drawtext=fontfile='{font}':text='IMAGEN A VIDEO · {safe_style}':x=70:y=104:fontsize=27:fontcolor=0xbfdbfe,"
        f"drawtext=fontfile='{font}':text='{safe_title}':x='70+20*max(0\\,1-t*2)':y=148:fontsize=50:fontcolor=white:line_spacing=8,"
        f"drawbox=x=54:y=1050:w=612:h=126:color=black@0.58:t=fill,"
        f"drawtext=fontfile='{font}':text='{safe_subtitle}':x=82:y=1084:fontsize=30:fontcolor=white:line_spacing=6,"
        f"drawtext=fontfile='{font}':text='Creado con APP FACTORY VIDEO IA':x=78:y=1210:fontsize=23:fontcolor={accent}@0.95,"
        "scale=760:1352,crop=720:1280:x='20+12*sin(t*0.5)':y='36+12*cos(t*0.4)',setsar=1,"
        "fade=t=in:st=0:d=0.35,fade=t=out:st=11.55:d=0.45,format=yuv420p[outv]"
    )
    command = [
        ffmpeg_path,
        "-y",
        "-loop",
        "1",
        "-t",
        str(duration),
        "-i",
        image_path,
        "-filter_complex",
        filter_complex,
        "-map",
        "[outv]",
        "-r",
        "30",
        "-movflags",
        "+faststart",
        str(OUTPUT_FILE),
    ]
    result = subprocess.run(command, capture_output=True, text=True, timeout=45, check=False)
    if result.returncode != 0:
        return {
            "status": "error",
            "message": result.stderr[-1600:],
            "path": str(OUTPUT_FILE),
            "duration_seconds": 0,
            "size_bytes": 0,
        }
    return {
        "status": "rendered",
        "message": "Video desde imagen generado correctamente",
        "path": str(OUTPUT_FILE),
        "duration_seconds": _probe_duration(ffmpeg_path, OUTPUT_FILE),
        "size_bytes": OUTPUT_FILE.stat().st_size,
        "resolution": "720x1280",
        "aspect_ratio": "9:16",
    }

