def select_music(video_type: str) -> dict[str, str]:
    mood = "corporativo tecnologico" if video_type == "Business" else "moderno y claro"
    return {"track": "Musica mock sin derechos", "mood": mood, "status": "Seleccionada para preview"}
