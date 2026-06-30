from app.models.production import ProductionJob, QualityReport


def run_quality_control(job: ProductionJob) -> QualityReport:
    audio_mix = job.music.get("audio_mix") if isinstance(job.music, dict) else None
    checks = {
        "storyboard_complete": bool(job.storyboard),
        "narration_available": job.narration is not None,
        "assets_defined": bool(job.assets),
        "subtitles_prepared": job.subtitles is not None,
        "music_selected": bool(job.music),
        "effects_assigned": bool(job.effects),
        "audio_mix_valid": isinstance(audio_mix, dict) and audio_mix.get("status") == "audio_mix_ready",
        "render_ready": job.render is not None and job.render.status == "Render mock listo",
    }
    score = 94 if all(checks.values()) else 62
    approved = all(checks.values()) and score >= 85
    notes = ["Produccion mock completa y lista para aprobacion."] if approved else ["Faltan componentes antes de aprobar."]
    return QualityReport(**checks, quality_score=score, approved=approved, notes=notes)
