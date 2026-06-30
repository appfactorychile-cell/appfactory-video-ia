MUSIC_LIBRARY: list[dict[str, object]] = [
    {
        "id": "energetica",
        "name": "Energetica",
        "mood": "Alta energia",
        "bpm": 128,
        "description": "Referencia mock para videos dinamicos tipo Reels o Shorts.",
        "copyright_safe": True,
        "real_file": False,
    },
    {
        "id": "misterio",
        "name": "Misterio",
        "mood": "Intriga suave",
        "bpm": 82,
        "description": "Referencia mock para curiosidad, suspenso moderado y descubrimiento.",
        "copyright_safe": True,
        "real_file": False,
    },
    {
        "id": "educativa",
        "name": "Educativa",
        "mood": "Clara y amable",
        "bpm": 96,
        "description": "Referencia mock para explicar ideas sin distraer de la narracion.",
        "copyright_safe": True,
        "real_file": False,
    },
    {
        "id": "corporativa",
        "name": "Corporativa",
        "mood": "Profesional",
        "bpm": 105,
        "description": "Referencia mock para negocio, tecnologia y presentaciones.",
        "copyright_safe": True,
        "real_file": False,
    },
    {
        "id": "emocional",
        "name": "Emocional",
        "mood": "Inspiradora",
        "bpm": 74,
        "description": "Referencia mock para historias humanas y cierres reflexivos.",
        "copyright_safe": True,
        "real_file": False,
    },
    {
        "id": "suspenso",
        "name": "Suspenso",
        "mood": "Tension controlada",
        "bpm": 88,
        "description": "Referencia mock para mantener atencion sin exagerar.",
        "copyright_safe": True,
        "real_file": False,
    },
    {
        "id": "tecnologia",
        "name": "Tecnologia",
        "mood": "Digital y futurista",
        "bpm": 118,
        "description": "Referencia mock para IA, software y datos.",
        "copyright_safe": True,
        "real_file": False,
    },
    {
        "id": "infantil",
        "name": "Infantil",
        "mood": "Ligera y ludica",
        "bpm": 112,
        "description": "Referencia mock para contenido educativo familiar.",
        "copyright_safe": True,
        "real_file": False,
    },
]


def list_music() -> list[dict[str, object]]:
    return MUSIC_LIBRARY


def get_music(style: str | None) -> dict[str, object]:
    normalized = (style or "educativa").lower()
    return next((track for track in MUSIC_LIBRARY if track["id"] == normalized), MUSIC_LIBRARY[2])
