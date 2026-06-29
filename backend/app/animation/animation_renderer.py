from app.animation.ffmpeg_pipeline import build_ffmpeg_plan


def prepare_render(project_id: str) -> dict[str, object]:
    plan = build_ffmpeg_plan(project_id)
    plan["render_engine"] = "FFmpeg Pipeline futuro"
    plan["quality_target"] = "Animacion profesional para Shorts, Reels y TikTok"
    return plan
