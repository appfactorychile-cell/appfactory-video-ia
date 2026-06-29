def select_character(video_type: str) -> dict[str, str]:
    if video_type == "Storytelling":
        return {"name": "Personaje principal", "role": "Vive el problema y descubre la solucion", "style": "Vector expresivo"}
    if video_type == "Business":
        return {"name": "Director ejecutivo", "role": "Explica la oportunidad con metricas", "style": "Profesional minimalista"}
    return {"name": "Narrador visual", "role": "Guia la explicacion escena por escena", "style": "Avatar 2D moderno"}
