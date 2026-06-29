def choose_backgrounds(video_type: str) -> list[str]:
    base = ["Fondo azul profundo", "Panel de datos luminoso", "Escenario modular"]
    if video_type in {"Infographic", "Timeline"}:
        return base + ["Mapa oscuro", "Linea temporal"]
    if video_type == "Whiteboard":
        return ["Pizarra digital limpia", "Hoja blanca animada", "Marcadores suaves"]
    return base + ["Ciudad abstracta global"]
