STYLE_PRESETS = {
    "Curiosidad": {"accent": "0x38bdf8", "title": "Dato curioso"},
    "Misterio": {"accent": "0xa855f7", "title": "Misterio visual"},
    "Educativo": {"accent": "0x22c55e", "title": "Aprendizaje rapido"},
    "Negocio": {"accent": "0xf59e0b", "title": "Idea de negocio"},
    "Historia": {"accent": "0xef4444", "title": "Historia breve"},
}


def create_motion_plan(analysis: dict[str, object], style: str) -> dict[str, object]:
    preset = STYLE_PRESETS.get(style, STYLE_PRESETS["Curiosidad"])
    orientation = str(analysis.get("orientation") or "desconocida")
    if orientation == "horizontal":
        background = "fondo blur animado con imagen expandida"
        framing = "imagen centrada con Ken Burns horizontal"
    elif orientation == "cuadrada":
        background = "fondo degradado con particulas y brillos"
        framing = "imagen cuadrada centrada con escala suave"
    else:
        background = "adaptacion vertical al frame 9:16"
        framing = "imagen principal con zoom lento"
    return {
        "style": style,
        "accent": preset["accent"],
        "layout": preset["title"],
        "background": background,
        "framing": framing,
        "duration_seconds": 12,
        "camera": ["zoom lento", "paneo sutil", "efecto Ken Burns"],
        "text": ["entrada de titulo", "subtitulo inferior", "CTA suave"],
        "particles": ["circulos", "lineas", "brillos"],
        "resolution": "720x1280",
        "aspect_ratio": "9:16",
    }

