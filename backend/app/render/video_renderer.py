import json
import subprocess
from pathlib import Path

from app.animation import animation_timeline, scene_composer
from app.render.ffmpeg_manager import detect_ffmpeg


PROJECT_ROOT = Path(__file__).resolve().parents[3]
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_FILE = OUTPUT_DIR / "video_0001.mp4"
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
        [
            str(ffprobe),
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "json",
            str(video_path),
        ],
        capture_output=True,
        text=True,
        timeout=12,
        check=False,
    )
    if result.returncode != 0:
        return 0.0
    try:
        payload = json.loads(result.stdout)
        return round(float(payload.get("format", {}).get("duration", 0)), 2)
    except (TypeError, ValueError, json.JSONDecodeError):
        return 0.0


def _scene_filter(scene: dict[str, object], index: int) -> str:
    colors = ["0x0b1026", "0x17114a", "0x102a4c", "0x27124f"]
    accent_colors = ["0x38bdf8", "0xa855f7", "0x22c55e", "0xf59e0b"]
    title = _escape_drawtext(scene.get("title"))
    main_text = _escape_drawtext(scene.get("main_text"))
    subtitle = _escape_drawtext(scene.get("subtitle"))
    color = colors[index % len(colors)]
    accent = accent_colors[index % len(accent_colors)]
    font = str(FONT_FILE).replace("\\", "/").replace(":", "\\:")
    duration = 3
    return (
        f"color=c={color}:s=720x1280:d={duration},format=yuv420p,"
        f"drawbox=x='mod(t*110+{index * 90},760)-40':y=120:w=210:h=210:color={accent}@0.23:t=fill,"
        f"drawbox=x=70:y=150:w=580:h=760:color=white@0.07:t=fill,"
        f"drawbox=x=90:y=170:w=540:h=720:color={accent}@0.11:t=4,"
        f"drawtext=fontfile='{font}':text='APP FACTORY VIDEO IA':x=70:y=62:fontsize=30:fontcolor=0x8bd3ff,"
        f"drawtext=fontfile='{font}':text='ESCENA {index + 1:02d}':x=70:y=112:fontsize=26:fontcolor=ffffff@0.78,"
        f"drawtext=fontfile='{font}':text='{title}':x=70:y=250:fontsize=54:fontcolor=ffffff:line_spacing=10:box=1:boxcolor=black@0.10:boxborderw=12,"
        f"drawtext=fontfile='{font}':text='{main_text}':x=78:y=560:fontsize=38:fontcolor=e8f3ff:line_spacing=8:box=1:boxcolor=black@0.16:boxborderw=16,"
        f"drawbox=x=60:y=1052:w=600:h=122:color=black@0.43:t=fill,"
        f"drawtext=fontfile='{font}':text='{subtitle}':x=82:y=1082:fontsize=30:fontcolor=ffffff:line_spacing=6,"
        f"fade=t=in:st=0:d=0.35,fade=t=out:st=2.65:d=0.35,"
        f"setpts=PTS-STARTPTS[v{index}]"
    )


def render_test_video() -> dict[str, object]:
    ffmpeg = detect_ffmpeg()
    if not ffmpeg.get("available"):
        return {
            "status": "error",
            "message": "FFmpeg no encontrado",
            "path": "",
            "duration_seconds": 0,
            "size_bytes": 0,
        }

    composed = scene_composer.compose_video_scenes({"video_id": "render-test-video"})
    scenes = composed.get("scenes", []) if isinstance(composed, dict) else []
    timeline = animation_timeline.build_timeline({"timeline_id": "render-test-timeline", "scenes": scenes})
    render_scenes = [scene for scene in scenes if isinstance(scene, dict)][:4]
    if len(render_scenes) < 4:
        render_scenes = scene_composer.compose_video_scenes({}).get("scenes", [])[:4]

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ffmpeg_path = str(ffmpeg["path"])
    filter_parts = [_scene_filter(scene, index) for index, scene in enumerate(render_scenes)]
    filter_parts.append("".join(f"[v{index}]" for index in range(len(render_scenes))) + f"concat=n={len(render_scenes)}:v=1:a=0,format=yuv420p[outv]")
    command = [
        ffmpeg_path,
        "-y",
        "-filter_complex",
        ";".join(filter_parts),
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
            "scene_count": len(render_scenes),
            "timeline_id": timeline.get("timeline_id"),
        }

    duration = _probe_duration(ffmpeg_path, OUTPUT_FILE)
    return {
        "status": "rendered",
        "message": "Primer MP4 generado correctamente",
        "path": str(OUTPUT_FILE),
        "duration_seconds": duration,
        "size_bytes": OUTPUT_FILE.stat().st_size,
        "scene_count": len(render_scenes),
        "aspect_ratio": "9:16",
        "resolution": "720x1280",
        "timeline_id": timeline.get("timeline_id"),
    }
