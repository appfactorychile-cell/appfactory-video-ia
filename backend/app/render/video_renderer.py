import json
import subprocess
from pathlib import Path

from app.animation import animation_timeline, scene_composer
from app.motion.motion_engine import motion_plan, scene_motion
from app.render.ffmpeg_manager import detect_ffmpeg


PROJECT_ROOT = Path(__file__).resolve().parents[3]
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_FILE = OUTPUT_DIR / "video_0001.mp4"
TEMP_OUTPUT_FILE = OUTPUT_DIR / "video_0001.rendering.mp4"
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
    subtitle_plan = scene.get("subtitle_plan") if isinstance(scene.get("subtitle_plan"), dict) else {}
    subtitle_lines = subtitle_plan.get("lines") if isinstance(subtitle_plan.get("lines"), list) else []
    subtitle = _escape_drawtext(" / ".join(str(line) for line in subtitle_lines) or scene.get("subtitle"))
    narration = scene.get("narration") if isinstance(scene.get("narration"), dict) else {}
    voice_label = _escape_drawtext(
        f"VOZ MOCK {narration.get('start', 0)}s-{narration.get('end', 3)}s"
    )
    character = scene.get("character") if isinstance(scene.get("character"), dict) else {}
    character_name = _escape_drawtext(character.get("name") or "Narrador Hombre")
    character_pose = _escape_drawtext(character.get("pose") or "Explicando")
    character_color = str(character.get("color") or "0x38bdf8")
    color = colors[index % len(colors)]
    accent = accent_colors[index % len(accent_colors)]
    font = str(FONT_FILE).replace("\\", "/").replace(":", "\\:")
    duration = 3
    motion = scene_motion(index)
    layout = motion["layout"]["positions"]
    camera_filter = motion["camera"]["ffmpeg_filter"]
    transition = _escape_drawtext(motion["transition"]["name"])
    text_motion = _escape_drawtext(motion["animation"]["texto"])
    title_y = int(layout["title_y"])
    main_y = int(layout["main_y"])
    subtitle_y = int(layout["subtitle_y"])
    return (
        f"color=c={color}:s=720x1280:d={duration},format=yuv420p,"
        f"drawgrid=width=60:height=60:thickness=1:color=white@0.045,"
        f"drawbox=x='mod(t*155+{index * 110},820)-80':y='120+18*sin(t*2)':w=230:h=230:color={accent}@0.20:t=fill,"
        f"drawbox=x='620-mod(t*92+{index * 70},760)':y=760:w=160:h=160:color=white@0.08:t=fill,"
        f"drawbox=x=42:y=138:w=636:h=790:color=white@0.055:t=fill,"
        f"drawbox=x=62:y=156:w=596:h=752:color={accent}@0.12:t=4,"
        f"drawbox=x='70+18*sin(t*3)':y=950:w=120:h=6:color={accent}@0.82:t=fill,"
        f"drawbox=x='500+10*cos(t*4)':y=210:w=92:h=92:color=white@0.10:t=fill,"
        f"drawbox=x=600:y='580+24*sin(t*1.6)':w=38:h=38:color={accent}@0.7:t=fill,"
        f"drawbox=x='500+8*sin(t*2)':y='650+5*sin(t*3)':w=92:h=160:color={character_color}@0.92:t=fill,"
        f"drawbox=x='482+8*sin(t*2)':y='706+5*sin(t*3)':w=40:h=12:color={character_color}@0.9:t=fill,"
        f"drawbox=x='592+8*sin(t*2)':y='706+5*sin(t*3)':w=54:h=12:color={character_color}@0.9:t=fill,"
        f"drawbox=x='514+8*sin(t*2)':y='604+5*sin(t*3)':w=60:h=60:color=0xffd7b5@0.95:t=fill,"
        f"drawbox=x='530+8*sin(t*2)':y='628+5*sin(t*3)':w=8:h=8:color=0x0f172a@0.95:t=fill,"
        f"drawbox=x='556+8*sin(t*2)':y='628+5*sin(t*3)':w=8:h=8:color=0x0f172a@0.95:t=fill,"
        f"drawbox=x='532+8*sin(t*2)':y='650+5*sin(t*3)':w=28:h=5:color=0x0f172a@0.82:t=fill,"
        f"drawtext=fontfile='{font}':text='{character_name}':x=486:y=836:fontsize=20:fontcolor=ffffff@0.88,"
        f"drawtext=fontfile='{font}':text='{character_pose}':x=486:y=862:fontsize=18:fontcolor=0xbfdbfe@0.86,"
        f"drawtext=fontfile='{font}':text='APP FACTORY VIDEO IA':x=70:y=62:fontsize=30:fontcolor=0x8bd3ff,"
        f"drawtext=fontfile='{font}':text='MOTION GRAPHICS - {transition}':x=70:y=112:fontsize=25:fontcolor=ffffff@0.78,"
        f"drawtext=fontfile='{font}':text='{title}':x='70+18*max(0\\,1-t*3)':y='{title_y}-16*max(0\\,1-t*2)':fontsize=56:fontcolor=ffffff:line_spacing=10:box=1:boxcolor=black@0.10:boxborderw=12,"
        f"drawbox=x=70:y={main_y - 26}:w='560*min(1\\,t*1.2)':h=8:color={accent}@0.86:t=fill,"
        f"drawtext=fontfile='{font}':text='{main_text}':x=78:y='{main_y}+10*sin(t*2)':fontsize=39:fontcolor=e8f3ff:line_spacing=8:box=1:boxcolor=black@0.18:boxborderw=16,"
        f"drawtext=fontfile='{font}':text='{text_motion}':x=78:y={main_y + 154}:fontsize=24:fontcolor=0xbfdbfe@0.86,"
        f"drawbox=x=54:y=1046:w=612:h=128:color=black@0.52:t=fill,"
        f"drawbox=x=70:y=1020:w='560*min(1\\,t/{duration})':h=8:color=0x22c55e@0.72:t=fill,"
        f"drawtext=fontfile='{font}':text='{voice_label}':x=82:y=1015:fontsize=20:fontcolor=0xbbf7d0@0.9,"
        f"drawtext=fontfile='{font}':text='{subtitle}':x=82:y={subtitle_y}:fontsize=30:fontcolor=ffffff:line_spacing=6,"
        f"{camera_filter},setsar=1,"
        f"fade=t=in:st=0:d=0.28,fade=t=out:st=2.72:d=0.28,"
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
    if TEMP_OUTPUT_FILE.exists():
        TEMP_OUTPUT_FILE.unlink()
    ffmpeg_path = str(ffmpeg["path"])
    motion = motion_plan(len(render_scenes))
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
        str(TEMP_OUTPUT_FILE),
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

    if OUTPUT_FILE.exists():
        OUTPUT_FILE.unlink()
    TEMP_OUTPUT_FILE.replace(OUTPUT_FILE)
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
        "motion_graphics": motion,
    }
