def create_lip_sync_plan(
    character_id: str,
    scene_id: str,
    narration: str,
    start: float = 0.0,
    duration_seconds: float | None = None,
) -> dict[str, object]:
    word_count = max(len((narration or "").split()), 1)
    duration = round(float(duration_seconds) if duration_seconds else max(2.0, word_count * 0.34), 2)
    return {
        "inicio": start,
        "fin": round(start + duration, 2),
        "duracion": duration,
        "escena": scene_id,
        "personaje": character_id,
        "estado": "planificado_sin_voz",
        "source": "speech_timeline" if duration_seconds else "estimated_from_text",
    }
